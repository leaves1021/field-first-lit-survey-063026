# Search Run 001 Candidate Selection

## 1. Purpose

本文件基于 `synthesis/search_run_001_review.md`，提出 Search Run 001 的第一批受控候选论文，供人工 review 后再决定是否追加到 `tables/candidate_papers.csv`。

本文件不选择 confirmed papers，不修改任何 CSV，不生成 notes，不下载 PDFs。这里的候选只是 title-level proposal。

## 2. Source and limitations

唯一信息源：`synthesis/search_run_001_review.md`。

限制：

- 本选择仅基于 title-level review、venue、year、identifiers、source search、label 和简短 reason。
- 没有读取 raw JSON/XML。
- 没有读取 full abstracts。
- 没有进行 full PDF 或 abstract-based confirmation。
- preprint 允许进入候选，但在 venue/category 中明确标记。
- 本文件适合 commit 到 GitHub：不包含 API keys、full abstracts、raw JSON/XML 或长文本摘录。

## 3. Proposed high-priority candidates

| # | Title | Year | Venue | Identifiers | Source search | Proposed category | Field axis | Reason for inclusion | Uncertainty |
|---:|---|---:|---|---|---|---|---|---|---|
| 1 | Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning | 2016 | PLoS Comput. Biol. | DOI: 10.1371/journal.pcbi.1005175; PMID: 27814352; PMCID: 5096671; S2: af1a65fa44773c427235e1f88bf714d64418883f | Semantic Scholar pop_dynamics | representative experimental landmark | population dynamics / neural manifolds | review 中标为 `likely_relevant`，并被描述为典型 population dynamics landmark-style paper。 | 需要后续确认具体任务、物种、记录尺度和 figure-level evidence。 |
| 2 | Preserved neural dynamics across animals performing similar behaviour | 2023 | Nature | DOI: 10.1038/s41586-023-06714-0; PMID: 37938772; PMCID: 10665198; S2: 6c2952e1d99761ae5bc40558905b37875e87a8ab | Semantic Scholar pop_dynamics | representative experimental landmark | population dynamics / neural manifolds | review 标为 `likely_relevant`，理由是跨动物 neural dynamics，高优先级。 | 需要确认跨动物一致性的分析对象和是否适合作为 field-level anchor。 |
| 3 | Brain-wide dynamics linking sensation to action during decision-making | 2024 | Nature | DOI: 10.1038/s41586-024-07908-w; PMID: 39261727; PMCID: 11499283; S2: edb148e6ccc32491a80ff81bc6918258bd6a4d7d | Semantic Scholar pop_dynamics | representative experimental landmark | brain-wide / distributed computation | review 标为 `likely_relevant`，直接对应 brain-wide dynamics 与 decision-making。 | 需要检查是否与 Semantic Scholar brain_wide 结果中的其他 brain-wide decision papers 概念重叠。 |
| 4 | Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input | 2025 | Nature Communications | DOI: 10.1038/s41467-025-66104-0; PMID: 41408036; PMCID: 12717177; S2: 1030c1b0db3a8a43b8aaee3fd215340359075bc2 | Semantic Scholar brain_wide | representative experimental landmark | brain-wide / distributed computation; causal perturbation | review 标为 `likely_relevant`，明确包含 brain-wide dynamics 和 single input activation，具备 causal angle。 | 需要后续确认 perturbation 类型、因果解释强度和结果图。 |
| 5 | Large-scale high-density brain-wide neural recording in nonhuman primates | 2025 | Nature Neuroscience | DOI: 10.1038/s41593-025-01976-5; PMID: 40551025; PMCID: 12229894; S2: ab37a484708b1832dff24b520120bd8a0e2e64a5 | Semantic Scholar brain_wide | representative experimental landmark / method | brain-wide / distributed computation | review 标为 `likely_relevant`，是 brain-wide recording scale 的 method/landmark 候选。 | 可能更偏技术平台，需要确认是否包含 computation-level results。 |
| 6 | Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile | 2016 | PNAS | DOI: 10.1073/pnas.1616361113; PMID: 27930323; S2: 027f3fff0947191976d13bb1ba2a7e95cd8d820e | Semantic Scholar brain_wide | representative experimental landmark | multi-area communication and routing | review 标为 `likely_relevant`，直接涉及 long-range projections 与 distributed brain-wide activity。 | 需要检查实验系统、投射通路和 causal status。 |
| 7 | Human brain state dynamics are highly reproducible and associated with neural and behavioral features | 2024 | PLoS Biology | DOI: 10.1371/journal.pbio.3002808; PMID: 39316635; PMCID: 11421804; S2: 8f7f30f53bdbbea2a78c81541e35df7ddbdb361d | Semantic Scholar brain_wide | representative experimental paper | brain-wide / distributed computation | review 标为 `likely_relevant`，理由是 human brain state dynamics 与 behavior 相关。 | 需要确认是 resting-state、task-state 还是 mixed，并判断行为解释力度。 |
| 8 | Arousal as a universal embedding for spatiotemporal brain dynamics | 2025 | Nature | DOI: 10.1038/s41586-025-09544-4; PMID: 40993399; PMCID: 12611781; S2: dbd6546505d7fa729f1cfabfa8a17bb68375d05f | Semantic Scholar brain_wide | representative experimental landmark | brain-wide / distributed computation | review 标为 `likely_relevant`，涉及 spatiotemporal brain dynamics 与 global state variable。 | 需要人工确认 arousal 是否是目标 survey 的核心 axis 还是 confound/control dimension。 |
| 9 | Inferring brain-wide interactions using data-constrained recurrent neural network models | 2020 | bioRxiv (preprint) | DOI: 10.1101/2020.12.18.423348; S2: baca7b0c09335ec73c9dd8d8ac97ea85998b0266 | Semantic Scholar brain_wide | theoretical / computational method | brain-wide / distributed computation; model-based inference | review 标为 `likely_relevant`，直接是 brain-wide interaction inference with RNN models。 | preprint；需要确认是否已有 peer-reviewed version，以及是否使用 real neural data。 |
| 10 | Inferring stochastic low-rank recurrent neural networks from neural data | 2024 | Neural Information Processing Systems | DOI: 10.48550/arXiv.2406.16749; arXiv: 2406.16749; S2: 579f56813a03517163b86fa89044dc78505bf2cb | Semantic Scholar pop_dynamics | theoretical / computational method | population dynamics / neural manifolds; model-based inference | review 标为 `likely_relevant`，理由是从 neural data 推断 model，符合 computational neuroscience。 | 需要确认是否是 method paper、benchmark data 类型，以及是否支持 field-first survey 的方法轴。 |

