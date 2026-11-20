# Editorial evidence and chapter 1 proof

For later work, see the [curriculum registers](curriculum/) and the [chapter 2 review](chapter-02-review.md).

## Repository audit

The authenticated GitHub CLI confirmed `fideliashadyy17-gif/MYP-Texbook`; the separate GitHub connector lookup returned unsupported. The working checkout was used directly. The baseline exposes one commit (`445af0d`), so earlier production history is not visible here.

| Level | Primary input at repository root | PDF pages |
|---|---|---:|
| MYP1 | `MYP-Mathematics-1-Student-Coursebook.pdf` | 240 |
| MYP2 | `MYP-Mathematics-2-Student-Coursebook.pdf` | 260 |
| MYP3 | `MYP-Mathematics-3-Student-Coursebook.pdf` | 281 |
| MYP4 | `MYP_Mathematics_4_Student_Coursebook.pdf` | 458 |
| MYP5 | `MYP_Mathematics_5_Student_Coursebook.pdf` | 340 |

Root inputs total 1,579 coursebook pages plus 18 assessment pages. Root inventory includes checksums, page counts and creation metadata. None has a PDF bookmark outline. The first three books report an original HTML/CSS print pipeline; MYP4 and MYP5 identify HeadlessChrome. This identifies a rendering route, not editable masters. No independently identifiable first-edition editable masters or standalone first-edition figures were found in the root inventory. Mathematical visuals are embedded in the PDFs. The `second-edition/` tree is a separate legacy workspace containing `sources`, `exports`, `prototype`, `audit`, `qa` and `correction-review`; it was excluded from curricular and design sourcing. Originals and that tree were left untouched.

## Assessment references

All nine two-page files were text-extracted and rendered into a contact sheet. The observations below address page composition and recognizable representation types; they are not a scale/label accuracy audit. No MYP1 assessment PDF was identified.

| Root PDF | Observed design or mathematical emphasis |
|---|---|
| `MYP2 1st Term examination.pdf` | Objective-to-theory progression; tables, Venn diagrams and compact graph prompts make students read different representations. |
| `MYP2 1st Term examination B.pdf` | Parallel exam structure; probability displays and a line graph support short interpretation prompts before longer tasks. |
| `Grade_8_MYP_3_Mathematics_Summative_Assessment.pdf` | Multiple-choice followed by substantial written work; small geometric diagrams make identifying relevant measurements part of the problem. |
| `Grade_8_MYP_3_Mathematics_Summative_Assessment_Version_B.pdf` | Number-line and geometry prompts; extended tasks require labelled reasoning rather than only selecting an option. |
| `Grade_9_MYP_4_Mathematics_Summative_Assessment.pdf` | Written statistical working and compact displays alongside short items; movement between a display and a conclusion matters. |
| `Grade_9_MYP_4_Mathematics_Summative_Assessment_Version_B.pdf` | Distribution and outlier interpretation, including rents; context gives a reason to question a summary statistic. |
| `GRADE 9 version C.pdf` | Short responses with tables, histograms and cumulative displays, followed by four criterion-focused synthesis tasks; includes an IQR outlier rule. |
| `Grade_10_MYP_5_Mathematics_Summative_Assessment.pdf` | From objective questions to written algebra, pattern diagrams and tables; a partial-sums prompt reverses the usual sequence-to-sum direction. |
| `GRade 10 version C.pdf` | Coordinate grids, response spaces and tabular questions embedded in the exam, followed by four structured synthesis tasks. |

Adaptation: use a progression from recognition to explanation, then ask students to infer a rule or defend a decision. Give graphs enough space to read independently of prose; retain the tight connection between a visual and its question without carrying over exam-density typesetting. In the MYP1 proof the direction is reversed from “round this value” to “recover the possible original values,” then those values constrain a kit-making decision. No exercise set was transplanted.

## International benchmark (initial public-source pass)

- [IB Mathematics subject brief](https://www.ibo.org/globalassets/new-structure/brochures-and-infographics/pdfs/myp-brief_mathematics_2015.pdf): public brief and its assessment example as surfaced by search. Adopt four-branch scope and make each criterion visible through the work students produce. The example’s combination of contextual data, graph and equation suggests giving students a reason to switch representations. This brief does not substitute for checking current full guidance and level-specific descriptors.
- [Oxford MYP 4&5 Standard](https://global.oup.com/education/product/9781382011020/?region=international) and [Extended](https://global.oup.com/education/product/9781382010948/?region=uk): publisher listings describe extensive practice, conceptual inquiry and enrichment. Adopt factual, conceptual and debatable questions serving different purposes, and make harder tasks require a new decision or argument rather than just larger numbers.
- [Pearson International Mathematics for the Middle Years](https://www.pearson.com/international-schools/international-baccalaureate-curriculum/ib-middle-years-myp/ib-middle-years-maths.html.html): publisher listing describes worked examples, investigations, differentiated practice, reflections and check-your-knowledge features. Adopt a visible sequence from worked reasoning to independent practice to reflection, with ATL demonstrated by an observable student action.

Publisher descriptions were not treated as evidence about actual typography, page composition or the depth of any complete exercise bank. Full copyrighted books were not examined in this benchmark. The proof’s typography, artwork and layout are independent.

## MYP1 chapter 1 source-to-proof mapping

The first-edition contents and chapter body informed this prototype. The original’s nested number families, number-line comparison, decimal place value, expanded form, rounding, estimation and contextual communication are useful foundations. Its estimation emphasis on convenient values is extended here by asking when an estimate can or cannot support a guarantee. Coverage below is for one chapter, not a full syllabus map.

| Original progression | Proof treatment |
|---|---|
| 1.1 Number systems and the number line | Classify overlapping number families; distinguish order, distance and signed location; use a vector number line and a rational counterexample. |
| 1.2 Place value and the role of zero | Read a place-value table, compare contributions of repeated digits and reason about a blank display column. |
| 1.3 Expanded form and equivalent representations | Preserve whole-number and decimal decomposition; distinguish standard expansion from regrouping for packing. |
| 1.4 Comparing, ordering and rounding | Place-value comparison and midpoint reasoning, with an inverse interval and a double-rounding counterexample. Signed-number comparison is introduced in 1.1. |
| 1.5 Estimation and sensible accuracy | Compare an estimate with exact arithmetic and test safety using bounds. |
| Community noticeboard application, review and reflection | Replace with a reuse-depot decision, a pattern investigation and mixed reasoning. Retain the question of what precision an audience needs. |

The proof uses mathematical relationships as the key concept and quantity/representation as related concepts. A partner audit of recommendation wording gives communication ATL a concrete purpose. The pattern task asks students to infer and justify a general rule (B practice); the depot task asks them to choose a model and quantify a guarantee (D practice), communicating results in a labelled table and a short note. These are original practice tasks, not official IB rubrics or claims of endorsement.

## Proof design and QA

A4 pages use ink navy, deep teal and pale mint panels, with a running series header and numbered footer. The number line uses an affine coordinate scale in SVG; the place-value table is native Typst. The proof contains five worked examples, 28 section-practice prompts, a four-question mixed review, a pattern investigation and a modelling task. No student answer key is embedded. Selected boundary and stock calculations are checked in `tools/build.py`. The seven-page layout was visually reviewed at contact-sheet scale; full-size print review and comprehensive independent numerical and editorial verification remain outstanding.

Deep chapter-by-chapter source analysis, complete vertical mappings, finished covers and preliminaries for each level, expanded exercise banks, and whole-book mathematical and visual QA are not complete. The proof must not be distributed as a complete coursebook.
