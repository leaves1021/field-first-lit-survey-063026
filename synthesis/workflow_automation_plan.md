# Run001 工作流自动化规划

## Purpose

Run001 的价值不只是找到几篇论文，而是把一条从 search metadata 到 figure-level evidence 的 field-first workflow 跑通了一遍。这个文件总结 Run001 测试过的环节，并提出后续自动化设计：减少反复创建小型 ad hoc plan、减少重复确认，同时保留真正需要人工判断的 gate。

本文件只是规划文档，不修改任何 CSV、notes、scripts、PDF、extracted text 或 `references.bib`。

## What Run001 Tested

Run001 已经测试过以下工作流模块：

| workflow step | Run001 tested behavior | current pain point |
|---|---|---|
| metadata verification | 从 `candidate_papers.csv` 出发，核对 DOI / PMID / PMCID / Semantic Scholar ID，并更新候选状态 | 需要多次手工检查 preview table 与 CSV header |
| Zotero / `references.bib` integration | 将 Zotero key、collection、references.bib 状态纳入确认逻辑 | Zotero / references.bib 状态检查目前主要靠人工叙述 |
| PDF download / text extraction | 从官方 OA / PMC / publisher 路径获取 PDF，并用 `scripts/extract_pdf_text.py` 抽取 Markdown | 文件存在、路径、low-text warning、YAML metadata 等检查可以脚本化 |
| note generation | 基于 extracted text 生成三篇 full-text notes | prompt 可模板化，schema 可自动检查 |
| note QC | 检查 note schema、candidate row header、evidence separation、causal_status 保守性 | QC 目前靠一次次生成独立 Markdown plan |
| candidate table cleanup | 将候选 note 中的 `paper_matrix.csv` / `figure_evidence_table.csv` 预案对齐真实表头 | header 对齐、缺失字段、citekey 缺失应自动检查 |
| figure-level PDF-check planning | 规划哪些图需要人工 PDF 复核，以及确认 / 降级 / hold 规则 | 这一步应保留人工判断，但 prompt 和结果格式可模板化 |

Run001 也验证了一个重要边界：automation 可以检查格式、状态和一致性，但不能替代 full-text reading、paper selection、figure-level evidence promotion 和最终 synthesis 判断。

## Steps That Should Become Automated Scripts

### `scripts/validate_tables.py`

建议功能：
- 验证 `candidate_papers.csv`、`confirmed_papers.csv`、`paper_matrix.csv`、`figure_evidence_table.csv` 的 header 是否与项目约定完全一致。
- 检查 DOI / PMID / PMCID / arXiv ID / Semantic Scholar ID / citekey 是否重复。
- 检查必填字段是否为空，例如 confirmed paper 的 `citekey`、`title`、`doi`、`pdf_path`、`extracted_text_path`。
- 检查 status transition 是否合理：
  - `candidate_title_level` -> `candidate_metadata_verified`
  - `candidate_metadata_verified` -> confirmed row
  - confirmed row -> `ready_for_reading`
  - note-ready row -> matrix promotion plan
- 输出 Markdown 或 JSON summary，供后续 prompt 使用。

### `scripts/validate_notes.py`

建议功能：
- 检查 note 是否包含固定章节：
  - Citation metadata
  - One-paragraph summary
  - Research question
  - Task / behavior
  - Species / brain area / recording method
  - Neural object analyzed
  - Main findings
  - Figure-by-figure evidence map
  - Modeling relevance
  - Relation to field-first survey axes
  - Uncertainty / caveats
  - Candidate entries for future `paper_matrix.csv`
  - Candidate entries for future `figure_evidence_table.csv`
- 检查候选 `paper_matrix.csv` 行是否包含真实表头：
  `paper,citekey,year,category,field_axis,species,brain_area_or_scale,task_or_behavior,neural_measurement,neural_object,computation,causal_status,key_finding_short,modeling_opportunity,identifiers,uncertainty,notes`
- 检查候选 `figure_evidence_table.csv` 行是否包含真实表头：
  `paper,citekey,figure_or_table,result_section,page,claim,evidence_summary,variable_or_neural_object,analysis_method,causal_status,relevance_to_research_question,uncertainty,notes`
- 检查是否出现危险措辞，例如把 extracted-text-only claim 写成 confirmed figure evidence。
- 检查 `causal_status` 是否使用保守词表。

### `scripts/check_no_leaked_paths.py`

建议功能：
- 扫描 commit-eligible Markdown / CSV / BibTeX 文件，防止出现：
  - Zotero local storage path
  - absolute local PDF path
  - extracted full-text dump
  - API key / token pattern
- 允许 repo-relative 路径，例如：
  - `papers/raw_pdf/<citekey>.pdf`
  - `papers/extracted_text/<citekey>.md`
- 输出违规路径、文件、行号和建议修复。

### `scripts/run_lit_batch.py`

