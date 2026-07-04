# Current usability problem

Run001 已经证明这个项目有一条可工作的 literature workflow：从 search metadata、candidate selection、metadata verification、PDF acquisition、text extraction、paper note、note QC，到 `paper_matrix.csv` 和 `figure_evidence_table.csv` 的受控追加，都已经跑通过一次。

当前问题不是 workflow 不存在，而是它还不容易被项目 owner 或另一个新用户稳定操作：

- `README.md` 当前为空，缺少一个最小入口来说明项目目的、当前状态、核心命令和下一步应该从哪里开始。
- workflow 知识分散在许多 `synthesis/*.md` 文件中；这些文件保留了很有价值的 audit trail，但不适合作为日常操作指南。
- validators、prompt templates、curated tables 已经存在，但还没有一个 user-facing quickstart 把它们串成标准流程。
- Run001 的完成状态、剩余 figure-level 项、prompt-template 设计和自动化规划分散在不同文件里，后续继续 Run001 leftovers 或启动 Run002 时容易重复创建小计划。
- `AGENTS.md` 同时承担通用操作规则和当前研究语境说明，长期看会让 repo-level agent policy 与具体研究方向纠缠在一起。

# What is already usable

当前已经可用的部分包括：

- validators:
  - `scripts/validate_tables.py`
  - `scripts/validate_notes.py`
  - `scripts/check_no_leaked_paths.py`
- prompt templates:
  - `templates/prompts/paper_note_prompt.md`
  - `templates/prompts/note_qc_prompt.md`
  - `templates/prompts/figure_pdf_check_prompt.md`
  - `templates/prompts/paper_matrix_promotion_prompt.md`
  - `templates/prompts/figure_evidence_table_promotion_prompt.md`
- curated tables:
  - `tables/candidate_papers.csv`
  - `tables/confirmed_papers.csv`
  - `tables/paper_matrix.csv`
  - `tables/figure_evidence_table.csv`
- Run001 current-state summary:
  - `synthesis/run001_first_batch_completion_summary.md`
  - `synthesis/figure_evidence_followup_plan_run001.md`
- `AGENTS.md` 中的可复用规则：
  - language policy
  - citation and evidence rules
  - file organization
  - output conventions
  - safety and execution boundaries
  - validation command guidance

# What blocks formal semi-automated use

正式进入 semi-automated use 前，主要阻塞点是：

1. 缺少 README。
   - `README.md` 为空，外部 reviewer 或未来的自己无法快速知道项目如何运行、哪些文件是入口、哪些文件不能提交。

2. 缺少 user-facing workflow guide。
   - `synthesis/workflow_automation_plan.md` 解释了自动化方向，但不是 quickstart。
   - 需要一个更短的操作指南，说明从 candidate 到 confirmed、note、matrix、figure evidence 的标准路径。

3. 缺少 status vocabulary。
   - `candidate_metadata_verified`、`ready_for_reading`、`matrix_ready`、`hold_until_methods_checked` 等状态已经在 workflow 中使用，但缺少统一定义、允许转换和人工 gate 说明。

4. 缺少 batch config。
   - Run001 的参数、目标论文、allowed transitions 和 validator expectations 分散在计划文件中。
   - Run002 如果没有 `configs/run_template.yml` 或类似配置，很容易再次依赖手工 prompt 串联。

5. 缺少 lightweight orchestrator。
   - 当前 validators 可以独立运行，但还没有一个只读或 dry-run 的 batch summary command 来统一汇总状态。
   - 不建议马上做 full orchestrator；应先让 config、validators 和 docs 稳定。

6. cleanup / archive policy 不清楚。
   - `synthesis/` 中保留了完整 Run001 audit trail，但日常入口会被大量中间计划淹没。
   - ignored local files 例如 PDFs、extracted text、raw API outputs、logs 只存在本地，GitHub 无法显示它们，需要本地 inventory。

7. `AGENTS.md` 含有当前 research-context-specific instructions。
   - field-first axes 和 “PFC / working memory 不是默认中心” 对本项目很重要，但更像 research context。
   - 这些内容应考虑迁移到独立 context 文档，让 `AGENTS.md` 更像稳定的 repo operation policy。

# AGENTS.md cleanup plan

应保留在 `AGENTS.md` 的 generic / operational 内容：

- language policy:
  - 默认使用 Simplified Chinese。
  - 保留 filenames、commands、code identifiers、standard technical terms 的 English。
- citation and evidence rules:
  - 不 invent citations。
  - 分离 paper claims、experimental evidence、model / agent inference、user interpretation。
  - full-text / figure anchors 的要求。
