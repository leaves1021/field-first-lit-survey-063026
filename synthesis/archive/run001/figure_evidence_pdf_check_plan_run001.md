# Run001 figure-level PDF check plan

目的：
- 在任何 `figure_evidence_table.csv` 条目被正式推进之前，先对高优先级 figure / panel 做人工 PDF 复核。
- 这个计划只针对三篇 Run001 first-batch note 中已经写出的候选 figure 证据，不扩展到其他图。

范围：
- `notes/khilkevich2024BrainwideDynamicsLinking.md`
- `notes/michaels2016NeuralPopulationDynamics.md`
- `notes/safaie2023PreservedNeuralDynamics.md`
- 参考 `synthesis/first_batch_note_qc_run001.md`

## 1) Khilkevich 2024

citekey: `khilkevich2024BrainwideDynamicsLinking`

| paper | citekey | figure/table | candidate claim from note | what must be checked in the PDF | expected result if confirmed | possible downgrade if not confirmed | current candidate row status | proposed notes wording for future `figure_evidence_table.csv` |
|---|---|---|---|---|---|---|---|---|
| `Brain-wide dynamics linking sensation to action during decision-making` | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 3` | `Evidence integration is parallel and multi-regional rather than purely local.` | 核对 sequential-pulse facilitation、change-period ramping 和 GLM kernel 的 panel 对应关系；确认哪些 region group 真的支持这句结论。 | panel-to-claim mapping 清楚，且 facilitation / ramping 的区域归属与 note 一致。 | 若 panel 对应不清，降级为“部分非视觉区显示与 evidence integration 相关的 pulse response”，并保留不确定性。 | `ready_after_pdf_check` | `Panel-level confirmation still needed for facilitation, ramping, and region grouping.` |
| `Brain-wide dynamics linking sensation to action during decision-making` | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 5` | `TF-responsive neurons are preferentially recruited into preparatory dynamics in integrative regions.` | 核对 region ordering、TF pulse response 与 preparatory vector 的 alignment、以及 timing thresholds 的定义。 | 能确认 integrative regions 的 alignment 强于 non-integrative visual regions，且 timing 语义和 note 一致。 | 若 alignment 或阈值定义不稳，降级为“evidence-encoding activity and preparatory activity are aligned in selected regions”。 | `needs_rewording` | `Alignment, region ordering, and timing thresholds need visual confirmation.` |
| `Brain-wide dynamics linking sensation to action during decision-making` | `khilkevich2024BrainwideDynamicsLinking` | `Fig. 6` | `Preparatory activity resides in movement-null subspace and sensory evidence responses align with that preparatory dimension rather than movement dimension.` | 核对 movement-null vs movement dimensions、subspace occupancy、projection geometry 与各面板的几何定义。 | 能确认 movement-null / movement subspace 的几何关系，以及 evidence responses 的投影方向。 | 若几何定义不清，降级为“subspace-level preparatory vs movement separation”，并避免具体方向性表述。 | `hold_until_methods_checked` | `Movement-null and movement-subspace geometry need explicit PDF confirmation before promotion.` |

## 2) Michaels 2016

citekey: `michaels2016NeuralPopulationDynamics`

| paper | citekey | figure/table | candidate claim from note | what must be checked in the PDF | expected result if confirmed | possible downgrade if not confirmed | current candidate row status | proposed notes wording for future `figure_evidence_table.csv` |
|---|---|---|---|---|---|---|---|---|
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | `michaels2016NeuralPopulationDynamics` | `Fig. 2` | `CMPT distinguishes representational from dynamical rotational structure.` | 核对 representational model、dynamical model 和 CMPT 的 panel mapping；确认对照与 permutation 逻辑对应。 | 能清楚区分 representational 和 dynamical 两种模拟情形，并且 CMPT 的作用和 note 一致。 | 若 panel mapping 复杂，降级为“statistical control comparison between representational and dynamical simulations”。 | `hold_until_methods_checked` | `CMPT panel mapping and permutation-control logic need PDF confirmation.` |
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | `michaels2016NeuralPopulationDynamics` | `Fig. 5` | `An RNN can reproduce reaching-like velocity output while also yielding population dynamics.` | 核对 population vector、velocity regression、lag definitions，以及这些分析与图面是否真正对应。 | 能确认这张图主要展示 model-only 的 representational / regression behavior，而不是生物学数据。 | 若定义或图面不稳，降级为“RNN fit illustration with variable tuning and lag structure”。 | `needs_rewording` | `Keep this as model-only illustration; do not merge with biological evidence.` |
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | `michaels2016NeuralPopulationDynamics` | `Fig. 6` | `Real PMd/M1 data and RNN both show strong rotational dynamics under CMPT.` | 核对真实 PMd/M1 vs RNN 的 rotational structure、source dataset、subset matching 和图例来源。 | 能确认真实数据和模型都在同一分析框架下呈现 rotational structure。 | 若 source dataset 或 matching 不清，降级为“real-data/model comparison of rotational structure”。 | `ready_after_pdf_check` | `Real-data and model-comparison evidence; verify source dataset and subset matching in PDF.` |
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | `michaels2016NeuralPopulationDynamics` | `Fig. 7` | `Small sample sizes may not robustly support rotational conclusions.` | 核对 neuron / condition subsampling thresholds，以及显著性曲线的稳定区间。 | 能确认 sample-size caution 的具体阈值，并保留方法学警告。 | 若阈值读不稳，降级为“subset resampling caution”或不单列证据。 | `hold_until_methods_checked` | `Subsampling thresholds should be checked before promotion.` |

