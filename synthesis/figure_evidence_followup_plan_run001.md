# Batch scope

- `batch_id`: `run001_first_batch`
- this follow-up plan covers only the remaining Run001 figure-level items that were not appended to `tables/figure_evidence_table.csv`
- source status references:
  - `synthesis/run001_first_batch_completion_summary.md`
  - `synthesis/figure_evidence_pdf_check_results_run001.md`
  - `synthesis/figure_evidence_table_append_plan_run001_first_batch.md`
- covered items:
  - later revision pass:
    - `khilkevich2024BrainwideDynamicsLinking` - `Fig. 3`
    - `khilkevich2024BrainwideDynamicsLinking` - `Fig. 5`
    - `michaels2016NeuralPopulationDynamics` - `Fig. 5`
    - `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 7`
  - methods / supplementary check:
    - `khilkevich2024BrainwideDynamicsLinking` - `Fig. 6`
    - `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 9`

# Items requiring revision pass

## `khilkevich2024BrainwideDynamicsLinking` - `Fig. 3`

- current issue:
  - 当前 note/候选 row 的 claim 仍偏宽，容易把 selected integrative regions 的证据写成更泛化的 brain-wide distributed integration 结论。
- safer final wording candidate:
  - `Sequential-pulse facilitation, change-period ramping, and GLM-derived change-related activity are visible in selected non-visual and integrative regions, supporting distributed rather than purely local evidence integration.`
- what needs to be checked before promotion:
  - panel `d-o` 的 facilitation、ramping、GLM kernel 是否都能稳定对应到这个较弱版本的 claim
  - region grouping 是否始终只支持 `selected regions`，而不是更强的全局泛化
- whether it may enter a later append plan:
  - yes, if the wording is kept narrow and panel-to-claim mapping is reconfirmed

## `khilkevich2024BrainwideDynamicsLinking` - `Fig. 5`

- current issue:
  - 当前表述中的 `preferentially recruited into preparatory dynamics in integrative regions` 仍可能强于图面支持，尤其容易滑向更强的 causal/initiation 语气。
- safer final wording candidate:
  - `In selected integrative regions, TF pulse-response structure is aligned with preparatory activity, and TF-responsive subpopulations are recruited earlier than non-responsive populations during pre-lick build-up.`
- what needs to be checked before promotion:
  - region ordering 是否稳定支持 `selected integrative regions`
  - timing thresholds 与 alignment window 是否只支持“earlier recruitment / stronger alignment”，而不支持更强因果措辞
- whether it may enter a later append plan:
  - yes, if the row is rewritten conservatively and avoids causal-initiation language

## `michaels2016NeuralPopulationDynamics` - `Fig. 5`

- current issue:
  - 当前风险不是 panel 错认，而是 evidence type 漂移：这张图是 RNN / model-only figure，很容易被误写成 PMd/M1 biological evidence。
- safer final wording candidate:
  - `In the RNN model, population-vector and velocity-regression analyses can reproduce movement-related structure even when single-neuron tuning and lag structure remain complex and unstable.`
- what needs to be checked before promotion:
  - regression fit、lag distribution、trajectory reconstruction 的图面细节是否都支持 model-only caution framing
  - note/append row 中是否把 `fit quality` 与 `mechanism inference` 清楚分开
- whether it may enter a later append plan:
  - yes, but only as explicitly `model-based` evidence and not as real-data support

## `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 7`

- current issue:
  - 当前风险是 control figure 被写成正向主发现；这张图更适合作为 “topology-only alignment is insufficient” 的 control insufficiency result。
- safer final wording candidate:
  - `The figure shows that alignment based on static/topological organization is insufficient to recover the stronger preserved-dynamics correlations obtained from latent-dynamics alignment.`
- what needs to be checked before promotion:
  - caption 与 panels A-D 是否始终支持“insufficient control”而不是“new positive mechanism”
  - notes wording 是否明确标成 control / robustness evidence
- whether it may enter a later append plan:
  - yes, if it remains explicitly labeled as control evidence

# Items requiring methods / supplementary check

## `khilkevich2024BrainwideDynamicsLinking` - `Fig. 6`

- current uncertainty:
  - 这条 claim 的科学价值很高，但 movement-null / movement-dimension 的几何定义、occupancy、projection conventions 都很方法依赖，当前还不够适合直接进表。
- exact Methods / supplementary / caption issue to inspect:
  - movement-null 与 movement dimensions 的正式定义
  - first movement-null dimension 与 movement dimension 的 projection conventions
  - region-by-region occupancy summary 是否与主图/Extended Data 的方法描述完全一致
- what evidence would be needed before promotion:
  - 一个能被图面、caption 和 Methods 同时支持的更窄版本 claim
  - 对 subspace geometry、occupancy metric、projection direction 的明确方法锚点

## `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 9`

- current uncertainty:
  - 当前主要问题不是 wording 太强，而是 panel-to-claim mapping 仍不够稳定；文本支持它是一个有用 control，但图级证据还没锁死。
- exact Methods / supplementary / caption issue to inspect:
  - Extended Data Fig. 9 的 exact panel / caption wording
  - same-animal cross-task 与 same-task across-animal 的具体比较对象、alignment metric、control framing
- what evidence would be needed before promotion:
  - 能明确指向这条比较关系的 panel/caption 锚点
  - 足够清晰的 comparison framing，确保它被写成 supplementary control，而不是主结果扩展

# Proposed follow-up order

1. First pass the low-risk revision items:
   - `khilkevich2024BrainwideDynamicsLinking` - `Fig. 3`
   - `khilkevich2024BrainwideDynamicsLinking` - `Fig. 5`
   - `michaels2016NeuralPopulationDynamics` - `Fig. 5`
   - `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 7`
2. Then handle the methods-dependent items:
   - `khilkevich2024BrainwideDynamicsLinking` - `Fig. 6`
   - `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 9`

This order is conservative because the first group mostly needs wording control and evidence-boundary cleanup, while the second group still depends on Methods / supplementary reinspection before any promotion-safe claim can be drafted.

# Boundaries

- this plan does not update any CSV files
- this plan does not create append rows
- this plan does not modify notes
- any future `figure_evidence_table.csv` append still requires:
  - a separate append plan
  - user approval
  - conservative rechecking of evidence type and wording

# Final recommendation

The safest next move is to process the four revision-pass items first, because they are closest to promotion-ready status and mostly need controlled wording cleanup rather than deep methodological reinterpretation. The two methods-dependent items should remain second-stage work until their figure/caption/Methods anchors are explicitly rechecked.

ready_for_user_review