- file organization:
  - `references.bib`
  - `papers/raw_pdf/`
  - `papers/extracted_text/`
  - `notes/`
  - `tables/`
  - `synthesis/`
  - `scripts/`
  - `templates/`
  - `logs/`
  - `data/raw/`
  - `data/processed/`
- output conventions:
  - Markdown notes and synthesis。
  - CSV evidence tables。
  - clear filenames。
- safety and execution:
  - 不提交 API keys。
  - 不把 PDFs / extracted full text 放进 tracked outputs。
  - 不自动 promote figure evidence。
  - 运行 validators 的默认方式。
- interaction style:
  - 报告 changed files、commands run、outputs generated、unresolved issues。

过于 specific、建议迁出的内容：

- 当前 survey 的 immediate research framing。
- field-level axes 的详细列表。
- “不要默认把 PFC / working memory / sequence tasks / subspaces / low-rank RNNs 当作项目中心”的研究语境。
- “PFC / frontal working-memory studies as possible case study”的当前方向判断。
- 当前 Run001 / Run002 的 field-first coverage 优先级。

建议迁移目标：

- 首选：`docs/research_context.md`
  - 适合作为长期、用户可读的研究背景。
- 备选：`synthesis/research_context.md`
  - 适合先作为 synthesis 层面的上下文，等 docs 稳定后再迁移。

本步骤不编辑 `AGENTS.md`。后续若执行 cleanup，可让 `AGENTS.md` 保留一句指向 context 文档的说明，例如：current research framing lives in `docs/research_context.md`。

# README and docs plan

建议 `README.md` 保持短而可执行，不替代所有深层文档。推荐结构：

1. Project purpose
   - 一段说明这是 field-first systems / computational neuroscience literature workflow。
2. Current repository state
   - Run001 first batch complete。
   - core tables 已更新。
   - remaining figure-level items tracked separately。
3. Quickstart
   - 如何运行 validators。
   - 哪些文件是当前入口。
   - 哪些目录是 local ignored outputs。
4. Core workflow
   - Search / metadata batch。
   - Confirm / PDF / extraction batch。
   - Notes batch。
   - QC batch。
   - Matrix promotion。
   - Figure evidence promotion after manual PDF inspection。
5. Key files
   - `tables/*.csv`
   - `notes/*.md`
   - `synthesis/run001_first_batch_completion_summary.md`
   - `templates/prompts/*.md`
   - `scripts/validate_*.py`
6. Safety boundaries
   - 不提交 PDFs、extracted text、API keys、Zotero local storage paths。
7. Next steps
   - 指向 Run001 follow-up 或 Run002 gating。

建议创建的 deeper docs：

- `docs/workflow_quickstart.md`
  - 面向日常操作，说明每个 batch 的最小命令、人工 gate 和输出文件。
- `docs/status_vocabulary.md`
  - 定义 `candidate_*`、confirmed paper status、promotion readiness、figure inspection status。
- `docs/file_retention_policy.md`
  - 说明 tracked vs ignored、local-only 文件、archive / delete-after-approval 规则。

README 应该只链接这些 deeper docs，不把完整 workflow 再写一遍。

# Synthesis folder cleanup plan

`synthesis/` 当前既包含 current-state docs，也包含完整 Run001 audit trail。建议先分类，再移动；本步骤不移动任何文件。

Core current-state docs：

- `synthesis/run001_first_batch_completion_summary.md`
- `synthesis/figure_evidence_followup_plan_run001.md`
- `synthesis/workflow_automation_plan.md`
- `synthesis/search_plan_v1.md`

Run001 audit trail：

- `synthesis/archive/run001/search_run_001.md`
- `synthesis/archive/run001/search_run_001_review.md`
- `synthesis/archive/run001/search_run_001_candidate_selection.md`
- `synthesis/archive/run001/candidate_append_plan_run001.md`
- `synthesis/archive/run001/candidate_metadata_enrichment_run001.md`
- `synthesis/archive/run001/candidate_metadata_enrichment_plan_confirm_first.md`
- `synthesis/archive/run001/candidate_metadata_verification_results_confirm_first.md`
- `synthesis/archive/run001/candidate_s2_retry_results_confirm_first.md`
- `synthesis/archive/run001/candidate_metadata_verification_plan_verify_later.md`
- `synthesis/archive/run001/candidate_metadata_verification_results_verify_later.md`
- `synthesis/archive/run001/candidate_to_confirmed_plan_run001.md`
- `synthesis/archive/run001/confirmed_append_plan_run001_first_batch.md`
- `synthesis/archive/run001/first_pdf_download_plan_run001.md`
- `synthesis/archive/run001/pdf_download_extraction_results_run001.md`
- `synthesis/archive/run001/first_batch_reading_note_plan_run001.md`
- `synthesis/archive/run001/first_batch_note_qc_run001.md`
- `synthesis/archive/run001/paper_matrix_append_plan_run001_first_batch.md`
- `synthesis/archive/run001/figure_evidence_pdf_check_plan_run001.md`
- `synthesis/archive/run001/figure_evidence_pdf_check_results_run001.md`
- `synthesis/archive/run001/figure_evidence_table_append_plan_run001_first_batch.md`
- `synthesis/archive/run001/confirmed_status_update_plan_run001_first_batch.md`