## 3) Safaie 2023

citekey: `safaie2023PreservedNeuralDynamics`

| paper | citekey | figure/table | candidate claim from note | what must be checked in the PDF | expected result if confirmed | possible downgrade if not confirmed | current candidate row status | proposed notes wording for future `figure_evidence_table.csv` |
|---|---|---|---|---|---|---|---|---|
| `Preserved neural dynamics across animals performing similar behaviour` | `safaie2023PreservedNeuralDynamics` | `Extended Data Fig. 2` | `Preserved dynamics are robust to several control choices.` | 核对 TME、manifold dimensionality 和 control comparison 的 panel 级对应关系。 | 能确认这些控制主要是在支持 preserved dynamics 的稳健性，而不是新结论。 | 若控制 panel 对应不清，降级为“robustness controls for preserved dynamics”。 | `ready_after_pdf_check` | `Control comparisons support robustness, but panel-level confirmation is still needed.` |
| `Preserved neural dynamics across animals performing similar behaviour` | `safaie2023PreservedNeuralDynamics` | `Extended Data Fig. 7` | `Static topological alignment is a weaker control than time-varying latent alignment.` | 核对静态 topological alignment control 的面板、比较对象和结论。 | 能确认 static topological alignment 只作为对照，不应被写成主证据。 | 若图面不稳，降级为“alignment control comparison”并保留不确定性。 | `ready_after_pdf_check` | `Static topological alignment should remain a control, not a primary evidence claim.` |
| `Preserved neural dynamics across animals performing similar behaviour` | `safaie2023PreservedNeuralDynamics` | `Extended Data Fig. 9` | `Same-task cross-animal latent dynamics are more preserved than same-animal cross-task dynamics.` | 核对 cross-task / cross-animal comparison 的 panel 级对应关系和所比较的任务。 | 能确认这个对比只作为补充控制，用来支持“task similarity is not enough”。 | 若比较关系不清，降级为“related-task comparison control”或不单列。 | `ready_after_pdf_check` | `Cross-task / cross-animal comparison should stay explicitly labeled as a control.` |

### 条件性补查

如果后续在整理 Safaie 的主图候选行时，需要把 Fig. 2-5 的主图 caption 也写得更紧，可以再做一次条件性补查：

| paper | citekey | figure/table | candidate claim from note | what must be checked in the PDF | expected result if confirmed | possible downgrade if not confirmed | current candidate row status | proposed notes wording for future `figure_evidence_table.csv` |
|---|---|---|---|---|---|---|---|---|
| `Preserved neural dynamics across animals performing similar behaviour` | `safaie2023PreservedNeuralDynamics` | `Fig. 2-5 captions` | `Main cross-animal preserved-dynamics claim and its behavioral-similarity control wording.` | 核对主图 caption 的精确措辞，避免把控制分析写成主证据。 | 主图 caption 与 note 的 claim 保持一致，但仍以 figure 级确认后的措辞为准。 | 若 caption 与 note 不完全一致，按 caption 收缩表述。 | `hold_until_methods_checked` | `Use caption-level wording only after visual confirmation; keep controls separate from the main claim.` |

## Promotion rules

- 不要在 panel-to-claim 没有视觉确认前推进任何 figure claim。
- 概念图、示意图和实证图要分开处理，不能混写。
- model-based evidence 要和 biological evidence 分开。
- `causal_status` 要保持保守，优先用 `correlational`、`methodological / simulation-based`、`model-based`、`biological data + model comparison` 这类措辞。
- 只靠 extracted text 的句子不应当被当作 confirmed figure-level evidence。

## Future results file

未来的结果文件将写成：

`synthesis/figure_evidence_pdf_check_results_run001.md`

建议记录字段：
- inspected figure / panel
- confirmed / revised / rejected
- final wording
- final causal_status
- whether ready for `figure_evidence_table.csv`

建议工作顺序：
1. 先核对 Khilkevich `Fig. 3 / 5 / 6`
2. 再核对 Michaels `Fig. 2 / 5 / 6 / 7`
3. 最后核对 Safaie `Extended Data Fig. 2 / 7 / 9`
4. 需要时再补 Safaie `Fig. 2-5` 的 caption 级检查
