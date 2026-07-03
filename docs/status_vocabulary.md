# Status Vocabulary

## Purpose

本文件定义本项目 semi-automated literature-review workflow 中使用的 status、readiness label 和 inspection label，目的是让用户与 agent 复用同一套词汇，而不是在不同 plan、QC 文档或 CSV 表里随意发明新标签。

这个文件优先记录已经在当前 workflow、validators、CSV 表和 Run001 文档中出现过的标签；少量尚未正式写入 CSV、但适合作为稳定保留词汇的标签，会明确标注为 `proposed` 或 `reserved`。

## Scope

本文件覆盖四类标签：

- CSV table statuses
  - 直接写入 `tables/candidate_papers.csv` 或 `tables/confirmed_papers.csv` 的 `status` 字段。
- synthesis-plan readiness labels
  - 出现在 QC、append plan、promotion plan 中，用于表达“是否接近可追加状态”。
- figure-inspection labels
  - 出现在 manual PDF inspection 结果中，用于表达 figure claim 在视觉核对后的结论。
- final human approval gates
  - 即使某条记录已经通过 validator 或获得 `ready` 标签，仍必须经过人工批准才能进入下一步。

## Candidate paper statuses

### `candidate_title_level`

- meaning:
  - 仅完成 title-level / metadata-light 初筛，尚未完成稳定标识符核验。
- where it is used:
  - `tables/candidate_papers.csv`
- allowed next statuses:
  - `candidate_metadata_verified`
  - `candidate_needs_manual_review`
  - `candidate_rejected`
  - `candidate_hold`
- whether human approval is required:
  - 从该状态进入任何 downstream table append 前，都需要人工判断。

### `candidate_metadata_verified`

- meaning:
  - title、year、venue 和至少一部分稳定标识符已经核对通过，metadata 层面可追溯。
- where it is used:
  - `tables/candidate_papers.csv`
- allowed next statuses:
  - `candidate_promoted_to_confirmed`
  - `candidate_hold`
  - `candidate_rejected`
- whether human approval is required:
  - 是。metadata verified 不等于自动进入 `confirmed_papers.csv`。

### `candidate_needs_manual_review`

- meaning:
  - metadata 或 scientific fit 存在未解决问题，需要人工复核后才能决定是否保留。
- where it is used:
  - `tables/candidate_papers.csv`
- allowed next statuses:
  - `candidate_metadata_verified`
  - `candidate_rejected`
  - `candidate_hold`
  - `candidate_promoted_to_confirmed`
- whether human approval is required:
  - 是。该状态本身就表示自动流程不足以做最终判断。

### `candidate_rejected`

- meaning:
  - 不进入当前 workflow 的后续步骤，原因通常是 drift、重复、scientific fit 不足或 metadata 无法稳定确认。
- where it is used:
  - `tables/candidate_papers.csv`
  - 当前 validator 已允许该值。
- allowed next statuses:
  - 通常无；如果需要恢复，应先在 plan 中说明原因，再人工改回 `candidate_needs_manual_review` 或 `candidate_metadata_verified`。
- whether human approval is required:
  - 写入 CSV 时应有人工批准或至少明确记录在 plan 中。

### `candidate_promoted_to_confirmed`

- meaning:
  - 该候选已被人工批准并转入 `tables/confirmed_papers.csv`。
- where it is used:
  - 这是一个 `proposed` 的 candidate-side terminal status，用于未来保持 `candidate_papers.csv` 与 `confirmed_papers.csv` 的关系可追踪。
  - 当前尚未写入现有 CSV，`scripts/validate_tables.py` 也尚未允许它。
- allowed next statuses:
  - 通常无；一旦进入该状态，后续主状态应在 `tables/confirmed_papers.csv` 中管理。
- whether human approval is required:
  - 是，必须先批准 append 到 `tables/confirmed_papers.csv`。

### `candidate_hold`

- meaning:
  - 记录暂时保留，但当前不继续推进；原因可能是 research fit 未定、依赖外部核验、或批次优先级不足。
- where it is used:
  - `tables/candidate_papers.csv`
  - 当前 validator 已允许该值。
- allowed next statuses:
  - `candidate_needs_manual_review`
  - `candidate_metadata_verified`
  - `candidate_rejected`
- whether human approval is required:
  - 是。解除 hold 不应作为静默自动动作。

## Confirmed paper statuses

下面先定义当前工作流真正需要的核心状态，再说明 validator 已保留但当前未广泛使用的辅助状态。

