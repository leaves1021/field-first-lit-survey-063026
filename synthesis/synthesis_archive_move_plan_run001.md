# Synthesis Archive Move Plan - Run001

## Purpose

本文件是一个 user-reviewable archive move plan，用于规划哪些 tracked `synthesis/*.md` 文件可以在用户批准后移动到 Run001 archive 目录。

本计划只描述 proposed move，不执行任何 archive action。本步骤不移动、不删除、不重命名、不压缩任何文件，也不启动 Run002。

## Execution status

- archive move executed
- `24` files moved to `synthesis/archive/run001/`
- no files deleted
- local ignored files not touched

## Files to keep at synthesis/ top level

以下文件应保留在 `synthesis/` 顶层，作为当前入口、active follow-up、workflow design 或 cleanup review 文件：

| file | reason |
|---|---|
| `synthesis/run001_first_batch_completion_summary.md` | Run001 first batch 的当前完成状态入口，汇总 table updates、完成步骤和剩余 figure-level items。 |
| `synthesis/figure_evidence_followup_plan_run001.md` | 当前仍活跃的 Run001 figure-level follow-up 计划；其中 revised / methods-dependent items 还没有完成。 |
| `synthesis/project_usability_cleanup_plan.md` | 当前 usability、docs、cleanup、Run002 gating 的顶层规划入口。 |
| `synthesis/workflow_automation_plan.md` | workflow automation 和 prompt / validator design 的长期设计参考。 |
| `synthesis/local_ignored_files_inventory.md` | 当前 local ignored / generated files inventory，cleanup 前应保持可见。 |
| `synthesis/local_cleanup_action_plan.md` | 当前 local cleanup user-review plan，等待用户决定 archive / delete-after-approval actions。 |
| `synthesis/search_plan_v1.md` | field-first search framing 的早期基础计划；在 Run002 batch config 稳定前仍可作为 search-scope reference。 |
| `synthesis/prompt_templates_qc.md` | prompt templates 的 QC / cleanup reference，属于 workflow design audit，不只是 Run001 中间产物。 |
| `synthesis/synthesis_archive_move_plan_run001.md` | 本文件是当前 archive move review plan；在用户批准并执行 archive 前应留在顶层。 |

## Proposed archive destination

Proposed archive destination:

- `synthesis/archive/run001/`

该目录用于保存 Run001 audit trail 和 intermediate plan files。Archive means move for organization; it does not mean delete.

## Proposed files to archive

以下文件属于 Run001 audit trail、metadata verification trail、PDF / note / append intermediate plans，或已经被 current-state summary 覆盖的中间结果。它们有 audit value，因此 proposed action 是 archive，不是 deletion。

