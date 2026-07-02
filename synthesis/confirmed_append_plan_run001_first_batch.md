# Confirmed Papers 追加计划 (Run001 First Batch)

本文件提出了将第一批 3 篇 `read_first` 文献安全追加至 [tables/confirmed_papers.csv](tables/confirmed_papers.csv) 的执行计划。目前仅作为计划方案归档，**在获得明确的批准指令前暂不改写任何 CSV 文件**。

本计划依据 [tables/candidate_papers.csv](tables/candidate_papers.csv)、[synthesis/candidate_to_confirmed_plan_run001.md](candidate_to_confirmed_plan_run001.md)、[synthesis/zotero_references_update_results_run001.md](zotero_references_update_results_run001.md) 以及最近完成的 [synthesis/zotero_references_pdf_attachment_check_run001.md](zotero_references_pdf_attachment_check_run001.md) 制定。

---

## 1. confirmed_papers.csv 标题与字段顺序

经读取 [tables/confirmed_papers.csv](tables/confirmed_papers.csv)，其精确的表头字段顺序如下：

```csv
citekey,title,authors,year,venue,doi,pmid,pmcid,arxiv_id,semantic_scholar_id,zotero_key,zotero_collection,pdf_path,extracted_text_path,status,confirmed_by,confirmed_at,notes
```

---

## 2. 拟追加的 3 篇文献数据行 (CSV 预览)

关于 `citekey` 和 `zotero_key` 的字段映射设计说明：
* **`citekey` 列**：使用 Zotero 经 Better BibTeX 验证的 Citekey (例如 `khilkevich2024BrainwideDynamicsLinking`)，保证本地引用系统与 `references.bib` 的严格一致性。
* **`zotero_key` 列**：使用 Zotero 内部的 8 位字母数字唯一标识码 (例如 `86S8CT7K`)，方便将来与 Zotero 数据库进行条目级精确关联。

以下为拟追加的三行数据预览（以 CSV 格式呈现）：

```csv
khilkevich2024BrainwideDynamicsLinking,"Brain-wide dynamics linking sensation to action during decision-making","Andrei Khilkevich; Michael Lohse; Ryan J. Low; Ivana Orsolic; Tadej Bozic; Paige Windmill; T. Mrsic-Flogel",2024,Nature,10.1038/s41586-024-07908-w,39261727,PMC11499283,unclear,edb148e6ccc32491a80ff81bc6918258bd6a4d7d,86S8CT7K,field_first_survey/run001/read_first,not_downloaded_yet,not_extracted_yet,ready_for_pdf_download,metadata_verification_and_zotero_references_run001,2026-07-02,"Zotero and references.bib are present; Better BibTeX citekey verified; PDF attachment was removed from BibTeX; full-text reading not started."
michaels2016NeuralPopulationDynamics,"Neural Population Dynamics during Reaching Are Better Explained by a Dynamical System than Representational Tuning","Jonathan A. Michaels; Benjamin Dann; Hansjorg Scherberger",2016,PLoS Comput. Biol.,10.1371/journal.pcbi.1005175,27814352,PMC5096671,unclear,af1a65fa44773c427235e1f88bf714d64418883f,WMPLSSU9,field_first_survey/run001/read_first,not_downloaded_yet,not_extracted_yet,ready_for_pdf_download,metadata_verification_and_zotero_references_run001,2026-07-02,"Zotero and references.bib are present; Better BibTeX citekey verified; PDF attachment was removed from BibTeX; full-text reading not started."
safaie2023PreservedNeuralDynamics,"Preserved neural dynamics across animals performing similar behaviour","M. Safaie; J. C. Chang; J. Park; L. E. Miller; J. T. Dudman; M. G. Perich; J. A. Gallego",2023,Nature,10.1038/s41586-023-06714-0,37938772,PMC10665198,unclear,6c2952e1d99761ae5bc40558905b37875e87a8ab,BCDHKRTP,field_first_survey/run001/read_first,not_downloaded_yet,not_extracted_yet,ready_for_pdf_download,metadata_verification_and_zotero_references_run001,2026-07-02,"Zotero and references.bib are present; Better BibTeX citekey verified; PDF attachment was removed from BibTeX; full-text reading not started."
```

### 状态值选择及合理性证明
我们为上述 3 篇文献的 `status` 字段统一指定了 **`ready_for_pdf_download`** 状态，理由如下：
* **元数据完全对齐**：这 3 篇文献已完成多渠道元数据对齐与校验，处于 `candidate_metadata_verified` 状态。
* **Zotero 条目及 Citekey 准备就绪**：文献在 Zotero 中的条目已成功导入，对应的 Better BibTeX citekey 和 Zotero Key 已提取并核对。
* **附件安全性已被证明**：通过 [synthesis/zotero_references_pdf_attachment_check_run001.md](zotero_references_pdf_attachment_check_run001.md) 确认，导出的 `references.bib` 中已不含任何本地 PDF 的 `file` 字段。
* **代表下一步最明确的行动**：将状态设置为 `ready_for_pdf_download` 可以明确指示流程当前的断点，即元数据整合完毕，允许并等待下一阶段的安全 PDF 下载和文本提取，比宽泛的 `confirmed_metadata_only` 更具有操作导向性。

---

## 3. 写入前的预检清单 (Preflight Checks)

在正式执行 CSV 追加修改前，必须手动或通过脚本核验以下条件是否全部满足：

1. **表头一致性**：确认修改后的 [tables/confirmed_papers.csv](tables/confirmed_papers.csv) 的首行表头字段顺序与原文件完全一致，没有列数增减或列名修改。
2. **Citekey 唯一性**：确认拟添加的 3 个 citekey（`khilkevich2024BrainwideDynamicsLinking` 等）未在 [tables/confirmed_papers.csv](tables/confirmed_papers.csv) 既有条目中重复出现。
3. **DOI 唯一性**：确认拟添加 of 3 个 DOI 未与已确认文献中的任何 DOI 冲突。
4. **Candidate 状态校验**：确认这 3 篇文献在 [tables/candidate_papers.csv](tables/candidate_papers.csv) 中对应的 status 均为 `candidate_metadata_verified`。
5. **BibTeX 引用键匹配**：确认本地 `references.bib` 中存在这 3 个 citekey。
6. **附件清理校验**：确认 `references.bib` 的这 3 个条目下确实不含有任何包含 PDF 本地路径的 `file` 字段。

---

## 4. What not to do yet (当前暂不执行的操作)

为确保流程推进的安全性，请严格遵守以下约束：
- **不要直接修改 CSV** (Do not write CSV yet)：在没有获得后续明确的“执行追加写入”指令前，本计划仅为方案，不对 `tables/confirmed_papers.csv` 进行物理写入。
- **不要下载任何 PDF**。
- **不要创建文献笔记**。
- **不要更新 `tables/paper_matrix.csv`**。
- **不要更新 `tables/figure_evidence_table.csv`**。

---

## 计划状态说明

* **文档性质**: 纯追加规划设计（非执行脚本）。
* **GitHub 状态**: 本文件不含本地绝对路径及完整 BibTeX 条目，可直接提交至 GitHub 仓库。
