# Search Run 001 Review

本文件是 Search Run 001 的 sanitized review packet，基于本地已生成的 CSV、raw 输出和相关日志整理。未读取或复制 full abstracts、raw JSON/XML 正文或 API key；本 review 仅做 title-level 初筛与 query 质量诊断，不选择 confirmed papers，也不向 `tables/candidate_papers.csv` 追加任何记录。

## 1. Run status summary

| Search | Status | Records | Notes |
|---|---:|---:|---|
| PubMed pop_dynamics | succeeded | 20 | 生成 raw XML 与 per-search CSV；结果混入明显 clinical、genetics、cell biology 与弱相关条目。 |
| Semantic Scholar pop_dynamics | retried_successfully | 20 | 初始请求出现 HTTP 429；之后成功生成 raw JSON 与 per-search CSV。结果前半较好，后半有 ML / physics / engineering drift。 |
| arXiv pop_dynamics | succeeded | 20 | 生成 raw XML 与 per-search CSV；结果明显偏向 ML、physics、graphics 与 generic neural network manifold。 |
| PubMed brain_wide | succeeded | 20 | 生成 raw XML 与 per-search CSV；结果漂移严重，包含 machining、seismology、nanofluid、plant disease、drug activity 等非 neuroscience 条目。 |
| Semantic Scholar brain_wide | succeeded | 20 | 生成 raw JSON 与 per-search CSV；整体最贴近 brain-wide / distributed neuroscience，但仍有少量 ML/clinical/engineering drift。 |

PubMed identifier note: PubMed DOI / PMCID parsing 已修复，本 review 中两张 PubMed title-level review 表的 identifiers 已按重新生成的 CSV 同步。

初始失败情况：`logs/semanticscholar_api_error.log` 记录 Semantic Scholar pop_dynamics query 在 2026-07-01 15:15 与 15:35 两次 HTTP 429。  
成功重试情况：同一 search 后续已生成 `data/raw/20260701_search_semanticscholar_pop_dynamics_raw.json` 与 `tables/20260701_search_semanticscholar_pop_dynamics.csv`，说明失败 search 后来重试成功。  
补充日志：`logs/semanticscholar_429_error.log` 记录了一个更早的 Semantic Scholar 429，query 为 `neural population dynamics` 且 limit=3，可能是 API/script smoke test 或早期试跑，不作为 5 个正式输出之一。

## 2. Output files generated

### Raw files under `data/raw/`

- `data/raw/20260701_search_pubmed_pop_dynamics_raw.xml`
- `data/raw/20260701_search_semanticscholar_pop_dynamics_raw.json`
- `data/raw/20260701_search_arxiv_pop_dynamics_raw.xml`
- `data/raw/20260701_search_pubmed_brain_wide_raw.xml`
- `data/raw/20260701_search_semanticscholar_brain_wide_raw.json`

### Per-search CSV files under `tables/`

- `tables/20260701_search_pubmed_pop_dynamics.csv` - 20 records
- `tables/20260701_search_semanticscholar_pop_dynamics.csv` - 20 records
- `tables/20260701_search_arxiv_pop_dynamics.csv` - 20 records
- `tables/20260701_search_pubmed_brain_wide.csv` - 20 records
- `tables/20260701_search_semanticscholar_brain_wide.csv` - 20 records

### Relevant logs under `logs/`

- `logs/semanticscholar_api_error.log` - 与 Search Run 001 的 Semantic Scholar pop_dynamics HTTP 429 初始失败相关，后续已成功重试。
- `logs/semanticscholar_429_error.log` - 记录更早的 Semantic Scholar 429，可能不是最终 5 个正式输出之一。

## 3. Title-level review

Labels 仅基于 title-level 初筛：`likely_relevant`、`borderline` 或 `likely_exclude`。原因说明刻意保持简短，不依赖 full abstract text。

### 3.1 `tables/20260701_search_pubmed_pop_dynamics.csv`

