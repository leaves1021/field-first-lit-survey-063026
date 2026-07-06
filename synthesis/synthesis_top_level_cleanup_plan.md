# Synthesis Top-level Cleanup Plan

## Purpose

本文件是一个针对 `synthesis/` 顶层目录文档整理的 user-reviewable plan。它的目的是在 README 稳定化之后，明确哪些 `synthesis/*.md` 文件应该继续保持活跃（keep active）、哪些应该归档（archive candidate），以及哪些需要用户进行显式决策（needs user decision）。

**本计划仅作为 proposed plan。在此步骤中，不执行任何文件移动、重命名或删除操作。**

## Current top-level synthesis files

当前 `synthesis/` 顶层共有如下 9 个 `.md` 文件，其分类与初步建议如下：

| 文件路径 | 状态分类 | 建议与原因简述 |
|---|---|---|
| `synthesis/run001_first_batch_completion_summary.md` | `keep active` | 记录 Run001 第一批次的完成状态，属于活跃的阶段性成果记录，应保持在顶层可见。 |
| `synthesis/figure_evidence_followup_plan_run001.md` | `keep active` | 记录 Run001 剩余图表证据的跟进计划，仍有未完成的活跃项，应保持顶层可见。 |
| `synthesis/workflow_automation_plan.md` | `keep active` | 属于长期工作流设计与自动化规划参考，并非中间产物，建议保留。 |
| `synthesis/search_plan_v1.md` | `needs user decision` | 作为 Run001 的检索设计基础已经使用完毕；但其 query plan 部分对 Run002 检索仍有参考价值，建议由用户决定是归档还是保留到 Run002 启动。 |
| `synthesis/project_usability_cleanup_plan.md` | `needs user decision` | 记录整个项目易用性重构的总体路线图，当前正在执行各 Phase 阶段，建议由用户决定是否在清理彻底完成后再归档。 |
| `synthesis/local_cleanup_action_plan.md` | `needs user decision` | 记录本地 14 项临时测试文件的清理规划，在用户正式批准执行这 14 项删除操作前，应当保持可见。 |
| `synthesis/local_ignored_files_inventory.md` | `needs user decision` | 作为 `local_cleanup_action_plan.md` 的源清单（source inventory），在本地清理（Phase 5）完成前应当与清理计划保持同步可见，由用户决策其归档时机。 |
| `synthesis/synthesis_archive_move_plan_run001.md` | `archive candidate` | 该归档方案在之前的步骤中已被执行（标记为 "archive move executed"），已属于历史记录，建议归档。 |
| `synthesis/prompt_templates_qc.md` | `archive candidate` | 属于对 prompt templates 进行 QC 的历史审计记录，且该 QC 只覆盖了 3/5 的模板（已过时），建议归档。 |

## Recommended keep-active files

以下文件在目前阶段推荐继续保持在 `synthesis/` 顶层：

1. **`synthesis/run001_first_batch_completion_summary.md`**：这是当前唯一已完成 Batch 的最高级成果入口，也是 Run002 启动前的重要比对基准。
2. **`synthesis/figure_evidence_followup_plan_run001.md`**：记录了尚未解决的图表证据提取跟进项，属于未结案的工作。
3. **`synthesis/workflow_automation_plan.md`**：长期的工程化与设计参考，指导后续 batch 配置与脚本改造。

## Recommended archive candidates

以下文件已完成其历史使命，或属于纯元级维护记录，推荐归档移动至 `synthesis/archive/run001/`：

1. **`synthesis/synthesis_archive_move_plan_run001.md`**：此文档记录了 Run001 的 24 个文件的归档计划且已被执行。它本身也应该作为 Run001 的一部分进行归档。
2. **`synthesis/prompt_templates_qc.md`**：虽然是一份审计参考，但它所提出的修改意见均已在 Phase 1 中被采纳并合入模板，其审计使命已完成。

## User decisions needed

需要用户在批准执行前做出如下明确决策：

1. **`synthesis/search_plan_v1.md` 是否保留？**
   - *保留理由*：在 Run002 启动并编写新的 Search Plan 之前，此文件是检索策略的唯一参考。
   - *归档理由*：该方案是针对 Run001 编写的，里面的很多具体限制可能不适用于 Run002。
   - *初步建议*：**保留在顶层**，直到 Run002 搜索范围规划完毕后再归档。

2. **`synthesis/project_usability_cleanup_plan.md` 是否保留？**
   - *保留理由*：它定义了 5 个 Phase 的重构，目前仅执行到 Phase 3A，作为后续重构（Phase 3B/4/5）的依据，应当保留在顶层供 Agent 读取。
   - *归档理由*：可以将其归档，重构指示由用户直接在 Prompt 中发出。
   - *初步建议*：**保留在顶层**，直到所有 Phase 彻底执行完毕并验证通过后再归档。

3. **`synthesis/local_cleanup_action_plan.md` 与 `synthesis/local_ignored_files_inventory.md` 是否保留？**
   - *保留理由*：`local_cleanup_action_plan.md` 内含 14 个待用户批准删除的本地 smoketest/API-test 文件规划，而 `local_ignored_files_inventory.md` 是其所依赖的源清单（source inventory）。在用户显式同意并执行这些删除（Phase 5 本地清理）之前，这两个文件应保持相互可见并同步留在顶层，以防止误删或对清理文件失去追溯能力。
   - *初步建议*：**保留在顶层**，直到删除操作被用户批准并执行（Phase 5 本地清理完成）后再进行归档。

## Proposed move table

如果用户批准归档，以下文件将计划执行移动（并不做任何删除）：

| 待归档源文件路径 (Source) | 建议归档目标路径 (Proposed Destination) | 归档原因 | 需要用户审批 |
|---|---|---|---|
| `synthesis/synthesis_archive_move_plan_run001.md` | `synthesis/archive/run001/synthesis_archive_move_plan_run001.md` | 方案已执行完毕，移入历史归档 | 是 |
| `synthesis/prompt_templates_qc.md` | `synthesis/archive/run001/prompt_templates_qc.md` | 审计结果已合并到 prompt，文件已过时 | 是 |

*注：`synthesis/local_ignored_files_inventory.md` 仅在 Phase 5 本地清理完成并验证无误后，才作为未来的归档候选文件进行移动。*

## Execution boundary

*   **当前步骤不执行任何实际的移动、重命名或删除操作。**
*   在用户对上述 "User decisions needed" 给出明确指示，且单独发出 "Proceed with archive" 的指令后，方可由 Agent 新建一个 move action 执行移动。
*   在执行任何归档移动后，必须在虚拟环境下运行以下校验程序：
    - `& .\.venv\Scripts\python.exe .\scripts\validate_tables.py`
    - `& .\.venv\Scripts\python.exe .\scripts\validate_notes.py`
    - `& .\.venv\Scripts\python.exe .\scripts\check_no_leaked_paths.py`

## Final recommendation

ready_for_user_review
