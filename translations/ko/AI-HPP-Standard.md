# TODO: Native speaker verification needed

> **면책 고지 (Korean):** 이 문서는 AI 보조 번역이며 부정확한 표현이 있을 수 있습니다. 영어 원문이 권위 있는 기준 문서입니다. PR 기여를 환영합니다.
>
> **Disclaimer (English):** This is an AI-assisted translation. It may contain inaccuracies. The English text is authoritative. Pull requests are welcome.

# AI-HPP-Standard (한국어 번역)

이 문서는 감사 가능한 안전 구현을 위한 AI-HPP-2025 표준의 한국어 번역본입니다.

## 변경 불가 핵심 원칙

1. **W_life → ∞** — 인간 생명 가중치는 무한이다.
2. **Human-in-the-Loop (HITL)** — 최종 책임은 인간에게 있다.
3. **Engineering Hack First** — 모두가 생존하는 제3의 해법을 우선 탐색한다.
4. **No Purposeless Revenge** — 보복이 아니라 책임성과 재발 방지.
5. **Evidence Vault** — 핵심 의사결정은 감사 가능하게 기록한다.

## 적용 범위

생명·권리·핵심 인프라·안전중요 프로세스에 영향을 줄 수 있는 의사결정형 AI 시스템에 적용됩니다.

## Module 구조 (12개 모듈)

- **Module 01: Agentic Orchestration** — 에이전트 오케스트레이션과 책임 추적.
- **Module 02: Interpretability** — 의사결정 해석 가능성 및 근거.
- **Module 03: Zero Trust** — 최소권한과 실행 경계 강제.
- **Module 04: Data Provenance** — 데이터 출처 및 변경 이력.
- **Module 05: Physical Safety** — 물리적 안전 제약과 페일세이프.
- **Module 06: Vulnerable Groups** — 취약 사용자 보호 및 에스컬레이션.
- **Module 07: Green Compute** — 안전을 유지하는 효율적 연산.
- **Module 08: Adversarial Robustness** — 적대적 조작 및 회피 대응.
- **Module 09: Graceful Degradation** — 위험 상태별 단계적 기능 축소.
- **Module 10: Multi Jurisdiction** — 다중 관할 규제 정합성.
- **Module 11: Multi Agent Governance** — 다중 에이전트 거버넌스.
- **Module 12: Regulatory Interface Requirement (RIR)** — 규제 감사용 내보내기 인터페이스.

## 운영 요구사항

- 고위험 작업은 HITL 승인 게이트를 통과해야 합니다.
- 핵심 결정 이벤트를 Evidence Vault에 기록해야 합니다.
- Tool Execution Boundary를 강제해야 합니다.
- 실패 신호 발생 시 정의된 degradation state로 전환해야 합니다.

## 투명성 및 감사

- 맥락, 판단 근거, 승인 경로, 결과를 기록합니다.
- 감사 내보내기에 redaction policy와 integrity hash를 포함합니다.
- JSON schema 검증 가능한 산출물을 유지합니다.

## 한계

- 법률 자문 문서가 아닙니다.
- AI-HPP 준수는 무위험을 의미하지 않습니다.
- 배포 전 법무 검토가 필요합니다.

## 커뮤니티 TODO

- 원어민 검수 수행.
- 용어 번역 표준화.
- 한국어 사례/시나리오 확장.