| # | Title | Year | Venue | Identifiers | Label | Reason |
|---:|---|---:|---|---|---|---|
| 1 | Long-term neuron tracking reveals balance of stability and plasticity in functional properties. | 2026 | PloS one | DOI: 10.1371/journal.pone.0321830; PMID: 42371930; PMCID: PMC13313350 | borderline | 神经元长期追踪相关，但 title 未明确 population dynamics。 |
| 2 | Broader autism phenotype, the default mode network, and brain entropy: A network-level hypothesis. | 2026 | Research in neurodiversity | DOI: 10.1016/j.rin.2026.100044; PMID: 42369596; PMCID: PMC13309189 | borderline | 属于 network-level neuroscience，但更像 autism 相关 hypothesis/review。 |
| 3 | Human striatal population state dynamics. | 2026 | bioRxiv | DOI: 10.64898/2026.06.17.733040; PMID: 42368010; PMCID: PMC13308143 | likely_relevant | 直接指向 human population state dynamics。 |
| 4 | Duration-modulated neural population dynamics in humans during BMI controls. | 2026 | Communications biology | DOI: 10.1038/s42003-026-10369-8; PMID: 42362714 | likely_relevant | 明确是 human BMI 行为中的 neural population dynamics。 |
| 5 | Neural and computational correlates of strategic aborting and long-run policy optimization in the dorsolateral prefrontal cortex. | 2026 | Nature communications | DOI: 10.1038/s41467-026-74783-6; PMID: 42362568 | likely_relevant | 结合 computational behavior 与 dlPFC，可作为 case-study 候选。 |
| 6 | Effect of Prenatal Vitamin D and Selenium Supplementation on Minipuberty in Male Offspring of Women with Autoimmune Thyroiditis. | 2026 | Nutrients | DOI: 10.3390/nu18121993; PMID: 42356378; PMCID: PMC13306070 | likely_exclude | 内分泌/营养临床主题，不是 systems neuroscience。 |
| 7 | HyperCOCO: Multi-sensory HyperCOgnitive COmputing for learning population level brain connectivity. | 2026 | Medical image analysis | DOI: 10.1016/j.media.2026.104156; PMID: 42349242 | borderline | 可能是 brain connectivity 的 ML 方法，需看是否有 neuroscience evidence。 |
| 8 | Biological Context-Informed and Population-Stratified Strategies Improve Genetic Diagnosis of CCDC22-Related Disorder. | 2026 | Genetics research | DOI: 10.1155/genr/8137770; PMID: 42339958; PMCID: PMC13292020 | likely_exclude | genetic diagnosis，不是 neural population dynamics。 |
| 9 | A ratiometric fluorescent reporter of mitochondrial sodium. | 2026 | Nature chemical biology | DOI: 10.1038/s41589-026-02253-7; PMID: 42332021 | likely_exclude | 分子/细胞工具方向，不是 population-level neural computation。 |
| 10 | Intrinsic chaos control in cortical circuits: A minimal E-I-M rate model for primary visual cortex. | 2026 | Journal of computational neuroscience | DOI: 10.1007/s10827-026-00938-5; PMID: 42329571 | likely_relevant | cortical circuit dynamics model，直接相关 computational neuroscience。 |
| 11 | Tuft dendrite spikes are accompanied by selective input from distinct functional networks. | 2026 | bioRxiv | DOI: 10.64898/2026.06.10.731464; PMID: 42327257; PMCID: PMC13277889 | borderline | 神经 circuit/network 机制相关，但 dendritic focus 可能低于 field-axis 尺度。 |
| 12 | Evaluating the play fighting of rats: A sociological perspective. | 2026 | Journal of neuroscience methods | DOI: 10.1016/j.jneumeth.2026.110836; PMID: 42323137 | likely_exclude | 行为方法为主，title 无明确 neural population evidence。 |
| 13 | The progesterone to estradiol ratio predicts fear extinction in mice and humans. | 2026 | Neurobiology of stress | DOI: 10.1016/j.ynstr.2026.100823; PMID: 42318369; PMCID: PMC13273471 | likely_exclude | 内分泌/压力行为方向，title 无 population dynamics 信号。 |
| 14 | Inhibitory cell type heterogeneity in a spatially structured mean-field model of V1. | 2026 | Physical review. E | DOI: 10.1103/hmyq-c1j2; PMID: 42316620 | likely_relevant | V1 mean-field model 和 cell-type dynamics 相关。 |
| 15 | Understanding Motor Adaptation in the Transition to Sustained Pain: Protocol for a Longitudinal Experimental Study. | 2026 | JMIR research protocols | DOI: 10.2196/99833; PMID: 42313885; PMCID: PMC13277826 | likely_exclude | 研究 protocol 和 pain adaptation，缺少 neural population/manifold focus。 |
| 16 | Clinical correlates and cognitive associations of the neutrophil-to-lymphocyte ratio in first-episode psychosis and at-risk mental states. | 2026 | Frontiers in psychiatry | DOI: 10.3389/fpsyt.2026.1838805; PMID: 42311571; PMCID: PMC13270933 | likely_exclude | 临床 biomarker psychiatry，不是目标 neural mechanism。 |
| 17 | Real-world effectiveness of antipsychotic treatment of functional outcomes over 10 years: A national cohort of patients in Denmark with schizophrenia. | 2026 | Psychological medicine | DOI: 10.1017/S0033291726104693; PMID: 42307260; PMCID: PMC13280698 | likely_exclude | 临床治疗 cohort，不是 neural dynamics。 |
| 18 | Fear prioritizes feedforward sensory coding at the expense of contextual processing in monkey V1. | 2026 | Neuroreport | DOI: 10.1097/WNR.0000000000002287; PMID: 42306915 | likely_relevant | monkey V1 coding 与 context modulation 符合 systems neuroscience。 |
| 19 | Characterization of Pestivirus scrofae infection in the tissues of a persistently infected boar. | 2026 | Porcine health management | DOI: 10.1186/s40813-026-00514-4; PMID: 42304515; PMCID: PMC13282871 | likely_exclude | 兽医 virology，主题无关。 |
| 20 | Neural peer pressure: intercellular dynamics and emergent phenotypes in the mosaic Rett syndrome brain. | 2026 | Cell communication and signaling | DOI: 10.1186/s12964-026-02987-w; PMID: 42304351 | borderline | brain disease 与 intercellular dynamics 相关，但可能偏 cellular/developmental。 |

### 3.2 `tables/20260701_search_semanticscholar_pop_dynamics.csv`

