# Contributing to AI-HPP

Thank you for your interest in contributing to the AI-HPP standard! This document provides guidelines for contributing to the project.

---

## 🎯 Mission

AI-HPP aims to create a comprehensive, implementable standard for ethical autonomous AI systems. We welcome contributions that:

- Improve clarity and precision
- Add practical implementation guidance
- Identify gaps or vulnerabilities
- Provide real-world case studies
- Translate content to other languages
- Strengthen mathematical foundations

---

## 🛡️ Core Principles Protection

**IMPORTANT:** The following principles are **IMMUTABLE** and cannot be changed or removed:

1. $W_{life} \to \infty$ — Human life has infinite weight
2. Human-in-the-Loop — Final accountability with humans
3. Engineering Hack First — Always seek solutions where everyone lives
4. Evidence Vault — All critical decisions must be recorded
5. No Purposeless Revenge — Responsibility over retribution

Contributions that contradict these principles will not be accepted.

---

## 🤝 How to Contribute

### Types of Contributions

#### 1. Bug Reports / Clarifications
Found ambiguity, typo, or error?

- **Where:** [GitHub Issues](https://github.com/your-repo/issues)
- **Label:** `bug` or `clarification`
- **Include:**
  - Location (document, section, line)
  - Description of issue
  - Suggested correction (if any)

**Example:**
```
Title: Ambiguity in Module 2 interpretability threshold
Location: v3/modules/Module_02_Interpretability.md, line 45
Issue: "threshold > 0.7" — is this inclusive or exclusive?
Suggestion: Clarify as ">= 0.7" or "> 0.7"
```

#### 2. Enhancement Proposals
Have an idea to improve AI-HPP?

- **Where:** [GitHub Issues](https://github.com/your-repo/issues)
- **Label:** `enhancement`
- **Include:**
  - Problem statement (what gap does this address?)
  - Proposed solution
  - Affected modules/sections
  - Backward compatibility analysis
  - Implementation complexity (low/medium/high)

**Example:**
```
Title: Add quantum computing safety considerations
Problem: v3.0 doesn't address quantum AI systems
Proposed Solution: New Module 11 or addendum to Module 8
Affected: Potentially all modules (cryptographic assumptions)
Compatibility: Additive, doesn't break existing implementations
Complexity: High (requires expert review)
```

#### 3. Implementation Examples
Built something using AI-HPP?

- **Where:** Pull Request to `examples/`
- **Include:**
  - Use case description
  - Which modules implemented
  - Technology stack
  - Code/configuration with comments
  - Lessons learned
  - README explaining the example

**Requirements:**
- Must follow AI-HPP core principles
- Code should be well-commented
- Include testing approach
- Specify license (must be compatible with CC BY-SA 4.0)

#### 4. Case Studies / Research
Real-world experience or academic research?

- **Where:** Pull Request to `whitepapers/` or new `case-studies/`
- **Include:**
  - Clear title and abstract
  - Methodology
  - Findings
  - Implications for AI-HPP
  - References

**Encouraged topics:**
- Security analysis (like Claude's review)
- Mathematical proofs
- Implementation challenges
- Regulatory analysis
- Ethical considerations

#### 5. Translations
Help make AI-HPP accessible globally!

- **Where:** Pull Request to `translations/`
- **Structure:** `translations/[lang-code]/`
- **Include:**
  - Full translation of core documents
  - Translator credits
  - Date of translation
  - Which version translated (e.g., "v3.0 as of 2026-01-16")

**Priority languages:** Ukrainian (UA), German (DE), French (FR), Spanish (ES), Chinese (ZH), Japanese (JA)

**Important:** Mathematical notation and YAML schemas should remain in English for consistency.

---

## 📝 Contribution Process

### Step 1: Discussion (Recommended for large changes)

Before investing significant time, open an Issue to discuss:

- Is this aligned with AI-HPP mission?
- Is this the right approach?
- Are there existing efforts in this area?

### Step 2: Fork & Branch

```bash
git clone https://github.com/your-repo/AI-HPP.git
cd AI-HPP
git checkout -b feature/your-feature-name
```

### Step 3: Make Changes

**Documentation:**
- Follow existing formatting (Markdown)
- Use clear, precise language
- Include examples where helpful
- Cross-reference related sections

**Code/Examples:**
- Follow language-specific best practices
- Comment extensively
- Include tests if applicable
- Document dependencies

### Step 4: Test

**Documentation changes:**
- Verify Markdown renders correctly
- Check all links work
- Ensure mathematical notation displays properly

**Code changes:**
- Run tests
- Verify against AI-HPP principles
- Test edge cases

### Step 5: Commit

Use clear, semantic commit messages:

```bash
git commit -m "docs: clarify interpretability threshold in Module 2"
git commit -m "feat(examples): add autonomous vehicle HITL example"
git commit -m "fix: correct Evidence Vault schema YAML syntax"
```

**Commit message format:**
- `docs:` — Documentation changes
- `feat:` — New feature or content
- `fix:` — Bug fix or correction
- `refactor:` — Restructuring without changing content
- `test:` — Adding or updating tests
- `chore:` — Maintenance tasks

### Step 6: Push & Pull Request

```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub with:

**Title:** Clear, concise description
**Description:**
- What: What does this change?
- Why: Why is this change needed?
- How: How does it work?
- Testing: How was it tested?
- Backward compatibility: Does this break anything?

**Checklist:**
- [ ] Follows AI-HPP core principles
- [ ] Documentation is clear
- [ ] Links work
- [ ] Mathematical notation correct
- [ ] Examples tested (if applicable)
- [ ] Commit messages are semantic
- [ ] No conflicts with main branch

### Step 7: Review & Iterate

- Maintainers will review your PR
- Address feedback through additional commits
- Discussion happens in PR comments
- Once approved, maintainers will merge

---

## 🎨 Style Guide

### Documentation Style

**Clarity over cleverness**
- Use simple, precise language
- Define technical terms
- Provide examples
- Avoid jargon when possible

**Structure**
- Use headings hierarchically (H1 → H2 → H3)
- Include table of contents for long documents
- Use lists for multiple items
- Use tables for comparisons

**Mathematical Notation**
- Use LaTeX for math: `$W_{life} \to \infty$`
- Define variables before use
- Include units where applicable

**Code Blocks**
- Specify language: ```yaml, ```python, etc.
- Include comments
- Show expected output when helpful

### YAML Style

```yaml
# Good: Clear structure, comments
module_name:
  setting: "value"          # Explanation of setting
  nested:
    option_a: true
    option_b: false         # Why false?

# Bad: No comments, unclear structure
module_name:
  setting: "value"
  nested: {option_a: true, option_b: false}
```

---

## 🔍 Review Criteria

Contributions are evaluated on:

### Technical Correctness
- Mathematically sound?
- Logically consistent?
- Implementable?

### Alignment with Mission
- Supports AI-HPP goals?
- Maintains core principles?
- Addresses real-world needs?

### Clarity
- Easy to understand?
- Well-documented?
- Includes examples?

### Completeness
- Addresses edge cases?
- Includes testing approach?
- Documents limitations?

### Backward Compatibility
- Breaks existing implementations?
- Migration path provided?
- Versioning appropriate?

---

## 🚫 What We Won't Accept

### Principle Violations
- Removing or weakening core principles
- Optimizing for outcomes over human life
- Removing human accountability
- Enabling revenge or retribution

### Incomplete Contributions
- "I have an idea but haven't worked it out"
- Code without documentation
- Proposals without implementation consideration

### Scope Creep
- Features unrelated to AI safety/ethics
- Marketing content
- Promotional material
- Unrelated projects

### Low Quality
- Unclear writing
- Untested code
- Broken links
- Plagiarism

---

## 🏆 Recognition

Contributors will be recognized in:

- CHANGELOG.md (for significant contributions)
- Credits section of affected documents
- GitHub contributors list

**Note:** AI-HPP is a collaborative effort. We aim to credit all contributors fairly while maintaining the coherence and quality of the standard.

---

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of:
- Age, body size, disability, ethnicity
- Gender identity and expression
- Level of experience
- Nationality
- Personal appearance
- Race, religion
- Sexual identity and orientation

### Our Standards

**Positive behavior:**
- Using welcoming and inclusive language
- Respecting differing viewpoints
- Accepting constructive criticism gracefully
- Focusing on what's best for the community
- Showing empathy toward others

**Unacceptable behavior:**
- Harassment, trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information
- Any conduct inappropriate in a professional setting

### Enforcement

Violations will result in:
1. **Warning** — First offense (minor)
2. **Temporary ban** — Repeated or serious violations
3. **Permanent ban** — Severe or persistent violations

Report violations to: [contact email]

---

## ❓ Questions?

- **General questions:** Open a [Discussion](https://github.com/your-repo/discussions)
- **Specific issues:** Open an [Issue](https://github.com/your-repo/issues)
- **Security concerns:** Email [security contact] (do not open public issue)
- **Contact author:** [Evgeniy Vasyliev on LinkedIn](https://www.linkedin.com/in/evgeniy-vasyliev/)

---

## 📚 Resources for Contributors

### Understanding AI-HPP
- [README.md](./README.md) — Overview
- [CHANGELOG.md](./CHANGELOG.md) — Version history
- [v3.0 Standard](./v3/AI-HPP-2026_Standard_v3.0.md) — Latest draft
- [Claude's Review](./v3/AI-HPP-2026_Claude_Review.md) — Security analysis

### Technical Resources
- [Engineering Hack Math](./whitepapers/Engineering_Hack_Math.md) — Mathematical foundations
- [Module Specifications](./v3/modules/) — Detailed requirements
- [Examples](./examples/) — Implementation examples

### Regulatory Context
- [EU AI Act](https://artificialintelligenceact.eu/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [UNESCO AI Ethics Recommendation](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics)

---

## 🙏 Thank You!

Every contribution, large or small, helps make AI safer and more ethical. Whether you're fixing a typo or proposing a new module, your effort matters.

Together, we're building a framework for AI that serves humanity while respecting human dignity and life.

---

*"The best contribution is the one that makes AI safer for everyone."*
