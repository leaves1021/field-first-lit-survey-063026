# Batch scope

- `batch_id`: `run001_first_batch`
- `pdf_check_results_path`: `synthesis/figure_evidence_pdf_check_results_run001.md`
- `note_paths`:
  - `notes/michaels2016NeuralPopulationDynamics.md`
  - `notes/safaie2023PreservedNeuralDynamics.md`
  - `notes/khilkevich2024BrainwideDynamicsLinking.md`
- `figure_evidence_table_csv_path`: `tables/figure_evidence_table.csv`
- `special_cautions`:
  - 只包含标记为 `ready_for_figure_evidence_table` 的 claims。
  - 不包含 `revise_before_promotion`。
  - 不包含 `hold_until_methods_checked`。
  - 不更新 `figure_evidence_table.csv`。
  - 不为 Khilkevich `Fig. 3 / Fig. 5 / Fig. 6` 草拟 rows。
  - 不为 Michaels `Fig. 5` 草拟 rows。
  - 不为 Safaie `Extended Data Fig. 7 / Extended Data Fig. 9` 草拟 rows。
  - 所有 proposed rows 都必须能直接追溯到 `synthesis/figure_evidence_pdf_check_results_run001.md`。

# Source PDF-check results

本 append plan 只从 `synthesis/figure_evidence_pdf_check_results_run001.md` 中挑选 `ready_for_figure_evidence_table` 的条目，并保留保守措辞。

可推进的 4 条：

1. `michaels2016NeuralPopulationDynamics` - `Fig. 2`
2. `michaels2016NeuralPopulationDynamics` - `Fig. 6`
3. `michaels2016NeuralPopulationDynamics` - `Fig. 7`
4. `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 2`

其余条目都进入 `# Claims excluded from this append plan`。

# Proposed figure_evidence_table.csv append rows

以下 rows 使用 `figure_evidence_table.csv` 的精确表头：

```text
paper,citekey,figure_or_table,result_section,page,claim,evidence_summary,variable_or_neural_object,analysis_method,causal_status,relevance_to_research_question,uncertainty,notes
```

| paper | citekey | figure_or_table | result_section | page | claim | evidence_summary | variable_or_neural_object | analysis_method | causal_status | relevance_to_research_question | uncertainty | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | `michaels2016NeuralPopulationDynamics` | `Fig. 2` | `Disrupting the underlying condition structure—covariance-matched permutation test` | `5-8` | `Within the paper's simulation framework, CMPT separates representational rotations that reappear after covariance-matched permutation from dynamical rotations that do not.` | `The figure directly shows that representational and dynamical simulations can both look rotational before control, but only the representational case regains rotational structure under covariance-matched permutation.` | `simulated representational model; dynamical model; condition structure; RGR` | `methodological / simulation-based` | `Establishes the key statistical-control logic needed to interpret rotation claims in population-dynamics analyses.` | `This is a simulation/control result, not direct biological evidence.` | `CMPT-based methodological evidence distinguishing two simulated explanatory frameworks.` |
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | `michaels2016NeuralPopulationDynamics` | `Fig. 6` | `Significant rotational structure in PMd/M1 data and RNN model` | `12-14` | `Under the paper's shared jPCA/CMPT analysis framework, both example PMd/M1 data and the RNN model show strong rotational structure.` | `The figure visually compares PMd/M1 and RNN rotations, then contrasts them against permuted and covariance-matched controls, supporting the real-data/model comparison claim.` | `PMd/M1 population activity; RNN activity` | `jPCA; CMPT; RGR; circularity` | `biological data + model comparison` | `Provides the main bridge between biological data and the dynamical-systems interpretation.` | `Keep dataset and down-sampling qualifiers conservative.` | `Real-data/model-comparison evidence; do not upgrade into causal mechanism evidence.` |
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | `michaels2016NeuralPopulationDynamics` | `Fig. 7` | `Number of neurons and conditions required for statistically significant rotations` | `12-14` | `The subset analysis indicates that rotational significance becomes much less stable at low neuron and condition counts, supporting a sample-size caution for rotation claims.` | `The heat maps and significance contours show that low-N / low-condition subsets weaken CMPT-based rotational significance and effect size.` | `subset size; statistical significance` | `subset resampling` | `methodological support` | `Important cautionary note for interpreting low-N rotation claims.` | `Exact numeric thresholds should be quoted conservatively.` | `Statistical-power / sample-size caution; avoid overcommitting to a single hard threshold.` |
| `Preserved neural dynamics across animals performing similar behaviour` | `safaie2023PreservedNeuralDynamics` | `Extended Data Fig. 2` | `Additional verification of preserved latent dynamics` | `14` | `Extended Data Fig. 2 supports the robustness of preserved latent dynamics across TME controls, manifold dimensionality choices, and an alternative linear alignment method.` | `The figure shows across-animal correlations exceeding TME and other lower-bound controls, preserved correspondence across manifold dimensionalities, and similar conclusions under Procrustes alignment.` | `surrogate dynamics; alignment robustness` | `control analyses` | `methodological support` | `Strengthens confidence in the main cross-animal preserved-dynamics claim.` | `Panel mapping remains tied to PDF captions and should stay conservative.` | `Promote only as robustness-control evidence for preserved dynamics, not as a separate primary result.` |