| # | Title | Year | Venue | Identifiers | Label | Reason |
|---:|---|---:|---|---|---|---|
| 1 | Dynamic Models of Neural Population Dynamics | 2024 | bioRxiv | DOI: 10.1101/2024.10.04.616750; S2: 0ca7d0a8541404cbcad23fcaa3cb073e691caa81 | likely_relevant | 直接是 neural population dynamics 方法论文。 |
| 2 | Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning | 2016 | PLoS Comput. Biol. | DOI: 10.1371/journal.pcbi.1005175; PMID: 27814352; PMCID: 5096671; S2: af1a65fa44773c427235e1f88bf714d64418883f | likely_relevant | 典型 population dynamics landmark-style paper。 |
| 3 | Preserved Neural Dynamics across Arm and Brain-controlled Movements | 2025 | bioRxiv | DOI: 10.1101/2025.11.27.691057; S2: 3b8bf48f059ea6b39b18e4097e846b13c70058f6 | likely_relevant | 比较 movement/control 条件下的 neural dynamics。 |
| 4 | Neural Manifold Decoder for Acupuncture Stimulations With Representation Learning: An Acupuncture-Brain Interface | 2025 | IEEE journal of biomedical and health informatics | DOI: 10.1109/JBHI.2025.3530922; PMID: 40031188; S2: 5413654a1b8540abe3c6cd7c70c8751772125add | borderline | 含 neural manifold/decoder，但 biomedical interface 范围可能较窄。 |
| 5 | Preserved neural dynamics across animals performing similar behaviour | 2023 | Nature | DOI: 10.1038/s41586-023-06714-0; PMID: 37938772; PMCID: 10665198; S2: 6c2952e1d99761ae5bc40558905b37875e87a8ab | likely_relevant | 跨动物 neural dynamics，高优先级。 |
| 6 | Low Tensor Rank Learning of Neural Dynamics | 2023 | Neural Information Processing Systems | DOI: 10.48550/arXiv.2308.11567; arXiv: 2308.11567; S2: 49d720873b5f793a13564a5777ab88152febb9f1 | borderline | computational method，需确认是 neural data 还是 generic ML。 |
| 7 | Spiking, Bursting, and Population Dynamics in a Network of Growth Transform Neurons | 2018 | IEEE Transactions on Neural Networks and Learning Systems | DOI: 10.1109/TNNLS.2017.2695171; PMID: 28463206; S2: 22ebd2f5b2b6df07b10296cea36c2d5089af5458 | borderline | 可能偏 artificial/neural-network dynamics，方法性较强。 |
| 8 | Brain-wide dynamics linking sensation to action during decision-making | 2024 | Nature | DOI: 10.1038/s41586-024-07908-w; PMID: 39261727; PMCID: 11499283; S2: edb148e6ccc32491a80ff81bc6918258bd6a4d7d | likely_relevant | 直接是 brain-wide dynamics 与 decision-making。 |
| 9 | Analyzing Populations of Neural Networks via Dynamical Model Embedding | 2023 | arXiv.org | DOI: 10.48550/arXiv.2302.14078; arXiv: 2302.14078; S2: 7f533196dd6ea1a1bf1ef66f24847dad77fc37f9 | likely_exclude | 研究 artificial neural networks 的 populations，不是 neuroscience。 |
| 10 | A Comparison of Neural Decoding Methods and Population Coding Across Thalamo-Cortical Head Direction Cells | 2019 | Front. Neural Circuits | DOI: 10.3389/fncir.2019.00075; PMID: 31920565; PMCID: 6914739; S2: a2f349f9f09db4ae0d4939d269c6362b7ec56750 | likely_relevant | population coding 与 thalamo-cortical circuits 相关。 |
| 11 | Energy-Performance Assessment of Oscillatory Neural Networks Based on VO2 Devices for Future Edge AI Computing | 2023 | IEEE Transactions on Neural Networks and Learning Systems | DOI: 10.1109/TNNLS.2023.3238473; PMID: 37022082; S2: 856f7599062e584c4acc02772d565dd875d31e1b | likely_exclude | hardware/edge AI，不是 biological neuroscience。 |
| 12 | Inference on the Macroscopic Dynamics of Spiking Neurons | 2024 | Neural Computation | DOI: 10.1162/neco_a_01701; PMID: 39141813; S2: f78f30eaccd812e4f928be9349086e2efeb5ba12 | likely_relevant | spiking population dynamics inference method。 |
| 13 | Quantum Many-Body Dynamics in Two Dimensions with Artificial Neural Networks. | 2019 | Physical Review Letters | DOI: 10.1103/PHYSREVLETT.125.100503; PMID: 32955321; arXiv: 1912.08828; S2: 86a58d70781cce4973334ec5db2a4e79e12f92e6 | likely_exclude | physics 主题，使用 artificial neural networks。 |
| 14 | Inferring stochastic low-rank recurrent neural networks from neural data | 2024 | Neural Information Processing Systems | DOI: 10.48550/arXiv.2406.16749; arXiv: 2406.16749; S2: 579f56813a03517163b86fa89044dc78505bf2cb | likely_relevant | 从 neural data 推断 model，符合 computational neuroscience。 |
| 15 | A machine learning approach to simulate flexible body dynamics | 2025 | Multibody system dynamics | DOI: 10.1007/s11044-024-10049-7; S2: 67af93fabb437cd24a459d0ac4310c385737c2e2 | likely_exclude | mechanical dynamics ML，不是 neuroscience。 |
| 16 | High Fidelity Video Prediction with Large Stochastic Recurrent Neural Networks | 2019 | Neural Information Processing Systems | arXiv: 1911.01655; S2: aec380c44646a7e467cd9f6d78cba301f877734c | likely_exclude | generic ML/video prediction。 |
| 17 | Neural Networks with Dynamic Synapses | 1998 | Neural Computation | DOI: 10.1162/089976698300017502; PMID: 9573407; S2: d96a14d09ce4412c0022f20ebe9427b754182c85 | borderline | 可能是 biologically inspired computational neuroscience，但 title 不够 population-level。 |
| 18 | Mean-Field Langevin Dynamics for Signed Measures via a Bilevel Approach | 2024 | Neural Information Processing Systems | DOI: 10.52202/079017-1109; arXiv: 2406.17054; S2: ad726a314c50ab1a37f7c1adf400a0690757cb2b | likely_exclude | mathematical ML optimization，不是 neuroscience。 |
| 19 | RefreshNet: learning multiscale dynamics through hierarchical refreshing | 2024 | Nonlinear dynamics | DOI: 10.1007/s11071-024-09813-3; arXiv: 2401.13282; S2: 4904fa1aaccb1ed4ab22aef8ef2c1cbc7ee4d974 | likely_exclude | generic ML/nonlinear dynamics。 |
| 20 | Coagulo-Net: Enhancing the Mathematical Modeling of Blood Coagulation using Physics-Informed Neural Networks | 2024 | Neural Networks | DOI: 10.1016/j.neunet.2024.106732; PMID: 39305783; PMCID: 11578045; S2: c7f18857f45241c30df665a94a8b825942aea123 | likely_exclude | biomedical PINN，不是 neural systems。 |

