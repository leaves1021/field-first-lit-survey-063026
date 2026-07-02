# Batch scope

- `batch_id`: `run001_first_batch`
- `pdf_check_plan_path`: `synthesis/figure_evidence_pdf_check_plan_run001.md`
- `note_paths`:
  - `notes/khilkevich2024BrainwideDynamicsLinking.md`
  - `notes/michaels2016NeuralPopulationDynamics.md`
  - `notes/safaie2023PreservedNeuralDynamics.md`
- `pdf_paths`:
  - `papers/raw_pdf/khilkevich2024BrainwideDynamicsLinking.pdf`
  - `papers/raw_pdf/michaels2016NeuralPopulationDynamics.pdf`
  - `papers/raw_pdf/safaie2023PreservedNeuralDynamics.pdf`
- `figure_evidence_table_csv_path`: `tables/figure_evidence_table.csv`
- 本步为人工/视觉 PDF inspection 结果记录，不更新 `figure_evidence_table.csv`，也不草拟 append rows。
- 特别边界：
  - 本步以 PDF 图面、panel、caption 的视觉确认为准。
  - 不把 extracted text 单独视为 visual confirmation。
  - 如果 note 中的 claim 强于图面支持，按 PDF/caption 收缩措辞。
  - conceptual、model-based、methodological、biological evidence 保持分开。

# Inspection summary

- 本次按计划完成了 10 个高优先级 figure 项的人工 PDF 复核：
  - Khilkevich 2024: `Fig. 3`, `Fig. 5`, `Fig. 6`
  - Michaels 2016: `Fig. 2`, `Fig. 5`, `Fig. 6`, `Fig. 7`
  - Safaie 2023: `Extended Data Fig. 2`, `Extended Data Fig. 7`, `Extended Data Fig. 9`
- 额外参考了 Safaie 主文 `Fig. 2-5` captions，用于校准主结论与 control 结论的边界，但不把这些 caption-only 观察单独提升为新候选条目。
- 总体判断：
  - `ready_for_figure_evidence_table`: 4
  - `revise_before_promotion`: 4
  - `hold_until_methods_checked`: 2
  - `do_not_promote`: 0
- 没有出现需要完全 `rejected` 的候选 claim，但有多处需要降级改写，主要原因是：
  - panel-to-claim mapping 比 note 里写得更窄；
  - 某些几何/方法性 claim 仍依赖 Methods 或 supplementary 定义；
  - control 图只能支持“稳健性/对照”而不是主结果扩写。

# Per-figure inspection results

## 1) Khilkevich 2024

### Entry 1

- paper: `Brain-wide dynamics linking sensation to action during decision-making`
- citekey: `khilkevich2024BrainwideDynamicsLinking`
- figure_or_table: `Fig. 3`
- panel or caption inspected: `panels d-o and figure caption`
- candidate claim from the note or PDF-check plan:
  - `Evidence integration is parallel and multi-regional rather than purely local.`
- visual confirmation result: `revised`
- final claim wording:
  - `Sequential-pulse facilitation, change-period ramping, and GLM-derived change-related activity are visible in selected non-visual and integrative regions, supporting distributed rather than purely local evidence integration.`
- final evidence_summary wording:
  - `The figure shows delayed/facilitated responses to repeated fast TF pulses and stronger change-period ramping in selected regions such as MOs and selected thalamic/hippocampal groups, rather than only early visual areas.`
- final causal_status:
  - `correlational`
- final uncertainty:
  - `The distributed-integration reading is supported visually, but the exact region grouping and panel-to-claim mapping for each facilitation/ramping subpanel should stay conservative.`
- proposed notes wording for future figure_evidence_table.csv:
  - `Use this as distributed evidence-integration evidence in selected regions; avoid claiming uniform brain-wide integration across all recorded areas.`
- ready for promotion:
  - `revise_before_promotion`

### Entry 2

- paper: `Brain-wide dynamics linking sensation to action during decision-making`
- citekey: `khilkevich2024BrainwideDynamicsLinking`
- figure_or_table: `Fig. 5`
- panel or caption inspected: `panels a-h and figure caption`
- candidate claim from the note or PDF-check plan:
  - `TF-responsive neurons are preferentially recruited into preparatory dynamics in integrative regions.`
- visual confirmation result: `revised`
- final claim wording:
  - `In selected integrative regions, TF pulse-response structure is aligned with preparatory activity, and TF-responsive subpopulations are recruited earlier than non-responsive populations during pre-lick build-up.`
