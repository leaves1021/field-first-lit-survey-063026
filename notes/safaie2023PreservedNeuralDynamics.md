# Citation metadata
- title: `Preserved neural dynamics across animals performing similar behaviour`
- authors: `M. Safaie; J. C. Chang; J. Park; L. E. Miller; J. T. Dudman; M. G. Perich; J. A. Gallego`
- year: `2023`
- venue: `Nature`
- DOI: `10.1038/s41586-023-06714-0`
- PMID: `37938772`
- PMCID: `PMC10665198`
- citekey: `safaie2023PreservedNeuralDynamics`
- PDF path: `papers/raw_pdf/safaie2023PreservedNeuralDynamics.pdf`
- extracted text path: `papers/extracted_text/safaie2023PreservedNeuralDynamics.md`

# One-paragraph summary
这篇论文想回答一个很直接、但在跨个体比较里很难的问题：如果不同动物执行相似行为，神经群体动力学是否也会以某种可对齐的方式被保留下来。作者结合猴子中心-外 reaching、猴子序列随机目标 reaching、mouse reaching/pulling，以及 mouse dorsolateral striatum 记录，用 PCA 估计低维 latent dynamics，再用 CCA 做跨动物对齐。结果显示，在同物种、同任务、且行为更 stereotpyed 的情况下，跨个体 latent dynamics 的相似度会显著高于随机或打乱对照，并且这种 preserved dynamics 不仅能支持跨动物的运动/目标解码，还能出现在 covert planning 阶段。作者进一步用 RNN 对照说明：仅有相似行为并不足以自动推出相似 latent dynamics，暗示这些动力学更像是受共同 circuit constraints 约束的 species-level 组织结果，而不是简单的输出拟合副产物。

# Research question
这篇工作的核心科学问题是：同一物种内的不同个体，在执行相似行为时，是否会共享可对齐的 neural population dynamics；如果会，这种共享究竟反映的是行为输出本身，还是更深层的 circuit-level constraint。

对 field-first systems/computational neuroscience 的意义是：

- 它直接落在 `population dynamics and neural manifolds` 轴上。
- 它把“跨个体 preserved dynamics”作为一个可检验的现象，而不是只做单个动物的描述。
- 它也延伸到 `cross-animal conserved dynamics` 和较弱形式的 `distributed computation` 讨论，因为保留的动力学不只出现在 motor cortex，也扩展到 dorsolateral striatum。

# Task / behavior
- Species or model system:
  - monkey：Macaca mulatta 和 Macaca fascicularis
  - mouse：4 只小鼠
- Behavioral task or computational setting:
  - monkey center-out reaching
  - monkey sequential random-target reaching
  - mouse reaching and pulling joystick
  - monkey 的 instructed-delay 段用于分析 covert planning
- Brain areas or scale:
  - monkey motor cortex：M1 / PMd，文中将两者合并为 motor cortex
  - mouse motor cortex 与 dorsolateral striatum
- Neural measurement or model object:
  - spike-based population recordings
  - 低维 latent dynamics / neural manifold / aligned latent dynamics
- Uncertainty:
  - monkey 数据来自多个实验子集和已发表数据集，部分细节以 Methods 为准
  - “covert behaviour” 主要指 planning period，而不是完全独立的认知任务

# Species / brain area / recording method
- Species:
  - monkey 和 mouse 两个物种都被用于主结论
- Brain areas:
  - monkey：M1、PMd
  - mouse：motor cortex、dorsolateral striatum
- Recording method:
  - monkey：Utah arrays，Cerebus 记录，spike sorting 或 multi-unit threshold crossings
  - mouse：Neuropixels probe，KiloSort + manual curation
- Dataset structure if available:
  - monkey center-out task：多个 session，跨 3 只 monkey 的比较
  - monkey random-target sequential reaching：进一步增加行为复杂度
  - mouse reaching/pulling：2 个位置 x 2 个 load 的 trial 结构
  - mouse striatum：与 motor cortex 的联合记录支持跨区域比较

