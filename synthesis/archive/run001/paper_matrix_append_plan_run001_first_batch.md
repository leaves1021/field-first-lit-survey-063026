# Batch scope

本文件是 `run001_first_batch` 的 `paper_matrix.csv` append plan。

目标：

- 基于 3 篇已完成 full-text note 且已有 candidate `paper_matrix.csv` rows 的文献，生成一个 proposed append plan。
- 本步骤只生成计划文档，不更新 `tables/paper_matrix.csv`，也不更新 `tables/figure_evidence_table.csv`。

特殊约束：

- Do not include figure-level rows.
- Do not update `paper_matrix.csv`.
- Keep all rows as proposed append rows only.
- Use only candidate `paper_matrix.csv` rows already present in the three notes.
- Treat unresolved figure-level PDF inspection as uncertainty, not as a blocker for paper-level matrix rows unless the paper-level claim itself depends on it.
- Check duplicate citekeys against existing `tables/paper_matrix.csv`.

# Source notes

本次 append plan 只使用以下 notes 中已经写出的 candidate `paper_matrix.csv` rows：

1. `notes/khilkevich2024BrainwideDynamicsLinking.md`
2. `notes/michaels2016NeuralPopulationDynamics.md`
3. `notes/safaie2023PreservedNeuralDynamics.md`

# QC basis

本次判断依据：

- `synthesis/first_batch_note_qc_run001.md`
- `tables/paper_matrix.csv`
- 三篇 source notes 中现有的 candidate `paper_matrix.csv` rows

QC 要点汇总：

- 三篇 note 都已具备 new-schema sections。
- 三篇 note 的 `paper_matrix` candidate row 现在都已经是完整表头格式。
- 当前主要未解决项在 figure-level PDF inspection，而不是 paper-level row 的结构完整性。
- 因此，paper-level matrix rows 可以先进入 proposed append plan，但 figure-level evidence 仍然必须留给独立流程。

# Proposed paper_matrix.csv append rows

以下 proposed rows 采用与 `tables/paper_matrix.csv` 完全一致的字段顺序：

`paper,citekey,year,category,field_axis,species,brain_area_or_scale,task_or_behavior,neural_measurement,neural_object,computation,causal_status,key_finding_short,modeling_opportunity,identifiers,uncertainty,notes`

| paper | citekey | year | category | field_axis | species | brain_area_or_scale | task_or_behavior | neural_measurement | neural_object | computation | causal_status | key_finding_short | modeling_opportunity | identifiers | uncertainty | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `Brain-wide dynamics linking sensation to action during decision-making` | `khilkevich2024BrainwideDynamicsLinking` | `2024` | `experimental landmark` | `brain-wide / distributed computation; population dynamics and neural manifolds; flexible behavior and cognitive control` | `Mouse` | `Brain-wide Neuropixels recordings across cortex, basal ganglia, thalamus, midbrain, cerebellum, hippocampus and hindbrain` | `Visual change detection with ambiguous evidence and lick report` | `Neuropixels spiking activity; face video; pupil; wheel movement` | `TF-responsive sparse subpopulations; preparatory activity; movement-null and movement subspaces` | `Distributed evidence accumulation and sensorimotor transformation` | `primarily correlational / state-space analysis` | `Training is associated with sparse distributed neural populations outside the visual system that integrate evidence and support preparatory dynamics in movement-null subspace before action.` | `Multi-area dynamical systems; subspace-switching models; distributed accumulators` | `DOI 10.1038/s41586-024-07908-w; PMID 39261727; PMCID PMC11499283; S2 edb148e6ccc32491a80ff81bc6918258bd6a4d7d` | `Figure-level panel mapping and any intervention-related claims require manual PDF inspection.` | `Proposed append row only; figure-level confirmation remains separate; trained-vs-untrained wording kept conservative.` |
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | `michaels2016NeuralPopulationDynamics` | `2016` | `computational/analysis landmark` | `population dynamics and neural manifolds; computational methods and modeling` | `Macaque monkey (PMd/M1 data as example dataset)` | `PMd/M1 motor cortex` | `13-direction center-out reaching` | `population activity; simulated neural activity; PMd/M1 comparison` | `rotational dynamics; representational tuning; preferred direction; jPCA planes` | `movement generation; dynamical systems explanation` | `primarily correlational/model-comparison` | `CMPT shows that rotational dynamics in PMd/M1 are better explained by dynamical-system logic than by representational tuning alone.` | `jPCA-style dimensionality reduction; covariance-matched permutation logic; RNN benchmarks for motor cortex dynamics` | `DOI 10.1371/journal.pcbi.1005175; PMID 27814352; PMCID PMC5096671; S2 af1a65fa44773c427235e1f88bf714d64418883f` | `Real data source details and some panel-to-claim mappings require manual PDF inspection.` | `Proposed append row only; preserve model-comparison framing and methodological caution.` |
| `Preserved neural dynamics across animals performing similar behaviour` | `safaie2023PreservedNeuralDynamics` | `2023` | `representative experimental landmark` | `population dynamics and neural manifolds; cross-animal conserved dynamics` | `monkey; mouse` | `motor cortex (M1/PMd), dorsolateral striatum` | `center-out reaching; sequential reaching; reach/pull joystick; instructed-delay planning` | `spike-based population recordings` | `preserved latent dynamics / neural manifold` | `cross-animal alignment; decoding; control analysis; RNN comparison` | `correlational + model-based control` | `same-behavior latent dynamics are preserved across individuals and extend beyond motor cortex` | `learn constraints that preserve shared latent geometry across individuals` | `DOI 10.1038/s41586-023-06714-0; PMID 37938772; PMCID PMC10665198` | `alignment- and manifold-dependent operational definition; no direct perturbation` | `Proposed append row only; extended-data control panels still need PDF confirmation but are not a blocker for the paper-level matrix row.` |

