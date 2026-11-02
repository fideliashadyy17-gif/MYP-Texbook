# Source register · MYP1 master correction

Access date: 2026-11-02. This register separates **official IB sources**, **officially hosted research**, **school-hosted copies of IB documents**, and **third-party interpretation**. A source is not treated as current policy merely because it is indexed by a search engine.

## A. Repository First Editions (primary reference)

| Level | File used | SHA-256 | Status |
|---|---|---|---|
| MYP1 | `MYP-Mathematics-1-Student-Coursebook.pdf` | `131a3a99d14ae5a7613c7e9da24c540e29029d93a1a360abcc8516835798b3f0` | Local tracked original; unchanged |
| MYP2 | `MYP-Mathematics-2-Student-Coursebook.pdf` | `565ed7876b3cf2e16d0a7c9607fe9cf93a8edc40d599ce8772ad70ca76baa30e` | Local tracked original; unchanged |
| MYP3 | `MYP-Mathematics-3-Student-Coursebook.pdf` | `c0d5136cd423336fca35b6743eac20e6825d5537b6ea2117820d61c2bf949524` | Local original; unchanged |
| MYP4 | `MYP_Mathematics_4_Student_Coursebook.pdf` | `4e0e8a32776f43f8565966edb54f9f30c6f45e7858259bd9799931e89197c393` | Recovered read-only from `origin/main` (`FETCH_HEAD`); cached outside repo |
| MYP5 | `MYP_Mathematics_5_Student_Coursebook.pdf` | `5f2e8001623ce1e26c72a94755127ee0828c4b0756fcc6c5bc0604e223d3274f` | Recovered read-only from `origin/main` (`FETCH_HEAD`); cached outside repo |

The earlier empty MYP4/5 cache files were caused by wrong filename assumptions (`MYP-Mathematics-4/5-...`). The actual remote paths use underscores: `MYP_Mathematics_4/5_Student_Coursebook.pdf`. The empty files were removed from the cache. No repository original was modified.

## B. Official IB sources

1. **IB Mathematics subject page** — https://www.ibo.org/programmes/middle-years-programme/curriculum/mathematics/  
   Status: fetched successfully. Page states last updated 19 February 2026. Used for: four branches, standard/extended mathematics, inquiry and application, link to the 2020 subject brief.

2. **MYP curriculum page** — https://www.ibo.org/programmes/middle-years-programme/curriculum/  
   Status: fetched successfully. Last updated 19 February 2026. Used for: minimum 50 hours per subject group per year; global contexts; conceptual understanding; ATL; inclusion; interdisciplinary learning.

3. **General regulations: Middle Years Programme (2026 assessment procedures)** — https://www.ibo.org/globalassets/new-structure/become-an-ib-school/pdfs/myp-2026-general-regulations.pdf  
   Status: fetched successfully (all chunks). Used for: Article 8.1 minimum 50 hours and recommended 70 hours in final two years for eAssessment candidates; Article 8.2 required use of MYP objectives and assessment criteria; Article 9.1 only MYP year 5 students may register for IB eAssessment.

4. **MYP Mathematics subject brief (from 2020; first assessment 2022)** — https://www.ibo.org/globalassets/new-structure/brochures-and-infographics/pdfs/myp-brief-mathematics-en.pdf  
   Status: direct PDF fetch failed this turn; official URL is linked from the current IB mathematics page. Search-indexed official content and earlier verified fetch support: four branches; key concepts form, logic, relationships; four equally weighted criteria, maximum 8; factual/conceptual/debatable inquiry. Treat as the current public brief, not as a newly published 2026 guide.

## C. School-hosted copies of IB guidance (supplementary; not official-hosted)

5. **Mathematics guide (for use from September 2020/January 2021), Park Crossing High School mirror** — https://files-backend.assets.thrillshare.com/documents/asset/uploaded_file/3852/Parkcrossinghs/1d8bcb99-9dfe-46f5-b99b-b935e76a5302/Math_Guide.pdf?disposition=inline  
   Status: direct fetch failed this turn; search excerpt verified title, framework purpose, school responsibility for course organisation, and Year 1 Criterion A objective wording. Used cautiously for: four reasoning-focused branches; topics/skills as framework rather than a mandatory grade-by-grade syllabus; criterion-related assessment. Full current PDF not re-verified in this turn.

6. **Earlier Franklin / RFS guide mirrors** — retained from prior audit only as corroborating copies of the 2020 guide. Not used to claim a newer official edition.

## D. Officially hosted research (context, not policy)

7. **Evaluation of the IB MYP Mathematics Skills Framework** — https://www.ibo.org/globalassets/new-structure/research/pdfs/myp-mathematics-skills-framework-full-report-en.pdf  
   Status: search-indexed official research excerpt. Used only to support the design principle that the framework is flexible and schools plan vertical progression. Not used as an assessment regulation.

## E. Third-party interpretation (not official policy)

8. **MYP Maths: comparing old and new guides** — https://www.mypmaths.com/post/comparing-the-old-and-new-myp-maths-guides  
   Status: third-party blog, updated 31 July 2022. Used only as a flag that related concepts changed (e.g. justification/measurement replaced by approximation/validity in the 2020 guide). Any concept list used in the prototype must be checked against the guide before final approval; it is not presented here as verified official wording.

## Verification limits

- No newer official MYP mathematics guide was verified in this turn. The current official subject page still points to the 2020 brief.
- The prototype will therefore use only well-established MYP structures: objectives/criteria, inquiry, global contexts, ATL, conceptual understanding, and school-designed progression.
- Printer trim, bleed, crop marks and colour profile remain unconfirmed; no commercial print-readiness claim is made.
