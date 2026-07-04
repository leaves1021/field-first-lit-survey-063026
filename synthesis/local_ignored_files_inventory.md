# Local Ignored Files Inventory

## Purpose

本文件是 local ignored / generated files 的只读 inventory，用于记录 GitHub 无法显示但本地存在的文件。它只列出 metadata，不移动、不删除、不重命名、不压缩，也不读取或复制 PDF / extracted text 的正文内容。

本 inventory 的清理原则来自 `docs/file_retention_policy.md`：先 inventory，再由用户审核；任何 archive 或 delete 都需要单独 plan 和 user approval。

## Inventory scope

本次盘点覆盖以下路径和 pattern：

- `papers/raw_pdf/*`
- `papers/extracted_text/*`
- `papers/supplementary/*`
- `data/raw/*`
- `data/processed/*`
- `logs/*`
- `tables/YYYYMMDD_search_*.csv`
- `tables/YYYYMMDD_search_*_raw.*`
- `references.bib`
- optional local scratch folders if present:
  - `scratch/`
  - `tmp/`
  - `temp/`

Tracked `.gitkeep` placeholder files 不列入 inventory table，因为它们不是 GitHub 看不到的 ignored/generated outputs。

## Summary counts

- inventoried ignored / generated files: `40`
- `keep`: `21`
- `archive`: `5`
- `delete after user approval`: `14`
- `needs user decision`: `0`

## Inventory table

