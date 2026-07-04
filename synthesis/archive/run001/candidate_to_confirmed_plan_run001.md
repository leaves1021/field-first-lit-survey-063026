# Candidate To Confirmed Plan Run001

## 1. Current candidate status summary

当前 `tables/candidate_papers.csv` 中共有 8 条 Search Run 001 candidates。

状态计数：

- `candidate_metadata_verified`: 5
- `candidate_needs_manual_review`: 3
- `candidate_title_level`: 0

按当前 status 列出 8 条 candidates：

### `candidate_metadata_verified`

1. `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
2. `Preserved neural dynamics across animals performing similar behaviour`
3. `Brain-wide dynamics linking sensation to action during decision-making`
4. `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input`
5. `Inferring stochastic low-rank recurrent neural networks from neural data`

### `candidate_needs_manual_review`

1. `Large-scale high-density brain-wide neural recording in nonhuman primates`
2. `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile`
3. `Human brain state dynamics are highly reproducible and associated with neural and behavioral features`

### `candidate_title_level`

- none

## 2. Candidate-level triage

| Title | Current status | Triage | Reason |
|---|---|---|---|
| `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | `candidate_metadata_verified` | `read_first` | population dynamics / neural manifolds 轴的经典 experimental landmark，metadata 已核验，较高概率能直接提供 figure-level evidence，并且适合作为 advisor-facing field-first survey 的代表性 anchor。 |
| `Preserved neural dynamics across animals performing similar behaviour` | `candidate_metadata_verified` | `read_first` | 直接命中跨动物 neural dynamics 与 generalization 问题，适合作为 population dynamics 轴的较新代表作，且 metadata 已完成 PMID / DOI / PMCID / S2 对齐。 |
| `Brain-wide dynamics linking sensation to action during decision-making` | `candidate_metadata_verified` | `read_first` | brain-wide / distributed computation 轴的高价值核心候选，title 已直接指向 sensation-to-action 与 decision-making 的跨脑区动态链路。 |
| `Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input` | `candidate_metadata_verified` | `read_later` | 有 causal perturbation angle，metadata 清楚，但更偏 resting-state fMRI；对 field-first survey 有价值，不过第一批未必比前三篇更能快速建立主轴证据框架。 |
| `Inferring stochastic low-rank recurrent neural networks from neural data` | `candidate_metadata_verified` | `read_later` | 方法轴价值明确，适合作为 model-based inference / theoretical method 补充，但第一批更应优先建立 experimental anchor，再进入方法补强。 |
| `Large-scale high-density brain-wide neural recording in nonhuman primates` | `candidate_needs_manual_review` | `manual_review_before_reading` | 目前更像 method/platform paper；虽然 brain-wide recording scale 很重要，但是否提供 computation-level results 仍不清楚，不适合作为第一批 PDF。 |
| `Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile` | `candidate_needs_manual_review` | `manual_review_before_reading` | field-axis relevance 很强，且可能有投射通路与 distributed activity 的 figure-level evidence；但当前仍有 S2 unresolved item，适合在 reading 前先做一次简短 manual check。 |
| `Human brain state dynamics are highly reproducible and associated with neural and behavioral features` | `candidate_needs_manual_review` | `hold` | metadata 基本清楚，但 scientific fit 仍不稳定，更偏 human brain-state / resting-state 解释框架；在当前 run001 中不应抢占第一轮 full-text 资源。 |

## 3. Triage criteria

本轮 triage 主要依据以下标准：

- `field-axis relevance`：优先直接对齐 `brain-wide / distributed computation`、`population dynamics / neural manifolds`、`multi-area communication`、`causal perturbation` 的论文。
- `paper type`：优先 experimental landmark；method/platform paper 与 theoretical method paper 重要，但通常排在建立实验锚点之后。
- `metadata status`：优先 `candidate_metadata_verified`；`candidate_needs_manual_review` 若 scientific fit 很强，可进入 manual review queue，但不优先进入首批 PDF。
- `scientific fit uncertainty`：如果 metadata 虽清楚，但对 survey 主轴是否 central 仍不确定，应先 defer 或 hold。
- `figure-level evidence potential`：优先明显可能提供任务、动态、跨区域协调、perturbation 结果图的候选。
- `advisor-facing field-first usefulness`：第一批阅读应尽快覆盖 broad field axes，而不是太早陷入技术平台细节或方法-only 文献。

