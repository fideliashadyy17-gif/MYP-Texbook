#!/usr/bin/env python3
"""Generate book.css for the assembled coursebook.

The file is the approved Chapter 7 prototype design system (page model, palette,
typography, running heads, answer blocks) followed by the legacy chapter
component styles and the book-level additions used by front matter, contents,
criterion practice, project pages, formula bank, glossary and references.
"""
import re, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent                      # sources/myp1
EDITION = HERE.parents[2]              # second-edition
PROTO = EDITION / "prototype/myp1/ch07/styles.css"
LEGACY = ROOT / "styles/book.css"

proto = PROTO.read_text(encoding="utf-8")
legacy = LEGACY.read_text(encoding="utf-8")

# --- legacy stylesheet: drop @import, named pages and the Paged.js page box ---
legacy = re.sub(r"@import[^;]+;\s*", "", legacy)
legacy = re.sub(r"@page[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}\s*", "", legacy)
legacy = legacy.replace(
    ".page{break-after:page; height:261mm; position:relative;}", "")
legacy = legacy.replace(".page:last-child{break-after:auto;}", "")
legacy = legacy.replace(".opener{page:opener; padding-top:8mm;}", ".opener{padding-top:6mm;}")
legacy = legacy.replace(
    ".cover.page{page:cover; background:var(--green); color:var(--cream); margin:0; width:210mm; height:297mm; padding:22mm 20mm; display:flex; flex-direction:column; justify-content:space-between; break-inside:avoid;}",
    ".cover.page{background:var(--green); color:var(--cream); display:flex; flex-direction:column; justify-content:space-between; break-inside:avoid;}")
legacy = re.sub(r"\n{3,}", "\n\n", legacy).strip()

