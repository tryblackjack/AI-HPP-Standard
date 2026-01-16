# AI-HPP Translations

This directory will contain translations of AI-HPP standard into various languages.

## 🌍 Translation Status

| Language | Code | v2.2 | v3.0 | Translator | Date |
|----------|------|------|------|------------|------|
| English | EN | ✅ | ✅ | Original | 2026-01-16 |
| Ukrainian | UA | 🔄 | ⏳ | TBD | — |
| German | DE | ⏳ | ⏳ | TBD | — |
| French | FR | ⏳ | ⏳ | TBD | — |
| Spanish | ES | ⏳ | ⏳ | TBD | — |
| Chinese | ZH | ⏳ | ⏳ | TBD | — |
| Japanese | JA | ⏳ | ⏳ | TBD | — |

**Legend:**
- ✅ Complete
- 🔄 In progress
- ⏳ Planned
- ❌ Not planned

## 🎯 Priority Languages

1. **Ukrainian (UA)** — Author's native language, critical for Ukrainian contributors
2. **German (DE)** — EU AI Act primary language
3. **Chinese (ZH)** — Large AI research community
4. **French (FR)** — International diplomacy language
5. **Spanish (ES)** — Wide global usage
6. **Japanese (JA)** — Major AI research hub

## 📝 Translation Guidelines

### What to Translate

**Must translate:**
- Full text of standard documents
- Explanations and examples
- Principles and guidelines
- README files

**Keep in English:**
- Mathematical notation (e.g., $W_{life} \to \infty$)
- YAML configuration keys (e.g., `evidence_vault:`, `human_in_loop:`)
- Technical identifiers
- Code snippets (comments can be translated)
- Module IDs (e.g., "Module_01_Agentic_Orchestration.md")

**Translate but note original:**
- Technical terms (provide English in parentheses first occurrence)
- Example: "Хранилище доказательств (Evidence Vault)"

### Directory Structure

```
translations/
├── README.md                  # This file
├── ua/                        # Ukrainian
│   ├── README_ua.md
│   ├── AI-HPP-2026_Standard_v3.0_ua.md
│   ├── CHANGELOG_ua.md
│   └── modules/
│       └── Module_01_ua.md
├── de/                        # German
│   └── ...
└── [language-code]/
    └── ...
```

### Translation Metadata

Each translated document should include:

```markdown
---
**Translation Information:**
- **Original:** AI-HPP-2026 Standard v3.0
- **Language:** Ukrainian (Українська)
- **Translator:** [Name]
- **Date:** 2026-01-XX
- **Status:** Complete / In Progress / Draft
- **Last Sync:** 2026-01-16 (original v3.0 release)

**Автентичний текст:** Тільки англійська версія є офіційною. При конфліктах англійська версія має пріоритет.
**Authentic Text:** Only the English version is authoritative. In case of conflicts, English version takes precedence.
---
```

### Style Guidelines

- **Maintain formality level** — AI-HPP is a technical standard, not casual documentation
- **Preserve mathematical precision** — Don't simplify technical terms
- **Cultural adaptation** — Examples can be adapted to local context while preserving principle
- **Consistency** — Use same translation for recurring terms throughout

### Technical Terms Glossary

Create a glossary file for each language: `translations/[code]/GLOSSARY.md`

Example:
```markdown
| English | Ukrainian | Notes |
|---------|-----------|-------|
| Evidence Vault | Хранилище доказательств | Keep English in first mention |
| Human-in-the-Loop | Людина в циклі | Acronym: ЛвЦ |
| Engineering Hack | Інженерний хак | Keep "hack" untranslated |
```

## 🤝 How to Contribute a Translation

1. **Check existing efforts** — Is someone already working on this language?
2. **Announce your intent** — Open an Issue: "Translation: [Language] - [Document]"
3. **Create directory structure** — Follow the pattern above
4. **Start with README** — Translate main README.md first (it's most visible)
5. **Translate incrementally** — Don't try to translate everything at once
6. **Get review** — Ask native speakers to review for accuracy and fluency
7. **Submit PR** — Follow the contribution guidelines in CONTRIBUTING.md

## ✅ Quality Checklist

Before submitting a translation:

- [ ] Translation metadata included
- [ ] Mathematical notation unchanged
- [ ] YAML keys unchanged
- [ ] Technical terms in glossary
- [ ] Reviewed by native speaker
- [ ] Links updated to translated versions (where available)
- [ ] Formatting preserved (headings, lists, tables)
- [ ] Code examples work (if modified)
- [ ] Commit message clear: "translation(ua): Add Module 1 translation"

## 🌟 Recognition

Translators will be credited:
- In the translated document header
- In the translation status table above
- In CHANGELOG.md
- As GitHub contributors

## 📧 Coordination

To coordinate translation efforts:
- **Discuss:** Use [GitHub Discussions](https://github.com/your-repo/discussions) with `translation` tag
- **Collaborate:** Multiple translators for same language? Coordinate via Issues
- **Review:** Native speakers please help review submissions

## ⚠️ Important Notes

### Official Status
Only the **English version** is the official, authoritative text. Translations are provided for accessibility but in case of any conflict, the English version prevails.

### Versioning
When the English version is updated (e.g., v3.0 → v3.1), translations must be updated. Mark outdated translations clearly:

```markdown
⚠️ **Translation Status:** This translation is based on v3.0 (2026-01-16).
The English version has been updated to v3.1. Translation update in progress.
```

### Licensing
Translations are derivative works under CC BY-SA 4.0 (same as original). Translators retain attribution but standard's license applies.

---

## 🙏 Thank You to Future Translators!

Making AI-HPP accessible in multiple languages is crucial for global adoption of ethical AI principles. Your contribution helps ensure AI safety transcends language barriers.

---

*"Safety speaks every language."*
*"Безпека розмовляє всіма мовами."* 🇺🇦
*"La sécurité parle toutes les langues."* 🇫🇷
*"安全性は全ての言語を話します。"* 🇯🇵
