# Run001 第一批 note QC

范围：
- `notes/khilkevich2024BrainwideDynamicsLinking.md`
- `notes/michaels2016NeuralPopulationDynamics.md`
- `notes/safaie2023PreservedNeuralDynamics.md`

目标：
- 在任何内容进入 `paper_matrix.csv` 或 `figure_evidence_table.csv` 之前，先确认 note 结构、证据锚点、图级审查需求和候选表格式是否足够稳妥。

## 总体判断

三篇 note 都已经覆盖了核心阅读结构，也都把 paper claim、extracted evidence、model interpretation、survey interpretation 分开写了。  
当前最主要的阻塞点不是 note 本身，而是 figure-level 条目要不要在进表前再做一次 PDF 核验，尤其是多图、多 panel、以及 extended data 比较多的那几篇。

| paper | schema completeness | evidence quality | readiness |
|---|---|---|---|
| `khilkevich2024BrainwideDynamicsLinking` | complete | good | `figure_evidence_ready_after_pdf_check` |
| `michaels2016NeuralPopulationDynamics` | complete | good | `figure_evidence_ready_after_pdf_check` |
| `safaie2023PreservedNeuralDynamics` | complete | good, but some control panels still need核验 | `figure_evidence_ready_after_pdf_check` |

## 逐篇 QC

### 1) `notes/khilkevich2024BrainwideDynamicsLinking.md`

**Schema completeness**
- 具备全部必需部分：citation metadata、summary、research question、task / behavior、species / brain area / recording method、neural object、main findings、figure-by-figure evidence map、modeling relevance、field-axis relation、uncertainty / caveats、候选 `paper_matrix` 行、候选 `figure_evidence_table` 行。
- 结构完整，且每个主发现都给出了 figure / page / result-section 锚点。

**Evidence quality**
- 主发现与图页锚点的对应关系整体清楚。
- paper claim 和作者解释分开写得比较干净。
- biological evidence、methodological evidence、model / agent interpretation 基本都有区分。
- `causal_status` 用法保守，主要保持在 `correlational / observational` 或 `correlational / geometric analysis`。
- 需要注意的是，`learning enables widespread sensory integration` 这类表述更适合在 QC 后续表述成训练相关对照，而不是强因果。

**Promotion readiness**
- `paper_matrix`: `paper_matrix_ready_after_minor_cleanup`
- `figure_evidence`: `figure_evidence_ready_after_pdf_check`

**Manual PDF inspection needs**
- `Fig. 3`：尤其是 sequential-pulse facilitation、change-period ramping、GLM kernel 相关的 panel 对应，当前 note 已明确 `j-o` 是重点，但 panel-to-claim 仍需 PDF 复核。
- `Fig. 5`：region ordering、TF pulse response 和 preparatory vector 对齐、timing threshold 的具体 panel。
- `Fig. 6`：movement-null vs movement subspace 的几何定义、各区域 occupancy，以及 projection 关系。

**Candidate table consistency**
- `paper_matrix` 候选行：**不完全符合**表头，主要问题是缺少 `citekey` 字段。
- `figure_evidence_table` 候选行：**不完全符合**表头，主要问题是缺少 `notes` 字段。

**Suggested cleanup before promotion**
- 给候选 `paper_matrix` 行补上 `citekey`。
- 给候选 `figure_evidence_table` 行补上 `notes`。
- 把少数较强的表述再压回到训练相关 / 对照相关的保守语言。

---

### 2) `notes/michaels2016NeuralPopulationDynamics.md`

**Schema completeness**
- 结构完整，必需部分齐全。
- 已把 simulation-based evidence、real PMd/M1 comparison、methodological control 和模型解释拆开。

**Evidence quality**
- 主发现都有 figure / page / result-section 锚点。
- biological data、simulation/model evidence、methodological comparison 分离得比较清楚。
- `causal_status` 也写得足够保守，核心结果仍然是 `methodological / simulation-based` 或 `biological data + model comparison`。
- 这篇最值得保留的不是“结论很强”，而是“方法学界限讲得很清楚”。

**Promotion readiness**
- `paper_matrix`: `paper_matrix_ready_after_minor_cleanup`
- `figure_evidence`: `figure_evidence_ready_after_pdf_check`

**Manual PDF inspection needs**
- `Fig. 2`：representational model / dynamical model / CMPT 的对应关系需要核对原图。
- `Fig. 5`：population vector、velocity regression、lag 分布的图面细节需要再看一次 PDF。
- `Fig. 6`：真实 PMd/M1 与 RNN 的 rotational structure 对比，最好确认 source dataset 和 subset matching。
- `Fig. 7`：neuron / condition subsampling 的阈值曲线，适合在进表前再核对。