### 3.3 `tables/20260701_search_arxiv_pop_dynamics.csv`

| # | Title | Year | Venue | Identifiers | Label | Reason |
|---:|---|---:|---|---|---|---|
| 1 | A Moving Bump in a Continuous Manifold: A Comprehensive Study of the Tracking Dynamics of Continuous Attractor Neural Networks | 2008 | arXiv | DOI: 10.1162/neco.2009.07-08-824; arXiv: 0808.2341v3 | likely_relevant | continuous attractor neural network dynamics，接近 computational neuroscience。 |
| 2 | Manifold Regularized Dynamic Network Pruning | 2021 | arXiv | arXiv: 2103.05861v1 | likely_exclude | deep learning pruning，不是 neuroscience。 |
| 3 | Simultaneous embedding of multiple attractor manifolds in a recurrent neural network using constrained gradient optimization | 2023 | arXiv | arXiv: 2310.18708v1 | borderline | attractor/RNN 方法，需确认是 neuroscience model 还是 generic ML。 |
| 4 | Neural network approach for the dynamics on the normally hyperbolic invariant manifold of periodically driven systems | 2020 | arXiv | DOI: 10.1103/PhysRevE.101.022219; arXiv: 2002.00478v1 | likely_exclude | physics/dynamical systems 使用 neural networks。 |
| 5 | Neural manifold analysis of brain circuit dynamics in health and disease | 2022 | arXiv | DOI: 10.48550/arXiv.2203.11874; arXiv: 2203.11874v2 | likely_relevant | 直接讨论 neural manifolds 与 brain circuit dynamics。 |
| 6 | ManifoldFormer: Geometric Deep Learning for Neural Dynamics on Riemannian Manifolds | 2025 | arXiv | arXiv: 2511.16828v1 | likely_exclude | geometric deep learning，缺少明确 neuroscience target。 |
| 7 | Learning on Manifolds: Universal Approximations Properties using Geometric Controllability Conditions for Neural ODEs | 2023 | arXiv | arXiv: 2305.08849v1 | likely_exclude | ML theory/neural ODEs，不是 neural data。 |
| 8 | Neural Garment Dynamics via Manifold-Aware Transformers | 2024 | arXiv | DOI: 10.1111/cgf.15028; arXiv: 2407.06101v1 | likely_exclude | computer graphics/garment simulation。 |
| 9 | Learning Manifold and Itô Dynamics with Branched Neural Rough Differential Equations | 2026 | arXiv | arXiv: 2606.05272v1 | likely_exclude | mathematical ML dynamics，不是 neuroscience。 |
| 10 | Drift-Diffusion Matching: Embedding dynamics in latent manifolds of asymmetric neural networks | 2026 | arXiv | arXiv: 2602.14885v2 | likely_exclude | generic artificial neural network method。 |
| 11 | Dynamically Stable Poincaré Embeddings for Neural Manifolds | 2021 | arXiv | arXiv: 2112.11172v2 | likely_exclude | 更像 representation learning phrase match，缺少 biological neuroscience 信号。 |
| 12 | Planning Neural Dynamics with Lie Group Embedding through Supervised Projective Manifold Learning | 2026 | arXiv | arXiv: 2605.26167v1 | likely_exclude | generic ML/planning method，不是 neuroscience。 |
| 13 | The Geometry of Cortical Computation: Manifold Disentanglement and Predictive Dynamics in VCNet | 2025 | arXiv | arXiv: 2508.02995v3 | borderline | cortical computation wording 可能相关，但 VCNet 可能只是 model-only。 |
| 14 | Model Predictive Control on the Neural Manifold | 2024 | arXiv | arXiv: 2406.14801v2 | likely_exclude | control/ML 使用 neural manifold，不是 biological neural population。 |
| 15 | Neural Cellular Automata Manifold | 2020 | arXiv | arXiv: 2006.12155v3 | likely_exclude | artificial neural cellular automata。 |
| 16 | State Space Representations of Deep Neural Networks | 2018 | arXiv | DOI: 10.1162/neco_a_01165; arXiv: 1806.03751v3 | likely_exclude | deep networks analysis，不是 neuroscience evidence。 |
| 17 | Modelling the influence of data structure on learning in neural networks: the hidden manifold model | 2019 | arXiv | DOI: 10.1103/PhysRevX.10.041044; arXiv: 1909.11500v4 | likely_exclude | statistical physics/ML theory。 |
| 18 | Deep learning to discover and predict dynamics on an inertial manifold | 2019 | arXiv | DOI: 10.1103/PhysRevE.101.062209; arXiv: 2001.04263v3 | likely_exclude | physics/dynamics ML。 |
| 19 | Storing overlapping associative memories on latent manifolds in low-rank spiking networks | 2024 | arXiv | arXiv: 2411.17485v2 | likely_relevant | spiking networks、low-rank dynamics、memory/manifold 主题相关。 |
| 20 | Exploring the Enigma of Neural Dynamics Through A Scattering-Transform Mixer Landscape for Riemannian Manifold | 2024 | arXiv | arXiv: 2405.16357v1 | likely_exclude | generic ML/manifold language，缺少 neuroscience 信号。 |