Prompt / workflow design docs：

- `synthesis/workflow_automation_plan.md`
- `synthesis/prompt_templates_qc.md`

Candidate files for archive：

- 已被 `run001_first_batch_completion_summary.md` 总结、且不再作为当前入口的 incremental Run001 files。
- 可考虑在用户批准后移动到：
  - `synthesis/archive/run001/`

建议 archive 原则：

- 保留 current-state docs 在 `synthesis/` 顶层。
- 将 Run001 的中间 append plans、verification plans、PDF download plans、QC results 放入 `synthesis/archive/run001/`。
- 不归档仍在使用的 follow-up plan，直到对应 leftovers 完成。
- archive 操作必须单独执行，并在移动前列出完整 move plan。

# Local ignored files inventory plan

GitHub 不能显示 ignored local files，因此不能只从 repository view 判断本地是否有 raw metadata、PDF、extracted full text 或 logs。建议后续让 Codex 生成一个只读 local inventory。

建议 inventory 覆盖：

- `tables/YYYYMMDD_search_*.csv`
- `data/raw/*`
- `data/processed/*`
- `logs/*`
- `papers/raw_pdf/*`
- `papers/extracted_text/*`

建议 inventory 输出字段：

- path
- file type
- size
- modified time
- tracked / ignored status
- related batch if inferable
- recommended category

建议分类：

- keep
  - 仍服务当前 Run001 follow-up 或 future audit 的 local outputs。
- archive
  - 有复现价值但不应留在日常工作区顶层的 generated outputs。
- delete after user approval
  - smoketest outputs、过时 logs、重复 raw downloads、确认不再需要的临时文件。

本计划不删除任何文件。任何 delete / move 都应先生成 separate inventory and cleanup plan，并获得用户批准。

# Run002 gating criteria

启动 Run002 前，建议至少完成：

- README first version
  - 让 repo 有一个稳定入口。
- status vocabulary first version
  - 让 candidate / confirmed / matrix / figure evidence 的状态转换可解释、可检查。
- batch config template
  - 例如 `configs/run_template.yml`，记录 batch id、sources、queries、target axes、allowed outputs、validator commands。
- cleanup / archive decision
  - 明确哪些 Run001 synthesis docs 留在顶层，哪些移动到 `synthesis/archive/run001/`。

Run002 的目的应明确为：

- workflow reuse test
  - 验证 Run001 形成的 validators、prompt templates、docs 是否能减少 ad hoc planning。
- expansion of under-covered field axes
  - 优先补充 Run001 未充分覆盖的 field axes，而不是重复已完成的 population dynamics / brain-wide first batch。

# Recommended execution order

1. 创建 `README.md` first version。
   - 只写项目入口、当前状态、validators、核心文件和安全边界。

2. 创建 `docs/status_vocabulary.md`。
   - 定义 candidate status、confirmed status、paper-level promotion status、figure-level inspection status。

3. 创建 `docs/workflow_quickstart.md`。
   - 把 Run001 经验压缩成可重复 batch workflow。

4. 创建 `docs/file_retention_policy.md`。
   - 明确 tracked vs ignored、local-only outputs、archive / delete-after-approval 规则。

5. 创建 local ignored files inventory plan 或 inventory report。
   - 只读列出 generated / ignored local files，不移动、不删除。

6. 拆分 `AGENTS.md` 的 research context。
   - 先创建 `docs/research_context.md` 或 `synthesis/research_context.md`。
   - 再单独计划精简 `AGENTS.md`。

7. 创建 batch config template。
   - 建议路径：`configs/run_template.yml`。
   - 先作为文档化 config，不急于接入 orchestrator。

8. 决定是否处理 Run001 held figure-level items 或启动 Run002。
   - 保守顺序是先完成 low-risk figure-level revision pass，再把 Run002 作为 workflow reuse test 启动。

# Final recommendation

ready_for_user_approval
