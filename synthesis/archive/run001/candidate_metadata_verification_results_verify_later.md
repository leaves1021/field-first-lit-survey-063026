# Candidate Metadata Verification Results Verify Later

## 1. Scope

本文件记录对以下 3 条 `candidate_title_level` records 的小范围 metadata verification 结果：

1. `Large-scale high-density brain-wide neural recording in nonhuman primates`
2. `Human brain state dynamics are highly reproducible and associated with neural and behavioral features`
3. `Inferring stochastic low-rank recurrent neural networks from neural data`

使用范围仅限：

- `tables/candidate_papers.csv`
- `synthesis/candidate_metadata_verification_plan_verify_later.md`
- DOI landing page / journal page
- PMID / PubMed / PMCID 的定点核验尝试
- Semantic Scholar ID 的定点核验尝试
- arXiv ID 的定点核验
- 本地 `references.bib`

本文件不修改任何 CSV，不下载 PDF，不创建 paper notes，也不运行 broad searches。

## 2. Verification Results

### 2.1 `Large-scale high-density brain-wide neural recording in nonhuman primates`

| Field | Result |
|---|---|
| Candidate title from `candidate_papers.csv` | `Large-scale high-density brain-wide neural recording in nonhuman primates` |
| Verified title | `Large-scale high-density brain-wide neural recording in nonhuman primates` |
| Verified authors | `Eric M. Trautmann; Janis K. Hesse; Gabriel M. Stine; Ruobing Xia; Shude Zhu; Daniel J. O'Shea; Bill Karsh; Jennifer Colonell; Frank F. Lanfranchi; Saurabh Vyas; Andrew Zimnik; Elom Amematsro; Natalie A. Steinemann; Daniel A. Wagenaar; Marius Pachitariu; Alexandru Andrei; Carolina Mora Lopez; John O'Callaghan; Jan Putzeys; Bogdan C. Raducanu; Marleen Welkenhuysen; Mark Churchland; Tirin Moore; Michael Shadlen; Krishna Shenoy; Doris Tsao; Barundeb Dutta; ...; Timothy Harris` |
| Verified year | `2025` |
| Verified venue | `Nature Neuroscience` |
| DOI match | `yes` |
| PMID match | `unclear` |
| PMCID match and normalized PMCID | `unclear; PMC12229894` |
| arXiv ID match | `not_available` |
| Semantic Scholar ID match | `unclear` |
| Publication status | `peer_reviewed_article` |
| Paper type | `method_platform_paper` |
| Zotero / `references.bib` status | `absent` |
| PDF availability | `available_open_access` |
| Recommended candidate status | `candidate_needs_manual_review` |
| Short verification note | DOI、title、year、venue 与 Nature Neuroscience article page 一致；页面明确标注 `Technical Report` 和 `Open access`，更像 platform / recording technology landmark。作者列表在当前浏览器视图中间有折叠省略，因此不宜把该条直接当作完整 authors 写回 CSV。当前 PMCID 与 PMID 未能通过结构化 NCBI endpoint 直接回读确认，Semantic Scholar ID 也未能在当前环境中直接核验，因此保留 manual review。 |

### 2.2 `Human brain state dynamics are highly reproducible and associated with neural and behavioral features`

| Field | Result |
|---|---|
| Candidate title from `candidate_papers.csv` | `Human brain state dynamics are highly reproducible and associated with neural and behavioral features` |
| Verified title | `Human brain state dynamics are highly reproducible and associated with neural and behavioral features` |
| Verified authors | `Kangjoo Lee; Jie Lisa Ji; Clara Fonteneau; Lucie Berkovitch; Masih Rahmati; Lining Pan; Grega Repovš; John H. Krystal; John D. Murray; Alan Anticevic` |
| Verified year | `2024` |
| Verified venue | `PLOS Biology` |
| DOI match | `yes` |
| PMID match | `unclear` |
| PMCID match and normalized PMCID | `unclear; PMC11421804` |
| arXiv ID match | `not_available` |
| Semantic Scholar ID match | `unclear` |
| Publication status | `peer_reviewed_article` |
| Paper type | `representative_experimental_paper` |
| Zotero / `references.bib` status | `absent` |
| PDF availability | `available_open_access` |
| Recommended candidate status | `candidate_needs_manual_review` |
| Short verification note | PLOS Biology article page明确标注 `Open Access`、`Peer-reviewed`、`Research Article`，title、authors、published date、DOI 与当前 row 一致。scientific fit 仍需人工判断，因为该 paper 更偏 human resting-state / co-activation pattern dynamics 与 behavior 关联，是否作为本轮 `brain_wide / distributed computation` 核心候选仍需后续确认。 |

### 2.3 `Inferring stochastic low-rank recurrent neural networks from neural data`

