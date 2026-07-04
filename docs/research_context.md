# Research Context

## Purpose

本文件记录当前文献综述项目的研究方向背景。它描述为什么采用 field-first 方法、当前关注哪些 field axes，以及哪些方向被有意排除在第一轮默认中心之外。

这不是 workflow 规则文件（那是 `AGENTS.md` 和 `docs/workflow_quickstart.md` 的职责），而是研究背景文件。**随着研究方向演化，本文件内容可以修改。**

## Why field-first

本项目的目标不是确认一个预设的研究方向，而是先建立一个结构化的证据库，用于评估：

- 广泛的 field-level research axes
- 代表性实验论文
- 候选研究问题
- 可行的计算建模方法

采用 field-first 方法的原因是：过早锁定到 PFC / working memory / subspace / low-rank RNN 等具体方向，可能会让文献证据选择偏向已有假设，而不是让证据真正引导研究问题的形成。

## Current field axes

当前 survey 优先覆盖以下 field axes（Run001 及后续 batch 都应以此为导向，而不是以任何单一脑区或机制为默认中心）：

1. **brain-wide / distributed computation** — 多脑区、全脑尺度的神经活动组织
2. **population dynamics and neural manifolds** — 神经群体状态空间、latent dynamics、流形结构
3. **flexible behavior and cognitive control** — 灵活行为、认知控制、任务适应
4. **multi-area communication and routing** — 多脑区通讯、信号路由、interaction subspace
5. **causal perturbation and model-based intervention** — 光遗传、微刺激、因果干预、closed-loop
6. **NeuroAI and interpretable trained models** — 可解释的训练模型、RNN 分析、NeuroAI 方法

## What is not the default center

以下方向在当前 survey 中被有意设定为非默认中心：

- **PFC / prefrontal cortex** — 可以作为 case study 纳入，但不是第一轮检索的默认核心
- **working memory** — 同上
- **sequence tasks** — 可以作为具体实验范式出现，但不应主导 paper selection 方向
- **subspaces** — 作为 analysis method 可以出现，但不应让整个 survey 锁定到 subspace-centric framing
- **low-rank RNNs** — 作为建模工具可以出现，但不应主导候选论文分类

这些方向被限制的原因不是它们不重要，而是：用它们作为默认出发点会让 field-first survey 退化为一个以预设方向为中心的文献回顾。

## Relation to seed papers

Run001 使用了两篇 seed papers 用于校准搜索范围和字段结构：

| seed paper | role in survey | main relevance |
|---|---|---|
| Vyas 2020, *Computation Through Neural Population Dynamics* | review / perspective | population dynamics; computation through dynamics; dynamical systems framing |
| Ye 2026, *Brain-wide topographic coordination of rotating waves* | experimental landmark | brain-wide distributed dynamics; structural constraints on mesoscale activity |

这两篇 seed papers 不应将整个 survey 锁定到 motor cortex、rotating waves、PFC、working memory 或任何单一机制。

## How to use this file

- **Agents**: 在执行 literature search、candidate selection、paper classification 时，应参考本文件判断当前 survey 的 scope 和优先级，而不是仅凭 search query 或 paper title 的字面匹配。
- **Project owner**: 当研究方向发生实质性变化（例如正式进入 PFC case study 阶段、或扩展到新的 field axis），应先更新本文件，再相应调整 search plan 和 batch config。
- **Future batch configs**: `configs/run_template.yml`（计划中）应引用本文件中的 field axes 作为 batch scope 的来源之一。

## Change history

| date | change |
|---|---|
| 2026-07-04 | 初始版本，从 AGENTS.md "Working principles" 和 "Project purpose" 中迁出 research-specific 内容 |