## Duplicate / conflict check

- Existing `tables/figure_evidence_table.csv` rows were checked by `paper + citekey + figure_or_table`.
- No exact duplicate row was found for any of the 4 proposed rows.
- No near-duplicate conflict was found with the current entries in `tables/figure_evidence_table.csv`.
- Existing rows are currently limited to `vyas_2020_computation_through_neural` and `ye_2026_brainwide_topographic_coordination`, so the proposed `Michaels` and `Safaie` rows do not collide with them.

## Claims excluded from this append plan

以下条目均不进入本次 append plan：

### 需要 later revision pass 的条目

- `khilkevich2024BrainwideDynamicsLinking` - `Fig. 3`
  - 需要把泛化的 `parallel and multi-regional` 收缩为 `selected non-visual and integrative regions` 一类更窄措辞。
- `khilkevich2024BrainwideDynamicsLinking` - `Fig. 5`
  - 需要把 `preferentially recruited` 收缩为 `selected-region alignment and earlier recruitment`。
- `michaels2016NeuralPopulationDynamics` - `Fig. 5`
  - 这是 model-only 证据，必须继续与 PMd/M1 biological evidence 分开。
- `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 7`
  - 这是 control insufficiency 结论，应继续保持为控制图，而不是主发现。

### 需要 methods / supplementary 复核的条目

- `khilkevich2024BrainwideDynamicsLinking` - `Fig. 6`
  - movement-null / movement-dimension 的几何定义和 occupancy summary 仍然方法依赖性很强。
- `safaie2023PreservedNeuralDynamics` - `Extended Data Fig. 9`
  - 本轮视觉复核没有稳定锁定足够清楚的 panel-to-claim mapping，不能安全升格。

## Field normalization notes

- `figure_or_table` 保持与 PDF-check 结果一致，必要时保留 `Fig. 2` / `Fig. 6` / `Extended Data Fig. 2` 这类原始命名。
- `causal_status` 全部保持保守：
  - `methodological / simulation-based`
  - `biological data + model comparison`
  - `methodological support`
- control / robustness 图必须继续标明是 control evidence，不要写成主 discovery。
- model-based 结果必须继续与 biological evidence 分开写。
- `uncertainty` 保持明确，不要把方法依赖性写没。
- 对 `Michaels Fig. 6` 和 `Safaie ED Fig. 2` 的措辞只做最小化规范化，不做强度升级。

## Final recommendation

- 本次可推进的 append rows 数量为 `4`。
- duplicate / conflict check 未发现冲突。
- excluded claims 中有 4 条需要 later revision pass，2 条需要 methods / supplementary 复核。
- 这份 append plan 足够保守，可以交由用户审核后再进入下一步的 CSV append 流程。

ready_for_user_approval