- final evidence_summary wording:
  - `The figure visually supports stronger alignment between fast-TF response vectors and preparatory vectors in selected regions, plus earlier preparatory recruitment of TF-responsive units.`
- final causal_status:
  - `correlational`
- final uncertainty:
  - `The note wording needed to be narrowed from broad preferential recruitment to selected-region alignment and earlier recruitment; exact timing thresholds remain method-dependent.`
- proposed notes wording for future figure_evidence_table.csv:
  - `Keep the claim at the level of selected-region alignment and earlier preparatory recruitment; do not generalize to all integrative regions or imply causal initiation.`
- ready for promotion:
  - `revise_before_promotion`

### Entry 3

- paper: `Brain-wide dynamics linking sensation to action during decision-making`
- citekey: `khilkevich2024BrainwideDynamicsLinking`
- figure_or_table: `Fig. 6`
- panel or caption inspected: `panels a-m and figure caption`
- candidate claim from the note or PDF-check plan:
  - `Preparatory activity resides in movement-null subspace and sensory evidence responses align with that preparatory dimension rather than movement dimension.`
- visual confirmation result: `hold`
- final claim wording:
  - `The figure supports a separation between preparatory and movement-related population geometry, with sensory-evidence-related projections appearing more consistent with movement-null than movement dimensions.`
- final evidence_summary wording:
  - `The visual layout supports movement-null versus movement-dimension separation and shows pulse-related projections in the movement-null direction, but the exact geometric definitions and occupancy summaries are tightly tied to methods choices.`
- final causal_status:
  - `correlational / geometric analysis`
- final uncertainty:
  - `This is a high-value claim, but the geometric interpretation is too methods-dependent to promote without another pass through the Methods and supplementary definitions.`
- proposed notes wording for future figure_evidence_table.csv:
  - `Keep this claim on hold until movement-null / movement-dimension definitions, occupancy metrics, and projection conventions are rechecked against Methods.`
- ready for promotion:
  - `hold_until_methods_checked`

## 2) Michaels 2016

### Entry 4

- paper: `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
- citekey: `michaels2016NeuralPopulationDynamics`
- figure_or_table: `Fig. 2`
- panel or caption inspected: `panels a-e and figure caption`
- candidate claim from the note or PDF-check plan:
  - `CMPT distinguishes representational from dynamical rotational structure.`
- visual confirmation result: `confirmed`
- final claim wording:
  - `Within the paper's simulation framework, CMPT separates representational rotations that reappear after covariance-matched permutation from dynamical rotations that do not.`
- final evidence_summary wording:
  - `The figure directly shows that representational and dynamical simulations can both look rotational before control, but only the representational case regains rotational structure under covariance-matched permutation.`
- final causal_status:
  - `methodological / simulation-based`
- final uncertainty:
  - `The claim is visually well supported, but it remains a statistical-control result inside a simulation/model-comparison framework rather than direct biological evidence.`
- proposed notes wording for future figure_evidence_table.csv:
  - `State explicitly that this is CMPT-based methodological evidence distinguishing two simulated explanatory frameworks.`
- ready for promotion:
  - `ready_for_figure_evidence_table`

### Entry 5

- paper: `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
- citekey: `michaels2016NeuralPopulationDynamics`
- figure_or_table: `Fig. 5`
- panel or caption inspected: `panels a-g and figure caption`
- candidate claim from the note or PDF-check plan:
  - `An RNN can reproduce reaching-like velocity output while also yielding population dynamics.`
- visual confirmation result: `revised`
- final claim wording:
  - `In the RNN model, population-vector and velocity-regression analyses can reproduce movement-related structure even when single-neuron tuning and lag structure remain complex and unstable.`
- final evidence_summary wording:
  - `The figure shows good movement reconstruction and high regression fit in the RNN while also displaying variable preferred-direction structure, multiphasic responses, and wide lag distributions.`
- final causal_status:
  - `model-based`
- final uncertainty:
  - `This should remain model-only evidence; it supports a caution about fit quality versus mechanism, not a direct PMd/M1 claim.`
- proposed notes wording for future figure_evidence_table.csv:
  - `Keep the entry explicitly labeled as RNN/model-only evidence and frame it as a mechanism-inference caution.`
- ready for promotion:
  - `revise_before_promotion`

### Entry 6

- paper: `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
- citekey: `michaels2016NeuralPopulationDynamics`
- figure_or_table: `Fig. 6`
- panel or caption inspected: `panels a-c and figure caption`
- candidate claim from the note or PDF-check plan:
  - `Real PMd/M1 data and RNN both show strong rotational dynamics under CMPT.`
