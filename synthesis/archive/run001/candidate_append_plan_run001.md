# Candidate Append Plan Run 001

## 1. Purpose

本文件是 Search Run 001 第一小批候选记录的 append plan，不是 append 本身。它的作用是把人工审批前可能追加到 `tables/candidate_papers.csv` 的记录整理成受控清单，便于下一步 review。

本文件不会修改 `tables/candidate_papers.csv`，不会选择 confirmed papers，也不会生成 notes、下载 PDFs 或运行 searches。

## 2. Current candidate table status

`tables/candidate_papers.csv` 当前只有 header，没有 data rows。

当前文件的 exact header 为：

```csv
source,title,authors,year,venue,doi,pmid,pmcid,arxiv_id,semantic_scholar_id,url,abstract,search_query,search_topic,retrieved_at,raw_file,initial_relevance,status,notes
```

该候选表的 exact header 字段与本 append plan 计划使用的字段完全一致。本文件不执行任何 CSV 修改。

## 3. Selection policy

本 append plan 的选择策略：

- 优先选择 peer-reviewed papers，且具有稳定 identifiers，例如 DOI、PMID、PMCID、Semantic Scholar ID 或 arXiv ID。
- 优先选择明确对齐以下 axes 的 records：
  - population dynamics / neural manifolds
  - brain-wide / distributed computation
  - multi-area communication
  - causal perturbation
  - model-based inference
- preprints、review / perspective papers、版本状态不清的 records 暂缓，除非它们对 field axis 明显 central。
- 不纳入 generic ML、clinical-only、medical imaging classifier、engineering、physics、machining、nanofluid 或 seismology drift records。
- 本计划只使用 `synthesis/search_run_001_candidate_selection.md` 中的 title-level 信息，不使用 abstracts 或 PDFs。

## 4. Proposed `append_now` records

以下 8 条来自 high-priority group，均为 title-level proposed append rows。`authors`、`abstract` 和部分 provenance 字段在 source 文件中不可得，因此使用占位值。

| source | title | authors | year | venue | doi | pmid | pmcid | arxiv_id | semantic_scholar_id | url | abstract | search_query | search_topic | retrieved_at | raw_file | initial_relevance | status | notes |
|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Semantic Scholar | Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning | unclear_from_review | 2016 | PLoS Comput. Biol. | 10.1371/journal.pcbi.1005175 | 27814352 | 5096671 |  | af1a65fa44773c427235e1f88bf714d64418883f | https://doi.org/10.1371/journal.pcbi.1005175 | not_included_title_level_only | from_search_run_001 | pop_dynamics | 2026-07-01 | unclear_from_review | high | candidate_title_level | representative experimental landmark；population dynamics / neural manifolds；需要人工确认任务、物种、记录尺度和 figure-level evidence。 |
| Semantic Scholar | Preserved neural dynamics across animals performing similar behaviour | unclear_from_review | 2023 | Nature | 10.1038/s41586-023-06714-0 | 37938772 | 10665198 |  | 6c2952e1d99761ae5bc40558905b37875e87a8ab | https://doi.org/10.1038/s41586-023-06714-0 | not_included_title_level_only | from_search_run_001 | pop_dynamics | 2026-07-01 | unclear_from_review | high | candidate_title_level | representative experimental landmark；跨动物 neural dynamics；需要确认是否适合作为 field-level anchor。 |
| Semantic Scholar | Brain-wide dynamics linking sensation to action during decision-making | unclear_from_review | 2024 | Nature | 10.1038/s41586-024-07908-w | 39261727 | 11499283 |  | edb148e6ccc32491a80ff81bc6918258bd6a4d7d | https://doi.org/10.1038/s41586-024-07908-w | not_included_title_level_only | from_search_run_001 | pop_dynamics | 2026-07-01 | unclear_from_review | high | candidate_title_level | representative experimental landmark；brain-wide / distributed computation；需检查是否与其他 decision-making multi-area papers 概念重叠。 |
| Semantic Scholar | Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input | unclear_from_review | 2025 | Nature Communications | 10.1038/s41467-025-66104-0 | 41408036 | 12717177 |  | 1030c1b0db3a8a43b8aaee3fd215340359075bc2 | https://doi.org/10.1038/s41467-025-66104-0 | not_included_title_level_only | from_search_run_001 | brain_wide | 2026-07-01 | unclear_from_review | high | candidate_title_level | representative experimental landmark；brain-wide dynamics 加 single thalamic input activation；具备 causal perturbation angle。 |
| Semantic Scholar | Large-scale high-density brain-wide neural recording in nonhuman primates | unclear_from_review | 2025 | Nature Neuroscience | 10.1038/s41593-025-01976-5 | 40551025 | 12229894 |  | ab37a484708b1832dff24b520120bd8a0e2e64a5 | https://doi.org/10.1038/s41593-025-01976-5 | not_included_title_level_only | from_search_run_001 | brain_wide | 2026-07-01 | unclear_from_review | high | candidate_title_level | representative experimental landmark / method；brain-wide recording scale；需确认是否包含 computation-level results。 |
| Semantic Scholar | Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile | unclear_from_review | 2016 | PNAS | 10.1073/pnas.1616361113 | 27930323 |  |  | 027f3fff0947191976d13bb1ba2a7e95cd8d820e | https://doi.org/10.1073/pnas.1616361113 | not_included_title_level_only | from_search_run_001 | brain_wide | 2026-07-01 | unclear_from_review | high | candidate_title_level | representative experimental landmark；multi-area communication and routing；需要检查实验系统、投射通路和 causal status。 |
| Semantic Scholar | Human brain state dynamics are highly reproducible and associated with neural and behavioral features | unclear_from_review | 2024 | PLoS Biology | 10.1371/journal.pbio.3002808 | 39316635 | 11421804 |  | 8f7f30f53bdbbea2a78c81541e35df7ddbdb361d | https://doi.org/10.1371/journal.pbio.3002808 | not_included_title_level_only | from_search_run_001 | brain_wide | 2026-07-01 | unclear_from_review | high | candidate_title_level | representative experimental paper；human brain state dynamics 与 behavior；需要确认 state 类型与行为解释力度。 |
| Semantic Scholar | Inferring stochastic low-rank recurrent neural networks from neural data | unclear_from_review | 2024 | Neural Information Processing Systems | 10.48550/arXiv.2406.16749 |  |  | 2406.16749 | 579f56813a03517163b86fa89044dc78505bf2cb | https://doi.org/10.48550/arXiv.2406.16749 | not_included_title_level_only | from_search_run_001 | pop_dynamics | 2026-07-01 | unclear_from_review | high | candidate_title_level | theoretical / computational method；model-based inference from neural data；需要确认 method paper、benchmark data 和 survey 方法轴价值。 |

