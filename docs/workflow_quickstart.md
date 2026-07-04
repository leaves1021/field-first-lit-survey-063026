# Workflow Quickstart

## Who this guide is for

本指南面向两类使用者：

- project owner
  - 需要快速判断当前 batch 该从哪里开始、在哪些节点必须人工批准、哪些文件是 authoritative outputs。
- future agents / collaborators
  - 需要在不发明新流程、不越过人工 gate 的前提下，沿用当前 semi-automated workflow 完成批次工作。

## Before you start

开始任何 batch 之前，先确认以下几点：

- 优先使用项目本地 `.venv`，不要默认依赖全局 `python` 或 `py` launcher。
- 先运行 validators，再决定是否继续做 batch 操作。
- 如果 `py -3` 在当前 Windows sandbox context 中报 known login-session / launcher error，不要把它误判为脚本本身出错；直接切回项目 `.venv`。

推荐命令：

```powershell
& .\.venv\Scripts\python.exe .\scripts\validate_tables.py
& .\.venv\Scripts\python.exe .\scripts\validate_notes.py
& .\.venv\Scripts\python.exe .\scripts\check_no_leaked_paths.py
```

如果这三条命令里有任何一条失败，先停下来处理 validator failure，再继续后续 batch。

## Standard batch workflow

### Stage 1: Search / metadata batch

- purpose:
  - 运行 search scripts，保存 raw metadata 和 per-search CSV，为后续 title-level review 做输入。
- main input files:
  - `scripts/search_pubmed.py`
  - `scripts/search_semantic_scholar.py`
  - `scripts/search_arxiv.py`
  - approved search scope or batch plan
- main output files:
  - `data/raw/YYYYMMDD_search_<source>_<topic>_raw.*`
  - `tables/YYYYMMDD_search_<source>_<topic>.csv`
  - search review / run record under `synthesis/`
- relevant prompt template if any:
  - 当前没有 search-stage 专用 template；应先用 batch plan 或 search plan 明确 scope。
- required human gate:
  - 确认 search scope、query strategy 和是否真的执行搜索。
- validators to run after the stage:
  - `validate_tables.py`
  - `check_no_leaked_paths.py`
- common failure modes:
  - query drift
  - raw output 保存路径不一致
  - 误以为 per-search CSV 会自动追加到 curated tables
  - 将 search result 当作 confirmed evidence

### Stage 2: Candidate selection

- purpose:
  - 从 per-search CSV 或 title-level review 中选择候选论文，并写入或规划写入 `tables/candidate_papers.csv`。
- main input files:
  - per-search CSV under `tables/`
  - search review under `synthesis/`
  - `tables/candidate_papers.csv`
- main output files:
  - candidate selection / append plan under `synthesis/`
  - after approval, updated `tables/candidate_papers.csv`
- relevant prompt template if any:
  - 当前还没有单独的 candidate selection template；应使用 plan-first pattern。
- required human gate:
  - paper selection
  - candidate append approval
- validators to run after the stage:
  - `validate_tables.py`
  - `check_no_leaked_paths.py`
- common failure modes:
  - title-level relevance判断过强
  - duplicate DOI / PMID / S2 ID
  - 将 `proposed` status 直接写入 CSV
  - 未记录 drift / exclusion reason

### Stage 3: Confirmed papers

- purpose:
  - 对候选论文做 metadata verification，并在用户批准后把选中的论文写入 `tables/confirmed_papers.csv`。
- main input files:
  - `tables/candidate_papers.csv`
  - metadata verification plans / results under `synthesis/`
  - `tables/confirmed_papers.csv`
- main output files:
  - confirmed append plan under `synthesis/`
  - after approval, updated `tables/confirmed_papers.csv`
- relevant prompt template if any:
  - 当前没有单独的 confirmed append template；仍应先写 plan，再执行 append。
- required human gate:
  - promotion to `confirmed_papers.csv`
- validators to run after the stage:
  - `validate_tables.py`
  - `check_no_leaked_paths.py`
- common failure modes:
  - `candidate_metadata_verified` 被误当成自动 confirmed
  - 使用 validator 尚未允许的 status
  - `pdf_path` / `extracted_text_path` 占位值与 status 不一致

### Stage 4: PDF / extraction

