# Citation metadata

- title: `Brain-wide dynamics linking sensation to action during decision-making`
- authors: `Andrei Khilkevich; Michael Lohse; Ryan J. Low; Ivana Orsolic; Tadej Bozic; Paige Windmill; T. Mrsic-Flogel`
- year: `2024`
- venue: `Nature`
- DOI: `10.1038/s41586-024-07908-w`
- PMID: `39261727`
- PMCID: `PMC11499283`
- citekey: `khilkevich2024BrainwideDynamicsLinking`
- PDF path: `papers/raw_pdf/khilkevich2024BrainwideDynamicsLinking.pdf`
- extracted text path: `papers/extracted_text/khilkevich2024BrainwideDynamicsLinking.md`

# One-paragraph summary

这篇论文研究在学习后的 perceptual decision task 中，ambiguous visual evidence 如何跨越大量脑区，被转化为 movement preparation 并最终触发 action。作者在 head-fixed mice 上进行 brain-wide Neuropixels recordings，提出 sensory evidence 的表征不仅存在于视觉系统，而且在训练后会出现在 frontal cortex、thalamus、basal ganglia、midbrain 和 cerebellum 的稀疏神经元群体中；这些群体表现出与 evidence accumulation 相符的延长时程，并与 preparatory activity 在 population level 上对齐。作者进一步将 preparatory activity 与 movement execution 分解到 orthogonal subspaces，认为 sensory evidence 主要驱动 movement-null / preparatory dynamics，而在 lick onset 附近全脑活动快速转入 movement-related dynamics。

# Research question

这篇论文的核心问题是：在需要时间整合的 perceptual decision task 中，sensory input 如何在 brain-wide scale 上被转换为 choice-related preparation 和 action execution，以及这些转换是分布式并行发生，还是局限在少数经典 decision areas。

对 field-first systems/computational neuroscience 的意义：

- 它直接对应 `brain-wide / distributed computation` 主轴。
- 它把 `evidence accumulation`、`movement preparation`、`movement execution` 放进同一个 brain-wide dynamics 框架。
- 它提供了一个把 decision-making 与 motor control 连接起来的 population-dynamics 案例，而不是只看单一脑区的 encoding。

# Task / behavior

- animal / species:
  - mouse
- behavioral task:
  - head-fixed visual change detection task
- stimulus / decision / action structure:
  - 小鼠在 running wheel 上保持相对静止，观看 temporal frequency (TF) 随机波动的 drifting grating
  - baseline TF 围绕 1 Hz 波动，change time 不可预测，change magnitude 随机
  - 动物需要在检测到持续的 stimulus speed increase 后，通过 licking 报告并获得奖励
  - 如果 change 前出现 lick 或 running-wheel movement，trial 会被中止
- uncertainty:
  - 提取文本明确支持 “ambiguous visual input” 和“需要 temporal integration”的任务结构
  - task 中 reward window、block structure、训练 stage 的精细参数仍建议在原 PDF methods 中手动复核

# Species / brain area / recording method

- species:
  - mouse
- brain-wide or multi-area scope:
  - 明确为 brain-wide / multi-area
  - 提取文本显示记录覆盖 cortex、basal ganglia、hippocampus、thalamus、midbrain、cerebellum 和 hindbrain
- recording method:
  - dense silicon electrode recordings with Neuropixels probes
  - 同时记录 face videography、pupil size 和 running wheel movement
- relevant brain areas or scale:
  - 视觉系统：LGd, VISp, SCs 等
  - frontal / premotor regions：MOs, ACA, mPFC, ORB, MOp
  - basal ganglia：CP, GPe, SNr/GPi
  - thalamus：VAL, PF, VB, LP 等
  - midbrain：MRN, APN, SCm, NPC
  - cerebellum：Lob4/5, SIM, DCN 等
- uncertainty:
  - 每个区域在主结果中的精确功能分工需要结合原 PDF figure labels 和 Supplementary Table 进一步确认

# Neural object analyzed

- population activity across dozens of brain regions
- sparse TF-responsive subpopulations
- lick-preparatory activity and lick-execution activity
- fast TF pulse responses and their response duration / peak latency
- preparatory and movement-related subspaces
- movement-null dimension and movement dimension
- region-level and grouped-region activity patterns
- uncertainty:
  - 文中显式使用 subspace / movement-null / movement dimensions
  - `latent variables` 不是本文最核心的术语；若在后续综述中使用 latent-state framing，需要标记为我们对 population geometry 的解释，而不是直接照搬作者主术语