### `confirmed`

- meaning:
  - 该论文已进入 `tables/confirmed_papers.csv`，且 metadata 层面可接受；这是一个较宽泛的 baseline confirmed 状态。
- required evidence or artifacts:
  - 至少需要稳定 bibliographic metadata 和人工确认该论文值得进入 confirmed pool。
- allowed next statuses:
  - `ready_for_reading`
  - `hold`
  - `excluded`
- whether CSV update requires user approval:
  - 是。进入 `confirmed_papers.csv` 本身就是人工 gate。

### `ready_for_reading`

- meaning:
  - PDF 与 extracted text 已准备好，可以进入 full-text note generation / reading 阶段。
- required evidence or artifacts:
  - `pdf_path`
  - `extracted_text_path`
  - 路径应符合 validator 约定：
    - `papers/raw_pdf/`
    - `papers/extracted_text/`
- allowed next statuses:
  - `matrix_ready`
  - `hold`
  - `excluded`
- whether CSV update requires user approval:
  - 是。虽然这是流程内状态，但更新 confirmed row 仍应在受控步骤中完成。

### `matrix_ready`

- meaning:
  - full-text note 已起草并通过基本 QC，paper-level matrix row 已追加，必要时 selected figure-level evidence 也已单独记录或追踪。
- required evidence or artifacts:
  - note draft 已存在
  - `paper_matrix.csv` row 已追加
  - 若有 figure-level items，已在 append results 或 follow-up plan 中被追踪
- allowed next statuses:
  - `hold`
  - `excluded`
  - 在未来如需更细分，可转向更后续的 synthesis-facing status
- whether CSV update requires user approval:
  - 是。该状态通常意味着多个 downstream artifacts 已被人工批准。

### `hold`

- meaning:
  - confirmed paper 暂停推进，但不从表中删除。
- required evidence or artifacts:
  - 至少需要在 `notes` 或相关 plan 中说明 hold 原因。
- allowed next statuses:
  - `confirmed`
  - `ready_for_reading`
  - `matrix_ready`
  - `excluded`
- whether CSV update requires user approval:
  - 是。hold 通常反映人工优先级或质量判断。

### `excluded`

- meaning:
  - 该 confirmed row 事后被判定不应继续作为当前 survey 的 active confirmed paper。
- required evidence or artifacts:
  - 应有明确排除理由，例如 duplicate, scientific drift, wrong scope, or superseded selection。
- allowed next statuses:
  - 通常无；如需恢复，应先在 plan 中解释，再人工改回更早状态。
- whether CSV update requires user approval:
  - 是。

### `confirmed_metadata_only`

- meaning:
  - `reserved`。metadata 已经确认，但尚未进入 PDF / reading 阶段。
- required evidence or artifacts:
  - bibliographic metadata 稳定；可能尚无 PDF path / extracted text。
- allowed next statuses:
  - `ready_for_pdf_download`
  - `ready_for_reading`
  - `hold`
  - `excluded`
- whether CSV update requires user approval:
  - 是。

### `ready_for_pdf_download`

- meaning:
  - `reserved`。论文已被确认应进入 PDF 获取步骤，但 PDF 还未下载。
- required evidence or artifacts:
  - `pdf_path = not_downloaded_yet`
  - `extracted_text_path = not_extracted_yet`
  - 这是 `scripts/validate_tables.py` 已显式检查的状态。
- allowed next statuses:
  - `ready_for_reading`
  - `hold`
  - `excluded`
- whether CSV update requires user approval:
  - 是。

### `note_drafted`

- meaning:
  - `reserved`。note 已生成，但尚未完成足够 QC 或未完成 `paper_matrix.csv` promotion。
- required evidence or artifacts:
  - note draft 存在
  - QC 尚未完全完成，或 paper-level append 尚未批准
- allowed next statuses:
  - `matrix_ready`
  - `hold`
  - `excluded`
- whether CSV update requires user approval:
  - 是。

## Paper matrix promotion labels

这些标签用于 plan、QC 报告或 note review，不直接写入 `paper_matrix.csv`。

### `paper_matrix_ready`

- meaning:
  - 纸面上已经足够稳定，可直接进入 `paper_matrix.csv` append plan。
- typical use:
  - note QC
  - promotion planning
- consequence:
  - 可以生成 proposed append row，但仍需用户批准后才能真正写入 CSV。

### `paper_matrix_ready_after_minor_cleanup`