- purpose:
  - 为 confirmed papers 准备本地 PDF 和 extracted text，供 full-text reading 使用。
- main input files:
  - `tables/confirmed_papers.csv`
  - official PDF source information
  - `scripts/extract_pdf_text.py`
- main output files:
  - `papers/raw_pdf/<citekey>.pdf`
  - `papers/extracted_text/<citekey>.md`
  - PDF / extraction results summary under `synthesis/`
- relevant prompt template if any:
  - 当前没有专用模板；这一步更像受控执行步骤。
- required human gate:
  - 是否下载 PDF
  - 是否接受下载来源
- validators to run after the stage:
  - `validate_tables.py`
  - `check_no_leaked_paths.py`
- common failure modes:
  - 使用非官方镜像
  - 路径不符合 repo-relative 约定
  - 把 extracted full text 当作可提交文件

### Stage 5: Note generation

- purpose:
  - 基于 confirmed row 和 extracted text 生成单篇 full-text note。
- main input files:
  - `tables/confirmed_papers.csv`
  - `papers/extracted_text/<citekey>.md`
- main output files:
  - `notes/<citekey>.md`
- relevant prompt template if any:
  - `templates/prompts/paper_note_prompt.md`
- required human gate:
  - note acceptance 之前不得把 note 当作稳定 evidence source
- validators to run after the stage:
  - `validate_notes.py`
  - `validate_tables.py`
  - `check_no_leaked_paths.py`
- common failure modes:
  - 缺少 required headings
  - candidate table header 漂移
  - figure-level claim 从 abstract 或 extracted-text-only 推断过强

### Stage 6: Note QC

- purpose:
  - 检查 notes 的 schema、evidence boundary、candidate row header 和 promotion readiness。
- main input files:
  - `notes/*.md`
  - `tables/paper_matrix.csv`
  - `tables/figure_evidence_table.csv`
  - `tables/confirmed_papers.csv`
- main output files:
  - QC document under `synthesis/`
- relevant prompt template if any:
  - `templates/prompts/note_qc_prompt.md`
- required human gate:
  - 是否接受 note 进入 promotion planning
- validators to run after the stage:
  - `validate_notes.py`
  - `validate_tables.py`
  - `check_no_leaked_paths.py`
- common failure modes:
  - note 结构完整但 scientific wording 仍不保守
  - `paper_matrix_ready_after_minor_cleanup` 被误当成直接可 append
  - PDF inspection 需求未单独列出

### Stage 7: `paper_matrix.csv` promotion

- purpose:
  - 将已通过 QC 的 paper-level candidate rows 转成 append plan，并在批准后追加到 `tables/paper_matrix.csv`。
- main input files:
  - validated notes
  - note QC document
  - `tables/paper_matrix.csv`
  - `tables/confirmed_papers.csv`
- main output files:
  - `paper_matrix.csv` append plan under `synthesis/`
  - after approval, updated `tables/paper_matrix.csv`
- relevant prompt template if any:
  - `templates/prompts/paper_matrix_promotion_prompt.md`
- required human gate:
  - `paper_matrix.csv` append approval
- validators to run after the stage:
  - `validate_tables.py`
  - `validate_notes.py`
  - `check_no_leaked_paths.py`
- common failure modes:
  - 直接从 note 复制 row 而不做 duplicate / conflict check
  - 把 figure-level evidence 混进 paper-level row
  - 用 unresolved figure issue 支撑核心 paper claim

### Stage 8: Figure-level PDF inspection

- purpose:
  - 对 note 中的候选 figure claims 做 manual PDF inspection，确认 panel-to-claim mapping 和 evidence boundary。
- main input files:
  - notes
  - PDFs under `papers/raw_pdf/`
  - figure PDF-check plan under `synthesis/`
- main output files:
  - figure PDF-check results under `synthesis/`
- relevant prompt template if any:
  - `templates/prompts/figure_pdf_check_prompt.md`
- required human gate:
  - figure-level visual judgment 必须是人工完成
- validators to run after the stage:
  - `validate_notes.py`
  - `validate_tables.py`
  - `check_no_leaked_paths.py`