# Neural object analyzed
- 论文分析的核心对象是 `preserved latent dynamics`，也就是从 population activity 中提取的低维时间演化结构。
- 技术上先用 PCA 建立每个 session 的 neural manifold，再用 CCA 对不同个体的 latent trajectories 做对齐。
- 作者把这种动力学解释为同物种个体之间共享的、可被行为对齐的 population geometry。
- 支撑概念还包括：
  - neural modes
  - canonical correlations
  - across-animal decoding
  - cross-animal alignment
  - dorsal striatal latent dynamics
- 标记不确定项：
  - 这里的“preserved”是 operational definition，依赖对齐方法和 manifold 估计方式，但作者做了多个控制来稳健化这一点。

# Main findings
- 同一物种、同一行为下，不同个体的 motor cortical latent dynamics 可以通过 CCA 高度对齐，且相似度接近 within-animal baseline，明显高于随机行为窗口或 surrogate data 对照。
- 对齐后的 latent dynamics 能跨个体解码 continuous kinematics 或 target class，说明这些动力学不仅相似，而且携带行为相关信息。
- 行为越 stereotyped，跨个体 preserved dynamics 越强；猴子和小鼠、简单和复杂任务之间的比较都支持这一点。
- preserved dynamics 不只见于 overt movement，也出现在 covert planning 的 instructed-delay period。
- 这种保留还扩展到 mouse dorsolateral striatum，说明它不是 motor cortex 独有现象。
- RNN 对照表明：即使两个网络产生很相似的行为输出，也可以拥有很不同的 latent dynamics，因此行为相似性本身并不足以保证动力学保留。
- 多个控制分析支持作者的解释：保留动力学不是简单的静态 topological alignment 产物，也不太可能只是低维度选择或少量 neuron 采样的伪影。

# Figure-by-figure evidence map
| figure/table | result section or page | paper claim | extracted evidence | neural variable/object | analysis method | causal status | model / agent interpretation | user-facing survey interpretation | uncertainty/caveat |
|---|---|---|---|---|---|---|---|---|---|
| Fig. 1 | p. 1 | 提出 species-wide neural landscape 与 preserved latent dynamics 的假设 | 这是一张概念图，说明不同个体的相似行为可能对应可对齐的 latent trajectories | latent dynamics, neural manifold | conceptual framing | speculative / conceptual | 作为后续对齐与比较的理论起点 | 适合作为 cross-animal conserved dynamics 的 framing figure | 不是实证结果，不能当作证据本身 |
| Fig. 2 | pp. 2-3 | 猴子和小鼠在同一行为下表现出 preserved latent dynamics | monkey center-out 和 mouse reach/pull 中，aligned CCs 接近 within-animal baseline，且高于 shuffled / TME controls；跨动物 decoder 也接近 within-animal decoder | motor cortical latent dynamics; hand kinematics; target labels | PCA + CCA; LSTM decoder; control alignment | correlational / analytical | 表明共享的动力学几何可支持跨个体解码 | 这是本篇最核心的 population dynamics 证据 | 依赖 alignment 方法，但作者做了多种控制 |
| Fig. 3 | p. 4 | 更复杂的 sequential reaching 也保留动力学，且保留程度与行为 stereotypy 相关 | random-target sequence 中，在更多 condition 和更高行为变异下仍可见 preserved dynamics；打乱 condition 后保留下降 | motor cortical latent dynamics; condition structure | PCA + CCA; condition subsampling; neuron subsampling | correlational / analytical | 支持“保留动力学和行为结构有关，但不是简单的 topological artifact” | 这部分强化 task structure 与 manifold alignment 的联系 | matching procedure 仍有结构性，需结合控制实验理解 |
| Fig. 4 | pp. 4-5 | preserved dynamics 扩展到 dorsolateral striatum，并出现在 covert planning | mouse striatum 中跨动物动力学仍可对齐，且可跨动物解码；猴子 planning period 的 latent dynamics 也保持一致并能预测目标 | striatal latent dynamics; preparatory/planning dynamics; target class | PCA + CCA; Bayesian classifier | correlational / analytical | 将结论从 motor cortex 推广到更 distributed 的回路层面 | 对 `brain-wide / distributed computation` 轴是弱支持，但对 cross-region conserved dynamics 很重要 | 仍是相关性证据，不是因果操控 |
| Fig. 5 | pp. 5-6 | 相似行为是必要但不充分：RNN 可产生相似输出却具有不同 latent dynamics | 标准网络与 constrained network 行为表现相近，但通过约束项可让 latent dynamics 明显分离；alpha 越大，保留越弱，权重变化结构也不同 | RNN latent dynamics; recurrent weights | constrained RNN simulation; weight analysis | model-based, not causal biology | 说明 biological preservation 可能反映 circuit constraints，而不是单纯 output fitting | 这是方法论和建模层面的关键补充 | 只能说明模型逻辑，不能直接等同于真实脑回路机制 |
| Extended Data Fig. 2 / 7 | pp. 14, 18-19（部分图注需手动核对） | 控制分析排除了若干方法性解释 | TME、不同 manifold dimensionality、Procrustes、以及静态 topological alignment 的对照支持主要结论 | surrogate dynamics; alignment robustness | control analyses | methodological support | 增强“对齐结果不是纯方法假象”的可信度 | 适合放在 note 的稳健性证据里 | 部分 panel 级别信息在抽取文本里不完整，必要时要回 PDF 核验 |
| Extended Data Fig. 9 | p. 21 | 同一动物的相关任务不如不同动物的同一任务更能保留 latent dynamics | 相近但不同的 wrist / reach tasks 里，同一只猴子的动力学相似度反而低于不同猴子做同一任务 | cross-task latent dynamics | principal-angle style comparison / alignment | correlational / analytical | 强化“任务相似不等于动力学保留” | 对 survey 的对比论证很有用 | 作为补充控制而非主结论 |

