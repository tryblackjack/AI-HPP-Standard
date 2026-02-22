# TODO: Native speaker verification needed

> **إخلاء مسؤولية (Arabic):** هذه ترجمة بمساعدة الذكاء الاصطناعي وقد تحتوي على أخطاء. النسخة الإنجليزية هي المرجع المعتمد. نرحب بطلبات السحب (PRs).
>
> **Disclaimer (English):** This is an AI-assisted translation. It may contain inaccuracies. The English text is authoritative. Pull requests are welcome.

# AI-HPP-Standard (ترجمة عربية)

هذه ترجمة عربية لمعيار AI-HPP-2025 بهدف دعم التنفيذ الهندسي القابل للتدقيق.

## المبادئ الأساسية غير القابلة للتعديل

1. **W_life → ∞** — حياة الإنسان ذات وزن لا نهائي في التحسين.
2. **Human-in-the-Loop (HITL)** — المسؤولية النهائية تبقى بيد الإنسان.
3. **Engineering Hack First** — البحث أولاً عن خيار يحافظ على حياة الجميع.
4. **No Purposeless Revenge** — المساءلة لا الانتقام.
5. **Evidence Vault** — توثيق جميع القرارات الحرجة بشكل قابل للمراجعة.

## نطاق التطبيق

ينطبق المعيار على أنظمة AI ذات قدرة اتخاذ القرار التي قد تؤثر على الحياة أو الحقوق أو البنية التحتية الحرجة أو عمليات السلامة.

## هيكل Module (12 وحدات)

- **Module 01: Agentic Orchestration** — تنسيق الوكلاء وسلسلة المسؤولية.
- **Module 02: Interpretability** — تفسير القرارات وربط المخرجات بالأدلة.
- **Module 03: Zero Trust** — أقل صلاحية ممكنة وحدود تنفيذ واضحة.
- **Module 04: Data Provenance** — مصدر البيانات وسجل التحويلات.
- **Module 05: Physical Safety** — ضوابط أمان في العالم المادي.
- **Module 06: Vulnerable Groups** — حماية الفئات الهشة وحدود المحتوى.
- **Module 07: Green Compute** — كفاءة حوسبية مع الحفاظ على السلامة.
- **Module 08: Adversarial Robustness** — مقاومة الهجمات والمحفزات العدائية.
- **Module 09: Graceful Degradation** — تقليل القدرات بشكل آمن عند زيادة المخاطر.
- **Module 10: Multi Jurisdiction** — مواءمة الامتثال عبر ولايات قضائية متعددة.
- **Module 11: Multi Agent Governance** — حوكمة أنظمة متعددة الوكلاء.
- **Module 12: Regulatory Interface Requirement (RIR)** — واجهة تصدير منظمة للمراجعة الرقابية.

## متطلبات تشغيلية

- تطبيق بوابات HITL للقرارات عالية المخاطر.
- تسجيل القرارات والأسباب في Evidence Vault.
- فرض Tool Execution Boundary ومنع التنفيذ غير المصرح.
- تشغيل آلية degradation state عند مؤشرات الفشل.

## الشفافية والتدقيق

- تسجيل سلسلة القرار والموافقات والسياق.
- تضمين سياسة redaction و integrity hash في حزم التصدير.
- إنتاج ملفات JSON متوافقة مع schemas للتحقق الآلي.

## حدود الوثيقة

- ليست استشارة قانونية.
- الامتثال لا يضمن انعدام المخاطر.
- مراجعة قانونية محلية مطلوبة قبل الاعتماد.

## TODO للمجتمع

- مراجعة لغوية من متحدثين أصليين.
- توحيد المصطلحات التقنية العربية.
- إضافة أمثلة تطبيقية محلية.
