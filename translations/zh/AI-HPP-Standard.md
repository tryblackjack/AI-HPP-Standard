# TODO: Native speaker verification needed

> **免责声明（简体中文）:** 本文为 AI 辅助翻译，可能存在不准确之处。英文版本为权威文本。欢迎提交 PR 改进。
>
> **Disclaimer (English):** This is an AI-assisted translation. It may contain inaccuracies. The English text is authoritative. Pull requests are welcome.

# AI-HPP-Standard（简体中文译本）

本文件是 AI-HPP-2025 标准的中文译本，面向可审计、可落地的工程实施。

## 不可变核心原则

1. **W_life → ∞** — 人类生命权重为无限。
2. **Human-in-the-Loop (HITL)** — 最终问责仍由人类承担。
3. **Engineering Hack First** — 优先寻找“所有人都能存活”的第三方案。
4. **No Purposeless Revenge** — 强调责任与纠正，不鼓励报复。
5. **Evidence Vault** — 关键决策必须保留可审计证据。

## 适用范围

适用于会影响生命安全、人权、关键基础设施或高风险流程的决策型 AI 系统。

## Module 结构（12 个模块）

- **Module 01: Agentic Orchestration** — 代理协同与责任链。
- **Module 02: Interpretability** — 决策可解释与因果说明。
- **Module 03: Zero Trust** — 最小权限、强边界、显式授权。
- **Module 04: Data Provenance** — 数据来源与变更可追溯。
- **Module 05: Physical Safety** — 物理环境安全约束。
- **Module 06: Vulnerable Groups** — 脆弱群体保护与升级机制。
- **Module 07: Green Compute** — 兼顾安全的计算效率。
- **Module 08: Adversarial Robustness** — 对抗攻击与规避行为防护。
- **Module 09: Graceful Degradation** — 风险上升时的分级降级。
- **Module 10: Multi Jurisdiction** — 多司法辖区合规映射。
- **Module 11: Multi Agent Governance** — 多代理治理与共识控制。
- **Module 12: Regulatory Interface Requirement (RIR)** — 监管审计接口与导出。

## 运行要求

- 高风险动作必须经过 HITL 审批门控。
- 关键决策链写入 Evidence Vault。
- 严格执行 Tool Execution Boundary。
- 触发故障信号时进入对应 degradation state。

## 透明度与审计

- 记录上下文、理由、审批、执行结果。
- 导出包必须包含 redaction policy 与 integrity hash。
- 所有关键工件应通过 JSON schema 验证。

## 文档边界

- 本文不构成法律意见。
- AI-HPP 合规不代表零风险。
- 上线前仍需法务与本地合规审查。

## 社区 TODO

- 由母语专家进行校审。
- 统一技术术语翻译。
- 补充行业化落地案例。