| Field | Result |
|---|---|
| Candidate title from `candidate_papers.csv` | `Inferring stochastic low-rank recurrent neural networks from neural data` |
| Verified title | `Inferring stochastic low-rank recurrent neural networks from neural data` |
| Verified authors | `Matthijs Pals; A Erdem Sagtekin; Felix Pei; Manuel Gloeckler; Jakob H Macke` |
| Verified year | `2024` |
| Verified venue | `The Thirty-eighth Annual Conference on Neural Information Processing Systems (NeurIPS) 2024` |
| DOI match | `yes` |
| PMID match | `not_available` |
| PMCID match and normalized PMCID | `not_available` |
| arXiv ID match | `yes` |
| Semantic Scholar ID match | `unclear` |
| Publication status | `proceedings_paper` |
| Paper type | `theoretical_computational_method` |
| Zotero / `references.bib` status | `absent` |
| PDF availability | `available_open_access` |
| Recommended candidate status | `candidate_metadata_verified` |
| Short verification note | arXiv page可直接核验 title、authors、arXiv ID、arXiv DOI，以及 `Journal reference: ... NeurIPS 2024`。abstract 首句直接定位到 computational neuroscience / neural dynamics / neural data inference，method-axis 对齐明确。当前 Semantic Scholar ID 未能在当前环境中直接核验，但没有发现与 DOI / arXiv / venue 的冲突。 |

## 3. Verification Caveats

- 本轮对 PMID / PMCID 的结构化 NCBI / PMC endpoint 做了定点访问尝试，但当前 Windows PowerShell 与网络环境下出现 TLS / credential 级别连接问题，无法稳定回读 JSON/XML metadata。
- 直接打开 PMC article URLs 时可以到达浏览器检查页，但未能绕过 reCAPTCHA，因此 `PMCID match` 对前两篇保守标记为 `unclear`，同时保留标准化后的 `PMC...` 形式。
- Semantic Scholar ID 做了定点 lookup 尝试，但当前环境未返回可核验的 paper metadata，也未明确返回 429，因此统一记为 `unclear`，而不是 `still_unresolved_due_429`。
- `references.bib` 中未检索到这 3 篇的 title、DOI、PMID、arXiv ID 或 Semantic Scholar ID。

## Proposed CSV Updates Preview

以下仅为后续可能写入 `tables/candidate_papers.csv` 的 preview，不在本步骤执行。

| title | authors | pmcid | raw_file | url | status | notes |
|---|---|---|---|---|---|---|
| `Large-scale high-density brain-wide neural recording in nonhuman primates` | `unclear_from_review` | `PMC12229894` | `data/raw/20260701_search_semanticscholar_brain_wide_raw.json` | `https://doi.org/10.1038/s41593-025-01976-5` | `candidate_needs_manual_review` | `DOI/title/year/venue verified from Nature Neuroscience; article type appears to be method/platform Technical Report; browser view shows a truncated author list, so authors should not be updated yet from this pass; PMID/PMCID/S2 direct verification remains incomplete in current environment; Zotero references.bib absent; PDF availability open-access.` |
| `Human brain state dynamics are highly reproducible and associated with neural and behavioral features` | `Kangjoo Lee; Jie Lisa Ji; Clara Fonteneau; Lucie Berkovitch; Masih Rahmati; Lining Pan; Grega Repovš; John H. Krystal; John D. Murray; Alan Anticevic` | `PMC11421804` | `data/raw/20260701_search_semanticscholar_brain_wide_raw.json` | `https://doi.org/10.1371/journal.pbio.3002808` | `candidate_needs_manual_review` | `DOI/title/authors/year/venue verified from PLOS Biology; peer-reviewed research article and open access; scientific fit to core brain-wide/distributed computation axis still needs manual review; Zotero references.bib absent.` |
| `Inferring stochastic low-rank recurrent neural networks from neural data` | `Matthijs Pals; A Erdem Sagtekin; Felix Pei; Manuel Gloeckler; Jakob H Macke` | `` | `data/raw/20260701_search_semanticscholar_pop_dynamics_raw.json` | `https://doi.org/10.48550/arXiv.2406.16749` | `candidate_metadata_verified` | `Title/authors/arXiv ID/arXiv DOI/journal reference verified from arXiv; proceedings version listed as NeurIPS 2024; method-axis relevance clear for model-based inference from neural data; Zotero references.bib absent; PDF availability open-access.` |

## 5. What Not To Do Yet

- 不要现在写入 `tables/candidate_papers.csv`。
- 不要更新 `tables/confirmed_papers.csv`。
- 不要更新 `tables/paper_matrix.csv`。
- 不要更新 `tables/figure_evidence_table.csv`。
- 不要下载 PDFs。
- 不要创建 paper notes。
- 不要把 `candidate_needs_manual_review` 误当成 negative exclusion；这里只是保留 scientific fit 或 identifier verification 的不确定性。
