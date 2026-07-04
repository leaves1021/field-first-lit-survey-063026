# Field-first Literature Survey Workflow

## Project purpose

本仓库用于构建一个可复现、semi-automated、field-first 的 systems neuroscience / computational neuroscience 文献综述 workflow。它的目标是先组织领域证据、代表性实验论文、计算建模机会和研究轴线，再进入更具体的研究问题。

有关当前的具体研究背景、研究轴线（field axes）以及排除 PFC / working memory 作为默认中心的考虑，请参阅 [docs/research_context.md](docs/research_context.md)。

这个项目不是 fully automated literature review。自动化主要负责 metadata 整理、schema validation、重复检查、prompt template 复用和安全检查；paper selection、full-text note acceptance、figure-level evidence promotion 和最终 synthesis 判断仍需要人工批准。

## Documentation map

项目核心文档职责划分如下：

- [AGENTS.md](AGENTS.md): 通用 agent 操作规则、安全边界、命名与引用规范。
- [docs/workflow_quickstart.md](docs/workflow_quickstart.md): 标准的 10 阶段 batch 工作流执行手册、输入输出定义和人工阀门（human gates）。
- [docs/status_vocabulary.md](docs/status_vocabulary.md): 流程中各类文献状态（status）和标签（label）的权威定义。
- [docs/file_retention_policy.md](docs/file_retention_policy.md): 文件保留、本地清理、归档和删除的规范。
- [docs/research_context.md](docs/research_context.md): 当前 survey 的研究方向背景、所选 field axes 以及脑区约束。

具体批次（batch）的执行记录、状态汇总、中间计划以及 follow-up 文档统一存放于 `synthesis/` 目录下；已完成批次的 audit trail 及历史计划已归档存放于 `synthesis/archive/` 目录。

## Repository structure

- `tables/`: Curated CSV tables。包括 `candidate_papers.csv`、`confirmed_papers.csv`、`paper_matrix.csv` 和 `figure_evidence_table.csv`。各表格精确的 schema 由 `templates/*.csv` 定义。
- `notes/`: Paper-level full-text reading notes。
- `synthesis/`: 活跃的批次总结、跟进计划、工作流自动化设计和高层综述草稿。
- `templates/`: 各种模板文件，包含 CSV 模板以及 `templates/prompts/` 下的可复用 prompt templates。
- `scripts/`: 文献搜索、PDF 提取、数据验证（validators）和路径防泄露扫描脚本（leakage checker）。
- `papers/raw_pdf/`: 本地 PDF 原文件（被 `.gitignore` 忽略，不可提交）。
- `papers/extracted_text/`: 从 PDF 提取出的纯文本（被 `.gitignore` 忽略，不可提交）。
- `data/`: 原始 API 响应及衍生出的本地生成数据（被 `.gitignore` 忽略，不可提交）。
- `logs/`: 各种工具运行的本地日志（被 `.gitignore` 忽略，不可提交）。

## Quickstart

进入仓库后，第一步先运行只读 validators，确认表格、notes 和 commit-eligible 文件没有明显问题。

Windows PowerShell 环境下建议使用项目本地的 virtual environment（`.venv`）：

```powershell
& .\.venv\Scripts\python.exe .\scripts\validate_tables.py
& .\.venv\Scripts\python.exe .\scripts\validate_notes.py
& .\.venv\Scripts\python.exe .\scripts\check_no_leaked_paths.py
```

如果项目本地的 `.venv` 不可用，请停止操作并向用户汇报，不要尝试使用未验证的全局解释器或自行安装第三方库。

## Core workflow

标准的 batch 工作流由 10 个阶段构成：

1. **Define scope** — 确定本批次的检索轴线或任务范围（参考 `docs/research_context.md`）。
2. **Search / metadata batch** — 运行 scripts 进行学术数据库检索，在 `data/raw/` 存放原始数据并在 `tables/` 存放检索 CSV。
3. **Clean / deduplicate** — 针对 DOI/PMID/S2ID/Title 进行去重。
4. **Candidate selection** — 从检索结果中初步挑选 candidate 论文并标记 status（参见 `docs/status_vocabulary.md`）。
5. **Confirmed papers** — 人工审核，验证 stable IDs，将论文加入 `confirmed_papers.csv`。
6. **PDF / extraction** — 获取 PDF 原文件并使用 `scripts/extract_pdf_text.py` 抽取文本。
7. **Note generation** — 编写或生成 paper-level notes（模板和 headings 见 `templates/paper_note_template.md` 和 `SKILL.md`）。
8. **Note QC** — 运行 QC，划分证据类型（生物、模型、方法），保证 causal status 结论保守。
9. **paper_matrix.csv promotion** — 将审核过的文献基本元数据追加到全局矩阵。
10. **figure_evidence_table.csv promotion** — 人工比对 PDF 图表细节后，将经过 visual check 的 figure-level evidence 追加到证据表。

详细的执行步骤与校验条件请查阅 [docs/workflow_quickstart.md](docs/workflow_quickstart.md)。

## Human gates

为保证综述质量，以下关键步骤必须保留人工决策与确认通道：

- **Paper selection**: 决定哪些论文进入 candidate / confirmed 状态。
- **Full-text note acceptance**: 决定 note 是否合格、是否归档。
- **Figure-level evidence promotion**: 决定具体图表证据是否满足 visual check 要求并入库。
- **Final synthesis decisions**: 各项高层科学推论和核心研究问题的确定。

## Safety and retention

为确保仓库的安全性和可维护性，必须严格遵守 `docs/file_retention_policy.md` 的规定。

请勿向仓库提交以下文件：
- 任何 PDF 文件（`papers/raw_pdf/`）
- 从 PDF 提取出的全文 Markdown（`papers/extracted_text/`）
- 任何包含 API keys、Zotero 本地绝对路径、个人邮箱等隐私信息的配置文件或环境变量（`.env`）
- 各种本地运行产生的 raw data（`data/raw/`）与 logs（`logs/`）

在清理本地忽略文件前，务必仔细比对 `synthesis/archive/` 下的历史 inventory，避免误删正在编辑的本地未同步资源。
