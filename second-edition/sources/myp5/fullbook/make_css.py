#!/usr/bin/env python3
"""Generate book.css for the assembled coursebook.

The file is the approved Chapter 7 prototype design system (page model, palette,
typography, running heads, answer blocks) followed by the legacy chapter
component styles and the book-level additions used by front matter, contents,
criterion practice, project pages, formula bank, glossary and references.
"""
import re, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent                      # sources/myp5
EDITION = HERE.parents[2]              # second-edition
PROTO = EDITION / "prototype/myp1/ch07/styles.css"
LEGACY = ROOT / "styles/book.css"

proto = PROTO.read_text(encoding="utf-8")
proto = proto.replace("MYP MATHEMATICS 1 · STUDENT COURSEBOOK",
                      "MYP MATHEMATICS 5 · STUDENT COURSEBOOK")
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
.investigate .construction-space{height:58mm}
.page .investigate figure svg{max-height:78mm;width:auto;max-width:100%}
.page .investigate .table-wrap{max-height:78mm;overflow:hidden}

/* --- assessment footer notes belong inside their task box --- */
.assessment-task .footer-note{position:static; margin:2.5mm 0 0; padding-top:2mm;
  border-top:1px solid var(--line); font-family:var(--label); font-size:7pt; color:#7a8784}


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
.page figure svg{max-height:105mm;width:auto;max-width:100%}
.page .example .visual svg{max-height:105mm;width:auto;max-width:100%}
.page figure figcaption{text-align:center}
.page figure{margin:3mm 0}
.katex{font-size:.99em}
.exercise-block{margin:3mm 0}

/* --- compact answers --- */
.answer-section .answer-item{padding:1mm 0;font-size:8.8pt;line-height:1.3}

/* ======================= MYP 5 opener-only tightening ======================= */
/* The MYP 5 openers carry longer standfirst, engage, inquiry, ATL and question
   text than MYP 3 or MYP 4.  Nothing here touches the cover copy: the openers
   are tightened so the chapter covers fit one page again. */
.opener{padding-top:5mm}
.chapter-number{font-size:46pt;line-height:1}
.opener h1{font-size:28pt;line-height:1.06;margin:1mm 0 2mm}
.opener .standfirst{font-size:12.5pt;line-height:1.34;margin:1.5mm 0 2.5mm}
.opener .callout{padding:2.6mm 3.4mm;margin:2.2mm 0;font-size:9.6pt;line-height:1.34}
.opener .callout .label{font-size:7pt;margin-bottom:1mm}
.opener .card{padding:2.4mm 3mm;margin:2.2mm 0}
.opener .card h3{font-size:10pt;margin-bottom:1mm}
.opener .atl{padding:2.2mm 3mm;margin:2mm 0;font-size:8.8pt;line-height:1.3}
.opener li{margin-bottom:.8mm;line-height:1.3}
.opener .opener-meta{font-size:8pt;margin-top:2mm}

/* --- references: tightened after the original prototype rules --- */
.references h3{font-family:Inter,sans-serif;font-size:8.6pt;text-transform:uppercase;letter-spacing:.07em;color:var(--green);margin:3.4mm 0 1.4mm}
.references ul{padding-left:4mm;margin:0}
.references li{margin-bottom:1.4mm;font-size:8.8pt;line-height:1.3}
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

/* --- author credit on the imprint (title) page --- */
.credit{display:flex;align-items:baseline;gap:4mm;margin:0 0 6mm;padding-bottom:4mm;border-bottom:.3mm solid var(--gold)}
.credit-label{font-family:Inter,sans-serif;font-size:7.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--rust)}
.credit-name{font-family:Fraunces,serif;font-weight:600;font-size:17pt;letter-spacing:.06em;color:var(--green)}

