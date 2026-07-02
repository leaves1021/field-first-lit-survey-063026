# First Batch Reading Note Plan Run001

## 1. Purpose

本文件为 Run001 首批 3 篇已标记为 `ready_for_reading` 的文献制定 full-text reading 与 paper-note generation plan。

这是一个 plan-only 文档。本步骤不创建 notes，不更新任何 CSV，不修改 scripts，不修改 `references.bib`，也不复制论文中的长段原文。

## 2. Scope

本计划覆盖以下 3 篇：

1. `khilkevich2024BrainwideDynamicsLinking`
2. `michaels2016NeuralPopulationDynamics`
3. `safaie2023PreservedNeuralDynamics`

已使用的本地依据：

- `tables/confirmed_papers.csv`
- `synthesis/pdf_download_extraction_results_run001.md`
- `papers/extracted_text/khilkevich2024BrainwideDynamicsLinking.md`
- `papers/extracted_text/michaels2016NeuralPopulationDynamics.md`
- `papers/extracted_text/safaie2023PreservedNeuralDynamics.md`
- `templates/paper_note_template.md`
- `tables/paper_matrix.csv`
- `tables/figure_evidence_table.csv`

## 3. Per-paper reading and note plan

### 3.1 `khilkevich2024BrainwideDynamicsLinking`

阅读优先级与原因：

- 优先级：`highest`
- 原因：这是当前最直接覆盖 `brain-wide / distributed computation` 主轴的核心实验论文，题目与提取文本首页都明确指向 sensation-to-action、decision-making、brain-wide neural activity 和 distributed sensorimotor transformation。

在 field-first survey 中的预期角色：

- `brain-wide / distributed computation`：第一锚点文献。
- `population dynamics / neural manifolds`：用于观察 evidence integration、movement preparation、movement execution 是否以 population subspace / dynamics 方式组织。
- `cross-animal conserved dynamics`：不是主角色。
- `representational tuning vs dynamical systems framing`：可作为后续与 `michaels2016NeuralPopulationDynamics` 对照的 brain-wide case。

拟定 note 路径：

- `notes/khilkevich2024BrainwideDynamicsLinking.md`

该 note 必须包含的 sections：

- citation metadata
- one-paragraph summary
- research question
- task / behavior
- species / brain area / recording method
- neural object analyzed
- main findings
- figure-by-figure evidence map
- modeling relevance
- relation to field-first survey axes
- uncertainty / caveats
- candidate entries for future `paper_matrix.csv`
- candidate entries for future `figure_evidence_table.csv`

未来 `paper_matrix.csv` 候选录入方向：

- `paper`: `Brain-wide dynamics linking sensation to action during decision-making`
- `citekey`: `khilkevich2024BrainwideDynamicsLinking`
- `category`: 预计为 `experimental landmark`
- `field_axis`: 预计至少包含 `brain-wide / distributed computation`
- `species`: 从全文确认
- `brain_area_or_scale`: brain-wide / multi-area，需从正文与图确认
- `task_or_behavior`: ambiguous visual input / perceptual decision task，需从方法与主图确认
- `neural_measurement`: 需从全文确认
- `neural_object`: evidence integration, preparatory subspace, execution dynamics 等，需从结果图确认
- `computation`: sensation-to-action transformation, evidence accumulation
- `causal_status`: 待全文确认
- `key_finding_short`: 仅能在 full-text reading 后写入
- `modeling_opportunity`: brain-wide latent dynamics / subspace interaction / distributed accumulation
- `identifiers`: DOI / PMID / PMCID / S2
- `uncertainty`: 是否 truly brain-wide parallel integration 以及与 motor-preparatory subspace 的关系

未来 `figure_evidence_table.csv` 候选录入方向：

- 优先抓取能区分 sensory response、evidence integration、movement preparation、movement execution 的主图。
- 优先抓取明确带有 subspace、population pattern、timescale、regional comparison 的图表。
- 每条 figure evidence 候选都必须回指 `figure_or_table`、`result_section`、`page`。

### 3.2 `michaels2016NeuralPopulationDynamics`

阅读优先级与原因：

