# Synthesis Top-level Cleanup Plan

## Purpose

本文件是一个针对 `synthesis/` 顶层目录文档整理的 user-reviewable plan。它的目的是在 README 稳定化之后，明确哪些 `synthesis/*.md` 文件应该继续保持活跃（keep active）、哪些应该归档（archive candidate），以及哪些需要用户进行显式决策（needs user decision）。

**本计划已执行第一阶段的归档移动。**

## Execution status

- archive move executed
- 2 files moved to `synthesis/archive/run001/`
- no files deleted
- local cleanup files not touched

## Current top-level synthesis files

当前 `synthesis/` 顶层剩余 8 个 `.md` 文件，其分类与实际状态如下：

| 文件路径 | 状态分类 | 建议与原因简述 |
|---|---|---|
| `synthesis/run001_first_batch_completion_summary.md` | `keep active` | 记录 Run001 第一批次的完成状态，属于活跃的阶段性成果记录，应保持在顶层可见。 |
| `synthesis/figure_evidence_followup_plan_run001.md` | `keep active` | 记录 Run001 剩余图表证据的跟进计划，仍有未完成的活跃项，应保持顶层可见。 |
| `synthesis/workflow_automation_plan.md` | `keep active` | 属于长期工作流设计与自动化规划参考，并非中间产物，建议保留。 |
| `synthesis/search_plan_v1.md` | `needs user decision` | 作为 Run001 的检索设计基础已经使用完毕；但其 query plan 部分对 Run002 检索仍有参考价值，建议由用户决定是归档还是保留到 Run002 启动。 |
| `synthesis/project_usability_cleanup_plan.md` | `needs user decision` | 记录整个项目易用性重构的总体路线图，当前正在执行各 Phase 阶段，建议由用户决定是否在清理彻底完成后再归档。 |
| `synthesis/local_cleanup_action_plan.md` | `needs user decision` | 记录本地 14 项临时测试文件的清理规划，在用户正式批准执行这 14 项删除操作前，应当保持可见。 |
| `synthesis/local_ignored_files_inventory.md` | `needs user decision` | 作为 `local_cleanup_action_plan.md` 的源清单（source inventory），在本地清理（Phase 5）完成前应当与清理计划保持同步可见，由用户决策其归档时机。 |
| `synthesis/synthesis_top_level_cleanup_plan.md` | `needs user decision` | 本规划文件本身，作为当前活跃的用户审查方案，在归档移动正式执行并验证前应当留在顶层。 |

## Recommended keep-active files

以下文件在目前阶段推荐继续保持在 `synthesis/` 顶层：

1. **`synthesis/run001_first_batch_completion_summary.md`**：这是当前唯一已完成 Batch 的最高级成果入口，也是 Run002 启动前的重要比对基准。
2. **`synthesis/figure_evidence_followup_plan_run001.md`**：记录了尚未解决的图表证据提取跟进项，属于未结案的工作。
3. **`synthesis/workflow_automation_plan.md`**：长期的工程化与设计参考，指导后续 batch 配置与脚本改造。

## Archived in this step

在 Phase 3B 的归档步骤中，以下文件已被成功移动至 `synthesis/archive/run001/`，且没有删除任何文件：

1. **`synthesis/archive/run001/synthesis_archive_move_plan_run001.md`**：Run001 批次的归档移动计划与执行记录（已归档）。
2. **`synthesis/archive/run001/prompt_templates_qc.md`**：Prompt 模板的 QC 审计记录，其修改意见已完成，已作为历史审计 trail 归档。

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

## Executed move table

以下为 Phase 3B 中已成功执行归档移动的文件列表（未进行任何物理删除）：

| 归档源文件路径 (Source) | 归档目标路径 (Destination) | 归档原因 | 执行状态 |
|---|---|---|---|
| `synthesis/synthesis_archive_move_plan_run001.md` | `synthesis/archive/run001/synthesis_archive_move_plan_run001.md` | 方案已执行完毕，移入历史归档 | 已执行 (Executed) |
| `synthesis/prompt_templates_qc.md` | `synthesis/archive/run001/prompt_templates_qc.md` | 审计结果已合并到 prompt，文件已过时 | 已执行 (Executed) |

*注：`synthesis/local_ignored_files_inventory.md` 仅在 Phase 5 本地清理完成并验证无误后，才作为未来的归档候选文件进行移动。在此之前，它与 `synthesis/local_cleanup_action_plan.md` 均需在顶层保持相互可见并同步保留。*

## Execution boundary

*   **本步骤已执行上述两项 approved 归档移动。未做任何物理删除。**
*   在执行任何归档移动后，必须在虚拟环境下运行以下校验程序：
    - `& .\.venv\Scripts\python.exe .\scripts\validate_tables.py`
    - `& .\.venv\Scripts\python.exe .\scripts\validate_notes.py`
    - `& .\.venv\Scripts\python.exe .\scripts\check_no_leaked_paths.py`

## Final recommendation

phase3b_archive_move_complete