## 4. Recommended first PDF batch

第一批 PDF / full-text reading 建议最多选 3 篇：

1. `Brain-wide dynamics linking sensation to action during decision-making`
   选择理由：
   这是目前最直接覆盖 `brain-wide / distributed computation` 主轴的核心 experimental paper，并且具有从 sensation 到 action 的完整链路表述，适合作为 field-first survey 的头部案例。
   首先应提取的证据：
   - 任务与行为范式
   - 记录尺度与跨脑区范围
   - 主要 dynamics / latent structure / coordination finding
   - 与 decision-making 关联最直接的结果图和结果段落

2. `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
   选择理由：
   这是 population dynamics 轴的代表性 landmark，能帮助 survey 建立“representational tuning vs dynamical systems framing”的核心对照。
   首先应提取的证据：
   - reaching task 与记录对象
   - 作者如何比较 representational tuning 和 dynamical system explanation
   - 支撑该比较的关键 figures / analyses
   - 对 population-level computation framing 的直接启发

3. `Preserved neural dynamics across animals performing similar behaviour`
   选择理由：
   这篇可以把 population dynamics 轴从单一任务/单一数据集扩展到跨动物保守性问题，对 advisor-facing survey 很有说服力。
   首先应提取的证据：
   - cross-animal comparison framework
   - “preserved dynamics” 的 operational definition
   - 支撑 preservation claim 的主图和统计比较
   - 其对 general motifs / shared computation 的意义

## 5. Papers not selected for first batch

`Brain-wide resting-state fMRI network dynamics elicited by activation of single thalamic input`：
有明确的 causal perturbation angle，也值得后续优先阅读，但第一批先建立更强的 behavior-linked experimental anchor 会更高效。

`Inferring stochastic low-rank recurrent neural networks from neural data`：
方法轴重要，尤其对后续 model-based inference 很有帮助；但在没有先完成第一轮 experimental anchor 阅读前，暂不优先。

`Large-scale high-density brain-wide neural recording in nonhuman primates`：
当前更像 platform / technical report，虽然可能成为 measurement-scale 背景文献，但暂不作为 first-batch confirmation driver。

`Long-range projections coordinate distributed brain-wide neural activity with a specific spatiotemporal profile`：
主题上很强，但当前仍留有 manual review item；建议先做一次短 manual check，再决定是否升到第二批 PDF。

`Human brain state dynamics are highly reproducible and associated with neural and behavioral features`：
对 human brain state literature 可能有价值，但当前 scientific fit 与核心 field-axis 的贴合度不如前三篇清楚，因此先 hold。

## 6. Zotero / references.bib next step

在下载或阅读第一批 PDF 之前，建议先把以下 3 篇加入 Zotero，并在后续导出 / 更新 `references.bib`：

1. `Brain-wide dynamics linking sensation to action during decision-making`
2. `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
3. `Preserved neural dynamics across animals performing similar behaviour`

这样做的理由：

- 这 3 篇最可能成为后续 confirmed pool 的第一批核心文献。
- 先进入 Zotero / `references.bib`，可以让后续 PDF、notes、matrix、figure evidence 的引用管理保持稳定。
- 这一步仍然只是 bibliographic organization，不等于把它们标记为 confirmed。

## 7. What not to do yet

- 不要把任何记录移动到 `tables/confirmed_papers.csv`。
- 不要生成 paper notes。
- 不要更新 `tables/paper_matrix.csv`。
- 不要更新 `tables/figure_evidence_table.csv`。
- 不要从 metadata 直接推断 figure-level claims。
- 不要把 `candidate_metadata_verified` 自动等同于 confirmed paper。