| source path | proposed destination path | reason for archive |
|---|---|---|
| `synthesis/candidate_append_plan_run001.md` | `synthesis/archive/run001/candidate_append_plan_run001.md` | Run001 candidate append planning 已被后续 candidate table / completion docs 覆盖，保留为 audit trail。 |
| `synthesis/candidate_metadata_enrichment_plan_confirm_first.md` | `synthesis/archive/run001/candidate_metadata_enrichment_plan_confirm_first.md` | confirm_first metadata enrichment 的中间计划，当前不再作为入口。 |
| `synthesis/candidate_metadata_enrichment_run001.md` | `synthesis/archive/run001/candidate_metadata_enrichment_run001.md` | Run001 candidate metadata enrichment planning 已完成，适合归档。 |
| `synthesis/candidate_metadata_verification_plan_verify_later.md` | `synthesis/archive/run001/candidate_metadata_verification_plan_verify_later.md` | verify_later metadata verification 的中间计划，已被结果和 table state 覆盖。 |
| `synthesis/candidate_metadata_verification_results_confirm_first.md` | `synthesis/archive/run001/candidate_metadata_verification_results_confirm_first.md` | confirm_first metadata verification results 有 audit value，但不应占用顶层入口。 |
| `synthesis/candidate_metadata_verification_results_verify_later.md` | `synthesis/archive/run001/candidate_metadata_verification_results_verify_later.md` | verify_later metadata verification results 已完成，适合归档。 |
| `synthesis/candidate_s2_retry_results_confirm_first.md` | `synthesis/archive/run001/candidate_s2_retry_results_confirm_first.md` | S2 retry result 是 metadata audit trail，后续状态已反映在 tables。 |
| `synthesis/candidate_to_confirmed_plan_run001.md` | `synthesis/archive/run001/candidate_to_confirmed_plan_run001.md` | candidate-to-confirmed triage plan 已被 first-batch completion state 覆盖。 |
| `synthesis/confirmed_append_plan_run001_first_batch.md` | `synthesis/archive/run001/confirmed_append_plan_run001_first_batch.md` | first-batch confirmed append plan 是受控写入依据，完成后保留为 audit trail。 |
| `synthesis/confirmed_status_update_plan_run001_first_batch.md` | `synthesis/archive/run001/confirmed_status_update_plan_run001_first_batch.md` | confirmed status cleanup 已执行，计划可归档但不删除。 |
| `synthesis/figure_evidence_pdf_check_plan_run001.md` | `synthesis/archive/run001/figure_evidence_pdf_check_plan_run001.md` | PDF figure-inspection plan 已产生 results 和 follow-up plan，适合归档。 |
| `synthesis/figure_evidence_pdf_check_results_run001.md` | `synthesis/archive/run001/figure_evidence_pdf_check_results_run001.md` | PDF inspection results 是重要 audit trail；active leftovers 已在 follow-up plan 中维护。 |
| `synthesis/figure_evidence_table_append_plan_run001_first_batch.md` | `synthesis/archive/run001/figure_evidence_table_append_plan_run001_first_batch.md` | figure evidence append plan 已执行，保留为 append audit trail。 |
| `synthesis/first_batch_note_qc_run001.md` | `synthesis/archive/run001/first_batch_note_qc_run001.md` | note QC 已完成，结果已反映在 notes cleanup、paper_matrix append 和 summary 中。 |
| `synthesis/first_batch_reading_note_plan_run001.md` | `synthesis/archive/run001/first_batch_reading_note_plan_run001.md` | first-batch note generation plan 已完成，适合作为 historical plan 归档。 |
| `synthesis/first_pdf_download_plan_run001.md` | `synthesis/archive/run001/first_pdf_download_plan_run001.md` | PDF acquisition plan 已被 download/extraction results 和 confirmed table state 覆盖。 |
| `synthesis/paper_matrix_append_plan_run001_first_batch.md` | `synthesis/archive/run001/paper_matrix_append_plan_run001_first_batch.md` | paper_matrix append plan 已执行，保留为 controlled append audit trail。 |
| `synthesis/pdf_download_extraction_results_run001.md` | `synthesis/archive/run001/pdf_download_extraction_results_run001.md` | PDF download / extraction results 已进入 completion summary，但仍有 audit value。 |
| `synthesis/search_run_001.md` | `synthesis/archive/run001/search_run_001.md` | Search Run001 execution plan 是 batch audit trail，不是当前 daily entry point。 |
| `synthesis/search_run_001_candidate_selection.md` | `synthesis/archive/run001/search_run_001_candidate_selection.md` | candidate selection document 已被 candidate / confirmed downstream state 覆盖。 |
| `synthesis/search_run_001_review.md` | `synthesis/archive/run001/search_run_001_review.md` | Search Run001 title-level review 是 audit trail，当前不需留在顶层。 |
| `synthesis/zotero_references_pdf_attachment_check_run001.md` | `synthesis/archive/run001/zotero_references_pdf_attachment_check_run001.md` | Zotero / PDF attachment check 属于 Run001 verification audit trail。 |
| `synthesis/zotero_references_update_plan_run001.md` | `synthesis/archive/run001/zotero_references_update_plan_run001.md` | Zotero / `references.bib` update plan 是 intermediate integration plan。 |
| `synthesis/zotero_references_update_results_run001.md` | `synthesis/archive/run001/zotero_references_update_results_run001.md` | Zotero / `references.bib` update results 可保留为 audit trail，但不需要顶层可见。 |

## Files not classified

No current `synthesis/*.md` files are left unclassified in this plan.

Classification summary after this plan is created:

- keep at `synthesis/` top level: `9`
- proposed archive to `synthesis/archive/run001/`: `24`
- not classified: `0`

## Execution boundary

Do not move anything in this step.

If the user approves later, execute a separate move action only for approved files. That later action should:

1. create `synthesis/archive/run001/` if it does not already exist;
2. move only the approved source files to their approved destination paths;
3. avoid deleting any file;
4. run validators and leakage checker afterward:
   - `.\.venv\Scripts\python.exe .\scripts\validate_tables.py`
   - `.\.venv\Scripts\python.exe .\scripts\validate_notes.py`
   - `.\.venv\Scripts\python.exe .\scripts\check_no_leaked_paths.py`

All paths in this plan are repo-relative. No local absolute paths are exposed.

## Final recommendation

ready_for_user_approval