# Main findings

- 学习后的 mice 在几乎全脑范围内出现对 task-relevant visual evidence 的稀疏表征，而不仅限于视觉系统。
  - evidence link: `Brain-wide encoding of sensory input`; `Fig. 1`; `Pages 2-3`
- 对 fast TF pulse 的响应在早期视觉区最短暂，但在 frontal cortex、basal ganglia、midbrain、thalamus 和 cerebellum 中更延迟、更持久，支持这些区域能够在数百毫秒尺度上整合 sensory evidence。
  - evidence link: `Timescales of sensory responses across the brain`; `Fig. 2`; `Pages 2-4`
- 非视觉 premotor / association areas 对 sequential fast pulses 表现出 facilitation，并且 change period 的 ramping 随 stimulus change magnitude 增强，说明 evidence accumulation 是 distributed、parallel 的，而不是只发生在单一区域。
  - evidence link: `Parallel sensory integration in premotor areas`; `Fig. 3`; `Pages 4-5`
- 这种 widespread evidence encoding and integration 在很大程度上依赖学习：untrained mice 的 TF-responsive cells 主要局限于视觉系统和少数 midbrain 区域，而非训练后的广泛 premotor / subcortical 分布。
  - evidence link: `Learning enables widespread sensory integration`; `Fig. 4`; `Page 6`
- 在能够整合 evidence 的区域中，TF-responsive subpopulations 与 preparatory activity 在 population-vector level 上显著对齐，并且这些 TF-responsive cells 往往更早参与 preparatory build-up。
  - evidence link: `Evidence-encoding cells initiate preparatory activity`; `Fig. 5`; `Pages 6-7`
- preparatory activity 主要占据 movement-null subspace，在 lick onset 后迅速转入 movement subspace；sensory evidence pulse 的响应主要沿着 first movement-null dimension 对齐，而不是直接沿 movement dimension 对齐。
  - evidence link: `Brain-wide orthogonal dynamics surrounding action`; `Fig. 6`; `Pages 8-9`
- 作者据此提出，learning 将 evidence accumulation 对齐到 action preparation，从而在 brain-wide scale 上形成分布式的 sensorimotor transformation。
  - evidence link: `Discussion`; `Pages 8-10`

# Figure-by-figure evidence map