# Duplicate / conflict check

对 `tables/paper_matrix.csv` 的现有 rows 做了检查。当前已存在的 `citekey` 为：

- `vyas_2020_computation_through_neural`
- `ye_2026_brainwide_topographic_coordination`

本次 3 条 proposed rows 的 duplicate / conflict 检查结果：

- `khilkevich2024BrainwideDynamicsLinking`：无 duplicate `citekey`
- `michaels2016NeuralPopulationDynamics`：无 duplicate `citekey`
- `safaie2023PreservedNeuralDynamics`：无 duplicate `citekey`

额外冲突检查：

- 未发现与现有 `paper` / `year` 的直接重复。
- 未发现需要因为 title-year 冲突而立即 hold 的条目。
- 三条 proposed rows 在概念上分别覆盖：
  - `brain-wide / distributed computation`
  - `population dynamics / computational methods`
  - `cross-animal conserved dynamics`
  因此即使 field axis 有部分重叠，也不构成重复 paper。

结论：

- 当前 duplicate / conflict check 没有发现阻止进入 user approval 的硬冲突。

# Field normalization notes

本次 append plan 只做保守的字段规范化，不改动 notes 源文件。

规范化说明：

- `category`
  - `khilkevich2024BrainwideDynamicsLinking` 保留为 `experimental landmark`
  - `michaels2016NeuralPopulationDynamics` 保留为 `computational/analysis landmark`
  - `safaie2023PreservedNeuralDynamics` 暂保留为 `representative experimental landmark`
  - 这里存在轻微风格差异，但都仍处于保守、可理解的范围；如果后续要统一词表，可在单独 cleanup 中处理。

- `field_axis`
  - 维持 notes 中的多轴分号分隔写法。
  - 不额外压缩成更短标签，避免在本步骤中引入新的解释偏差。

- `causal_status`
  - `khilkevich2024BrainwideDynamicsLinking`：保留 `primarily correlational / state-space analysis`
  - `michaels2016NeuralPopulationDynamics`：保留 `primarily correlational/model-comparison`
  - `safaie2023PreservedNeuralDynamics`：保留 `correlational + model-based control`
  - 三者都保持保守，没有升级为因果性措辞。

- `brain_area_or_scale`
  - 保留 notes 中较具体的区域/尺度描述，不在本步骤进一步压缩。

- `computation`
  - 保留 note-level 的 paper-wide computation framing。
  - 不加入 figure-level mechanism 细节。

# Rows not ready for append

当前没有需要因为结构缺失、duplicate `citekey`、或核心字段为空而移出的 rows。

但仍需显式记录以下非阻塞性 caution：

- `khilkevich2024BrainwideDynamicsLinking`
  - 高价值 figure-level claims 仍需 PDF inspection；
  - 这影响未来 `figure_evidence_table.csv`，不阻止当前 paper-level matrix row 进入 proposed append。

- `michaels2016NeuralPopulationDynamics`
  - 真实 PMd/M1 source dataset 与部分 panel mapping 还应人工核对；
  - 这属于 figure/method detail，不阻止当前 paper-level matrix row。

- `safaie2023PreservedNeuralDynamics`
  - Extended Data control panels 仍需 PDF inspection；
  - 这影响 control-level figure evidence，不阻止当前 paper-level matrix row。

# Final recommendation

`ready_for_user_approval`

理由：

- 三条 proposed rows 都已经具备完整 `paper_matrix.csv` 所需核心字段：`paper`、`citekey`、`year`、`category`、`field_axis`、`causal_status` 非空。
- 未发现 duplicate `citekey` 或直接 title-year conflict。
- 当前未解决的问题主要在 figure-level PDF inspection，而不是 paper-level matrix row 的结构或保守性。
- 因此这 3 条 rows 适合进入一个后续单独的 user-approved append step，但本文件本身不执行 append。
