# Prompt Templates QC

## 1. Purpose

本文件用于在进一步清理 prompt templates 之前，先对当前 3 个可复用模板做一次结构化 QC。

本步骤只审查模板本身，不修改模板，不修改 notes，不修改 CSV，不修改 scripts，不修改 `references.bib`，也不生成新的 note、QC document 或 PDF-check results document。

## 2. Template inventory

本次检查的模板如下：

1. `templates/prompts/paper_note_prompt.md`
2. `templates/prompts/note_qc_prompt.md`
3. `templates/prompts/figure_pdf_check_prompt.md`

总体判断：

- 三个模板都已经具备可复用的基本骨架。
- 三个模板都把“只创建一个目标文档”“不直接写 CSV”“收尾运行 validators”写清楚了。
- 当前最明显的共性问题不是结构，而是有一条仓库级语言约定还没有显式写入模板：  
  `Use Simplified Chinese for explanations.`  
  `Keep technical filenames, field names, and standard technical terms in English.`

## 3. Placeholder completeness

### `templates/prompts/paper_note_prompt.md`

检查结果：

- 已包含 `batch_id`
- 已包含输入路径：`confirmed_papers_csv_path`、`extracted_text_path`、`pdf_path`
- 已包含输出路径：`output_note_path`
- 已包含 `special_cautions`
- 已包含可选 schema reference：`prior_note_schema_reference`

结论：

- placeholder 完整度良好。
- 对单篇 note 生成任务已经足够。

### `templates/prompts/note_qc_prompt.md`

检查结果：

- 已包含 `batch_id`
- 已包含输入路径：`note_paths`、`paper_matrix_csv_path`、`figure_evidence_table_csv_path`、`confirmed_papers_csv_path`
- 已包含输出路径：`output_qc_path`
- 已包含 `special_cautions`

结论：

- placeholder 完整度良好。
- 对 batch note QC 任务已经足够。

### `templates/prompts/figure_pdf_check_prompt.md`

检查结果：

- 已包含 `batch_id`
- 已包含输入路径：`pdf_check_plan_path`、`note_paths`、`pdf_paths`、`figure_evidence_table_csv_path`
- 已包含输出路径：`output_results_path`
- 已包含 `special_cautions`

结论：

- placeholder 完整度良好。
- 对 manual PDF figure inspection 结果记录任务已经足够。

## 4. Boundary rules

### 共同优点

三份模板都明确写出了以下边界中的大部分：

- 不修改 CSV files
- 不修改 scripts
- 不修改 `references.bib`
- 不运行 searches
- 不下载 PDFs
- 不抽取 text
- 不直接 append 到表

### 逐模板判断

#### `paper_note_prompt.md`

- 明确允许只创建一个 note。
- 明确禁止修改 CSV、scripts、`references.bib`。
- 明确禁止直接更新 `paper_matrix.csv` 与 `figure_evidence_table.csv`。
- 边界清楚，适合当前 workflow。

#### `note_qc_prompt.md`

- 明确只创建一个 QC review document。
- 明确不修改 notes、CSV、scripts、`references.bib`。
- 明确不直接推进 `paper_matrix.csv` 或 `figure_evidence_table.csv`。
- 边界清楚。

#### `figure_pdf_check_prompt.md`

- 明确只创建一个 results document。
- 明确不更新 `figure_evidence_table.csv`、`paper_matrix.csv`。
- 明确不把 extracted text 当作 visual confirmation。
- 明确后续还需要单独的 append plan。
- 边界最清楚，且最贴近 workflow_automation_plan 的人工 gate 设计。

## 5. Output structure

### `paper_note_prompt.md`

检查结果：

- 明确规定了 `validate_notes.py` 期望的全部 top-level headings。
- 明确规定了候选 `paper_matrix.csv` header。
- 明确规定了候选 `figure_evidence_table.csv` header。

结论：

- 结构约束足够强。
- 与 `scripts/validate_notes.py` 的预期一致。

### `note_qc_prompt.md`

检查结果：

- 明确规定了 QC 文档的基本 sections：
  - `# Batch scope`
  - `# Overall judgment`
  - `# Per-note QC`
  - `# Candidate table consistency`
  - `# Manual PDF inspection needs`
  - `# Final recommendation`
- 明确要求核对 candidate headers 是否精确匹配真实 CSV header。

结论：

- 结构完整，足以支撑后续 QC batch。

### `figure_pdf_check_prompt.md`

检查结果：

- 明确规定了结果文档的基本 sections：
  - `# Batch scope`
  - `# Inspection summary`
  - `# Per-figure inspection results`
  - `# Claims ready for promotion`
  - `# Claims requiring revision`
  - `# Claims rejected or held`
  - `# Final recommendation`
