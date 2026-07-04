# Candidate Metadata Enrichment Plan: Confirm First

## 1. Purpose

本文件为 5 个 `confirm_first` candidates 制定具体 metadata enrichment plan。它不是 metadata 写入步骤，不修改任何 CSV，不移动任何 candidate 到 confirmed，也不生成 paper notes 或下载 PDFs。

使用来源：

- `tables/candidate_papers.csv`
- `synthesis/candidate_metadata_enrichment_run001.md`

本文件不包含 full abstracts，不推断未核验 authors，适合 commit 到 GitHub。

## 2. Scope

本计划仅覆盖以下 5 条：

1. `Brain-wide dynamics linking sensation to action during decision-making`
2. `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
3. `Preserved neural dynamics across animals performing similar behaviour`
4. `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input`
5. `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile`

## 3. Candidate Plans

### 3.1 `Brain-wide dynamics linking sensation to action during decision-making`

Current `candidate_papers.csv` row values:

| Field | Value |
|---|---|
| source | Semantic Scholar |
| title | Brain-wide dynamics linking sensation to action during decision-making |
| authors | unclear_from_review |
| year | 2024 |
| venue | Nature |
| doi | 10.1038/s41586-024-07908-w |
| pmid | 39261727 |
| pmcid | 11499283 |
| arxiv_id |  |
| semantic_scholar_id | edb148e6ccc32491a80ff81bc6918258bd6a4d7d |
| url | https://doi.org/10.1038/s41586-024-07908-w |
| abstract | not_included_title_level_only |
| search_query | from_search_run_001 |
| search_topic | pop_dynamics |
| retrieved_at | 2026-07-01 |
| raw_file | unclear_from_review |
| initial_relevance | high |
| status | candidate_title_level |
| notes | representative experimental landmark；brain-wide / distributed computation；需检查是否与其他 decision-making multi-area papers 概念重叠。 |

Metadata fields to enrich: `authors`, publication status, normalized `pmcid`, `raw_file` provenance, Zotero / `references.bib` status, PDF availability status, and concise verification notes. Do not insert full abstract text in this planning file.

Verification tasks:

- DOI: verify `10.1038/s41586-024-07908-w` resolves to the same title.
- PMID: verify `39261727` corresponds to the same paper.
- PMCID: verify `11499283` corresponds to the same paper and normalize to `PMC11499283` if verified.
- Semantic Scholar ID: verify `edb148e6ccc32491a80ff81bc6918258bd6a4d7d` corresponds to the same paper.
- Zotero / `references.bib`: check whether the record already exists before adding.
- PDF availability: check later, only after metadata verification.

Proposed final status after enrichment: `candidate_metadata_verified` if all identifiers agree; `candidate_needs_manual_review` if one metadata source disagrees; `candidate_hold` if DOI/title or PMID/title conflict.

### 3.2 `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`

Current `candidate_papers.csv` row values:

| Field | Value |
|---|---|
| source | Semantic Scholar |
| title | Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning |
| authors | unclear_from_review |
| year | 2016 |
| venue | PLoS Comput. Biol. |
| doi | 10.1371/journal.pcbi.1005175 |
| pmid | 27814352 |
| pmcid | 5096671 |
| arxiv_id |  |
| semantic_scholar_id | af1a65fa44773c427235e1f88bf714d64418883f |
| url | https://doi.org/10.1371/journal.pcbi.1005175 |
| abstract | not_included_title_level_only |
| search_query | from_search_run_001 |
| search_topic | pop_dynamics |
| retrieved_at | 2026-07-01 |
| raw_file | unclear_from_review |
| initial_relevance | high |
| status | candidate_title_level |
| notes | representative experimental landmark；population dynamics / neural manifolds；需要人工确认任务、物种、记录尺度和 figure-level evidence。 |

Metadata fields to enrich: `authors`, publication status, normalized `pmcid`, `raw_file` provenance, Zotero / `references.bib` status, PDF availability status, and concise verification notes.

Verification tasks:

- DOI: verify `10.1371/journal.pcbi.1005175` resolves to the same title.
- PMID: verify `27814352` corresponds to the same paper.
- PMCID: verify `5096671` corresponds to the same paper and normalize to `PMC5096671` if verified.
- Semantic Scholar ID: verify `af1a65fa44773c427235e1f88bf714d64418883f` corresponds to the same paper.
- Zotero / `references.bib`: check whether the record already exists before adding.
- PDF availability: check later, only after metadata verification.

Proposed final status after enrichment: `candidate_metadata_verified` if all identifiers agree; otherwise `candidate_needs_manual_review` or `candidate_hold` depending on conflict severity.

### 3.3 `Preserved neural dynamics across animals performing similar behaviour`

Current `candidate_papers.csv` row values:

| Field | Value |
|---|---|
| source | Semantic Scholar |
| title | Preserved neural dynamics across animals performing similar behaviour |
| authors | unclear_from_review |
| year | 2023 |
| venue | Nature |
| doi | 10.1038/s41586-023-06714-0 |
| pmid | 37938772 |
| pmcid | 10665198 |
| arxiv_id |  |
| semantic_scholar_id | 6c2952e1d99761ae5bc40558905b37875e87a8ab |
| url | https://doi.org/10.1038/s41586-023-06714-0 |
| abstract | not_included_title_level_only |
| search_query | from_search_run_001 |
| search_topic | pop_dynamics |
| retrieved_at | 2026-07-01 |
| raw_file | unclear_from_review |
| initial_relevance | high |
| status | candidate_title_level |
| notes | representative experimental landmark；跨动物 neural dynamics；需要确认是否适合作为 field-level anchor。 |

Metadata fields to enrich: `authors`, publication status, normalized `pmcid`, `raw_file` provenance, Zotero / `references.bib` status, PDF availability status, and concise verification notes.

Verification tasks:

- DOI: verify `10.1038/s41586-023-06714-0` resolves to the same title.
- PMID: verify `37938772` corresponds to the same paper.
- PMCID: verify `10665198` corresponds to the same paper and normalize to `PMC10665198` if verified.
- Semantic Scholar ID: verify `6c2952e1d99761ae5bc40558905b37875e87a8ab` corresponds to the same paper.
- Zotero / `references.bib`: check whether the record already exists before adding.
- PDF availability: check later, only after metadata verification.

Proposed final status after enrichment: `candidate_metadata_verified` if all identifiers agree; otherwise `candidate_needs_manual_review` or `candidate_hold`.

### 3.4 `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input`

Current `candidate_papers.csv` row values:

| Field | Value |
|---|---|
| source | Semantic Scholar |
| title | Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input |
| authors | unclear_from_review |
| year | 2025 |
| venue | Nature Communications |
| doi | 10.1038/s41467-025-66104-0 |
| pmid | 41408036 |
| pmcid | 12717177 |
| arxiv_id |  |
| semantic_scholar_id | 1030c1b0db3a8a43b8aaee3fd215340359075bc2 |
| url | https://doi.org/10.1038/s41467-025-66104-0 |
| abstract | not_included_title_level_only |
| search_query | from_search_run_001 |
| search_topic | brain_wide |
| retrieved_at | 2026-07-01 |
| raw_file | unclear_from_review |
| initial_relevance | high |
| status | candidate_title_level |
| notes | representative experimental landmark；brain-wide dynamics 加 single thalamic input activation；具备 causal perturbation angle。 |

Metadata fields to enrich: `authors`, publication status, normalized `pmcid`, `raw_file` provenance, Zotero / `references.bib` status, PDF availability status, and concise verification notes.

Verification tasks:

- DOI: verify `10.1038/s41467-025-66104-0` resolves to the same title.
- PMID: verify `41408036` corresponds to the same paper.
- PMCID: verify `12717177` corresponds to the same paper and normalize to `PMC12717177` if verified.
- Semantic Scholar ID: verify `1030c1b0db3a8a43b8aaee3fd215340359075bc2` corresponds to the same paper.
- Zotero / `references.bib`: check whether the record already exists before adding.
- PDF availability: check later, only after metadata verification.

Proposed final status after enrichment: `candidate_metadata_verified` if all identifiers agree; otherwise `candidate_needs_manual_review` or `candidate_hold`.

### 3.5 `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile`

Current `candidate_papers.csv` row values:

| Field | Value |
|---|---|
| source | Semantic Scholar |
| title | Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile |
| authors | unclear_from_review |
| year | 2016 |
| venue | PNAS |
| doi | 10.1073/pnas.1616361113 |
| pmid | 27930323 |
| pmcid |  |
| arxiv_id |  |
| semantic_scholar_id | 027f3fff0947191976d13bb1ba2a7e95cd8d820e |
| url | https://doi.org/10.1073/pnas.1616361113 |
| abstract | not_included_title_level_only |
| search_query | from_search_run_001 |
| search_topic | brain_wide |
| retrieved_at | 2026-07-01 |
| raw_file | unclear_from_review |
| initial_relevance | high |
| status | candidate_title_level |
| notes | representative experimental landmark；multi-area communication and routing；需要检查实验系统、投射通路和 causal status。 |

Metadata fields to enrich: `authors`, publication status, PMCID availability, `raw_file` provenance, Zotero / `references.bib` status, PDF availability status, and concise verification notes.

Verification tasks:

- DOI: verify `10.1073/pnas.1616361113` resolves to the same title.
- PMID: verify `27930323` corresponds to the same paper.
- PMCID: no PMCID is currently available in the row; check whether one exists before leaving blank.
- Semantic Scholar ID: verify `027f3fff0947191976d13bb1ba2a7e95cd8d820e` corresponds to the same paper.
- Zotero / `references.bib`: check whether the record already exists before adding.
- PDF availability: check later, only after metadata verification.

Proposed final status after enrichment: `candidate_metadata_verified` if DOI, PMID, S2 ID, title, year, and venue agree; `candidate_needs_manual_review` if PMCID availability remains unclear; `candidate_hold` if identifiers conflict.

## 4. Exact Fields To Update Later In `candidate_papers.csv`

Do not update these fields now. A later approved write step may update:

- `authors`
- `pmcid`, normalized to `PMC...` where verified
- `raw_file`, if provenance should point back to a verified local metadata file
- `url`, only if a more appropriate verified URL is chosen
- `status`, from `candidate_title_level` to `candidate_metadata_verified`, `candidate_needs_manual_review`, or `candidate_hold`
- `notes`, adding concise metadata verification notes

Do not add full abstracts unless a separate project policy explicitly asks to store abstracts. If publication status, PDF availability, Zotero status, or BibTeX key need durable tracking, decide that in a separate schema update before editing CSV.

## 5. No-Write Preflight Checklist

Before any write operation:

1. Confirm `tables/candidate_papers.csv` still contains the 5 target rows.
2. Confirm none of the 5 rows has already been moved to `tables/confirmed_papers.csv`.
3. Verify DOI-title-year-venue match for all 5 candidates.
4. Verify PMID-title match where PMID is available.
5. Verify PMCID-title match where PMCID is available; normalize only after match is confirmed.
6. Verify Semantic Scholar ID-title match.
7. Check Zotero / `references.bib` for existing entries to avoid duplicates.
8. Record whether PDF availability exists, but do not download PDFs.
9. Prepare a diff preview of intended CSV updates before applying them.

## 6. Later-Write Checklist

Only after human approval:

1. Update only approved rows in `tables/candidate_papers.csv`.
2. Preserve all existing columns and column order.
3. Fill `authors` only from explicitly verified metadata.
4. Normalize PMCID values only when verified.
5. Set `status` to `candidate_metadata_verified`, `candidate_needs_manual_review`, or `candidate_hold` according to verification outcome.
6. Keep abstracts out unless separately approved.
7. Add short verification notes without paper claims or abstract text.
8. Re-run a schema/header check after writing.

## 7. What Not To Do Yet

- Do not modify `tables/candidate_papers.csv`.
- Do not modify `tables/confirmed_papers.csv`.
- Do not modify `tables/paper_matrix.csv`.
- Do not modify `tables/figure_evidence_table.csv`.
- Do not modify scripts.
- Do not download PDFs.
- Do not create paper notes.
- Do not move any candidate to confirmed.
- Do not run broad searches.
- Do not infer missing authors unless metadata has been explicitly verified.
- Do not include full abstracts in this planning file.