### 3.4 `tables/20260701_search_pubmed_brain_wide.csv`

| # | Title | Year | Venue | Identifiers | Label | Reason |
|---:|---|---:|---|---|---|---|
| 1 | Modelling and computational optimization of different neural network architectures for prediction of depth of cut in abrasive water jet machining of Ti6Al4V. | 2026 | Scientific reports | DOI: 10.1038/s41598-026-54813-5; PMID: 42380377 | likely_exclude | machining/engineering neural network application。 |
| 2 | High-rate phase association with travel time neural fields. | 2026 | Nature communications | DOI: 10.1038/s41467-026-74092-y; PMID: 42380143 | likely_exclude | 可能是 seismology/geophysics，`neural fields` 更像 ML 方法词。 |
| 3 | Whole-brain network dynamics underlying intolerance of uncertainty. | 2026 | NeuroImage | DOI: 10.1016/j.neuroimage.2026.122091; PMID: 42379405 | likely_relevant | 直接是 whole-brain network dynamics。 |
| 4 | Neural mechanisms of mixed speech and grasp representation in sensorimotor cortices. | 2026 | Journal of neural engineering | DOI: 10.1088/1741-2552/ae847b; PMID: 42379192 | borderline | systems neuroscience 相关，但 title 不明确 brain-wide/distributed。 |
| 5 | Whole brain fluorescence imaging in  | 2026 | iScience | DOI: 10.1016/j.isci.2026.116389; PMID: 42375524; PMCID: PMC13311176 | borderline | 含 whole-brain imaging，但 title 截断，需要人工核查。 |
| 6 | The functional neurobiology of dispositions towards negative emotions. | 2026 | Nature communications | DOI: 10.1038/s41467-026-74565-0; PMID: 42373635; PMCID: PMC13315715 | borderline | neurobiology 可能相关，但 field-axis link 不清楚。 |
| 7 | Developing a binary communication protocol between biological neural networks using virtual white matter. | 2026 | Journal of neural engineering | DOI: 10.1088/1741-2552/ae840f; PMID: 42372793 | borderline | biological neural networks 与 communication 相关，但可能是 engineered in vitro。 |
| 8 | Regional inequities in acute stroke care in Norway: a national benchmark for the "stroke action plan for Europe" implementation. | 2026 | European stroke journal | DOI: 10.1093/esj/aakag072; PMID: 42372228; PMCID: PMC13313314 | likely_exclude | health services/clinical care，不是 neural computation。 |
| 9 | The neural mechanisms of aligning spatial perspectives. | 2026 | Cerebral cortex | DOI: 10.1093/cercor/bhag090; PMID: 42372223; PMCID: PMC13313315 | borderline | cognitive neuroscience 相关，但不明显是 brain-wide。 |
| 10 | Lightweight English Text Classification with Deep Learning Based on Complex System Theory. | 2026 | Journal of visualized experiments | DOI: 10.3791/69344; PMID: 42372063 | likely_exclude | NLP/deep learning engineering。 |
| 11 | Physics-informed neural network analysis of kerosene-based penta-hybrid nanofluid flow and heat transfer. | 2026 | Discover nano | DOI: 10.1186/s11671-026-04765-6; PMID: 42371290; PMCID: PMC13315057 | likely_exclude | nanofluid physics with neural networks。 |
| 12 | Self-adaptive forward-forward network for anomaly detection and medical image analysis. | 2026 | Frontiers in radiology | DOI: 10.3389/fradi.2026.1771850; PMID: 42368785; PMCID: PMC13294442 | likely_exclude | medical imaging ML，不是 systems neuroscience。 |
| 13 | Predicting Surfactant Oil-Water Interfacial Tension Using Gated Message-Passing Graph Neural Networks. | 2026 | ACS omega | DOI: 10.1021/acsomega.6c03262; PMID: 42368064; PMCID: PMC13295050 | likely_exclude | chemistry/materials graph neural network。 |
| 14 | DeltaQ: Value-Guided Hebbian Learning in Spiking Neuronal Networks for Multi-Goal Navigation. | 2026 | bioRxiv | DOI: 10.64898/2026.06.12.731882; PMID: 42367984; PMCID: PMC13308139 | borderline | computational spiking model，可能相关 NeuroAI，但不是 brain-wide。 |
| 15 | Dynamic geometry remapping of neural activity within frontal and subcortical areas during decision-making. | 2026 | bioRxiv | DOI: 10.64898/2026.06.11.731612; PMID: 42367841; PMCID: PMC13308009 | likely_relevant | decision-making 中的 multi-area neural geometry。 |
| 16 | DAPR-AM-Net: an end-to-end smart farming system powered by dual-attention progressive refinement and adaptive MixUp for explainable tomato leaf disease classification and forecasting. | 2026 | Plant methods | DOI: 10.1186/s13007-026-01556-z; PMID: 42366369 | likely_exclude | agriculture computer vision。 |
| 17 | Artificial intelligence driven multiphysics analysis of Casson bioconvective ternary nanofluid flow over an inclined needle. | 2026 | Discover nano | DOI: 10.1186/s11671-026-04762-9; PMID: 42364041; PMCID: PMC13310214 | likely_exclude | nanofluid engineering。 |
| 18 | The role of the subcortical structures in subthreshold depression: evidence from static and dynamic functional connectivity. | 2026 | Brain structure & function | DOI: 10.1007/s00429-026-03144-2; PMID: 42362827 | borderline | functional connectivity 与 subcortical structures 相关，但偏 clinical depression。 |
| 19 | Interpretable graph neural networks for predicting drug activity in triple-negative breast cancer using scaffold-based splits. | 2026 | Scientific reports | DOI: 10.1038/s41598-026-58978-x; PMID: 42362709 | likely_exclude | drug discovery graph neural networks。 |
| 20 | Coupled dual-channel memristors for hardware-native trustworthy Bayesian intelligence. | 2026 | Nature communications | DOI: 10.1038/s41467-026-74898-w; PMID: 42362554 | likely_exclude | hardware AI，不是 neuroscience。 |