- 明确规定了每条 inspected figure/panel 要记录的字段。

结论：

- 输出结构清晰，适合形成后续 append-plan 的上游依据。

## 6. Evidence safety

### `paper_note_prompt.md`

检查结果：

- 已明确区分：
  - paper claim
  - extracted evidence
  - model / agent interpretation
  - user-facing survey interpretation
- 已明确 biological evidence 与 model-based evidence 分离。
- 已明确 `causal_status` 要保守。
- 已明确 manual PDF inspection boundary。

结论：

- evidence safety 表达是充分的。

### `note_qc_prompt.md`

检查结果：

- 已明确要求检查：
  - claim / evidence / interpretation separation
  - biological vs model vs methodological vs review-level evidence separation
  - conservative `causal_status`
  - explicit uncertainty

结论：

- QC 维度覆盖完整。
- 与 Run001 note QC 的人工判断方式一致。

### `figure_pdf_check_prompt.md`

检查结果：

- 已明确 extracted text 不能替代 visual confirmation。
- 已明确 panel-to-claim mapping 是 promotion 前提。
- 已明确 conceptual/schematic figure 不能混成 empirical evidence。
- 已明确 model-based evidence 与 biological evidence 分开。
- 已明确如果 PDF 与 note 冲突，应 revise 或 reject，而不是硬贴。

结论：

- 这是三份模板里 evidence boundary 最强的一份。
- 很适合作为 figure-level promotion 前的人工结果记录模板。

## 7. Validator integration

三份模板都要求在生成目标文档后运行：

- `py -3 scripts\validate_notes.py`
- `py -3 scripts\validate_tables.py`
- `py -3 scripts\check_no_leaked_paths.py`

结论：

- validator integration 已经统一。
- 这一点和 `synthesis/workflow_automation_plan.md` 的设计目标一致。

## 8. Language convention

本轮重点检查：

1. 是否显式写出：`Use Simplified Chinese for explanations.`
2. 是否显式写出：`Keep technical filenames, field names, and standard technical terms in English.`

检查结果：

### `paper_note_prompt.md`

- 当前**没有显式写出**这两条语言约定。
- 虽然模板整体已经偏中文说明 + 英文 technical terms，但规则没有明文固定。

### `note_qc_prompt.md`

- 当前**没有显式写出**这两条语言约定。
- 实际结构已经符合，但缺少显式约束。

### `figure_pdf_check_prompt.md`

- 当前**没有显式写出**这两条语言约定。
- 这是最明确的一项共性小缺口。

结论：

- 三个模板目前都可用，但语言约定仍建议显式补入。

## 9. Recommended cleanup

本步骤只给出最小修改建议，不实际修改模板。

### `templates/prompts/paper_note_prompt.md`

建议最小修改：

1. 在前部加入一句：`Use Simplified Chinese for explanations.`
2. 再加入一句：`Keep technical filenames, field names, and standard technical terms in English.`
3. 可选小修：在 validator 命令后补一句，如果 `py -3` 在当前沙箱不可用，可使用项目 `.venv` 解释器作为 fallback。

### `templates/prompts/note_qc_prompt.md`

建议最小修改：

1. 在前部加入一句：`Use Simplified Chinese for explanations.`
2. 再加入一句：`Keep technical filenames, field names, and standard technical terms in English.`
3. 可选小修：在 `Promotion Readiness Labels` 处补一句“默认优先保守分类”。

### `templates/prompts/figure_pdf_check_prompt.md`

建议最小修改：

1. 在前部加入一句：`Use Simplified Chinese for explanations.`
2. 再加入一句：`Keep technical filenames, field names, and standard technical terms in English.`
3. 可选小修：在 `Future Append Boundary` 处补一句“do not draft append rows in this step”，让边界更硬一些。

## 10. Final recommendation

当前判断：

- 这三份模板已经**可用**，并且可以继续支持后续 Run001 / Run002 风格的半自动 workflow。
- 在进入下一批模板之前，建议先做一次**很小的模板清理**，优先补齐语言约定这一个共性缺口。
- 不需要大改，不需要重写结构，也不需要改变 validator integration。

建议顺序：

1. 先修改这三份模板，补入统一语言约定与一个轻量 fallback 说明。
2. 然后继续创建后续模板，例如 `paper_matrix_promotion_prompt.md` 或 `figure_evidence_table_append_plan` 相关模板。
3. 在没有修改之前，当前模板也可以继续使用，但应带着一个小心点：  
   使用时最好在调用处手动提醒“解释用中文、technical filenames/fields 用 English”。