| figure/table | result section or page | paper claim | extracted evidence | neural variable/object | analysis method | causal status | uncertainty/caveat |
|---|---|---|---|---|---|---|---|
| `Fig. 1` | `Brain-wide encoding of sensory input`; `Pages 2-3` | task-relevant visual evidence、lick preparation 和 lick execution 在训练后的 mouse brain 中呈现广泛分布，但 TF-responsive cells 是稀疏的 | 提取文本显示作者用 single-cell Poisson GLM 区分 stimulus TF、lick preparation、lick execution，并报告 TF-responsive units 分布在多数脑区，而 medulla / orofacial execution nuclei 不表现出类似 TF responses | TF-responsive units; lick-preparatory units; lick-execution units | task design + Neuropixels + Poisson GLM + cross-validated nested test | correlational / observational | 图中文字提取较乱，区域热图细节需要人工看 PDF 主图；这里不能只依赖 caption 判断具体百分比 |
| `Fig. 2` | `Timescales of sensory responses across the brain`; `Pages 2-4` | 早期视觉区对 fast TF pulse 的响应更早、更短；非视觉 integrative regions 的响应更晚、更宽，支持 prolonged evidence representation | 文本明确说 visual areas 对 pulse 响应 brief and faithful，而 frontal cortex、basal ganglia、midbrain、thalamus、cerebellum 的响应更延迟、更持久，部分区域在 stimulus sample 结束后仍维持表示 | fast TF pulse responses; response peak time; half-peak width | pulse-aligned responses; GLM TF kernels; regional comparison | correlational / observational | 具体哪些区域进入每个 grouped comparison 需参照 Supplementary Table；图轴与统计检验最好人工核对 PDF |
| `Fig. 3` | `Parallel sensory integration in premotor areas`; `Pages 4-5` | evidence integration 是并行、多区域的；部分非视觉区对 sequential fast pulses 出现 facilitation，change-period ramping 随 evidence strength 增强 | 文本指出 higher visual areas 多数不表现明显 second-pulse facilitation，但 LP、hippocampal regions、VAL、PF 以及 MOs 等区域可在 0.2–0.3 s 尺度表现 facilitation；同时 MOs 的 ramping slope 随 change magnitude 增大 | sequential-pulse facilitation; change-period ramping; TF-responsive vs non-responsive units | pulse-pair analysis; relative facilitation; GLM change kernels; change-size scaling | correlational / observational | 提取文本中 Fig. 3 caption 不完整，部分 panel 需要人工 PDF 检查，尤其是 `j-o` 的 panel-to-claim 对应 |
| `Fig. 4` | `Learning enables widespread sensory integration`; `Page 6` | 非视觉系统中的 evidence representation / integration 很大程度上是 learning-dependent，而 intrinsic timescales 本身并不随训练显著改变 | untrained mice 只在 visual system 和少数 midbrain 区域见到明显 TF responses；训练后 premotor / basal ganglia / cerebellar / MRN 等区出现更多 TF-responsive cells。作者还报告 intrinsic timescale 与 fast-pulse half-width 不显著相关，trained vs untrained intrinsic timescales 相近 | TF-responsive spatial distribution; focality index; intrinsic timescale; pulse-response half-width | trained vs untrained comparison; focality index; autocorrelation timescale; correlation analysis | correlational / observational | 这是强 learning comparison，但不是 intervention；“learning causes distributed integration” 仍应表述为经验依赖/训练相关，而非严格因果 |
| `Fig. 5` | `Evidence-encoding cells initiate preparatory activity`; `Pages 6-7` | 在 integrative regions，TF-responsive subpopulations 与 preparatory activity 对齐，并且更早参与 pre-lick build-up | 文本指出 MOs 以及 frontal cortex、basal ganglia、cerebellum、midbrain 等区中，TF pulse response vector 与 preparatory vector 显著对齐；TF-responsive populations 在 hit-lick 前被更早 recruit；其 preparatory onset 与 fast-pulse response duration 存在关系 | alignment between pulse response and preparatory activity; fraction of active TF-responsive units | population vector alignment; correlation; onset timing analysis | correlational / observational | alignment 指标的精确定义与 window selection 需要复核 Methods；图中 region ordering 和 timing thresholds 需人工核对 |
| `Fig. 6` | `Brain-wide orthogonal dynamics surrounding action`; `Pages 8-9` | preparatory activity 主要位于 movement-null subspace，动作开始后活动迅速切换到 movement subspace；evidence pulse responses 主要沿 first movement-null dimension 对齐 | 提取文本明确说 pre-lick activity predominantly resided in movement-null subspace，lick onset 后转入 movement subspace；fast TF pulse responses 与 first movement-null dimension 对齐，而不是 movement dimension；TF-responsive subpopulation 对 movement-null preparatory activity 有 disproportionate contribution | movement-null subspace; movement subspace; first movement-null dimension; TF-responsive contribution | subspace decomposition; projections; occupancy; cosine alignment; state-space visualization | correlational / observational with model-style geometric analysis | 这一部分对全文主张最关键，但图与 Extended Data 的对应较复杂；必须人工检查 PDF 图形和 Methods 才能做更细的 figure-level note |

# Modeling relevance

- latent dynamics:
  - 虽然本文主要术语是 subspace / movement-null dynamics，而不是直接强调 latent state models，但它非常适合后续用低维 population dynamics 语言重述 brain-wide sensorimotor transformation。
- distributed computation:
  - 论文把 evidence accumulation 从经典局部 decision-area framing 扩展成跨 frontal cortex、thalamus、basal ganglia、midbrain、cerebellum 的 distributed computation。
- evidence accumulation / sensorimotor transformation:
  - 这是本文最直接的 modeling interface。后续可以考虑：
  - region-coupled accumulator models
  - low-dimensional multi-area dynamical systems
  - movement-null / movement subspace transition models
  - task-trained recurrent networks with distributed preparatory channels
- possible computational models or analyses:
  - multi-area latent dynamical systems
  - state-space analyses aligned to behaviorally defined events
  - subspace occupancy / subspace switching metrics
  - learned evidence-accumulation timescales decoupled from intrinsic autocorrelation timescales
- model / agent interpretation:
  - 从 survey 角度看，这篇很适合作为 “brain-wide decision computation can still be described by structured population dynamics” 的示范案例
  - 但这一步是我们的 modeling interpretation，不应与作者已直接证明的结论混写

