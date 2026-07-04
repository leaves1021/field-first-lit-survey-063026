# Candidate Metadata Enrichment Run 001

## 1. Current candidate table status

`tables/candidate_papers.csv` 当前包含 8 条 `candidate_title_level` rows。本文件只为这 8 条 Search Run 001 candidates 制定 metadata enrichment 与 verification 计划，不修改任何 CSV。

8 条 titles：

1. `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
2. `Preserved neural dynamics across animals performing similar behaviour`
3. `Brain-wide dynamics linking sensation to action during decision-making`
4. `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input`
5. `Large-scale high-density brain-wide neural recording in nonhuman primates`
6. `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile`
7. `Human brain state dynamics are highly reproducible and associated with neural and behavioral features`
8. `Inferring stochastic low-rank recurrent neural networks from neural data`

## 2. Metadata gaps

这些 gaps 来自 `tables/candidate_papers.csv`、`synthesis/candidate_append_plan_run001.md` 和 `synthesis/search_run_001_candidate_selection.md` 的 title-level 信息；未读取 abstracts、raw JSON/XML 或 PDFs。

| Title | Missing or placeholder fields |
|---|---|
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | authors=`unclear_from_review`; abstract=`not_included_title_level_only`; raw_file=`unclear_from_review`; publication status 需核验为 peer-reviewed article; PMCID 当前为 `5096671`，需核验并规范为 `PMC5096671` 格式；Zotero / `references.bib` status 未检查；PDF availability 未检查。 |
| `Preserved neural dynamics across animals performing similar behaviour` | authors=`unclear_from_review`; abstract=`not_included_title_level_only`; raw_file=`unclear_from_review`; publication status 需核验为 peer-reviewed article; PMCID 当前为 `10665198`，需核验并规范为 `PMC10665198` 格式；Zotero / `references.bib` status 未检查；PDF availability 未检查。 |
| `Brain-wide dynamics linking sensation to action during decision-making` | authors=`unclear_from_review`; abstract=`not_included_title_level_only`; raw_file=`unclear_from_review`; publication status 需核验为 peer-reviewed article; PMCID 当前为 `11499283`，需核验并规范为 `PMC11499283` 格式；Zotero / `references.bib` status 未检查；PDF availability 未检查。 |
| `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input` | authors=`unclear_from_review`; abstract=`not_included_title_level_only`; raw_file=`unclear_from_review`; publication status 需核验为 peer-reviewed article; PMCID 当前为 `12717177`，需核验并规范为 `PMC12717177` 格式；Zotero / `references.bib` status 未检查；PDF availability 未检查。 |
| `Large-scale high-density brain-wide neural recording in nonhuman primates` | authors=`unclear_from_review`; abstract=`not_included_title_level_only`; raw_file=`unclear_from_review`; publication status 需核验为 peer-reviewed article; PMCID 当前为 `12229894`，需核验并规范为 `PMC12229894` 格式；Zotero / `references.bib` status 未检查；PDF availability 未检查。 |
| `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile` | authors=`unclear_from_review`; abstract=`not_included_title_level_only`; raw_file=`unclear_from_review`; publication status 需核验为 peer-reviewed article; PMCID 缺失或不可得；Zotero / `references.bib` status 未检查；PDF availability 未检查。 |
| `Human brain state dynamics are highly reproducible and associated with neural and behavioral features` | authors=`unclear_from_review`; abstract=`not_included_title_level_only`; raw_file=`unclear_from_review`; publication status 需核验为 peer-reviewed article; PMCID 当前为 `11421804`，需核验并规范为 `PMC11421804` 格式；Zotero / `references.bib` status 未检查；PDF availability 未检查。 |
| `Inferring stochastic low-rank recurrent neural networks from neural data` | authors=`unclear_from_review`; abstract=`not_included_title_level_only`; raw_file=`unclear_from_review`; publication status 需核验，当前 venue 为 Neural Information Processing Systems 且 DOI 为 arXiv DOI；PMID/PMCID 缺失或不可得；arXiv ID=`2406.16749`；Zotero / `references.bib` status 未检查；PDF availability 未检查。 |

## 3. Verification tasks per candidate

| Title | Verification tasks |
|---|---|
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | 核验 DOI `10.1371/journal.pcbi.1005175` 是否解析到同一 title；核验 PMID `27814352`；核验 PMCID `5096671` 是否对应同一 paper 并规范格式；核验 Semantic Scholar ID `af1a65fa44773c427235e1f88bf714d64418883f`；确认 peer-reviewed version；确认 paper type 是否为 representative experimental landmark。 |
| `Preserved neural dynamics across animals performing similar behaviour` | 核验 DOI `10.1038/s41586-023-06714-0`；核验 PMID `37938772`；核验 PMCID `10665198` 并规范格式；核验 Semantic Scholar ID `6c2952e1d99761ae5bc40558905b37875e87a8ab`；确认 peer-reviewed version；确认 paper type 是否为 representative experimental landmark。 |
| `Brain-wide dynamics linking sensation to action during decision-making` | 核验 DOI `10.1038/s41586-024-07908-w`；核验 PMID `39261727`；核验 PMCID `11499283` 并规范格式；核验 Semantic Scholar ID `edb148e6ccc32491a80ff81bc6918258bd6a4d7d`；确认 peer-reviewed version；确认 paper type 是否为 experimental landmark / brain-wide case-study paper。 |
| `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input` | 核验 DOI `10.1038/s41467-025-66104-0`；核验 PMID `41408036`；核验 PMCID `12717177` 并规范格式；核验 Semantic Scholar ID `1030c1b0db3a8a43b8aaee3fd215340359075bc2`；确认 peer-reviewed version；确认 paper type 是否为 causal perturbation / experimental landmark。 |
| `Large-scale high-density brain-wide neural recording in nonhuman primates` | 核验 DOI `10.1038/s41593-025-01976-5`；核验 PMID `40551025`；核验 PMCID `12229894` 并规范格式；核验 Semantic Scholar ID `ab37a484708b1832dff24b520120bd8a0e2e64a5`；确认 peer-reviewed version；确认 paper type 是 method/platform landmark 还是包含 experimental computation finding。 |
| `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile` | 核验 DOI `10.1073/pnas.1616361113`；核验 PMID `27930323`；确认是否存在 PMCID；核验 Semantic Scholar ID `027f3fff0947191976d13bb1ba2a7e95cd8d820e`；确认 peer-reviewed version；确认 paper type 是否为 multi-area communication experimental landmark。 |
| `Human brain state dynamics are highly reproducible and associated with neural and behavioral features` | 核验 DOI `10.1371/journal.pbio.3002808`；核验 PMID `39316635`；核验 PMCID `11421804` 并规范格式；核验 Semantic Scholar ID `8f7f30f53bdbbea2a78c81541e35df7ddbdb361d`；确认 peer-reviewed version；确认 paper type 是 representative experimental paper 还是 broader brain-state analysis。 |
| `Inferring stochastic low-rank recurrent neural networks from neural data` | 核验 DOI `10.48550/arXiv.2406.16749` 是否解析到同一 title；确认 PMID/PMCID 是否不存在或不可得；核验 arXiv ID `2406.16749`；核验 Semantic Scholar ID `579f56813a03517163b86fa89044dc78505bf2cb`；确认是否有 peer-reviewed NeurIPS version；确认 paper type 是否为 theoretical / computational method。 |

## 4. Candidate priority for confirmation

| Title | Priority | Reason |
|---|---|---|
| `Brain-wide dynamics linking sensation to action during decision-making` | confirm_first | peer-reviewed Nature；直接对齐 brain-wide / distributed computation 和 decision-making，是 Search Run 001 中最核心的 field-axis candidate 之一。 |
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | confirm_first | peer-reviewed PLoS Computational Biology；title-level selection 已标为 population dynamics landmark-style paper。 |
| `Preserved neural dynamics across animals performing similar behaviour` | confirm_first | peer-reviewed Nature；跨动物 neural dynamics，适合作为 population dynamics / neural manifolds 的代表性候选。 |
| `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input` | confirm_first | peer-reviewed Nature Communications；含 brain-wide dynamics 与 single thalamic input activation，优先核验 causal perturbation status。 |
| `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile` | confirm_first | peer-reviewed PNAS；直接对齐 multi-area communication / distributed brain-wide neural activity。 |
| `Human brain state dynamics are highly reproducible and associated with neural and behavioral features` | verify_later | peer-reviewed PLoS Biology；相关性高，但需先确认是 task-state、resting-state 还是 broader brain-state analysis。 |
| `Large-scale high-density brain-wide neural recording in nonhuman primates` | verify_later | peer-reviewed Nature Neuroscience；可能是技术/platform landmark，需判断是否包含 computation-level findings。 |
| `Inferring stochastic low-rank recurrent neural networks from neural data` | verify_later | 对 model-based inference 很有价值，但需要确认 NeurIPS version、是否为 peer-reviewed proceedings、以及 method 与 neural data 的连接强度。 |

当前 8 条中没有建议直接 `hold` 的记录；`hold` 可在 DOI/PMID/S2/版本核验失败、发现题名不匹配、或发现只是 generic ML drift 时再使用。

## 5. Recommended enrichment workflow

1. 以 DOI 为第一入口逐条核验 title、year、venue、authors 和 publication status。
2. 对有 PMID 的 records，用 PMID 核验是否对应同一 paper。
3. 对有 PMCID 的 records，用 PMCID 核验是否对应同一 paper，并把数字格式规范为 `PMC...`。
4. 对所有 records，用 Semantic Scholar ID 核验是否对应同一 title，并补充 authors、venue、publication year、open access / PDF 线索。
5. 对含 arXiv ID 的 record，核验 arXiv ID 与 DOI 是否指向同一 version，并确认是否已有 peer-reviewed proceedings entry。
6. enrichment 结果只应在后续单独步骤中更新 `tables/candidate_papers.csv`，本文件不修改 CSV。
7. 人工确认后，再把 selected papers 加入 Zotero，并通过 Better BibTeX 更新 `references.bib`。
8. 只有 metadata verification 完成后，才下载或读取 PDFs。
9. 只有完成 metadata verification、paper type 判断和必要的 full-text/PDF evidence 检查后，才考虑移动到 `tables/confirmed_papers.csv`。

## 6. What not to do yet

- 不要生成 paper-level notes。
- 不要更新 `tables/paper_matrix.csv`。
- 不要更新 `tables/figure_evidence_table.csv`。
- 不要把这 8 条 candidates 当作 confirmed papers。
- 不要下载 PDFs。
- 不要修改 scripts。
- 不要运行 broad searches。
- 不要在本步骤修改 `tables/candidate_papers.csv` 或 `tables/confirmed_papers.csv`。
