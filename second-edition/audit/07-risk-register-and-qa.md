# 07 · Risk register and pre-rewrite QA report

Status: pre-rewrite. This is a sampled audit, not a certification that every question, answer, diagram or rubric is correct. The first-edition PDFs remain unchanged.

## 1. QA method and coverage

Evidence files:
- `evidence/chapter-register.csv`: 57 chapter/capstone units.
- `evidence/subtopic-register.csv`: 323 numbered/capstone subtopics.
- `evidence/learning-feature-register.csv`: located unnumbered learning features; locator aid, not exhaustive feature audit.
- `evidence/verified_sample_checks.py` and `evidence/verified-sample-results.csv`: reproducible source-linked checks.
- `evidence/renders/`: selected defect and blank-page renders.

The sample ledger contains 62 checks:
- 57 chapter/capstone sample checks, at least one per chapter/capstone. All 57 agree with the sampled book values.
- 5 defect probes that confirm recorded issues/ambiguities. These are not counted as “passes” against the book.

Coverage by level: MYP1 10, MYP2 11, MYP3 10, MYP4 15, MYP5 16 checks. The ledger records physical page, reference, prompt, independent result, book value/claim and outcome.

An earlier exploratory 49-check file was discarded because many prompts were not source-anchored. It is not used as verification evidence.

## 2. Confirmed defects and required corrections

| ID | Level | Source anchor | Finding | Required correction | Status |
|---|---|---|---|---|---|
| D-01 | MYP2 | physical p.136 | Figure 7.6 caption clipped at right edge | Reflow caption/diagram; print test | Open in first edition; record erratum |
| D-02 | MYP2 | physical p.242 | Answer equations/cost text clipped | Reflow answer block; print test | Open |
| D-03 | MYP3 | physical p.189 | “r≈0 rules out a linear trend” overstates evidence | Replace with “suggests little linear association in these data; non-linear patterns may remain” | Open |
| D-04 | MYP4 | physical p.441 / printed p.430 | Dice-game answer says a single game always has a winner/loser; totals other than 7/8 award neither | Correct language; keep P(neither)=25/36 | Open |
| D-05 | MYP5 | physical p.145 / printed p.132 | SSA two-triangle condition overgeneralised | State `b sin A < a < b` for two triangles; equality/other cases give zero/one | Open |
| D-06 | MYP5 | physical p.232 / printed p.219 | 2×2 matrix called 3×3 | Correct order label and any dependent text | Open |
| D-07 | MYP5 | physical p.234 / printed p.221 | Day-origin ambiguity in modelling prompt | Define day 0/day 1 and units | Open |
| D-08 | MYP5 | physical p.235 / printed p.222 | Raw LaTeX visible | Render mathematics properly | Open |
| D-09 | MYP5 | physical p.240 / printed p.227; answer p.323 | Profit hint sign slip: `900−4a` with `a=−5` gives gain, not loss | Correct hint to `900+4a` for P(48), loss `−4a` | Open |
| D-10 | MYP5 | physical p.241 / printed p.228; answer p.324 | Tank prompt omits open top/lid pricing | State open top or price lid; answer key acknowledges ambiguity | Open |
| D-11 | MYP5 | answer p.322, Exercise 11B Q1(a) | Only-one-variable ambiguity | Repair student prompt; do not confuse with Exercise 11A Q3 | Open |
| D-12 | MYP5 | physical p.328 / printed p.315 | Raw LaTeX visible in revision answer | Render mathematics properly | Open |
| D-13 | MYP4/5 | blank pages listed in repository inventory | Blank/off-white pages may be intentional but are not explained | Remove or label intentional blanks in second edition | Decision needed |

## 3. Alignment and design risks

| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| R-01 | Missing editable sources forces lossy PDF conversion | High | High | Recover sources; otherwise rebuild editable manuscript with PDFs as reference | User/production |
| R-02 | School curriculum/pathway documents missing | High | High | Supply current guide, planners, hours, assessment policy, standard/extended decision | User/school |
| R-03 | MYP4–5 content labelled extended/enrichment without approval | Medium | High | Pathway decision; label core/extension/enrichment | User/school |
| R-04 | Planner lists criteria not evidenced by tasks | High | High | Criterion-evidence map; task-level strand audit | Editor |
| R-05 | MYP3 Criterion C omits strand v; B stops at verify | High | Medium | Repair planner maps and task demands | Editor/school |
| R-06 | MYP4 map/opener concept/context mismatches | High | Medium | Choose one lens per chapter; align map, opener, task, reflection | User/editor |
| R-07 | Local concept vocabulary presented as prescribed | Medium | Medium | Concept policy: prescribed default, explicit local additions | User/editor |
| R-08 | ATL labels without measurable statements | High | Medium | Exact ATL wording; practice/feedback/evidence map | Editor |
| R-09 | Contexts generic or unverified | High | Medium | Data provenance rule; verified/simulated Benin/Africa/world contexts | Editor |
| R-10 | Answer-key errata not reflected in student prompts | High | High | Repair student text; maintain errata log; full answer sweep | Editor/QA |
| R-11 | Diagrams not redrawable or print-unsafe | High | High | Recover/rebuild diagram sources; A4 print test | Production |
| R-12 | Challenge tiers increase arithmetic length only | Medium | Medium | Tier by reasoning, representation, constraint, transfer | Editor |
| R-13 | DP-only content inserted to make MYP5 advanced | Medium | High | Bounded DP-readiness language; pathway approval | User/editor |
| R-14 | First-edition PDFs overwritten | Low | Critical | Archive rule; separate second-edition directories; hash checks | Production |
| R-15 | Unapproved commit/merge/export | Low | High | Approval gate; branch-only work; no main commits | Agent/user |

## 4. QA checks completed

- Repository/ref/history inspection and SHA-256 manifest.
- PDF technical inspection: page count, size, encryption, bookmarks, embedded files, fonts, raster XObjects, blank pages.
- Chapter/subtopic structural registers repaired against TOC/body headings.
- Source-linked sample calculations for every chapter/capstone.
- Targeted visual confirmation of clipping, raw LaTeX, dice answer and blank pages.
- Concept/context/ATL/criterion scan and planner/opener extraction.
- Vertical progression and duplication analysis.

## 5. QA not yet completed

- Full question-by-question answer matching for all exercises.
- Full assessment rubric validation against current official descriptors and school policy.
- Full diagram redraw and geometric/statistical accuracy sweep.
- Full readability, accessibility, colour, greyscale and A4 print/export test.
- Verification of every real-world datum, price, currency and source.
- Recovery of editable sources and reproducible build.
- Independent human review of prototype and final exports.

## 6. Release gates

A level may not be exported as a verified second edition until:
1. Editable sources and build are reproducible.
2. All confirmed defects for that level are repaired or explicitly deferred with user approval.
3. Full answer/diagram/rubric QA is complete.
4. Criterion/ATL/concept maps are approved.
5. Print/export QA passes.
6. User approves the level for release.