# Relation to field-first survey axes

- `brain-wide / distributed computation`:
  - 强相关，是当前 Run001 最直接的主轴核心文献之一
- `population dynamics and neural manifolds`:
  - 明确相关，尤其是 movement-null / movement dimensions、population alignment、brain-wide preparatory dynamics
- `multi-area communication and routing`:
  - 中等相关。本文强调跨多脑区并行 transformation，但并没有在当前提取文本中给出明确的 routing 机制或特定投射因果证据
- `causal perturbation and model-based intervention`:
  - 当前不应强写。提取文本中未见核心 perturbation result；如果正文或 supplementary 有 intervention，需要后续手动 PDF 复核
- `NeuroAI / interpretable models`:
  - 间接相关。它为 interpretable multi-area dynamical models 提供目标现象，但本文主证据仍是实验记录与 state-space analysis，不是 AI/model paper

# Uncertainty / caveats

- extraction limitations:
  - 提取文本保留了主要正文和不少 figure captions，但多图页的版面顺序比较混乱
  - 某些 panel labels、统计标记和 caption 片段有截断或错位
- figures / supplementary completeness:
  - Extended Data captions 部分可见，但很多主图的 panel-to-panel mapping 仍需人工 PDF inspection
  - 如果后续要写 figure-level evidence table，必须回看 PDF 图注与具体 panel
- claims requiring manual PDF figure inspection:
  - `Fig. 3` 中各 panel 与具体 facilitation / ramping / GLM kernel claims 的对应
  - `Fig. 5` 中不同 region group 的 activation ordering
  - `Fig. 6` 中 movement-null vs movement dimensions 的几何定义和 region-by-region occupancy
- conceptual caution:
  - 这篇论文非常强调 distributed evidence accumulation，但“brain-wide”不应被误写成所有区域等价参与相同 computation
  - “learning-dependent emergence” 在当前证据下应表述为 trained vs untrained contrast，不应夸大成严格单因果证明

# Candidate entries for future `paper_matrix.csv`

以下为候选条目预案，不实际写入 CSV：

| field | proposed value |
|---|---|
| `paper` | `Brain-wide dynamics linking sensation to action during decision-making` |
| `citekey` | `khilkevich2024BrainwideDynamicsLinking` |
| `year` | `2024` |
| `category` | `experimental landmark` |
| `field_axis` | `brain-wide / distributed computation; population dynamics and neural manifolds; flexible behavior and cognitive control` |
| `species` | `Mouse` |
| `brain_area_or_scale` | `Brain-wide Neuropixels recordings across cortex, basal ganglia, thalamus, midbrain, cerebellum, hippocampus and hindbrain` |
| `task_or_behavior` | `Visual change detection with ambiguous evidence and lick report` |
| `neural_measurement` | `Neuropixels spiking activity; face video; pupil; wheel movement` |
| `neural_object` | `TF-responsive sparse subpopulations; preparatory activity; movement-null and movement subspaces` |
| `computation` | `Distributed evidence accumulation and sensorimotor transformation` |
| `causal_status` | `primarily correlational / state-space analysis` |
| `key_finding_short` | `Learning recruits sparse distributed neural populations outside the visual system that integrate evidence and drive preparatory dynamics in movement-null subspace before action.` |
| `modeling_opportunity` | `Multi-area dynamical systems; subspace-switching models; distributed accumulators` |
| `identifiers` | `DOI 10.1038/s41586-024-07908-w; PMID 39261727; PMCID PMC11499283; S2 edb148e6ccc32491a80ff81bc6918258bd6a4d7d` |
| `uncertainty` | `Figure-level panel mapping and any intervention-related claims require manual PDF inspection.` |
| `notes` | `First full-text note drafted from extracted text; figure map still needs manual PDF confirmation.` |

# Candidate entries for future `figure_evidence_table.csv`

以下为候选条目预案，不实际写入 CSV：