建议先不要马上做完整 orchestrator。等 validators 稳定后，再让它做轻量编排：
- 读取 batch config，例如 `configs/run001.yml`。
- 调用 search scripts，但默认 dry-run。
- 调用 validators。
- 生成 batch summary。
- 不自动下载 PDF，不自动 promote figure evidence。

### Batch Summary Generation

可以先做成 `scripts/summarize_batch.py` 或放入 `run_lit_batch.py`：
- 汇总每个 batch 的候选数量、确认数量、ready_for_reading 数量、note 数量、QC 状态。
- 汇总未通过 validators 的原因。
- 自动生成一个 commit-safe Markdown summary，例如：
  `synthesis/run001_batch_summary.md`

## Steps That Should Become Prompt Templates

### `templates/prompts/candidate_selection_prompt.md`

用途：
- 输入 search review / title-level review。
- 输出一批 proposed candidates。
- 保留人工选择 gate，不直接写 CSV。

### `templates/prompts/paper_note_prompt.md`

用途：
- 输入 `confirmed_papers.csv` row、extracted text path、PDF extraction result。
- 输出单篇 paper note。
- 固定 note schema，要求分离：
  - paper claim
  - extracted evidence
  - model / agent interpretation
  - user-facing survey interpretation

### `templates/prompts/note_qc_prompt.md`

用途：
- 输入一批 notes 和表头。
- 输出 schema completeness、evidence quality、promotion readiness、manual PDF inspection needs。
- 标准化 `paper_matrix_ready_after_minor_cleanup`、`figure_evidence_ready_after_pdf_check` 等状态。

### `templates/prompts/figure_pdf_check_prompt.md`

用途：
- 输入 note 候选 figure rows 和 PDF check plan。
- 辅助人工记录 figure / panel 检查结果。
- 输出 future results file：
  `synthesis/archive/run001/figure_evidence_pdf_check_results_run001.md`

### `templates/prompts/paper_matrix_promotion_prompt.md`

用途：
- 输入 validated notes、QC results、`paper_matrix.csv` header。
- 输出 proposed append preview。
- 不直接写 CSV，除非用户明确批准。

### `templates/prompts/figure_evidence_promotion_prompt.md`

用途：
- 输入 PDF check results、note candidate rows、`figure_evidence_table.csv` header。
- 输出 final append preview。
- 必须要求人工确认每条 figure evidence 是否 `confirmed / revised / rejected`。

## Human Gates That Must Remain

| gate | why it remains human |
|---|---|
| paper selection | 需要判断 paper 是否服务 field-first survey，而不是只按关键词或 citation count 选择 |
| full-text note acceptance | 需要判断 note 是否准确、是否过度推断、是否适合 advisor-facing framing |
| figure-level evidence promotion | 必须人工看 PDF panel-to-claim mapping，不能从 extracted text 自动确认 |
| final research-question / synthesis decisions | 需要把证据放回研究问题、field axes 和 advisor discussion 语境中 |
| exclusion / hold decisions for ambiguous papers | 方法论文、preprint、review、clinical-only drift 等需要语境判断 |

自动化应该减少重复确认，而不是移除判断。脚本可以说“这个 row 合法 / 不合法”，但不应该说“这条 figure claim 已经是 confirmed evidence”。

## Proposed Future Batch Workflow

### 1. Search / Metadata Batch

输入：
- `configs/run001.yml`
- search topics
- query strings
- source list

自动化：
- 调用 `scripts/search_pubmed.py`、`scripts/search_semantic_scholar.py`、`scripts/search_arxiv.py`
- 保存 raw metadata 到 `data/raw/`
- 保存 per-search CSV 到 `tables/`
- 运行 table validator

人工 gate：
- 选择哪些 title-level records 进入 candidate pool。

输出：
- search review
- candidate append plan
- candidate table append preview

### 2. Confirm / PDF / Extraction Batch

输入：
- approved candidate rows
- stable identifiers
- Zotero / `references.bib` status

自动化：
- 验证 DOI / PMID / PMCID / S2 ID 是否一致。
- 检查 Zotero key / references.bib 是否存在。
- 检查 PDF path / extracted text path 是否符合 repo-relative convention。
- 运行 PDF extraction only when explicitly requested.

人工 gate：
- 批准哪些 candidates 进入 `confirmed_papers.csv`。
- 批准是否下载 PDF。

输出：
- confirmed rows preview
- PDF / extraction result summary

### 3. Notes Batch

输入：
- confirmed rows with `ready_for_reading`
- extracted text files
- `paper_note_prompt.md`

自动化：
- 生成 note draft。
- 运行 `validate_notes.py`。
- 输出 missing sections / header mismatch / causal_status warning。

人工 gate：
- 接受、修订或 hold note。

输出：
- `notes/<citekey>.md`
- note validation summary

### 4. QC Batch

输入：
- notes
- table headers
- `note_qc_prompt.md`

自动化：
- 检查 note schema。
- 检查 candidate row headers。
- 检查 obvious risky phrasing。
- 生成 batch-level QC summary。