# Modeling relevance
- 这篇文章对 modeling 的直接价值在于，它把 `cross-animal alignment` 变成了一个可以检验的目标，而不只是事后解释。
- `latent dynamics` 在这里不是纯粹的数学降维，而是和 motor behavior、planning、以及 shared circuit constraints 绑在一起。
- RNN 部分说明：如果想让模型解释 preserved dynamics，不能只拟合输出轨迹，还要考虑训练如何约束内部状态几何。
- 对 NeuroAI / interpretable models 的启发是：模型比较应同时看 `behavioral fit` 和 `latent geometry`，否则很容易把不同内部机制误当成同一种解。
- 论文最强的模型信息来自“行为相似并不自动导向动力学相似”，这为后续构建约束更强的生成模型提供了方向。

# Relation to field-first survey axes
- population dynamics and neural manifolds:
  - 强支持。整篇就是围绕跨动物 latent dynamics 和 manifold alignment 展开。
- cross-animal conserved dynamics:
  - 强支持。标题和主结果都直接对应这一轴。
- computational methods and modeling:
  - 中强支持。CCA、decoder、TME、RNN control 都是方法与模型比较的核心。
- brain-wide / distributed computation:
  - 中等支持。不是典型 brain-wide paper，但 striatum 扩展说明 preserved dynamics 可跨区域出现。
- multi-area communication and routing:
  - 仅弱支持。文章没有直接研究区域间 routing，但从 motor cortex 到 striatum 的扩展可以作为相关背景。
- causal perturbation and model-based intervention:
  - 直接支持较弱。没有真实因果操控，主要是分析与建模。
- NeuroAI and interpretable trained models:
  - 间接支持。RNN 对照更像是模型解释工具，而不是 NeuroAI 主线。

# Uncertainty / caveats
- 抽取文本对部分 Extended Data figure 的 panel 级别描述不完整，必要时要回原 PDF 核对图注和 panel 对应关系。
- `preserved latent dynamics` 是一个 operational construct，依赖 PCA/CCA/manifold dimensionality；虽然作者做了控制，但它仍不是一个独立于分析流程的裸事实。
- monkey 和 mouse 数据来自不同实验设置和不同任务复杂度，跨物种比较更适合当作趋势性支持，而不是严格等价比较。
- `covert planning` 在这篇里主要是 instructed-delay period 的 planning window，不应过度泛化成所有认知隐性过程。
- RNN 结果证明的是建模逻辑：相似输出不必然对应相似 internal dynamics；它不是对真实脑回路的因果证明。
- extracted text 的最后几页基本为空，说明正文主体已足够，但若要做 figure-panel 级别精读，还是需要回看 PDF。