### 3.5 `tables/20260701_search_semanticscholar_brain_wide.csv`

| # | Title | Year | Venue | Identifiers | Label | Reason |
|---:|---|---:|---|---|---|---|
| 1 | Global motor dynamics - Invariant neural representations of motor behavior in distributed brain-wide recordings | 2023 | bioRxiv | DOI: 10.1088/1741-2552/ad851c; PMID: 39383883; S2: 0c99364df468bf0d39c425a2d76bd56e37f773d1 | likely_relevant | 直接涉及 distributed brain-wide recordings 与 motor dynamics。 |
| 2 | Conserved brain-wide emergence of emotional response from sensory experience in humans and mice | 2025 | Science | DOI: 10.1126/science.adt3971; PMID: 40440375; PMCID: 12286656; S2: 070e70b1925f591602570475994a5774221b3b52 | likely_relevant | 跨物种 brain-wide emotional response。 |
| 3 | Large-scale high-density brain-wide neural recording in nonhuman primates | 2025 | Nature Neuroscience | DOI: 10.1038/s41593-025-01976-5; PMID: 40551025; PMCID: 12229894; S2: ab37a484708b1832dff24b520120bd8a0e2e64a5 | likely_relevant | brain-wide recording scale 的 method/landmark 候选。 |
| 4 | Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input | 2025 | Nature Communications | DOI: 10.1038/s41467-025-66104-0; PMID: 41408036; PMCID: 12717177; S2: 1030c1b0db3a8a43b8aaee3fd215340359075bc2 | likely_relevant | brain-wide dynamics 加 single input activation，具备 causal angle。 |
| 5 | Insular Traveling Waves Link Distributed Neural Dynamics to Human Memory Performance | 2025 | bioRxiv | DOI: 10.1101/2025.09.15.676376; S2: 9e995e426987944b688377c65dfc152b8283a961 | likely_relevant | distributed dynamics 与 human memory performance 关联。 |
| 6 | Link Brain-Wide Projectome to Neuronal Dynamics in the Mouse Brain | 2024 | Neuroscience Bulletin | DOI: 10.1007/s12264-024-01232-z; PMID: 38819707; PMCID: 11607363; S2: 7de58c9289944ad54531d56eae15487e6409142e | likely_relevant | brain-wide projectome 与 neuronal dynamics。 |
| 7 | Brain-wide organization of intrinsic timescales at single-neuron resolution | 2025 | bioRxiv | DOI: 10.1101/2025.08.30.673281; PMID: 40909563; PMCID: 12407892; S2: d1c718dfe8bb50c99eb83fd74e3cf4a167a313da | likely_relevant | brain-wide timescales 与 single-neuron resolution。 |
| 8 | Activity-dependent capture reveals brain-wide signatures of isoflurane anesthesia-induced unconsciousness | 2025 | bioRxiv | DOI: 10.64898/2025.12.02.691631; PMID: 41573848; S2: c8763fb90cb9a5cb24bf1b9447e64a7401301c72 | borderline | 有 brain-wide signatures，但 anesthesia state 可能偏离核心 axes。 |
| 9 | Human brain state dynamics are highly reproducible and associated with neural and behavioral features | 2024 | PLoS Biology | DOI: 10.1371/journal.pbio.3002808; PMID: 39316635; PMCID: 11421804; S2: 8f7f30f53bdbbea2a78c81541e35df7ddbdb361d | likely_relevant | human brain state dynamics 与 behavior 相关。 |
| 10 | Slow and Weak Attractor Computation Embedded in Fast and Strong E-I Balanced Neural Dynamics | 2023 | Neural Information Processing Systems | DOI: 10.52202/075280-0914; S2: 2755117c30b6cb34533679fe1062797b6dcc6039 | borderline | computational dynamics 相关，但不明确 brain-wide。 |
| 11 | Arousal as a universal embedding for spatiotemporal brain dynamics | 2025 | Nature | DOI: 10.1038/s41586-025-09544-4; PMID: 40993399; PMCID: 12611781; S2: dbd6546505d7fa729f1cfabfa8a17bb68375d05f | likely_relevant | spatiotemporal brain dynamics 与 global state variable。 |
| 12 | Maternal experience alters brain-wide representation of infant cries | 2026 | bioRxiv | DOI: 10.64898/2026.06.26.734581; S2: 405f1545c7dcb84290d75a4937a57b9c7c59eeb0 | likely_relevant | brain-wide representation 与 experience-dependent change。 |
| 13 | Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile | 2016 | PNAS | DOI: 10.1073/pnas.1616361113; PMID: 27930323; S2: 027f3fff0947191976d13bb1ba2a7e95cd8d820e | likely_relevant | long-range projections 与 distributed brain-wide activity。 |
| 14 | Toward brain-wide lifetime electrophysiology at single-cell single-spike resolution in mammals via implantable microelectronics | 2026 | Nano Reseach | DOI: 10.26599/nr.2026.94908864; S2: d54637c0bc9d02936e578cf924caac581291967c | borderline | technology/method paper，可能有用但不是 computation evidence。 |
| 15 | Biologically plausible models of cognitive flexibility: merging recurrent neural networks with full-brain dynamics | 2024 | Current Opinion in Behavioral Sciences | DOI: 10.1016/j.cobeha.2024.101351; S2: 2a5be09341f9c20885131ac4360edb231e95b435 | likely_relevant | RNN 与 full-brain dynamics 的 review/modeling bridge。 |
| 16 | Distributed Synaptic Connection Strength Changes Dynamics in a Population Firing Rate Model in Response to Continuous External Stimuli | 2025 | Neural Computation | DOI: 10.1162/neco_a_01749; PMID: 40112143; S2: 4e1909689b1bf7d1d01539e553a627609be02d78 | borderline | population firing-rate model 相关，但不明确 brain-wide。 |
| 17 | MRI-Based Brain Tumor Classification Using a Dilated Parallel Deep Convolutional Neural Network | 2024 | Digit. | DOI: 10.3390/digital4030027; S2: a9a53a7e05c4e5439700a0b93d45cfba54c60568 | likely_exclude | medical imaging classifier。 |
| 18 | TransBrain: A computational framework for translating brain-wide phenotypes between humans and mice | 2025 | bioRxiv | DOI: 10.1038/s41592-025-02961-3; PMID: 41461907; S2: 80624364755fca6db086f4799e3845538adb7207 | likely_relevant | brain-wide phenotype translation 与 computational framework。 |
| 19 | Inferring brain-wide interactions using data-constrained recurrent neural network models | 2020 | bioRxiv | DOI: 10.1101/2020.12.18.423348; S2: baca7b0c09335ec73c9dd8d8ac97ea85998b0266 | likely_relevant | 直接是 brain-wide interaction inference with RNN models。 |
| 20 | Distribution-Allowed Noise-Resistant Neural Dynamics for Constrained Time-Dependent Quadratic Programming With kWTA Application | 2025 | IEEE Transactions on Systems, Man, and Cybernetics: Systems | DOI: 10.1109/TSMC.2025.3547387; S2: 6aba97b71e551fbe95c7cd4418ee3c92a6553ac6 | likely_exclude | optimization/neural dynamics engineering，不是 neuroscience。 |

