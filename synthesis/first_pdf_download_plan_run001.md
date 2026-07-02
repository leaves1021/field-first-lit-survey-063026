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
  1. **首选 (PMC 全文源)**: 利用 PMCID `PMC11499283` 从 NCBI PubMed Central 开放获取源直接获取（可通过 Europe PMC API 自动获取，或直接访问 PMC 页面下载）。
  2. **备选 (Publisher OA 源)**: 访问 Nature 出版商页面 [Nature DOI](https://doi.org/10.1038/s41586-024-07908-w) 并下载开放获取 PDF。
  3. **终极备选 (手动下载)**: 若自动脚本受限，由用户手动下载 PDF 并存入指定目录。
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
  1. **首选 (PMC 全文源)**: 利用 PMCID `PMC5096671` 从 PMC 开放获取源获取。
  2. **备选 (Publisher OA 源)**: 访问 PLOS Computational Biology 出版商页面 [PLOS DOI](https://doi.org/10.1371/journal.pcbi.1005175) 并下载。
  3. **终极备选 (手动下载)**: 手动下载 PDF 并存入指定目录。
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
  1. **首选 (PMC 全文源)**: 利用 PMCID `PMC10665198` 从 PMC 开放获取源获取。
  2. **备选 (Publisher OA 源)**: 访问 Nature 出版商页面 [Nature DOI](https://doi.org/10.1038/s41586-023-06714-0) 下载。
  3. **终极备选 (手动下载)**: 手动下载 PDF 并存入指定目录。
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
* **自动下载风险**:
  - 虽然 3 篇文献均为带有 PMCID 的 Open Access 文献，但通过 API 自动下载可能会遭遇速率限制（Rate Limit）、IP 封禁或非预期的 HTML 页面混淆。
  - 由于 Zotero 之前已自动附加了本地 PDF，可以直接在 Zotero 本地存储路径中找到这些文件，重命名后直接移动至 `papers/raw_pdf/` 目录，这是**最安全、最快捷且不消耗外部网络流量**的方法。
* **手动下载建议**:
  - 如果选择重新下载，建议直接访问 PMC 页面手动点击下载，然后按规范重命名。
* **命名规范**:
  - PDF 原始文件和提取出的文本文件必须使用一致的、基于 Better BibTeX Citekey 的命名：
    - PDF 文件: `papers/raw_pdf/<citekey>.pdf`
    - Markdown 文本: `papers/extracted_text/<citekey>.md`

---

## 3. 文本提取命令行计划

提取 PDF 文本时将运行本地 Python 脚本 `scripts/extract_pdf_text.py`（该脚本使用 PyMuPDF 进行高质量的页面级文本解析与 Markdown 生成）。

### 批量提取命令 (Batch Mode)
当 3 个 PDF 文件下载并命名完毕并存放于 `papers/raw_pdf/` 目录下后，可一键批量处理：
```bash
python scripts/extract_pdf_text.py --input-dir papers/raw_pdf --output-dir papers/extracted_text
```

### 逐个文件安全处理命令 (Per-file Mode)
为确保处理的可控性和日志精细度，也可选择单文件逐个提取：
```bash
# 处理第一篇
python scripts/extract_pdf_text.py --input papers/raw_pdf/khilkevich2024BrainwideDynamicsLinking.pdf --output-dir papers/extracted_text

# 处理第二篇
python scripts/extract_pdf_text.py --input papers/raw_pdf/michaels2016NeuralPopulationDynamics.pdf --output-dir papers/extracted_text

# 处理第三篇
python scripts/extract_pdf_text.py --input papers/raw_pdf/safaie2023PreservedNeuralDynamics.pdf --output-dir papers/extracted_text
```

---

## 4. Git 追踪与隐私约束

根据项目规范以及 `.gitignore` 中的配置，数据隐私与版权约束如下：
* **PDF 版权规避**：`papers/raw_pdf/*` 以及辅助文件目录已在 `.gitignore` 中被声明忽略，严禁将受版权保护的学术 PDF 原始文件推送或提交至公共 GitHub 仓库。
* **提取文本规避**：提取后的纯文本包含论文全文内容，`papers/extracted_text/*` 亦已在 `.gitignore` 中被忽略，不可提交。
* **可提交的成果**：仅当数据表 `tables/confirmed_papers.csv` 更新或在此生成摘要/说明 manifest 时，才可以将元数据信息和规划报告提交至 Git 历史。

---

## 5. What not to do yet (当前暂不执行的操作)

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
