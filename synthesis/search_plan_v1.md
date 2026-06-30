# Search Plan v1

## 1. Purpose

本文件用于在正式运行 PubMed / Semantic Scholar / arXiv 搜索前，先定义一个受控、可复查的 field-first 文献检索计划。

本 survey 的目标是为 systems neuroscience 和 computational neuroscience 建立结构化证据库，而不是从 PFC-first、working-memory-first 或 subspace-first 的预设方向出发。PFC / WM / subspace 相关文献可以作为后续 case study 纳入，但不作为第一轮检索的中心。

第一轮搜索应优先覆盖 field-level axes、代表性实验论文、理论/计算方法论文，以及能帮助评估研究问题和建模机会的核心文献。

## 2. Current Seed Papers

| seed paper | role in survey | main relevance |
|---|---|---|
| Vyas 2020, Computation Through Neural Population Dynamics | review / perspective | population dynamics; computation through dynamics; dynamical systems framing for neural population activity |
| Ye 2026, Brain-wide topographic coordination of rotating waves | experimental landmark | brain-wide rotating waves; distributed dynamics; cortex-subcortex coordination; structural constraints on mesoscale activity |

这两个 seed papers 只用于校准搜索范围和字段结构，不应把整个 survey 锁定到 motor cortex、rotating waves、PFC、working memory 或任何单一机制。

## 3. Field Axes

1. population dynamics / neural manifolds
2. brain-wide / distributed computation
3. multi-area communication / routing
4. causal perturbation / intervention
5. interpretable trained models / NeuroAI
6. PFC / WM / subspace as possible case study

## 4. Search Sources

- PubMed: 用于 neuroscience、experimental systems、review / perspective、causal perturbation 和 biologically grounded papers。
- Semantic Scholar: 用于跨 neuroscience、machine learning、computational modeling 的广义覆盖，并辅助发现高引用/相关论文。
- arXiv: 用于 recent computational neuroscience、NeuroAI、interpretable trained models、machine learning methods；不应作为实验 neuroscience 的唯一证据来源。
- Zotero / `references.bib`: 作为本地 confirmed citation database，用于校验已确认论文、Better BibTeX citekey、DOI 和本地 PDF 路径。

## 5. Query Plan

| field axis | PubMed query | Semantic Scholar query | arXiv query if appropriate | expected paper type | max-results first pass |
|---|---|---|---|---|---|
| population dynamics / neural manifolds | `("neural population dynamics" OR "population dynamics") AND (neuroscience OR cortex OR "neural manifolds")` | `"neural population dynamics" "neural manifolds" computation dynamics` | `all:"neural population dynamics" AND all:"neural manifolds"` | field-level reviews / perspectives; experimental landmarks; computational methods | 20-30 per source |
| brain-wide / distributed computation | `("brain-wide" OR "whole-brain" OR "distributed computation") AND (neural activity OR neural dynamics OR systems neuroscience)` | `"brain-wide" "distributed computation" neural dynamics` | `all:"brain-wide" AND all:"neural dynamics"` | representative experimental landmarks; methods for large-scale recording / analysis | 20-30 per source |
| multi-area communication / routing | `("multi-area" OR "inter-areal" OR "cortical communication" OR routing) AND (neural population OR neural dynamics)` | `"multi-area communication" routing neural populations cortical` | `all:"multi-area" AND all:"communication" AND all:"neural"` | experimental papers; theory papers; communication subspace / routing methods | 20-30 per source |
| causal perturbation / intervention | `(optogenetic OR microstimulation OR perturbation OR intervention) AND ("population dynamics" OR "neural dynamics" OR "neural manifold")` | `causal perturbation intervention neural population dynamics optogenetic microstimulation` | `all:"causal perturbation" AND all:"neural dynamics"` | perturbational experimental papers; model-based intervention papers | 20-30 per source |
| interpretable trained models / NeuroAI | `("recurrent neural network" OR "trained models" OR "deep learning") AND (neuroscience OR neural dynamics) AND (interpretable OR interpretation)` | `"interpretable" "trained models" NeuroAI neural dynamics recurrent neural network` | `all:"interpretable" AND all:"neural dynamics" AND (all:"RNN" OR all:"recurrent neural network" OR all:"NeuroAI")` | theoretical / computational method papers; model interpretation papers | 20-30 per source |
| PFC / WM / subspace as possible case study | `("prefrontal cortex" OR PFC OR "working memory") AND (subspace OR manifold OR "population dynamics" OR "neural dynamics")` | `"prefrontal cortex" "working memory" subspace population dynamics` | `all:"working memory" AND all:"population dynamics" AND (all:"subspace" OR all:"manifold")` | case-study papers; representative experimental papers; modeling papers | 20-30 per source |

