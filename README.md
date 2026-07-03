# Field-first Literature Survey Workflow

## Project purpose

本仓库用于构建一个可复现、semi-automated、field-first 的 systems neuroscience / computational neuroscience 文献综述 workflow。它的目标是先组织领域证据、代表性实验论文、计算建模机会和研究轴线，再进入更具体的研究问题。

这个项目不是 fully automated literature review。自动化主要负责 metadata 整理、schema validation、重复检查、prompt template 复用和安全检查；paper selection、full-text note acceptance、figure-level evidence promotion 和最终 synthesis 判断仍需要人工批准。

## Current entry points

Run001 first batch 已完成，并已单独文档化。README 不是 batch status report；详细 batch 状态、row counts 和未完成的 figure-level items 维护在 `synthesis/` 文档中，而不是固定写在 landing page 里。

当前建议优先查看：

- `synthesis/run001_first_batch_completion_summary.md`
- `synthesis/figure_evidence_followup_plan_run001.md`
- `synthesis/project_usability_cleanup_plan.md`

## Repository structure

- `tables/`: curated CSV tables 和部分 generated search CSV；核心表包括 `candidate_papers.csv`、`confirmed_papers.csv`、`paper_matrix.csv`、`figure_evidence_table.csv`。
- `notes/`: paper-level full-text reading notes。
- `synthesis/`: search reviews、workflow plans、append plans、completion summaries 和 higher-level synthesis。
- `templates/prompts/`: 可复用 prompt templates，用于 paper note、note QC、paper matrix promotion、figure evidence promotion 等步骤。
- `scripts/`: search scripts、PDF text extraction script、validators 和 leakage checker。
- `papers/raw_pdf/`: 本地 PDF 文件；被 `.gitignore` 忽略，不应提交。
- `papers/extracted_text/`: 本地 extracted full text；被 `.gitignore` 忽略，不应提交。
- `data/`: raw API outputs 和 processed generated data；默认作为 local generated outputs 管理。
- `logs/`: search、extraction 和 workflow logs；默认不作为 GitHub 可见入口。

## Quickstart

进入仓库后，第一步先运行只读 validators，确认表格、notes 和 commit-eligible 文件没有明显问题。

Windows PowerShell 推荐使用项目本地 virtual environment：

```powershell
& .\.venv\Scripts\python.exe .\scripts\validate_tables.py
& .\.venv\Scripts\python.exe .\scripts\validate_notes.py
& .\.venv\Scripts\python.exe .\scripts\check_no_leaked_paths.py
```

在当前 Windows sandbox context 中，`py -3` 可能因为 launcher / login-session 问题失败；优先使用 `.\.venv\Scripts\python.exe`。

## Core workflow

1. Search / metadata batch
   - 使用 `scripts/search_pubmed.py`、`scripts/search_semantic_scholar.py`、`scripts/search_arxiv.py` 生成 raw outputs 和 per-search CSV。
2. Candidate selection
   - 从 title-level review 中选择候选论文；不要直接把 search CSV 当作 confirmed evidence。
3. Confirmed papers
   - 验证 DOI / PMID / PMCID / arXiv ID / Semantic Scholar ID，并将人工批准的论文写入 `tables/confirmed_papers.csv`。
4. PDF / extraction
   - 仅在明确需要时下载官方 PDF，并用 `scripts/extract_pdf_text.py` 生成 local extracted text。
5. Note generation
   - 使用 extracted text 和 confirmed row 生成 `notes/<citekey>.md`。
6. Note QC
   - 检查 note schema、evidence separation、candidate table headers 和 conservative `causal_status`。
7. `paper_matrix.csv` promotion
   - 从已验证 notes 中生成 append plan，经用户批准后再追加 paper-level rows。
8. Figure-level PDF inspection
   - 人工检查 PDF panels / captions，确认 figure claim 与图面证据是否匹配。
9. `figure_evidence_table.csv` promotion
   - 只追加 PDF inspection 后标记为 ready 的 figure-level rows。
10. Status cleanup / completion summary
    - 同步 `confirmed_papers.csv` status，并更新 batch completion summary。

## Human gates

以下步骤必须保留人工批准：

- paper selection
- full-text note acceptance
- figure-level evidence promotion
- final research-question / synthesis decisions

自动化可以帮助发现格式错误、重复 ID、状态不一致和路径泄露，但不能替代 scientific judgment。

## Safety and retention

不要提交：

- PDFs
- extracted full text
- API keys 或 `.env`
- Zotero local storage paths
- absolute local paths
- local raw API outputs

`.gitignore` 已忽略：

- `papers/raw_pdf/*`
- `papers/extracted_text/*`
- `papers/supplementary/*`
- `data/raw/*`
- `data/processed/*`
- `logs/*`
- `tables/YYYYMMDD_search_*.csv`

删除 ignored local files 前，应先生成 local inventory，并将文件分为 `keep`、`archive`、`delete after user approval`。不要直接删除 generated outputs。

## Key current files

- `synthesis/run001_first_batch_completion_summary.md`: example completed batch summary and current Run001 record。
- `synthesis/figure_evidence_followup_plan_run001.md`: Run001 remaining figure-level follow-up items。
- `synthesis/workflow_automation_plan.md`: automation and workflow design notes。
- `synthesis/project_usability_cleanup_plan.md`: usability, docs, cleanup, and Run002 gating plan。

## Development roadmap

建议按项目基础设施建设顺序推进：

1. 创建 `docs/status_vocabulary.md`。
2. 创建 `docs/workflow_quickstart.md`。
3. 创建 `docs/file_retention_policy.md`。
4. 创建 local ignored files inventory。
5. 将 research context 从 `AGENTS.md` 拆分到独立文档。
6. 创建 `configs/run_template.yml`。
7. 然后再决定优先处理 Run001 leftovers，还是启动 Run002。