| path | tracked / ignored | file type | size | modified time | related batch | recommended category | reason |
|---|---|---|---:|---|---|---|---|
| `data/raw/20260630_search_arxiv_low_rank_rnn_smoketest_raw.xml` | untracked / ignored | xml | 6035 | 2026-06-30 18:38:35 | smoketest | delete after user approval | smoketest raw output; safe only for later deletion after user confirms it is no longer needed. |
| `data/raw/20260630_search_arxiv_neuroscience_smoketest_raw.xml` | untracked / ignored | xml | 7320 | 2026-06-30 18:37:56 | smoketest | delete after user approval | smoketest raw output; not current workflow state. |
| `data/raw/20260630_search_pubmed_population_dynamics_smoketest_raw.xml` | untracked / ignored | xml | 79300 | 2026-06-30 18:32:36 | smoketest | delete after user approval | smoketest raw output; can be considered for cleanup only after approval. |
| `data/raw/20260701_search_arxiv_arxiv_neural_dynamics_smoketest2_raw.xml` | untracked / ignored | xml | 6918 | 2026-07-01 00:15:11 | smoketest | delete after user approval | second smoketest raw output; not a curated Run001 source file. |
| `data/raw/20260701_search_arxiv_pop_dynamics_raw.xml` | untracked / ignored | xml | 50760 | 2026-07-01 15:16:32 | Run001 | keep | raw output for Run001 `arxiv_pop_dynamics`; needed for audit/reproducibility. |
| `data/raw/20260701_search_pubmed_api_key_pubmed_test_raw.xml` | untracked / ignored | xml | 115749 | 2026-07-01 14:19:12 | API test | delete after user approval | API-key test raw output; should only be deleted after user confirms it is obsolete. |
| `data/raw/20260701_search_pubmed_brain_wide_raw.xml` | untracked / ignored | xml | 355035 | 2026-07-01 16:54:12 | Run001 | keep | raw output for Run001 `pubmed_brain_wide`; supports search audit trail. |
| `data/raw/20260701_search_pubmed_pop_dynamics_raw.xml` | untracked / ignored | xml | 467587 | 2026-07-01 16:54:05 | Run001 | keep | raw output for Run001 `pubmed_pop_dynamics`; supports search audit trail. |
| `data/raw/20260701_search_pubmed_pubmed_population_dynamics_smoketest2_raw.xml` | untracked / ignored | xml | 75118 | 2026-07-01 00:10:59 | smoketest | delete after user approval | second PubMed smoketest output; not needed as current state unless user wants to retain test artifacts. |
| `data/raw/20260701_search_semanticscholar_api_key_s2_test2_raw.json` | untracked / ignored | json | 7729 | 2026-07-01 14:33:49 | API test | delete after user approval | Semantic Scholar API test output; cleanup candidate after user review. |
| `data/raw/20260701_search_semanticscholar_brain_wide_raw.json` | untracked / ignored | json | 65456 | 2026-07-01 15:17:10 | Run001 | keep | raw output for Run001 `semanticscholar_brain_wide`; needed for audit/reproducibility. |
| `data/raw/20260701_search_semanticscholar_pop_dynamics_raw.json` | untracked / ignored | json | 61707 | 2026-07-01 15:42:52 | Run001 | keep | raw output for Run001 `semanticscholar_pop_dynamics`; needed for audit/reproducibility. |
| `logs/20260630_extract_pdf_text.log` | untracked / ignored | log | 421 | 2026-06-30 23:42:47 | legacy/trial extraction | archive | extraction log has audit value but is not a current entry point. |
| `logs/20260701_extract_pdf_text.log` | untracked / ignored | log | 941 | 2026-07-01 00:29:24 | legacy/trial extraction | archive | extraction log has audit value; consider archive rather than deletion. |
| `logs/20260702_extract_pdf_text.log` | untracked / ignored | log | 1191 | 2026-07-02 12:11:18 | Run001 PDF extraction | archive | Run001 extraction log supports audit trail; not a current entry point. |
| `logs/semanticscholar_429_error.log` | untracked / ignored | log | 430 | 2026-07-01 00:12:54 | Semantic Scholar API issue | archive | API rate-limit/error log may explain prior unresolved S2 checks. |
| `logs/semanticscholar_api_error.log` | untracked / ignored | log | 1216 | 2026-07-01 15:35:46 | Search Run001 / S2 issue | archive | Relevant to Search Run001 error context; preserve as audit material. |
| `papers/extracted_text/khilkevich2024BrainwideDynamicsLinking.md` | untracked / ignored | md | 334923 | 2026-07-02 12:11:18 | Run001 first batch | keep | extracted text for confirmed Run001 paper; needed for note audit and possible follow-up. |
| `papers/extracted_text/michaels2016NeuralPopulationDynamics.md` | untracked / ignored | md | 103828 | 2026-07-02 12:11:17 | Run001 first batch | keep | extracted text for confirmed Run001 paper; needed for note audit and possible follow-up. |
| `papers/extracted_text/safaie2023PreservedNeuralDynamics.md` | untracked / ignored | md | 172291 | 2026-07-02 12:11:18 | Run001 first batch | keep | extracted text for confirmed Run001 paper; needed for note audit and possible follow-up. |
| `papers/extracted_text/vyas_2020_computation_through_neural.md` | untracked / ignored | md | 134558 | 2026-07-01 00:27:53 | legacy/trial confirmed row | keep | extracted text corresponds to existing local note / confirmed trial row; keep until legacy cleanup decision. |
| `papers/extracted_text/ye_2026_brainwide_topographic_coordination.md` | untracked / ignored | md | 271924 | 2026-06-30 23:42:47 | legacy/trial confirmed row | keep | extracted text corresponds to existing local note / confirmed trial row; keep until legacy cleanup decision. |
| `papers/raw_pdf/khilkevich2024BrainwideDynamicsLinking.pdf` | untracked / ignored | pdf | 59519723 | 2026-07-02 12:10:27 | Run001 first batch | keep | PDF for confirmed Run001 paper; needed for figure-level follow-up and audit. |
| `papers/raw_pdf/michaels2016NeuralPopulationDynamics.pdf` | untracked / ignored | pdf | 3400052 | 2026-07-02 12:10:29 | Run001 first batch | keep | PDF for confirmed Run001 paper; needed for figure-level follow-up and audit. |
| `papers/raw_pdf/safaie2023PreservedNeuralDynamics.pdf` | untracked / ignored | pdf | 16170884 | 2026-07-02 12:10:33 | Run001 first batch | keep | PDF for confirmed Run001 paper; needed for figure-level follow-up and audit. |
| `papers/raw_pdf/vyas_2020_computation_through_neural.pdf` | untracked / ignored | pdf | 840084 | 2026-07-01 00:26:53 | legacy/trial confirmed row | keep | PDF corresponds to existing local note / confirmed trial row; keep until legacy cleanup decision. |
| `papers/raw_pdf/ye_2026_brainwide_topographic_coordination.pdf` | untracked / ignored | pdf | 6977341 | 2026-06-30 23:41:01 | legacy/trial confirmed row | keep | PDF corresponds to existing local note / confirmed trial row; keep until legacy cleanup decision. |
| `references.bib` | untracked / ignored | bib | 13368 | 2026-07-02 11:20:09 | Zotero / Better BibTeX local source | keep | Ignored because it may contain local Zotero paths, but important for local citation verification. |
| `tables/20260630_search_arxiv_low_rank_rnn_smoketest.csv` | untracked / ignored | csv | 3909 | 2026-06-30 18:38:35 | smoketest | delete after user approval | generated smoketest CSV; candidate cleanup item after user review. |
| `tables/20260630_search_arxiv_neuroscience_smoketest.csv` | untracked / ignored | csv | 4447 | 2026-06-30 18:37:56 | smoketest | delete after user approval | generated smoketest CSV; not current curated state. |
| `tables/20260630_search_pubmed_population_dynamics_smoketest.csv` | untracked / ignored | csv | 5874 | 2026-06-30 18:32:36 | smoketest | delete after user approval | generated smoketest CSV; cleanup candidate after approval. |
| `tables/20260701_search_arxiv_arxiv_neural_dynamics_smoketest2.csv` | untracked / ignored | csv | 4237 | 2026-07-01 00:15:11 | smoketest | delete after user approval | generated second smoketest CSV; not current curated state. |
| `tables/20260701_search_arxiv_pop_dynamics.csv` | untracked / ignored | csv | 36080 | 2026-07-01 15:16:32 | Run001 | keep | per-search CSV used by Run001 review; keep for audit/reproducibility. |
| `tables/20260701_search_pubmed_api_key_pubmed_test.csv` | untracked / ignored | csv | 6218 | 2026-07-01 14:19:12 | API test | delete after user approval | generated API test CSV; should be removed only after user approval. |
| `tables/20260701_search_pubmed_brain_wide.csv` | untracked / ignored | csv | 44661 | 2026-07-01 16:54:12 | Run001 | keep | per-search CSV used by Run001 review; keep for audit/reproducibility. |
| `tables/20260701_search_pubmed_pop_dynamics.csv` | untracked / ignored | csv | 45912 | 2026-07-01 16:54:05 | Run001 | keep | per-search CSV used by Run001 review; keep for audit/reproducibility. |
| `tables/20260701_search_pubmed_pubmed_population_dynamics_smoketest2.csv` | untracked / ignored | csv | 5898 | 2026-07-01 00:10:59 | smoketest | delete after user approval | generated second PubMed smoketest CSV; cleanup candidate after approval. |
| `tables/20260701_search_semanticscholar_api_key_s2_test2.csv` | untracked / ignored | csv | 4247 | 2026-07-01 14:33:49 | API test | delete after user approval | generated Semantic Scholar API test CSV; cleanup candidate after approval. |
| `tables/20260701_search_semanticscholar_brain_wide.csv` | untracked / ignored | csv | 36923 | 2026-07-01 15:17:10 | Run001 | keep | per-search CSV used by Run001 review; keep for audit/reproducibility. |
| `tables/20260701_search_semanticscholar_pop_dynamics.csv` | untracked / ignored | csv | 41257 | 2026-07-01 15:42:52 | Run001 | keep | per-search CSV used by Run001 review; keep for audit/reproducibility. |

## High-priority user decisions

- Decide whether smoketest and API-test outputs should be deleted after user approval.
- Decide whether logs should be archived into a future local or tracked audit location.
- Keep Run001 raw outputs, per-search CSVs, PDFs, extracted text, and `references.bib` until Run001 follow-up and future audit needs are clearly resolved.

## Cleanup recommendation

Do not delete anything immediately.

Recommended next step is a separate cleanup plan after user review. That plan should list exact files approved for archive or deletion, then run validators and leakage checker after any approved action.
