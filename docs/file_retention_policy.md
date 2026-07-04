# File Retention Policy

## Purpose

本文件定义 literature-review workflow 中哪些文件应被 tracked、哪些应保留为 local ignored files、哪些可以 later archive、哪些只能在 user approval 后删除。

它不是 cleanup 执行清单，也不会授权 agent 自动移动或删除文件。它的作用是让 project owner、future agents 和 collaborators 在处理 generated outputs、Run001 audit trail、PDFs、extracted text、logs 和 curated tables 时使用同一套边界。

## Core principle

- Do not delete or move files automatically.
- Always create an inventory or move/delete plan first.
- User approval is required before archive or deletion.
- Cleanup 应优先保护 reproducibility、audit trail 和 commit safety。
- 如果某个文件是否仍有用不清楚，默认归为 `keep` 或 `archive candidate`，不要直接删除。

## Tracked authoritative files

以下文件通常应保持 tracked，且不应被 cleanup 自动删除：

- `README.md`
- `AGENTS.md`
- `.gitignore`
- `.env.example`
- `requirements.txt`
- `scripts/*.py`
- `templates/prompts/*.md`
- `docs/*.md`

Curated tables 应作为 workflow 的 authoritative structured state 保留：

- `tables/candidate_papers.csv`
- `tables/confirmed_papers.csv`
- `tables/paper_matrix.csv`
- `tables/figure_evidence_table.csv`

Paper notes 应作为人工阅读和 evidence extraction 的可审查记录保留：

- `notes/*.md`

这些文件可以在用户明确要求时被编辑，但不应作为“清理 generated files”的一部分被移动或删除。

## Synthesis files

`synthesis/*.md` 同时包含 current-state docs、workflow design、batch audit trail 和 append / verification plans。它们不应被自动删除；最多在单独 move plan 和用户批准后进行 archive。

### Current-state docs

这些文件通常应留在 `synthesis/` 顶层，作为当前入口或 ongoing work reference：

- `synthesis/run001_first_batch_completion_summary.md`
- `synthesis/figure_evidence_followup_plan_run001.md`
- `synthesis/project_usability_cleanup_plan.md`
- `synthesis/workflow_automation_plan.md`
- `synthesis/search_plan_v1.md`

### Workflow / automation design docs

这些文件描述项目流程、prompt design 或自动化方向，通常应保持 tracked，并在变成稳定 docs 后考虑迁移到 `docs/`：

- `synthesis/workflow_automation_plan.md`
- `synthesis/prompt_templates_qc.md`

### Batch audit trail

这些文件记录 Run001 的 search、candidate selection、metadata verification、PDF acquisition、note QC、append planning 和 status cleanup。当前它们已移动到 `synthesis/archive/run001/`，仍有审计价值，不应删除：

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
- `synthesis/archive/run001/first_pdf_download_plan_run001.md`
- `synthesis/archive/run001/pdf_download_extraction_results_run001.md`
- `synthesis/archive/run001/first_batch_reading_note_plan_run001.md`
- `synthesis/archive/run001/first_batch_note_qc_run001.md`
- `synthesis/archive/run001/figure_evidence_pdf_check_plan_run001.md`
- `synthesis/archive/run001/figure_evidence_pdf_check_results_run001.md`
- `synthesis/archive/run001/confirmed_status_update_plan_run001_first_batch.md`

### Append / verification plans

这些文件通常是某次受控写入或核验的依据。即使对应 append 已完成，也应保留到 batch completion summary 足够稳定之后：

- `synthesis/archive/run001/paper_matrix_append_plan_run001_first_batch.md`
- `synthesis/archive/run001/figure_evidence_table_append_plan_run001_first_batch.md`
- `synthesis/archive/run001/confirmed_append_plan_run001_first_batch.md`
- `synthesis/archive/run001/zotero_references_update_plan_run001.md`
- `synthesis/archive/run001/zotero_references_update_results_run001.md`
- `synthesis/archive/run001/zotero_references_pdf_attachment_check_run001.md`

### Archive candidates

Run001 audit trail files may later be moved to:

- `synthesis/archive/run001/`

