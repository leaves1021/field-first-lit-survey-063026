# PDF Download Extraction Results Run001

## Scope

本文件记录 Run001 first batch 的 PDF acquisition 与 text extraction 结果，仅覆盖以下 3 篇：

1. `khilkevich2024BrainwideDynamicsLinking`
2. `michaels2016NeuralPopulationDynamics`
3. `safaie2023PreservedNeuralDynamics`

本步骤未更新 `tables/paper_matrix.csv`、`tables/figure_evidence_table.csv`，未创建 paper notes，未修改 scripts，未使用 Zotero local storage paths，未使用第三方 PDF 镜像。

## Source decision

- PMC OA / article path 已检查，但当前自动访问返回的是 challenge HTML，而不是真实 PDF 字节流。
- 按 `synthesis/first_pdf_download_plan_run001.md` 的 fallback 规则，本次实际使用 official publisher OA page 下载 PDF。
- 3 个 publisher links 均返回真实 PDF 文件头 `%PDF`，因此下载继续执行。

## Results

| citekey | title | DOI | PMCID | PDF source used | PDF path | extracted text path | PDF file size | number of pages | extraction status | low-text warning | proposed `tables/confirmed_papers.csv` update preview |
|---|---|---|---|---|---|---|---:|---:|---|---|---|
| `khilkevich2024BrainwideDynamicsLinking` | `Brain-wide dynamics linking sensation to action during decision-making` | `10.1038/s41586-024-07908-w` | `PMC11499283` | `Nature publisher OA PDF` | `papers/raw_pdf/khilkevich2024BrainwideDynamicsLinking.pdf` | `papers/extracted_text/khilkevich2024BrainwideDynamicsLinking.md` | 59519723 | 44 | `extracted` | `no` | `pdf_path -> papers/raw_pdf/khilkevich2024BrainwideDynamicsLinking.pdf; extracted_text_path -> papers/extracted_text/khilkevich2024BrainwideDynamicsLinking.md; status -> ready_for_reading; notes -> PDF downloaded and text extracted successfully.` |
| `michaels2016NeuralPopulationDynamics` | `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning` | `10.1371/journal.pcbi.1005175` | `PMC5096671` | `PLOS publisher OA PDF` | `papers/raw_pdf/michaels2016NeuralPopulationDynamics.pdf` | `papers/extracted_text/michaels2016NeuralPopulationDynamics.md` | 3400052 | 22 | `extracted` | `no` | `pdf_path -> papers/raw_pdf/michaels2016NeuralPopulationDynamics.pdf; extracted_text_path -> papers/extracted_text/michaels2016NeuralPopulationDynamics.md; status -> ready_for_reading; notes -> PDF downloaded and text extracted successfully.` |
| `safaie2023PreservedNeuralDynamics` | `Preserved neural dynamics across animals performing similar behaviour` | `10.1038/s41586-023-06714-0` | `PMC10665198` | `Nature publisher OA PDF` | `papers/raw_pdf/safaie2023PreservedNeuralDynamics.pdf` | `papers/extracted_text/safaie2023PreservedNeuralDynamics.md` | 16170884 | 25 | `extracted` | `no` | `pdf_path -> papers/raw_pdf/safaie2023PreservedNeuralDynamics.pdf; extracted_text_path -> papers/extracted_text/safaie2023PreservedNeuralDynamics.md; status -> ready_for_reading; notes -> PDF downloaded and text extracted successfully.` |

## Post-run verification

对 3 篇文献均已核验：

- PDF 文件存在。
- PDF 文件大小非 0。
- PDF 文件名与 citekey 完全匹配。
- 提取后的 Markdown 文件存在。
- Markdown 文件以 YAML metadata 开头。
- YAML 中包含 `original_file`。
- YAML 中可读取 `num_pages`。
- 每次 extraction summary 均报告 `Extracted: 1`、`Errors: 0` 隐含成立，且脚本日志只有 `Successfully extracted` 记录。
- low-text warning 未触发，3 篇均记录为 `no`。
- 在可提交/可跟踪文件范围内，未检出 Zotero local storage path。

## Confirmed table update status

由于 3 个 PDF 与 3 个 extracted Markdown files 均已成功验证，本次已将 `tables/confirmed_papers.csv` 中对应 3 行更新为：

- `pdf_path`: 指向计划中的 citekey-based PDF 路径
- `extracted_text_path`: 指向计划中的 citekey-based Markdown 路径
- `status`: `ready_for_reading`
- `notes`: 更新为下载与提取成功说明

## What not to do yet

- 不要把这些 papers 的 figure-level claims 从 metadata 或提取文本头部直接写入结构化 evidence tables。
- 不要现在更新 `tables/paper_matrix.csv`。
- 不要现在更新 `tables/figure_evidence_table.csv`。
- 不要现在创建 paper notes。