**Candidate table consistency**
- `paper_matrix` 候选行：**不完全符合**表头，主要问题是缺少 `citekey` 字段。
- `figure_evidence_table` 候选行：**不完全符合**表头，主要问题是缺少 `notes` 字段。

**Suggested cleanup before promotion**
- 给候选 `paper_matrix` 行补上 `citekey`。
- 给候选 `figure_evidence_table` 行补上 `notes`。
- `category` 和 `field_axis` 的措辞可以再贴近仓库既有风格，但目前不算硬伤。

---

### 3) `notes/safaie2023PreservedNeuralDynamics.md`

**Schema completeness**
- 结构完整，必需部分齐全。
- 主发现、模型意义和 survey 轴映射都写出来了。
- 但 note 里有一处可见的小拼写问题：`stereoptyed` 应为 `stereotyped`。

**Evidence quality**
- 主发现大体都有 figure / page 锚点。
- paper claim 与 extracted evidence 分离是清楚的。
- biological evidence 与 RNN / modeling evidence 也有分离。
- `causal_status` 保持在 correlational / model-based 级别，整体是保守的。
- 当前主要不足不在主图，而在 extended data controls 的 panel-level 核验还不够完整。

**Promotion readiness**
- `paper_matrix`: `paper_matrix_ready_after_minor_cleanup`
- `figure_evidence`: `figure_evidence_ready_after_pdf_check`

**Manual PDF inspection needs**
- `Extended Data Fig. 2`：建议逐 panel 核对，尤其是 A-H 中关于 TME、manifold dimensionality、以及 control comparison 的部分。
- `Extended Data Fig. 7`：static topological alignment control 的 panel 级对应需要复核。
- `Extended Data Fig. 9`：cross-task / cross-animal comparison 的 panel 级对应需要复核。
- 另外，若要把 `Fig. 2-5` 的补充 control 也写成表格条目，建议一并回看 PDF 的 caption。

**Candidate table consistency**
- `paper_matrix` 候选行：**不完全符合**表头，主要问题是当前是 compact table / prose 混写，不是严格 row schema；同时缺少 `citekey`，`notes` 也未按表头形式给出。
- `figure_evidence_table` 候选行：**不完全符合**表头，主要问题是缺少 `citekey` 与 `notes`。

**Suggested cleanup before promotion**
- 把未来 `paper_matrix` 候选行改成严格的 row schema。
- 补上 `citekey` 和 `notes`。
- 修正 `stereoptyed` 拼写。

## 候选表头一致性检查

### `tables/paper_matrix.csv`
实际表头：
`paper,citekey,year,category,field_axis,species,brain_area_or_scale,task_or_behavior,neural_measurement,neural_object,computation,causal_status,key_finding_short,modeling_opportunity,identifiers,uncertainty,notes`

检查结果：
- `khilkevich2024BrainwideDynamicsLinking`：候选区块缺少 `citekey`
- `michaels2016NeuralPopulationDynamics`：候选区块缺少 `citekey`
- `safaie2023PreservedNeuralDynamics`：候选区块不是严格 row schema，且缺少 `citekey` / `notes` 的正式写法

### `tables/figure_evidence_table.csv`
实际表头：
`paper,citekey,figure_or_table,result_section,page,claim,evidence_summary,variable_or_neural_object,analysis_method,causal_status,relevance_to_research_question,uncertainty,notes`

检查结果：
- 三篇 note 的候选 figure 行都**没有完全对齐**这个表头
- 共通问题是 `notes` 字段缺失
- `safaie2023PreservedNeuralDynamics` 还额外缺少 `citekey` 的正式写法

## 最终建议

建议顺序是：
1. 先做 **note 层面的轻量 cleanup**
   - 修拼写
   - 补齐候选行的 `citekey`
   - 给 `figure_evidence_table` 候选行补 `notes`
2. 然后创建一个 **figure_evidence PDF-check plan**
   - 先核对 Khilkevich 的 `Fig. 3 / 5 / 6`
   - 再核对 Michaels 的 `Fig. 2 / 5 / 6 / 7`
   - 最后核对 Safaie 的 `Extended Data Fig. 2 / 7 / 9`
3. 通过 PDF 核验后，再推进到 `paper_matrix` 和 `figure_evidence_table` 的正式追加

当前不建议直接进入正式 append。最稳的下一步是先把 PDF-check 计划写出来，再做表格落地。