第一轮 query 的目标是评估检索质量，而不是穷尽领域。若某个 axis 返回结果明显偏离 systems/computational neuroscience，应先调整 query，再扩大结果数。

## 6. Inclusion Criteria

纳入候选论文应至少满足以下之一：

- representative experimental landmarks，能作为某个 field axis 的实验证据支点。
- field-level reviews / perspectives，能帮助界定研究轴、概念框架或文献地图。
- theoretical or computational method papers，能提供分析、建模、解释或干预框架。
- 明确连接 neural dynamics、brain-wide coordination、population geometry、causal perturbation 或 interpretable models。
- 提供可追踪 metadata，优先包括 DOI、PMID、PMCID、arXiv ID 或 Semantic Scholar ID。

## 7. Exclusion Criteria

排除或暂缓处理以下论文：

- 只与 neural dynamics 或 systems/computational neuroscience 弱相关。
- 纯临床研究，且缺少 mechanistic neural population analysis。
- 纯 machine learning 论文，且没有明确 neuroscience relevance。
- 与已有候选论文高度重复，除非它是 canonical paper、关键方法论文或重要 review。
- metadata 无法核验，且没有可用 stable identifier。

## 8. Candidate-to-Confirmed Workflow

1. API search result -> `tables/candidate_papers.csv`
   - 保存原始 metadata、source、query、retrieved_at 和初筛备注。
2. human screening -> `tables/confirmed_papers.csv`
   - 只将通过人工筛选且 metadata 可核验的论文标记为 confirmed。
3. PDF extraction -> `notes/`
   - 对核心论文优先使用本地 PDF 和 `papers/extracted_text/`，生成 paper-level notes。
4. structured extraction -> `tables/paper_matrix.csv` and `tables/figure_evidence_table.csv`
   - 将论文映射到 field axes、neural object、computation、causal status、modeling opportunity 和 figure-level evidence。

## 9. First-Pass Limits

- 第一轮 formal search 应保持小规模，用于验证 query 质量和筛选规则。
- 每个 source / axis 的 `max-results` 设为 20-30。
- 在审查搜索质量前，不处理超过 10 篇 candidate papers。
- 如果某个 axis 的结果过宽、过窄或明显偏题，应先记录问题并调整 query，而不是继续批量处理。

## 10. Open Risks

- search term drift: query 可能从 field-level axis 漂移到单一任务、脑区或方法。
- overfitting to current seed papers: 可能过度围绕 Vyas 2020 的 population dynamics 或 Ye 2026 的 rotating waves。
- missing canonical older papers: API 排序可能偏向近期或高可见度论文，遗漏经典早期文献。
- over-reliance on recent API results: recent papers 可能尚未形成稳定引用网络或领域共识。
- metadata inconsistency: DOI、PMID、arXiv ID、Semantic Scholar ID、title capitalization 和 author lists 可能在不同 sources 间不一致。
- ambiguity between Zotero item key and Better BibTeX citekey: `references.bib` 的 BibTeX key 可用于本地引用，但不一定等同 Zotero internal item key 或 collection 信息。

