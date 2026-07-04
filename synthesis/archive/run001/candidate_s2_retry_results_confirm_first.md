# Candidate S2 Retry Results: Confirm First

## 1. Scope

本文件只记录两个此前因 Semantic Scholar 429 而未完成 S2 ID verification 的 `confirm_first` candidates。本次仅使用 targeted Semantic Scholar ID lookup，没有运行 broad searches，没有下载 PDFs，没有修改任何 CSV、scripts 或 confirmed tables。

Retry scope:

1. `Preserved neural dynamics across animals performing similar behaviour`
   - S2 ID: `6c2952e1d99761ae5bc40558905b37875e87a8ab`
2. `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile`
   - S2 ID: `027f3fff0947191976d13bb1ba2a7e95cd8d820e`

## 2. Retry results

| Candidate title | S2 ID | Retry result | S2 title | S2 DOI | S2 PMID | S2 PMCID | Match assessment | Recommended status |
|---|---|---|---|---|---|---|---|---|
| `Preserved neural dynamics across animals performing similar behaviour` | `6c2952e1d99761ae5bc40558905b37875e87a8ab` | success | Preserved neural dynamics across animals performing similar behaviour | 10.1038/s41586-023-06714-0 | 37938772 | 10665198 | S2 title / DOI / PMID / PMCID match current candidate metadata. | candidate_metadata_verified |
| `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile` | `027f3fff0947191976d13bb1ba2a7e95cd8d820e` | still_unresolved_due_429 | not_available_due_429 | not_available_due_429 | not_available_due_429 | not_available_due_429 | Semantic Scholar returned 429 again; PubMed metadata remains verified from prior step, but S2 ID match is still unresolved. | candidate_needs_manual_review |

## 3. Proposed CSV update preview, if any

Do not write these updates now. This is only a preview.

Allowed future update fields should remain limited to the previously approved metadata fields, especially `status` and `notes`.

| title | proposed status | proposed notes update |
|---|---|---|
| `Preserved neural dynamics across animals performing similar behaviour` | candidate_metadata_verified | Metadata verified by PMID/DOI/PMCID/S2 title match; Zotero references.bib absent; PDF availability open-access via PMCID. |
| `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile` | candidate_needs_manual_review | PubMed metadata verified and PMCID found; S2 ID check still unresolved due 429 rate limit; Zotero references.bib absent; PDF availability open-access via PMCID. |

## 4. Remaining unresolved items

- `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile` still needs a successful targeted Semantic Scholar ID lookup before upgrading to `candidate_metadata_verified`.
- No DOI / PMID / PMCID conflict is known for that candidate from the prior PubMed verification step.
- No full abstracts were read or copied.
- No PDFs were downloaded.

## 5. What not to do yet

- Do not modify `tables/candidate_papers.csv` in this step.
- Do not modify `tables/confirmed_papers.csv`.
- Do not modify `tables/paper_matrix.csv`.
- Do not modify `tables/figure_evidence_table.csv`.
- Do not modify scripts.
- Do not download PDFs.
- Do not create paper notes.
- Do not move any candidate to confirmed.
- Do not run broad searches.
