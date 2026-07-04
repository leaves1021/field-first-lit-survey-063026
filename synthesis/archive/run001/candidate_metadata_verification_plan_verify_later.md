# Candidate Metadata Verification Plan Verify Later

## 1. Purpose

本文件用于为 `tables/candidate_papers.csv` 中剩余 3 条 `candidate_title_level` records 制定 metadata verification plan。

这是一个 planning-only 文档，不执行任何 CSV 更新，不运行 broad searches，不下载 PDFs，不创建 paper notes，也不修改 scripts。

## 2. Scope

本计划只使用以下本地文件：

- `tables/candidate_papers.csv`
- `synthesis/candidate_metadata_enrichment_run001.md`
- `synthesis/candidate_append_plan_run001.md`

本计划覆盖的 3 条 records：

1. `Large-scale high-density brain-wide neural recording in nonhuman primates`
2. `Human brain state dynamics are highly reproducible and associated with neural and behavioral features`
3. `Inferring stochastic low-rank recurrent neural networks from neural data`

## 3. Record Plans

### 3.1 `Large-scale high-density brain-wide neural recording in nonhuman primates`

当前 `candidate_papers.csv` row values：

| field | value |
|---|---|
| source | Semantic Scholar |
| title | `Large-scale high-density brain-wide neural recording in nonhuman primates` |
| authors | `unclear_from_review` |
| year | `2025` |
| venue | `Nature Neuroscience` |
| doi | `10.1038/s41593-025-01976-5` |
| pmid | `40551025` |
| pmcid | `12229894` |
| arxiv_id | empty |
| semantic_scholar_id | `ab37a484708b1832dff24b520120bd8a0e2e64a5` |
| url | `https://doi.org/10.1038/s41593-025-01976-5` |
| abstract | `not_included_title_level_only` |
| search_query | `from_search_run_001` |
| search_topic | `brain_wide` |
| retrieved_at | `2026-07-01` |
| raw_file | `unclear_from_review` |
| initial_relevance | `high` |
| status | `candidate_title_level` |
| notes | `representative experimental landmark / method；brain-wide recording scale；需确认是否包含 computation-level results。` |

需核验的 metadata fields：

- authors
- year
- venue
- DOI
- PMID
- PMCID
- Semantic Scholar ID
- publication status
- Zotero / `references.bib` status
- PDF availability status

具体核验任务：

- 核验 DOI `10.1038/s41593-025-01976-5` 是否与当前 title、year、venue 一致。
- 核验 PMID `40551025` 是否对应同一 paper。
- 核验 PMCID `12229894` 是否对应同一 paper，并在后续更新时规范为 `PMC12229894`。
- 核验 Semantic Scholar ID `ab37a484708b1832dff24b520120bd8a0e2e64a5` 是否对应同一 title。
- 判断该 paper 属于 `peer_reviewed_article`、`proceedings_paper`、`preprint`、`method/platform paper` 或 `review/perspective` 中的哪一类。
- 重点确认它是否主要是 method/platform paper，还是同时包含对 brain-wide / distributed computation 有直接价值的 experimental/computation-level results。
- 检查是否已在 Zotero / `references.bib` 中存在。
- PDF availability 只做状态核验规划，后续再检查，不在本步骤下载。

建议的核验后候选状态：

- 若 DOI / PMID / PMCID / S2 一致，且 paper 为 peer-reviewed article 或明确的 method/platform landmark，可设为 `candidate_metadata_verified`。
- 若 identifiers 一致，但 paper 对本 survey 的 field-axis 价值仍不清晰，可设为 `candidate_needs_manual_review`。
- 若 identifiers 冲突，或发现与当前 title/version 不一致，可设为 `candidate_hold`。

后续允许更新的字段：

- `authors`
- `pmcid`
- `raw_file`
- `url`
- `status`
- `notes`

### 3.2 `Human brain state dynamics are highly reproducible and associated with neural and behavioral features`

当前 `candidate_papers.csv` row values：

| field | value |
|---|---|
| source | Semantic Scholar |
| title | `Human brain state dynamics are highly reproducible and associated with neural and behavioral features` |
| authors | `unclear_from_review` |
| year | `2024` |
| venue | `PLoS Biology` |
| doi | `10.1371/journal.pbio.3002808` |
| pmid | `39316635` |
| pmcid | `11421804` |
| arxiv_id | empty |
| semantic_scholar_id | `8f7f30f53bdbbea2a78c81541e35df7ddbdb361d` |
| url | `https://doi.org/10.1371/journal.pbio.3002808` |
| abstract | `not_included_title_level_only` |
| search_query | `from_search_run_001` |
| search_topic | `brain_wide` |
| retrieved_at | `2026-07-01` |
| raw_file | `unclear_from_review` |
| initial_relevance | `high` |
| status | `candidate_title_level` |
| notes | `representative experimental paper；human brain state dynamics 与 behavior；需要确认 state 类型与行为解释力度。` |

需核验的 metadata fields：

- authors
- year
- venue
- DOI
- PMID
- PMCID
- Semantic Scholar ID
- publication status
- Zotero / `references.bib` status
- PDF availability status

具体核验任务：