## 4. Query quality diagnosis

### PubMed pop_dynamics

The query retrieved some useful neural population dynamics and computational neuroscience titles, but it also pulled in clinical, endocrine, genetics, molecular biology, veterinary, and general behavior-methods records. Title-level evidence suggests that broad terms such as `population dynamics`, `neuroscience`, and `cortex` are insufficiently specific in PubMed, and may also interact poorly with PubMed indexing.

Diagnosis: moderate signal, substantial drift. The output is worth manual inspection, but the query should be revised before scaling.

### Semantic Scholar pop_dynamics

This search produced several strong hits on population dynamics, neural manifolds, neural data, and brain-wide decision-making. However, the later results drifted into artificial neural networks, physics, mechanics, video prediction, blood coagulation, and generic ML dynamics. Semantic Scholar appears sensitive to `neural` + `dynamics` as an ML phrase.

Diagnosis: good first-pass signal, but needs manual filtering and a revised query if rerun at larger scale.

### arXiv pop_dynamics

The arXiv results show severe drift into geometric deep learning, physics, graphics, control, deep neural networks, and generic manifold learning. A few computational neuroscience-adjacent items are present, especially attractor/spiking network and neural manifold review titles, but the query is too permissive.

Diagnosis: low precision. This search should be rerun with stronger neuroscience anchors or narrower categories.