ADDITIONS = """
/* ============================ book-level additions ============================ */

/* --- contents --- */
.toc{margin-top:2mm}
.toc .part-head{font-family:Inter,sans-serif;font-size:8pt;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--green);margin:5mm 0 1mm;border-bottom:1.5px solid var(--gold);padding-bottom:1mm}
.toc ol{list-style:none;padding:0;margin:0}
.toc li{display:flex;align-items:baseline;gap:2mm;padding:1.05mm 0;border-bottom:1px dotted var(--line)}
.toc li .num{font-family:Inter,sans-serif;font-size:8pt;font-weight:600;color:var(--rust);width:9mm}
.toc li .t{flex:1}
.toc li .dots{flex:0 0 12mm;border-bottom:1px dotted var(--line);margin-bottom:1mm}
.toc li .p{font-family:Inter,sans-serif;font-size:8.5pt;color:var(--ink)}
.toc li.sub{padding-left:9mm;font-size:9.5pt;color:#3d4a47}

/* --- criterion banners --- */
.criterion-banner{display:flex;gap:3mm;align-items:baseline;border:1px solid var(--line);border-left:4px solid var(--gold);background:#fffdf8;padding:2.5mm 4mm;margin:0 0 4mm}
.criterion-banner .k{font-family:Inter,sans-serif;font-size:8pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--rust)}
.criterion-banner .v{font-family:Inter,sans-serif;font-size:8pt;color:var(--muted)}
.criterion-banner.a{border-left-color:var(--green)}
.criterion-banner.a .k{color:var(--green)}
.criterion-banner.b{border-left-color:var(--rust)}
.criterion-banner.c{border-left-color:#4d7a72}
.criterion-banner.c .k{color:#3f6a62}
.criterion-banner.d{border-left-color:var(--gold)}

/* --- investigation pages --- */
.investigate .task{border:1px solid var(--line);border-top:3px solid var(--gold);background:#fffdf8;padding:4mm 5mm;margin:4mm 0}
.investigate .task .label{font-family:Inter,sans-serif;font-size:7.5pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--rust);margin-bottom:1.5mm}
.investigate .prompts{margin:3mm 0 0;padding-left:5mm}
.investigate .prompts li{margin-bottom:1.5mm}
.investigate .discovery{border-left:3px solid #4d7a72;background:var(--pale);padding:3mm 4mm;margin:4mm 0;font-size:9.5pt}
.investigate .conclusion{border:1.5px solid var(--green);border-radius:2mm;padding:3.5mm 4mm;margin:4mm 0;background:#fffdf8}
.investigate .conclusion .label{font-family:Inter,sans-serif;font-size:7.5pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--green);margin-bottom:1.5mm}

/* --- project connections --- */
.project-card{border:1px solid var(--line);border-radius:2mm;padding:2.8mm 3.5mm;margin:2.8mm 0;background:#fffdf8;break-inside:avoid}
.project-card h3{margin-top:0;font-size:11.5pt}
.project-card dl{display:grid;grid-template-columns:31mm 1fr;gap:.9mm 2.5mm;margin:1.5mm 0 0;font-size:8.6pt;line-height:1.32}
.project-card dt{font-family:Inter,sans-serif;font-size:7.5pt;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--rust);padding-top:.6mm}
.project-card dd{margin:0}
.project-note{font-size:8.5pt;color:var(--muted);margin-top:3mm}

/* --- formula bank and glossary --- */
.formula-bank .fb-group{margin:4mm 0;break-inside:avoid}
.formula-bank .fb-group h3{font-family:Inter,sans-serif;font-size:9pt;text-transform:uppercase;letter-spacing:.08em;color:var(--green);border-bottom:1px solid var(--line);padding-bottom:1.5mm;margin-bottom:2mm}
.formula-bank dl{margin:0}
.formula-bank dt{font-family:Inter,sans-serif;font-size:8pt;font-weight:600;color:var(--rust);margin-top:2mm}
.formula-bank dd{margin:.5mm 0 0 0;font-size:10pt;color:var(--ink)}
.glossary{columns:2;column-gap:9mm;font-size:9.5pt}
.glossary dl{margin:0}
.glossary dt{font-family:Inter,sans-serif;font-size:8.5pt;font-weight:600;color:var(--green);break-after:avoid;margin-top:2mm}
.glossary dd{margin:.5mm 0 2mm 0;break-inside:avoid}
.glossary .ch{font-family:Inter,sans-serif;font-size:7pt;color:var(--muted)}

/* --- references --- */
.references h3{font-family:Inter,sans-serif;font-size:9pt;text-transform:uppercase;letter-spacing:.08em;color:var(--green);margin:5mm 0 2mm}
.references ul{padding-left:5mm}
.references li{margin-bottom:2.5mm;font-size:9.5pt}
.references .url{font-family:Inter,sans-serif;font-size:8pt;color:#4d7a72;word-break:break-all}

/* --- book page geometry and figure rhythm --- */
.page{padding:16mm 16mm 17mm}
.page figure img{width:100%;height:auto;max-height:56mm;object-fit:contain;display:block;margin:0 auto}
.page figure figcaption{text-align:center}
.page figure{margin:3mm 0}
.katex{font-size:.99em}
.exercise-block{margin:3mm 0}

/* --- compact answers --- */
.answer-section .answer-item{padding:1mm 0;font-size:8.8pt;line-height:1.3}
.answer-section .answer-item .reasoning{font-size:8.2pt}
.answer-section h2{font-size:15pt;margin-bottom:2.5mm}
.answer-section .answer-group-title{font-family:Inter,sans-serif;font-size:7.5pt;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--green);margin:2.4mm 0 1mm;border-bottom:1px solid var(--line);padding-bottom:.8mm}
.answer-section .answer-group-title:first-child{margin-top:0}

/* --- chapter 7 cover fit --- */
.page[data-page-id="cover"] .inquiry{margin-top:6mm}
.page[data-page-id="cover"] .figure{margin:3mm 0}

/* --- front matter --- */
.imprint p{margin-bottom:4mm}
.steps{counter-reset:step;list-style:none;padding-left:0;margin:3mm 0}
.steps li{counter-increment:step;position:relative;padding-left:9mm;margin-bottom:2.5mm}
.steps li::before{content:counter(step);position:absolute;left:0;top:.3mm;width:5.5mm;height:5.5mm;border-radius:50%;background:var(--green);color:var(--cream);font-family:Inter,sans-serif;font-size:7.5pt;display:flex;align-items:center;justify-content:center}
.steps li strong{color:var(--green)}
.checklist{list-style:none;padding:0}
.checklist li{padding-left:6.5mm;position:relative;margin-bottom:2mm}
.checklist li::before{content:'';position:absolute;left:0;top:1.1mm;width:3mm;height:3mm;border:.35mm solid var(--rust);border-radius:.5mm}
.book-cover .chips{display:flex;gap:3mm;flex-wrap:wrap;margin-top:8mm}
"""

out = "\n\n".join([
    "/* MYP 1 Student Coursebook (second edition) - assembled book stylesheet.",
    "   Base: approved Chapter 7 prototype design system, then legacy chapter",
    "   component styles, then book-level additions. */",
    proto.strip(),
    "\n/* ==================== legacy chapter component styles ==================== */",
    legacy,
    ADDITIONS.strip(),
]) + "\n"
(HERE / "book.css").write_text(out, encoding="utf-8")
print("book.css written:", len(out.splitlines()), "lines")
