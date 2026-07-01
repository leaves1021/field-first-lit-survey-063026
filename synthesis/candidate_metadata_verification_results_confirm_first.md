# Candidate Metadata Verification Results: Confirm First

## Scope and sources

本文件记录 5 个 `confirm_first` candidates 的 metadata verification 结果，用于后续人工决定是否更新 `tables/candidate_papers.csv`。本步骤没有修改任何 CSV、scripts、notes 或 PDFs。

使用的信息源：

- `tables/candidate_papers.csv`
- `synthesis/candidate_metadata_enrichment_plan_confirm_first.md`
- PubMed / NCBI ESummary 定点 PMID 查询
- Semantic Scholar Graph API 定点 paper ID 查询
- local `references.bib` 定点匹配

未执行 broad searches，未读取 full abstracts，未下载 PDFs。

## Verification results

| Candidate title from `candidate_papers.csv` | Verified title | Verified authors | Verified year | Verified venue | DOI match | PMID match | PMCID match / normalized PMCID | Semantic Scholar ID match | Publication status | Zotero / `references.bib` status | PDF availability | Recommended candidate status | Short verification note |
|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|
| `Brain-wide dynamics linking sensation to action during decision-making` | Brain-wide dynamics linking sensation to action during decision-making | Andrei Khilkevich; Michael Lohse; Ryan J. Low; Ivana Orsolic; Tadej Bozic; Paige Windmill; T. Mrsic-Flogel | 2024 | Nature | yes | yes | yes / `PMC11499283` | yes | peer_reviewed_article | absent | available_open_access | candidate_metadata_verified | PubMed DOI/PMID/PMCID match title; Semantic Scholar ID also matches title and identifiers. Authors differ only in initials/diacritics conventions across sources. |
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning | Jonathan A. Michaels; Benjamin Dann; Hansjorg Scherberger | 2016 | PLoS Computational Biology | yes | yes | yes / `PMC5096671` | yes | peer_reviewed_article | absent | available_open_access | candidate_metadata_verified | PubMed and Semantic Scholar agree on title, DOI, PMID, PMCID, year, and venue. |
| `Preserved neural dynamics across animals performing similar behaviour` | Preserved neural dynamics across animals performing similar behaviour | M. Safaie; J. C. Chang; J. Park; L. E. Miller; J. T. Dudman; M. G. Perich; J. A. Gallego | 2023 | Nature | yes | yes | yes / `PMC10665198` | unclear | peer_reviewed_article | absent | available_open_access | candidate_needs_manual_review | PubMed verifies DOI/PMID/PMCID/title. Semantic Scholar ID lookup was rate-limited by 429 during this run, so S2 match remains unclear. |
| `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input` | Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input | Linshan Xie; Xunda Wang; Xuehong Lin; Junjian Wen; Teng Ma; Alex T. L. Leong; Ed X. Wu | 2025 | Nature Communications | yes | yes | yes / `PMC12717177` | yes | peer_reviewed_article | absent | available_open_access | candidate_metadata_verified | PubMed and Semantic Scholar agree on title, DOI, PMID, PMCID, year, and venue. PDF availability is treated as open-access because PMCID is present, despite S2 reporting no direct OA PDF URL. |
| `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile` | Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile | Leong AT; Chan RW; Gao PP; Chan YS; Tsia KK; Yung WH; Wu EX | 2016 | Proceedings of the National Academy of Sciences of the United States of America | yes | yes | yes / `PMC5187697` | unclear | peer_reviewed_article | absent | available_open_access | candidate_needs_manual_review | PubMed verifies DOI/PMID/title and provides a PMCID not present in the current candidate row. Semantic Scholar ID lookup was rate-limited by 429 during this run, so S2 match remains unclear. |

## Proposed CSV updates preview

Do not write these updates now. This table is only a preview of allowed future changes to `tables/candidate_papers.csv`.

Allowed future update fields only: `authors`, `pmcid`, `raw_file`, `url`, `status`, `notes`.

| title | authors | pmcid | raw_file | url | status | notes |
|---|---|---|---|---|---|---|
| `Brain-wide dynamics linking sensation to action during decision-making` | Andrei Khilkevich; Michael Lohse; Ryan J. Low; Ivana Orsolic; Tadej Bozic; Paige Windmill; T. Mrsic-Flogel | PMC11499283 | data/raw/20260701_search_semanticscholar_pop_dynamics_raw.json | https://doi.org/10.1038/s41586-024-07908-w | candidate_metadata_verified | Metadata verified by PMID/DOI/PMCID/S2 title match; Zotero references.bib absent; PDF availability open-access via PMCID. |
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | Jonathan A. Michaels; Benjamin Dann; Hansjorg Scherberger | PMC5096671 | data/raw/20260701_search_semanticscholar_pop_dynamics_raw.json | https://doi.org/10.1371/journal.pcbi.1005175 | candidate_metadata_verified | Metadata verified by PMID/DOI/PMCID/S2 title match; Zotero references.bib absent; PDF availability open-access. |
| `Preserved neural dynamics across animals performing similar behaviour` | M. Safaie; J. C. Chang; J. Park; L. E. Miller; J. T. Dudman; M. G. Perich; J. A. Gallego | PMC10665198 | data/raw/20260701_search_semanticscholar_pop_dynamics_raw.json | https://doi.org/10.1038/s41586-023-06714-0 | candidate_needs_manual_review | PubMed metadata verified; S2 ID check unresolved due 429 rate limit; Zotero references.bib absent; PDF availability open-access via PMCID. |
| `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input` | Linshan Xie; Xunda Wang; Xuehong Lin; Junjian Wen; Teng Ma; Alex T. L. Leong; Ed X. Wu | PMC12717177 | data/raw/20260701_search_semanticscholar_brain_wide_raw.json | https://doi.org/10.1038/s41467-025-66104-0 | candidate_metadata_verified | Metadata verified by PMID/DOI/PMCID/S2 title match; Zotero references.bib absent; PDF availability open-access via PMCID. |
| `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile` | Leong AT; Chan RW; Gao PP; Chan YS; Tsia KK; Yung WH; Wu EX | PMC5187697 | data/raw/20260701_search_semanticscholar_brain_wide_raw.json | https://doi.org/10.1073/pnas.1616361113 | candidate_needs_manual_review | PubMed metadata verified and PMCID found; S2 ID check unresolved due 429 rate limit; Zotero references.bib absent; PDF availability open-access via PMCID. |

## Notes on unresolved items

- Semantic Scholar API returned 429 for two IDs during this verification run:
  - `6c2952e1d99761ae5bc40558905b37875e87a8ab`
  - `027f3fff0947191976d13bb1ba2a7e95cd8d820e`
- Those two records are therefore not marked `candidate_metadata_verified` yet, even though PubMed DOI/PMID/PMCID metadata matched.
- `references.bib` had no exact matches for the checked DOI/PMID/Semantic Scholar IDs, so all five are marked `absent` for Zotero / `references.bib` status.
- No abstracts were copied into this file.
- No PDFs were downloaded.

## What not to do yet

- Do not modify `tables/candidate_papers.csv`.
- Do not modify `tables/confirmed_papers.csv`.
- Do not modify `tables/paper_matrix.csv`.
- Do not modify `tables/figure_evidence_table.csv`.
- Do not modify scripts.
- Do not download PDFs.
- Do not create paper notes.
- Do not move any candidate to confirmed.
- Do not infer paper claims from metadata alone.