- meaning:
  - 科学内容基本够用，但 candidate row 仍需轻量清理，例如 header 对齐、字段补齐、措辞保守化。
- typical use:
  - note QC
- consequence:
  - 先修 note / candidate row，再进入 append plan。

### `not_ready_for_matrix`

- meaning:
  - `proposed` 的稳定否决标签，用于表示 paper-level candidate row 还不足以进入 append plan。
- typical use:
  - future QC / promotion plans
  - 当前 Run001 文档里更常用自然语言表达 defer/hold；此标签适合作为后续统一词汇。
- consequence:
  - 不应生成 append row。

### `hold`

- meaning:
  - paper-level promotion 暂停；通常因为 metadata、scientific fit 或 note 质量仍不稳定。
- typical use:
  - QC summary
  - promotion plan
- consequence:
  - 保留记录，但不推进 append。

## Figure evidence inspection labels

这些标签用于 manual PDF inspection 结果，描述图面核对后的直接结论。它们不自动等同于 CSV append approval。

### `confirmed`

- meaning:
  - 视觉核对支持该 figure claim 的当前版本，panel-to-claim mapping 可接受。
- next use:
  - 可能进入 `ready_for_figure_evidence_table`，但还需要 promotion planning 和用户批准。

### `revised`

- meaning:
  - 图面支持较弱版本或更窄版本的 claim；原始措辞需要降级或重写。
- next use:
  - 通常对应 `revise_before_promotion`。

### `rejected`

- meaning:
  - 图面不支持该 claim，或 claim 与 figure 不匹配。
- next use:
  - 不进入 append plan。

### `hold`

- meaning:
  - 当前 inspection 不足以做最终判断，通常需要 Methods、supplementary、caption 或更细 panel mapping 复核。
- next use:
  - 通常对应 `hold_until_methods_checked`。

## Figure evidence promotion readiness labels

这些标签用于 figure evidence append planning，表达“是否允许进入 append plan”。

### `ready_for_figure_evidence_table`

- meaning:
  - 该 figure-level claim 已经过 PDF inspection，可进入 `figure_evidence_table.csv` append plan。
- important boundary:
  - 只有这个标签可以进入 figure-evidence append plan。
  - 即使如此，真正写入 `tables/figure_evidence_table.csv` 之前仍需要用户批准。

### `revise_before_promotion`

- meaning:
  - claim 方向基本可保留，但 wording、evidence boundary 或 panel mapping 仍需修订。
- consequence:
  - 不进入当前 append plan；应先修措辞再重新评估。

### `hold_until_methods_checked`

- meaning:
  - 该 figure claim 依赖 Methods / supplementary / geometric definition / control framing 的额外核对。
- consequence:
  - 不进入当前 append plan。

### `do_not_promote`

- meaning:
  - 即使它在 note 中曾作为候选 claim 出现，也不应继续作为 figure-level evidence 推进。
- consequence:
  - 不进入 append plan，也不应在没有新证据的情况下重新包装成 ready item。

## Human gates

以下步骤始终需要人工批准：

- paper selection
- promotion to `confirmed_papers.csv`
- full-text note acceptance
- `paper_matrix.csv` append
- figure-level PDF evidence promotion
- `figure_evidence_table.csv` append
- final synthesis / research-question decisions

validator 通过、metadata 匹配、或获得 `ready` 标签，都不等于自动越过这些 gate。

## Do not invent statuses

- agents 应优先复用本文件中的词汇。
- 不要在 CSV 表里静默加入新的 `status` 值。
- 如果确实需要新 status，应先在 plan 中提出，并说明：
  - why existing labels are insufficient
  - where the new label will be used
  - whether validators need updating

## Relationship to validators

`scripts/validate_tables.py` 与 `scripts/validate_notes.py` 会检查一部分 schema 和 status consistency，例如：

- CSV header 是否匹配
- `candidate_papers.csv` / `confirmed_papers.csv` 的允许状态值
- 必填字段是否为空
- `ready_for_pdf_download` / `ready_for_reading` 的路径约束
- note 中 candidate table headers 是否匹配预期格式

但 validators 不会替代人工判断。它们不能决定：

- 某篇论文是否值得进入 confirmed pool
- 某个 note 是否已经科学上足够稳健
- 某个 figure claim 是否应被降级、搁置或拒绝
- 某个 append 是否真的应该执行

因此，本文件应与 validators 配合使用：validator 负责约束格式和已知规则，人类负责最终 scientific judgment。
