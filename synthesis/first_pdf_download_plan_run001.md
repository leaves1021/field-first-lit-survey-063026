# 首批 PDF 下载与文本提取计划 (Run001)

本计划旨在为已确认的 3 篇首批文献制定安全的 PDF 下载与文本提取工作流。目前本文件仅作为规划文档归档，**在获得明确的批准指令前暂不下载 PDF、不提取文本且不改写任何数据表**。

本计划依据 `tables/confirmed_papers.csv`、`synthesis/confirmed_append_plan_run001_first_batch.md` 以及 `synthesis/zotero_references_pdf_attachment_check_run001.md` 中的状态进行制定。

---

## 1. 文献下载与提取方案

### 1) Brain-wide dynamics linking sensation to action during decision-making
* **Citekey**: `khilkevich2024BrainwideDynamicsLinking`
* **DOI**: `10.1038/s41586-024-07908-w`
* **PMID / PMCID**: `39261727` / `PMC11499283`
* **PDF 下载源优先级**:
  1. **首选 (PMC 全文源)**: 拥有 PMCID 意味着该文献在 PMC 中有记录。在下载前，必须使用 PMC 页面或 PMC OA Web Service 确认该 PMCID 是否有可供下载的 PDF 全文。确认后，优先从 PMC 官方源获取。
  2. **备选 (Publisher OA 源)**: 优先选择 PMC 或出版商（Nature）的官方开放获取源，避免使用第三方的任意网页副本。访问 [Nature DOI](https://doi.org/10.1038/s41586-024-07908-w) 进行官方 OA PDF 下载。
  3. **终极备选 (手动下载)**: 若自动脚本获取失败或受限，通过手动访问上述官方源下载 PDF 并存入指定目录。
* **目标 PDF 路径**: `papers/raw_pdf/khilkevich2024BrainwideDynamicsLinking.pdf`
* **目标提取文本路径**: `papers/extracted_text/khilkevich2024BrainwideDynamicsLinking.md`
* **后续 confirmed_papers.csv 更新预案**:
  - `pdf_path`: `papers/raw_pdf/khilkevich2024BrainwideDynamicsLinking.pdf`
  - `extracted_text_path`: `papers/extracted_text/khilkevich2024BrainwideDynamicsLinking.md`
  - `status`: `ready_for_reading`
  - `notes`: `Zotero and references.bib present; citekey verified; PDF downloaded and text extracted successfully; ready for full-text reading and figure evidence extraction.`

---

### 2) Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning
* **Citekey**: `michaels2016NeuralPopulationDynamics`
* **DOI**: `10.1371/journal.pcbi.1005175`
* **PMID / PMCID**: `27814352` / `PMC5096671`
* **PDF 下载源优先级**:
  1. **首选 (PMC 全文源)**: 拥有 PMCID 意味着该文献在 PMC 中有记录。下载前，必须使用 PMC 页面或 PMC OA Web Service 确认该 PMCID 是否有可供下载的 PDF 全文。确认后，优先从 PMC 官方源获取。
  2. **备选 (Publisher OA 源)**: 优先选择 PMC 或出版商的官方开放获取源，避免使用第三方的任意网页副本。访问 PLOS Computational Biology 出版商页面 [PLOS DOI](https://doi.org/10.1371/journal.pcbi.1005175) 并下载。
  3. **终极备选 (手动下载)**: 手动访问上述官方源下载 PDF 并存入指定目录。
* **目标 PDF 路径**: `papers/raw_pdf/michaels2016NeuralPopulationDynamics.pdf`
* **目标提取文本路径**: `papers/extracted_text/michaels2016NeuralPopulationDynamics.md`
* **后续 confirmed_papers.csv 更新预案**:
  - `pdf_path`: `papers/raw_pdf/michaels2016NeuralPopulationDynamics.pdf`
  - `extracted_text_path`: `papers/extracted_text/michaels2016NeuralPopulationDynamics.md`
  - `status`: `ready_for_reading`
  - `notes`: `Zotero and references.bib present; citekey verified; PDF downloaded and text extracted successfully; ready for full-text reading and figure evidence extraction.`

---

### 3) Preserved neural dynamics across animals performing similar behaviour
* **Citekey**: `safaie2023PreservedNeuralDynamics`
* **DOI**: `10.1038/s41586-023-06714-0`
* **PMID / PMCID**: `37938772` / `PMC10665198`
* **PDF 下载源优先级**:
  1. **首选 (PMC 全文源)**: 拥有 PMCID 意味着该文献在 PMC 中有记录。下载前，必须使用 PMC 页面或 PMC OA Web Service 确认该 PMCID 是否有可供下载的 PDF 全文。确认后，优先从 PMC 官方源获取。
  2. **备选 (Publisher OA 源)**: 优先选择 PMC 或出版商的官方开放获取源，避免使用第三方的任意网页副本。访问 Nature 出版商页面 [Nature DOI](https://doi.org/10.1038/s41586-023-06714-0) 下载。
  3. **终极备选 (手动下载)**: 手动访问上述官方源下载 PDF 并存入指定目录。
* **目标 PDF 路径**: `papers/raw_pdf/safaie2023PreservedNeuralDynamics.pdf`
* **目标提取文本路径**: `papers/extracted_text/safaie2023PreservedNeuralDynamics.md`
* **后续 confirmed_papers.csv 更新预案**:
  - `pdf_path`: `papers/raw_pdf/safaie2023PreservedNeuralDynamics.pdf`
  - `extracted_text_path`: `papers/extracted_text/safaie2023PreservedNeuralDynamics.md`
  - `status`: `ready_for_reading`
  - `notes`: `Zotero and references.bib present; citekey verified; PDF downloaded and text extracted successfully; ready for full-text reading and figure evidence extraction.`

---

## 2. 下载方式与命名规范

### 自动下载与手动下载的安全性权衡
* **自动下载风险与约束**:
  - 虽然 3 篇文献均为带有 PMCID 的 Open Access 文献，但通过 API 自动下载可能会遭遇速率限制（Rate Limit）、IP 封禁或非预期的 HTML 页面混淆。
  - **重要约束**：Zotero 中的 PDF 附件已被故意删除，且 Zotero 垃圾箱已清空。**在此步骤中绝对不要依赖 Zotero 的本地存储**。
  - **PDF 获取策略**：PDF 获取应当通过可控的方式直接从 PMC 或出版商官方页面下载，或者采用手动下载后进行基于 Citekey 命名的规则放入 `papers/raw_pdf/` 目录。
* **手动下载建议**:
  - 如果选择手动下载，直接访问确认可用的 PMC 页面下载 PDF，然后按规范重命名保存。
* **命名规范**:
  - PDF 原始文件和提取出的文本文件必须使用一致的、基于 Better BibTeX Citekey 的命名：
    - PDF 文件: `papers/raw_pdf/<citekey>.pdf`
    - Markdown 文本: `papers/extracted_text/<citekey>.md`

---

## 3. 文本提取命令行计划

提取 PDF 文本时将运行本地 Python 脚本 `scripts/extract_pdf_text.py`（该脚本使用 PyMuPDF 进行高质量的页面级文本解析与 Markdown 生成）。

### 逐个文件安全处理命令 (Per-file Mode) - **推荐默认策略**
为确保处理的可控性，首批 Run001 推荐默认使用单文件逐个提取的策略。
* **原因**：`papers/raw_pdf/` 目录中可能包含之前的测试 PDF（例如 Ye 2026 或 Vyas 2020），如果运行 `--input-dir` 批量提取命令，脚本会处理目录下所有的 `*.pdf` 文件，可能导致对既有已确认文献提取结果的不必要覆写或冗余计算。

命令行如下：
```bash
# 处理第一篇
python scripts/extract_pdf_text.py --input papers/raw_pdf/khilkevich2024BrainwideDynamicsLinking.pdf --output-dir papers/extracted_text

# 处理第二篇
python scripts/extract_pdf_text.py --input papers/raw_pdf/michaels2016NeuralPopulationDynamics.pdf --output-dir papers/extracted_text

# 处理第三篇
python scripts/extract_pdf_text.py --input papers/raw_pdf/safaie2023PreservedNeuralDynamics.pdf --output-dir papers/extracted_text
```

### 批量提取命令 (Batch Mode) - **仅作为备选**
若能确保 `papers/raw_pdf/` 目录下无任何多余测试 PDF 文件，亦可选择批量处理：
```bash
python scripts/extract_pdf_text.py --input-dir papers/raw_pdf --output-dir papers/extracted_text
```

---

## 4. 下载与提取后验证清单 (Post-Download & Extraction Verification)

在完成 PDF 下载与文本提取后，针对每篇文献必须显式核验以下内容：
1. **文件存在性**：确认 PDF 文件已成功保存在 `papers/raw_pdf/` 目录下。
2. **文件名准确性**：确认 PDF 文件名与 Better BibTeX Citekey 完全匹配（包含大小写，如 `khilkevich2024BrainwideDynamicsLinking.pdf`）。
3. **文件大小有效性**：确认 PDF 文件大小不为 0 (非空文件)，且文件扩展名严格为 `.pdf`。
4. **Zotero 本地路径检查**：确认条目导出的 `references.bib` 中不残留任何 Zotero 的本地 PDF 存储路径。
5. **Markdown 文件生成**：提取完成后，确认在 `papers/extracted_text/` 下生成了对应的 `.md` 文本文件。
6. **YAML 元数据包含**：确认生成的 Markdown 文本开头包含完整的 YAML 格式元数据，且其中必须包含 `original_file` 字段。
7. **提取无错汇总**：确认控制台输出或日志文件中的统计汇总没有报错（Errors 计数为 0）。

---

## 5. 结果清单文件规划 (Results Manifest Plan)

实际完成下载与提取后，应创建以下结果归档清单文件：
`synthesis/pdf_download_extraction_results_run001.md`

该未来结果文件必须详细记录以下项目：
- **citekey**：文献的 Better BibTeX 引用键。
- **PDF path**：本地 PDF 保存的相对路径。
- **extracted text path**：提取后 Markdown 的相对路径。
- **download source used**：实际使用的下载源（如 `PMC API`, `Nature Publisher OA`, `Manual Download` 等）。
- **extraction status**：提取状态（如 `extracted`, `skipped`, `error`）。
- **number of pages**：提取出的 PDF 页数。
- **low-text warning**：是否触发了 PyMuPDF 脚本的低文本量警告（即是否可能为扫描版图像 PDF）。
- **proposed confirmed_papers.csv update preview**：拟对 `tables/confirmed_papers.csv` 数据行进行状态更新的预览。

---

## 6. Git 追踪与隐私约束

根据项目规范以及 `.gitignore` 中的配置，数据隐私与版权约束如下：
* **PDF 版权规避**：`papers/raw_pdf/*` 以及辅助文件目录已在 `.gitignore` 中被声明忽略，严禁将受版权保护的学术 PDF 原始文件推送或提交至公共 GitHub 仓库。
* **提取文本规避**：提取后的纯文本包含论文全文内容，`papers/extracted_text/*` 亦已在 `.gitignore` 中被忽略，不可提交。
* **可提交的成果**：仅当数据表 `tables/confirmed_papers.csv` 更新或在此生成摘要/说明 manifest 时，才可以将元数据信息和规划报告提交至 Git 历史。

---

## 7. What not to do yet (当前暂不执行的操作)

为确保当前阶段流程合规与安全，以下操作在本次规划步骤中**均不执行**：
- **不要下载 PDF** (Do not download PDFs yet)。
- **不要提取文本** (Do not extract text yet)。
- **不要创建文献笔记** (Do not create paper notes)。
- **不要更新 `tables/paper_matrix.csv`**。
- **不要更新 `tables/figure_evidence_table.csv`**。
- **不要在此阶段直接修改 `tables/confirmed_papers.csv`**。

---

## 计划状态说明

* **文档性质**: 下载与提取工作流规划书。
* **GitHub 状态**: 本文件不含本地绝对路径及敏感数据，可直接提交至 GitHub 仓库。
