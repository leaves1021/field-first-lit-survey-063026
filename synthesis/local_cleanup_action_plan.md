# Local Cleanup Action Plan

## Purpose

本文件是基于 `synthesis/local_ignored_files_inventory.md` 的 proposed cleanup plan，不是 cleanup execution。

本步骤不移动、不删除、不重命名、不压缩任何文件。所有 archive 或 deletion 都必须等用户审核并明确批准后，才能在后续单独 action 中执行。

## Source inventory

Source inventory:

- `synthesis/local_ignored_files_inventory.md`

Inventory counts:

- total: `40`
- keep: `21`
- archive: `5`
- delete after user approval: `14`
- needs user decision: `0`

## Keep items

以下类别不应在本轮 cleanup 中触碰：

- Run001 raw outputs
  - 保留原因：支持 Search Run001 的 audit / reproducibility。
- Run001 per-search CSVs
  - 保留原因：支持 title-level review、candidate selection 和后续复核。
- PDFs
  - 保留原因：支持 confirmed papers、full-text reading 和 figure-level follow-up。
- extracted text
  - 保留原因：支持 notes、QC、future verification 和 figure evidence review。
- `references.bib`
  - 保留原因：虽然被 `.gitignore` 忽略，但它是本地 Zotero / Better BibTeX source，可能包含 citation verification 所需信息。
- legacy/trial PDFs and extracted text
  - 保留原因：它们仍对应 existing local notes / confirmed trial rows；是否清理应等待 separate legacy cleanup decision。

## Proposed archive items

Suggested destination:

- `logs/archive/`

Archive should not be executed until user approval.

| repo-relative path | reason | proposed destination if archived |
|---|---|---|
| `logs/20260630_extract_pdf_text.log` | extraction log has audit value but is not a current entry point | `logs/archive/20260630_extract_pdf_text.log` |
| `logs/20260701_extract_pdf_text.log` | extraction log has audit value but is not a current entry point | `logs/archive/20260701_extract_pdf_text.log` |
| `logs/20260702_extract_pdf_text.log` | Run001 extraction log supports audit trail but does not need to remain at top-level `logs/` | `logs/archive/20260702_extract_pdf_text.log` |
| `logs/semanticscholar_429_error.log` | Semantic Scholar rate-limit/error log may explain unresolved S2 checks | `logs/archive/semanticscholar_429_error.log` |
| `logs/semanticscholar_api_error.log` | Semantic Scholar API error log is relevant to Search Run001 context | `logs/archive/semanticscholar_api_error.log` |

## Proposed delete-after-approval items

These files should not be deleted in this step. They are only grouped here for user review.

### Smoketest raw outputs

| repo-relative path | reason |
|---|---|
| `data/raw/20260630_search_arxiv_low_rank_rnn_smoketest_raw.xml` | smoketest raw output; not current workflow state |
| `data/raw/20260630_search_arxiv_neuroscience_smoketest_raw.xml` | smoketest raw output; not current workflow state |
| `data/raw/20260630_search_pubmed_population_dynamics_smoketest_raw.xml` | smoketest raw output; can be removed only after user confirms it is obsolete |
| `data/raw/20260701_search_arxiv_arxiv_neural_dynamics_smoketest2_raw.xml` | second smoketest raw output; not a curated Run001 source file |
| `data/raw/20260701_search_pubmed_pubmed_population_dynamics_smoketest2_raw.xml` | second PubMed smoketest output; not needed as current state unless user wants to retain test artifacts |

### Smoketest CSVs

| repo-relative path | reason |
|---|---|
| `tables/20260630_search_arxiv_low_rank_rnn_smoketest.csv` | generated smoketest CSV; not current curated state |
| `tables/20260630_search_arxiv_neuroscience_smoketest.csv` | generated smoketest CSV; not current curated state |
| `tables/20260630_search_pubmed_population_dynamics_smoketest.csv` | generated smoketest CSV; cleanup candidate only after approval |
| `tables/20260701_search_arxiv_arxiv_neural_dynamics_smoketest2.csv` | generated second smoketest CSV; not current curated state |
| `tables/20260701_search_pubmed_pubmed_population_dynamics_smoketest2.csv` | generated second PubMed smoketest CSV; cleanup candidate only after approval |

### API-test raw outputs

| repo-relative path | reason |
|---|---|
| `data/raw/20260701_search_pubmed_api_key_pubmed_test_raw.xml` | API-key test raw output; should be deleted only after user confirms it is obsolete |
| `data/raw/20260701_search_semanticscholar_api_key_s2_test2_raw.json` | Semantic Scholar API test output; cleanup candidate after user review |

### API-test CSVs

| repo-relative path | reason |
|---|---|
| `tables/20260701_search_pubmed_api_key_pubmed_test.csv` | generated API test CSV; not current curated state |
| `tables/20260701_search_semanticscholar_api_key_s2_test2.csv` | generated Semantic Scholar API test CSV; not current curated state |

## Items explicitly not proposed for cleanup

The following categories remain `keep`:

- Run001 raw outputs
- Run001 search CSVs
- PDFs
- extracted text
- `references.bib`

These files support reproducibility, audit, note verification, or future figure-level follow-up. They should not be archived or deleted in the first cleanup action.

## Execution boundary

Do not execute archive or deletion in this step.

If the user approves, a later separate action should:

1. archive approved logs
2. delete approved smoketest/API-test outputs
3. run validators and leakage checker afterward

Use repo-relative paths only. Do not expose local absolute paths.

## Final recommendation

ready_for_user_approval