- visual confirmation result: `confirmed`
- final claim wording:
  - `Under the paper's shared jPCA/CMPT analysis framework, both example PMd/M1 data and the RNN model show strong rotational structure.`
- final evidence_summary wording:
  - `The figure visually compares PMd/M1 and RNN rotations, then contrasts them against permuted and covariance-matched controls, supporting the real-data/model comparison claim.`
- final causal_status:
  - `biological data + model comparison`
- final uncertainty:
  - `The figure supports the comparison directly, but the source dataset details and down-sampling match procedure should remain noted as analysis-context qualifiers.`
- proposed notes wording for future figure_evidence_table.csv:
  - `Treat this as the main real-data/model-comparison figure; do not upgrade it into causal mechanism evidence.`
- ready for promotion:
  - `ready_for_figure_evidence_table`

### Entry 7

- paper: `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
- citekey: `michaels2016NeuralPopulationDynamics`
- figure_or_table: `Fig. 7`
- panel or caption inspected: `panels a-b and figure caption`
- candidate claim from the note or PDF-check plan:
  - `Small sample sizes may not robustly support rotational conclusions.`
- visual confirmation result: `confirmed`
- final claim wording:
  - `The subset analysis indicates that rotational significance becomes much less stable at low neuron and condition counts, supporting a sample-size caution for rotation claims.`
- final evidence_summary wording:
  - `The heat maps and significance contours show that low-N / low-condition subsets weaken CMPT-based rotational significance and effect size.`
- final causal_status:
  - `methodological support`
- final uncertainty:
  - `This is a methods-caution figure rather than a biological finding, and exact numeric thresholds should be quoted conservatively.`
- proposed notes wording for future figure_evidence_table.csv:
  - `Use this as a statistical-power / sample-size caution; avoid overcommitting to a single hard threshold.`
- ready for promotion:
  - `ready_for_figure_evidence_table`

## 3) Safaie 2023

### Entry 8

- paper: `Preserved neural dynamics across animals performing similar behaviour`
- citekey: `safaie2023PreservedNeuralDynamics`
- figure_or_table: `Extended Data Fig. 2`
- panel or caption inspected: `panels A-H and figure caption`
- candidate claim from the note or PDF-check plan:
  - `Preserved dynamics are robust to several control choices.`
- visual confirmation result: `confirmed`
- final claim wording:
  - `Extended Data Fig. 2 supports the robustness of preserved latent dynamics across TME controls, manifold dimensionality choices, and an alternative linear alignment method.`
- final evidence_summary wording:
  - `The figure shows across-animal correlations exceeding TME and other lower-bound controls, preserved correspondence across manifold dimensionalities, and similar conclusions under Procrustes alignment.`
- final causal_status:
  - `methodological support`
- final uncertainty:
  - `This is a robustness/control figure rather than a primary discovery figure, so it should stay explicitly labeled as support for the main claim.`
- proposed notes wording for future figure_evidence_table.csv:
  - `Promote only as robustness-control evidence for preserved dynamics, not as a separate primary result.`
- ready for promotion:
  - `ready_for_figure_evidence_table`

### Entry 9

- paper: `Preserved neural dynamics across animals performing similar behaviour`
- citekey: `safaie2023PreservedNeuralDynamics`
- figure_or_table: `Extended Data Fig. 7`
- panel or caption inspected: `panels A-D and figure caption`
- candidate claim from the note or PDF-check plan:
  - `Static topological alignment is a weaker control than time-varying latent alignment.`
- visual confirmation result: `revised`
- final claim wording:
  - `The figure shows that alignment based on static/topological organization is insufficient to recover the stronger preserved-dynamics correlations obtained from latent-dynamics alignment.`
- final evidence_summary wording:
  - `The topology-alignment comparisons fall below the latent-dynamics alignment comparisons, indicating that static manifold topology alone does not account for the main preserved-dynamics result.`
- final causal_status:
  - `methodological support`
- final uncertainty:
  - `This should stay framed as a control insufficiency claim, not as a new positive discovery about neural coding.`
- proposed notes wording for future figure_evidence_table.csv:
  - `Keep this entry explicitly labeled as a control showing that topological alignment alone is insufficient.`
- ready for promotion:
  - `revise_before_promotion`

### Entry 10

- paper: `Preserved neural dynamics across animals performing similar behaviour`
- citekey: `safaie2023PreservedNeuralDynamics`
- figure_or_table: `Extended Data Fig. 9`
- panel or caption inspected: `caption/text cross-reference; main comparison discussed in article text`
- candidate claim from the note or PDF-check plan:
  - `Same-task cross-animal latent dynamics are more preserved than same-animal cross-task dynamics.`
- visual confirmation result: `hold`
- final claim wording:
  - `The article text supports a control comparison in which related-but-distinct tasks within one animal preserve latent dynamics less well than the same task across animals, but this item should remain on hold until the exact Extended Data panel is rechecked directly.`
- final evidence_summary wording:
  - `The current pass supports the narrative role of this control, but the exact panel-level figure mapping was not clean enough in the available inspection pass to promote safely.`
- final causal_status:
  - `correlational / analytical`
- final uncertainty:
  - `The claim is plausible from the text and plan context, but the direct panel-to-claim mapping was not visually stable enough in this pass.`
- proposed notes wording for future figure_evidence_table.csv:
  - `Do not promote yet; re-open the exact Extended Data Fig. 9 panel and caption before any figure-level row is drafted.`
- ready for promotion:
  - `hold_until_methods_checked`

# Claims ready for promotion

以下 4 项可以进入后续单独的 `figure_evidence_table` append planning，但仍应保持当前保守措辞：

1. `michaels2016NeuralPopulationDynamics` - `Fig. 2`
   - CMPT 区分 representational 与 dynamical rotational structure
   - 类型：`methodological / simulation-based`

2. `michaels2016NeuralPopulationDynamics` - `Fig. 6`
   - PMd/M1 与 RNN 在共享分析框架下都显示强 rotational structure
   - 类型：`biological data + model comparison`

3. `michaels2016NeuralPopulationDynamics` - `Fig. 7`
   - 低 neuron / condition 数量下 rotational significance 不稳健
   - 类型：`methodological support`

4. `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 2`
   - preserved latent dynamics 对 TME、dimensionality、Procrustes 等 control 具有稳健性
   - 类型：`methodological support`

# Claims requiring revision

以下 4 项不建议原文照搬，需先按本文件中的收缩版本改写：

1. `khilkevich2024BrainwideDynamicsLinking` - `Fig. 3`
   - 从泛化的 `parallel and multi-regional` 改为“selected non-visual and integrative regions”。

2. `khilkevich2024BrainwideDynamicsLinking` - `Fig. 5`
   - 从泛化的 `preferentially recruited into preparatory dynamics in integrative regions` 改为“selected-region alignment and earlier recruitment”。

3. `michaels2016NeuralPopulationDynamics` - `Fig. 5`
   - 明确限制为 `model-based` 图，不与 PMd/M1 biological evidence 混写。

4. `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 7`
   - 明确写成“static/topological alignment alone is insufficient”的 control 结论，而不是正向主发现。

# Claims rejected or held

本轮没有需要完全 `rejected` 的条目，但以下 2 项应继续 `hold`：

1. `khilkevich2024BrainwideDynamicsLinking` - `Fig. 6`
   - 原因：movement-null / movement-dimension 的几何定义、occupancy summary、projection convention 都较依赖 Methods，当前适合保守保留。

2. `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 9`
   - 原因：本次人工复核未稳定锁定足够清晰的 panel-to-claim mapping；只能确认这是一个相关 control 方向，不能安全升格为 figure-level row。

# Final recommendation

- 下一步不应直接修改 `tables/figure_evidence_table.csv`。
- 更稳妥的后续顺序是：
  1. 先基于本文件创建一个单独的 `figure_evidence_table_append_plan`；
  2. 只纳入当前标记为 `ready_for_figure_evidence_table` 的 4 项；
  3. 对 `revise_before_promotion` 的 4 项，先按本文件给出的 final wording 更新候选措辞，再考虑进入 append plan；
  4. 对 `hold_until_methods_checked` 的 2 项，先做一次更细的 Methods / supplementary 复核，再决定是否保留为候选 figure evidence。
- 特别提醒：
  - Khilkevich 的 `Fig. 3` 和 `Fig. 5` 已经足够支持较弱版本 claim，但还不适合用更强的 brain-wide 泛化措辞。
  - Michaels 的 `Fig. 2 / 6 / 7` 是当前最适合先推进到 append plan 的一组，因为 visual confirmation 最直接、证据边界也最清楚。
  - Safaie 的 Extended Data controls 很有价值，但应始终明确标成 control / robustness evidence，而不是替代主图主结论。