## 4. Proposed maybe-priority candidates

| # | Title | Year | Venue | Identifiers | Source search | Proposed category | Field axis | Reason for inclusion | Uncertainty |
|---:|---|---:|---|---|---|---|---|---|---|
| 1 | Dynamic Models of Neural Population Dynamics | 2024 | bioRxiv (preprint) | DOI: 10.1101/2024.10.04.616750; S2: 0ca7d0a8541404cbcad23fcaa3cb073e691caa81 | Semantic Scholar pop_dynamics | theoretical / computational method | population dynamics / neural manifolds | review 标为 `likely_relevant`，直接是 neural population dynamics 方法论文。 | preprint；需要确认方法是否成熟、是否有 neural data validation。 |
| 2 | Human striatal population state dynamics | 2026 | bioRxiv (preprint) | DOI: 10.64898/2026.06.17.733040; PMID: 42368010; PMCID: PMC13308143 | PubMed pop_dynamics | representative experimental paper | population dynamics / neural manifolds | review 标为 `likely_relevant`，直接指向 human population state dynamics。 | preprint；需要确认 human striatal 数据类型、任务和分析是否足够代表 field axis。 |
| 3 | Dynamic geometry remapping of neural activity within frontal and subcortical areas during decision-making | 2026 | bioRxiv (preprint) | DOI: 10.64898/2026.06.11.731612; PMID: 42367841; PMCID: PMC13308009 | PubMed brain_wide | representative experimental paper | multi-area dynamics; flexible behavior and cognitive control | review 标为 `likely_relevant`，涉及 decision-making 中的 multi-area neural geometry。 | preprint；需要确认是否真正 multi-area，以及 geometry remapping 是否有稳定 figure-level evidence。 |
| 4 | Brain-wide organization of intrinsic timescales at single-neuron resolution | 2025 | bioRxiv (preprint) | DOI: 10.1101/2025.08.30.673281; PMID: 40909563; PMCID: 12407892; S2: d1c718dfe8bb50c99eb83fd74e3cf4a167a313da | Semantic Scholar brain_wide | representative experimental paper / method | brain-wide / distributed computation | review 标为 `likely_relevant`，涉及 brain-wide timescales 与 single-neuron resolution。 | preprint；需要确认是否是 descriptive atlas-style paper，还是能支持 computation-level claims。 |
| 5 | Biologically plausible models of cognitive flexibility: merging recurrent neural networks with full-brain dynamics | 2024 | Current Opinion in Behavioral Sciences | DOI: 10.1016/j.cobeha.2024.101351; S2: 2a5be09341f9c20885131ac4360edb231e95b435 | Semantic Scholar brain_wide | field-level review / perspective | NeuroAI and interpretable trained models; brain-wide / distributed computation | review 标为 `likely_relevant`，是 RNN 与 full-brain dynamics 的 review/modeling bridge。 | review/perspective 不能作为 primary experimental evidence，但适合帮助组织 field axes。 |

