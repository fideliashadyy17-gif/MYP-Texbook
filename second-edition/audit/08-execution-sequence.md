# 08 · Execution sequence starting with MYP1

Status: proposed. No rewrite, export, commit or merge is authorised by this document. The current audit stops for user review and approval.

## 1. Git and preservation workflow

- Keep the five root PDFs untouched as the first-edition archive.
- Work only on the dedicated second-edition branch. Do not commit directly to `main`.
- Before any commit/merge, summarise changes and wait for approval where review is required.
- Use a new directory convention, for example:

```text
second-edition/
  audit/                     # this pre-rewrite audit
  sources/
    myp1/
      manuscript/
      diagrams/
      data/
      styles/
    myp2/
    ...
  exports/
    myp1/
      MYP-Mathematics-1-Student-Coursebook-Second-Edition-v0.1.pdf
    ...
  qa/
    myp1/
      answer-checks.csv
      diagram-checks.csv
      export-checks.md
    ...
  errata/
    first-edition-errata.md
```

- Predictable export names: level, edition, version. Do not overwrite first-edition filenames.
- Keep sources needed to reproduce PDFs: manuscript, diagram sources, data, styles, fonts/licences, build scripts and lockfiles.
- Record SHA-256 hashes of first-edition PDFs and verified exports.

## 2. Phase 0 · Approval gate (now)

Deliverables submitted:
1. Repository inventory.
2. Curriculum-source inventory.
3. Chapter audits for MYP1–MYP5.
4. Vertical progression/gap/duplication analysis.
5. Common design/chapter template.
6. Level priorities.
7. Risk register and QA report.
8. Execution sequence.

User decisions required before Phase 1:
- Approve audit findings and framework, or request revisions.
- Supply/approve current official guide and school planning documents.
- Confirm MYP4–5 pathway and enrichment policy.
- Confirm concept-vocabulary and ATL policy.
- Choose MYP1 prototype chapter.
- Confirm visual identity recovery approach and context/data policy.

## 3. Phase 1 · MYP1 prototype

Scope: one complete chapter plus minimal shared production scaffolding. Do not rewrite the whole book.

Steps:
1. Recover editable sources if available; otherwise create a new editable source project using the PDF as reference.
2. Extract first-edition visual tokens: colours, typography, spacing, chapter-opener rhythm, icons, diagram style.
3. Build shared styles and components: inquiry, key idea, worked example, practice tiers, criterion task, reflection.
4. Rewrite the approved prototype chapter using the common template flexibly.
5. Add exact ATL statements and evidence.
6. Add one genuine Criterion B investigation and one genuine Criterion D contextual task where appropriate.
7. Create/edit diagram sources and data files with provenance.
8. Write answer key and sample responses.
9. Run QA: mathematics, answer matching, diagrams, criterion evidence, readability, print/export.
10. Export a versioned prototype PDF and present it for approval.

Prototype acceptance:
- Editable source rebuilds the PDF.
- No confirmed defect carried forward.
- Criterion/ATL maps match task evidence.
- Visual identity is recognisably first-edition-derived.
- User approves prototype before scaling.

## 4. Phase 2 · MYP1 full level

After prototype approval:
1. Apply approved components chapter by chapter.
2. Maintain chapter-level QA ledger and errata log.
3. Reconcile annual criterion/ATL coverage.
4. Full answer/diagram/rubric sweep.
5. Print/export QA.
6. User approval before MYP1 release.

## 5. Phase 3 · MYP2–MYP5 one level at a time

For each level:
1. Confirm level priorities and pathway decisions.
2. Repair confirmed defects first.
3. Rewrite/revise chapters using approved framework.
4. Align vertical progression contracts with adjacent levels.
5. Full QA and export.
6. User approval before moving to the next level.

Suggested order: MYP1 → MYP2 → MYP3 → MYP4 → MYP5. MYP4–5 may require parallel pathway planning, but production should remain one level at a time.

## 6. Phase 4 · Series-level QA and release

1. Cross-level notation, glossary, formula bank and progression audit.
2. Confirm all four branches across the programme.
3. Confirm criterion/ATL coverage each year.
4. Confirm context/data provenance and inclusion policy.
5. Final print/export/accessibility QA.
6. Release only after explicit user approval.

## 7. Stop rule

If a required source, curriculum decision or approval is missing, stop and ask. Do not invent school policy, official descriptors, data, prices, sources, commit hashes or export verification. Do not rewrite or export any book until the audit/framework is approved.
