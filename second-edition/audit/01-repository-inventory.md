# 01 · Repository inventory and source-of-truth status

Audit date: 2026-11-01. Repository: `fideliashadyy17-gif/MYP-Texbook`. Working branch: `arena/122604d9-myp-texbook`. Live `main` and local HEAD: `910ec1cce82e7dbe4074def33bf7b1128cb7f4e9`.

## 1. What is actually in the repository

The live tree contains exactly five first-edition PDFs at the repository root. There are no other branches, tags, releases, issues, pull requests, or GitHub Actions workflows in the inspected repository. The commit history consists of four upload commits:

| Commit | UTC timestamp | Content |
|---|---|---|
| `910ec1cce82e7dbe4074def33bf7b1128cb7f4e9` | 2026-11-01 16:03:12 | MYP3 PDF |
| `6f565ea512675f415d6eb3c54bbb28443af51411` | 2026-11-01 15:54:39 | MYP5 PDF |
| `637363052c44f5ce5b66d921f3c49750cb688fbe` | 2026-11-01 15:53:55 | MYP4 PDF |
| `dc98eca1fd13d44eab348116640c2742f59bb0a7` | 2026-11-01 15:52:18 | MYP1 and MYP2 PDFs |

MYP3 is present. An earlier stale checkout did not show it; live `main` and the updated checkout both contain it. The first-edition PDFs have not been modified by this audit.

| Level | File | Pages | Bytes | SHA-256 |
|---|---|---:|---:|---|
| MYP1 | `MYP-Mathematics-1-Student-Coursebook.pdf` | 240 | 16,777,029 | `131a3a99d14ae5a7613c7e9da24c540e29029d93a1a360abcc8516835798b3f0` |
| MYP2 | `MYP-Mathematics-2-Student-Coursebook.pdf` | 260 | 15,079,740 | `565ed7876b3cf2e16d0a7c9607fe9cf93a8edc40d599ce8772ad70ca76baa30e` |
| MYP3 | `MYP-Mathematics-3-Student-Coursebook.pdf` | 274 | 18,791,285 | `5e5e050cb194fe05d76e531567bd9a5ee2122502ae65f3ae87f158c98e6e5767` |
| MYP4 | `MYP_Mathematics_4_Student_Coursebook.pdf` | 458 | 11,462,227 | `4e0e8a32776f43f8565966edb54f9f30c6f45e7858259bd9799931e89197c393` |
| MYP5 | `MYP_Mathematics_5_Student_Coursebook.pdf` | 340 | 11,276,894 | `5f2e8001623ce1e26c72a94755127ee0828c4b0756fcc6c5bc0604e223d3274f` |

Total: 1,572 pages. Machine-readable details are in `evidence/repository-manifest.json`.

## 2. Editable sources versus exports

The PDFs are exports, not safe editable sources. The repository and its history contain no HTML/CSS, Markdown/LaTeX manuscript, diagram source, build script, package lockfile, font file, or standalone curriculum-planning file. The books’ credits describe an HTML/CSS paged-media workflow for MYP1–3 and a Chrome/Skia PDF workflow for MYP4–5, but the source files needed to reproduce those PDFs are absent.

Technical inspection found:

- Page size approximately A4: `594.96 × 841.92 pt`.
- MYP1–3: PDF 1.7; creator/producer indicate HTML/CSS, Chrome DevTools Protocol and pdf-lib.
- MYP4–5: PDF 1.4; HeadlessChrome 157 / Skia PDF m157.
- No encryption, bookmarks, embedded files, or raster image XObjects.
- Fonts are embedded. MYP1–3 include Type3 font material; MYP4–5 use embedded Type0 fonts. Font embedding is not a confirmed defect.
- Diagrams are vector drawing operations in the PDF, but their editable sources are missing.

## 3. Confirmed production defects and limits

These are first-edition findings, not changes made by the audit:

| Finding | Source anchor | Status |
|---|---|---|
| Right-edge clipping of Figure 7.6 caption | MYP2 physical p.136 | Confirmed by render |
| Right-edge clipping of answer equations/cost text | MYP2 physical p.242 | Confirmed by render |
| Blank/off-white pages | MYP4 physical pp.181, 203, 231, 291, 325, 373; MYP5 physical pp.55, 101, 121, 163, 185, 207, 229, 257, 331 | Confirmed by contact-sheet renders |
| Visible raw LaTeX commands | MYP5 physical p.235 / printed p.222; physical p.328 / printed p.315 | Confirmed by text/render |
| Answer-key errata acknowledge student-prompt defects | MYP5 physical pp.321–324 | Confirmed; student prompts still need repair |

Selected renders are preserved in `evidence/renders/`. They are evidence, not replacement pages.

## 4. Missing-material inventory

Required before a safe second-edition production workflow:

1. Editable manuscript sources for all five levels.
2. Editable diagram sources and data files.
3. Build scripts, dependency lockfiles, font files and licence texts.
4. Official school unit planners, scope-and-sequence, assessment policy and ATL map.
5. Standard/extended pathway decision for MYP4–5.
6. Answer-key source, errata log and independent solution-check record.
7. Print/export QA reports: trim/bleed, margins, font embedding, colour, links, bookmarks, accessibility and file naming.
8. Permission/licence record for any third-party data, images or adapted material.

If these cannot be recovered, the second edition must be rebuilt as a new editable source project that uses the PDFs as reference, not as a lossy PDF-to-text conversion.

## 5. Preservation rule

Keep the five root PDFs untouched as the first-edition archive. Put second-edition work under `second-edition/`, with separate `sources/`, `exports/`, and `qa/` directories once production is approved. Do not overwrite a first-edition PDF to “fix” a page. Record errata separately and generate new, predictably named second-edition exports.