- 核验 DOI `10.1371/journal.pbio.3002808` 是否与当前 title、year、venue 一致。
- 核验 PMID `39316635` 是否对应同一 paper。
- 核验 PMCID `11421804` 是否对应同一 paper，并在后续更新时规范为 `PMC11421804`。
- 核验 Semantic Scholar ID `8f7f30f53bdbbea2a78c81541e35df7ddbdb361d` 是否对应同一 title。
- 判断 publication status，确认其是否为 peer-reviewed article，而不是 dataset note、perspective 或 broader methods paper。
- 重点确认 title 中的 `brain state dynamics` 指向何种 state 分析框架，以及它与 `neural and behavioral features` 的关系是否足以支持当前 `brain_wide` 轴。
- 检查是否已在 Zotero / `references.bib` 中存在。
- PDF availability 只做后续核验规划，本步骤不下载。

建议的核验后候选状态：

- 若 DOI / PMID / PMCID / S2 一致，且 paper 明确是与人类 brain-state dynamics 和 behavior 相关的 peer-reviewed experimental article，可设为 `candidate_metadata_verified`。
- 若 metadata 一致，但 title-level 仍不足以判断其与 survey 主轴的贴合度，可设为 `candidate_needs_manual_review`。
- 若 identifiers 或版本信息不一致，或发现 paper 类型与当前候选定位冲突，可设为 `candidate_hold`。

后续允许更新的字段：

- `authors`
- `pmcid`
- `raw_file`
- `url`
- `status`
- `notes`

### 3.3 `Inferring stochastic low-rank recurrent neural networks from neural data`

当前 `candidate_papers.csv` row values：

| field | value |
|---|---|
| source | Semantic Scholar |
| title | `Inferring stochastic low-rank recurrent neural networks from neural data` |
| authors | `unclear_from_review` |
| year | `2024` |
| venue | `Neural Information Processing Systems` |
| doi | `10.48550/arXiv.2406.16749` |
| pmid | empty |
| pmcid | empty |
| arxiv_id | `2406.16749` |
| semantic_scholar_id | `579f56813a03517163b86fa89044dc78505bf2cb` |
| url | `https://doi.org/10.48550/arXiv.2406.16749` |
| abstract | `not_included_title_level_only` |
| search_query | `from_search_run_001` |
| search_topic | `pop_dynamics` |
| retrieved_at | `2026-07-01` |
| raw_file | `unclear_from_review` |
| initial_relevance | `high` |
| status | `candidate_title_level` |
| notes | `theoretical / computational method；model-based inference from neural data；需要确认 method paper、benchmark data 和 survey 方法轴价值。` |

需核验的 metadata fields：

- authors
- year
- venue
- DOI
- arXiv ID
- Semantic Scholar ID
- publication status
- Zotero / `references.bib` status
- PDF availability status

具体核验任务：

- 核验 DOI `10.48550/arXiv.2406.16749` 是否与当前 title、year 一致。
- 核验 arXiv ID `2406.16749` 是否对应同一 title。
- 核验 Semantic Scholar ID `579f56813a03517163b86fa89044dc78505bf2cb` 是否对应同一 title。
- 确认当前 `venue = Neural Information Processing Systems` 与 arXiv DOI 的组合是否指向同一版本，或是否存在单独的 peer-reviewed proceedings version。
- 判断该 paper 属于 `peer_reviewed_article`、`proceedings_paper`、`preprint`、`method/platform paper` 或 `review/perspective` 中的哪一类。
- 重点确认它是否真的是 `from neural data` 的 method paper，而不只是 generic ML / RNN inference paper。
- 检查是否已在 Zotero / `references.bib` 中存在。
- PDF availability 仅作后续状态核验规划，本步骤不下载。

建议的核验后候选状态：

- 若 arXiv / S2 / venue/version 信息一致，且确认是与 neural data 紧密相关的 proceedings paper 或稳定版本 method paper，可设为 `candidate_metadata_verified`。
- 若 metadata 基本一致，但 peer-reviewed status、version 映射或 neuroscience relevance 仍有不确定性，可设为 `candidate_needs_manual_review`。
- 若 title/version/venue 冲突明显，或发现主要是 generic ML drift，可设为 `candidate_hold`。

后续允许更新的字段：

- `authors`
- `pmcid`
- `raw_file`
- `url`
- `status`
- `notes`

## 4. Shared Verification Focus

这 3 条 `verify_later` records 的共同核验重点：

- 先确认 identifiers 是否一一对应，再判断 scientific fit，不要反过来。
- 不要因为 title 看起来相关，就跳过 DOI / PMID / PMCID / arXiv / S2 的一致性检查。
- `Large-scale high-density brain-wide neural recording in nonhuman primates` 要重点防止把 platform/method paper 直接当作 computation evidence。
- `Human brain state dynamics are highly reproducible and associated with neural and behavioral features` 要重点确认其 state framework 与 behavior relevance，不要仅因 `brain state dynamics` 命中就默认纳入核心轴。
- `Inferring stochastic low-rank recurrent neural networks from neural data` 要重点防止 generic ML / modeling drift，并确认 arXiv version 与 proceedings version 的关系。

## 5. Exact Fields That May Be Updated Later

后续若完成 metadata verification，允许在单独步骤中更新 `tables/candidate_papers.csv` 的字段仅限：

- `authors`
- `pmcid`
- `raw_file`
- `url`
- `status`
- `notes`

本计划不会写入这些字段。

## 6. What Not To Do Yet

- 不要修改 `tables/candidate_papers.csv`。
- 不要修改任何其他 CSV。
- 不要运行 broad searches。
- 不要下载 PDFs。
- 不要创建 paper notes。
- 不要更新 `tables/confirmed_papers.csv`。
- 不要更新 `tables/paper_matrix.csv`。
- 不要更新 `tables/figure_evidence_table.csv`。
- 不要修改 scripts。
- 不要在 metadata 未核验前推断 authors。
- 不要在本文件中加入 full abstracts。