| paper | citekey | figure_or_table | result_section | page | claim | evidence_summary | variable_or_neural_object | analysis_method | causal_status | relevance_to_research_question | uncertainty |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `Brain-wide dynamics linking sensation to action during decision-making` | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 1` | `Brain-wide encoding of sensory input` | `2-3` | Task-relevant sensory evidence is represented by sparse neurons across many brain regions after learning. | GLM-based encoding analysis separates TF, lick preparation, and lick execution; TF-responsive cells are widespread but sparse. | `TF-responsive units; lick-preparatory activity` | `Poisson GLM; cross-validated nested test` | `correlational` | Establishes that decision-related sensory evidence is not confined to classical sensory areas. | Exact region percentages should be checked in PDF heatmaps. |
| `Brain-wide dynamics linking sensation to action during decision-making` | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 2` | `Timescales of sensory responses across the brain` | `2-4` | Non-visual premotor and subcortical regions show more prolonged evidence-related responses than early visual areas. | Fast TF pulse responses are later and wider outside the early visual system, consistent with integrative dynamics. | `fast TF pulse response duration / peak time` | `pulse alignment; GLM kernel comparison` | `correlational` | Supports the distributed accumulation-timescale story. | Group composition and statistics need PDF confirmation. |
| `Brain-wide dynamics linking sensation to action during decision-making` | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 3` | `Parallel sensory integration in premotor areas` | `4-5` | Evidence integration is parallel and multi-regional rather than purely local. | Sequential-pulse facilitation and change-related ramping appear in non-visual integrative regions such as MOs and selected thalamic / hippocampal regions. | `facilitation to second pulse; ramping activity` | `pulse-pair analysis; GLM change kernels` | `correlational` | Connects behavioral integration timescale to multi-area neural dynamics. | Caption extraction is incomplete; panel-specific details require manual PDF reading. |
| `Brain-wide dynamics linking sensation to action during decision-making` | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 4` | `Learning enables widespread sensory integration` | `6` | Widespread non-visual evidence encoding emerges with learning, not from intrinsic regional properties alone. | Trained vs untrained comparison shows broader TF-responsive distribution in trained animals, while intrinsic timescales remain similar. | `TF-responsive distribution; intrinsic timescale` | `trained/untrained comparison; autocorrelation analysis` | `correlational / learning contrast` | Important for arguing that distributed computation is task-experience dependent. | Should not be overstated as strong causal intervention evidence. |
| `Brain-wide dynamics linking sensation to action during decision-making` | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 5` | `Evidence-encoding cells initiate preparatory activity` | `6-7` | TF-responsive neurons are preferentially recruited into preparatory dynamics in integrative regions. | Alignment between pulse response vectors and preparatory activity is strong in MOs and other integrative regions, but not in non-integrative visual regions like SCs. | `population-vector alignment; preparatory onset` | `vector correlation; onset timing analysis` | `correlational` | Links evidence accumulation directly to movement preparation. | Alignment windows and thresholds should be checked in Methods/PDF. |
| `Brain-wide dynamics linking sensation to action during decision-making` | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 6` | `Brain-wide orthogonal dynamics surrounding action` | `8-9` | Preparatory activity resides in movement-null subspace and sensory evidence responses align with that preparatory dimension rather than movement dimension. | Pre-lick activity is concentrated in movement-null subspace, then shifts into movement subspace at lick onset; TF-responsive contribution to movement-null preparatory activity is disproportionate in premotor regions. | `movement-null dimension; movement dimension; subspace occupancy` | `subspace decomposition; projection; cosine alignment` | `correlational / geometric analysis` | Provides the strongest bridge between evidence accumulation and population-dynamics framing of action preparation. | High-priority target for manual PDF figure inspection before any confirmed figure-level claim is entered. |

# Separation of claim, evidence, interpretation

- paper claim:
  - learning aligns evidence accumulation to action preparation across many brain regions
  - preparatory activity and movement execution are organized in different subspaces
- extracted evidence:
  - TF-responsive sparse populations are widespread in trained animals
  - non-visual regions show prolonged pulse responses, pulse facilitation, preparatory alignment, and movement-null occupancy
- model / agent interpretation:
  - 这可以被重述为 brain-wide distributed dynamical computation，且适合作为 multi-area latent-dynamics 建模目标
- user-facing survey interpretation:
  - 这篇可作为 field-first survey 中“decision-related computation is distributed yet structured” 的核心实验 anchor

# Extraction notes

- 本 note 主要基于 extracted text 和 figure captions 的局部可读部分完成。
- low-text warning:
  - `no`
- pages with sparse text:
  - 当前提取结果未触发 sparse-text 警告，但多图页文本顺序混乱。
- missing figures, captions, equations, or references:
  - 没有缺失整篇正文，但部分图 caption 和 panel 细节在提取文本中不完整。
  - 后续若要把任何具体图级 claim 视为 confirmed evidence，必须手动检查 PDF 原图和图注。
