# Zotero / references.bib 更新计划 (Run001)

本计划旨在为第一批 `read_first` 的 3 篇文献准备 Zotero 导入与 [references.bib](references.bib) 的更新规范。此更新有助于确保后续 PDF 关联、文献笔记、证据矩阵和引用的元数据一致性。

本计划依据 [tables/candidate_papers.csv](tables/candidate_papers.csv) 和 [synthesis/candidate_to_confirmed_plan_run001.md](synthesis/candidate_to_confirmed_plan_run001.md) 中的筛选决策制定。

---

## 1. 文献更新列表

### 1. Brain-wide dynamics linking sensation to action during decision-making
1. **Title (英文原名)**: `Brain-wide dynamics linking sensation to action during decision-making`
2. **DOI**: `10.1038/s41586-024-07908-w`
3. **PMID**: `39261727`
4. **PMCID**: `PMC11499283`
5. **当前 Candidate 状态**: `candidate_metadata_verified`
6. **推荐 Zotero 导入方法**:
   - **首选**: 使用 DOI `10.1038/s41586-024-07908-w` 或 PMID `39261727` 通过 Zotero "Add Item(s) by Identifier" 功能自动导入。
   - **备选**: 若自动导入失败，访问 [Publisher Page (Nature)](https://doi.org/10.1038/s41586-024-07908-w) 并使用 Zotero Connector 浏览器插件进行捕获。
7. **导入后需校验的字段**:
   - **Title**: `Brain-wide dynamics linking sensation to action during decision-making`
   - **Authors**: Andrei Khilkevich; Michael Lohse; Ryan J. Low; Ivana Orsolic; Tadej Bozic; Paige Windmill; T. Mrsic-Flogel (检查并确保作者列表完整且顺序正确)
   - **Year**: `2024` (通常 Zotero 导入会显示为 2024 或具体日期 2024-09-11)
   - **Venue**: `Nature`
   - **DOI**: `10.1038/s41586-024-07908-w`
   - **PMID**: `39261727`
   - **PMCID**: `PMC11499283`
8. **预计 Better BibTeX Citekey 命名规则**:
   - 格式：`[auth:lower][year][title:select:1:3:camel]`
   - 预期 Citekey：`khilkevich2024BrainwideDynamicsLinking` *(注：由于 Better BibTeX 对连字符 `Brain-wide` 的处理机制可能有所不同，如将其分为两个词，也可能生成为 `khilkevich2024BrainWideDynamics` 或 `khilkevich2024BrainwideDynamics`。导入后需检查并以实际生成为准)*
9. **标签分配 (Tags)**:
   - `run001`
   - `read_first`
   - `population_dynamics`
   - `brain_wide`
   - `field_first_survey`
10. **更新完成后需记录的信息**:
    - **citekey**: (如 `khilkevich2024BrainwideDynamicsLinking`)
    - **Zotero key**: (Zotero 内部的 8 位字母数字 ID，如 `A1B2C3D4`)
    - **references.bib 是否包含该条目**: (Yes / No)
    - **PDF 是否已关联**: (No) *(根据安全策略，本阶段暂不下载或关联 PDF)*

---

### 2. Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning
1. **Title (英文原名)**: `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
2. **DOI**: `10.1371/journal.pcbi.1005175`
3. **PMID**: `27814352`
4. **PMCID**: `PMC5096671`
5. **当前 Candidate 状态**: `candidate_metadata_verified`
6. **推荐 Zotero 导入方法**:
   - **首选**: 使用 DOI `10.1371/journal.pcbi.1005175` 或 PMID `27814352` 通过 Zotero "Add Item(s) by Identifier" 功能自动导入。
   - **备选**: 若自动导入失败，访问 [Publisher Page (PLOS Computational Biology)](https://doi.org/10.1371/journal.pcbi.1005175) 并使用 Zotero Connector 插件捕获。
7. **导入后需校验的字段**:
   - **Title**: `Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning`
   - **Authors**: Jonathan A. Michaels; Benjamin Dann; Hansjorg Scherberger
   - **Year**: `2016` (具体为 2016-11-07)
   - **Venue**: `PLoS Computational Biology` (或缩写形式 `PLoS Comput. Biol.`)
   - **DOI**: `10.1371/journal.pcbi.1005175`
   - **PMID**: `27814352`
   - **PMCID**: `PMC5096671`
8. **预计 Better BibTeX Citekey 命名规则**:
   - 格式：`[auth:lower][year][title:select:1:3:camel]`
   - 预期 Citekey：`michaels2016NeuralPopulationDynamics` *(注：`during` 在 Better BibTeX 中通常被归为 skipword，因此跳过直接取后面的 `Neural`, `Population`, `Dynamics` 并 CamelCase 合并)*
9. **标签分配 (Tags)**:
   - `run001`
   - `read_first`
   - `population_dynamics`
   - `field_first_survey`
   - *(不分配 `brain_wide` 标签)*
10. **更新完成后需记录的信息**:
    - **citekey**: (如 `michaels2016NeuralPopulationDynamics`)
    - **Zotero key**: (Zotero 内部的 8 位字母数字 ID)
    - **references.bib 是否包含该条目**: (Yes / No)
    - **PDF 是否已关联**: (No) *(根据安全策略，本阶段暂不下载或关联 PDF)*

---

### 3. Preserved neural dynamics across animals performing similar behaviour
1. **Title (英文原名)**: `Preserved neural dynamics across animals performing similar behaviour`
2. **DOI**: `10.1038/s41586-023-06714-0`
3. **PMID**: `37938772`
4. **PMCID**: `PMC10665198`
5. **当前 Candidate 状态**: `candidate_metadata_verified`
6. **推荐 Zotero 导入方法**:
   - **首选**: 使用 DOI `10.1038/s41586-023-06714-0` 或 PMID `37938772` 通过 Zotero "Add Item(s) by Identifier" 功能自动导入。
   - **备选**: 访问 [Publisher Page (Nature)](https://doi.org/10.1038/s41586-023-06714-0) 并使用 Zotero Connector 插件捕获。
7. **导入后需校验的字段**:
   - **Title**: `Preserved neural dynamics across animals performing similar behaviour`
   - **Authors**: M. Safaie; J. C. Chang; J. Park; L. E. Miller; J. T. Dudman; M. G. Perich; J. A. Gallego
   - **Year**: `2023` (具体为 2023-11-08)
   - **Venue**: `Nature`
   - **DOI**: `10.1038/s41586-023-06714-0`
   - **PMID**: `37938772`
   - **PMCID**: `PMC10665198`
8. **预计 Better BibTeX Citekey 命名规则**:
   - 格式：`[auth:lower][year][title:select:1:3:camel]`
   - 预期 Citekey：`safaie2023PreservedNeuralDynamics` *(注：`across` 通常被 Better BibTeX 识别为 skipword，因此跳过直接取后面的 `Preserved`, `Neural`, `Dynamics` 并 CamelCase 合并)*
9. **标签分配 (Tags)**:
   - `run001`
   - `read_first`
   - `population_dynamics`
   - `field_first_survey`
   - *(不分配 `brain_wide` 标签)*
10. **更新完成后需记录的信息**:
    - **citekey**: (如 `safaie2023PreservedNeuralDynamics`)
    - **Zotero key**: (Zotero 内部的 8 位字母数字 ID)
    - **references.bib 是否包含该条目**: (Yes / No)
    - **PDF 是否已关联**: (No) *(根据安全策略，本阶段暂不下载或关联 PDF)*

---

## Manual checklist (手动操作指南)

为了将这些文献安全、规范地纳入 Zotero 及 `references.bib`，请遵循以下手动操作步骤：

1. **添加文献条目 (Add Item by DOI or PMID)**：
   - 打开 Zotero 客户端。
   - 点击顶部工具栏中的 **"Add Item(s) by Identifier" (魔棒图标)**。
   - 复制并粘贴相应文献的 **DOI** 或 **PMID** 进行快速检索并导入。如果自动获取有延迟，可使用备选的浏览器捕获方式导入。
2. **核验文献元数据 (Verify Imported Metadata)**：
   - 核对 Zotero 右侧属性面板，确认标题、第一作者及全部合作作者、年份、期刊（Venue）等核心字段是否完整且正确无误。
   - 特别核对 `DOI`、`PMID` (Extra 字段中通常包含 `PMID: 39261727` 等形式) 和 `PMCID` 是否成功关联。
3. **分配集合与标签 (Assign Collection / Tags)**：
   - 将这三篇文献拖拽至专门用于当前文献调研项目的 Zotero 分类集合中。
   - 手动在右侧面板的 **"Tags" (标签)** 中添加对应的标签：
     - 所有三篇均添加：`run001`、`read_first`、`field_first_survey`。
     - 研究轴标签分配：
       - `Brain-wide dynamics linking sensation to action during decision-making` 添加 `brain_wide` 和 `population_dynamics`。
       - 另外两篇添加 `population_dynamics`。
4. **同步或刷新 Better BibTeX `references.bib` (Export or Refresh)**：
   - 检查 Better BibTeX 插件是否为条目自动生成了符合规范的 Citekey。
   - 手动触发 Zotero 的 Better BibTeX 自动导出或更新，确保新添加的 3 篇文献被写入到项目根目录下的 [references.bib](references.bib) 中。
5. **PDF 附件控制 (Do Not Attach PDFs Yet)**：
   - **请勿在此阶段关联或下载 PDF 附件**。除非后续获得明确的批量下载与分析指令，否则先保持文献条目的无 PDF 状态。
   - **安全警告**：使用 Zotero Connector 浏览器插件时，可能会自动下载并附加可公开获取（Open Access）的 PDF。在此步骤中，**推荐优先使用 "Add Item by Identifier" (魔棒图标) 进行导入**。
   - **处理方法**：如果使用了 Zotero Connector 导致 PDF 被自动附加，请手动在 Zotero 中删除该 PDF 附件，除非 PDF 下载已获得明确的批准。

---

## What not to do yet (当前暂不执行的操作)

为了保持工作流的安全和整洁，请严格遵守以下约束：
- **不要下载 PDF** (Do not download PDFs)：本阶段仅更新文献元数据，不执行 PDF 的批量下载。
- **不要创建文献笔记** (Do not create notes)：暂不在 `notes/` 目录下为这三篇文献新建 Markdown 格式的论文笔记。
- **不要更新 `confirmed_papers.csv`**：该文件只存放已正式确认并进入阅读阶段的文献，当前不作更新。
- **不要更新 `paper_matrix.csv`**。
- **不要更新 `figure_evidence_table.csv`**。

---

## 计划状态说明

* **文档性质**: 纯规划与手动操作指南（非执行脚本）。
* **GitHub 状态**: 本文件已作安全核验，可直接提交至 GitHub 仓库。