# Candidate entries for future `paper_matrix.csv`
| field | proposed value |
|---|---|
| paper | `Preserved neural dynamics across animals performing similar behaviour` |
| year | `2023` |
| category | `representative experimental landmark` |
| field_axis | `population dynamics and neural manifolds; cross-animal conserved dynamics` |
| species | `monkey; mouse` |
| brain_area_or_scale | `motor cortex (M1/PMd), dorsolateral striatum` |
| task_or_behavior | `center-out reaching; sequential reaching; reach/pull joystick; instructed-delay planning` |
| neural_measurement | `spike-based population recordings` |
| neural_object | `preserved latent dynamics / neural manifold` |
| computation | `cross-animal alignment; decoding; control analysis; RNN comparison` |
| causal_status | `correlational + model-based control` |
| key_finding_short | `same-behavior latent dynamics are preserved across individuals and extend beyond motor cortex` |
| modeling_opportunity | `learn constraints that preserve shared latent geometry across individuals` |
| identifiers | `DOI 10.1038/s41586-023-06714-0; PMID 37938772; PMCID PMC10665198` |
| uncertainty | `alignment- and manifold-dependent operational definition; no direct perturbation` |

# Candidate entries for future `figure_evidence_table.csv`
| paper | figure_or_table | result_section | claim | evidence_summary | variable_or_neural_object | analysis_method | causal_status | relevance_to_research_question | uncertainty |
|---|---|---|---|---|---|---|---|---|---|
| `safaie2023PreservedNeuralDynamics` | `Fig. 1` | `Intro / hypothesis` | same-species animals may instantiate a shared neural landscape | schematic hypothesis only | latent dynamics | conceptual framing | speculative | frames the cross-animal conserved dynamics question | not empirical |
| `safaie2023PreservedNeuralDynamics` | `Fig. 2` | `Preserved latent dynamics across animals performing the same behaviour` | same-behavior latent dynamics are highly preserved across animals | cross-animal CCs exceed shuffled/TME controls; across-animal decoding works | motor cortical latent dynamics; kinematics | PCA + CCA; LSTM | correlational | central evidence for cross-animal population dynamics | depends on alignment choices |
| `safaie2023PreservedNeuralDynamics` | `Fig. 3` | `Necessity of behavioural similarity` | preservation persists in complex behavior but drops when behavior is less stereotyped | sequential reaching, condition/neuron subsampling, condition shuffling | motor cortical latent dynamics; condition structure | PCA + CCA; subsampling controls | correlational | links behavioral structure to preserved dynamics | matching strategy still matters |
| `safaie2023PreservedNeuralDynamics` | `Fig. 4` | `Preserved dynamics in dorsal striatum / covert behaviour` | preserved dynamics extend beyond cortex and into planning | mouse striatum and monkey planning period both align across animals | striatal / preparatory dynamics | PCA + CCA; Bayesian classifier | correlational | broadens the survey axis beyond one area | no direct causality |
| `safaie2023PreservedNeuralDynamics` | `Fig. 5` | `Behavioural similarity is not sufficient` | similar outputs can arise from distinct latent dynamics | RNNs match behavior while diverging in internal geometry as constraints increase | RNN latent dynamics; recurrent weights | constrained RNN simulation | model-based | gives a mechanistic counterexample for naive behavior-only interpretation | model-to-brain mapping indirect |
| `safaie2023PreservedNeuralDynamics` | `Extended Data Fig. 2 / 7` | `Controls` | preservation is robust to several control choices | TME, dimensionality, Procrustes, and static topology controls support the main claim | surrogate / aligned dynamics | control analyses | methodological support | strengthens confidence in the main survey claim | some panel mapping requires PDF check |