/* ==================== premium exterior covers ==================== */
.premium-cover,.back-cover-page{display:block;padding:0;background:#0d2a28;color:var(--cream)}
.premium-cover::before,.premium-cover::after,.back-cover-page::before,.back-cover-page::after{display:none}
.pc-bg{position:absolute;inset:0;
  background:
    radial-gradient(115% 78% at 86% 4%, rgba(215,165,93,.15), rgba(215,165,93,0) 58%),
    radial-gradient(95% 65% at 6% 98%, rgba(178,79,50,.11), rgba(178,79,50,0) 62%),
    linear-gradient(180deg,#10332f 0%,#0d2a28 46%,#09201e 100%)}
.pc-grid{position:absolute;inset:0;
  background-image:linear-gradient(rgba(215,165,93,.075) .25mm,transparent .25mm),
                   linear-gradient(90deg,rgba(215,165,93,.075) .25mm,transparent .25mm);
  background-size:7mm 7mm;
  -webkit-mask-image:linear-gradient(212deg,rgba(0,0,0,.95) 14%,rgba(0,0,0,0) 66%);
  mask-image:linear-gradient(212deg,rgba(0,0,0,.95) 14%,rgba(0,0,0,0) 66%)}

/* shared bands */
.pc-top{position:absolute;top:15mm;left:18mm;right:18mm;display:flex;justify-content:space-between;
  align-items:baseline;font-family:Inter,sans-serif;font-size:7.4pt;letter-spacing:.15em;
  text-transform:uppercase;color:var(--gold);border-bottom:.3mm solid rgba(215,165,93,.34);
  padding-bottom:3mm;z-index:2}
.pc-top .r{color:rgba(215,165,93,.75)}
.pc-foot{position:absolute;left:18mm;right:18mm;bottom:14mm;display:flex;justify-content:space-between;
  align-items:baseline;font-family:Inter,sans-serif;font-size:7pt;letter-spacing:.13em;
  text-transform:uppercase;color:rgba(251,246,236,.6);border-top:.3mm solid rgba(215,165,93,.34);
  padding-top:4mm;z-index:2}
.pc-foot .pc-author{font-size:9.2pt;letter-spacing:.15em;color:var(--cream)}

/* front cover */
.pc-body{position:absolute;left:18mm;top:47mm;width:84mm;z-index:2}
.pc-eyebrow{font-family:Inter,sans-serif;font-size:10pt;letter-spacing:.44em;text-transform:uppercase;
  color:var(--gold);margin-bottom:4.5mm}
.premium-cover .pc-title{font-family:Fraunces,serif;font-weight:600;font-size:30pt;line-height:1;letter-spacing:.004em;
  color:var(--cream);margin:0}
.pc-level{display:flex;align-items:flex-end;gap:5mm;margin:6mm 0 0}
.pc-numeral{font-family:Fraunces,serif;font-weight:600;font-size:52pt;line-height:.8;color:var(--gold)}
.pc-leveltext{display:flex;flex-direction:column;gap:1.4mm;padding-bottom:1.5mm}
.pc-levelname{font-family:Inter,sans-serif;font-size:10pt;letter-spacing:.15em;text-transform:uppercase;
  color:var(--cream)}
.pc-levelnote{font-family:Inter,sans-serif;font-size:7pt;letter-spacing:.13em;text-transform:uppercase;
  color:rgba(251,246,236,.55)}
.premium-cover .pc-standfirst{font-family:'Source Serif 4',serif;font-style:italic;font-size:11pt;line-height:1.5;
  color:rgba(251,246,236,.86);margin:8mm 0 0;max-width:80mm}
.pc-rule{width:26mm;border-top:.6mm solid var(--gold);margin:7mm 0 5mm}
.pc-topics{font-family:Inter,sans-serif;font-size:7.2pt;line-height:1.85;letter-spacing:.05em;
  text-transform:uppercase;color:rgba(251,246,236,.5)}
.pc-topics .t{white-space:nowrap}
.pc-topics .t::after{content:' ·';color:rgba(215,165,93,.75)}
.pc-topics .t:last-child::after{content:''}
.pc-inquiry{margin-top:8mm;border-left:.6mm solid var(--rust);padding-left:4.5mm;max-width:80mm}
.pc-inquirylabel{font-family:Inter,sans-serif;font-size:7pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);margin-bottom:1.6mm}
.pc-inquiry p{font-family:'Source Serif 4',serif;font-size:9.6pt;line-height:1.45;margin:0;
  color:rgba(251,246,236,.82)}
.pc-criteria{margin-top:9mm;max-width:80mm}
.pc-criteriahead{font-family:Inter,sans-serif;font-size:6.6pt;letter-spacing:.2em;text-transform:uppercase;
  color:rgba(215,165,93,.85);margin-bottom:2.6mm}
.pc-criteriagrid{display:grid;grid-template-columns:auto 1fr;gap:1.5mm 4mm;align-items:baseline}
.pc-criteria .k{font-family:Inter,sans-serif;font-size:6.4pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold)}
.pc-criteria .v{font-family:'Source Serif 4',serif;font-size:8.4pt;line-height:1.25;
  color:rgba(251,246,236,.72)}
.pc-art{position:absolute;left:104mm;top:32mm;width:92mm;height:214mm;z-index:1}
.pc-art .plate{width:100%;height:100%}

/* back cover */
.pc-bbody{position:absolute;left:18mm;top:42mm;width:118mm;z-index:2}
.pc-bheading{font-family:Inter,sans-serif;font-size:8pt;letter-spacing:.15em;text-transform:uppercase;
  color:var(--gold);margin-bottom:5mm}
.pc-btext p{font-family:'Source Serif 4',serif;font-size:10.4pt;line-height:1.55;margin:0 0 4.5mm;
  color:rgba(251,246,236,.88)}
.pc-becho{position:absolute;left:126mm;top:8mm;width:66mm;height:141mm;opacity:.2;z-index:1}
.pc-becho .plate{width:100%;height:100%}
.pc-collection{position:absolute;left:18mm;right:18mm;top:166mm;z-index:2}
.pc-collectionhead{font-family:Inter,sans-serif;font-size:8pt;letter-spacing:.15em;
  text-transform:uppercase;color:var(--gold);margin-bottom:5mm;
  border-bottom:.3mm solid rgba(215,165,93,.3);padding-bottom:3mm}
.pc-strip{display:flex;gap:4.6mm}
.pc-vol{width:30mm}
.mini{width:30mm;height:45mm;background:#0d2a28;border:.25mm solid rgba(215,165,93,.3);
  display:flex;flex-direction:column;justify-content:space-between;padding:2.4mm 2.2mm;
  box-sizing:border-box}
.mini.now{border:.55mm solid var(--gold)}
.mini .m-top{font-family:Inter,sans-serif;font-size:3.6pt;letter-spacing:.3em;color:var(--gold)}
.mini .m-art{height:17mm}
.mini .m-art svg{width:100%;height:100%}
.mini .m-foot{text-align:center}
.mini .m-num{font-family:Fraunces,serif;font-weight:600;font-size:17pt;line-height:.9;color:var(--gold)}
.mini .m-lab{font-family:Inter,sans-serif;font-size:3.2pt;letter-spacing:.22em;text-transform:uppercase;
  color:rgba(251,246,236,.75);margin-top:.6mm}
.pc-cap{font-family:Inter,sans-serif;font-size:5.4pt;letter-spacing:.09em;text-transform:uppercase;
  color:rgba(251,246,236,.55);text-align:center;margin-top:1.8mm;line-height:1.35}
.pc-cap.now{color:var(--gold)}
.pc-collectionnote{font-family:'Source Serif 4',serif;font-size:8.4pt;line-height:1.45;
  color:rgba(251,246,236,.6);margin:5mm 0 0;max-width:158mm}
.pc-smallprint{position:absolute;left:18mm;right:18mm;bottom:31mm;font-family:Inter,sans-serif;
  font-size:6.2pt;letter-spacing:.05em;line-height:1.5;color:rgba(251,246,236,.42);z-index:2}

/* collection cover concepts (MYP 1-4, not yet produced) */
.pc-concept{font-family:Inter,sans-serif;font-size:7.6pt;letter-spacing:.14em;text-transform:uppercase;
  color:rgba(215,165,93,.8);border:.3mm solid rgba(215,165,93,.4);padding:3mm 4mm;max-width:80mm;
  line-height:1.6}
"""

out = "\n\n".join([
    "/* MYP 5 Student Coursebook (second edition) - assembled book stylesheet.",
    "   Base: approved Chapter 7 prototype design system, then legacy chapter",
    "   component styles, then book-level additions. */",
    proto.strip(),
    "\n/* ==================== legacy chapter component styles ==================== */",
    legacy,
    ADDITIONS.strip(),
]) + "\n"
(HERE / "book.css").write_text(out, encoding="utf-8")
print("book.css written:", len(out.splitlines()), "lines")