## 5. Proposed `hold_for_manual_check` records

以下 records 暂不建议直接 append，需要人工检查版本、paper type、是否 central，或是否只是方法/平台/perspective。

| Title | Year | Venue | Identifiers | Source search | Hold reason |
|---|---:|---|---|---|---|
| Inferring brain-wide interactions using data-constrained recurrent neural network models | 2020 | bioRxiv (preprint) | DOI: 10.1101/2020.12.18.423348; S2: baca7b0c09335ec73c9dd8d8ac97ea85998b0266 | Semantic Scholar brain_wide | preprint；需要确认是否已有 peer-reviewed version，以及是否使用 real neural data。 |
| Dynamic Models of Neural Population Dynamics | 2024 | bioRxiv (preprint) | DOI: 10.1101/2024.10.04.616750; S2: 0ca7d0a8541404cbcad23fcaa3cb073e691caa81 | Semantic Scholar pop_dynamics | preprint；方法是否成熟、是否有 neural data validation 需要人工确认。 |
| Human striatal population state dynamics | 2026 | bioRxiv (preprint) | DOI: 10.64898/2026.06.17.733040; PMID: 42368010; PMCID: PMC13308143 | PubMed pop_dynamics | preprint；需要确认 human striatal 数据类型、任务和代表性。 |
| Dynamic geometry remapping of neural activity within frontal and subcortical areas during decision-making | 2026 | bioRxiv (preprint) | DOI: 10.64898/2026.06.11.731612; PMID: 42367841; PMCID: PMC13308009 | PubMed brain_wide | preprint；需要确认是否真正 multi-area，以及 geometry remapping 是否有稳定 evidence。 |
| Brain-wide organization of intrinsic timescales at single-neuron resolution | 2025 | bioRxiv (preprint) | DOI: 10.1101/2025.08.30.673281; PMID: 40909563; PMCID: 12407892; S2: d1c718dfe8bb50c99eb83fd74e3cf4a167a313da | Semantic Scholar brain_wide | preprint；需要判断是 descriptive atlas-style paper 还是支持 computation-level claims。 |
| Biologically plausible models of cognitive flexibility: merging recurrent neural networks with full-brain dynamics | 2024 | Current Opinion in Behavioral Sciences | DOI: 10.1016/j.cobeha.2024.101351; S2: 2a5be09341f9c20885131ac4360edb231e95b435 | Semantic Scholar brain_wide | review/perspective；适合组织 field axes，但不应作为 primary experimental evidence。 |
| Arousal as a universal embedding for spatiotemporal brain dynamics | 2025 | Nature | DOI: 10.1038/s41586-025-09544-4; PMID: 40993399; PMCID: 12611781; S2: dbd6546505d7fa729f1cfabfa8a17bb68375d05f | Semantic Scholar brain_wide | peer-reviewed 但需人工判断 arousal 是核心 field axis、global state variable，还是主要 confound/control dimension。 |

## 6. Explicit exclusions

以下 drift examples 不应进入本轮 append：

- `Modelling and computational optimization of different neural network architectures for prediction of depth of cut in abrasive water jet machining of Ti6Al4V.`：machining / engineering neural network application。
- `High-rate phase association with travel time neural fields.`：candidate selection 判断可能是 seismology/geophysics drift。
- `Physics-informed neural network analysis of kerosene-based penta-hybrid nanofluid flow and heat transfer.`：nanofluid physics / engineering drift。
- `Manifold Regularized Dynamic Network Pruning`：deep learning pruning，不是 neuroscience。
- `Neural Garment Dynamics via Manifold-Aware Transformers`：computer graphics / garment simulation。
- `Deep learning to discover and predict dynamics on an inertial manifold`：physics/dynamics ML，不是 neural data 或 brain computation。

## 7. Deduplication checks needed before actual append

实际 append 前必须检查：

- DOI
- PMID
- PMCID
- arXiv ID
- Semantic Scholar ID
- normalized title/year

还需要特别检查：

- `Brain-wide dynamics linking sensation to action during decision-making` 与其他 decision-making / multi-area dynamics records 是否只是概念相近，还是存在版本/预印本关系。
- `Inferring stochastic low-rank recurrent neural networks from neural data` 与 held preprint `Inferring brain-wide interactions using data-constrained recurrent neural network models` 是否属于同一 method axis 下的互补 records，而不是重复 records。
- `candidate_papers.csv` 的当前 header 与本 plan 字段完全一致。

## 8. Exact next action

人工批准后，后续应在一个单独步骤中，仅把获批的 `append_now` rows 追加到 `tables/candidate_papers.csv`。

不要现在 append。  
不要在本步骤修改任何 CSV。  
不要生成 notes、下载 PDFs 或更新 `confirmed_papers.csv`。
