# MYP Mathematics 1–5 · Second-edition pre-rewrite audit

Status: **STOPPED for review and approval**. No book has been rewritten, exported, committed or merged. The five first-edition PDFs are unchanged.

Repository: `fideliashadyy17-gif/MYP-Texbook`  
Branch: `arena/122604d9-myp-texbook`  
Live/main HEAD: `910ec1cce82e7dbe4074def33bf7b1128cb7f4e9`  
Audit date: 2026-11-01

## Deliverables

| # | Deliverable | File |
|---|---|---|
| 1 | Repository inventory | [01-repository-inventory.md](01-repository-inventory.md) |
| 2 | Curriculum-source inventory | [02-curriculum-source-inventory.md](02-curriculum-source-inventory.md) |
| 3 | Chapter/subtopic audits | [Index](03-chapter-audits.md) · [MYP1](chapter-audits/myp1-audit.md) · [MYP2](chapter-audits/myp2-audit.md) · [MYP3](chapter-audits/myp3-audit.md) · [MYP4](chapter-audits/myp4-audit.md) · [MYP5](chapter-audits/myp5-audit.md) |
| 4 | Vertical progression/gaps/duplication | [04-vertical-progression.md](04-vertical-progression.md) |
| 5 | Common design/chapter template | [05-common-design-framework.md](05-common-design-framework.md) |
| 6 | Level priorities | [06-level-priorities.md](06-level-priorities.md) |
| 7 | Risk register and QA report | [07-risk-register-and-qa.md](07-risk-register-and-qa.md) |
| 8 | Execution sequence starting with MYP1 | [08-execution-sequence.md](08-execution-sequence.md) |

## Evidence

- [Chapter register](evidence/chapter-register.csv): 57 chapter/capstone units with pages, branch, concepts, planner strands, keep/improve/issues/decision.
- [Subtopic register](evidence/subtopic-register.csv): 323 numbered/capstone subtopics, titles repaired against TOC/body headings.
- [Learning-feature register](evidence/learning-feature-register.csv): located unnumbered investigations/applications/tasks/reviews; locator aid, not exhaustive.
- [Sample QA script](evidence/verified_sample_checks.py) and [results](evidence/verified-sample-results.csv): 62 source-linked checks; 57 chapter samples agree, 5 defect probes confirm issues.
- [Repository manifest](evidence/repository-manifest.json): hashes, page counts, PDF metadata, missing materials.
- [Selected renders](evidence/renders/): clipping, raw LaTeX, dice answer and blank-page evidence.

## Executive findings

1. **All five first editions are present.** MYP3 is available; the earlier missing-MYP3 claim came from a stale checkout.
2. **The repository is PDF-only.** No editable manuscript, diagram sources, build scripts, fonts or school planning documents are present. A safe second edition requires source recovery or a new editable source project.
3. **The series has genuine vertical progression in most threads.** Revisited topics should not be deleted merely because they recur; the audit proposes progression contracts where demand must increase.
4. **Confirmed defects need repair before reuse.** These include MYP2 clipping, MYP3 correlation overstatement, MYP4 dice-game winner/loser contradiction, MYP5 SSA overgeneralisation, MYP5 capstone prompt defects and raw LaTeX.
5. **Assessment alignment needs tightening.** Planner lists do not prove criterion evidence. MYP3 Criterion C omits strand v; MYP3 B must move beyond verification. MYP4 map/opener concept/context mismatches must be resolved.
6. **MYP4–5 pathway is a user decision.** Several MYP5 chapters are extended/enrichment-leaning. Do not label them mandatory or DP-only without school approval.
7. **ATL statements need the exact required wording.** The phrase “In order for a student to… students must…” was not found in the books.
8. **QA is sampled, not exhaustive.** Every chapter/capstone has at least one source-linked sample check, but full answer/diagram/rubric/print QA remains a release gate.

## Approval requested

Please review and decide:

1. Approve the audit/framework, or request revisions.
2. Supply/approve current official guide and school planning documents.
3. Confirm MYP4–5 standard/extended/enrichment pathway.
4. Approve concept-vocabulary and ATL policy.
5. Choose the MYP1 prototype chapter.
6. Approve visual identity recovery and Benin/Africa/world context/data policy.
7. Authorise Phase 1 only after the above decisions.

No rewrite, export, commit or merge should occur before approval.
