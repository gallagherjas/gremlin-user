# 👹 Gremlin User

[![CI](https://github.com/gallagherjas/gremlin-user/actions/workflows/ci.yml/badge.svg)](https://github.com/gallagherjas/gremlin-user/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[English](README.md) | [简体中文](README.zh-CN.md)

一个教编码智能体（coding agent）用真实用户的误用行为测试 Web 应用的 skill：重复操作、被中断的请求、过期的标签页、会话失效、奇怪输入、并发编辑。

常规 UI 测试只走预期路径，真实用户不会。Gremlin User 把用户带给真实软件的行为补进测试：反复点击、过期标签页、失效会话、奇怪输入、被中断的请求、互相冲突的编辑。

智能体会确认每一个失败、收集证据，并为确认的缺陷编写回归测试。

## 示例

一个结账测试在"点一次、网络干净"的条件下可以通过。Gremlin User 会让同样的流程遭遇响应丢失和重试：

```text
提交订单
请求已离开浏览器后连接中断
服务端可能已提交订单
连接恢复
用户重试
```

一份有用的结果长这样：

```text
[HIGH] Retry after unknown outcome creates a duplicate order

Invariant: one purchase intent creates one order
Observed: two orders share the same cart and customer
Evidence: two POST /orders requests, two created order IDs
Likely cause: retry path has no idempotency guard
Regression: tests/checkout/retry-after-timeout.spec.ts
```

完整走查见 [`examples/checkout.md`](examples/checkout.md) 和 [`examples/crud-app.md`](examples/crud-app.md)（英文）。

## 工作原理

Gremlin User 不乱点一气。每个 Gremlin 都是一个命名的失败假设（failure hypothesis），从流程的状态变更中挑选。

1. 梳理流程，写下它必须保持的不变量——"一次购买意图只创建一个订单"、"过期的编辑器不能无声覆盖更新的版本"。
2. 先跑通正常路径（happy path），然后每次只改变一个条件：时序、输入、导航、网络、会话或并发。
3. 复现每一个疑似缺陷，把产品 bug 与自动化噪声区分开，之后才写进报告。
4. 用项目现有的测试技术栈，为确认的缺陷补回归测试。

## Gremlins

| Gremlin | 测试内容 |
| --- | --- |
| Click | 重复操作与加载态（pending）控制 |
| Form | 校验、归一化与边界输入 |
| Navigation | 刷新、前进/后退、过期页面、被中断的跳转 |
| Network | 超时、响应丢失、重试与恢复 |
| Session | 会话过期、登出与权限变更 |
| Concurrency | 多标签页、多用户与并发写入 |
| Data | 数值、日期、标识符、导入与文本边界 |

完整场景库见 [`references/gremlin-catalog.md`](references/gremlin-catalog.md)（英文）。

## 模式

| 模式 | 增加什么 |
| --- | --- |
| Mild | 常见边界情况，低改动风险 |
| Spicy | 网络中断、会话过期、竞争标签页、受控的服务端错误 |
| Unhinged | 组合两个真实条件（前提是各自单独通过），保持明确的失败假设并守住测试边界 |

## 安装

适用于任何支持开放 Agent Skills `SKILL.md` 格式的智能体客户端。浏览器自动化与 Python 均为可选项。

本仓库根目录就是 skill 目录：把它克隆（或下载解压）为 `gremlin-user`，放进你的智能体客户端能发现的 skills 目录即可。

| 客户端 | 位置 |
| --- | --- |
| Claude Code | `.claude/skills/gremlin-user/`（项目级）或 `~/.claude/skills/gremlin-user/`（全局） |
| Codex | `.codex/skills/gremlin-user/` |
| 其他客户端 | 见你的客户端的 skills 目录 |

保持文件夹完整、`SKILL.md` 位于根目录。`tests/`、CI 配置等仓库附带文件无害——智能体只读 `SKILL.md` 及其引用的文件。

## 使用

让智能体带着这个 skill 测试某条流程：

```text
用 gremlin-user 测试创建订单流程，跑 Mild 模式。
```

```text
对 staging 环境做 auth 和会话过期的 Gremlin 测试。不要发真实邮件。
```

```text
用支付沙箱对这条结账流程跑 Spicy 模式。
```

智能体会先跑正常路径，挑选与流程匹配的 Gremlins，确认每个疑似缺陷，并在项目条件允许时补回归覆盖。没有浏览器自动化时，它会产出一份可执行的 Gremlin 测试计划，而不是声称未执行的场景通过或失败。

## Gremlin 分数

每次运行用分数总结已执行场景的结果：

```text
score = passed / (passed + failed) * 100
```

被阻塞（blocked）与不确定（inconclusive）的场景不计入分母。运行辅助脚本：

```bash
python scripts/gremlin_score.py --passed 28 --failed 6 --blocked 3
```

```text
Gremlin Score: 82/100
Passed: 28
Failed: 6
Blocked or inconclusive: 3
```

把这个分数当作本次运行的摘要，而不是产品质量评分。

## 安全边界

变更类测试请在本地、预览、staging、沙箱或专用测试环境中使用测试数据。真实支付、真实消息、非测试数据、真实用户权限和基础设施压力，都要挡在运行之外——除非被授权的测试系统为该操作提供了安全路径。

测试带外部副作用的流程之前，先读 [`references/safety.md`](references/safety.md)（英文）。

## 命名与前身

"Gremlin" 在这里指没人盯着时捣乱机器的小精灵，不是那家混沌工程公司。本项目与 Gremlin Inc. 无关。

把捣乱的用户放进应用的历史很久远，最著名的是猴子测试库 [gremlins.js](https://github.com/marmelab/gremlins.js)。Gremlin User 用编码智能体实现同一想法：以不变量驱动的场景选择、证据收集与回归覆盖，取代随机 fuzzing。

## 贡献

一个好的 Gremlin 要写清它攻击的不变量、执行步骤，以及确认缺陷所需的证据。具体要求、仓库结构和测试命令见 [CONTRIBUTING.md](CONTRIBUTING.md)（英文）。

## 许可证

[MIT](LICENSE)
