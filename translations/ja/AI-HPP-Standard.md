# TODO: Native speaker verification needed

> **免責事項 (Japanese):** この文書はAI支援による翻訳であり、誤りを含む可能性があります。正式な参照元は英語版です。PRを歓迎します。
>
> **Disclaimer (English):** This is an AI-assisted translation. It may contain inaccuracies. The English text is authoritative. Pull requests are welcome.

# AI-HPP-Standard（日本語訳）

本書は、監査可能な安全実装を目的とした AI-HPP-2025 標準の日本語訳です。

## 不変の中核原則

1. **W_life → ∞** — 人命の重みは無限。
2. **Human-in-the-Loop (HITL)** — 最終責任は人間が負う。
3. **Engineering Hack First** — まず全員の生存を満たす第三の解を探す。
4. **No Purposeless Revenge** — 報復ではなく責任と再発防止。
5. **Evidence Vault** — 重大判断は監査可能な形で記録する。

## 適用範囲

人命、権利、重要インフラ、安全重要プロセスに影響し得る意思決定AIに適用します。

## Module 構成（12モジュール）

- **Module 01: Agentic Orchestration** — エージェント連携と責任連鎖。
- **Module 02: Interpretability** — 判断理由と説明可能性。
- **Module 03: Zero Trust** — 最小権限と実行境界。
- **Module 04: Data Provenance** — データ由来と改変履歴。
- **Module 05: Physical Safety** — 物理世界での安全制御。
- **Module 06: Vulnerable Groups** — 脆弱な利用者の保護。
- **Module 07: Green Compute** — 安全を維持した計算効率。
- **Module 08: Adversarial Robustness** — 敵対的入力への耐性。
- **Module 09: Graceful Degradation** — リスク上昇時の段階的縮退。
- **Module 10: Multi Jurisdiction** — 複数法域での適合管理。
- **Module 11: Multi Agent Governance** — マルチエージェント統治。
- **Module 12: Regulatory Interface Requirement (RIR)** — 規制監査向け出力。

## 運用要件

- 高リスク操作にはHITL承認ゲートを必須化。
- 重要イベントをEvidence Vaultへ記録。
- Tool Execution Boundaryを強制。
- failure signal時にdegradation stateへ遷移。

## 透明性と監査

- 決定文脈、理由、承認者、実行結果を記録。
- 監査出力にredaction policyとintegrity hashを含める。
- JSON schemaに適合する機械可読アーティファクトを維持。

## 注意事項

- 法的助言ではありません。
- AI-HPP準拠でも残余リスクは存在します。
- 導入前に法務レビューが必要です。

## コミュニティTODO

- ネイティブ話者による精読。
- 用語統一（監査・安全・規制関連）。
- 実運用ケースの日本語追補。