但只能在以下条件满足后执行：

- 已创建 separate synthesis archive move plan。
- move plan 明确列出每个 source path 和 destination path。
- 用户批准该 move plan。
- 移动后运行 validators 和 leakage checker。

## Ignored local files

`.gitignore` 已将多类 local / generated / sensitive 文件排除在 Git tracking 之外。这些文件可能仍然对本地复现有价值，但不应直接提交。

Ignored local files include:

- `papers/raw_pdf/*`
- `papers/extracted_text/*`
- `papers/supplementary/*`
- `data/raw/*`
- `data/processed/*`
- `logs/*`
- `tables/YYYYMMDD_search_*.csv`
- `references.bib`

GitHub cannot show ignored local files。也就是说，只看 GitHub 或 `git status` 不能判断本地是否存在 raw metadata、PDFs、extracted text、logs 或 generated search CSVs。任何 local cleanup 都应先生成 local inventory。

## Keep / archive / delete-after-approval categories

### `keep`

用于仍服务当前 workflow、Run001 follow-up 或 future audit 的文件。

Typical examples:

- curated tables
- active docs
- accepted notes
- current completion summaries
- local PDFs or extracted text still needed for reading or figure inspection

### `archive`

用于有 audit value、但不再适合作为当前入口的文件。

Typical examples:

- old Run001 intermediate plans after completion summary is stable
- historical verification plans
- batch-specific append plans that should remain reproducible but not crowd the top-level working view

Archive does not mean delete。Archive 只是把文件移动到更明确的位置，例如 `synthesis/archive/run001/`。

### `delete after user approval`

用于 duplicate、obsolete、temporary 或 failed-run generated files，并且只有在 inventory 中记录后才能删除。

Typical examples:

- failed-run outputs
- duplicated smoketest outputs
- temporary files
- obsolete local generated files that are superseded by a better documented result

即使一个文件看起来“显然没用”，agent 也不应直接删除。先写 inventory 和 reason，再等用户批准。

## Local ignored files inventory

推荐先创建一个只读 inventory，再决定是否 cleanup。Inventory 建议包含以下字段：

- `path`
- `tracked / ignored`
- `file type`
- `size`
- `modified time`
- `related batch if inferable`
- `recommended category`
- `reason`

Inventory 应覆盖：

- `papers/raw_pdf/*`
- `papers/extracted_text/*`
- `papers/supplementary/*`
- `data/raw/*`
- `data/processed/*`
- `logs/*`
- `tables/YYYYMMDD_search_*.csv`
- `references.bib` if present locally

Inventory step must be read-only。它只描述本地状态，不移动、不删除、不重命名。

## What agents must not do

- Do not delete files automatically.
- Do not move synthesis files automatically.
- Do not commit PDFs or extracted text.
- Do not expose local absolute paths.
- Do not remove audit trail files unless there is a user-approved plan.
- Do not treat `.gitignore` as permission to delete local files.
- Do not remove `references.bib` merely because it is ignored; it may be the local Zotero / Better BibTeX source.

## Recommended cleanup sequence

1. Create local ignored files inventory.
2. Create synthesis archive move plan.
3. User reviews both plans.
4. Execute approved moves/deletions only.
5. Run validators and leakage checker afterward.

Recommended validation commands after approved cleanup:

```powershell
& .\.venv\Scripts\python.exe .\scripts\validate_tables.py
& .\.venv\Scripts\python.exe .\scripts\validate_notes.py
& .\.venv\Scripts\python.exe .\scripts\check_no_leaked_paths.py
```

If any validator fails after cleanup, stop and inspect the failure before doing additional cleanup.

## Relationship to .gitignore

`.gitignore` controls what Git ignores; it does not define what should be deleted.

Files already tracked by Git are not automatically affected by later `.gitignore` rules. If a tracked file later matches an ignore pattern, Git will usually continue tracking it until it is explicitly removed from the index in a separate, user-approved step.

Therefore:

- `.gitignore` is a commit-safety boundary.
- This policy is a retention and cleanup boundary.
- Actual cleanup still requires inventory, plan, and user approval.