人工 gate：
- 决定是否进入 matrix promotion 或先修 note。

输出：
- note QC report
- cleanup checklist

### 5. Matrix Promotion

输入：
- validated notes
- accepted QC report
- `paper_matrix.csv` header

自动化：
- 生成 append preview。
- 检查 duplicate DOI / citekey / normalized title-year。
- 检查 category / field_axis / causal_status 词表。

人工 gate：
- 批准 append。

输出：
- approved `paper_matrix.csv` append rows

### 6. Figure Evidence Promotion After PDF Inspection

输入：
- figure PDF check plan
- manually inspected PDF results
- candidate figure rows from notes

自动化：
- 检查每条 figure claim 是否有 `confirmed / revised / rejected`。
- 检查 `causal_status` 是否保守。
- 生成 append preview。

人工 gate：
- 必须人工确认 PDF panel-to-claim mapping。

输出：
- approved `figure_evidence_table.csv` append rows

### 7. Synthesis

输入：
- `paper_matrix.csv`
- `figure_evidence_table.csv`
- accepted notes

自动化：
- 汇总 field-axis coverage。
- 统计 evidence density。
- 列出 unresolved gaps。

人工 gate：
- 最终研究问题、survey framing、advisor-facing narrative。

输出：
- synthesis draft
- candidate research questions
- advisor discussion packet

## Proposed New Files Or Scripts

只建议创建，不在本步骤实际创建：

| proposed path | type | purpose |
|---|---|---|
| `configs/run001.yml` | config | 记录 batch id、queries、sources、topics、target papers、allowed transitions |
| `scripts/validate_tables.py` | script | 检查 CSV schema、重复 ID、状态转换、路径字段 |
| `scripts/validate_notes.py` | script | 检查 note schema、候选 row header、figure evidence 候选字段 |
| `scripts/check_no_leaked_paths.py` | script | 防止 Zotero local path、absolute path、API key、full-text leakage |
| `scripts/run_lit_batch.py` | script | 后期轻量 orchestrator，先 dry-run，再逐步接入搜索、验证、summary |
| `templates/prompts/paper_note_prompt.md` | prompt template | 标准化 full-text note generation |
| `templates/prompts/note_qc_prompt.md` | prompt template | 标准化 note QC |
| `templates/prompts/figure_pdf_check_prompt.md` | prompt template | 标准化人工 PDF inspection results |

## Recommended Next Implementation Order

优先做低风险 validators，再考虑 full orchestrator：

1. `scripts/validate_tables.py`
   - 先只检查 header、row counts、duplicate identifiers。
   - 不写文件，只输出 report。

2. `scripts/check_no_leaked_paths.py`
   - 先扫描 `synthesis/`、`notes/`、`tables/`、`references.bib`。
   - 只报错，不自动修复。

3. `scripts/validate_notes.py`
   - 先检查固定章节和 candidate row headers。
   - 再逐步加入 causal_status / figure evidence wording checks。

4. Prompt templates
   - `paper_note_prompt.md`
   - `note_qc_prompt.md`
   - `figure_pdf_check_prompt.md`

5. Batch summary generator
   - 汇总 candidate / confirmed / ready_for_reading / note / QC 状态。

6. `configs/run001.yml`
   - 用 Run001 复盘填一个 static example config。

7. `scripts/run_lit_batch.py`
   - 最后做，只负责串联 validators 和 summary。
   - 搜索、PDF、CSV append 都保持显式 opt-in。

## Boundary Conditions

- PDFs 和 extracted full text 保持 local / ignored，不进入 GitHub。
- GitHub 只跟踪 metadata、notes、plans、manifests、scripts、templates。
- `figure_evidence_table.csv` 不能在没有人工 PDF inspection 的情况下自动追加。
- automation 的目标是减少重复确认、减少格式错误、减少漏字段，不是移除 human judgment。
- 所有 API key、Zotero local storage path、absolute local PDF path 都不得进入 tracked files。
- prompt-generated notes 不能直接变成 confirmed evidence；必须经过 QC 和人工 acceptance。
- review / perspective papers 不能作为 primary experimental evidence，除非明确标记为 review-level synthesis。
- 对 core papers，不能只依赖 abstract；需要使用 full PDF text 和 figure / result anchors。

## Minimal Success Criteria

下一轮实现如果只完成下面几件事，就已经足够降低重复劳动：

- `validate_tables.py` 能确认四张 CSV 的 header、重复 ID、状态值。
- `validate_notes.py` 能确认 notes 的章节完整性和候选 row header。
- `check_no_leaked_paths.py` 能拦住绝对本地路径、Zotero storage path、API key pattern。
- prompt templates 能把候选选择、note generation、note QC、figure PDF check 统一成稳定输入输出。

这样后续每个 batch 就可以从“很多小计划”压缩成：

1. 运行 batch。
2. 运行 validators。
3. 人工批准 gate。
4. 生成 append preview。
5. 人工确认 append。