### PubMed brain_wide

This is the weakest search. The title list contains many non-neuroscience uses of `neural network`, including machining, seismology, nanofluid flow, text classification, tomato disease classification, drug discovery, and hardware AI. Only a few titles clearly match whole-brain/network dynamics or multi-area neural activity.

Diagnosis: severe drift. The query should be rerun with revised terms that exclude generic artificial neural network records and emphasize brain imaging, neural activity, neural circuits, and systems neuroscience.

### Semantic Scholar brain_wide

This search is the strongest output of Run 001. Most top records are directly related to brain-wide recordings, distributed neural activity, whole-brain dynamics, intrinsic timescales, long-range projections, or cross-species brain-wide phenotypes. Drift is present but limited, mainly generic computational dynamics, medical imaging, and engineering neural dynamics.

Diagnosis: high signal, suitable for manual inspection and deduplication.

## 5. Query-level decision

| Search | Decision | Rationale |
|---|---|---|
| PubMed pop_dynamics | inspect_manually | 有可用记录，但漂移较多，merge 前需要 title-level 人工过滤。 |
| Semantic Scholar pop_dynamics | inspect_manually | signal 较好，但有 429 retry 记录；建议人工筛查后再决定是否精修重跑。 |
| arXiv pop_dynamics | rerun_with_revised_query | 当前 query precision 低，ML/physics/graphics drift 很明显。 |
| PubMed brain_wide | rerun_with_revised_query | generic `neural network` 和宽泛 computation terms 导致严重非 neuroscience drift。 |
| Semantic Scholar brain_wide | keep | 本轮 signal 最强，可进入 manual dedup/screening。 |

## 6. Proposed revised queries

以下只是 proposed query strings；创建本 review 时没有运行任何 search。

### PubMed pop_dynamics

```text
("neural population dynamics"[Title/Abstract] OR "population coding"[Title/Abstract] OR "neural manifold"[Title/Abstract] OR "population activity"[Title/Abstract]) AND (cortex[Title/Abstract] OR cortical[Title/Abstract] OR "neural activity"[Title/Abstract] OR "systems neuroscience"[Title/Abstract]) NOT (clinical[Title/Abstract] OR diagnosis[Title/Abstract] OR vitamin[Title/Abstract] OR genetic[Title/Abstract] OR infection[Title/Abstract])
```

### Semantic Scholar pop_dynamics

```text
"neural population dynamics" OR "neural manifold" OR "population activity" neuroscience cortex behavior
```

Optional stricter variant:

```text
"neural population dynamics" "neural data" behavior cortex
```

### arXiv pop_dynamics

```text
("neural population dynamics" OR "neural manifolds" OR "spiking networks" OR "attractor networks") AND (neuroscience OR cortical OR brain OR neural data)
```

对 arXiv，还应考虑限制 categories，或在后处理中过滤含有 generic ML/physics 词汇的 title，例如 `garment`、`quantum`、`fluid`、`pruning`、`video`、`Poincare embeddings`、`neural ODEs`；除非后续人工检查能确认其明确连接 neuroscience。

### PubMed brain_wide

```text
("brain-wide"[Title/Abstract] OR "whole-brain"[Title/Abstract] OR "distributed neural activity"[Title/Abstract] OR "large-scale neural dynamics"[Title/Abstract]) AND ("neural activity"[Title/Abstract] OR "neural dynamics"[Title/Abstract] OR "brain network"[Title/Abstract] OR "systems neuroscience"[Title/Abstract]) NOT ("neural network"[Title/Abstract] OR "deep learning"[Title/Abstract] OR machining[Title/Abstract] OR nanofluid[Title/Abstract] OR plant[Title/Abstract] OR tumor[Title/Abstract] OR drug[Title/Abstract])
```

### Semantic Scholar brain_wide

```text
"brain-wide" "neural activity" "distributed" "dynamics" neuroscience
```

Optional stricter variant:

```text
"brain-wide recordings" OR "whole-brain dynamics" OR "distributed brain-wide neural activity"
```

## 7. No confirmed papers selected yet

本 review 不选择 confirmed papers。上面的 labels 只是 preliminary title-level triage，不应作为最终纳入决定。

## 8. No append to `candidate_papers.csv`

本 review 不向 `tables/candidate_papers.csv` 追加记录，也不修改任何 screening matrix。候选表应在后续单独的 merge/dedup/screening step 中，根据 stable identifiers 和人工检查结果再填充。

## 9. Recommended next step

1. 先人工检查 Semantic Scholar brain_wide 与 Semantic Scholar pop_dynamics 中的 `likely_relevant` 和高价值 `borderline` records。
2. 按 DOI、PMID、PMCID、arXiv ID、Semantic Scholar ID、title、year 跨 source deduplicate。
3. 只对低 precision 的 search 使用 revised queries 重跑：arXiv pop_dynamics 与 PubMed brain_wide。
4. 人工筛选后，在单独的受控步骤中把 selected records 追加到 `tables/candidate_papers.csv`。