- common failure modes:
  - 把 extracted text 当作 visual confirmation
  - panel mapping 不稳时仍强行写 `confirmed`
  - 未区分 `revised` 和 `hold`

### Stage 9: `figure_evidence_table.csv` promotion

- purpose:
  - 只把经过 inspection 且被标为 `ready_for_figure_evidence_table` 的 rows 转成 append plan，并在批准后追加。
- main input files:
  - figure PDF-check results
  - supporting notes
  - `tables/figure_evidence_table.csv`
- main output files:
  - figure-evidence append plan under `synthesis/`
  - after approval, updated `tables/figure_evidence_table.csv`
- relevant prompt template if any:
  - `templates/prompts/figure_evidence_table_promotion_prompt.md`
- required human gate:
  - `figure_evidence_table.csv` append approval
- validators to run after the stage:
  - `validate_tables.py`
  - `validate_notes.py`
  - `check_no_leaked_paths.py`
- common failure modes:
  - 将 `revise_before_promotion` 或 `hold_until_methods_checked` 误写进 append plan
  - `figure_or_table` / `causal_status` 字段不保守
  - duplicate `paper + citekey + figure_or_table`

### Stage 10: Status cleanup and completion summary

- purpose:
  - 在 append 成功后同步 `confirmed_papers.csv` 状态，并生成批次 completion summary。
- main input files:
  - `tables/confirmed_papers.csv`
  - `tables/paper_matrix.csv`
  - `tables/figure_evidence_table.csv`
  - append plans / results under `synthesis/`
- main output files:
  - updated `tables/confirmed_papers.csv`
  - completion summary under `synthesis/`
- relevant prompt template if any:
  - 当前没有专用模板；通常使用 summary / status-update plan。
- required human gate:
  - status cleanup approval
  - completion summary framing approval if it affects broader synthesis direction
- validators to run after the stage:
  - `validate_tables.py`
  - `validate_notes.py`
  - `check_no_leaked_paths.py`
- common failure modes:
  - `confirmed_papers.csv` status 与真实 downstream completion 不同步
  - completion summary 写成 batch-specific internals dump，而不是稳定记录
  - 在 append 失败前提前更新状态

## Status rules during workflow

- authoritative status definitions 以 `docs/status_vocabulary.md` 为准。
- `proposed` 或 `reserved` labels 可以在文档里描述，但除非 `scripts/validate_tables.py` 已允许，否则不要写入 CSV `status` 字段。
- readiness labels 例如 `paper_matrix_ready_after_minor_cleanup`、`ready_for_figure_evidence_table`、`hold_until_methods_checked` 只表示 planning / QC 状态，不会绕过 user approval。

## Safe append pattern

所有 CSV append 都应遵循同一模式：

1. 先创建 append plan。
2. 用户审核 append plan。
3. 只追加已批准的 rows。
4. 追加后立刻运行 validators。
5. 只有在 append 成功且 validators 通过后，才更新 status 或 completion summary。

如果其中任一步失败，就不要跳到后面的状态清理或总结步骤。

## What agents must not do automatically

- 不要自动做 paper selection。
- 不要自动 append 到 `confirmed_papers.csv`。
- 不要自动 append 到 `paper_matrix.csv`。
- 不要自动 append 到 `figure_evidence_table.csv`。
- 不要自动删除或移动 local generated files。
- 不要自动启动 Run002。

## Run001 as example

Run001 可以作为一条已跑通的 example batch，但这份 quickstart 不重复其 row counts 或长篇细节。当前可参考：

- `synthesis/run001_first_batch_completion_summary.md`
- `synthesis/figure_evidence_followup_plan_run001.md`

## When to stop and ask the user

以下情况应暂停自动推进并询问用户：

- 需要新 status
- validator fails
- PDF figure evidence ambiguous
- local ignored files 可能要被 delete 或 archive
- 某个 CSV append 已经被提出
- 需要做 research framing 或 synthesis decision

## Minimal next action for a new batch

对于新的 batch，不要直接开始搜索或 append。最小安全动作是先创建或获得批准：

- batch config
  - 例如未来的 `configs/run_template.yml`
- 或一个明确的 batch plan
  - 说明 scope、sources、target outputs、status boundary 和 human gates

在这些前置条件明确之前，不应在本指南的执行层面直接启动 Run002。