## 5. Excluded examples and why

以下 examples 不是完整排除清单，只是代表性 drift 类型，用于后续 query 修订和人工筛选时保持警觉。

| Title | Source search | Review label | Why excluded |
|---|---|---|---|
| Modelling and computational optimization of different neural network architectures for prediction of depth of cut in abrasive water jet machining of Ti6Al4V. | PubMed brain_wide | likely_exclude | machining / engineering neural network application，不是 neuroscience。 |
| High-rate phase association with travel time neural fields. | PubMed brain_wide | likely_exclude | review 判断可能是 seismology/geophysics，`neural fields` 更像 ML 方法词。 |
| Physics-informed neural network analysis of kerosene-based penta-hybrid nanofluid flow and heat transfer. | PubMed brain_wide | likely_exclude | nanofluid physics with neural networks，属于 physics/engineering drift。 |
| Manifold Regularized Dynamic Network Pruning | arXiv pop_dynamics | likely_exclude | deep learning pruning，不是 neuroscience。 |
| Neural Garment Dynamics via Manifold-Aware Transformers | arXiv pop_dynamics | likely_exclude | computer graphics/garment simulation，是 arXiv manifold/neural keyword drift。 |
| Deep learning to discover and predict dynamics on an inertial manifold | arXiv pop_dynamics | likely_exclude | physics/dynamics ML，不是 neural data 或 brain computation。 |

## 6. Deduplication notes

- `Brain-wide dynamics linking sensation to action during decision-making` 与 `Dynamic geometry remapping of neural activity within frontal and subcortical areas during decision-making` 都涉及 decision-making 和 distributed/multi-area dynamics，但 identifiers 不同；可能是概念重叠，不应自动合并。
- `Inferring brain-wide interactions using data-constrained recurrent neural network models` 与 `Inferring stochastic low-rank recurrent neural networks from neural data` 都是 model-based inference / RNN 方法方向，但一个是 brain-wide interactions，一个是 stochastic low-rank RNN inference；需要人工判断是否属于同一方法轴下的互补候选。
- `Dynamic Models of Neural Population Dynamics`、`Neural Population Dynamics during Reaching...`、`Preserved neural dynamics across animals...` 都落在 population dynamics 轴，但类型不同：method、landmark-style experimental、cross-animal experimental。
- `Large-scale high-density brain-wide neural recording in nonhuman primates` 和 `Brain-wide organization of intrinsic timescales at single-neuron resolution` 都偏 brain-wide measurement scale；一个可能是平台/技术 landmark，一个可能是 timescale organization result，后续应避免把技术贡献和 computational finding 混为一类。
- `Biologically plausible models of cognitive flexibility...` 是 review/perspective，不应与 primary experimental papers 合并，也不应作为 figure-level experimental evidence。

## 7. Recommendation

建议人工优先检查以下 candidates：

1. `Brain-wide dynamics linking sensation to action during decision-making`
2. `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
3. `Preserved neural dynamics across animals performing similar behaviour`
4. `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input`
5. `Inferring brain-wide interactions using data-constrained recurrent neural network models`

推荐流程：

- 先人工检查 high-priority group 的 identifiers、版本状态、paper type 和是否有 full PDF。
- 再检查 maybe-priority group 中的 preprints，决定是否进入 candidate table。
- `tables/candidate_papers.csv` 可以在后续单独步骤中更新，但不应在本文件创建时自动更新。
- append 前应先做 DOI、PMID、PMCID、arXiv ID、Semantic Scholar ID、title/year 的 dedup。

## 8. What not to do yet

- 不要生成 paper-level notes。
- 不要下载 PDFs。
- 不要更新 `tables/confirmed_papers.csv`。
- 不要更新 `tables/candidate_papers.csv`。
- 不要更新 `tables/paper_matrix.csv` 或 `tables/figure_evidence_table.csv`。
- 不要把任何 candidate 视为 confirmed paper。