- 优先级：`high`
- 原因：这是 `population dynamics / neural manifolds` 轴上的核心 landmark，而且题目本身就把 `representational tuning` 与 `dynamical system` framing 放在对照位，是后续 survey 组织理论分歧的关键锚点。

在 field-first survey 中的预期角色：

- `brain-wide / distributed computation`：不是主角色，但可作为局部系统中 dynamics framing 的强对照。
- `population dynamics / neural manifolds`：主角色。
- `cross-animal conserved dynamics`：不是主角色。
- `representational tuning vs dynamical systems framing`：主角色，是本轮最直接的 framing contrast 文献。

拟定 note 路径：

- `notes/michaels2016NeuralPopulationDynamics.md`

该 note 必须包含的 sections：

- citation metadata
- one-paragraph summary
- research question
- task / behavior
- species / brain area / recording method
- neural object analyzed
- main findings
- figure-by-figure evidence map
- modeling relevance
- relation to field-first survey axes
- uncertainty / caveats
- candidate entries for future `paper_matrix.csv`
- candidate entries for future `figure_evidence_table.csv`

未来 `paper_matrix.csv` 候选录入方向：

- `paper`: `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
- `citekey`: `michaels2016NeuralPopulationDynamics`
- `category`: 预计为 `experimental landmark` 或 `computational/analysis landmark`
- `field_axis`: `population dynamics / neural manifolds`; `computational methods and modeling`
- `species`: 从全文确认
- `brain_area_or_scale`: motor cortex / reaching system，需正文确认
- `task_or_behavior`: center-out reaching
- `neural_measurement`: neural population activity
- `neural_object`: rotational dynamics / representational tuning / recurrent dynamics
- `computation`: movement generation framing, dynamical system explanation
- `causal_status`: likely correlational/model-comparison, 待全文确认
- `key_finding_short`: 需等 full-text 阅读后写入
- `modeling_opportunity`: recurrent network comparison, covariance-matched permutation logic, latent dynamics benchmarking
- `identifiers`: DOI / PMID / PMCID / S2
- `uncertainty`: 需要区分 simulation / motor cortex data / RNN model 三者证据层级

未来 `figure_evidence_table.csv` 候选录入方向：

- 优先抽取直接比较 representational model 与 dynamical model 的图。
- 优先抽取 rotational dynamics、CMPT、RNN emergent dynamics 的关键图表。
- 对于作者的 methodological claim，要单独标记为 `methodological`，不要混成 primary biological evidence。

### 3.3 `safaie2023PreservedNeuralDynamics`

阅读优先级与原因：

- 优先级：`high`
- 原因：这是目前最适合把 population dynamics 轴延展到 `cross-animal conserved dynamics` 的实验论文。首页提取文本已经清楚提出 shared circuit-level constraints、preserved latent dynamics、cross-individual decoding、cortex 与 dorsal striatum extension。

在 field-first survey 中的预期角色：

- `brain-wide / distributed computation`：次角色，可用于说明 preserved dynamics 并不只局限于单一 recording set。
- `population dynamics / neural manifolds`：主角色。
- `cross-animal conserved dynamics`：主角色。
- `representational tuning vs dynamical systems framing`：可作为 dynamics framing 的更高层次 extension，而不是直接对照 paper。

拟定 note 路径：

- `notes/safaie2023PreservedNeuralDynamics.md`

该 note 必须包含的 sections：

- citation metadata
- one-paragraph summary
- research question
- task / behavior
- species / brain area / recording method
- neural object analyzed
- main findings
- figure-by-figure evidence map
- modeling relevance
- relation to field-first survey axes
- uncertainty / caveats
- candidate entries for future `paper_matrix.csv`
- candidate entries for future `figure_evidence_table.csv`

未来 `paper_matrix.csv` 候选录入方向：

- `paper`: `Preserved neural dynamics across animals performing similar behaviour`
- `citekey`: `safaie2023PreservedNeuralDynamics`
- `category`: 预计为 `experimental landmark`
- `field_axis`: `population dynamics / neural manifolds`; `cross-animal conserved dynamics`
- `species`: monkey / mouse，需全文核对具体 dataset 结构
- `brain_area_or_scale`: motor cortex; dorsal striatum extension，需图文确认
- `task_or_behavior`: similar behaviour / future movement planning / covert behavior，需全文拆开确认
- `neural_measurement`: neural population recordings
- `neural_object`: latent dynamics / preserved dynamics / cross-individual alignment
- `computation`: conserved behavior-related neural organization
- `causal_status`: likely correlational plus model support, 待全文确认
- `key_finding_short`: 等 full-text 阅读后写入
- `modeling_opportunity`: cross-animal alignment, latent geometry preservation, constraint-based neural modeling
- `identifiers`: DOI / PMID / PMCID / S2
- `uncertainty`: preservation 的 operational definition、alignment method、跨物种与跨个体边界条件

未来 `figure_evidence_table.csv` 候选录入方向：

- 优先抽取定义和证明 `preserved latent dynamics` 的主图。
- 优先抽取跨个体 decoding、covert behavior、dorsal striatum extension 的结果图。
- 模型结果要和 experimental evidence 分开记录。

## 4. Required note structure

结合 `templates/paper_note_template.md`、当前项目 workflow 和本轮任务约束，3 篇 notes 建议统一使用以下结构：

1. citation metadata
2. one-paragraph summary
3. research question
4. task / behavior
5. species / brain area / recording method
6. neural object analyzed
7. main findings
8. figure-by-figure evidence map
9. modeling relevance
10. relation to field-first survey axes
11. uncertainty / caveats
12. candidate entries for future `paper_matrix.csv`
13. candidate entries for future `figure_evidence_table.csv`

建议在 note 内额外保留两个小原则：

- `paper claim` 与 `our interpretation` 分段写，避免混淆。
- `experimental evidence` 与 `model/method evidence` 分段写，尤其对 `michaels2016NeuralPopulationDynamics` 和 `safaie2023PreservedNeuralDynamics` 很重要。

## 5. Figure-evidence extraction rules

本轮 figure-level extraction 必须遵守以下规则：

- 不要从 abstract alone 推断 figure-level claims。
- 每条 figure claim 必须指向 `figure/table/result section/page` 中至少一个明确位置；如果页码或图号暂时不确定，必须写 `unclear`。
- 明确区分：
  - paper claim
  - extracted evidence
  - model/agent interpretation
  - user-facing survey interpretation
- 对存在 debate、multiple analyses、alignment assumptions 或 model dependence 的结论，必须显式标记 uncertainty。
- Introduction / Discussion 中的背景表述不能直接当作 figure evidence。
- 如果 extracted text 遗漏图注、公式、supplementary mapping，要在 note 里专门标记 extraction limitation。

## 6. Copyright / safety rules

- 所有 findings 一律使用中文或英文技术术语的概括性 paraphrase，不复制长段原文。
- 不要把 `papers/extracted_text/` 下的全文内容转写进 notes 或 synthesis 文件。
- 不要提交 extracted full text。
- 若需要保留极短原句，只能在确有必要时做最小引用，并优先改写。

## 7. Recommended order

建议阅读顺序：

1. `khilkevich2024BrainwideDynamicsLinking`
   原因：
   最能先建立 `brain-wide / distributed computation` 的 field-first 总框架，也最可能产出后续 advisor-facing 综述里作为开篇实验锚点的 figure-level evidence。

2. `michaels2016NeuralPopulationDynamics`
   原因：
   第二步用它建立 population dynamics 的经典 framing，对后续解释什么叫 dynamics-first、以及为何它不同于 representational tuning 非常关键。

3. `safaie2023PreservedNeuralDynamics`
   原因：
   第三步把 dynamics 轴扩展到跨动物 conserved structure，能帮助 survey 从单一任务系统跳到更 general 的 organizing principle。

这个顺序的好处是：

- 先拿到一个 brain-wide experimental anchor。
- 再拿到一个 population dynamics 的经典理论/实验对照 anchor。
- 最后补上 cross-animal conserved dynamics 的 broader generalization case。

## 8. What not to do yet

- 不要在本步骤创建 notes。
- 不要更新 `tables/paper_matrix.csv`。
- 不要更新 `tables/figure_evidence_table.csv`。
- 不要在 full-text reading 完成前把 figure-level evidence 标记为 confirmed。
