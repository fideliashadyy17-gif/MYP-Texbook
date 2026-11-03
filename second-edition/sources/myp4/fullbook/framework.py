#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Authored editorial framework for the MYP 4 second-edition coursebook.

Content reference: the pre-rewrite MYP 4 chapter and subtopic audit
(``second-edition/audit/chapter-audits/myp4-audit.md`` and the chapter and
subtopic registers). Chapter scope and teaching order follow that audit; the
teaching sequence, investigations, worked examples, practice sets, assessment
tasks and project connections are author-designed material written for this
second edition.

Every chapter is built as a complete MYP unit from the start: an official global
context with its official exploration, a statement of inquiry that names the key
concept and the related concepts, three question categories derived from the
same elements, an inquiry question opening every investigation, and Criterion
A-D practice written to exercise that unit rather than to repeat a drill.

Year 4 is the bridge level. The register records thirteen numbered chapters and
a capstone, and the front-map concept and context labels of the earlier edition
disagree with its openers in several chapters; the labels used here are the
opener labels, which are the ones the teaching actually develops, and every
mismatch is recorded in ``second-edition/correction-review/myp4-unit-alignment.md``.
"""
import diagrams2

LEVEL = 4
AUTHOR = "SADIKOU MOUKODDIM"

SERIES = dict(
    name="MYP Mathematics",
    line="MYP Mathematics · Student coursebook",
    edition="Second edition",
)

# Five-volume collection. MYP 1 and MYP 2 are produced; MYP 3 is produced; MYP 4
# is the volume in hand; MYP 5 does not exist yet and is shown as a coordinated
# cover concept only.
COLLECTION = [
    dict(level=1, status="published", theme="Year 1 · number, algebra, shape and data"),
    dict(level=2, status="published", theme="Year 2 · ratio, algebra, geometry, probability"),
    dict(level=3, status="published", theme="Year 3 · proof, models and evidence"),
    dict(level=4, status="this volume", theme="Year 4 · models, proof and application"),
    dict(level=5, status="forthcoming", theme="Year 5 · modelling, proof, transition"),
]

PARTS = {
    1: "Part I · Number and abstract reasoning",
    2: "Part I · Number and abstract reasoning",
    3: "Part II · Thinking with models",
    4: "Part II · Thinking with models",
    5: "Part II · Thinking with models",
    6: "Part II · Thinking with models",
    7: "Part II · Thinking with models",
    8: "Part II · Thinking with models",
    9: "Part III · Spatial reasoning",
    10: "Part III · Spatial reasoning",
    11: "Part III · Spatial reasoning",
    12: "Part IV · Reasoning with data",
    13: "Part IV · Reasoning with data",
    14: "Part V · Integrated modelling",
}

CRITERIA = {
    "A": ("Knowing and understanding", "a"),
    "B": ("Investigating patterns", "b"),
    "C": ("Communicating", "c"),
    "D": ("Applying mathematics in real-life contexts", "d"),
}

# ------------------------------------------------------------------ formula bank
FORMULAS = [
    ("Number, accuracy and form", [
        ("Index laws", "aᵐ × aⁿ = aᵐ⁺ⁿ; aᵐ ÷ aⁿ = aᵐ⁻ⁿ; (aᵐ)ⁿ = aᵐⁿ, for a ≠ 0."),
        ("Zero and negative indices", "a⁰ = 1 for a ≠ 0; a⁻ⁿ = 1/aⁿ."),
        ("Rational index", "a^(1/n) is the nth root of a; a^(m/n) = (ⁿ√a)ᵐ."),
        ("Standard form", "a × 10ⁿ with 1 ≤ a < 10."),
        ("Surd rules", "√a × √b = √(ab); √a ÷ √b = √(a/b); (√a)² = a."),
        ("Rationalising", "multiply by the conjugate so that the denominator becomes rational."),
        ("Error interval", "a value given to the nearest unit lies within half a unit either side."),
        ("Bounds of a calculation", "the lower bound uses the lower bounds of subtracted terms."),
        ("Percentage multiplier", "an increase of r% multiplies by 1 + r/100; a decrease by 1 − r/100."),
    ]),
    ("Algebra and equations", [
        ("Expanding", "a(b + c) = ab + ac."),
        ("Difference of squares", "a² − b² = (a − b)(a + b)."),
        ("Perfect square", "a² + 2ab + b² = (a + b)²; a² − 2ab + b² = (a − b)²."),
        ("Quadratic equation", "ax² + bx + c = 0 with a ≠ 0."),
        ("Quadratic formula", "x = (−b ± √(b² − 4ac)) ÷ 2a."),
        ("Discriminant", "b² − 4ac > 0 gives two real roots, = 0 one repeated root, < 0 none."),
        ("Completing the square", "ax² + bx + c = a(x + b/2a)² + c − b²/4a."),
        ("Algebraic fraction", "cancel only common factors, and state the excluded values first."),
        ("Inequality rule", "multiplying or dividing by a negative number reverses the sign."),
        ("Function", "a rule giving exactly one output for each input of its domain."),
    ]),
    ("Functions, graphs and sequences", [
        ("Straight line", "y = mx + c, with gradient m and y-intercept c."),
        ("Gradient", "m = (y₂ − y₁) ÷ (x₂ − x₁)."),
        ("Parallel and perpendicular", "parallel lines share a gradient; perpendicular gradients multiply to −1."),
        ("Distance and midpoint", "d = √((x₂ − x₁)² + (y₂ − y₁)²); midpoint = ((x₁ + x₂)/2, (y₁ + y₂)/2)."),
        ("Parabola", "y = ax² + bx + c; vertex form y = a(x − h)² + k has vertex (h, k)."),
        ("Axis of symmetry", "x = −b ÷ 2a."),
        ("nth term, linear", "a constant first difference gives term = mn + c."),
        ("nth term, quadratic", "a constant second difference 2d gives term = dn² + en + f."),
        ("Recursive rule", "each term is defined from the one before it; an initial value is required."),
        ("Compound change", "final = initial × multiplierⁿ."),
        ("Direct variation", "y = kxⁿ; inverse variation y = k/xⁿ."),
    ]),
    ("Shape, space and measurement", [
        ("Congruence", "SSS, SAS, ASA, RHS for triangles."),
        ("Similarity", "corresponding angles equal and corresponding sides in one ratio k."),
        ("Scale laws", "lengths scale by k, areas by k² and volumes by k³."),
        ("Pythagoras", "a² + b² = c² for the hypotenuse c of a right-angled triangle."),
        ("Trigonometric ratios", "sin θ = opposite/hypotenuse; cos θ = adjacent/hypotenuse; tan θ = opposite/adjacent."),
        ("Angles of elevation and depression", "measured from the horizontal, and equal by alternate angles."),
        ("Sine rule", "a/sin A = b/sin B = c/sin C."),
        ("Cosine rule", "a² = b² + c² − 2bc cos A."),
        ("Area of a triangle", "½ab sin C."),
        ("Prism", "volume = area of cross-section × length."),
        ("Cylinder", "volume = πr²h; curved surface area = 2πrh."),
        ("Cone", "volume = ⅓πr²h; curved surface area = πrl for slant height l."),
        ("Sphere", "volume = ⁴⁄₃πr³; surface area = 4πr²."),
        ("Frustum", "a cone or pyramid with the top cut off parallel to the base."),
        ("Density", "density = mass ÷ volume."),
    ]),
    ("Data, probability and evidence", [
        ("Frequency density", "frequency ÷ class width; it is the height of a histogram bar."),
        ("Cumulative frequency", "the running total of frequencies up to the upper class boundary."),
        ("Median and quartiles", "the median halves the data; the quartiles quarter it."),
        ("Interquartile range", "Q3 − Q1, a measure of spread that ignores the extremes."),
        ("Box plot", "minimum, Q1, median, Q3, maximum on one axis."),
        ("Sample and population", "a sample estimates a population parameter; bias makes it unreliable."),
        ("Stratified sampling", "sample each group in proportion to its size in the population."),
        ("Probability of an event", "P(event) = favourable outcomes ÷ total equally likely outcomes."),
        ("Addition rule", "P(A or B) = P(A) + P(B) − P(A and B)."),
        ("Multiplication rule", "P(A and B) = P(A) × P(B) for independent events."),
        ("Conditional probability", "P(A given B) = P(A and B) ÷ P(B)."),
        ("Expected frequency", "expected count = probability × number of trials."),
    ]),
]

# ---------------------------------------------------------------------- glossary
GLOSSARY = [
    ("Algebraic fraction", "A fraction whose numerator and denominator are algebraic expressions.", 2),
    ("Bounds", "The greatest and least values a rounded quantity could have had.", 1),
    ("Box plot", "A display of the minimum, lower quartile, median, upper quartile and maximum.", 12),
    ("Class width", "The difference between the upper and lower boundaries of a class interval.", 12),
    ("Common factor", "A factor shared by every term of an expression.", 2),
    ("Completing the square", "Rewriting a quadratic as a(x + p)² + q so that its vertex is visible.", 5),
    ("Compound interest", "Interest earned on interest, modelled by repeated multiplication.", 8),
    ("Conditional probability", "The probability of an event given that another event has occurred.", 13),
    ("Congruent", "Identical in shape and size; for triangles, SSS, SAS, ASA or RHS proves it.", 9),
    ("Conjecture", "A mathematical claim believed to be true but not yet justified.", 7),
    ("Conjugate", "The pair a + √b and a − √b, whose product is rational.", 1),
    ("Correlation", "The strength and direction of a linear association between two variables.", 12),
    ("Cumulative frequency", "The running total of frequencies up to a class boundary.", 12),
    ("Dependent events", "Events where the outcome of one changes the probability of the other.", 13),
    ("Depreciation", "A loss of value, modelled by repeated multiplication by a factor below 1.", 8),
    ("Discriminant", "b² − 4ac, which decides how many real roots a quadratic has.", 5),
    ("Domain", "The set of permitted inputs of a function.", 4),
    ("Enlargement", "A transformation that multiplies every distance from a centre by one factor.", 9),
    ("Error interval", "The interval of values that would round to a stated value.", 1),
    ("Expected frequency", "How often an event is expected to occur in a given number of trials.", 13),
    ("Factorise", "Rewrite an expression as a product of simpler expressions.", 2),
    ("Frequency density", "Frequency divided by class width, used as the height of a histogram bar.", 12),
    ("Function", "A rule that gives exactly one output for each permitted input.", 4),
    ("Gradient", "The change in y per unit change in x; the steepness of a line.", 4),
    ("Histogram", "A display of grouped continuous data in which area represents frequency.", 12),
    ("Independent events", "Events where neither changes the probability of the other.", 13),
    ("Index", "The power to which a base is raised; plural indices.", 1),
    ("Interquartile range", "The difference between the upper and lower quartiles.", 12),
    ("Intersection", "The set of outcomes in both of two sets; for events, A and B.", 13),
    ("Inverse variation", "A relationship y = k/xⁿ in which one variable falls as the other rises.", 8),
    ("Lower quartile", "The value below which a quarter of the data lies.", 12),
    ("Midpoint", "The point halfway between two points, found by averaging each coordinate.", 4),
    ("Model", "A mathematical description of a situation, built on stated assumptions.", 8),
    ("Multiplier", "The single factor by which a quantity is repeatedly multiplied.", 8),
    ("Mutually exclusive", "Events that cannot both happen, so P(A or B) = P(A) + P(B).", 13),
    ("Outlier", "A value that lies well away from the rest of the data.", 12),
    ("Parabola", "The graph of a quadratic function, symmetric about a vertical axis.", 6),
    ("Perpendicular", "At right angles; two lines are perpendicular when their gradients multiply to −1.", 4),
    ("Population", "The whole group a claim is about.", 12),
    ("Quadratic", "An expression of degree two, containing a term in x² and no higher power.", 5),
    ("Range (of a function)", "The set of outputs a function can produce.", 4),
    ("Recursive rule", "A rule that gives each term of a sequence from the term before it.", 7),
    ("Sample space", "The set of all possible outcomes of an experiment.", 13),
    ("Similar", "Same shape, possibly different size: corresponding angles equal, sides in ratio.", 9),
    ("Standard form", "A number written as a × 10ⁿ with 1 ≤ a < 10.", 1),
    ("Stratified sample", "A sample that takes each group in proportion to its share of the population.", 12),
    ("Surd", "An exact irrational root left in root form, such as √2 or 3√5.", 1),
    ("Transformation", "A rule that moves or changes a shape: translation, reflection, rotation, enlargement.", 9),
    ("Union", "The set of outcomes in either of two sets; for events, A or B.", 13),
    ("Upper quartile", "The value below which three quarters of the data lies.", 12),
    ("Vertex", "The turning point of a parabola, written (h, k) in vertex form.", 6),
    ("y-intercept", "The value of y where a line crosses the y-axis.", 4),
]

REFERENCES = [
    ("Official IB sources", [
        "IB Middle Years Programme curriculum — https://www.ibo.org/programmes/middle-years-programme/curriculum/ (page states last updated 19 February 2026). Used for: at least 50 hours per subject per year, global contexts, conceptual understanding, approaches to learning and service as action.",
        "IB MYP mathematics subject page — https://www.ibo.org/programmes/middle-years-programme/curriculum/mathematics/ Used for: the four branches of MYP mathematics, standard and extended mathematics, and the inquiry and application focus.",
        "IB MYP projects — https://www.ibo.org/programmes/middle-years-programme/curriculum/myp-projects/ (page states last updated 19 February 2026). Used for: the Community Project completed by students finishing MYP in Year 3 or Year 4, the Personal Project completed by Year 5 students, and the student-centred nature of both.",
        "IB MYP general regulations (2026 assessment procedures) — https://www.ibo.org/globalassets/new-structure/become-an-ib-school/pdfs/myp-2026-general-regulations.pdf Used for: the required use of MYP objectives and assessment criteria, minimum teaching hours, and Year 5 eAssessment eligibility.",
    ]),
    ("Principal content reference", [
        "Pre-rewrite MYP 4 chapter and subtopic audit (second-edition/audit/chapter-audits/myp4-audit.md with the chapter and subtopic registers). Used as the principal content reference for chapter scope, teaching order and the key concepts, related concepts, global contexts and inquiry questions of each chapter. The audit records that the earlier edition's course map and its chapter openers disagreed on the key concept and global context in eight chapters; the opener labels are used here, and each reconciliation is listed in the alignment review.",
    ]),
    ("Author-designed material", [
        "The chapter sequence, investigations, worked examples, practice sets, assessment tasks, project connections, formula bank, glossary and this edition's editorial framework are author-designed material written to serve the programme requirements above. They are not IB publications and carry no IB endorsement.",
        "All classroom data sets are simulated and are labelled in the text. No claim in this book relies on unverified real-world data.",
    ]),
]


# ------------------------------------------------------------------- front matter
FRONT = dict(
    cover=dict(
        kicker="MYP Mathematics · Student coursebook",
        edition="Second edition",
        title="Mathematics",
        level="4",
        level_text="Student coursebook",
        level_note="MYP 4 · Year 4 · thirteen chapters and a capstone in four parts",
        standfirst="A concept-driven inquiry course in number, algebra, functions, shape and "
                   "space, statistics and probability. You model, justify and apply, then "
                   "reason, communicate and evaluate.",
        topics=["Number foundations: exponents, surds and accuracy",
                "Algebraic expressions and factorisation",
                "Linear equations, inequalities and systems",
                "Functions, coordinates and linear models",
                "Quadratic expressions and equations",
                "Quadratic functions and graphical reasoning",
                "Patterns, sequences and generalisation",
                "Growth and financial mathematics",
                "Congruence, similarity and transformations",
                "Pythagoras, trigonometry and measurement",
                "Surface area and volume", "Statistics: distributions and data",
                "Probability: combined events",
                "Capstone: designing a sustainable space"],
        criteria=[("A", "Knowing and understanding"), ("B", "Investigating patterns"),
                  ("C", "Communicating"), ("D", "Applying mathematics in real-life contexts")],
        inquiry_label="How this book works",
        inquiry="Every chapter opens with a task. You investigate, notice a pattern, state a "
                "mathematical conclusion and justify it before you meet the formal explanation.",
        author=AUTHOR,
        series="MYP Mathematics · Volume 4 of 5",
    ),
    imprint=dict(
        title="About this edition",
        credit="Author",
        author=AUTHOR,
        body=[
            "This is the second edition of the MYP 4 mathematics coursebook. It was rebuilt from the pre-rewrite MYP 4 audit, which recorded the chapter scope, the key and related concepts, the global contexts and the inquiry questions of the earlier edition, and identified where the teaching had to be strengthened.",
            "The edition keeps that chapter scope and the visual identity of the collection, and rebuilds the teaching sequence around inquiry: engagement, inquiry questions, investigation, observation, mathematical conclusion, formal development, worked examples, extensive visual practice, and application, assessment and reflection.",
            "The earlier edition's course map and its chapter openers disagreed on the key concept and the global context in eight chapters. The opener labels are used here, because they are the ones the teaching actually develops, and each reconciliation is recorded in the alignment review. The one confirmed defect in the earlier text — a probability game described as always having a winner — is corrected in Chapter 13.",
            "All classroom data sets are simulated and are labelled as such. Real data would require provenance, so no claim in this book rests on unverified statistics.",
            "No publisher, ISBN, print specification or commercial print-readiness claim is made in this file. The book is produced as an A4 review copy: fonts are embedded, pagination is continuous and every page has been checked for overflow.",
        ],
    ),
    howto=dict(
        title="How to use this book",
        intro="Each chapter follows the same sequence, so you always know what is coming next. The "
              "sequence is deliberate: you investigate before you are told the rule, because a rule "
              "you have discovered is a rule you can defend — and defending it is what Year 4 asks "
              "of you.",
        steps=[
            ("Engagement", "A short situation that raises the question the chapter will answer."),
            ("Inquiry questions", "Factual, conceptual and debatable questions that frame the chapter."),
            ("Investigation", "A task you complete before the formal teaching: record evidence in a table and look for a pattern."),
            ("Observation and discovery", "What you noticed, stated in your own words and compared with a partner."),
            ("Mathematical conclusion", "The rule that the evidence supports, written as a general statement you can justify."),
            ("Formal development", "The explanation, definitions and notation, with the reasoning made explicit."),
            ("Worked examples", "Problem, visual representation, mathematical reasoning, step-by-step solution, final answer and interpretation."),
            ("Practice", "Separated into Criterion A, B, C and D practice, with visual representations throughout."),
            ("Application, assessment and reflection", "Real-context tasks, criterion-based assessment practice, and a reflection that returns to the statement of inquiry."),
        ],
        criteria_title="The four MYP mathematics criteria",
        criteria=[
            ("A · Knowing and understanding", "Apply knowledge to familiar and unfamiliar problems, and check results."),
            ("B · Investigating patterns", "Investigate relationships, describe patterns, formulate a conjecture, test it and justify the generalisation — at Year 4 level a justification is a general argument, not a list of cases."),
            ("C · Communicating", "Use correct mathematical language, notation and complete representations, and organise reasoning into a coherent structure that a reader can follow."),
            ("D · Applying mathematics in real-life contexts", "Apply mathematics to authentic situations, identify relevant information, and comment on the accuracy and sense of the result."),
        ],
        notes=[
            "Practice is separated by criterion so that you can see which skill a task is training. Criterion B practice is additional genuine pattern investigation, not a repeat of the teaching.",
            "Visuals are part of the mathematics. Where a task supplies a diagram, grid, table, number line or model, use it; where it asks you to sketch, your drawing is part of the answer.",
            "Answers and student-facing reasoning are collected at the back of the book, with a formula bank, a glossary and references.",
            "Every chapter ends with project connections: a Service as Action opportunity, a Community Project connection and a Personal Project connection for MYP 5.",
            "The book closes with a capstone chapter: a single sustained modelling task that uses mathematics from every part of the year.",
        ],
    ),
    intro=dict(
        title="MYP mathematics and this coursebook",
        paras=[
            "The IB Middle Years Programme asks students to inquire into concepts through global contexts, to develop approaches to learning (ATL) skills, and to act on what they learn through service as action. In mathematics this means more than practising procedures: students investigate patterns, justify generalisations, communicate with precise language and apply mathematics to situations that matter to them.",
            "MYP mathematics is organised into four branches — number, algebra, geometry and trigonometry, and statistics and probability — and the programme recommends at least 50 hours of teaching per subject each year. This coursebook covers the Year 4 content of those branches across thirteen chapters and a capstone, grouped into five parts.",
            "Year 4 is the bridge level. The register for this year records the same four branches as every other year, and the chapters here follow the branch recorded for each of them: number and abstract reasoning, thinking with models, spatial reasoning, and reasoning with data, with an integrated capstone at the end.",
            "Assessment in MYP mathematics uses four equally weighted criteria, each with a maximum of 8: A knowing and understanding, B investigating patterns, C communicating, and D applying mathematics in real-life contexts. This book trains each criterion explicitly, and says so on the page where the training happens.",
        ],
        projects_title="Projects, service and action",
        projects=[
            ("Service as Action", "Each chapter includes a service opportunity with a community need, a mathematical connection, a proposed action, an expected impact and a student reflection. Completing an exercise is not service: service requires action that benefits others and reflection on that action."),
            ("Community Project", "MYP students completing the programme in Year 3 or Year 4 complete a community project. Each chapter offers a student-led project idea with a research question, the mathematics involved, an action or outcome, beneficiaries and evidence. Follow your school's requirements and supervision."),
            ("Personal Project (MYP 5)", "Students completing MYP in Year 5 complete a personal project. Each chapter offers an adaptable MYP 5-oriented extension with a personal interest, a learning goal, a product, the mathematics involved, a process and evidence. It is deliberately different from the community project and from service as action."),
        ],
        honesty_title="What this book does not claim",
        honesty=[
            "Programme requirements quoted here follow the official IB MYP curriculum, mathematics and projects pages and the MYP general regulations. Everything else — the chapter sequence, the investigations, the practice sets and the project ideas — is author-designed material built to serve those requirements, and is not an IB publication.",
            "No ISBN, publisher, imprint or print specification is claimed. The file is an A4 review copy with embedded fonts and continuous pagination, produced for proofing and classroom review rather than for commercial print production.",
        ],
    ),
    backcover=dict(
        kicker="MYP Mathematics · Student coursebook",
        edition="Second edition",
        heading="About this book",
        paras=[
            "Thirteen chapters and a capstone that take number foundations, algebraic expressions and factorisation, linear equations and systems, functions and linear models, quadratics, sequences and generalisation, growth and financial mathematics, congruence and similarity, Pythagoras and trigonometry, surface area and volume, statistics and combined probability from first ideas to justified use. Each chapter opens with a task: you investigate, notice a pattern, state a mathematical conclusion you can defend, and only then meet the formal explanation — with worked examples that model a complete solution and practice separated into Criterion A, B, C and D sets so you can see which skill each task trains.",
            "Year 4 reasoning is applied, not just correct: models are built from stated assumptions, checked against data and evaluated for their limitations, and Criterion B tasks ask you to justify a generalisation rather than to list cases. Every chapter closes with a reflection that returns to the statement of inquiry.",
            "The book closes with a capstone: a sustained modelling task in which a design claim about space, cost, shade and water becomes defensible only when it is modelled, tested and evaluated. Every chapter also closes with a Service as Action opportunity, a Community Project connection and a Personal Project extension for MYP 5. The back of the book carries complete student-facing answers with reasoning, a formula bank, a glossary and references.",
        ],
        collection_heading="MYP Mathematics · the five-volume collection",
        collection_note="One inquiry-led course from Year 1 to Year 5. Volumes 1, 2 and 3 are "
                        "produced; volume 4 is this volume; volume 5 is in preparation. The covers "
                        "shown here are coordinated collection designs, not published volumes.",
        smallprint="Second edition · A4 review copy · embedded fonts · continuous pagination. No ISBN, "
                   "publisher, print specification or commercial print-readiness claim is made.",
        author=AUTHOR,
        foot_right="Second edition · MYP Mathematics",
    ),
)

CHAPTERS = []

F = diagrams2.fig

CHAPTERS.extend([
dict(
    num=1, title="Number Foundations: Exponents, Surds and Accuracy",
    key="Form", related=["Simplification", "Equivalence", "Approximation", "Quantity"],
    context="Scientific and technical innovation",
    exploration="Precision, accuracy and measurement",
    inquiry=("The form in which a quantity is written — exact, approximate, or as a power — "
             "determines both the precision that can be claimed and the operations that can be "
             "performed, and simplification is the art of choosing the form that answers the "
             "question."),
    atl=("Critical thinking",
         "In order for a student to decide how exact an answer must be, students must compare "
         "two forms of the same quantity, identify what each form hides, and justify the choice "
         "of form for a stated purpose."),
    standfirst="The same number can be written as a fraction, a decimal, a power or a surd. Each "
               "form is exact or approximate, and each makes a different operation easy.",
    engage="A engineer specifies a bolt as 12.7 mm across. A machinist measures it as 12.73 mm. "
           "A calculator gives 12.732 051… mm. Which of these is the bolt, and which is the "
           "measurement?",
    questions=[("Factual", "What do the index laws say, and how is a number written in standard "
                           "form?"),
               ("Conceptual", "Why does the form of a quantity decide which operations are easy, "
                              "and what does an error interval tell you that a rounded value "
                              "cannot?"),
               ("Debatable", "When a measurement is reported to the nearest millimetre, is the "
                             "rounded value a lie, a convenience, or the most honest statement "
                             "available?")],
    application_lede="These tasks use index laws, standard form, surds and error intervals. "
                     "State the form of every quantity you report, and say whether it is exact "
                     "or approximate.",
    projects_lede="Precision is a design decision. Choose the form that makes the quantity "
                  "usable, and say what the choice costs.",
    sections=[
        dict(id="1.1", title="Number systems and proof",
             inquiry_q="How can a claim about all numbers be shown to be true rather than "
                       "tested?",
             teach=[
                 "The number system is built in stages: the counting numbers, then the integers, then the rationals, then the irrationals. Each stage exists because the previous one could not answer a question that arose naturally.",
                 "A rational number is one that can be written as a fraction of two integers. Its decimal either terminates or recurs. An irrational number cannot be written as a fraction, and its decimal neither terminates nor recurs. Equivalence between two forms of a number means that they name the same point, not that they look alike.",
                 "Proof at this level means a general argument. To show that the sum of two rationals is rational, write them as a/b and c/d and add: (ad + bc)/bd, which is again a fraction of integers. One argument covers every pair, so no list of examples is needed.",
                 "A counterexample is enough to destroy a universal claim. Finding ten examples that work is not enough to establish one, and this asymmetry is the whole logic of generalisation.",
             ], examples=[
                 dict(q="Show that the sum of two rational numbers is rational, and find an "
                        "irrational number whose sum with 1 is rational.",
                      vis=F("table", [["number", "form", "kind"],
                                      ["3/4", "fraction", "rational"],
                                      ["0.25", "terminating decimal", "rational"],
                                      ["√2", "surd", "irrational"],
                                      ["π", "non-repeating decimal", "irrational"]],
                            caption="Form decides kind, and kind decides which operations stay inside the system."),
                      reasoning="Write both numbers as fractions and add; the result is again a "
                               "fraction, which is the definition of rational.",
                      steps=["Let the numbers be a/b and c/d with integers a, b, c, d and b, d ≠ 0.",
                             "Their sum is a/b + c/d = (ad + bc)/bd.",
                             "ad + bc and bd are integers and bd ≠ 0, so the sum is rational.",
                             "For the second part, √2 − 1 is irrational and 1 + (√2 − 1) = √2, so "
                             "no such example exists with a rational result unless the irrational "
                             "part is removed."],
                      ans="the sum of two rationals is always rational; an irrational plus a "
                          "rational is always irrational",
                      interp="One algebraic argument settles infinitely many cases, which is why "
                             "proof is worth more than testing."),
                 dict(q="A student claims that the product of two irrational numbers is always "
                        "irrational. Investigate.",
                      vis=F("table", [["first", "second", "product", "kind of product"],
                                      ["√2", "√8", "4", "rational"],
                                      ["√2", "√3", "√6", "irrational"],
                                      ["π", "1/π", "1", "rational"]],
                            caption="Two irrationals can multiply to a rational or to an irrational."),
                      reasoning="A universal claim needs one counterexample to fall, and here "
                               "there are several.",
                      steps=["√2 × √8 = √16 = 4, which is rational.",
                             "So the claim is false as stated.",
                             "But √2 × √3 = √6, which is irrational, so no simple replacement "
                             "claim works either.",
                             "The honest statement is that the product of two irrationals may be "
                             "rational or irrational, and each case must be checked."],
                      ans="the claim is false: √2 × √8 = 4",
                      interp="A counterexample ends a universal claim, and finding one is a "
                             "complete proof of its falsity."),
             ], inv=dict(
                 task="Take six numbers of your own: two rational, two irrational, and two you "
                      "are unsure about. Add and multiply each pair, and decide for each result "
                      "whether it is rational or irrational. Then try to state a rule that "
                      "predicts the kind of the answer before you calculate it.",
                 table=[["pair", "operation", "result", "rational?"],
                        ["1/2 + 1/3", "add", "5/6", "yes"],
                        ["1/2 + √2", "add", "irrational", "no"],
                        ["√2 × √8", "multiply", "4", "yes"],
                        ["√2 × √3", "multiply", "√6", "no"],
                        ["√2 × 0", "multiply", "0", "yes"],
                        ["√2 + (−√2)", "add", "0", "yes"]],
                 notice=["Adding two rationals always gave a rational.",
                         "Adding a rational and an irrational always gave an irrational.",
                         "Multiplying two irrationals sometimes gave a rational and sometimes an "
                         "irrational, so no single rule exists.",
                         "Zero is the exception that breaks every multiplication rule, because "
                         "anything times zero is zero."],
                 obs="The kind of a result is fixed by the operation and the kinds of the inputs, "
                     "except for multiplication, where the surds can combine into a perfect "
                     "square.",
                 concl="The rationals are closed under addition, subtraction, multiplication and "
                       "division by a non-zero rational; the irrationals are closed under none of "
                       "them, and this is why exact form matters when a calculation must stay "
                       "exact.")),
        dict(id="1.2", title="Integer and rational exponents",
             inquiry_q="Why do the index laws hold for every exponent, not only for the ones we "
                       "can count?",
             teach=[
                 "For positive integers the index laws are definitions of repeated multiplication: aᵐ × aⁿ means m copies of a times n copies of a, which is m + n copies.",
                 "The zero index is fixed by the quotient law. If aᵐ ÷ aⁿ = aᵐ⁻ⁿ must hold when m = n, then a⁰ = aᵐ ÷ aᵐ = 1, and this forces a ≠ 0 because division by zero is undefined.",
                 "The negative index follows the same way. a⁻ⁿ must satisfy aⁿ × a⁻ⁿ = a⁰ = 1, so a⁻ⁿ = 1/aⁿ. The laws are not memorised; they are the only extension that keeps them consistent.",
                 "A rational index is a root written as a power. a^(1/n) is the number whose nth power is a, and a^(m/n) = (ⁿ√a)ᵐ. This unifies roots and powers into one notation.",
             ], examples=[
                 dict(q="Evaluate 8^(2/3) × 8^(1/3) ÷ 8^(−1).",
                      vis=F("table", [["step", "working", "value"],
                                      ["8^(2/3)", "cube root then square", "4"],
                                      ["× 8^(1/3)", "4 × 2", "8"],
                                      ["÷ 8^(−1)", "8 ÷ 1/8", "64"]],
                            caption="one base throughout, so the exponents add and subtract"),
                      reasoning="All three factors have base 8, so the exponents combine by the "
                               "product and quotient laws.",
                      steps=["8^(2/3) × 8^(1/3) = 8^(2/3 + 1/3) = 8¹.",
                             "8¹ ÷ 8^(−1) = 8^(1 − (−1)) = 8².",
                             "8² = 64.",
                             "Check: 8^(2/3) = 4, 8^(1/3) = 2, and 4 × 2 ÷ (1/8) = 8 × 8 = 64."],
                      ans="64",
                      interp="The laws turn a calculation with roots and reciprocals into one "
                             "line of arithmetic on exponents."),
                 dict(q="Solve 4^(x+1) = 8^(x−1).",
                      vis=F("table", [["side", "as a power of 2"],
                                      ["4^(x+1)", "(2²)^(x+1) = 2^(2x+2)"],
                                      ["8^(x−1)", "(2³)^(x−1) = 2^(3x−3)"]],
                            caption="Both sides are powers of the same base."),
                      reasoning="Rewrite both sides with a common base, then equate the exponents "
                               "because a one-to-one power function has one input per output.",
                      steps=["4 = 2² and 8 = 2³.",
                             "So 2^(2x+2) = 2^(3x−3).",
                             "Equal powers of the same base have equal exponents: 2x + 2 = 3x − 3.",
                             "Solving gives x = 5.",
                             "Check: 4⁶ = 4096 and 8⁴ = 4096."],
                      ans="x = 5",
                      interp="A common base converts an exponential equation into a linear one, "
                             "which is the standard first move."),
             ], inv=dict(
                 task="Build a table of powers of 2 from 2^(−3) to 2⁴ and a matching table of "
                      "powers of 3. Use only your tables to work out 2^(−3) × 2⁵, 3⁴ ÷ 3⁶ and "
                      "(2³)^(2/3). Then explain why the answers must be what they are.",
                 table=[["expression", "using the laws", "value"],
                        ["2^(−3) × 2⁵", "2^(−3+5) = 2²", "4"],
                        ["3⁴ ÷ 3⁶", "3^(4−6) = 3^(−2)", "1/9"],
                        ["(2³)^(2/3)", "2^(3 × 2/3) = 2²", "4"],
                        ["2^(−3) ÷ 2^(−3)", "2⁰", "1"],
                        ["(3^(−2))^(−1)", "3²", "9"]],
                 notice=["Every answer came from adding, subtracting or multiplying exponents, "
                         "never from calculating the powers.",
                         "A negative exponent always produced a reciprocal.",
                         "A zero exponent always produced 1, which is what the quotient law "
                         "requires.",
                         "The fractional exponent undid the integer exponent exactly, because "
                         "3 × 2/3 = 2."],
                 obs="The index laws are the only rules needed, and they work for negative, zero "
                     "and fractional exponents without any new idea.",
                 concl="The index laws hold for all rational exponents because they are the "
                       "unique extension that keeps aᵐ × aⁿ = aᵐ⁺ⁿ true, and a zero or negative "
                       "exponent is a consequence of that requirement rather than a separate "
                       "rule.")),
        dict(id="1.3", title="Standard form and estimation",
             inquiry_q="Why is a × 10ⁿ the most useful way to write a very large or very small "
                       "quantity?",
             teach=[
                 "Standard form writes a number as a × 10ⁿ with 1 ≤ a < 10 and n an integer. It separates the size of a quantity from its digits, so 3.2 × 10⁸ and 3.2 × 10⁻⁸ can be compared at a glance.",
                 "Multiplying in standard form multiplies the coefficients and adds the exponents: (a × 10ᵐ)(b × 10ⁿ) = ab × 10ᵐ⁺ⁿ, then adjust so the coefficient lies in range.",
                 "Estimation is a deliberate choice of precision. Rounding every quantity to one significant figure before calculating gives an answer whose error can be bounded, which is what an engineer needs before a detailed calculation.",
                 "Significant figures count measured meaning from the first non-zero digit. A leading zero is never significant, and a trailing zero is significant only if the quantity is known to that precision.",
             ], examples=[
                 dict(q="A red blood cell is about 0.000 007 5 m across and a grain of sand about "
                        "0.000 35 m. Write both in standard form and estimate how many cells fit "
                        "across one grain.",
                      vis=F("table", [["object", "ordinary form", "standard form"],
                                      ["red blood cell", "0.0000075", "7.5 × 10⁻⁶"],
                                      ["grain of sand", "0.00035", "3.5 × 10⁻⁴"],
                                      ["ratio", "0.00035 ÷ 0.0000075", "4.7 × 10¹"]],
                            caption="Standard form makes the sizes and their ratio readable."),
                      reasoning="Write each quantity as a coefficient times a power of ten, then "
                               "divide the coefficients and subtract the exponents.",
                      steps=["0.000 007 5 = 7.5 × 10⁻⁶ m.",
                             "0.000 35 = 3.5 × 10⁻⁴ m.",
                             "The ratio is (3.5 ÷ 7.5) × 10^(−4 − (−6)) = 0.47 × 10².",
                             "Adjusting to standard form: 4.7 × 10¹, so about 47 cells fit across "
                             "one grain."],
                      ans="7.5 × 10⁻⁶ m and 3.5 × 10⁻⁴ m; about 47 cells fit across",
                      interp="Standard form turns a comparison of six zeros into a comparison of "
                             "two exponents."),
                 dict(q="Estimate (4.9 × 10⁶) ÷ (2.1 × 10⁻³) and state the error interval of "
                        "your estimate.",
                      vis=F("number_line", 0, 3000, 500, [2333], "thousands", "estimate"),
                      reasoning="Round each coefficient to one significant figure, then divide "
                               "the coefficients and subtract the exponents.",
                      steps=["4.9 × 10⁶ ≈ 5 × 10⁶ and 2.1 × 10⁻³ ≈ 2 × 10⁻³.",
                             "The estimate is (5 ÷ 2) × 10^(6 − (−3)) = 2.5 × 10⁹.",
                             "The true value is about 2.333 × 10⁹, so the estimate is about 7% "
                             "high.",
                             "Stating one significant figure signals that the answer is an "
                             "estimate, not a measurement."],
                      ans="about 2.5 × 10⁹, roughly 7% above the true value",
                      interp="An estimate is only useful if its precision is stated, because the "
                             "point of estimating is to know how good the answer is."),
             ], inv=dict(
                 task="Find four quantities from science or everyday life: one very large, one "
                      "very small, one a ratio, and one you can only estimate. Write each in "
                      "standard form, then estimate a calculation that combines two of them and "
                      "state the precision of your answer.",
                 table=[["quantity", "standard form", "kind"],
                        ["distance to the Sun", "1.5 × 10¹¹ m", "very large"],
                        ["width of a virus", "1 × 10⁻⁷ m", "very small"],
                        ["cells in the body", "3.7 × 10¹³", "very large"],
                        ["body cells ÷ virus width", "3.7 × 10²⁰", "ratio"]],
                 notice=["Every large quantity had a positive exponent and every small one a "
                         "negative exponent.",
                         "The ratio had an exponent equal to the difference of the two "
                         "exponents.",
                         "Rounding to one significant figure before dividing kept the arithmetic "
                         "mental.",
                         "The precision of the estimate was set by the least precise input."],
                 obs="Standard form separates the digits of a quantity from its size, so "
                     "operations on very large and very small quantities become operations on "
                     "small numbers and on exponents.",
                 concl="A quantity is written in standard form when its size and its digits must "
                       "be handled separately, and the precision claimed is decided by the "
                       "least precise quantity in the calculation.")),
        dict(id="1.4", title="Surds and exact values",
             inquiry_q="When is √12 a better answer than 3.464, and what does exact form let you "
                       "do that a decimal cannot?",
             teach=[
                 "A surd is an exact irrational root left in root form, such as √2 or 3√5. It is exact because it names the number rather than approximating it.",
                 "Surds simplify by extracting square factors: √(ab) = √a × √b, so √12 = √(4 × 3) = 2√3. Simplification makes two surds comparable, because 2√3 and √12 are the same number in different forms.",
                 "Rationalising a denominator multiplies by the conjugate so that the denominator becomes rational: 1/(√3) = √3/3, and 1/(2 + √3) = 2 − √3, because (2 + √3)(2 − √3) = 1.",
                 "Exact form is not pedantry. A calculation carried out in exact form and rounded once at the end has less error than the same calculation rounded at every step, and the difference grows with the number of steps.",
             ], examples=[
                 dict(q="Simplify √72 + √50 − √18 and hence estimate its value.",
                      vis=F("surd_spiral", 5, "√1, √2, √3, √4, √5 as hypotenuses"),
                      reasoning="Extract the square factor from each surd, then collect like "
                               "terms.",
                      steps=["√72 = √(36 × 2) = 6√2.",
                             "√50 = √(25 × 2) = 5√2.",
                             "√18 = √(9 × 2) = 3√2.",
                             "So the expression is 6√2 + 5√2 − 3√2 = 8√2.",
                             "Since √2 ≈ 1.414, the value is about 11.31."],
                      ans="8√2, which is about 11.31",
                      interp="Three unrelated-looking surds collapse into one term once they are "
                             "written in the same form, which is what simplification is for."),
                 dict(q="Rationalise the denominator of 6/(√5 − 1).",
                      vis=F("table", [["step", "expression"],
                                      ["start", "6/(√5 − 1)"],
                                      ["multiply by the conjugate", "6(√5 + 1)/((√5 − 1)(√5 + 1))"],
                                      ["denominator", "5 − 1 = 4"],
                                      ["simplified", "(3/2)(√5 + 1)"]],
                            caption="The conjugate removes the surd from the denominator."),
                      reasoning="Multiplying by (√5 + 1)/(√5 + 1) is multiplying by 1, so the "
                               "value is unchanged while the denominator becomes rational.",
                      steps=["(√5 − 1)(√5 + 1) = 5 − 1 = 4, by the difference of squares.",
                             "So 6/(√5 − 1) = 6(√5 + 1)/4.",
                             "Simplifying the fraction gives (3/2)(√5 + 1).",
                             "Numerically that is about 4.854, and 6/(√5 − 1) ≈ 6/1.236 ≈ 4.854."],
                      ans="(3/2)(√5 + 1)",
                      interp="Rationalising does not change the number; it changes the form so "
                             "that the value can be read or compared more easily."),
             ], inv=dict(
                 task="Draw a spiral of right-angled triangles, each with one leg of length 1 and "
                      "the other leg the previous hypotenuse. Record each hypotenuse exactly and "
                      "to four decimal places, then find the point at which the decimal form "
                      "stops being useful.",
                 table=[["step", "exact", "to 4 d.p.", "kind"],
                        ["1", "√1", "1.0000", "rational"],
                        ["2", "√2", "1.4142", "irrational"],
                        ["3", "√3", "1.7321", "irrational"],
                        ["4", "√4 = 2", "2.0000", "rational"],
                        ["5", "√5", "2.2361", "irrational"],
                        ["6", "√6", "2.4495", "irrational"]],
                 notice=["Only the perfect squares gave rational hypotenuses.",
                         "The decimal form of √2 repeats no pattern, so it can never be written "
                         "exactly as a decimal.",
                         "The exact form stays short while the decimal form grows without end.",
                         "Adding the next triangle used the exact form, not the rounded one."],
                 obs="Exact form stays finite and computable where decimal form does not, and "
                     "the two forms are the same number.",
                 concl="An irrational quantity is best left in exact form while a calculation is "
                       "in progress, and rounded once at the end, because the exact form carries "
                       "no error and the decimal form carries an unbounded one.")),
        dict(id="1.5", title="Accuracy, bounds and error",
             inquiry_q="What does a rounded value actually promise, and how do the promises "
                       "combine?",
             teach=[
                 "A value given to the nearest unit lies within half a unit of the true value. That interval is the error interval, and it is what the rounded value actually claims. Approximation is therefore a claim with a width, not a single number.",
                 "Bounds combine by the operation. The upper bound of a sum uses the upper bounds of both terms; the upper bound of a difference uses the upper bound of the first and the lower bound of the second.",
                 "Truncation is not rounding. Truncating 3.97 to one decimal place gives 3.9, while rounding gives 4.0, and the two have different error intervals.",
                 "Relative error compares the error with the quantity itself. A 1 mm error matters in a 10 mm part and hardly at all in a 10 m bridge, so absolute error alone never says whether a measurement is good enough.",
             ], examples=[
                 dict(q="A length is recorded as 4.6 cm to one decimal place. State its error "
                        "interval, and find the error interval of 3 × this length.",
                      vis=F("number_line", 4.5, 4.8, 0.1, [4.55, 4.65], "cm", "bounds"),
                      reasoning="The recorded value is within half of the last unit, and "
                               "multiplication by a positive constant scales the interval.",
                      steps=["The last unit is 0.1 cm, so half of it is 0.05 cm.",
                             "The length lies in [4.55, 4.65) cm.",
                             "Tripling gives [13.65, 13.95) cm.",
                             "Rounded to one decimal place the answer is between 13.6 and 13.9 "
                             "cm, which is a wide interval for a single recorded measurement."],
                      ans="the length is in [4.55, 4.65) cm and three times it is in "
                          "[13.65, 13.95) cm",
                      interp="Multiplication magnifies absolute error, so a measurement that is "
                             "fine on its own can be poor after it is scaled up."),
                 dict(q="A rectangular card measures 12.4 cm by 8.6 cm, each to one decimal "
                        "place. Find the error interval of its area.",
                      vis=F("table", [["quantity", "lower bound", "upper bound"],
                                      ["length", "12.35", "12.45"],
                                      ["width", "8.55", "8.65"],
                                      ["area", "105.5925", "107.6925"]],
                            caption="The extreme areas come from the extreme dimensions."),
                      reasoning="The largest area uses both upper bounds and the smallest uses "
                               "both lower bounds, because both dimensions are positive.",
                      steps=["Length is in [12.35, 12.45) cm and width in [8.55, 8.65) cm.",
                             "Minimum area = 12.35 × 8.55 = 105.5925 cm².",
                             "Maximum area = 12.45 × 8.65 = 107.6925 cm².",
                             "So the area is in [105.5925, 107.6925) cm², about 106 cm² to three "
                             "significant figures."],
                      ans="the area lies between 105.5925 cm² and 107.6925 cm²",
                      interp="The area is known to about 1%, even though each side is known to "
                             "about 0.4%, because the relative errors add."),
             ], inv=dict(
                 task="Measure the same object three times with three different instruments: a "
                      "ruler to the nearest millimetre, a tape to the nearest centimetre, and a "
                      "digital caliper to 0.01 mm. Record each reading, find its error interval, "
                      "and decide which instrument is good enough for a stated purpose.",
                 table=[["instrument", "reading", "error interval", "relative error"],
                        ["ruler", "12.4 cm", "±0.05 cm", "0.4%"],
                        ["tape", "12 cm", "±0.5 cm", "4%"],
                        ["caliper", "12.43 cm", "±0.005 cm", "0.04%"]],
                 notice=["All three instruments measured the same object and gave three "
                         "different-looking answers.",
                         "The error interval, not the number of digits shown, is what "
                         "distinguishes them.",
                         "The caliper's relative error is ten times smaller than the ruler's.",
                         "The best instrument depends on the purpose, not on the instrument."],
                 obs="An instrument's precision is a property of its smallest division, and the "
                     "error interval is the honest statement of what a reading claims.",
                 concl="A measurement is reported with its error interval, and the fitness of a "
                       "measurement is judged against the purpose it must serve rather than "
                       "against the number of digits it happens to show.")),
        dict(id="1.6", title="Investigation: how exact is exact?",
             inquiry_q="When is an exact form necessary, and when does it cost more than it is "
                       "worth?",
             teach=[
                 "An exact form is necessary when a later step would amplify the error of a rounded one, or when the answer must be checked symbolically rather than numerically.",
                 "An exact form costs more when the calculation is long, the numbers are awkward, and the required precision is low. In that case rounding early is efficient and the error is bounded.",
                 "The decision is a modelling decision: it depends on the required precision, the number of steps, and whether the result will be compared with a measurement.",
                 "A calculation carried out exactly and rounded once has less error than the same calculation rounded at every step, and the difference is the accumulated rounding error.",
             ], examples=[
                 dict(q="A cube has side 3.7 cm, measured to one decimal place. Find the error "
                        "interval of its volume, first exactly and then with each side rounded "
                        "to 3.7 from the start.",
                      vis=F("prism", "cuboid", 4, 3, 2, "side 3.7 cm"),
                      reasoning="The exact calculation keeps the bounds symbolic; the rounded "
                               "calculation loses them immediately.",
                      steps=["Side is in [3.65, 3.75) cm.",
                             "Exact: volume is in [3.65³, 3.75³) = [48.627 125, 52.734 375) cm³.",
                             "Rounded: volume = 3.7³ = 50.653 cm³, which sits inside the interval "
                             "but says nothing about it.",
                             "The interval is about 8% of the value, which is large for a "
                             "measurement to one decimal place."],
                      ans="the volume lies between 48.627 125 cm³ and 52.734 375 cm³",
                      interp="A single rounded value hides an interval that a power has "
                             "magnified, because the relative error is multiplied by the "
                             "exponent."),
                 dict(q="A bank pays 4% interest on a deposit of 12 500 dollars for 3 years, "
                        "compounded annually. Compare the answer calculated exactly with the "
                        "answer rounded at each step.",
                      vis=F("table", [["year", "exact balance", "rounded to cents"],
                                      ["0", "12500.00", "12500.00"],
                                      ["1", "13000.00", "13000.00"],
                                      ["2", "13520.00", "13520.00"],
                                      ["3", "14060.80", "14060.80"]],
                            caption="Here the two agree, because the rounding is small and the "
                                    "number of steps is few."),
                      reasoning="Compounding multiplies by the same factor each year, so the "
                               "exact form is initial × multiplierⁿ.",
                      steps=["The multiplier is 1.04, so the balance is 12 500 × 1.04³.",
                             "Exactly that is 12 500 × 1.124 864 = 14 060.80 dollars.",
                             "Rounded to cents at each step gives the same figure here.",
                             "With a larger number of years the two methods would separate, and "
                             "the exact form would be the honest one."],
                      ans="14 060.80 dollars, and the two methods agree at three years",
                      interp="Rounding at each step is harmless while the accumulated error is "
                             "below the precision required, and the modeller's job is to know "
                             "when that stops being true."),
             ], inv=dict(
                 task="Choose one calculation that matters to you — a recipe scaled up, a journey "
                      "cost, a savings target, or a measurement for a project. Carry it out three "
                      "ways: exactly throughout, rounded at every step, and rounded once at the "
                      "end. Compare the three answers and decide which you would report.",
                 table=[["method", "answer", "error", "cost"],
                        ["exact throughout", "14060.80", "0", "most work"],
                        ["rounded each step", "14060.80", "0 here", "least work"],
                        ["rounded once at end", "14060.80", "0 here", "medium"]],
                 notice=["With three years of compounding all three methods agreed.",
                         "With thirty years they would not, and the exact form would win.",
                         "The cost of exactness is arithmetic effort, not accuracy.",
                         "The cost of rounding early is accuracy that cannot be recovered."],
                 obs="Exactness is free in accuracy and expensive in effort; rounding is the "
                     "reverse, and the trade-off is decided by the number of steps and the "
                     "precision required.",
                 concl="An exact form is used while a calculation is in progress and a rounded "
                       "form is used to report its result, because the exact form carries no "
                       "error and the rounded form communicates the precision actually "
                       "achieved.")),
    ],
    practice=dict(
        A=[("1.1.1", "Write 0.4̄5̄ as a fraction.", "5/11",
            "Let x = 0.4555…, then 10x − x = 4.1.", "F"),
           ("1.1.2", "Classify √16, √20 and ³√8 as rational or irrational.", "√16 = 4 rational; "
            "√20 irrational; ³√8 = 2 rational", "Simplify each root before classifying.", "F"),
           ("1.1.3", "Show that √2 + √3 is irrational.", "If it were rational r, then (√3 + √2)² "
            "= 5 + 2√6 would be rational, so √6 would be rational, which is false.",
            "Square the sum and use the closure of the rationals.", "R"),
           ("1.1.4", "Evaluate 27^(2/3).", "9", "Take the cube root first, then square.", "F"),
           ("1.1.5", "Solve 2^(x+2) = 32.", "x = 3", "Write both sides as powers of 2.", "F"),
           ("1.1.6", "Simplify (3x²y)³ ÷ (9x⁴y).", "3x²y²", "Apply the power law then the quotient "
            "law.", "F"),
           ("1.1.7", "Write 0.000 000 42 in standard form.", "4.2 × 10⁻⁷",
            "Move the point seven places right.", "F"),
           ("1.1.8", "Simplify √48.", "4√3", "Extract the square factor 16.", "F"),
           ("1.1.9", "Rationalise 5/√7.", "5√7/7", "Multiply top and bottom by √7.", "F"),
           ("1.1.10", "A mass is 3.40 kg to two decimal places. State its error interval.",
            "[3.395, 3.405) kg", "Half of the last unit either side.", "F"),
           ("1.1.11", "Explain why 1/3 cannot be written exactly as a decimal.",
            "Its decimal recurs, so no finite decimal equals it; only a fraction can be exact.",
            "A finite decimal is a fraction whose denominator is a product of 2s and 5s.", "R"),
           ("1.1.12", "Find the error interval of the area of a rectangle with sides 5.2 m and "
            "3.1 m, each to one decimal place.", "[15.4225, 17.1075) m²",
            "Use the extreme dimensions for the extreme areas.", "R")],
        B=[("1.2.1", "The first four terms of a sequence of index values are 2⁰, 2¹, 2², 2³. "
            "Predict the next three and justify your rule.",
            "2⁴, 2⁵, 2⁶; each term is the previous term multiplied by 2.",
            "A geometric sequence has a constant multiplier.", "R"),
           ("1.2.2", "Investigate whether √(n² + n) is ever an integer for n a positive integer. "
            "State and justify a conclusion.",
            "Never: n² < n² + n < (n + 1)², so the root lies strictly between two consecutive "
            "integers.", "Sandwich the value between consecutive squares.", "R"),
           ("1.2.3", "Build a table of √n for n = 1 to 20 and describe the pattern of the gaps "
            "between consecutive values.",
            "The gaps decrease as n grows, because the square root function flattens.",
            "Compute the differences and look at their trend.", "R"),
           ("1.2.4", "Conjecture a rule for the last digit of 2ⁿ for positive integers n, test "
            "it, and justify it.",
            "The last digit cycles 2, 4, 8, 6, because 2⁴ = 16 ends in 6 and multiplying by 2 "
            "repeats the cycle.", "Only the last digit of each power matters.", "R"),
           ("1.2.5", "Investigate the values of n^(1/n) for n = 1 to 6 and predict where the "
            "maximum occurs.",
            "The maximum is at n = 3; the values fall after that.",
            "Compute the values and compare.", "R"),
           ("1.2.6", "The perimeters of the spiral triangles in section 1.4 form a sequence. "
            "Find its rule and test it on a term you did not draw.",
            "Each perimeter is the previous one plus 1, because each new triangle adds a leg of "
            "length 1.", "Track what is added at each step.", "R"),
           ("1.2.7", "Investigate whether n³ − n is always divisible by 6 for positive integers "
            "n, and justify your conclusion.",
            "Yes: n³ − n = (n − 1)n(n + 1), the product of three consecutive integers, so it is "
            "divisible by both 2 and 3.", "Factorise first.", "R"),
           ("1.2.8", "Conjecture a rule for the number of digits of 2ⁿ and test it for "
            "n = 1 to 10.",
            "The number of digits is the smallest integer greater than n log 2, so it grows "
            "roughly every three or four steps.", "Compare with powers of 10.", "C"),
           ("1.2.9", "Find the pattern in the sums 1/2, 1/2 + 1/4, 1/2 + 1/4 + 1/8 and justify "
            "the general rule.",
            "The sums approach 1, because the total is 1 − 1/2ⁿ.", "Write each sum with a common "
            "denominator.", "R"),
           ("1.2.10", "Investigate the error intervals of √n when n is rounded to the nearest "
            "integer, for n from 1 to 10.",
            "The interval widens as n grows, because the square root function flattens.",
            "Use the bounds of n and take roots.", "R"),
           ("1.2.11", "A pattern of tiles gives 1, 5, 13, 25 dots for figures 1 to 4. Find the "
            "rule and test it on figure 6.",
            "The rule is 2n² − 2n + 1, giving 61 for figure 6.",
            "Take differences to identify a quadratic.", "R")],
        C=[("1.3.1", "Explain in your own words what an index law is and why it holds for "
            "negative exponents.", "An index law is a rule for combining powers; it holds for "
            "negative exponents because aⁿ × a⁻ⁿ must equal a⁰ = 1, so a⁻ⁿ is forced to be "
            "1/aⁿ.", "State the requirement, then the consequence.", "R"),
           ("1.3.2", "Write a complete solution to: simplify √200 − √72, explaining each step.",
            "√200 = 10√2 and √72 = 6√2, so the difference is 4√2.",
            "Extract square factors, then collect like terms.", "F"),
           ("1.3.3", "Choose between 3.464 and 2√3 as the answer to a calculation and justify "
            "your choice.", "2√3 if the calculation continues or must be exact; 3.464 only to "
            "report a final value to a stated precision.", "Say what each form costs.", "R"),
           ("1.3.4", "Set out a full solution to (2 × 10⁵) × (3 × 10⁻⁸), labelling each step.",
            "6 × 10⁻³", "Multiply the coefficients and add the exponents.", "F"),
           ("1.3.5", "Explain the difference between rounding 3.97 to one decimal place and "
            "truncating it.", "Rounding gives 4.0 with error interval [3.965, 3.975); truncating "
            "gives 3.9 with interval [3.90, 3.91).", "State each interval.", "R"),
           ("1.3.6", "Describe, with a diagram, the error interval of a length recorded as "
            "5.0 cm.", "[4.95, 5.05) cm, because the last unit is 0.1 cm and half of it is "
            "0.05 cm either side.", "A number line makes the interval visible.", "F"),
           ("1.3.7", "Explain why the upper bound of a difference uses the lower bound of the "
            "second quantity.", "Because subtracting a smaller number gives a larger result, so "
            "the maximum of a − b uses the minimum of b.", "Test with numbers.", "R"),
           ("1.3.8", "Write the reasoning that shows √2 × √2 = 2, using the index laws.",
            "√2 = 2^(1/2), so √2 × √2 = 2^(1/2) × 2^(1/2) = 2¹ = 2.",
            "Convert to powers and apply the product law.", "F"),
           ("1.3.9", "Set out the argument that the rationals are closed under addition, in a "
            "form another student could follow.",
            "Let the numbers be a/b and c/d; their sum is (ad + bc)/bd, a fraction of integers "
            "with non-zero denominator, hence rational.", "Use the definition directly.", "R"),
           ("1.3.10", "Explain what standard form is and give one large and one small example.",
            "A number written as a × 10ⁿ with 1 ≤ a < 10; for example 3.2 × 10⁸ and 4.5 × 10⁻⁹.",
            "State the definition and two cases.", "F"),
           ("1.3.11", "Describe the relationship between significant figures and precision.",
            "The number of significant figures states the precision claimed; more figures mean a "
            "narrower error interval.", "Link digits to interval width.", "R"),
           ("1.3.12", "Explain, with an example, why a counterexample is enough to disprove a "
            "universal claim.", "A universal claim says every case works; one case that fails "
            "makes it false, as √2 × √8 = 4 disproves 'the product of two irrationals is "
            "irrational'.", "Contrast with needing infinitely many examples to prove one.", "R")],
        D=[("1.4.1", "A pipe is specified as 2.50 m to the nearest centimetre. Find the error "
            "interval of its length and of three pipes joined end to end.",
            "One pipe: [2.495, 2.505) m; three pipes: [7.485, 7.515) m.",
            "Half of the last unit either side, then multiply.", "A"),
           ("1.4.2", "A sample of soil has mass 0.046 kg measured to the nearest gram. Write "
            "this in standard form and find its error interval.",
            "4.6 × 10⁻² kg, interval [0.0455, 0.0465) kg.",
            "Convert first, then bound.", "A"),
           ("1.4.3", "A tank measures 1.2 m by 0.8 m by 0.5 m, each to one decimal place. Find "
            "the error interval of its capacity in litres and comment on whether it holds 480 "
            "litres.",
            "[426, 534) litres, so 480 litres is possible but not certain.",
            "Extreme dimensions give extreme volumes; 1000 litres = 1 m³.", "A"),
           ("1.4.4", "A phone signal takes 0.000 000 13 s to travel 40 m. Estimate the speed and "
            "state the precision of your estimate.",
            "About 3 × 10⁸ m/s, to one significant figure.",
            "Divide distance by time in standard form.", "A"),
           ("1.4.5", "A recipe for 4 people uses 0.35 kg of flour measured to the nearest 10 g. "
            "Scale it for 15 people and state the error interval.",
            "1.3125 kg, interval about [1.265, 1.360) kg.",
            "Scale the interval with the multiplier.", "A"),
           ("1.4.6", "A car's fuel consumption is 5.6 litres per 100 km, measured to one decimal "
            "place. Estimate the fuel for a 380 km trip and state the error interval.",
            "About 21.3 litres, interval about [20.7, 21.9] litres.",
            "Multiply, then bound the inputs.", "A"),
           ("1.4.7", "A builder needs a beam at least 3.00 m long. A supplier offers 2.98 m "
            "measured to the nearest centimetre. Is it acceptable? Justify.",
            "No: 2.98 m to the nearest centimetre could be as short as 2.975 m, which is below "
            "3.00 m.", "Compare the lower bound with the requirement.", "R"),
           ("1.4.8", "A photograph is 12.4 cm by 8.6 cm, each to one decimal place. It is "
            "enlarged by a factor of 2.5. Find the error interval of the enlarged area and "
            "comment on the accuracy.",
            "About 660 cm² to 690 cm², a spread of about 2%.",
            "Scale each dimension, then the interval.", "A"),
           ("1.4.9", "A bank rounds interest to the nearest cent each year. Explain whether the "
            "balance after 20 years is exact, and what a customer should ask for.",
            "It is not exact; the customer should ask for the exact balance and the rounding "
            "policy, because accumulated rounding is the bank's gain or the customer's loss.",
            "Compare rounding each step with rounding once.", "R"),
           ("1.4.10", "A nurse measures a dose as 2.5 ml to one decimal place. The safe range is "
            "2.4 to 2.6 ml. Is the measurement safe? Justify.",
            "Yes: the interval [2.45, 2.55) ml lies inside [2.4, 2.6] ml.",
            "Compare intervals, not single values.", "R"),
           ("1.4.11", "A farmer's field is 120 m by 85 m, each measured to the nearest metre. "
            "Find the error interval of the area in hectares and comment on the effect on a "
            "yield estimate.",
            "[1.019, 1.027] hectares, a spread of about 0.8%, so the yield estimate carries the "
            "same relative error.", "Bound each side, then the area; 1 ha = 10 000 m².", "A"),
           ("1.4.12", "Explain, with a calculation of your own, when reporting a measurement to "
            "too many digits is misleading.",
            "Any answer is acceptable if it shows that the digits beyond the instrument's "
            "precision are not measured and imply an accuracy that does not exist.",
            "Link digits to error interval.", "R")],
    ),
    assessment=[
        dict(title="A1 · The bridge cable",
             text="A suspension bridge cable is specified as 48.6 m to one decimal place. The "
                  "design load is calculated from the cross-sectional area, which is 2.4 × 10⁻³ "
                  "m² measured to two significant figures. Find the error interval of the volume "
                  "of cable needed, state it to a sensible precision, and explain whether "
                  "reporting the answer to six significant figures would be honest.",
             note="Criteria A and D · carry the bounds through the calculation and comment on "
                  "the precision you report."),
        dict(title="A2 · The medicine dose",
             text="A syrup is supplied at a concentration of 4.5 mg per ml, measured to two "
                  "significant figures. A patient needs a dose of 18 mg. A nurse measures the "
                  "dose with a syringe marked to 0.1 ml. Find the error interval of the delivered "
                  "dose, state whether it lies within 10% of 18 mg, and explain which measurement "
                  "limits the accuracy.",
             note="Criteria A and C · set out the bounds of each measurement before combining "
                  "them."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of simplification, equivalence, "
        "approximation and quantity appear in your work?",
        "How is the global context of scientific and technical innovation, and its exploration of "
        "precision, accuracy and measurement, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a rounded value for a decision about safety or cost, and what "
        "would you still like to ask?",
    ],
    review=dict(
        ideas=["The rationals are closed under addition and multiplication; the irrationals are not.",
               "Index laws hold for negative, zero and rational exponents.",
               "Standard form separates the digits of a quantity from its size.",
               "A surd is exact; a decimal approximation is not.",
               "Rationalising multiplies by the conjugate and leaves the value unchanged.",
               "A rounded value lies within half of its last unit.",
               "Bounds combine according to the operation used.",
               "Relative error, not absolute error, decides whether a measurement is good enough."],
        vocab=["rational", "irrational", "surd", "index", "standard form", "significant figures",
               "error interval", "bound", "truncation", "relative error", "conjugate",
               "rationalise"],
        mixed=[("1.R1", "Simplify √98."),
               ("1.R2", "Evaluate 16^(−3/4)."),
               ("1.R3", "Write 0.000 035 in standard form."),
               ("1.R4", "A length is 7.3 cm to one decimal place. State its bounds."),
               ("1.R5", "Rationalise 4/(3 − √2)."),
               ("1.R6", "Explain why a⁰ = 1 for a ≠ 0.")],
    ),
    projects=dict(
        service=[("Community need", "Public measurements — water volumes, medicine doses, "
                                    "construction sizes — are reported without their precision."),
                 ("Mathematical connection", "Error intervals, bounds and relative error."),
                 ("Proposed action", "Collect three reported measurements, find the error "
                                     "interval of each, and publish what they actually claim."),
                 ("Expected impact", "A reader can tell how precise a reported number is."),
                 ("Student reflection", "Record the measurements, the intervals and what you "
                                        "found.")],
        community=[("Project idea", "A precision audit of the school's own measurements."),
                   ("Need", "Timetables, budgets and lab results are quoted to different "
                            "precisions without explanation."),
                   ("Research question", "How precise are the numbers the school publishes, and "
                                         "does the precision match the use?"),
                   ("Mathematics", "Bounds, error intervals, relative error and standard form."),
                   ("Action or outcome", "A one-page audit with the interval for each figure."),
                   ("Beneficiaries", "Everyone who relies on a school figure."),
                   ("Evidence", "The audit sheet with intervals and a verdict for each figure.")],
        personal=[("Personal interest", "Cooking, sport, music or gaming."),
                  ("Learning goal", "To measure something you care about and state honestly how "
                                    "well you measured it."),
                  ("Product or outcome", "A measurement report with error intervals."),
                  ("Mathematics", "Bounds, relative error and choice of form."),
                  ("Process", "Measure three times, find the intervals, and report the "
                              "precision."),
                  ("Evidence", "The report and the intervals you found.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=2, title="Algebraic Expressions and Factorisation",
    key="Form", related=["Equivalence", "Simplification", "Pattern", "Representation"],
    context="Scientific and technical innovation",
    exploration="Design, optimisation and efficient form",
    inquiry=("The form an algebraic expression is written in decides what it reveals — a "
             "factorised form shows roots, an expanded form shows coefficients, and a completed "
             "square shows a turning point — and equivalence between forms means each one can "
             "be rewritten without changing its value."),
    atl=("Transfer",
         "Students apply factorisation, the laws of indices and algebraic fractions to "
         "expressions that first appear in expanded form, and transfer the structure of a "
         "pattern they have seen numerically to an expression they have not met before."),
    standfirst="The same expression can be expanded, factorised, or written as a single "
               "fraction. Choosing the right form is the whole skill, and every choice is "
               "reversible.",
    engage="A packaging designer needs a box whose surface area is S = 2x² + 10x + 8. Written "
           "this way the shape is invisible. What does the expression look like once it is "
           "factorised, and what does that tell you about the box?",
    questions=[("Factual", "What are the four methods of factorising a quadratic, and how is an "
                           "algebraic fraction simplified?"),
               ("Conceptual", "Why does factorising reveal information about a quadratic that "
                              "expansion hides, and what does it mean for two expressions to be "
                              "equivalent?"),
               ("Debatable", "Is a factorised form always the most useful form of an expression, "
                             "or does usefulness depend entirely on the question being asked?")],
    application_lede="Each task asks you to choose a form and justify the choice. Show the "
                     "rewriting, not just the answer.",
    projects_lede="Efficient form is a design goal. Find an expression in the world around you "
                  "and show which form answers the question being asked.",
    sections=[
        dict(id="2.1", title="Expanding and simplifying",
             inquiry_q="When do two different-looking expressions represent the same quantity?",
             teach=[
                 "Expanding multiplies out brackets using the distributive law: a(b + c) = ab + ac. The product of two binomials has four terms before any are collected.",
                 "Simplifying collects like terms and combines indices. Only terms with the same variables to the same powers can be combined, so 3x² and 5x² combine while 3x² and 5x do not.",
                 "Equivalence is tested by substituting values or by rewriting. Two expressions are equivalent if they give the same value for every input, which is a stronger claim than agreeing at one value.",
                 "Simplification is the search for the shortest equivalent form, and it is always reversible, so no information is lost when an expression is simplified.",
                 "The product (a + b)(c + d) = ac + ad + bc + bd is the engine of every expansion, and (a + b)² = a² + 2ab + b² and (a − b)² = a² − 2ab + b² are the two special cases worth knowing.",
             ], examples=[
                 dict(q="Expand and simplify (3x − 2)(2x + 5) − x(4x − 1).",
                      vis=F("table", [["method", "working"],
                                      ["product", "6x² + 15x − 4x − 10"],
                                      ["second product", "4x² − x"],
                                      ["subtract", "6x² + 11x − 10 − 4x² + x"],
                                      ["collect", "2x² + 12x − 10"]],
                            caption="Four terms from the first product, two from the second."),
                      reasoning="Expand each product, subtract every term of the second, then "
                               "collect like terms.",
                      steps=["(3x − 2)(2x + 5) = 6x² + 15x − 4x − 10 = 6x² + 11x − 10.",
                             "x(4x − 1) = 4x² − x.",
                             "Subtracting gives 6x² + 11x − 10 − 4x² + x.",
                             "Collecting like terms: 2x² + 12x − 10."],
                      ans="2x² + 12x − 10",
                      interp="The expanded form shows the coefficients directly, which is what "
                             "makes it easy to read off the size of each term."),
                 dict(q="Show that (x + 3)² − 9 and x² + 6x are equivalent, and say what each "
                        "form reveals.",
                      vis=F("table", [["form", "what it reveals"],
                                      ["(x + 3)² − 9", "a square shifted down by 9"],
                                      ["x² + 6x", "a quadratic with no constant term"],
                                      ["x(x + 6)", "roots at 0 and −6"]],
                            caption="Three forms of the same expression, three readings."),
                      reasoning="Expand the first expression and compare term by term with the "
                               "second.",
                      steps=["(x + 3)² = x² + 6x + 9.",
                             "So (x + 3)² − 9 = x² + 6x.",
                             "This is exactly the second expression, so they are equivalent.",
                             "The first shows a minimum at x = −3; the factorised form x(x + 6) "
                             "shows the roots."],
                      ans="the two expressions are equivalent",
                      interp="Equivalence is proved by rewriting, and each form exposes a "
                             "different feature of the same quantity."),
             ], inv=dict(
                 task="Take the expression (x + a)(x + b) and expand it for five pairs of "
                      "values of a and b. Record the coefficients of x and the constant term, "
                      "then predict the expansion of (x + a)(x + b) for a = 12 and b = −5 "
                      "without expanding.",
                 table=[["a", "b", "x² coefficient", "x coefficient", "constant"],
                        ["2", "3", "1", "5", "6"],
                        ["−2", "3", "1", "1", "−6"],
                        ["4", "−1", "1", "3", "−4"],
                        ["−3", "−3", "1", "−6", "9"],
                        ["5", "0", "1", "5", "0"]],
                 notice=["The x² coefficient was always 1, because both leading terms were x.",
                         "The x coefficient was always a + b.",
                         "The constant term was always ab.",
                         "The signs of a and b decided the signs of both results, exactly as "
                         "multiplication of signs predicts."],
                 obs="The expanded form carries a + b and ab as its middle and constant terms, "
                     "so the factorised form can be recovered from them.",
                 concl="Expanding (x + a)(x + b) gives x² + (a + b)x + ab, and factorising a "
                       "monic quadratic is therefore the search for two numbers whose sum and "
                       "product are the middle and constant terms.")),        dict(id="2.2", title="Common factors and grouping",
             inquiry_q="How does a common factor reveal the structure of an expression?",
             teach=[
                 "Every term of an expression may share a factor, and taking out the highest common factor rewrites the expression as a product. This is the first thing to try, because it makes every later step smaller.",
                 "The highest common factor includes the largest number that divides every coefficient and the lowest power of every variable that appears in every term. Taking out a smaller factor leaves work still to do.",
                 "When there is no common factor for the whole expression, the terms can often be grouped in pairs so that each pair has one. Four-term expressions are the usual case, and the same bracket then appears twice.",
                 "Grouping is expanding in reverse: the distributive law is applied backwards. Checking by expanding confirms the factorisation, and the check is quick enough that it should always be done.",
             ], examples=[
                 dict(q="Factorise fully 12x³y − 18x²y² + 6xy³.",
                      vis=F("tiles", 3, 3, [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1),
                                             (0, 2)],
                            "each term shares the same shaded factor",
                            note="6xy is common to all three terms"),
                      reasoning="Find the highest common factor of the coefficients and of each "
                               "variable, then divide every term by it.",
                      steps=["The coefficients are 12, 18 and 6, whose highest common factor "
                             "is 6.",
                             "The lowest power of x present in every term is x, and of y is "
                             "y.",
                             "So the highest common factor is 6xy.",
                             "Dividing each term by 6xy gives 2x² − 3xy + y².",
                             "Hence 12x³y − 18x²y² + 6xy³ = 6xy(2x² − 3xy + y²)."],
                      ans="6xy(2x² − 3xy + y²)",
                      interp="Taking out the highest common factor first leaves a shorter "
                             "expression, and the shorter expression is the one that can be "
                             "examined for further structure."),
                 dict(q="Factorise ax + ay + bx + by by grouping.",
                      vis=F("table", [["step", "expression"],
                                      ["group", "(ax + ay) + (bx + by)"],
                                      ["factor each pair", "a(x + y) + b(x + y)"],
                                      ["common bracket", "(x + y)(a + b)"]],
                            caption="the same bracket appears in both groups"),
                      reasoning="Group the terms in pairs, take out the factor of each pair, "
                               "then take out the bracket the pairs now share.",
                      steps=["Group as (ax + ay) + (bx + by).",
                             "The first pair has factor a and the second has factor b.",
                             "So the expression is a(x + y) + b(x + y).",
                             "Now (x + y) is common, so the expression is (x + y)(a + b).",
                             "Check by expanding: ax + ay + bx + by, which matches."],
                      ans="(x + y)(a + b)",
                      interp="Grouping works whenever the terms can be paired so that the same "
                             "bracket appears twice, and the expansion check confirms it."),
             ], inv=dict(
                 task="Take ten expressions of your own: four with a common factor, four "
                      "needing grouping in pairs, and two with neither. Factorise each where "
                      "possible, record the method, and check every answer by expanding.",
                 table=[["expression", "method", "factorised"],
                        ["8x² + 12x", "common factor", "4x(2x + 3)"],
                        ["x³ + x²", "common factor", "x²(x + 1)"],
                        ["ax + ay + bx + by", "grouping", "(x + y)(a + b)"],
                        ["2am + 2an + bm + bn", "grouping", "(m + n)(2a + b)"],
                        ["x² + x + 1", "neither", "does not factorise"]],
                 notice=["Every expression with a common factor gave a product immediately.",
                         "Every four-term expression could be grouped once the pairs were "
                         "chosen.",
                         "The last expression had no factorisation, which is a legitimate "
                         "outcome.",
                         "Expanding each answer returned the original expression exactly."],
                 obs="Factorising is the distributive law applied backwards, and the two "
                     "routes into it are a common factor for the whole expression or a common "
                     "factor for each of two groups.",
                 concl="An expression is factorised by taking out the highest common factor, "
                       "and when there is none for the whole expression the terms are grouped "
                       "so that each group has one.")),
        dict(id="2.3", title="Quadratic factorisation",
             inquiry_q="How is a quadratic turned into a product, and what does the product "
                       "reveal?",
             teach=[
                 "A monic quadratic x² + bx + c factorises when two numbers can be found whose sum is b and whose product is c. The order of the pair does not matter, because multiplication is commutative.",
                 "When the leading coefficient is not 1, either split the middle term into two terms whose coefficients multiply to ac and add to b, or take out a common factor first if there is one.",
                 "A product is zero only when one of its factors is zero, so a factorised quadratic equation becomes two linear equations. This is the reason factorising is worth the effort.",
                 "Not every quadratic factorises over the integers, and recognising that quickly saves time. The test is whether b² − 4ac is a perfect square, which is examined in chapter 5.",
             ], examples=[
                 dict(q="Factorise 2x² + 7x − 15 fully and hence solve 2x² + 7x − 15 = 0.",
                      vis=F("tiles", 3, 3, [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)],
                            "splitting the middle term into 10x and −3x"),
                      reasoning="Split the middle term into two terms whose coefficients "
                               "multiply to 2 × (−15) = −30 and add to 7.",
                      steps=["Two numbers with product −30 and sum 7 are 10 and −3.",
                             "So 2x² + 7x − 15 = 2x² + 10x − 3x − 15.",
                             "Grouping: 2x(x + 5) − 3(x + 5) = (2x − 3)(x + 5).",
                             "Setting each factor to zero gives x = 3/2 or x = −5."],
                      ans="(2x − 3)(x + 5), so x = 1.5 or x = −5",
                      interp="Factorisation converts a quadratic equation into two linear ones, "
                             "which is the whole point of the technique."),
                 dict(q="Factorise 3x² + 12x and explain what the factorised form shows that "
                        "the expanded form does not.",
                      vis=F("table", [["form", "expression", "what it shows"],
                                      ["expanded", "3x² + 12x", "the two terms"],
                                      ["factorised", "3x(x + 4)", "the roots 0 and −4"]],
                            caption="the factorised form answers a question the expanded form "
                                    "cannot"),
                      reasoning="Take out the highest common factor, then read the roots from "
                               "the product.",
                      steps=["The highest common factor of 3x² and 12x is 3x.",
                             "So 3x² + 12x = 3x(x + 4).",
                             "Setting 3x(x + 4) = 0 gives x = 0 or x = −4.",
                             "The expanded form gives no hint of either root.",
                             "The factorised form answers the question in one step."],
                      ans="3x(x + 4), with roots 0 and −4",
                      interp="The factorised form makes the roots visible, which is the "
                             "information a factorisation is usually wanted for."),
             ], inv=dict(
                 task="Build a table of quadratics x² + bx + c for b from −6 to 6 and c from "
                      "−6 to 6, and mark which factorise over the integers. Then find the "
                      "condition on b and c for factorising to be possible, and test it on a "
                      "case you did not tabulate.",
                 table=[["b", "c", "factorises?", "factors"],
                        ["5", "6", "yes", "(x + 2)(x + 3)"],
                        ["1", "−6", "yes", "(x − 2)(x + 3)"],
                        ["2", "5", "no", "—"],
                        ["−6", "9", "yes", "(x − 3)²"],
                        ["4", "4", "no", "—"]],
                 notice=["Factorising worked whenever two integers had the right sum and "
                         "product.",
                         "The discriminant b² − 4c was a perfect square in every successful "
                         "case.",
                         "b = 2, c = 5 failed because b² − 4c = −16 is negative.",
                         "The same two numbers appear in the factors and in the discriminant."],
                 obs="Whether a monic quadratic factorises over the integers is decided by "
                     "whether b² − 4c is a perfect square, and the two numbers needed are half "
                     "of b plus or minus half of that square root.",
                 concl="Factorising over the integers is possible exactly when b² − 4c is a "
                       "perfect square, which is the first appearance of the discriminant as a "
                       "test of structure rather than of calculation.")),
        dict(id="2.4", title="Special products and identities",
             inquiry_q="Why do the special products of a binomial deserve their own names?",
             teach=[
                 "Expanding a product of two binomials gives four terms, and in three important cases they collapse. Recognising the cases turns a multiplication into a substitution.",
                 "The perfect squares (a + b)² = a² + 2ab + b² and (a − b)² = a² − 2ab + b² each have three terms, and the middle one is twice the product of the two parts.",
                 "The difference of two squares a² − b² = (a + b)(a − b) has only two terms, and the absence of a middle term is the signal that identifies it.",
                 "These identities are equivalences, so they read in both directions. Reading them forwards expands and reading them backwards factorises, and the commonest error is to forget the cross term.",
                 "A pattern in a table of squares is one representation of these identities, and the representation as a diagram shows why the cross term must be there.",
             ], examples=[
                 dict(q="Expand (3x + 2)² and explain why it is not 9x² + 4.",
                      vis=F("tiles", 3, 3, [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1),
                                             (0, 2), (1, 2)],
                            "a 3 by 3 square of side 3x + 2",
                            note="9x², 12x and 4"),
                      reasoning="Use the perfect square identity and identify the missing cross "
                               "term.",
                      steps=["(3x + 2)² = (3x)² + 2(3x)(2) + 2² = 9x² + 12x + 4.",
                             "The term 12x is the cross term, and it is what 9x² + 4 leaves out.",
                             "The error is treating the square of a sum as the sum of the "
                             "squares.",
                             "A check at x = 1 gives 25 against 13, so the claim fails.",
                             "One substitution is enough to refute an algebraic claim."],
                      ans="9x² + 12x + 4",
                      interp="The cross term is the signature of a perfect square, and its "
                             "absence is the commonest error in expanding."),
                 dict(q="Factorise 9x² − 25 and explain why the answer is not (3x − 5)².",
                      vis=F("table", [["form", "structure"],
                                      ["9x² − 25", "difference of two squares"],
                                      ["(3x)² − 5²", "a² − b² with a = 3x, b = 5"],
                                      ["(3x + 5)(3x − 5)", "factorised"]],
                            caption="A difference of two squares, not a perfect square."),
                      reasoning="Recognise a² − b² and apply the identity.",
                      steps=["9x² = (3x)² and 25 = 5².",
                             "So 9x² − 25 = (3x + 5)(3x − 5).",
                             "Squaring (3x − 5) would give 9x² − 30x + 25, which has a middle "
                             "term.",
                             "A difference has no middle term, so the two are not the same.",
                             "The absence of a middle term is the signal for the identity."],
                      ans="(3x + 5)(3x − 5)",
                      interp="Confusing a difference of squares with a perfect square is the "
                             "commonest error with these identities, and the middle term is "
                             "what distinguishes them."),
             ], inv=dict(
                 task="Build a table of (a + b)² and (a − b)² for a = 1 to 5 and b = 1 to 5. "
                      "Record the coefficients of the cross term and of the constant, then "
                      "predict (5x − 7)² and 16x² − 49 without expanding, and check one case "
                      "by multiplication.",
                 table=[["a", "b", "(a + b)²", "cross term", "a² − b²"],
                        ["1", "1", "a² + 2ab + b²", "2", "0"],
                        ["1", "2", "a² + 4ab + 4b²", "4", "−3"],
                        ["2", "3", "4a² + 12ab + 9b²", "12", "−5"],
                        ["5", "7", "25a² + 70ab + 49b²", "70", "−24"],
                        ["4", "7", "16a² − 56ab + 49b²", "−56", "−33"]],
                 notice=["The cross term was always 2ab, whatever a and b were.",
                         "The constant term was always b².",
                         "The difference a² − b² always factorised as (a + b)(a − b).",
                         "The prediction for a = 5, b = 7 was confirmed by direct "
                         "multiplication."],
                 obs="The expansion of a squared binomial is completely determined by the two "
                     "parts, and the difference of two squares is completely determined by "
                     "them too.",
                 concl="(a + b)² = a² + 2ab + b², (a − b)² = a² − 2ab + b² and "
                       "a² − b² = (a + b)(a − b) are general identities, so any specific case "
                       "is a substitution rather than a new multiplication.")),
        dict(id="2.5", title="Algebraic fractions",
             inquiry_q="Why must an algebraic fraction be simplified before it can be used?",
             teach=[
                 "An algebraic fraction is simplified by factorising numerator and denominator and cancelling common factors. Cancellation is only legal for factors, never for terms.",
                 "Multiplying fractions multiplies numerators and denominators; dividing multiplies by the reciprocal. Adding and subtracting needs a common denominator.",
                 "A fraction is undefined wherever its denominator is zero, and these excluded values must be stated. They are not removable by cancelling; they are properties of the original expression.",
                 "Simplifying first keeps expressions small and errors rare, and it is the algebraic version of choosing the efficient form.",
             ], examples=[
                 dict(q="Simplify (x² − 9)/(x² + x − 12) and state the excluded values.",
                      vis=F("table", [["part", "factorised"],
                                      ["numerator", "(x + 3)(x − 3)"],
                                      ["denominator", "(x + 4)(x − 3)"],
                                      ["cancelled", "(x + 3)/(x + 4)"],
                                      ["excluded", "x = −4, x = 3"]],
                            caption="The common factor cancels, but the excluded value stays."),
                      reasoning="Factorise both parts, cancel the common factor, and state the "
                               "values that made the original denominator zero.",
                      steps=["x² − 9 = (x + 3)(x − 3), a difference of squares.",
                             "x² + x − 12 = (x + 4)(x − 3), because 4 and −3 have sum 1 and "
                             "product −12.",
                             "Cancelling (x − 3) gives (x + 3)/(x + 4).",
                             "The original denominator is zero at x = −4 and x = 3, so both are "
                             "excluded even though only −4 remains."],
                      ans="(x + 3)/(x + 4), with x ≠ −4 and x ≠ 3",
                      interp="Cancelling removes a factor from the expression but not from the "
                             "domain, and stating the excluded values is part of the answer."),
                 dict(q="Simplify 2/(x + 1) + 3/(x − 2) as a single fraction.",
                      vis=F("table", [["step", "expression"],
                                      ["common denominator", "(x + 1)(x − 2)"],
                                      ["rewrite", "2(x − 2)/((x + 1)(x − 2))"],
                                      ["rewrite", "3(x + 1)/((x + 1)(x − 2))"],
                                      ["add", "(2x − 4 + 3x + 3)/((x + 1)(x − 2))"],
                                      ["simplify", "(5x − 1)/((x + 1)(x − 2))"]],
                            caption="One denominator, then one numerator."),
                      reasoning="Rewrite each fraction with the common denominator, add the "
                               "numerators, and factorise the result.",
                      steps=["The common denominator is (x + 1)(x − 2).",
                             "2/(x + 1) = 2(x − 2)/((x + 1)(x − 2)) and 3/(x − 2) = 3(x + 1)/((x "
                             "+ 1)(x − 2)).",
                             "Adding the numerators: 2x − 4 + 3x + 3 = 5x − 1.",
                             "So the sum is (5x − 1)/((x + 1)(x − 2))."],
                      ans="(5x − 1)/((x + 1)(x − 2))",
                      interp="A single fraction is easier to evaluate and to compare than two "
                             "separate ones, which is why addition is always carried out this "
                             "way."),
             ], inv=dict(
                 task="Take six fractions of the form (x² + bx + c)/(x² + dx + e) of your own "
                      "choice. Factorise each, simplify, and record the excluded values. Then "
                      "find one pair of fractions that simplify to the same expression but have "
                      "different excluded values.",
                 table=[["fraction", "simplifies to", "excluded"],
                        ["(x² − 4)/(x² − x − 6)", "(x + 2)/(x − 3)", "x = 3, x = −2"],
                        ["(x² − 4)/(x² + x − 6)", "(x − 2)/(x + 3)", "x = −3, x = 2"],
                        ["(x² − 9)/(x² − 9)", "1", "x = 3, x = −3"],
                        ["(x² + 5x + 6)/(x² − 4)", "(x + 3)/(x − 2)", "x = 2, x = −2"]],
                 notice=["Cancelling changed the look of the fraction but never its domain.",
                         "Two fractions can simplify to the same expression and still be "
                         "different functions.",
                         "A fraction that simplifies to 1 still has excluded values.",
                         "The excluded values came from the denominator, not from the "
                         "numerator."],
                 obs="A simplified fraction and its original are equal everywhere except at "
                     "the values excluded by the original denominator, so simplification is an "
                     "equivalence with holes.",
                 concl="Simplifying an algebraic fraction is legitimate only when the excluded "
                       "values are carried alongside the simplified form, because the "
                       "denominator's zeros survive cancellation.")),        dict(id="2.6", title="Rearranging formulae",
             inquiry_q="Why does rearranging a formula preserve equality at every step?",
             teach=[
                 "Rearranging applies the same operation to both sides, so equality is preserved. Adding, subtracting, multiplying and dividing by a non-zero quantity are all reversible.",
                 "The subject of a formula is the quantity being found, and rearranging changes which quantity is the subject. A formula with two subjects is a relationship, not a recipe.",
                 "Squaring both sides can introduce solutions that do not satisfy the original, so it must be checked. Multiplying by an expression that could be zero can lose solutions, which is the opposite risk.",
                 "Efficient rearrangement chooses the order of operations that avoids fractions inside fractions, because each extra layer is a place where an error can hide.",
                 "The pattern of a rearrangement is the same for every formula of the same shape, so a method learned on one transfers to the next."
             ], examples=[
                 dict(q="Make r the subject of A = πr² + 2πrh.",
                      vis=F("table", [["step", "working"],
                                      ["start", "A = πr² + 2πrh"],
                                      ["group the r terms", "A = πr(r + 2h)"],
                                      ["divide", "A/(πr) = r + 2h"],
                                      ["isolate", "r = A/(πr) − 2h"]],
                            caption="The radius appears twice, so it must be grouped first."),
                      reasoning="Factorise the right-hand side by r, then isolate r by "
                               "reversible operations.",
                      steps=["A = πr² + 2πrh = πr(r + 2h).",
                             "Dividing by πr gives A/(πr) = r + 2h.",
                             "Subtracting 2h gives r = A/(πr) − 2h.",
                             "This still contains r on both sides, so the formula must instead "
                             "be treated as a quadratic in r: πr² + 2πhr − A = 0.",
                             "Solving gives r = −h + √(h² + A/π), taking the positive root."],
                      ans="r = −h + √(h² + A/π)",
                      interp="Recognising that a rearrangement is a quadratic in disguise "
                             "prevents a circular manipulation that never isolates the subject."),
                 dict(q="Make x the subject of (x + a)/(x + b) = c, stating any restriction.",
                      vis=F("table", [["step", "working"],
                                      ["multiply by x + b", "x + a = c(x + b)"],
                                      ["expand", "x + a = cx + cb"],
                                      ["collect x", "x − cx = cb − a"],
                                      ["factorise", "x(1 − c) = cb − a"]],
                            caption="Clearing the fraction makes the algebra linear."),
                      reasoning="Multiply by the denominator, expand, collect the terms in x, "
                               "then factorise x out.",
                      steps=["Multiply both sides by (x + b): x + a = c(x + b).",
                             "Expanding: x + a = cx + cb.",
                             "Collecting x terms: x − cx = cb − a.",
                             "Factorising: x(1 − c) = cb − a, so x = (cb − a)/(1 − c).",
                             "This needs c ≠ 1, and the original needs x ≠ −b."],
                      ans="x = (cb − a)/(1 − c), with c ≠ 1 and x ≠ −b",
                      interp="Every division and every multiplication by a variable introduces a "
                             "condition, and the conditions are part of the answer."),
             ], inv=dict(
                 task="Take five formulae from science, sport or home economics of your choice. "
                      "For each, rearrange to make a different quantity the subject, and record "
                      "the conditions introduced at each step.",
                 table=[["formula", "original subject", "new subject", "condition"],
                        ["v = u + at", "v", "t", "a ≠ 0"],
                        ["A = πr²", "A", "r", "r ≥ 0"],
                        ["P = 2(l + w)", "P", "w", "none"],
                        ["F = ma", "F", "m", "a ≠ 0"],
                        ["s = d/t", "s", "t", "t ≠ 0"]],
                 notice=["Every rearrangement that divided by a variable introduced a "
                         "condition.",
                         "The formulae with two variables stayed symmetrical whichever was the "
                         "subject.",
                         "Making r the subject of A = πr² gave two roots, and only one was "
                         "physically meaningful.",
                         "Recording the conditions was as important as the rearrangement."],
                 obs="Rearrangement is a chain of reversible operations, and each irreversible "
                     "step adds a condition that must travel with the result.",
                 concl="A rearranged formula is equivalent to the original only on the domain "
                       "where every step is reversible, so the conditions are stated as part of "
                       "the formula.")),
    ],
    practice=dict(
        A=[("2.1.1", "Expand (x + 5)(x − 3).", "x² + 2x − 15",
            "Multiply every term of one bracket by every term of the other.", "F"),
           ("2.1.2", "Factorise x² − 7x + 12.", "(x − 3)(x − 4)",
            "Two numbers with sum −7 and product 12.", "F"),
           ("2.1.3", "Simplify (x² − 16)/(x² − 8x + 16).", "(x + 4)/(x − 4)",
            "Factorise both parts and cancel.", "F"),
           ("2.1.4", "Make x the subject of y = 3x − 7.", "x = (y + 7)/3",
            "Add 7, then divide by 3.", "F"),
           ("2.1.5", "Evaluate (2x³)² when x = −1.", "4",
            "Square the coefficient and multiply the indices.", "F"),
           ("2.1.6", "Expand and simplify (x + 4)² − (x − 4)².", "16x",
            "Expand both squares and collect; the x² terms cancel.", "F"),
           ("2.1.7", "Factorise 4x² − 49.", "(2x + 7)(2x − 7)",
            "A difference of two squares.", "F"),
           ("2.1.8", "Simplify 3/(x) + 2/(x + 1) as a single fraction.",
            "(5x + 3)/(x(x + 1))", "Use the common denominator x(x + 1).", "F"),
           ("2.1.9", "Write (x^(−2))^(−3) with a positive index.", "x⁶",
            "Multiply the indices: (−2)(−3) = 6.", "F"),
           ("2.1.10", "Make a the subject of v = u + at.", "a = (v − u)/t",
            "Subtract u, then divide by t.", "F"),
           ("2.1.11", "Expand (2x − 3y)².", "4x² − 12xy + 9y²",
            "Use a² − 2ab + b² with a = 2x, b = 3y.", "F"),
           ("2.1.12", "Simplify (6x³y²)/(9x⁵y).", "2y/(3x²)",
            "Divide the coefficients and subtract the indices.", "F")],
        B=[("2.2.1", "The perimeters of a sequence of rectangles are 6, 10, 14, 18 cm. Find the "
            "rule for the nth perimeter and test it on the fifth rectangle.",
            "4n + 2, giving 22 cm for the fifth.", "The common difference is 4.", "R"),
           ("2.2.2", "Investigate the areas of the same rectangles and find the rule.",
            "The areas are 2, 6, 12, 20, following n² + n.",
            "Take differences to identify a quadratic.", "R"),
           ("2.2.3", "Conjecture a rule for the number of diagonals of an n-sided polygon and "
            "test it for n = 4, 5, 6.",
            "n(n − 3)/2, giving 2, 5, 9.", "Each vertex joins to n − 3 others; divide by 2.", "R"),
           ("2.2.4", "Investigate the pattern in 1², 2², 3² and the differences between "
            "consecutive squares.",
            "The differences are the odd numbers, because (n + 1)² − n² = 2n + 1.",
            "Expand the difference of squares.", "R"),
           ("2.2.5", "Build a table of x² + bx + c for b = 4 and c = −5, −4, −3, …, 5 and mark "
            "which factorise.",
            "Those with b² − 4c a perfect square: c = −5, 3, 4.",
            "Compute the discriminant.", "R"),
           ("2.2.6", "Conjecture a rule for the sum of the first n odd numbers and justify it.",
            "n², because the odd numbers are the differences of consecutive squares.",
            "Relate to the pattern in 2.2.4.", "R"),
           ("2.2.7", "Investigate whether x² + x + 41 is prime for every positive integer x, "
            "and state your conclusion.",
            "It is prime for x = 1 to 39 but not for x = 40, where the value is 41².",
            "Test, then look for a counterexample.", "R"),
           ("2.2.8", "The sequence of expressions x, x(x + 1), x(x + 1)(x + 2) is built by "
            "multiplication. Predict the next and investigate its factors.",
            "x(x + 1)(x + 2)(x + 3), which is always divisible by 24.",
            "Four consecutive integers include a multiple of 4 and two evens.", "C"),
           ("2.2.9", "Find the pattern in the sums 1/(1×2), 1/(1×2) + 1/(2×3), and justify the "
            "general rule.",
            "n/(n + 1), because each term is 1/k − 1/(k + 1).",
            "Split the fraction into partial fractions.", "R"),
           ("2.2.10", "Investigate the areas of squares drawn on the sides of a right-angled "
            "triangle with legs a and b.",
            "The sum of the two smaller squares equals the largest, which is Pythagoras' "
            "theorem.", "Draw and measure for several triangles.", "R"),
           ("2.2.11", "Conjecture a rule for the last digit of n⁵ for positive integers n and "
            "justify it.",
            "The last digit of n⁵ equals the last digit of n.",
            "Only the last digit matters, so test ten cases.", "R")],
        C=[("2.3.1", "Explain in your own words what it means for two expressions to be "
            "equivalent.", "They give the same value for every permitted input, which is "
            "stronger than agreeing at one value.", "State the definition and its strength.", "R"),
           ("2.3.2", "Write a complete solution to: factorise 3x² − 12.",
            "3(x + 2)(x − 2)", "Take out the common factor, then the difference of squares.", "F"),
           ("2.3.3", "Choose between (x + 2)(x + 3) and x² + 5x + 6 as the answer to a question "
            "about roots and justify.", "(x + 2)(x + 3), because a product is zero only when a "
            "factor is zero.", "Say what each form gives.", "R"),
           ("2.3.4", "Set out a full solution to: simplify (x² − 25)/(x² − 10x + 25).",
            "(x + 5)/(x − 5), with x ≠ 5.", "Factorise both parts and cancel.", "F"),
           ("2.3.5", "Explain why (x + y)² is not x² + y².",
            "Squaring a sum produces a cross term 2xy, which is missing from the sum of the "
            "squares.", "Expand and compare.", "R"),
           ("2.3.6", "Describe, with an example, the difference between cancelling a factor and "
            "cancelling a term.", "A factor may be cancelled because it divides both parts; a "
            "term may not, because (x + 3)/(x) does not simplify.", "Test with a number.", "R"),
           ("2.3.7", "Explain why the excluded values of a fraction must be stated.",
            "The original expression is undefined there even when the simplified form is not, "
            "so the two expressions differ at those points.", "Link to the definition of a "
            "function.", "R"),
           ("2.3.8", "Write the reasoning that shows x⁻ⁿ = 1/xⁿ.",
            "xⁿ × x⁻ⁿ = x⁰ = 1, so x⁻ⁿ is the reciprocal of xⁿ.",
            "Use the product law and the zero index.", "F"),
           ("2.3.9", "Set out the argument that the discriminant b² − 4c decides whether a monic "
            "quadratic factorises.", "The roots are (−b ± √(b² − 4c))/2, and they are rational "
            "exactly when b² − 4c is a perfect square.", "Use the quadratic formula.", "R"),
           ("2.3.10", "Explain what the subject of a formula is and give an example.",
            "The quantity isolated on one side; in v = u + at the subject is v.",
            "State the definition and an example.", "F"),
           ("2.3.11", "Describe the relationship between factorising and solving an equation.",
            "Factorising converts a product equal to zero into linear factors, each of which "
            "gives a solution.", "Use the zero-product property.", "R"),
           ("2.3.12", "Explain, with an example, why squaring both sides of an equation can "
            "introduce false solutions.", "x = −3 becomes x² = 9, which also has x = 3 as a "
            "solution.", "Square and check both roots.", "R")],
        D=[("2.4.1", "A rectangular garden has length (2x + 6) m and width (x − 1) m. Find its "
            "area in factorised form and the value of x that gives zero area.",
            "A = (2x + 6)(x − 1), zero at x = −3 or x = 1.",
            "A product is zero when a factor is zero.", "A"),
           ("2.4.2", "A company's profit is P = (x − 20)(200 − x) dollars for x items. Find the "
            "factorised form, the break-even values, and the number of items giving the "
            "greatest profit.",
            "Break-even at x = 20 and x = 200; the greatest profit is at x = 110.",
            "The maximum of a quadratic with roots 20 and 200 lies halfway between them.", "A"),
           ("2.4.3", "A tray's surface area is S = 2x² + 14x + 24 cm². Find the value of x that "
            "gives the smallest area and the area itself.",
            "S = 2(x + 3)(x + 4), smallest at x = −3.5 with S = 0.5 cm².",
            "Complete the square or use the midpoint of the roots.", "A"),
           ("2.4.4", "A phone plan costs C = 20 + 0.05n dollars for n minutes. Rewrite this to "
            "make n the subject and find the minutes affordable for 35 dollars.",
            "n = (C − 20)/0.05, so 300 minutes for 35 dollars.",
            "Rearrange, then substitute.", "A"),
           ("2.4.5", "A photograph is enlarged by a factor of k and its area becomes "
            "A = k²(2x + 10)(x + 4). Find the factorised form and the value of k giving zero "
            "area.", "Zero only when k = 0, since k² ≥ 0 and the frame factors are positive.",
            "A product is zero when a factor is zero.", "R"),
           ("2.4.6", "A swimming pool's volume is V = x(2x + 6)(x − 2) m³. Find the value of x "
            "that gives the greatest volume for 0 < x < 2 and justify.",
            "The greatest volume is at x = 1, by symmetry about the midpoint of the roots 0 and "
            "2.", "A cubic with roots 0, −3, 2 is symmetric about x = 1.", "R"),
           ("2.4.7", "A bridge cable's tension is T = (3x + 12)(x − 5) newtons. Explain whether "
            "a tension of zero is possible, and justify.",
            "Yes, at x = −4 or x = 5, but only x = 5 is physically meaningful.",
            "A product is zero when a factor is zero.", "R"),
           ("2.4.8", "A shop's revenue is R = x(40 − x) dollars. Find the price giving the "
            "greatest revenue and explain why the factorised form makes this easy.",
            "x = 20 dollars, because the maximum lies halfway between the roots 0 and 40.",
            "Use the symmetry of a quadratic with two known roots.", "A"),
           ("2.4.9", "A field's yield is Y = (x + 3)(x − 1)(10 − x) tonnes. Investigate the "
            "values of x in 1 < x < 10 that maximise the yield and justify.",
            "The maximum is near x = 4.2, found by testing values rather than by symmetry, "
            "because the cubic has no axis of symmetry.", "Evaluate at several points.", "C"),
           ("2.4.10", "A car's value is V = 12000(1 − r)ⁿ dollars after n years. Rewrite to make "
            "r the subject and find the rate that halves the value in 3 years.",
            "r = 1 − (1/2)^(1/3) ≈ 0.206, about 21% per year.",
            "Set V = 6000, divide, and take the cube root.", "A"),
           ("2.4.11", "A cone's volume is V = (1/3)πr²h. Rewrite to make r the subject and "
            "explain which form is best for a given volume and height.",
            "r = √(3V/(πh)); this form is best when V and h are known.",
            "Multiply by 3, divide by πh, then take the root.", "A"),
           ("2.4.12", "Explain, with a formula of your own, when a factorised form is "
            "misleading.", "Any answer is acceptable if it identifies a case where the "
            "factorised form hides the size of a coefficient or a gradient, as in "
            "1000(x + 1).", "Give a specific counterexample.", "R")],
    ),
    assessment=[
        dict(title="A1 · The packaging problem",
             text="A box with a square base of side x cm and height 8 cm has surface area "
                  "S = 2x² + 32x + 128 cm². Factorise S fully, find the value of x for which the "
                  "surface area is zero, and explain why that value is not a useful answer for a "
                  "designer. Then find the value of x that gives a surface area of 200 cm².",
             note="Criteria A and C · show the factorisation and the equation you solve, and "
                  "comment on the physical meaning of each root."),
        dict(title="A2 · The formula and the conditions",
             text="A formula for the speed v of a wave is v = √(T/μ), where T is tension and μ "
                  "is mass per unit length. Rewrite the formula to make μ the subject, state the "
                  "conditions that apply, and explain what happens to the speed when the mass "
                  "per unit length is quadrupled.",
             note="Criteria A and D · square both sides, isolate μ, and check the direction of "
                  "the change."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of equivalence, simplification, "
        "pattern and representation appear in your work?",
        "How is the global context of scientific and technical innovation, and its exploration of "
        "design, optimisation and efficient form, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of choosing a form for convenience rather than for the question, "
        "and what would you still like to ask?",
    ],
    review=dict(
        ideas=["Expanding uses the distributive law; factorising reverses it.",
               "(x + a)(x + b) = x² + (a + b)x + ab.",
               "a² − b² = (a + b)(a − b) is the difference of two squares.",
               "A product is zero only when a factor is zero.",
               "Algebraic fractions simplify by cancelling factors, never terms.",
               "Excluded values come from the original denominator and survive cancellation.",
               "Index laws apply to any base and any rational exponent.",
               "(x + y)² = x² + 2xy + y², not x² + y².",
               "Rearranging preserves equality only while every step is reversible."],
        vocab=["expand", "factorise", "equivalence", "like terms", "common factor",
               "difference of squares", "algebraic fraction", "excluded value", "subject",
               "cross term", "zero-product property", "discriminant"],
        mixed=[("2.R1", "Expand (2x − 5)(x + 3)."),
               ("2.R2", "Factorise 3x² + 10x − 8."),
               ("2.R3", "Simplify (x² − 1)/(x² + 2x + 1)."),
               ("2.R4", "Make t the subject of s = ut + ½at²."),
               ("2.R5", "Evaluate (27x⁶)^(1/3) when x = 2."),
               ("2.R6", "Explain why x = 0 is excluded from 1/(x² − x).")],
    ),
    projects=dict(
        service=[("Community need", "Packaging and material use are decided without showing the "
                                    "algebra behind them."),
                 ("Mathematical connection", "Expanding, factorising and choosing an efficient "
                                             "form."),
                 ("Proposed action", "Model the surface area of one real package in factored "
                                     "form and publish what the form reveals."),
                 ("Expected impact", "A reader sees why the shape of a box follows from its "
                                     "algebra."),
                 ("Student reflection", "Record the model, the factorisation and what it "
                                        "showed.")],
        community=[("Project idea", "An algebra audit of the school's own cost formulae."),
                   ("Need", "Costs, timetables and catering figures are quoted as numbers with "
                            "no visible structure."),
                   ("Research question", "Which forms of the school's own formulae make "
                                         "decisions easiest, and why?"),
                   ("Mathematics", "Expanding, factorising, rearranging and indices."),
                   ("Action or outcome", "A sheet showing three school formulae in two forms "
                                         "each, with a recommendation."),
                   ("Beneficiaries", "Anyone who has to use the school's figures."),
                   ("Evidence", "The audit sheet with the forms and the reasoning.")],
        personal=[("Personal interest", "Cooking, sport, gaming or music."),
                  ("Learning goal", "To model something you enjoy with an algebraic expression "
                                    "and choose the best form of it."),
                  ("Product or outcome", "A model with two forms and a justified choice."),
                  ("Mathematics", "Expanding, factorising and rearranging."),
                  ("Process", "Build the model, rewrite it in two forms, and test each against "
                              "a real question."),
                  ("Evidence", "The model and the comparison of the two forms.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=3, title="Linear Equations, Inequalities and Systems",
    key="Relationships", related=["Equivalence", "Change", "System"],
    context="Fairness and development",
    exploration="Collective decisions under constraints",
    inquiry=("A linear equation records an equivalence between two descriptions of the same "
             "quantity, and solving it is the search for the value at which the two "
             "descriptions agree; when several constraints act at once, the feasible values are "
             "a system rather than a single number, and the solution is the region where all "
             "the constraints hold."),
    atl=("Communication",
         "Students move between the algebraic, tabular and graphical representations of the "
         "same linear relationship, and explain to a reader which representation answers the "
         "question asked."),
    standfirst="Two linear descriptions of one quantity agree at exactly one point. Several "
               "constraints acting together describe a region, and the answer is often a set "
               "of values rather than a single one.",
    engage="A school has 240 dollars to spend on 30 books. Some cost 6 dollars and some cost "
           "10 dollars. How many of each can it buy, and how many answers are possible?",
    questions=[("Factual", "What are the three algebraic methods for solving a pair of "
                           "simultaneous linear equations, and how is a linear inequality "
                           "solved?"),
               ("Conceptual", "Why does solving a linear equation preserve equivalence, and "
                              "what does the solution of a system of inequalities represent?"),
               ("Debatable", "When a group must share a limited resource under several "
                             "constraints, is there a single fair answer, or is fairness "
                             "itself the thing being negotiated?")],
    application_lede="Each task involves a constraint and a decision. State the constraint as "
                     "an equation or inequality before solving it, and check that your answer "
                     "satisfies every condition.",
    projects_lede="Fairness under constraints is a mathematical question with a human answer. "
                  "Model one real allocation and say which solution you would defend.",
    sections=[
        dict(id="3.1", title="Linear equations and formulae",
             inquiry_q="Why does every step in solving an equation preserve equivalence?",
             teach=[
                 "An equation states that two expressions have the same value. Solving means finding every value of the unknown for which that statement is true, and every legal step keeps the statement true.",
                 "The legal steps are adding, subtracting, multiplying and dividing both sides by the same non-zero quantity. Each is reversible, so the solution set is unchanged at every step.",
                 "Collecting the unknown on one side and the constants on the other turns the equation into x = k. The order of the steps does not matter, but doing the same thing to both sides always does.",
                 "An equation with the unknown on both sides is solved by collecting terms, and an equation with brackets is solved by expanding first. Multiplying by a common denominator clears fractions in one step.",
             ], examples=[
                 dict(q="Solve 3(2x − 5) − 4(x + 1) = 5.",
                      vis=F("number_line", -2, 6, 2, [3], "x", "the solution"),
                      reasoning="Expand, collect the unknown on one side and the constants on "
                               "the other, then divide by the coefficient.",
                      steps=["3(2x − 5) = 6x − 15 and 4(x + 1) = 4x + 4.",
                             "So 6x − 15 − 4x − 4 = 5, which is 2x − 19 = 5.",
                             "Adding 19 to both sides gives 2x = 24.",
                             "Dividing by 2 gives x = 12.",
                             "Check: 3(24 − 5) − 4(13) = 57 − 52 = 5."],
                      ans="x = 12",
                      interp="Every step was reversible, so the solution of the final equation "
                             "is the solution of the original, which is why checking works."),
                 dict(q="Solve (x + 2)/3 − (x − 1)/4 = 1.",
                      vis=F("table", [["step", "working"],
                                      ["common denominator", "12"],
                                      ["multiply through", "4(x + 2) − 3(x − 1) = 12"],
                                      ["expand", "4x + 8 − 3x + 3 = 12"],
                                      ["collect", "x + 11 = 12"],
                                      ["solve", "x = 1"]],
                            caption="Clearing the fractions first keeps the arithmetic small."),
                      reasoning="Multiply every term by the lowest common denominator, then "
                               "solve the resulting linear equation.",
                      steps=["The lowest common denominator of 3 and 4 is 12.",
                             "Multiplying every term by 12 gives 4(x + 2) − 3(x − 1) = 12.",
                             "Expanding: 4x + 8 − 3x + 3 = 12.",
                             "Collecting: x + 11 = 12, so x = 1.",
                             "Check: 3/3 − 0/4 = 1."],
                      ans="x = 1",
                      interp="Multiplying by a non-zero common denominator does not change the "
                             "solution set, so the cleared equation is equivalent to the "
                             "original."),
             ], inv=dict(
                 task="Take five linear equations of increasing difficulty: one with the "
                      "unknown on one side, one with it on both, one with brackets, one with "
                      "fractions, and one of your own invention. Solve each, record the "
                      "sequence of steps, and check each solution in the original equation.",
                 table=[["equation", "steps used", "solution", "check"],
                        ["5x + 3 = 18", "subtract, divide", "3", "18 = 18"],
                        ["7x − 4 = 3x + 12", "collect, divide", "4", "24 = 24"],
                        ["2(x + 5) = 3(x − 1)", "expand, collect", "13", "36 = 36"],
                        ["x/2 + 1 = 4", "clear, subtract", "6", "4 = 4"],
                        ["(x − 2)/5 = (x + 1)/3", "clear, collect", "−5.5", "check passes"]],
                 notice=["Every solution came from reversible steps only.",
                         "The check always gave a true statement, which is the definition of a "
                         "correct solution.",
                         "The equations with brackets needed expansion before collecting.",
                         "The equations with fractions needed one multiplication to clear "
                         "them."],
                 obs="Solving a linear equation is a chain of reversible transformations, and "
                     "the check confirms that the chain was reversible at every link.",
                 concl="Two equations linked by reversible steps have exactly the same solution "
                       "set, which is what makes algebraic solution legitimate rather than "
                       "merely convenient.")),
        dict(id="3.2", title="Inequalities and number lines",
             inquiry_q="How does a solution change when equality is replaced by an inequality?",
             teach=[
                 "A linear inequality states that one expression is greater or less than another. Its solution is a set of values, usually an interval, not a single number.",
                 "Solving an inequality uses the same steps as solving an equation, with one exception: multiplying or dividing by a negative number reverses the inequality sign.",
                 "The solution is shown on a number line, with an open circle for a strict inequality and a closed circle for one that includes the endpoint, and it is written in interval notation.",
                 "Compound inequalities such as 3 < 2x + 1 ≤ 9 are solved by applying the same operation to all three parts, which keeps the two comparisons linked.",
             ], examples=[
                 dict(q="Solve 5 − 2x ≥ 11 and show the solution on a number line.",
                      vis=F("number_line", -6, 6, 2, [-3], "x", "x ≤ −3"),
                      reasoning="Collect the unknown, then divide by a negative coefficient, "
                               "which reverses the sign.",
                      steps=["5 − 2x ≥ 11.",
                             "Subtracting 5 from both sides gives −2x ≥ 6.",
                             "Dividing by −2 reverses the sign: x ≤ −3.",
                             "On a number line this is every value to the left of −3, including "
                             "−3.",
                             "Check at x = −4: 5 + 8 = 13 ≥ 11, and at x = 0: 5 ≥ 11 is false."],
                      ans="x ≤ −3",
                      interp="The reversal of the sign is the only difference between solving an "
                             "inequality and solving an equation, and forgetting it is the "
                             "commonest error."),
                 dict(q="A taxi charges 3 dollars plus 1.80 dollars per kilometre. A budget of "
                        "25 dollars is available. Find the greatest whole number of kilometres "
                        "possible.",
                      vis=F("double_number_line", "cost in dollars", "distance in km",
                            "the same journey in two units"),
                      reasoning="Model the cost as a linear function of distance, write the "
                               "budget as an inequality, and solve.",
                      steps=["The cost is C = 3 + 1.8k, where k is the distance in kilometres.",
                             "The budget gives 3 + 1.8k ≤ 25.",
                             "Subtracting 3 gives 1.8k ≤ 22.",
                             "Dividing by 1.8 gives k ≤ 12.22…",
                             "So the greatest whole number of kilometres is 12."],
                      ans="12 km",
                      interp="The continuous solution was 12.22 km, and the question asked for "
                             "a whole number, so the answer was rounded down rather than to the "
                             "nearest."),
             ], inv=dict(
                 task="Take five inequalities: one with a positive coefficient, one with a "
                      "negative coefficient, one compound, one with brackets, and one with "
                      "fractions. Solve each, draw the solution on a number line, and test one "
                      "value inside and one outside your solution set.",
                 table=[["inequality", "solution", "inside", "outside"],
                        ["2x + 1 > 7", "x > 3", "x = 4 works", "x = 2 fails"],
                        ["−3x ≤ 9", "x ≥ −3", "x = 0 works", "x = −4 fails"],
                        ["1 ≤ 2x − 3 < 7", "2 ≤ x < 5", "x = 3 works", "x = 6 fails"],
                        ["4(x − 1) < 2x + 6", "x < 5", "x = 0 works", "x = 6 fails"],
                        ["x/3 − 2 ≥ 1", "x ≥ 9", "x = 9 works", "x = 8 fails"]],
                 notice=["The negative coefficient reversed the sign in exactly one case.",
                         "The compound inequality gave a closed left end and an open right end.",
                         "Testing a value inside and a value outside caught every sign error.",
                         "The solution was a set in every case, never a single number."],
                 obs="An inequality is solved by the same reversible steps as an equation, "
                     "except that division by a negative reverses the order, and the answer is "
                     "an interval rather than a value.",
                 concl="The solution of a linear inequality is the set of values for which the "
                       "statement is true, and it is verified by testing one value from inside "
                       "the set and one from outside.")),
        dict(id="3.3", title="Systems of equations: graphs and substitution",
             inquiry_q="Why do two linear equations in two unknowns have one solution, and how "
                       "is it found?",
             teach=[
                 "A pair of simultaneous linear equations is a system: two conditions that must hold at the same time. Each equation alone has infinitely many solutions, and the system has the values that satisfy both.",
                 "Graphically, each equation is a line and the solution is the point where the lines cross. The graphical method gives an estimate whose precision is limited by the grid, and it is the method that shows why a solution exists.",
                 "Substitution replaces one unknown with an expression taken from the other equation. It is the natural choice when one equation already has a subject, and it turns a system into a single equation in one unknown.",
                 "The algebraic and graphical methods must always agree, because they answer the same question. A disagreement means an error in one of them, and the check is worth doing every time.",
             ], examples=[
                 dict(q="Solve y = 2x − 1 and 3x + y = 12 by substitution.",
                      vis=F("grid", [(2.6, 4.2), (4, 0), (0, 12)], ["crossing", "", ""], -1, 6,
                            -2, 14, [(0, -1), (2.6, 4.2)],
                            "the lines cross at (2.6, 4.2)"),
                      reasoning="Substitute the expression for y from the first equation into "
                               "the second.",
                      steps=["The first equation gives y = 2x − 1.",
                             "Substituting into the second: 3x + (2x − 1) = 12.",
                             "So 5x = 13 and x = 2.6.",
                             "Then y = 2(2.6) − 1 = 4.2.",
                             "Check in the second equation: 3(2.6) + 4.2 = 12."],
                      ans="x = 2.6, y = 4.2",
                      interp="Substitution reduces two equations to one, and the check confirms "
                             "that the pair still holds."),
                 dict(q="Solve x + y = 7 and x − y = 1 graphically, and state the precision of "
                        "your answer.",
                      vis=F("grid", [(4, 3), (7, 0), (0, 7)], ["crossing", "", ""], -1, 8, -1, 8,
                            [(0, 7), (7, 0), (0, -1), (7, 1)],
                            "the two lines cross at (4, 3)"),
                      reasoning="Draw both lines on the same axes and read the coordinates of "
                               "the crossing point.",
                      steps=["x + y = 7 passes through (0, 7) and (7, 0).",
                             "x − y = 1 passes through (0, −1) and (7, 6), so it has gradient "
                             "1.",
                             "The lines cross at (4, 3), which the grid shows directly.",
                             "Reading from a grid gives the answer to the precision of the "
                             "grid, here about 0.1.",
                             "Solving algebraically gives exactly x = 4 and y = 3, confirming "
                             "the reading."],
                      ans="x = 4, y = 3, to the precision of the grid",
                      interp="The graphical method shows why a solution exists and gives an "
                             "estimate; the algebraic method gives the exact value, and the two "
                             "must agree."),
             ], inv=dict(
                 task="Take five pairs of linear equations: one with a subject already "
                      "isolated, one needing rearranging first, one with parallel lines, one "
                      "with the same line twice, and one of your own. Solve each by "
                      "substitution and by drawing, and record what the pair of lines looks "
                      "like.",
                 table=[["pair", "substitution result", "lines"],
                        ["y = 3, x + y = 8", "x = 5, y = 3", "cross once"],
                        ["y = 2x, 3x + y = 10", "x = 2, y = 4", "cross once"],
                        ["x + y = 4, x + y = 7", "no solution", "parallel"],
                        ["2x + 2y = 6, x + y = 3", "infinitely many", "the same line"],
                        ["3x − y = 2, 6x − 2y = 5", "no solution", "parallel"]],
                 notice=["Every consistent pair with different gradients gave exactly one "
                         "solution.",
                         "The parallel pairs gave no solution, because no point lies on both "
                         "lines.",
                         "The pair with proportional equations gave infinitely many solutions.",
                         "Substitution was easier when one equation already had a subject."],
                 obs="Two linear equations in two unknowns have one solution, no solution, or "
                     "infinitely many, according to whether their lines cross, are parallel, "
                     "or coincide.",
                 concl="The number of solutions of a linear system is a property of the pair of "
                       "lines, so the algebraic answer and the graphical answer must always "
                       "agree.")),
        dict(id="3.4", title="Elimination and special cases",
             inquiry_q="Why do two linear equations in two unknowns have one solution, and when "
                       "do they have none or many?",
             teach=[
                 "A pair of simultaneous linear equations is a system: two conditions that must hold at the same time. Each equation alone has infinitely many solutions, and the system has the values that satisfy both.",
                 "Elimination adds or subtracts the equations to remove one unknown, and works when a coefficient can be matched. Substitution replaces one unknown with an expression from the other equation.",
                 "Two equations with the same left-hand side but different right-hand sides describe parallel lines and have no solution. Two equations that are multiples of each other describe the same line and have infinitely many solutions.",
                 "Solving a system is equivalent to finding the point of intersection of two lines, which is why the graphical method and the algebraic method must always agree.",
             ], examples=[
                 dict(q="Solve 3x + 2y = 16 and 5x − 2y = 8 simultaneously.",
                      vis=F("grid", [(2, 5), (3, 3.5)], ["A", "B"], -1, 6, -1, 7, [],
                            "the two lines meet at (3, 3.5)"),
                      reasoning="The coefficients of y are opposites, so adding the equations "
                               "removes y in one step.",
                      steps=["Adding: (3x + 2y) + (5x − 2y) = 16 + 8, so 8x = 24.",
                             "Hence x = 3.",
                             "Substituting into the first equation: 9 + 2y = 16, so 2y = 7.",
                             "Hence y = 3.5.",
                             "Check in the second: 15 − 7 = 8."],
                      ans="x = 3, y = 3.5",
                      interp="Choosing to add rather than subtract is the whole skill of "
                             "elimination, and it is decided by looking at the coefficients "
                             "before starting."),
                 dict(q="A cinema sells 200 tickets for 1560 dollars. Adult tickets cost 10 "
                        "dollars and child tickets 6 dollars. Find how many of each were sold.",
                      vis=F("table", [["quantity", "equation", "value"],
                                      ["adults", "a", "to find"],
                                      ["children", "c", "to find"],
                                      ["total tickets", "a + c = 200", "200"],
                                      ["total money", "10a + 6c = 1560", "1560"]],
                            caption="Two conditions, two equations."),
                      reasoning="Write one equation for the number of tickets and one for the "
                               "money, then eliminate.",
                      steps=["Let a be the number of adults and c the number of children.",
                             "a + c = 200 and 10a + 6c = 1560.",
                             "Multiplying the first by 6 gives 6a + 6c = 1200.",
                             "Subtracting from the second gives 4a = 360, so a = 90.",
                             "Then c = 200 − 90 = 110."],
                      ans="90 adult tickets and 110 child tickets",
                      interp="The two conditions are independent, so the system has one "
                             "solution, and the check is that both totals are matched."),
             ], inv=dict(
                 task="Take five pairs of linear equations: one with a clean elimination, one "
                      "needing substitution, one with parallel lines, one with the same line "
                      "twice, and one of your own. Solve each, and record what the pair of "
                      "lines looks like as a graph.",
                 table=[["pair", "result", "lines"],
                        ["x + y = 5, x − y = 1", "x = 3, y = 2", "cross once"],
                        ["2x + y = 7, y = 3", "x = 2, y = 3", "cross once"],
                        ["x + y = 4, x + y = 7", "no solution", "parallel"],
                        ["2x + 2y = 6, x + y = 3", "infinitely many", "the same line"],
                        ["3x − y = 2, 6x − 2y = 5", "no solution", "parallel"]],
                 notice=["Every consistent pair with different gradients gave exactly one "
                         "solution.",
                         "The parallel pairs gave no solution, because no point lies on both "
                         "lines.",
                         "The pair with proportional equations gave infinitely many solutions.",
                         "Substitution was easier when one equation already had a subject."],
                 obs="Two linear equations in two unknowns have one solution, no solution, or "
                     "infinitely many, according to whether their lines cross, are parallel, "
                     "or coincide.",
                 concl="The number of solutions of a linear system is a property of the pair of "
                       "lines, so the algebraic answer and the graphical answer must always "
                       "agree.")),
        dict(id="3.5", title="Modelling with systems",
             inquiry_q="How does a real constraint become an equation, and what does the "
                       "solution mean?",
             teach=[
                 "A linear model has a fixed part and a part that changes with the quantity. Writing it as y = mx + c separates the two, and the intercept is the value at zero.",
                 "Break-even is where cost equals revenue, so the model is an equation. Profit is where revenue exceeds cost, so the model is an inequality.",
                 "Mixture problems are conservation problems: the total amount and the total value are both unchanged, which gives two equations.",
                 "Allocation problems divide a limited resource under several conditions, and the conditions are the equations. The solution is feasible only if every variable is non-negative, which the algebra does not know.",
             ], examples=[
                 dict(q="A print shop charges a setup fee of 40 dollars plus 2 dollars per "
                        "poster. A rival charges 6 dollars per poster with no fee. Find the "
                        "number of posters at which the two shops charge the same, and say "
                        "which is cheaper for 30 posters.",
                      vis=F("grid", [(10, 60), (15, 70)], ["A", "B"], 0, 25, 0, 160,
                            [(0, 40), (25, 90)],
                            "the two cost lines cross at 10 posters"),
                      reasoning="Write each cost as a linear model and solve the equation that "
                               "sets them equal.",
                      steps=["The first shop charges C₁ = 40 + 2n and the second C₂ = 6n.",
                             "Setting them equal: 40 + 2n = 6n.",
                             "So 40 = 4n and n = 10.",
                             "For 30 posters the first shop charges 100 dollars and the second "
                             "180 dollars.",
                             "So the first shop is cheaper for 30 posters."],
                      ans="the shops charge the same at 10 posters; the first is cheaper for 30",
                      interp="The break-even point is where two models agree, and the cheaper "
                             "option is decided by which side of that point the order lies on."),
                 dict(q="A 40% saline solution is mixed with a 10% solution to make 300 ml of "
                        "a 25% solution. Find the volume of each.",
                      vis=F("bar_model", 300, [120, 180], ["40%", "10%"],
                            "the two parts make 300 ml"),
                      reasoning="The total volume and the total amount of salt are both "
                               "conserved, which gives two equations.",
                      steps=["Let x be the volume of the 40% solution and y the volume of the "
                             "10% solution.",
                             "x + y = 300.",
                             "0.40x + 0.10y = 0.25 × 300 = 75.",
                             "Multiplying the first by 0.10 and subtracting gives 0.30x = 45.",
                             "So x = 150 and y = 150."],
                      ans="150 ml of each",
                      interp="The two conserved quantities give two equations, and the solution "
                             "is feasible only because both volumes came out positive."),
             ], inv=dict(
                 task="Find three real situations that can be modelled by a linear equation or "
                      "a system: one cost comparison, one mixture or recipe, and one "
                      "allocation. Model each, solve it, and test whether the solution is "
                      "physically possible.",
                 table=[["situation", "model", "solution", "feasible?"],
                        ["two phone plans", "15 + 0.5n = 30 + 0.2n", "n = 50", "yes"],
                        ["nut mix", "x + y = 500, 8x + 5y = 3200", "x = 233, y = 267", "yes"],
                        ["shift roster", "a + b = 40, 6a + 4b = 200", "a = 20, b = 20", "yes"],
                        ["over-budget trip", "x + y = 10, 30x + 12y = 400", "x = 11.1", "no"]],
                 notice=["Every feasible solution had all variables non-negative.",
                         "The over-budget trip gave a negative value for the cheaper option, "
                         "so the model said the budget was impossible.",
                         "The mixture models always conserved both total and value.",
                         "The model's failure was informative, not a mistake."],
                 obs="A linear model turns a constraint into an equation, and the algebra "
                     "returns a solution whose physical sense must still be checked.",
                 concl="A solution is acceptable only when it satisfies every constraint of the "
                       "situation, including the ones the equations do not express.")),
        dict(id="3.6", title="Investigation: break-even and beyond",
             inquiry_q="When two linear models are compared, where do they agree, and what "
                       "does the comparison decide?",
             teach=[
                 "Two linear models of the same quantity agree where their graphs cross, and the crossing point is found by solving the equation obtained by setting them equal. That point is the break-even point of the comparison.",
                 "On one side of the crossing point one model is larger and on the other side the other is, so the better choice depends on where the quantity being compared lies.",
                 "A comparison is only complete when the period of use is stated, because a model that is cheaper for a short period can be dearer for a long one.",
                 "A model makes the consequences of a choice visible. It does not make the choice, and a modeller who hides the assumption on which the choice rests is not being honest.",
             ], examples=[
                 dict(q="A print shop charges 45 dollars for a call-out plus 2 dollars per "
                        "poster. A rival charges 6 dollars per poster with no fee. Find the "
                        "number of posters at which the two shops charge the same, and say "
                        "which is cheaper for 30 posters.",
                      vis=F("grid", [(11.25, 67.5), (30, 105), (30, 180)],
                            ["break-even", "shop 1", "shop 2"], 0, 35, 0, 220,
                            [(0, 45), (30, 105)],
                            "the two cost lines cross at 11.25 posters"),
                      reasoning="Write each cost as a linear model and solve the equation that "
                               "sets them equal.",
                      steps=["The first shop charges C₁ = 45 + 2n and the second C₂ = 6n.",
                             "Setting them equal: 45 + 2n = 6n.",
                             "So 45 = 4n and n = 11.25.",
                             "For fewer than 11.25 posters the second shop is cheaper; for "
                             "more, the first is.",
                             "For 30 posters the first shop charges 105 dollars and the "
                             "second 180 dollars, so the first is cheaper."],
                      ans="the shops charge the same at 11.25 posters; the first is cheaper "
                          "for 30",
                      interp="The break-even point is where two models agree, and the cheaper "
                             "option is decided by which side of that point the order lies "
                             "on."),
                 dict(q="A school has 60 hours of tutoring to share between three year groups. "
                        "Year 9 needs at least 10 hours, Year 10 at least 15, and Year 11 at "
                        "most 25. Model the situation and find the feasible region.",
                      vis=F("grid", [(10, 15, 35), (10, 25, 25), (25, 15, 20)],
                            ["A", "B", "C"], 0, 30, 0, 30,
                            [(10, 15), (10, 25), (25, 15)],
                            "three constraints meet in a region"),
                      reasoning="Write the total as an equation and each condition as an "
                               "inequality, then find the region.",
                      steps=["Let x, y and z be the hours for Years 9, 10 and 11.",
                             "x + y + z = 60, with x ≥ 10, y ≥ 15 and z ≤ 25.",
                             "Substituting z = 60 − x − y gives x ≥ 10, y ≥ 15 and x + y ≥ 35.",
                             "The feasible region is a triangle in the (x, y) plane with "
                             "vertices (10, 25), (25, 15) and (10, 15).",
                             "Equal shares would be (20, 20, 20), which is feasible."],
                      ans="the feasible region is a triangle, and equal shares are feasible",
                      interp="The model shows which shares are possible; it does not say which "
                             "is fair, because that depends on a criterion the model does not "
                             "contain.")
             ], inv=dict(
                 task="Choose a limited resource that matters to you — money, time, space or "
                      "food. Model the sharing with one equation and at least two inequalities, "
                      "draw the feasible region, and then choose a point using a stated "
                      "criterion. Defend the criterion in writing.",
                 table=[["criterion", "point chosen", "why"],
                        ["equal shares", "the centre of the region", "everyone gets the same"],
                        ["greatest need", "a vertex", "the largest share goes to the greatest "
                         "need"],
                        ["least disruption", "the point nearest the current share", "change is "
                         "costly"],
                        ["maximum total benefit", "a vertex", "a linear objective is optimised "
                         "at a vertex"]],
                 notice=["Every criterion chose a different point of the same region.",
                         "The region itself was the same, so the mathematics was neutral.",
                         "The choice of criterion was a judgement, not a calculation.",
                         "Some criteria gave points on the boundary and some gave interior "
                         "points."],
                 obs="A model of a shared resource produces a feasible region, and the point "
                     "chosen within it is decided by a criterion that comes from outside the "
                     "model.",
                 concl="Mathematics can show which allocations are possible and what each "
                       "criterion would choose, but the choice of criterion is a decision about "
                       "values that the model itself cannot make.")),
    ],
    practice=dict(
        A=[("3.1.1", "Solve 4x − 7 = 21.", "x = 7", "Add 7, then divide by 4.", "F"),
           ("3.1.2", "Solve 5 − 3x = 17.", "x = −4", "Collect, then divide by −3 and reverse "
            "the sign.", "F"),
           ("3.1.3", "Solve 2(x + 3) = 5(x − 1).", "x = 11/3", "Expand both sides, then collect.",
            "F"),
           ("3.1.4", "Solve x/4 + 2 = 5.", "x = 12", "Multiply by 4, then subtract 8.", "F"),
           ("3.1.5", "Solve the pair x + y = 9 and x − y = 3.", "x = 6, y = 3",
            "Add the equations to eliminate y.", "F"),
           ("3.1.6", "Solve the pair 2x + y = 11 and x − y = 1.", "x = 4, y = 3",
            "Add the equations to eliminate y.", "F"),
           ("3.1.7", "Solve 3x + 4 < 19 and show the solution on a number line.", "x < 5",
            "Subtract 4, then divide by 3.", "F"),
           ("3.1.8", "Solve −2x ≥ 10.", "x ≤ −5",
            "Divide by −2 and reverse the sign.", "F"),
           ("3.1.9", "Solve the pair y = 2x and y = x + 3.", "x = 3, y = 6",
            "Substitute the first into the second.", "F"),
           ("3.1.10", "Solve 7 − 2x ≤ 1.", "x ≥ 3",
            "Collect, then divide by −2 and reverse.", "F"),
           ("3.1.11", "Solve (x − 1)/3 = (x + 2)/5.", "x = 5.5",
            "Multiply through by 15, then collect.", "F"),
           ("3.1.12", "Solve 4(x − 2) = 2(x + 5).", "x = 9", "Expand, then collect.", "F")],
        B=[("3.2.1", "The number of diagonals of an n-sided polygon is n(n − 3)/2. Find n for a "
            "polygon with 20 diagonals and justify the rejection of the second root.",
            "n = 8; the other root is negative, so it is not a polygon.", "Solve the quadratic "
            "and test both roots.", "R"),
           ("3.2.2", "Investigate the pattern in the sums 1 + 3 + 5 + … for 1, 2, 3 and 4 "
            "terms, and justify the general rule.",
            "The sums are 1, 4, 9, 16, so the sum of the first n odd numbers is n².",
            "Relate to the difference of consecutive squares.", "R"),
           ("3.2.3", "Conjecture a rule for the number of handshakes among n people and test "
            "it for n = 3, 4, 5.",
            "n(n − 1)/2, giving 3, 6, 10.", "Each pair shakes once.", "R"),
           ("3.2.4", "Investigate the sequence of perimeters of rectangles with sides n and "
            "n + 3 and find its rule.",
            "4n + 6, an arithmetic sequence with common difference 4.",
            "Add the four sides.", "R"),
           ("3.2.5", "Build a table of solutions to x + 2y = 12 for whole numbers and describe "
            "the pattern.",
            "The solutions fall by 1 in x and by 0.5 in y, all lying on one line.",
            "Solve for y and vary x.", "R"),
           ("3.2.6", "Conjecture a rule for the number of matches needed to make a row of n "
            "squares and justify it.",
            "3n + 1, because each new square shares one side.", "Count for n = 1, 2, 3.", "R"),
           ("3.2.7", "Investigate the pattern in the number of intersection points of n lines "
            "in general position.",
            "n(n − 1)/2, because each pair of lines meets once.",
            "Count for n = 2, 3, 4.", "R"),
           ("3.2.8", "A pattern of dots gives 4, 9, 16, 25 for figures 1 to 4. Find the rule "
            "and test it on figure 7.",
            "(n + 1)², giving 64 for figure 7.", "Take differences to identify a quadratic.",
            "R"),
           ("3.2.9", "Investigate the areas of the rectangles with perimeter 24 and find the "
            "shape of greatest area.",
            "The greatest area is 36, at the square 6 by 6.",
            "Write the area as a quadratic and find its vertex.", "R"),
           ("3.2.10", "Conjecture a rule for the number of diagonals from one vertex of an "
            "n-sided polygon.",
            "n − 3, because the vertex joins to all but itself and its two neighbours.",
            "Count for several polygons.", "R"),
           ("3.2.11", "Investigate the pattern in 2ⁿ − 1 for n = 1 to 6 and describe what you "
            "find.",
            "1, 3, 7, 15, 31, 63; each is one less than a power of two, and several are prime.",
            "Compute the values and test for factors.", "R")],
        C=[("3.3.1", "Explain in your own words what it means to solve an equation.",
            "To find every value of the unknown that makes the statement true, and to show that "
            "no other value does.", "State the definition and its strength.", "R"),
           ("3.3.2", "Write a complete solution to 3(2x − 1) = 4(x + 5), labelling each step.",
            "x = 11.5", "Expand, collect, then divide.", "F"),
           ("3.3.3", "Choose between solving graphically and solving algebraically for a pair "
            "of equations and justify.", "Algebraically for exact values; graphically for a "
            "quick check or for a system of inequalities.", "Say what each method gives.", "R"),
           ("3.3.4", "Set out a full solution to the pair 3x + 2y = 12 and x − y = 1.",
            "x = 14/5, y = 9/5", "Substitute x = y + 1 into the first equation.", "F"),
           ("3.3.5", "Explain why multiplying an inequality by a negative number reverses the "
            "sign.", "Because the order of numbers is reversed by multiplying by a negative, "
            "so the larger side becomes the smaller.", "Test with numbers.", "R"),
           ("3.3.6", "Describe, with an example, the difference between no solution and "
            "infinitely many solutions.", "No solution: the lines are parallel, as x + y = 1 "
            "and x + y = 3. Infinitely many: the lines coincide, as x + y = 1 and 2x + 2y = 2.",
            "Compare the gradients and intercepts.", "R"),
           ("3.3.7", "Explain why the solution of a system of inequalities is a region.",
            "Because each inequality allows infinitely many values, and the system keeps those "
            "that satisfy all of them, which is a region.", "Draw a simple case.", "R"),
           ("3.3.8", "Write the reasoning that shows two equations with the same left-hand "
            "side have no solution.", "If ax + by = p and ax + by = q with p ≠ q, then "
            "subtracting gives 0 = p − q, which is false.", "Subtract the equations.", "R"),
           ("3.3.9", "Set out the argument that the optimum of a linear function over a "
            "polygon occurs at a vertex.", "A linear function has no interior maximum, so its "
            "extreme values on a polygon occur where the boundary changes direction.",
            "Test with a triangle.", "R"),
           ("3.3.10", "Explain what the intercept of a linear model represents in a real "
            "situation.", "The value of the quantity when the variable is zero — the fixed "
            "charge, the starting amount, or the initial reading.", "Give a real example.", "R"),
           ("3.3.11", "Describe the relationship between the algebraic and graphical solutions "
            "of a pair of linear equations.", "They are the same answer: the algebraic "
            "solution is the coordinates of the point where the two lines cross.",
            "Solve both ways for one pair.", "R"),
           ("3.3.12", "Explain, with an example, why a feasible solution must be checked "
            "against the situation.", "Because an equation may allow negative or fractional "
            "values that the situation does not, as with a negative number of books.",
            "Model one case and check.", "R")],
        D=[("3.4.1", "A phone plan costs 15 dollars plus 0.05 dollars per minute. Another costs "
            "40 dollars with unlimited minutes. Find the number of minutes at which the two "
            "plans cost the same, and say which is cheaper for 400 minutes.",
            "The plans cost the same at 500 minutes; the first is cheaper for 400 minutes.",
            "Set the two linear models equal.", "A"),
           ("3.4.2", "A charity has 500 dollars to spend on 40 food parcels. A small parcel "
            "costs 10 dollars and a large one 15. Find how many of each it can buy.",
            "20 small and 20 large parcels.", "Two conditions, two equations.", "A"),
           ("3.4.3", "A farmer mixes feed at 12 dollars per kg with feed at 8 dollars per kg "
            "to make 200 kg at 10 dollars per kg. Find the mass of each.",
            "100 kg of each.", "Conserve the total mass and the total cost.", "A"),
           ("3.4.4", "A taxi charges 4 dollars plus 2.50 dollars per km. A bus costs 1.20 "
            "dollars per km with no fixed charge. Find the distance at which the taxi is "
            "cheaper and state the answer for a 6 km trip.",
            "The taxi is cheaper up to about 3.08 km, so for 6 km the bus is cheaper.",
            "Set the two models equal.", "A"),
           ("3.4.5", "A print shop has 60 hours of machine time and needs at least 20 jobs of "
            "type A and at most 30 of type B. Model the situation and find the feasible range "
            "for the number of type A jobs.",
            "The feasible range is 30 to 60 type A jobs, depending on the mix.",
            "Write the total as an equation and the conditions as inequalities.", "R"),
           ("3.4.6", "A school canteen sells 120 meals for 900 dollars. A student meal costs "
            "6 dollars and an adult meal 9 dollars. Find how many of each were sold.",
            "60 student and 60 adult meals.", "Two conditions, two equations.", "A"),
           ("3.4.7", "A builder has 40 m of fencing and wants a rectangular pen of area at "
            "least 96 m². Find the feasible range of widths and the dimensions of greatest "
            "area.",
            "Widths from 4 to 16 m give area at least 96 m²; the greatest area is 100 m² at 10 "
            "m by 10 m.", "Write the area as a quadratic in the width.", "A"),
           ("3.4.8", "A coach company charges 200 dollars plus 12 dollars per passenger. A "
            "group of 30 has a budget of 700 dollars. Is the trip affordable, and what is the "
            "largest group possible?",
            "The cost for 30 is 560 dollars, so it is affordable; the largest group is 41.",
            "Model the cost and solve the inequality.", "A"),
           ("3.4.9", "A chemist mixes a 30% acid solution with a 60% solution to make 500 ml "
            "at 45%. Investigate whether this is possible and justify.",
            "Yes, 250 ml of each, because the target is exactly halfway between the two "
            "concentrations.", "Conserve volume and acid.", "R"),
           ("3.4.10", "A farm has 100 hectares and at least 40 hectares of maize. Wheat needs "
            "3 workers per hectare and maize 5, with 420 workers available. Model the "
            "situation and find the feasible region.",
            "The feasible region runs from 40 to 60 hectares of maize.",
            "Write the land and labour constraints.", "A"),
           ("3.4.11", "A bakery sells loaves at 3 dollars and rolls at 0.50 dollars. It sold "
            "200 items for 400 dollars. Investigate whether the figures are consistent.",
            "They are not: solving gives 120 loaves and 80 rolls, which does give 400 dollars, "
            "so they are consistent.", "Solve and check.", "R"),
           ("3.4.12", "Explain, with a model of your own, when a linear model is a poor "
            "description of a situation.", "Any answer is acceptable if it identifies "
            "diminishing returns, a fixed capacity, or a threshold that a straight line cannot "
            "show.", "Give a specific counterexample.", "R")],
    ),
    assessment=[
        dict(title="A1 · The shared budget",
             text="A community centre has 600 dollars and 40 m² of floor space to set up a "
                  "study area and a play area. Each square metre of study area costs 12 dollars "
                  "and each square metre of play area costs 15 dollars. The play area must be at "
                  "least 10 m² and the study area at least 15 m². Model the situation, find the "
                  "feasible region, and recommend one allocation with a stated reason.",
             note="Criteria A and D · state the constraints, solve the system, and justify the "
                  "allocation you recommend."),
        dict(title="A2 · The two suppliers",
             text="Two suppliers quote for printed programmes. Supplier A charges 150 dollars "
                  "plus 0.80 dollars per copy; supplier B charges 60 dollars plus 1.20 dollars "
                  "per copy. Find the number of copies at which the quotes are equal, say which "
                  "supplier is cheaper for 300 copies, and find the largest number of copies "
                  "affordable within a 900 dollar budget.",
             note="Criteria A and C · model both quotes, solve the equation, and solve the "
                  "inequality."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of equivalence, "
        "change and system appear in your work?",
        "How is the global context of fairness and development, and its exploration of "
        "collective decisions under constraints, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a linear model for a decision about sharing, and what would "
        "you still like to ask?",
    ],
    review=dict(
        ideas=["Solving an equation uses reversible steps only.",
               "Dividing an inequality by a negative number reverses the sign.",
               "The solution of an inequality is an interval, not a value.",
               "Two linear equations in two unknowns have one, none, or infinitely many "
               "solutions.",
               "The solution of a pair of equations is the intersection of two lines.",
               "A system of inequalities describes a feasible region.",
               "The optimum of a linear model over a region occurs at a vertex.",
               "A feasible solution must still be physically possible."],
        vocab=["equation", "inequality", "simultaneous", "elimination", "substitution",
               "feasible region", "vertex", "break-even", "linear model", "interval",
               "half-plane", "constraint"],
        mixed=[("3.R1", "Solve 5x − 3 = 2x + 12."),
               ("3.R2", "Solve 3 − 4x > 11."),
               ("3.R3", "Solve the pair 2x + 3y = 16 and x − y = 2."),
               ("3.R4", "Find the feasible region for x ≥ 1, y ≥ 2 and x + y ≤ 8."),
               ("3.R5", "Solve (2x − 1)/4 = (x + 3)/3."),
               ("3.R6", "Explain why x + y = 2 and 2x + 2y = 5 have no solution.")],
    ),
    projects=dict(
        service=[("Community need", "Shared budgets and shared spaces are allocated without "
                                    "showing the constraints behind them."),
                 ("Mathematical connection", "Linear equations, inequalities and feasible "
                                             "regions."),
                 ("Proposed action", "Model one real allocation and publish the feasible "
                                     "choices with the reasoning."),
                 ("Expected impact", "A group can see which choices are possible before it "
                                     "argues about which is best."),
                 ("Student reflection", "Record the model, the region and what you chose.")],
        community=[("Project idea", "A fairness audit of one school allocation."),
                   ("Need", "Budgets, rooms and time are divided without stated criteria."),
                   ("Research question", "Which allocations are feasible, and what does each "
                                         "criterion choose?"),
                   ("Mathematics", "Linear models, systems and feasible regions."),
                   ("Action or outcome", "A one-page report with the model and two "
                                         "recommendations."),
                   ("Beneficiaries", "Everyone affected by the allocation."),
                   ("Evidence", "The report with the region and the criteria compared.")],
        personal=[("Personal interest", "Money, time or a team you belong to."),
                  ("Learning goal", "To model a limited resource and state a criterion for "
                                    "sharing it."),
                  ("Product or outcome", "A model with a feasible region and a defended "
                                         "choice."),
                  ("Mathematics", "Linear equations and inequalities."),
                  ("Process", "State the constraints, solve, and choose a point with a stated "
                              "criterion."),
                  ("Evidence", "The model, the region and the written defence.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=4, title="Functions, Coordinates and Linear Models",
    key="Form", related=["Representation", "Change", "Pattern"],
    context="Orientation in space and time",
    exploration="Maps, routes and rates",
    inquiry=("A function is a rule that gives exactly one output for each permitted input, and "
             "the form of that rule decides what can be read from it — a graph shows change, a "
             "table shows values, and an equation shows structure — so the same relationship "
             "can be represented in several ways, each of which answers a different question."),
    atl=("Thinking",
         "Students identify the key features of a linear function from its graph, its table "
         "and its equation, and explain which representation is most efficient for the "
         "question asked."),
    standfirst="A coordinate turns a location into a pair of numbers. A function turns a rule "
               "into a table, a graph and an equation, and all three describe the same "
               "relationship.",
    engage="A delivery rider travels 12 km in 40 minutes. Where is she after 15 minutes, how "
           "fast is she going, and which representation of the journey answers each question "
           "most easily?",
    questions=[("Factual", "What is a function, and what are the gradient and intercept of a "
                           "linear function?"),
               ("Conceptual", "Why do the table, graph and equation of a function describe the "
                              "same relationship, and what does the gradient tell you about "
                              "change?"),
               ("Debatable", "Is a graph a picture of reality or a model of it, and what is "
                             "lost when a journey is drawn as a straight line?")],
    application_lede="Each task asks you to move between representations. Say which "
                     "representation you are using and why it answers the question.",
    projects_lede="A route, a rate or a map is a function in disguise. Model one and show "
                  "which representation answers the question you care about.",
    sections=[
        dict(id="4.1", title="Functions and function notation",
             inquiry_q="What makes a rule a function, and what does function notation add?",
             teach=[
                 "A function is a rule that gives exactly one output for each permitted input. The permitted inputs form the domain and the possible outputs form the range.",
                 "Function notation f(x) names the rule f and the input x together, so f(3) means the output when the input is 3. The letter is a label, not a multiplier.",
                 "A function can be given as a formula, a table, a graph or a description in words, and all four are the same function if they agree on every input of the domain.",
                 "The vertical line test decides whether a graph is a function: a vertical line that meets the graph twice would give one input two outputs, which is not allowed.",
                 "A function is a representation of a relation between two quantities, and a formula, a graph and a table are different representations of the same function. Each representation makes some questions easy and others hard, so a modeller chooses deliberately.",
             ], examples=[
                 dict(q="A function is given by f(x) = 3x − 4. Find f(2), f(−1) and f(0), and "
                        "find x when f(x) = 11.",
                      vis=F("function_machine", [(2, 2), (-1, -7), (0, -4), (5, 11)],
                            "3x − 4", "inputs on the left, outputs on the right"),
                      reasoning="Substitute each input into the rule, and solve the equation for "
                               "the inverse question.",
                      steps=["f(2) = 3(2) − 4 = 2.",
                             "f(−1) = 3(−1) − 4 = −7.",
                             "f(0) = 3(0) − 4 = −4.",
                             "Setting 3x − 4 = 11 gives 3x = 15, so x = 5.",
                             "The outputs rise by 3 for every rise of 1 in the input."],
                      ans="f(2) = 2, f(−1) = −7, f(0) = −4, and f(x) = 11 at x = 5",
                      interp="Finding an output is substitution; finding the input is solving an "
                             "equation, and the two questions are different."),
                 dict(q="Decide whether the relation g = {(1, 2), (2, 4), (3, 2), (4, 8)} is a "
                        "function, and state its domain and range.",
                      vis=F("table", [["input", "output"],
                                      ["1", "2"],
                                      ["2", "4"],
                                      ["3", "2"],
                                      ["4", "8"]],
                            caption="Each input appears once, so the relation is a function."),
                      reasoning="Check that no input is paired with two different outputs.",
                      steps=["The inputs are 1, 2, 3 and 4, each appearing exactly once.",
                             "So every permitted input has exactly one output, and g is a "
                             "function.",
                             "The domain is {1, 2, 3, 4}.",
                             "The range is {2, 4, 8}, because the output 2 occurs twice.",
                             "The range is smaller than the domain, which is allowed."],
                      ans="g is a function with domain {1, 2, 3, 4} and range {2, 4, 8}",
                      interp="Two inputs may share an output, but one input may not have two, "
                             "and that asymmetry is the definition."),
             ], inv=dict(
                 task="Collect five rules from everyday life: a bus fare, a phone charge, a "
                      "recipe, a sports score and one of your own. For each, state the domain, "
                      "the range, and whether the rule is a function. Then write each as a "
                      "formula where you can.",
                 table=[["rule", "domain", "range", "function?"],
                        ["bus fare 2.50 per ride", "rides", "money", "yes"],
                        ["bus fare capped at 5.00", "rides", "money", "yes"],
                        ["square of a number", "all numbers", "non-negative numbers", "yes"],
                        ["square root of a number", "non-negative numbers", "non-negative "
                         "numbers", "yes"],
                        ["a person's height", "people", "heights", "no, changes with time"]],
                 notice=["Every rule that gave one output per input was a function.",
                         "The capped bus fare was still a function, though not a linear one.",
                         "Height was not a function of the person, because it changes with time.",
                         "Adding time to the domain made height a function again."],
                 obs="Whether a rule is a function depends on the domain chosen, and the same "
                     "quantity can be a function of one variable and not of another.",
                 concl="A function is a rule with exactly one output for each permitted input, "
                       "and the domain is part of the definition rather than an afterthought.")),
        dict(id="4.2", title="Distance and midpoint",
             inquiry_q="How is the distance between two points found from their coordinates?",
             teach=[
                 "The distance between two points is found from the differences of their coordinates. When the points share a coordinate the distance is simply the difference of the other one.",
                 "In general the horizontal and vertical differences are the legs of a right-angled triangle whose hypotenuse is the distance, so Pythagoras' theorem gives the distance formula.",
                 "The midpoint of two points is found by averaging each coordinate, and it is the point equidistant from both. It is also the centre of symmetry of the segment.",
                 "A coordinate turns a location into a pair of numbers, and that is what makes distance and midpoint calculable rather than measurable, which is the whole advantage of coordinates.",
             ], examples=[
                 dict(q="Find the distance and the midpoint of A(−3, 2) and B(5, 10).",
                      vis=F("grid", [(-3, 2), (5, 10), (1, 6)], ["A", "B", "midpoint"], -5, 8, 0,
                            13, [(-3, 2), (5, 10)],
                            "the segment from A to B"),
                      reasoning="Take the differences for the legs, apply Pythagoras, and "
                               "average the coordinates for the midpoint.",
                      steps=["The horizontal difference is 5 − (−3) = 8 and the vertical "
                             "difference is 10 − 2 = 8.",
                             "So the distance is √(8² + 8²) = √128 = 8√2 ≈ 11.31.",
                             "The midpoint is ((−3 + 5)/2, (2 + 10)/2) = (1, 6).",
                             "The midpoint lies on the segment, halfway along it.",
                             "Check: the distance from A to the midpoint is also 8√2/2."],
                      ans="distance 8√2 ≈ 11.31, midpoint (1, 6)",
                      interp="One calculation gives the length of a segment that could not be "
                             "measured directly, which is why coordinates are used."),
                 dict(q="The points P(2, 5), Q(6, 1) and R form a straight line with Q the "
                        "midpoint of PR. Find R.",
                      vis=F("grid", [(2, 5), (6, 1), (10, -3)], ["P", "Q", "R"], 0, 12, -5, 8,
                            [(2, 5), (6, 1), (10, -3)],
                            "Q is the midpoint of PR"),
                      reasoning="Use the midpoint formula in reverse: the midpoint is the "
                               "average of the endpoints.",
                      steps=["If Q is the midpoint of P and R, then Q = (P + R)/2.",
                             "So R = 2Q − P, coordinate by coordinate.",
                             "The x-coordinate is 2(6) − 2 = 10.",
                             "The y-coordinate is 2(1) − 5 = −3.",
                             "So R is (10, −3), and the three points are collinear."],
                      ans="R is (10, −3)",
                      interp="The midpoint formula can be read backwards, and reading it "
                             "backwards finds an endpoint from a midpoint."),
             ], inv=dict(
                 task="Take five pairs of points of your own, including one pair sharing a "
                      "coordinate, one pair on a diagonal and one pair in different quadrants. "
                      "For each, find the distance and the midpoint, and check the midpoint by "
                      "measuring on squared paper.",
                 table=[["pair", "distance", "midpoint"],
                        ["(0, 0), (6, 8)", "10", "(3, 4)"],
                        ["(1, 1), (1, 9)", "8", "(1, 5)"],
                        ["(−2, 3), (4, −1)", "√52 ≈ 7.21", "(1, 1)"],
                        ["(−5, −5), (5, 5)", "√200 ≈ 14.14", "(0, 0)"],
                        ["(2, −3), (8, 5)", "√116 ≈ 10.77", "(5, 1)"]],
                 notice=["The pair sharing a coordinate gave a distance that was a simple "
                         "difference.",
                         "Every other pair needed Pythagoras on the two differences.",
                         "The midpoint coordinates were always the averages.",
                         "The midpoint always lay on the segment, as the check confirmed."],
                 obs="The distance between two points comes from Pythagoras applied to the "
                     "coordinate differences, and the midpoint comes from averaging them.",
                 concl="Coordinates make distance and midpoint calculable, and the two "
                       "quantities are found from the same pair of differences.")),
        dict(id="4.3", title="Gradient and equations of lines",
             inquiry_q="What does the gradient of a line measure, and how is it read from an "
                       "equation?",
             teach=[
                 "The gradient of a line is the change in y for a unit change in x. It is the rate at which the output changes as the input changes, and it is the same everywhere on a straight line.",
                 "The equation y = mx + c gives the gradient as m and the intercept as c directly. Parallel lines have equal gradients and perpendicular lines have gradients whose product is −1.",
                 "A gradient of zero is a horizontal line, and a vertical line has no gradient because the change in x is zero. A line with an undefined gradient is not the graph of a function of x.",
                 "The gradient is the slope of a real rate: speed, cost per item, or change per year. Reading it from an equation is the fastest way to interpret a model.",
                 "A straight line is the picture of a constant pattern of change: equal steps in the input give equal steps in the output. When the steps stop being equal, the graph bends and the model is no longer linear.",
             ], examples=[
                 dict(q="A line has equation 3x + 4y = 20. Find its gradient, its intercepts, "
                        "and the gradient of a line perpendicular to it.",
                      vis=F("grid", [(0, 5), (20/3, 0)], ["A", "B"], -1, 8, -1, 7,
                            [(0, 5), (20/3, 0)],
                            "the line 3x + 4y = 20"),
                      reasoning="Rearrange into y = mx + c, then read the gradient and use the "
                               "perpendicular rule.",
                      steps=["3x + 4y = 20 gives 4y = −3x + 20, so y = (−3/4)x + 5.",
                             "The gradient is −3/4 and the intercept is 5.",
                             "The x-intercept is at y = 0, so 3x = 20 and x = 20/3.",
                             "A perpendicular line has gradient 4/3, because (−3/4)(4/3) = −1.",
                             "Both intercepts are positive, so the line falls through the first "
                             "quadrant."],
                      ans="gradient −3/4, intercepts (0, 5) and (20/3, 0), perpendicular "
                          "gradient 4/3",
                      interp="Rearranging into gradient-intercept form makes the two key "
                             "features visible without any drawing."),
                 dict(q="A cyclist's distance from home is d = 6t + 2, with t in hours. Find "
                        "the distance at the start, the speed, and the time to reach 50 km.",
                      vis=F("double_number_line", "time in hours", "distance in km",
                            "each hour adds 6 km"),
                      reasoning="Read the intercept and gradient from the equation, then solve "
                               "for the required time.",
                      steps=["At t = 0 the distance is d = 2 km, so she starts 2 km from home.",
                             "The gradient is 6, so her speed is 6 km/h.",
                             "Setting 6t + 2 = 50 gives 6t = 48, so t = 8 hours.",
                             "The straight line assumes a constant speed with no stops.",
                             "The model is therefore a simplification of any real journey."],
                      ans="2 km at the start, 6 km/h, 8 hours to reach 50 km",
                      interp="The two numbers in the equation are the two facts about the "
                             "journey: where it began and how fast it moved."),
             ], inv=dict(
                 task="Take six linear equations of your own: three in the form y = mx + c and "
                      "three in another form. For each, find the gradient and the intercepts, "
                      "then draw the six lines on one pair of axes and group them by gradient.",
                 table=[["equation", "gradient", "y-intercept", "x-intercept"],
                        ["y = 2x + 1", "2", "1", "−0.5"],
                        ["y = −2x + 1", "−2", "1", "0.5"],
                        ["y = 0.5x − 3", "0.5", "−3", "6"],
                        ["x + y = 5", "−1", "5", "5"],
                        ["2x − 3y = 6", "2/3", "−2", "3"],
                        ["y = 4", "0", "4", "none"]],
                 notice=["Lines with the same gradient were parallel, whichever form they were "
                         "written in.",
                         "The intercepts decided where the line crossed the axes, not its "
                         "direction.",
                         "A horizontal line had a gradient of 0 and no x-intercept unless it "
                         "was the axis itself.",
                         "Rearranging every equation into the same form made the comparison "
                         "immediate."],
                 obs="The gradient and the intercepts of a line can be read from any form of "
                     "its equation once it has been rearranged, and together they fix the line "
                     "completely.",
                 concl="A straight line is determined by its gradient and one point, and "
                       "y = mx + c is the form that displays both without further work.")),
        dict(id="4.4", title="Parallel and perpendicular lines",
             inquiry_q="How do the gradients of two lines decide whether they are parallel or "
                       "perpendicular?",
             teach=[
                 "Two lines are parallel when they have the same gradient, and they are perpendicular when the product of their gradients is −1. Both statements follow from the meaning of gradient as change in y per unit change in x.",
                 "A vertical line has no gradient, so it is parallel to every other vertical line and perpendicular to every horizontal one. These are the two cases the product rule does not cover.",
                 "Rearranging an equation into y = mx + c makes the gradient visible, so the first step in any question about parallel or perpendicular lines is to rearrange.",
                 "The gradient of a line perpendicular to one of gradient m is −1/m, which is the negative reciprocal. This is the rule used to find the equation of a perpendicular through a given point.",
             ], examples=[
                 dict(q="Find the equation of the line through (2, 7) that is parallel to "
                        "3x + 4y = 20.",
                      vis=F("grid", [(2, 7), (6, 0.5)], ["on the new line", ""], -1, 8, 0, 10,
                            [(0, 5), (20/3, 0)],
                            "the parallel line through (2, 7)"),
                      reasoning="Find the gradient of the given line, then use it with the "
                               "point to find the new line.",
                      steps=["3x + 4y = 20 gives y = (−3/4)x + 5, so the gradient is −3/4.",
                             "A parallel line has the same gradient, so the new line is "
                             "y = (−3/4)x + c.",
                             "Substituting (2, 7) gives 7 = (−3/4)(2) + c, so c = 8.5.",
                             "Hence the line is y = (−3/4)x + 8.5, or 3x + 4y = 34.",
                             "The two lines never meet, which is what parallel means."],
                      ans="y = −¾x + 8.5, or 3x + 4y = 34",
                      interp="Parallel lines share a gradient, so one gradient and one point "
                             "fix the new line completely."),
                 dict(q="Find the equation of the line through (1, −2) that is perpendicular "
                        "to y = 2x + 5.",
                      vis=F("grid", [(1, -2), (2, 1)], ["on the new line", ""], -2, 4, -5, 5,
                            [(0, 5), (2.5, 0)],
                            "the perpendicular line through (1, −2)"),
                      reasoning="Take the negative reciprocal of the gradient, then use the "
                               "point.",
                      steps=["The gradient of y = 2x + 5 is 2.",
                             "A perpendicular line has gradient −1/2.",
                             "So the new line is y = (−1/2)x + c.",
                             "Substituting (1, −2) gives −2 = (−1/2)(1) + c, so c = −1.5.",
                             "Hence the line is y = −½x − 1.5, and the product of the "
                             "gradients is 2 × (−1/2) = −1."],
                      ans="y = −½x − 1.5",
                      interp="The negative reciprocal is the only gradient that makes the "
                             "product −1, and the check is the product itself."),
             ], inv=dict(
                 task="Take six lines of your own: three parallel pairs and three "
                      "perpendicular pairs. For each, rearrange into gradient-intercept form, "
                      "compute the product of the gradients, and record whether the pair is "
                      "parallel, perpendicular or neither.",
                 table=[["pair", "gradients", "product", "relation"],
                        ["y = 3x + 1, y = 3x − 4", "3, 3", "9", "parallel"],
                        ["y = −2x, y = −2x + 7", "−2, −2", "4", "parallel"],
                        ["y = x, y = −x + 3", "1, −1", "−1", "perpendicular"],
                        ["y = 2x, y = −½x", "2, −0.5", "−1", "perpendicular"],
                        ["y = 4x + 1, y = −¼x + 2", "4, −0.25", "−1", "perpendicular"]],
                 notice=["Every parallel pair had equal gradients.",
                         "Every perpendicular pair had a product of exactly −1.",
                         "The perpendicular gradient was always the negative reciprocal.",
                         "A vertical and a horizontal line are perpendicular, and the product "
                         "rule does not apply to them."],
                 obs="Parallel lines have equal gradients and perpendicular lines have "
                     "gradients whose product is −1, and both facts are read from the "
                     "gradient-intercept form.",
                 concl="The relation between two lines is decided by their gradients: equal "
                       "gradients give parallel lines and a product of −1 gives perpendicular "
                       "lines.")),
        dict(id="4.5", title="Linear models and variation",
             inquiry_q="How is a real rate turned into a linear model, and what does the model "
                       "assume?",
             teach=[
                 "A linear model has the form y = mx + c, where c is the starting value and m is the rate of change. Every linear model assumes that the rate is constant.",
                 "Building a model means identifying the two quantities, choosing units, and finding the rate from two data points. The rate is the gradient of the segment joining them.",
                 "Interpolation predicts inside the range of the data and extrapolation predicts outside it. Extrapolation assumes the rate continues, which is often false.",
                 "A model is judged by its usefulness, not its truth. A linear model of a cooling cup is wrong but useful for the first few minutes.",
             ], examples=[
                 dict(q="A plumber charges 45 dollars for a call-out and 60 dollars per hour. "
                        "Write the cost as a linear model, find the cost of a 3-hour job, and "
                        "find the longest job affordable for 300 dollars.",
                      vis=F("table", [["hours", "cost"],
                                      ["0", "45"],
                                      ["1", "105"],
                                      ["2", "165"],
                                      ["3", "225"],
                                      ["4", "285"],
                                      ["5", "345"]],
                            caption="The cost rises by 60 for every extra hour."),
                      reasoning="Identify the fixed charge as the intercept and the hourly rate "
                               "as the gradient.",
                      steps=["The model is C = 60h + 45, with h in hours.",
                             "For a 3-hour job, C = 60(3) + 45 = 225 dollars.",
                             "Setting 60h + 45 = 300 gives 60h = 255, so h = 4.25 hours.",
                             "So the longest whole-number job is 4 hours, at 285 dollars.",
                             "The model assumes the same rate for every hour, including "
                             "overtime."],
                      ans="C = 60h + 45; 225 dollars for 3 hours; 4 hours within 300 dollars",
                      interp="The fixed charge is the intercept and the hourly rate is the "
                             "gradient, and both come straight from the wording of the "
                             "situation."),
                 dict(q="A tree is 1.4 m tall when planted and grows 0.25 m per year. Model "
                        "its height, predict the height after 12 years, and comment on the "
                        "model's limits.",
                      vis=F("grid", [(0, 1.4), (12, 4.4)], ["planted", "12 years"], 0, 14, 0, 6,
                            [(0, 1.4), (12, 4.4)],
                            "the model is a straight line"),
                      reasoning="Write the model in gradient-intercept form and substitute.",
                      steps=["The model is h = 0.25t + 1.4, with t in years.",
                             "After 12 years, h = 0.25(12) + 1.4 = 4.4 m.",
                             "The model assumes the same growth every year.",
                             "In reality growth slows as the tree matures, so the model "
                             "overestimates later heights.",
                             "It is useful for the first decade and unreliable beyond it."],
                      ans="h = 0.25t + 1.4; 4.4 m after 12 years; unreliable in the long term",
                      interp="A linear model is a local description, and extrapolating it far "
                             "beyond the data is where it fails."),
             ], inv=dict(
                 task="Find three real rates: a speed, a cost per unit and a change per year. "
                      "Model each as a linear function, use it to interpolate one value and "
                      "extrapolate another, and comment on the reliability of each prediction.",
                 table=[["rate", "model", "interpolation", "extrapolation"],
                        ["water filling a tank", "V = 4t + 20", "60 litres at t = 10",
                         "220 litres at t = 50"],
                        ["savings", "S = 50m + 200", "500 at m = 6", "5200 at m = 100"],
                        ["temperature", "T = −0.5t + 20", "15 at t = 10", "−30 at t = 100"]],
                 notice=["The interpolation values were close to what really happens.",
                         "The extrapolation values grew without limit, which reality does not "
                         "allow.",
                         "The temperature model predicted an impossible negative value.",
                         "Every model assumed a constant rate, which is the source of the "
                         "failure."],
                 obs="A linear model is reliable inside the range of the data and increasingly "
                     "unreliable outside it, because the assumption of a constant rate is "
                     "rarely true for long.",
                 concl="A linear model is built from a starting value and a rate, and its "
                       "predictions are trustworthy only where the rate itself can be trusted.")),
        dict(id="4.6", title="Investigation: modelling a fair fare",
             inquiry_q="How is a fare modelled, and what does the model leave out?",
             teach=[
                 "A fare usually has a fixed part and a part that depends on distance or time, so it is a linear model whose intercept is the flag-fall and whose gradient is the rate per unit.",
                 "The graph of a fare against distance is a straight line that does not pass through the origin, so the fare is not proportional to the distance. The intercept is the charge for travelling no distance at all.",
                 "A fare model assumes the rate is constant, and real fares have waiting time, traffic, surcharges and shared rides, none of which a single straight line can show.",
                 "Comparing two fares means comparing their models over a stated journey, and the fairer fare depends on the distance travelled, which is why a single answer is impossible.",
             ], examples=[
                 dict(q="A taxi charges a flag-fall of 3 dollars plus 2.20 dollars per "
                        "kilometre. Model the fare, draw the graph, and find the fare for a "
                        "15 km journey.",
                      vis=F("grid", [(15, 36), (0, 3)], ["15 km", "flag-fall"], 0, 20, 0, 50,
                            [(0, 3), (20, 47)],
                            "the fare rises linearly from the flag-fall"),
                      reasoning="Read the intercept and the gradient from the wording, then "
                               "substitute.",
                      steps=["The model is C = 2.2d + 3, with d in kilometres.",
                             "The intercept of 3 dollars is the charge for travelling no "
                             "distance.",
                             "The gradient of 2.20 is the charge per kilometre.",
                             "For 15 km the fare is 2.2 × 15 + 3 = 36 dollars.",
                             "The graph starts at (0, 3), not at the origin, so the fare is "
                             "not proportional to the distance."],
                      ans="C = 2.2d + 3, and the fare for 15 km is 36 dollars",
                      interp="The two numbers in the model are the two parts of the fare, and "
                             "the non-zero intercept is what distinguishes a fare from a "
                             "proportional charge."),
                 dict(q="A second company charges 1.50 dollars per kilometre with a "
                        "flag-fall of 6 dollars. Find the distance at which the two companies "
                        "charge the same, and say which is fairer for a 5 km trip.",
                      vis=F("grid", [(4.29, 12.43), (5, 14), (5, 13.5)],
                            ["break-even", "company 1", "company 2"], 0, 12, 0, 30,
                            [(0, 3), (12, 29.4), (0, 6), (12, 24)],
                            "the two fare lines cross at about 4.3 km"),
                      reasoning="Set the two models equal and solve, then compare at the "
                               "stated distance.",
                      steps=["The first company charges 3 + 2.2d and the second 6 + 1.5d.",
                             "Setting them equal gives 2.2d − 1.5d = 6 − 3.",
                             "So 0.7d = 3 and d ≈ 4.29 km.",
                             "For a 5 km trip the first charges 14 dollars and the second "
                             "13.50 dollars.",
                             "So the second is fairer for 5 km, and the first for longer "
                             "trips."],
                      ans="the fares are equal at about 4.29 km; the second company is "
                          "cheaper for 5 km",
                      interp="Which fare is fairer depends on the distance, so a recommendation "
                             "must state the journey it assumes."),
             ], inv=dict(
                 task="Find two real fare structures: two bus routes, two phone plans, two "
                      "delivery services or two taxis. Model each as a linear function, draw "
                      "both graphs on the same axes, find the break-even point, and write a "
                      "recommendation that states the journey length it assumes and what the "
                      "model leaves out.",
                 table=[["fare", "flag-fall", "rate", "break-even", "cheaper for short trips"],
                        ["company 1", "3.00", "2.20", "4.29 km", "yes"],
                        ["company 2", "6.00", "1.50", "4.29 km", "no"],
                        ["bus route A", "0.50", "0.80", "—", "yes"],
                        ["bus route B", "2.00", "0.40", "3.75 stops", "no"]],
                 notice=["Every fare had a flag-fall, so no graph passed through the origin.",
                         "The break-even point was where the two lines crossed.",
                         "The fare with the larger flag-fall was cheaper for long journeys "
                         "only.",
                         "Waiting time and surcharges were left out of every model."],
                 obs="A fare is modelled by an intercept and a gradient, and the fairer fare "
                     "depends on the journey length, so the recommendation must state the "
                     "journey it assumes.",
                 concl="A fare is a linear model whose intercept is the fixed charge and whose "
                       "gradient is the rate, and comparing two fares gives a break-even point "
                       "beyond which the ordering reverses.")),
    ],
    practice=dict(
        A=[("4.1.1", "Find the midpoint of (2, 5) and (8, −1).", "(5, 2)",
            "Average each coordinate.", "F"),
           ("4.1.2", "Find the gradient of the line through (1, 3) and (5, 11).", "2",
            "Divide the change in y by the change in x.", "F"),
           ("4.1.3", "Find the gradient of the line y = −3x + 7.", "−3",
            "Read it from the gradient-intercept form.", "F"),
           ("4.1.4", "Find f(4) for f(x) = 2x − 5.", "3", "Substitute x = 4.", "F"),
           ("4.1.5", "Find the y-intercept of 2x + 5y = 20.", "4",
            "Set x = 0 and solve for y.", "F"),
           ("4.1.6", "A line has gradient 3 and passes through (0, −2). Write its equation.",
            "y = 3x − 2", "Use y = mx + c with c = −2.", "F"),
           ("4.1.7", "Find the gradient of a line perpendicular to y = 2x + 1.", "−1/2",
            "The product of perpendicular gradients is −1.", "F"),
           ("4.1.8", "Find x when f(x) = 9 for f(x) = 4x − 7.", "x = 4",
            "Solve the equation 4x − 7 = 9.", "F"),
           ("4.1.9", "Find the gradient of the line through (−2, 4) and (4, −8).", "−2",
            "Divide the change in y by the change in x.", "F"),
           ("4.1.10", "A car travels 150 km in 2 hours. Find its average speed.",
            "75 km/h", "Divide distance by time.", "F"),
           ("4.1.11", "Find the x-intercept of y = 5x − 15.", "3",
            "Set y = 0 and solve for x.", "F"),
           ("4.1.12", "Write the equation of the horizontal line through (3, 4).", "y = 4",
            "A horizontal line has gradient 0.", "F")],
        B=[("4.2.1", "The number of tiles in the nth figure of a pattern is 3n + 2. Find the "
            "first four terms and test the rule on the tenth figure.",
            "5, 8, 11, 14; and 32 for the tenth.", "Substitute n = 1, 2, 3, 4 and 10.", "R"),
           ("4.2.2", "Investigate the pattern in the gradients of the lines joining (0, 0) to "
            "(1, 1), (2, 4), (3, 9) and (4, 16).",
            "The gradients are 1, 2, 3, 4, so they rise by 1 each time.",
            "Compute each gradient and compare.", "R"),
           ("4.2.3", "Conjecture a rule for the midpoint of the points (n, 0) and (0, n) and "
            "test it.",
            "(n/2, n/2), which lies on the line y = x.", "Average each coordinate.", "R"),
           ("4.2.4", "Investigate the pattern in the number of unit squares a diagonal of an "
            "n by n grid crosses.",
            "2n − 1, because the diagonal leaves each row and column once.", "Draw for n = 2, "
            "3, 4.", "R"),
           ("4.2.5", "Build a table of the first differences of f(n) = n² and describe the "
            "pattern.",
            "The first differences are the odd numbers 1, 3, 5, 7, rising by 2.",
            "Subtract consecutive terms.", "R"),
           ("4.2.6", "Conjecture a rule for the distance from (0, 0) to (n, n) and justify it.",
            "n√2, by Pythagoras' theorem on an isosceles right triangle.",
            "Apply the distance formula.", "R"),
           ("4.2.7", "Investigate the gradients of the segments joining consecutive points of "
            "(0, 1), (1, 3), (2, 6), (3, 10).",
            "The gradients are 2, 3, 4, rising by 1, because the rule is quadratic.",
            "Compute each gradient and take differences.", "R"),
           ("4.2.8", "A pattern of lines is drawn from (0, 0) to (1, 1), (2, 1), (3, 1) and "
            "so on. Investigate the gradients and find the rule.",
            "The gradients are 1, 1/2, 1/3, …, halving and then continuing as 1/n.",
            "Compute each gradient.", "C"),
           ("4.2.9", "Find the pattern in the intercepts of the lines y = nx + (3 − n) for "
            "n = 1 to 5 and justify it.",
            "The intercepts are 2, 1, 0, −1, −2, falling by 1 each time.",
            "Read the intercept from each equation.", "R"),
           ("4.2.10", "Investigate the point of intersection of y = 2x + 1 and y = −x + 4 as "
            "the coefficients change.",
            "The intersection moves along the first line as the second line rotates.",
            "Solve for several values of the coefficients.", "R"),
           ("4.2.11", "Conjecture a rule for the number of regions made by n lines in general "
            "position.",
            "n(n + 1)/2 + 1, because each new line cuts all the others.",
            "Count for n = 1, 2, 3, 4.", "R")],
        C=[("4.3.1", "Explain in your own words what a function is.",
            "A rule that gives exactly one output for each permitted input.",
            "State the definition and give an example.", "R"),
           ("4.3.2", "Write a complete solution to: find the equation of the line through "
            "(1, 4) with gradient −3.",
            "y = −3x + 7", "Substitute into y = mx + c and solve for c.", "F"),
           ("4.3.3", "Choose between a graph and an equation to answer a question about speed "
            "and justify.", "The equation for an exact value; the graph for a comparison or a "
            "trend over a range.", "Say what each gives.", "R"),
           ("4.3.4", "Set out a full solution to: find the gradient and intercepts of "
            "4x − 2y = 8.",
            "Gradient 2, intercepts (0, −4) and (2, 0).", "Rearrange into y = mx + c.", "F"),
           ("4.3.5", "Explain why the gradient is the same everywhere on a straight line.",
            "Because the ratio of the change in y to the change in x is constant for any two "
            "points on the line.", "Compute it from two pairs of points.", "R"),
           ("4.3.6", "Describe, with an example, the difference between interpolation and "
            "extrapolation.", "Interpolation predicts inside the range of the data, as "
            "predicting the cost at 3 hours from data covering 1 to 5 hours; extrapolation "
            "predicts outside it.", "Define both and give an example of each.", "R"),
           ("4.3.7", "Explain why a vertical line is not the graph of a function of x.",
            "Because one value of x would be paired with many values of y, giving more than one "
            "output for one input.", "Apply the definition.", "R"),
           ("4.3.8", "Write the reasoning that shows the product of perpendicular gradients is "
            "−1.", "A rotation through 90° maps a segment of gradient m to one of gradient "
            "−1/m, so their product is −1.", "Draw two perpendicular segments.", "R"),
           ("4.3.9", "Set out the argument that two quantities are in direct proportion "
            "exactly when their graph passes through the origin.",
            "If y = kx then y = 0 when x = 0; and if the line passes through the origin its "
            "equation is y = mx, which is direct proportion.", "Use y = mx + c.", "R"),
           ("4.3.10", "Explain what the intercept of a distance-time graph represents.",
            "The distance from the start at time zero — how far away the journey began.",
            "Give a real example.", "R"),
           ("4.3.11", "Describe the relationship between the gradient of a distance-time graph "
            "and speed.", "The gradient is the speed, because it is the change in distance per "
            "unit change in time.", "Read one from the other.", "R"),
           ("4.3.12", "Explain, with an example, when a linear model is a poor description of "
            "a real rate.", "Any answer is acceptable if it identifies a rate that changes, "
            "such as a cooling cup, a growing tree, or a filling tank.", "Give a specific "
            "counterexample.", "R")],
        D=[("4.4.1", "A taxi charges 3 dollars plus 2.20 dollars per km. Model the fare, find "
            "the fare for 15 km, and find the distance affordable for 30 dollars.",
            "C = 2.2d + 3; 36 dollars for 15 km; about 12.27 km for 30 dollars.",
            "Read the intercept and gradient, then solve.", "A"),
           ("4.4.2", "A worker is paid 12 dollars per hour plus a 20 dollar bonus. Model the "
            "pay, find the pay for 35 hours, and find the hours needed for 400 dollars.",
            "P = 12h + 20; 440 dollars for 35 hours; 31.67 hours for 400 dollars.",
            "Read the intercept and gradient, then solve.", "A"),
           ("4.4.3", "A tank holds 500 litres and is filled at 12 litres per minute. Model the "
            "volume, find when it is full, and find the volume after 20 minutes.",
            "V = 12t; full at about 41.7 minutes; 240 litres after 20 minutes.",
            "Use a proportional model.", "A"),
           ("4.4.4", "A candle 25 cm long burns 1.5 cm per hour. Model its height, find when "
            "it burns out, and find the height after 6 hours.",
            "h = 25 − 1.5t; burns out at about 16.7 hours; 16 cm after 6 hours.",
            "The gradient is negative.", "A"),
           ("4.4.5", "A train leaves at 60 km/h and a second leaves the same station 1 hour "
            "later at 90 km/h. Find when the second catches the first.",
            "After 2 hours, at 180 km from the station.",
            "Set the two distance models equal.", "A"),
           ("4.4.6", "A school's roll falls by 15 students per year from 480. Model the roll, "
            "find when it reaches 300, and comment on the model's limits.",
            "N = 480 − 15t; 12 years to reach 300; the model cannot go below zero.",
            "Read the gradient, then solve.", "A"),
           ("4.4.7", "A recipe serves 6 with 400 g of flour. Model the flour needed, find the "
            "amount for 11 people, and find the people served by 1.5 kg.",
            "F = 66.7p; about 733 g for 11; 22 people from 1.5 kg.",
            "Use a proportional model.", "A"),
           ("4.4.8", "A cyclist covers 12 km in 40 minutes. Find the speed, model the "
            "distance, and find the distance covered in 2 hours 30 minutes.",
            "18 km/h; d = 18t; 45 km in 2.5 hours.", "Convert units first.", "A"),
           ("4.4.9", "A phone battery falls from 100% to 68% in 4 hours. Model the charge, "
            "find when it reaches zero, and comment on the model.",
            "About 8% per hour, so zero at about 8.5 hours; real batteries fall faster near "
            "the end, so the model overestimates.", "Find the rate and solve.", "R"),
           ("4.4.10", "A plant grows from 15 cm to 47 cm in 8 weeks. Model the height, find "
            "the weekly growth, and predict the height after 20 weeks with a comment.",
            "4 cm per week; 95 cm after 20 weeks, which is unlikely for a real plant.",
            "Find the rate, then extrapolate.", "A"),
           ("4.4.11", "Two cyclists start 30 km apart and ride towards each other at 14 and "
            "16 km/h. Find when and where they meet.",
            "After 1 hour, 14 km from the first cyclist's start.",
            "Set the sum of the distances equal to 30.", "A"),
           ("4.4.12", "Explain, with a model of your own, when reporting a prediction to a "
            "false precision is misleading.",
            "Any answer is acceptable if it shows that the digits beyond the model's "
            "reliability are not justified, as in predicting 95.3 cm for a plant.",
            "Link precision to reliability.", "R")],
    ),
    assessment=[
        dict(title="A1 · The delivery route",
             text="A courier starts 3 km from the depot and rides away at 15 km/h for 40 "
                  "minutes, rests for 15 minutes, then returns at 12 km/h. Model the distance "
                  "from the depot as a function of time, draw the graph, and find the total "
                  "time until the courier is back at the depot.",
             note="Criteria A and C · state the model for each part of the journey and read the "
                  "graph."),
        dict(title="A2 · The two rates",
             text="A printer charges 80 dollars plus 0.15 dollars per page. Another charges "
                  "no fee but 0.40 dollars per page. Model both, find the number of pages at "
                  "which the costs are equal, and find the number of pages for which the first "
                  "printer is cheaper by at least 20 dollars.",
             note="Criteria A and D · solve the equation for equality and the inequality for "
                  "the saving."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of representation, change and "
        "pattern appear in your work?",
        "How is the global context of orientation in space and time, and its exploration of "
        "maps, routes and rates, visible in the investigations and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a linear model of a journey or a rate, and what would you "
        "still like to ask?",
    ],
    review=dict(
        ideas=["A coordinate pair fixes a point on a plane.",
               "The midpoint averages the coordinates; the gradient divides the differences.",
               "A function gives exactly one output for each permitted input.",
               "y = mx + c displays the gradient and the intercept.",
               "Parallel lines have equal gradients; perpendicular gradients multiply to −1.",
               "A proportional relationship has a constant ratio and a graph through the "
               "origin.",
               "A rate is only meaningful with its units stated.",
               "Interpolation is inside the data; extrapolation assumes the rate continues."],
        vocab=["coordinate", "midpoint", "gradient", "intercept", "function", "domain",
               "range", "linear model", "rate", "proportion", "interpolation",
               "extrapolation"],
        mixed=[("4.R1", "Find the gradient of the line through (−1, 5) and (3, −7)."),
               ("4.R2", "Write the equation of the line with gradient −2 through (0, 6)."),
               ("4.R3", "Find f(3) and f(−2) for f(x) = 5 − 2x."),
               ("4.R4", "Find the intercepts of 3x − 2y = 12."),
               ("4.R5", "A car covers 210 km in 3 hours. Find the speed and the time for "
                        "350 km."),
               ("4.R6", "Explain why y = mx + c is not proportional unless c = 0.")],
    ),
    projects=dict(
        service=[("Community need", "Journeys, fares and rates are quoted without the model "
                                    "behind them."),
                 ("Mathematical connection", "Linear functions, gradients and rates."),
                 ("Proposed action", "Model one local journey or fare and publish the model "
                                     "with its assumptions."),
                 ("Expected impact", "A reader can compare two fares or routes on the same "
                                     "terms."),
                 ("Student reflection", "Record the model, the graph and what you found.")],
        community=[("Project idea", "A route audit for a school or neighbourhood."),
                   ("Need", "Distances, times and costs are estimated without a shared "
                            "method."),
                   ("Research question", "Which route is fastest for which purpose, and what "
                                         "does the model assume?"),
                   ("Mathematics", "Coordinates, gradients and linear models."),
                   ("Action or outcome", "A one-page map with a distance-time model for each "
                                         "route."),
                   ("Beneficiaries", "Everyone who travels the route."),
                   ("Evidence", "The map, the models and the comparison.")],
        personal=[("Personal interest", "A journey, a sport or a hobby with a rate."),
                  ("Learning goal", "To model a rate you care about and state what the model "
                                    "assumes."),
                  ("Product or outcome", "A linear model with a graph and a prediction."),
                  ("Mathematics", "Gradients, intercepts and proportional reasoning."),
                  ("Process", "Collect two data points, build the model, and test a "
                              "prediction."),
                  ("Evidence", "The model, the graph and the test of the prediction.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=5, title="Quadratic Expressions and Equations",
    key="Logic", related=["Equivalence", "Generalisation", "Justification"],
    context="Scientific and technical innovation",
    exploration="Design, motion and optimisation",
    inquiry=("A quadratic equation is solved by transforming it into an equivalent form whose "
             "solutions are visible, and the justification for each transformation is a "
             "reversible step; the discriminant then decides, before any solving, how many "
             "solutions exist, which turns a calculation into a general claim."),
    atl=("Reflection",
         "Students consider which method to use for a given quadratic, justify the choice, "
         "and reflect on the accuracy and the efficiency of the method they chose."),
    standfirst="Every quadratic can be solved, and the method chosen decides how much work is "
               "needed and what the answer reveals about the equation.",
    engage="A ball is thrown upwards from a platform 5 m high. Its height after t seconds is "
           "h = 20t − 5t². When is it 15 m high, and when does it hit the ground?",
    questions=[("Factual", "What are the four methods of solving a quadratic equation, and "
                           "what does the discriminant tell you?"),
               ("Conceptual", "Why does completing the square work for every quadratic, and "
                              "how does the discriminant justify a claim about the number of "
                              "solutions?"),
               ("Debatable", "Is the quadratic formula a tool for understanding or a tool for "
                             "avoiding understanding, and does it matter which method a "
                             "student uses?")],
    application_lede="Each task asks for a solution and a justification. State the method you "
                     "chose and why it suits the equation.",
    projects_lede="Optimisation and motion are quadratic. Model one and say which method "
                  "answers the question most clearly.",
    sections=[
        dict(id="5.1", title="From expressions to equations",
             inquiry_q="How does a quadratic equation arise from a quadratic expression, and why must "
                       "the equation be rearranged before it can be solved?",
             teach=[
                 "An expression is a rule for computing a value, and an equation is a claim that two expressions are equal. Solving an equation means finding every input that makes the claim true.",
                 "A quadratic equation is one that can be written in the standard form ax² + bx + c = 0, and the first step is always to rearrange it into that form, because every solving method assumes it.",
                 "The zero-product property says that if a product is zero then at least one factor is zero, and this is the single fact that turns factorisation into a method of solving.",
                 "Expanding and factorising are the two directions of the same equivalence, and a generalisation stated with letters is justified by the identity that proves it for every case at once.",
                 "A solution that has been found must be checked by substitution, because rearranging can introduce a value that does not satisfy the original claim.",
             ], examples=[
                 dict(q="Evaluate (2x − 3)(x + 4) when x = 1, first by substitution and then "
                        "by expanding.",
                      vis=F("table", [["method", "working", "value"],
                                      ["substitute first", "(2 − 3)(1 + 4)", "−5"],
                                      ["expand first", "2x² + 8x − 3x − 12 = 2x² + 5x − 12",
                                       "−5"]],
                            caption="Both routes give the same value, as equivalence requires."),
                      reasoning="Substitution gives the value directly; expansion gives a form "
                               "that works for every x.",
                      steps=["Substituting x = 1: (2(1) − 3)(1 + 4) = (−1)(5) = −5.",
                             "Expanding: (2x − 3)(x + 4) = 2x² + 8x − 3x − 12 = 2x² + 5x − 12.",
                             "Substituting x = 1 into the expansion: 2 + 5 − 12 = −5.",
                             "The two answers agree, which they must because expansion is an "
                             "equivalence.",
                             "The expanded form would also give the value at any other x "
                             "without re-multiplying."],
                      ans="−5, by either route",
                      interp="Expanding is worth the effort only when more than one value is "
                             "needed, which is the usual case in modelling."),
                 dict(q="Expand (3x + 2)² and explain why it is not 9x² + 4.",
                      vis=F("tiles", 3, 3, [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1),
                                             (0, 2), (1, 2)],
                            "a 3 by 3 square of side 3x + 2",
                            note="9x², 12x and 4"),
                      reasoning="Use the perfect square identity and identify the missing cross "
                               "term.",
                      steps=["(3x + 2)² = (3x)² + 2(3x)(2) + 2² = 9x² + 12x + 4.",
                             "The term 12x is the cross term, and it is what 9x² + 4 leaves out.",
                             "A check at x = 1 gives 25 against 13, so the claim fails.",
                             "The missing term is twice the product of the two parts.",
                             "This is the commonest error in expanding, and it comes from "
                             "treating a square as distributive over addition."],
                      ans="9x² + 12x + 4",
                      interp="A single substitution refutes a false identity, which is why "
                             "checking with a number is a reliable habit."),
             ], inv=dict(
                 task="Take five equations that are not in standard form: one with terms on "
                      "both sides, one with brackets, one with fractions, one with the "
                      "variable on both sides, and one of your own. Rearrange each into the "
                      "form ax² + bx + c = 0, state a, b and c, then check one solution by "
                      "substitution into the original equation.",
                 table=[["equation", "standard form", "a, b, c", "check"],
                        ["x² = 7x − 12", "x² − 7x + 12 = 0", "1, −7, 12", "9 − 63 + 12 = 0"],
                        ["(x − 2)(x + 3) = 0", "x² + x − 6 = 0", "1, 1, −6", "−3 − 3 − 6 = 0"],
                        ["2x(x − 5) = 0", "2x² − 10x = 0", "2, −10, 0", "0 − 0 = 0"],
                        ["x² + 4 = 4x", "x² − 4x + 4 = 0", "1, −4, 4", "4 − 8 + 4 = 0"],
                        ["3x² = 12", "3x² − 12 = 0", "3, 0, −12", "12 − 12 = 0"]],
                 notice=["Every equation became a quadratic once it was rearranged.",
                         "The equation with no linear term gave symmetric roots.",
                         "The equation (x − 2)(x + 3) = 0 was already factorised, so its "
                         "roots came from the factors directly.",
                         "The check into the original equation was as important as the "
                         "rearrangement."],
                 obs="Every quadratic equation can be rearranged into the standard form, and "
                     "the standard form is what the solving methods need.",
                 concl="Rearranging to ax² + bx + c = 0 is the first step of every "
                       "quadratic method, and the zero-product property is the fact that "
                       "turns a factorisation into solutions.")),
        dict(id="5.2", title="Solving by factorising",
             inquiry_q="Why does factorisation solve a quadratic equation, and when does it "
                       "fail?",
             teach=[
                 "To solve a factorised quadratic, set each factor equal to zero. This is the zero-product property, and it works because a product is zero only when one of its factors is zero.",
                 "The method needs a quadratic that factorises over the integers, and it fails silently when the factors are not found, so a check by substitution is essential.",
                 "Factorising the difference of two squares x² − a² gives two roots that are symmetric about zero, and factorising a perfect square gives one repeated root.",
                 "When the leading coefficient is not 1, factorise by grouping or by inspection, and the two factors then give the two roots directly.",
             ], examples=[
                 dict(q="Solve x² − 6x + 5 = 0 by factorising, and check each root.",
                      vis=F("grid", [(3, -4), (1, 0), (5, 0)], ["vertex", "r1", "r2"], -1, 7,
                            -5, 3, [(1, 0), (2, -3), (3, -4), (4, -3), (5, 0)],
                            "the roots are where the parabola meets the axis"),
                      reasoning="Factorise the quadratic, then set each factor to zero.",
                      steps=["Find two numbers that multiply to 5 and add to −6: −1 and −5.",
                             "So x² − 6x + 5 = (x − 1)(x − 5).",
                             "Setting each factor to zero gives x − 1 = 0 or x − 5 = 0.",
                             "Hence x = 1 or x = 5.",
                             "Check: 1 − 6 + 5 = 0 and 25 − 30 + 5 = 0, so both roots work."],
                      ans="x = 1 or x = 5",
                      interp="The two factors give the two roots, and each root is a value that "
                             "makes the original equation true."),
                 dict(q="Solve 2x² + 7x + 3 = 0 by factorising.",
                      vis=F("grid", [(-1.75, -3.125), (-0.5, 0), (-3, 0)],
                            ["vertex", "r1", "r2"], -4, 2, -5, 3,
                            [(-3, 0), (-2, -3), (-1.75, -3.125), (-1, -2), (-0.5, 0)],
                            "two roots, one of them fractional"),
                      reasoning="The leading coefficient is not 1, so factorise by inspection "
                               "or by grouping.",
                      steps=["2x² + 7x + 3 = (2x + 1)(x + 3), because 2x² + 6x + x + 3 "
                             "regroups.",
                             "Setting each factor to zero: 2x + 1 = 0 or x + 3 = 0.",
                             "Hence x = −½ or x = −3.",
                             "Check: 2(¼) + 7(−½) + 3 = 0.5 − 3.5 + 3 = 0.",
                             "The roots are rational but not integers, so factorising still "
                             "works."],
                      ans="x = −½ or x = −3",
                      interp="A non-monic quadratic factorises just as well, and the roots can "
                             "be fractions without spoiling the method."),
             ], inv=dict(
                 task="Take eight quadratics of your own: four monic and four with a leading "
                      "coefficient other than 1. Solve each by factorising, and record which "
                      "factorised at the first attempt and which needed a different method.",
                 table=[["quadratic", "factorisation", "roots", "method"],
                        ["x² − 9", "(x − 3)(x + 3)", "3, −3", "difference of squares"],
                        ["x² + 10x + 25", "(x + 5)²", "−5 (repeated)", "perfect square"],
                        ["x² − 5x + 6", "(x − 2)(x − 3)", "2, 3", "monic"],
                        ["3x² − 12", "3(x − 2)(x + 2)", "2, −2", "common factor first"],
                        ["2x² − 5x − 3", "(2x + 1)(x − 3)", "−½, 3", "grouping"]],
                 notice=["Every quadratic that factorised gave its roots immediately.",
                         "The difference of squares gave roots symmetric about zero.",
                         "The perfect square gave one repeated root.",
                         "The common factor had to be taken out before factorising.",
                         "A quadratic that did not factorise would need the formula instead."],
                 obs="Factorising solves a quadratic by turning the equation into a product "
                     "equal to zero, and the two factors give the two roots.",
                 concl="The zero-product property is what makes factorisation a solving "
                       "method, and the method applies whenever the quadratic factorises over "
                       "the integers.")),
        dict(id="5.3", title="Completing the square",
             inquiry_q="Why does completing the square work for every quadratic, and what does "
                       "it reveal?",
             teach=[
                 "Completing the square rewrites ax² + bx + c as a(x + p)² + q. It works for every quadratic because the square can always absorb the linear term.",
                 "The method is to factor out the leading coefficient, add and subtract the square of half the coefficient of x, and regroup. The value is unchanged because the same quantity is added and subtracted.",
                 "The completed form shows the vertex of the parabola at (−p, q) and the axis of symmetry at x = −p, which is the information the expanded form hides.",
                 "The quadratic formula is derived by completing the square on ax² + bx + c = 0, so completing the square is the more fundamental of the two methods.",
             ], examples=[
                 dict(q="Solve x² − 6x + 5 = 0 by completing the square.",
                      vis=F("grid", [(3, -4), (1, 0), (5, 0)], ["vertex", "r1", "r2"],
                            -2, 8, -6, 4, [(1, 0), (2, -3), (3, -4), (4, -3), (5, 0)],
                            "the vertex is at x = 3, halfway between the roots"),
                      reasoning="Add and subtract the square of half the coefficient of x, then "
                               "solve the resulting square.",
                      steps=["Half of −6 is −3, and its square is 9.",
                             "So x² − 6x + 5 = (x² − 6x + 9) − 9 + 5 = (x − 3)² − 4.",
                             "The equation becomes (x − 3)² = 4.",
                             "Taking square roots gives x − 3 = ±2, so x = 5 or x = 1.",
                             "The vertex is (3, −4) and the axis of symmetry is x = 3, which "
                             "is the average of the two roots."],
                      ans="x = 5 or x = 1",
                      interp="The completed square gives the roots and the vertex from the "
                             "same rewrite, which is why it is the more informative method."),
             ], inv=dict(
                 task="Take five quadratics: one monic with an even coefficient of x, one monic "
                      "with an odd coefficient, one with a leading coefficient of 2, one with "
                      "a negative leading coefficient, and one of your own. Complete the "
                      "square for each, and use the completed form to find the vertex and the "
                      "axis of symmetry.",
                 table=[["quadratic", "completed square", "vertex"],
                        ["x² + 4x + 1", "(x + 2)² − 3", "(−2, −3)"],
                        ["x² + 5x + 2", "(x + 2.5)² − 4.25", "(−2.5, −4.25)"],
                        ["2x² − 8x + 3", "2(x − 2)² − 5", "(2, −5)"],
                        ["−x² + 6x − 5", "−(x − 3)² + 4", "(3, 4)"],
                        ["3x² + 12x − 2", "3(x + 2)² − 14", "(−2, −14)"]],
                 notice=["The x-coordinate of the vertex was always −b/(2a).",
                         "The y-coordinate was the value of the expression at that x.",
                         "A negative leading coefficient turned the minimum into a maximum.",
                         "The odd coefficient of x gave a half-integer in the vertex."],
                 obs="The completed square always has the form a(x + p)² + q, and the vertex "
                     "is read from it immediately.",
                 concl="Completing the square works for every quadratic, and it is the method "
                       "that reveals the vertex, which is why the other methods are derived "
                       "from it.")),
        dict(id="5.4", title="The quadratic formula and discriminant",
             inquiry_q="How does the quadratic formula solve every quadratic, and what does its "
                       "discriminant reveal about the roots?",
             teach=[
                 "The quadratic formula x = (−b ± √(b² − 4ac))/(2a) solves every quadratic equation, and it is obtained by completing the square on ax² + bx + c = 0.",
                 "The formula is used when factorising is not quick, and it always works, so it is the method of last resort that never fails.",
                 "The expression b² − 4ac under the root is called the discriminant, and its sign decides the nature of the roots: positive gives two distinct real roots, zero gives one repeated root, and negative gives none.",
                 "The discriminant also justifies a claim about every quadratic of a given shape, because a single calculation proves what would otherwise need infinitely many substitutions.",
                 "The graph and the algebra must agree: the discriminant says whether the parabola crosses the x-axis twice, touches it once, or misses it entirely.",
             ],
             examples=[

                 dict(q="Solve 3x² − 5x − 2 = 0 using the quadratic formula.",
                      vis=F("table", [["step", "value"],
                                      ["a, b, c", "3, −5, −2"],
                                      ["b² − 4ac", "25 + 24 = 49"],
                                      ["√49", "7"],
                                      ["x = (5 ± 7)/6", "2 or −1/3"]],
                            caption="The discriminant is a perfect square, so the roots are "
                                    "rational."),
                      reasoning="Identify a, b and c, evaluate the discriminant, and simplify "
                               "both roots.",
                      steps=["Here a = 3, b = −5 and c = −2.",
                             "b² − 4ac = 25 − 4(3)(−2) = 25 + 24 = 49.",
                             "So x = (5 ± 7)/6.",
                             "The roots are x = 12/6 = 2 and x = −2/6 = −1/3.",
                             "Check: 3(4) − 5(2) − 2 = 0 and 3(1/9) − 5(−1/3) − 2 = 0."],
                      ans="x = 2 or x = −1/3",
                      interp="A perfect-square discriminant is the signal that the quadratic "
                             "would also have factorised, and here it gives (3x + 1)(x − 2)."),
                 dict(q="Solve 2x² + 7x + 4 = 0, giving the roots to three significant "
                        "figures.",
                      vis=F("grid", [(-1.75, -2.125), (-2.78, 0), (-0.72, 0)],
                            ["vertex", "r1", "r2"],
                            -3.5, 0.5, -4, 2,
                            [(-2.78, 0), (-2.4, -1.28), (-1.75, -2.125), (-1.1, -1.28),
                             (-0.72, 0)],
                            "the two roots are close together"),
                      reasoning="Apply the formula and round only at the end.",
                      steps=["a = 2, b = 7, c = 4, so b² − 4ac = 49 − 32 = 17.",
                             "x = (−7 ± √17)/4.",
                             "√17 ≈ 4.123, so x ≈ (−7 + 4.123)/4 = −0.719 and x ≈ (−7 − "
                             "4.123)/4 = −2.78.",
                             "To three significant figures the roots are −0.719 and −2.78.",
                             "The exact form is (−7 ± √17)/4, which is preferable if the "
                             "calculation continues."],
                      ans="x ≈ −0.719 or x ≈ −2.78",
                      interp="Rounding was done once, at the end, so the answers carry the "
                             "precision the inputs justify and no more."),

                 dict(q="Find the discriminant of 2x² − 4x + 5 and state the nature of its "
                        "roots, with a reason.",
                      vis=F("grid", [(1, 3), (0, 5), (2, 5)], ["vertex", "", ""], -1, 3, 0, 7,
                            [(0, 5), (2, 5)],
                            "the parabola misses the x-axis entirely"),
                      reasoning="Evaluate b² − 4ac and read the sign.",
                      steps=["a = 2, b = −4, c = 5.",
                             "b² − 4ac = 16 − 40 = −24.",
                             "The discriminant is negative, so there are no real roots.",
                             "The graph is a parabola opening upwards with its vertex above the "
                             "x-axis, so it never crosses.",
                             "The statement 'no real solutions' is therefore justified, not "
                             "merely observed."],
                      ans="the discriminant is −24, so there are no real roots",
                      interp="The discriminant proves a general claim about every equation of "
                             "this form, which testing values could never do."),
                 dict(q="Find the values of k for which x² + kx + 9 = 0 has exactly one real "
                        "root.",
                      vis=F("grid", [(-3, 0), (3, 0), (0, 9)], ["r", "r", ""], -6, 6, 0, 12,
                            [(-3, 0), (3, 0)],
                            "a repeated root means the parabola touches the axis"),
                      reasoning="A repeated root occurs when the discriminant is zero, so set "
                               "b² − 4ac = 0 and solve for k.",
                      steps=["Here a = 1, b = k and c = 9.",
                             "The discriminant is k² − 36.",
                             "Setting it to zero gives k² = 36, so k = ±6.",
                             "For k = 6 the equation is x² + 6x + 9 = (x + 3)², with root −3.",
                             "For k = −6 the equation is x² − 6x + 9 = (x − 3)², with root 3."],
                      ans="k = 6 or k = −6",
                      interp="A condition on the number of roots becomes an equation in the "
                             "parameter, and the discriminant is what converts the one into "
                             "the other.")
             ],
             inv=dict(
                 task="Take five quadratics, including one that does not factorise over the "
                      "integers. Solve each by the formula and by at least one other method, "
                      "record which was quicker, and check one root by substitution in every "
                      "case.",
                 table=[["quadratic", "formula root", "other method", "quicker"],
                        ["x² − 5x + 6", "2 or 3", "factorising", "factorising"],
                        ["x² + 4x + 1", "−2 ± √3", "completing the square", "equal"],
                        ["2x² + 5x − 3", "0.5 or −3", "factorising", "factorising"],
                        ["x² + x + 1", "complex", "discriminant only", "discriminant"],
                        ["3x² − 2x − 7", "(1 ± 22)/3", "formula", "formula"]],
                 notice=["Factorising was quickest whenever the discriminant was a perfect "
                         "square.",
                         "The formula always worked, even when factorising failed.",
                         "One quadratic had a negative discriminant, so it had no real roots "
                         "and no method could produce any.",
                         "The check by substitution passed in every case where real roots "
                         "existed."],
                 obs="The choice of method is a question of efficiency, and the formula is the "
                     "method that is never wrong but is not always the fastest.",
                 concl="A quadratic is solved by the method that suits its coefficients, and "
                       "the formula is the fallback that always succeeds.")),
        dict(id="5.5", title="Forming and applying equations",
             inquiry_q="How does a quadratic model describe motion, area and optimisation?",
             teach=[
                 "A projectile's height is a quadratic in time, because gravity gives a constant acceleration and the height is the integral of a linear velocity.",
                 "The vertex of the model gives the maximum height and the time at which it occurs, and the roots give when the object is at ground level.",
                 "Area problems often produce a quadratic when a fixed perimeter or a fixed area is rearranged, and the optimum is at the vertex.",
                 "A quadratic model is only valid within its domain, and a root outside that domain is a mathematical solution with no physical meaning.",
             ], examples=[
                 dict(q="A ball is thrown upwards from a platform 5 m high with height "
                        "h = 20t − 5t² metres after t seconds. Find when it is 15 m high and "
                        "when it hits the ground.",
                      vis=F("grid", [(2, 20), (4.58, 0), (1, 15), (3, 15)],
                            ["max", "ground", "15 m", "15 m"], 0, 5, 0, 24,
                            [(0, 5), (2, 20), (4.58, 0)],
                            "the height of the ball against time"),
                      reasoning="Set the model equal to the required height and solve the "
                               "resulting quadratic, keeping only the meaningful roots.",
                      steps=["For h = 15: 20t − 5t² = 15, so 5t² − 20t + 15 = 0.",
                             "Dividing by 5 gives t² − 4t + 3 = 0, so (t − 1)(t − 3) = 0.",
                             "Hence t = 1 or t = 3 seconds, on the way up and on the way down.",
                             "For h = 0: 20t − 5t² = 0, so 5t(4 − t) = 0.",
                             "Hence t = 0 or t = 4 seconds; the answer is 4 seconds."],
                      ans="15 m at 1 s and 3 s; the ground at 4 s",
                      interp="Both roots of the height equation were meaningful, but the root "
                             "t = 0 for the ground was the launch, not the landing."),
                 dict(q="A farmer has 40 m of fencing for a rectangular pen against a wall. "
                        "Find the dimensions of greatest area.",
                      vis=F("grid", [(10, 100), (20, 200), (15, 225)], ["", "", "max"],
                            0, 24, 0, 240, [(0, 0), (20, 0), (20, 200)],
                            "area against width, with a maximum at 10 m"),
                      reasoning="Write the area as a quadratic in one variable and find its "
                               "vertex.",
                      steps=["Let x be the width and y the depth; the fence gives 2x + y = 40.",
                             "So y = 40 − 2x and the area is A = x(40 − 2x) = 40x − 2x².",
                             "This is a downward parabola with roots at x = 0 and x = 20.",
                             "The maximum lies halfway between the roots, at x = 10.",
                             "Then y = 20 and the greatest area is 200 m²."],
                      ans="10 m by 20 m, giving 200 m²",
                      interp="The symmetry of a quadratic with known roots gives the maximum "
                             "without any calculus, which is why the factorised form is useful "
                             "here."),
             ], inv=dict(
                 task="Find two real situations that produce a quadratic: one about motion and "
                      "one about area or profit. Model each, solve it, and check that every "
                      "root you keep is physically meaningful.",
                 table=[["situation", "model", "roots", "meaningful?"],
                        ["ball from a cliff", "h = 25 + 30t − 5t²", "t = 7 and t = −1",
                         "only t = 7"],
                        ["rectangular pen", "A = 40x − 2x²", "x = 0 and x = 20",
                         "the maximum at x = 10"],
                        ["ticket profit", "P = −2x² + 60x − 200", "x = 4.2 and x = 25.8",
                         "the maximum at x = 15"],
                        ["thrown stone", "h = 1.5 + 14t − 5t²", "t = 3 and t = −0.1",
                         "only t = 3"]],
                 notice=["Every motion model gave one positive and one negative root, and only "
                         "the positive one described the future.",
                         "Every area model gave a root at zero, which described the degenerate "
                         "case.",
                         "The maximum always lay halfway between the two roots.",
                         "The negative roots were solutions of the equation but not of the "
                         "situation."],
                 obs="A quadratic model of a physical situation returns roots that must be "
                     "tested against the domain, and the negative or degenerate roots are "
                     "rejected.",
                 concl="A quadratic model is solved like any quadratic, and its roots are "
                       "accepted only when they lie inside the domain of the situation.")),
        dict(id="5.6", title="Investigation: the discriminant detective",
             inquiry_q="What can the discriminant b² − 4ac tell us about a quadratic before "
                       "we solve it?",
             teach=[
                 "The discriminant is a detective's tool: a single calculation reports the number of real roots, and it does so without solving anything.",
                 "A discriminant that is a perfect square tells us the roots are rational, so factorising will work. A positive non-square discriminant gives irrational roots, and a negative one gives none at all.",
                 "Setting the discriminant to zero is how a parameter is chosen so that a quadratic has a repeated root, which is the condition for a parabola to touch a line or an axis.",
                 "The discriminant must agree with the graph. If the calculation says two roots and the graph shows none, one of the two is wrong, and the check is what makes the tool trustworthy.",
             ], examples=[
                 dict(q="Solve x² + 10x + 21 = 0 by two methods and say which you would "
                        "recommend.",
                      vis=F("table", [["method", "working", "roots"],
                                      ["factorising", "(x + 3)(x + 7) = 0", "−3, −7"],
                                      ["completing the square", "(x + 5)² − 4 = 0", "−3, −7"],
                                      ["formula", "x = (−10 ± 4)/2", "−3, −7"]],
                            caption="Three methods, the same two roots."),
                      reasoning="All three methods are valid, and the choice is a question of "
                               "speed and of what is revealed.",
                      steps=["Factorising: two numbers with sum 10 and product 21 are 3 and 7, "
                             "so (x + 3)(x + 7) = 0.",
                             "The roots are x = −3 and x = −7.",
                             "Completing the square gives (x + 5)² = 4, so x = −5 ± 2, the same "
                             "roots.",
                             "The formula gives x = (−10 ± 4)/2, again the same.",
                             "Factorising is quickest here, but completing the square also "
                             "shows the vertex at (−5, −4)."],
                      ans="x = −3 or x = −7; factorising is quickest, completing the square is "
                          "most informative",
                      interp="The fastest method and the most informative method are not "
                             "always the same, and the choice depends on the purpose."),
                 dict(q="A model of a company's profit is P = −2x² + 40x − 150. Find the "
                        "maximum profit and the number of items that gives it, using the "
                        "method that shows the most.",
                      vis=F("grid", [(10, 50), (5, 0), (15, 0)], ["max", "r1", "r2"], 0, 18, -60,
                            60, [(5, 0), (7.5, 37.5), (10, 50), (12.5, 37.5), (15, 0)],
                            "the profit parabola with its maximum at x = 10"),
                      reasoning="The factorised or vertex form shows the maximum immediately.",
                      steps=["P = −2x² + 40x − 150 = −2(x² − 20x + 75).",
                             "Now x² − 20x + 75 = (x − 5)(x − 15), so P = −2(x − 5)(x − 15).",
                             "The roots are 5 and 15, so the maximum is at x = 10.",
                             "At x = 10, P = −2(25) + 400 − 150 = 50.",
                             "The maximum profit is 50 dollars at 10 items, and the company "
                             "loses money below 5 or above 15 items."],
                      ans="maximum profit 50 dollars at 10 items; break-even at 5 and 15 items",
                      interp="The factorised form gave the break-even points and the maximum "
                             "in one step, which the expanded form did not.")
             ], inv=dict(
                 task="Take ten quadratics of your own. Compute b² − 4ac for each before "
                      "solving, predict the number and the type of roots, then solve and "
                      "check whether the prediction held. Finally find the value of k for "
                      "which x² + kx + 9 has a repeated root.",
                 table=[["quadratic", "discriminant", "prediction", "roots"],
                        ["x² − 5x + 6", "1", "two rational", "2, 3"],
                        ["x² + 4x + 4", "0", "one repeated", "−2"],
                        ["x² + x + 1", "−3", "no real roots", "none"],
                        ["2x² − 3x + 1", "1", "two rational", "½, 1"],
                        ["x² − 2", "8", "two irrational", "±√2"]],
                 notice=["A perfect-square discriminant always gave rational roots.",
                         "A zero discriminant gave exactly one repeated root.",
                         "A negative discriminant gave no real roots, and the parabola "
                         "missed the axis.",
                         "The repeated-root condition b² = 4ac gave k = ±6 for "
                         "x² + kx + 9."],
                 obs="The discriminant reports the number and the type of the real roots, and "
                     "it agrees with the graph in every case.",
                 concl="The discriminant is the quickest test of a quadratic's roots, and "
                       "setting it to zero is how a parameter is chosen for a repeated root.")),
    ],
    practice=dict(
        A=[("5.1.1", "Expand (x + 5)(x − 2).", "x² + 3x − 10",
            "Multiply every term of one bracket by every term of the other.", "F"),
           ("5.1.2", "Expand (2x + 3)².", "4x² + 12x + 9",
            "Use a² + 2ab + b² with a = 2x, b = 3.", "F"),
           ("5.1.3", "Solve x² − 9x + 20 = 0 by factorising.", "x = 4 or x = 5",
            "Two numbers with sum 9 and product 20.", "F"),
           ("5.1.4", "Solve x² − 7x = 0.", "x = 0 or x = 7", "Take out the common factor x.",
            "F"),
           ("5.1.5", "Solve 2x² − 50 = 0.", "x = ±5", "A difference of two squares.", "F"),
           ("5.1.6", "Complete the square for x² + 8x + 3.", "(x + 4)² − 13",
            "Add and subtract 16.", "F"),
           ("5.1.7", "Find the discriminant of x² + 4x + 5.", "−4",
            "b² − 4ac = 16 − 20.", "F"),
           ("5.1.8", "Solve x² + 6x + 5 = 0.", "x = −1 or x = −5",
            "Two numbers with sum 6 and product 5.", "F"),
           ("5.1.9", "Solve 3x² − 12 = 0.", "x = ±2", "Divide by 3, then take roots.", "F"),
           ("5.1.10", "Find the vertex of y = x² − 6x + 1.", "(3, −8)",
            "Complete the square.", "F"),
           ("5.1.11", "Solve x² + 2x − 8 = 0 using the formula.",
            "x = 2 or x = −4", "b² − 4ac = 4 + 32 = 36.", "F"),
           ("5.1.12", "Solve (x − 2)² = 9.", "x = 5 or x = −1",
            "Take square roots of both sides.", "F")],
        B=[("5.2.1", "The areas of a sequence of squares are 1, 4, 9, 16. Find the rule for "
            "the nth area and test it on the seventh square.",
            "n², giving 49 for the seventh.", "The areas are the square numbers.", "R"),
           ("5.2.2", "Investigate the pattern in the sums of the first n square numbers and "
            "justify the general rule.",
            "n(n + 1)(2n + 1)/6, which can be proved by induction or by a telescoping sum.",
            "Compute the sums and look for a cubic rule.", "C"),
           ("5.2.3", "Conjecture a rule for the difference between consecutive squares and "
            "test it.",
            "(n + 1)² − n² = 2n + 1, the odd numbers.", "Expand the difference.", "R"),
           ("5.2.4", "Investigate the pattern in the number of rectangles in an n by n grid "
            "and justify it.",
            "n²(n + 1)²/4, because a rectangle is fixed by two vertical and two horizontal "
            "lines.", "Count for n = 2 and n = 3.", "C"),
           ("5.2.5", "Build a table of the roots of x² + bx + 1 = 0 for b = 2 to 6 and "
            "describe the pattern.",
            "The roots are always negative and get closer together as b grows.",
            "Use the formula.", "R"),
           ("5.2.6", "Conjecture a rule for the maximum product of two numbers with a fixed "
            "sum and justify it.",
            "The maximum is at equal numbers, because x(S − x) is a parabola with vertex at "
            "S/2.", "Write the product as a quadratic.", "R"),
           ("5.2.7", "Investigate the pattern in the discriminants of x² + nx + (n + 1) and "
            "state when real roots exist.",
            "n² − 4n − 4, which is non-negative for n ≥ 2 + 2√2.",
            "Compute the discriminant and solve the inequality.", "R"),
           ("5.2.8", "A pattern of nested squares has side lengths following the rule "
            "s = 1 + 1/n. Investigate the areas and their limit.",
            "The areas approach 1 from above, so the limit is 1.",
            "Compute for n = 1 to 10.", "C"),
           ("5.2.9", "Find the pattern in the heights h = 20t − 5t² at t = 0, 1, 2, 3, 4 and "
            "justify the shape.",
            "The heights rise to a maximum at t = 2 then fall, as a parabola requires.",
            "Compute the values and compare with the vertex.", "R"),
           ("5.2.10", "Investigate the pattern in the roots of x² − 2x − k = 0 as k grows.",
            "One root grows and the other falls, and the discriminant is 4 + 4k, so real roots "
            "exist for all k ≥ −1.", "Use the formula.", "R"),
           ("5.2.11", "Conjecture a rule for the number of regions into which n lines divide "
            "a plane when no two are parallel and no three meet.",
            "n(n + 1)/2 + 1, because each new line is cut into n + 1 pieces.",
            "Count for n = 1, 2, 3, 4.", "R")],
        C=[("5.3.1", "Explain in your own words what the discriminant is and what it decides.",
            "The quantity b² − 4ac, whose sign decides whether a quadratic has two, one or no "
            "real roots.", "State the definition and the three cases.", "R"),
           ("5.3.2", "Write a complete solution to x² + 4x − 5 = 0 by completing the square.",
            "x = 1 or x = −5", "Rewrite as (x + 2)² = 9.", "F"),
           ("5.3.3", "Choose between factorising and the formula for 2x² + 7x + 3 and justify.",
            "The formula, because the leading coefficient is not 1 and the factorisation is not "
            "obvious.", "Say what each method costs.", "R"),
           ("5.3.4", "Set out a full solution to 3x² + 2x − 4 = 0, giving roots to three "
            "significant figures.",
            "x ≈ 0.914 or x ≈ −1.46", "Use the formula and round once.", "F"),
           ("5.3.5", "Explain why a negative discriminant means there are no real roots.",
            "Because the square root of a negative number is not a real number, so the formula "
            "cannot produce a real root.", "Look at the formula.", "R"),
           ("5.3.6", "Describe, with an example, the difference between a repeated root and "
            "two equal-looking roots.",
            "A repeated root is one value counted twice, as in (x − 2)² = 0; two roots are "
            "different values, as in x² − 4 = 0.", "Compare the discriminants.", "R"),
           ("5.3.7", "Explain why completing the square works for every quadratic.",
            "Because half the coefficient of x can always be squared and then subtracted, "
            "which leaves the value unchanged.", "Show the general step.", "R"),
           ("5.3.8", "Write the reasoning that shows the vertex of y = ax² + bx + c is at "
            "x = −b/(2a).",
            "Completing the square gives a(x + b/2a)² + …, whose square term is zero at "
            "x = −b/(2a).", "Complete the square generally.", "R"),
           ("5.3.9", "Set out the argument that the maximum product of two numbers with a "
            "fixed sum occurs when they are equal.",
            "The product x(S − x) = Sx − x² is a downward parabola with vertex at S/2, so the "
            "maximum is at x = S/2.", "Use the symmetry of the roots.", "R"),
           ("5.3.10", "Explain what a root of a model means in a real situation.",
            "The value of the variable at which the modelled quantity is zero — the "
            "break-even point, the landing time, or the empty moment.",
            "Give a real example.", "R"),
           ("5.3.11", "Describe the relationship between the roots of a quadratic and the "
            "x-intercepts of its graph.", "They are the same: a root is a value of x for which "
            "y = 0, which is exactly an x-intercept.", "Set y = 0.", "R"),
           ("5.3.12", "Explain, with an example, why a root of an equation may not be an "
            "acceptable answer.", "A negative time or a negative length is a root of the "
            "equation but not of the situation, as with t = −1 in a motion model.",
            "Check the domain.", "R")],
        D=[("5.4.1", "A ball is thrown from a 20 m cliff with height h = 20 + 18t − 5t². Find "
            "when it hits the ground and its greatest height.",
            "It hits the ground after about 4.85 s and reaches about 36.2 m.",
            "Solve h = 0 and find the vertex.", "A"),
           ("5.4.2", "A rectangular garden has a perimeter of 60 m. Find the dimensions of "
            "greatest area and the area.",
            "15 m by 15 m, giving 225 m².", "Write the area as a quadratic in one side.", "A"),
           ("5.4.3", "A company's profit is P = −3x² + 120x − 800. Find the break-even values "
            "and the maximum profit.",
            "Break-even at about 8.45 and 31.5 items; maximum profit 400 dollars at 20 items.",
            "Factorise or use the vertex.", "A"),
           ("5.4.4", "A bridge arch is modelled by y = −0.02x² + 0.8x. Find its greatest "
            "height and the width at the base.",
            "Greatest height 8 m at x = 20; the base is 40 m wide.",
            "Find the vertex and the roots.", "A"),
           ("5.4.5", "A rectangle has area 48 m² and one side 2 m longer than the other. Find "
            "the dimensions.",
            "6 m by 8 m.", "Write x(x + 2) = 48 and solve.", "A"),
           ("5.4.6", "A rocket's height is h = 40t − 8t². Find when it returns to the ground "
            "and its greatest height.",
            "It returns after 5 s and reaches 50 m.", "Solve h = 0 and find the vertex.", "A"),
           ("5.4.7", "A hall's seating revenue is R = x(30 − x) for a ticket price of x "
            "dollars. Investigate whether a revenue of 200 dollars is possible and justify.",
            "Yes: x² − 30x + 200 = 0 gives x = 10 or x = 20.",
            "Solve the quadratic and check both roots.", "R"),
           ("5.4.8", "A photograph is 20 cm by 15 cm and is surrounded by a frame of uniform "
            "width with area 136 cm². Find the width.",
            "2 cm.", "Write (20 + 2w)(15 + 2w) = 436 and solve.", "A"),
           ("5.4.9", "A ball is thrown so that h = 1.5 + 14t − 5t². Investigate whether it "
            "clears a 12 m wall and justify.",
            "Yes: the maximum is 11.3 m, so it does not clear a 12 m wall.",
            "Compare the maximum with the wall height.", "R"),
           ("5.4.10", "A field is divided into two rectangles with a total perimeter of 80 m. "
            "Investigate the division that maximises the total area and justify.",
            "The maximum occurs when the two rectangles are equal, because the area is a "
            "downward parabola in the dividing position.",
            "Write the area as a quadratic.", "C"),
           ("5.4.11", "A company finds that its cost is C = 2x² + 60x + 500 and its revenue is "
            "R = 100x. Find the production level that maximises profit and the profit.",
            "x = 10 items, with profit 150 dollars.",
            "Write the profit as a quadratic and find the vertex.", "A"),
           ("5.4.12", "Explain, with a model of your own, when a quadratic model is a poor "
            "description of a situation.",
            "Any answer is acceptable if it identifies air resistance, a fixed capacity, or a "
            "rate that is not constant.", "Give a specific counterexample.", "R")],
    ),
    assessment=[
        dict(title="A1 · The water fountain",
             text="A fountain shoots water upwards from ground level with height "
                  "h = 24t − 6t² metres after t seconds. Find the greatest height reached, the "
                  "time at which it occurs, the times at which the water is 18 m high, and the "
                  "time at which it returns to the ground. Justify each answer with the method "
                  "you used.",
             note="Criteria A and C · solve each quadratic and state the domain that makes the "
                  "answers meaningful."),
        dict(title="A2 · The parameter problem",
             text="The equation kx² − 4x + 1 = 0 has real roots for some values of k and not "
                  "for others. Find the values of k for which it has two distinct real roots, "
                  "one repeated root and no real roots, and explain why k = 0 must be excluded "
                  "from your answer.",
             note="Criteria B and D · use the discriminant to justify each case and state the "
                  "condition on k."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of logic and the related concepts of equivalence, "
        "generalisation and justification appear in your work?",
        "How is the global context of scientific and technical innovation, and its exploration of "
        "design, motion and optimisation, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a quadratic model for motion or profit, and what would you "
        "still like to ask?",
    ],
    review=dict(
        ideas=["(a + b)² = a² + 2ab + b² and (a − b)² = a² − 2ab + b².",
               "a² − b² = (a + b)(a − b) is the difference of two squares.",
               "Every quadratic can be written as a(x + p)² + q.",
               "The quadratic formula solves ax² + bx + c = 0 for any a ≠ 0.",
               "b² − 4ac > 0 gives two roots, = 0 gives one, < 0 gives none.",
               "The vertex of a parabola is at x = −b/(2a).",
               "The roots of a model must lie inside the domain of the situation.",
               "The best method depends on the coefficients and on the question."],
        vocab=["perfect square", "cross term", "complete the square", "vertex",
               "axis of symmetry", "quadratic formula", "discriminant", "repeated root",
               "parabola", "domain", "projectile", "optimisation"],
        mixed=[("5.R1", "Expand (3x − 4)(x + 2)."),
               ("5.R2", "Solve x² − 8x + 12 = 0."),
               ("5.R3", "Write x² − 10x + 7 in completed square form."),
               ("5.R4", "Find the discriminant of 2x² + 3x + 5 and state the nature of the "
                        "roots."),
               ("5.R5", "Solve 2x² + 5x − 3 = 0 using the formula."),
               ("5.R6", "Find the maximum value of 12x − 3x² and the x that gives it.")],
    ),
    projects=dict(
        service=[("Community need", "Optimisation decisions in design and sport are made "
                                    "without showing the model."),
                 ("Mathematical connection", "Quadratic models, vertices and discriminants."),
                 ("Proposed action", "Model one real optimisation and publish the model with "
                                     "its answer."),
                 ("Expected impact", "A reader can see why the best choice is the best."),
                 ("Student reflection", "Record the model, the solution and the check.")],
        community=[("Project idea", "An optimisation audit of the school's own spaces."),
                   ("Need", "Room layouts, timetables and budgets are decided by guesswork."),
                   ("Research question", "Which layout or allocation maximises a stated "
                                         "quantity, and what does the model assume?"),
                   ("Mathematics", "Quadratic models, vertices and the discriminant."),
                   ("Action or outcome", "A one-page report with the model and the optimum."),
                   ("Beneficiaries", "Everyone who uses the space."),
                   ("Evidence", "The report with the model, the vertex and the check.")],
        personal=[("Personal interest", "Sport, gaming or a design you enjoy."),
                  ("Learning goal", "To model an optimisation you care about and justify the "
                                    "answer."),
                  ("Product or outcome", "A quadratic model with a maximum or minimum found "
                                         "and checked."),
                  ("Mathematics", "Completing the square, the formula and the discriminant."),
                  ("Process", "Build the model, solve it, and check the root against the "
                              "situation."),
                  ("Evidence", "The model, the solution and the check.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=6, title="Quadratic Functions and Graphical Reasoning",
    key="Form", related=["Representation", "Change", "Pattern"],
    context="Orientation in space and time",
    exploration="Arches, paths and trajectories",
    inquiry=("The graph of a function is a representation that shows change at a glance — "
             "where a quantity rises and falls, where it is greatest, and how it behaves far "
             "from the origin — and reading that representation is a form of reasoning that "
             "the equation alone does not provide."),
    atl=("Communication",
         "Students read a graph, a table and an equation of the same function, and explain "
         "in words what each shows about the change it describes."),
    standfirst="A parabola is the graph of a quadratic function. Its shape is fixed, and every "
               "other parabola is obtained from it by a shift, a stretch or a reflection.",
    engage="A garden arch follows the curve y = −0.2x² + 2. How wide is it at ground level, "
           "how high is it in the middle, and how would you draw it without a calculator?",
    questions=[("Factual", "What are the key features of the graph of a quadratic function, "
                           "and how do the coefficients a, b and c affect its shape?"),
               ("Conceptual", "Why does every parabola have the same shape, and how does a "
                              "graph show change that an equation hides?"),
               ("Debatable", "Is a sketch drawn from reasoning more trustworthy than one drawn "
                             "by plotting points, or does precision always require "
                             "computation?")],
    application_lede="Each task asks you to read a graph or to sketch one. State the feature "
                     "you are reading and the evidence for it.",
    projects_lede="Arches, paths and trajectories are parabolas. Model one and show what its "
                  "graph tells you that its equation does not.",
    sections=[
        dict(id="6.1", title="Parabolas and key features",
             inquiry_q="What are the key features of a parabola, and how are they found from "
                       "the equation?",
             teach=[
                 "The graph of y = ax² + bx + c is a parabola. It is symmetric about the vertical line through its vertex, and it opens upwards when a > 0 and downwards when a < 0.",
                 "A pattern in a table of values becomes a shape on a graph, and the representation as a picture is what makes the pattern of change visible.",
                 "The vertex is the maximum or minimum point, and its x-coordinate is −b/(2a). The axis of symmetry is the line x = −b/(2a).",
                 "The y-intercept is c, because setting x = 0 leaves y = c. The x-intercepts, if they exist, are the roots of ax² + bx + c = 0.",
                 "The value of a controls the width: a larger |a| gives a narrower parabola. The value of c moves the whole graph up or down without changing its shape.",
             ], examples=[
                 dict(q="For y = x² − 6x + 5, find the vertex, the axis of symmetry, the "
                        "intercepts, and sketch the graph.",
                      vis=F("grid", [(3, -4), (1, 0), (5, 0), (0, 5)],
                            ["vertex", "root", "root", "y-int"], -1, 7, -6, 7,
                            [(1, 0), (5, 0)],
                            "the parabola y = x² − 6x + 5"),
                      reasoning="Read the intercepts directly, complete the square for the "
                               "vertex, and factorise for the roots.",
                      steps=["The y-intercept is 5, at (0, 5).",
                             "The axis of symmetry is x = −(−6)/2 = 3.",
                             "The vertex is at x = 3, where y = 9 − 18 + 5 = −4, so (3, −4).",
                             "Factorising gives x² − 6x + 5 = (x − 1)(x − 5), so the roots are "
                             "1 and 5.",
                             "The parabola opens upwards, so (3, −4) is a minimum."],
                      ans="vertex (3, −4), axis x = 3, intercepts (0, 5), (1, 0), (5, 0)",
                      interp="Four features and a sketch come from one equation, and each "
                             "feature answers a different question about the function."),
                 dict(q="Compare the graphs of y = x², y = 2x² and y = ½x² on the same axes.",
                      vis=F("grid", [(2, 4), (2, 8), (2, 2)], ["y = x²", "y = 2x²", "y = ½x²"],
                            -3, 3, 0, 10, [(1, 1), (2, 4), (-2, 4)],
                            "the same shape at three widths"),
                      reasoning="All three pass through the origin and are symmetric about the "
                               "y-axis; only the width differs.",
                      steps=["At x = 2 the values are 4, 8 and 2 respectively.",
                             "So y = 2x² rises twice as fast as y = x², and y = ½x² half as "
                             "fast.",
                             "All three pass through (0, 0) and are symmetric about the y-axis.",
                             "The shape is the same in every case; only the scale of the "
                             "y-axis differs.",
                             "A larger leading coefficient means a narrower parabola."],
                      ans="the three graphs have the same shape and vertex but different widths",
                      interp="The leading coefficient changes the width without changing the "
                             "form, which is why every parabola is the same curve at a "
                             "different scale."),
             ], inv=dict(
                 task="Take five quadratic functions with different signs and sizes of a, b "
                      "and c. For each, find the vertex, the axis of symmetry and the "
                      "intercepts, sketch the graph, and record whether the parabola opens up "
                      "or down.",
                 table=[["function", "vertex", "axis", "opens"],
                        ["y = x² − 4", "(0, −4)", "x = 0", "up"],
                        ["y = −x² + 9", "(0, 9)", "x = 0", "down"],
                        ["y = x² + 4x + 3", "(−2, −1)", "x = −2", "up"],
                        ["y = −2x² + 8x − 6", "(2, 2)", "x = 2", "down"],
                        ["y = 3x² + 6x − 2", "(−1, −5)", "x = −1", "up"]],
                 notice=["The sign of a decided the direction of opening in every case.",
                         "The axis of symmetry was always x = −b/(2a).",
                         "The vertex's y-coordinate was the value of the function at the axis.",
                         "The y-intercept was always c, and it moved the graph without "
                         "changing its shape."],
                 obs="The three coefficients decide the direction, the position and the width "
                     "of the parabola, and none of them changes its fundamental shape.",
                 concl="Every quadratic graph is a parabola whose direction, position and width "
                       "are read from a, b and c, so a sketch can be made from the equation "
                       "without plotting any points.")),
        dict(id="6.2", title="Vertex form and transformations",
             inquiry_q="How is one graph obtained from another, and what does each "
                       "transformation do?",
             teach=[
                 "A translation moves every point by the same amount. Replacing y by y − k shifts the graph up by k, and replacing x by x − h shifts it right by h.",
                 "A stretch multiplies distances from the axis. Replacing y by y/a stretches vertically by a, and replacing x by x/a stretches horizontally by a.",
                 "A reflection in the x-axis replaces y by −y, and a reflection in the y-axis replaces x by −x. Both change the direction of the curve.",
                 "Transformations compose, and the order matters for stretches combined with translations. Describing a transformation is a precise use of language that a diagram alone cannot give.",
             ], examples=[
                 dict(q="Describe the transformation that maps y = x² to y = (x − 3)² + 2, and "
                        "find the new vertex.",
                      vis=F("grid", [(0, 0), (3, 2)], ["old vertex", "new vertex"], -2, 7, -2, 7,
                            [(1, 1), (4, 3)],
                            "a translation by (3, 2)"),
                      reasoning="Compare the two equations term by term.",
                      steps=["The term (x − 3)² is x² shifted 3 units to the right.",
                             "The + 2 outside the bracket shifts the graph 2 units up.",
                             "So the transformation is a translation by the vector (3, 2).",
                             "The vertex moves from (0, 0) to (3, 2).",
                             "The shape is unchanged, because no stretch or reflection is "
                             "involved."],
                      ans="a translation by (3, 2); the new vertex is (3, 2)",
                      interp="Reading the transformation from the equation is faster than "
                             "plotting points, and it gives the vertex immediately."),
                 dict(q="Sketch y = −2(x + 1)² + 8, stating each transformation from y = x².",
                      vis=F("grid", [(-1, 8), (1, 0), (-3, 0)],
                            ["vertex", "root", "root"], -5, 3, -4, 10, [(1, 0), (-3, 0)],
                            "a reflected, stretched and translated parabola"),
                      reasoning="Apply the transformations in order from the inside out.",
                      steps=["The bracket (x + 1)² shifts the graph 1 unit to the left.",
                             "The −2 reflects it in the x-axis and stretches it vertically by "
                             "2.",
                             "The + 8 then shifts the whole graph 8 units up.",
                             "The vertex is at (−1, 8), and the parabola opens downwards.",
                             "Setting y = 0 gives (x + 1)² = 4, so the roots are 1 and −3."],
                      ans="left 1, reflect in the x-axis, stretch by 2, up 8; vertex (−1, 8)",
                      interp="The order of the transformations is visible in the equation, and "
                             "reading it from the inside out avoids mistakes."),
             ], inv=dict(
                 task="Take the graph of y = x² and apply six transformations of your own "
                      "choice: two translations, two stretches and two reflections. For each, "
                      "write the equation, sketch the graph, and record the new vertex.",
                 table=[["transformation", "equation", "vertex"],
                        ["up 3", "y = x² + 3", "(0, 3)"],
                        ["right 4", "y = (x − 4)²", "(4, 0)"],
                        ["stretch 3", "y = 3x²", "(0, 0)"],
                        ["reflect in x-axis", "y = −x²", "(0, 0)"],
                        ["left 2, up 5", "y = (x + 2)² + 5", "(−2, 5)"],
                        ["reflect, stretch 2, up 6", "y = −2x² + 6", "(0, 6)"]],
                 notice=["Every translation moved the vertex without changing the shape.",
                         "The stretches changed the width but not the vertex.",
                         "The reflection in the x-axis turned a minimum into a maximum.",
                         "A reflection in the y-axis left y = x² unchanged, because it is "
                         "symmetric."],
                 obs="Translations move the vertex, stretches change the width, and "
                     "reflections reverse the direction, and each transformation is visible in "
                     "the equation.",
                 concl="Any parabola can be obtained from y = x² by a sequence of translations, "
                       "stretches and reflections, and the sequence can be read from the "
                       "equation.")),
        dict(id="6.3", title="Quadratic inequalities",
             inquiry_q="How is the solution of a quadratic inequality found, and why is it a "
                       "region rather than a number?",
             teach=[
                 "A quadratic inequality is solved by first solving the equation, because the roots divide the number line into the intervals where the sign of the quadratic cannot change.",
                 "The sign of the quadratic is then tested in one interval, and the sign of the other intervals follows from the shape of the parabola: it has the same sign throughout each interval between and beyond the roots.",
                 "The solution is a set of values, usually a union of intervals, and it is drawn on a number line as a region. A single value is almost never the answer.",
                 "On the graph the solution is where the parabola lies above or below the x-axis, so the algebra and the picture must give the same region. This is the test that catches a sign error.",
             ], examples=[
                 dict(q="Solve x² − 6x + 5 < 0, and show the solution on a number line.",
                      vis=F("grid", [(3, -4), (1, 0), (5, 0)], ["vertex", "r1", "r2"], -1, 7,
                            -5, 3, [(1, 0), (2, -3), (3, -4), (4, -3), (5, 0)],
                            "the parabola is below the axis between the roots"),
                      reasoning="Solve the equation first, then test the sign in one interval.",
                      steps=["x² − 6x + 5 = 0 gives (x − 1)(x − 5) = 0, so x = 1 or x = 5.",
                             "The roots divide the line into three intervals: x < 1, 1 < x < 5 "
                             "and x > 5.",
                             "Test x = 3: 9 − 18 + 5 = −4, which is negative, so the middle "
                             "interval satisfies the inequality.",
                             "The parabola opens upwards, so it is positive outside the roots "
                             "and negative between them.",
                             "Hence the solution is 1 < x < 5, drawn as the open interval "
                             "between 1 and 5."],
                      ans="1 < x < 5",
                      interp="The roots are the boundary of the solution, and the sign between "
                             "them is the sign that the inequality asks for."),
                 dict(q="Solve x² + 2x − 8 ≥ 0.",
                      vis=F("grid", [(-1, -9), (-4, 0), (2, 0)], ["vertex", "r1", "r2"], -5, 3,
                            -10, 2, [(-4, 0), (-2.5, -6.75), (-1, -9), (0.5, -6.75), (2, 0)],
                            "the parabola is above the axis outside the roots"),
                      reasoning="Factorise, find the roots, then decide which intervals are "
                               "positive.",
                      steps=["x² + 2x − 8 = (x + 4)(x − 2) = 0, so x = −4 or x = 2.",
                             "Test x = 0: 0 + 0 − 8 = −8, which is negative.",
                             "So the middle interval is negative and the two outer intervals "
                             "are positive.",
                             "The inequality allows equality, so the roots are included.",
                             "Hence the solution is x ≤ −4 or x ≥ 2."],
                      ans="x ≤ −4 or x ≥ 2",
                      interp="An inequality that allows equality includes the roots, and the "
                             "solution is a union of two intervals rather than one."),
             ], inv=dict(
                 task="Take six quadratic inequalities of your own, including one with a "
                      "negative leading coefficient, one with no real roots, one with a "
                      "repeated root, and one whose solution is a single interval. Solve "
                      "each, draw the solution on a number line, and sketch the parabola to "
                      "confirm the region.",
                 table=[["inequality", "roots", "solution", "region"],
                        ["x² − 4 < 0", "−2, 2", "−2 < x < 2", "one interval"],
                        ["x² + 1 > 0", "none", "all x", "whole line"],
                        ["x² − 4x + 4 ≥ 0", "2", "all x", "whole line"],
                        ["−x² + x + 6 > 0", "−2, 3", "−2 < x < 3", "one interval"],
                        ["x² − x − 6 < 0", "−2, 3", "−2 < x < 3", "one interval"]],
                 notice=["The roots always formed the boundary of the solution.",
                         "A negative leading coefficient reversed the region.",
                         "A quadratic with no real roots was either always positive or "
                         "always negative, so the answer was every value or none.",
                         "The repeated root gave a parabola that touched the axis, so the "
                         "region was the whole line."],
                 obs="A quadratic inequality is solved by finding the roots and testing the "
                     "sign of one interval, and the answer is a region of the number line.",
                 concl="The roots of the equation divide the number line into intervals of "
                       "constant sign, and the solution of an inequality is the set of "
                       "intervals whose sign the inequality asks for.")),
        dict(id="6.4", title="Optimisation and modelling",
             inquiry_q="How is a graph used to answer a question that the equation asks badly?",
             teach=[
                 "A graph answers questions about comparison, about trend and about limits, and it answers them faster than an equation.",
                 "Two graphs on the same axes answer questions about which is larger, where they cross, and how the gap changes.",
                 "The intersection of two graphs is the solution of the equation obtained by setting them equal, so the graphical and algebraic methods are the same.",
                 "A graph drawn from a model carries the model's assumptions. Drawing a smooth curve through scattered data asserts a relationship that the data may not support.",
             ], examples=[
                 dict(q="A company's revenue is R = 40x − 2x² and its cost is C = 10x + 100. "
                        "Draw both graphs on the same axes and find the values of x for which "
                        "the company makes a profit.",
                      vis=F("grid", [(7.5, 165), (15, 150), (4.7, 147)],
                            ["max R", "C", "cross"], 0, 20, 0, 220,
                            [(0, 100), (20, 300)],
                            "revenue is a parabola, cost is a line"),
                      reasoning="Set the two models equal to find the crossing points, and read "
                               "the profit region from the graphs.",
                      steps=["Setting 40x − 2x² = 10x + 100 gives 2x² − 30x + 100 = 0.",
                             "Dividing by 2 gives x² − 15x + 50 = 0, so (x − 5)(x − 10) = 0.",
                             "The graphs cross at x = 5 and x = 10.",
                             "Between these values the parabola is above the line, so the "
                             "company makes a profit.",
                             "The maximum profit is at x = 7.5, halfway between the two "
                             "crossings."],
                      ans="a profit is made for 5 < x < 10 items, with the maximum at x = 7.5",
                      interp="The graphs show the region of profit at a glance, and the "
                             "equation gives its exact boundaries."),
                 dict(q="A bridge arch is modelled by y = −0.05x² + 1.2x. Find the span of "
                        "the arch and its greatest height, and say what the model assumes.",
                      vis=F("grid", [(12, 7.2), (0, 0), (24, 0)], ["max", "end", "end"],
                            -2, 26, -2, 10, [(0, 0), (24, 0)],
                            "the arch as a parabola"),
                      reasoning="The roots give the span and the vertex gives the height.",
                      steps=["Setting y = 0 gives x(−0.05x + 1.2) = 0, so x = 0 or x = 24.",
                             "The span is therefore 24 m.",
                             "The vertex is at x = 12, where y = −0.05(144) + 14.4 = 7.2 m.",
                             "The greatest height is 7.2 m at the middle of the span.",
                             "The model assumes a parabolic arch, which is an idealisation of "
                             "any real structure."],
                      ans="span 24 m, greatest height 7.2 m",
                      interp="The model is an idealisation, and the graph makes the "
                             "idealisation visible so that its limits can be discussed."),
             ], inv=dict(
                 task="Choose two real quantities that can be modelled on the same axes — "
                      "income and spending, height and weight, distance and time. Draw both "
                      "graphs, find where they cross if they do, and state what the crossing "
                      "means and what the graphs do not show.",
                 table=[["pair", "crossing", "meaning", "not shown"],
                        ["revenue and cost", "break-even", "no profit, no loss", "fixed costs "
                         "detail"],
                        ["distance and time", "none", "different quantities", "the speed"],
                        ["height and age", "several", "growth spurts", "the cause"]],
                 notice=["Two graphs on the same axes answer questions neither answers alone.",
                         "The crossing point had a clear meaning in one case and none in "
                         "another.",
                         "Different quantities on the same axes can mislead if the scales "
                         "differ.",
                         "The graphs showed correlation but never cause."],
                 obs="Graphs are compared by placing them on the same axes, and the crossing "
                     "point is the solution of the equation that sets the two models equal.",
                 concl="A graph is used to answer questions about comparison and trend, and its "
                       "answers are limited by the assumptions of the model it was drawn "
                       "from.")),
        dict(id="6.5", title="Comparing models",
             inquiry_q="How does a graph show growth that is not linear?",
             teach=[
                 "An exponential function has the form y = a·bˣ with b > 0 and b ≠ 1. Its graph rises or falls at a rate proportional to its own value.",
                 "Exponential growth is faster than any linear growth in the long run, because the rate itself grows. This is the difference between adding and multiplying.",
                 "The y-intercept is a, because b⁰ = 1. The graph never crosses the x-axis, so the x-axis is a horizontal asymptote.",
                 "Halving and doubling are the two most common exponential models, and their graphs are mirror images in the y-axis.",
             ], examples=[
                 dict(q="Compare the values of y = 10x and y = 2ˣ for x = 0 to 10, and say "
                        "which grows faster and where they cross.",
                      vis=F("grid", [(6, 60), (10, 100)], ["linear", "exponential"], 0, 10, 0,
                            100, [(0, 0), (10, 100)],
                            "the line is overtaken by the curve"),
                      reasoning="Compute both values and compare, then find the crossing point "
                               "by solving.",
                      steps=["At x = 0 the values are 0 and 1, so the line is lower.",
                             "At x = 5 the values are 50 and 32, so the line is higher.",
                             "At x = 10 the values are 100 and 1024, so the curve is far "
                             "higher.",
                             "Solving 2ˣ = 10x gives x ≈ 1.4 and x ≈ 6.6.",
                             "Beyond x = 6.6 the exponential is always larger, and the gap "
                             "grows without limit."],
                      ans="the exponential overtakes the line at about x = 6.6 and then grows "
                          "far faster",
                      interp="A linear model and an exponential model can agree for a while and "
                             "then diverge completely, which is why the choice of model "
                             "matters."),
                 dict(q="A car loses 15% of its value each year from 20 000 dollars. Model "
                        "the value and find it after 5 years and after 10 years.",
                      vis=F("table", [["year", "value"],
                                      ["0", "20000"],
                                      ["1", "17000"],
                                      ["2", "14450"],
                                      ["5", "8874"],
                                      ["10", "3932"]],
                            caption="Each year multiplies the previous value by 0.85."),
                      reasoning="Repeated multiplication by a constant factor is an exponential "
                               "model.",
                      steps=["The multiplier is 1 − 0.15 = 0.85.",
                             "So the model is V = 20000 × 0.85ⁿ.",
                             "After 5 years, V = 20000 × 0.85⁵ ≈ 8874 dollars.",
                             "After 10 years, V = 20000 × 0.85¹⁰ ≈ 3932 dollars.",
                             "The value falls quickly at first and then more slowly, which the "
                             "graph shows as a curve flattening out."],
                      ans="V = 20000 × 0.85ⁿ; about 8874 dollars after 5 years and 3932 dollars "
                          "after 10",
                      interp="The model never reaches zero, so a car always has some value in "
                             "the model even though it does not in reality."),
             ], inv=dict(
                 task="Take three quantities that change by a fixed percentage each period: "
                      "one growing, one decaying, and one of your own. Model each "
                      "exponentially, tabulate six values, sketch the graph, and compare with "
                      "the linear model that starts at the same point.",
                 table=[["period", "exponential", "linear comparison"],
                        ["0", "1", "1"],
                        ["1", "1.5", "1.5"],
                        ["2", "2.25", "2"],
                        ["3", "3.375", "2.5"],
                        ["4", "5.06", "3"],
                        ["5", "7.59", "3.5"]],
                 notice=["The two models agreed at the first period and then diverged.",
                         "The exponential grew faster than the linear model at every later "
                         "period.",
                         "The decaying model fell quickly at first and then slowly.",
                         "The multiplier was the same at every step, which is the defining "
                         "property."],
                 obs="An exponential model changes by a constant multiplier, so its graph "
                     "curves away from any linear model that starts at the same point.",
                 concl="Exponential growth and decay are modelled by repeated multiplication, "
                       "and their graphs separate from linear models without limit.")),
        dict(id="6.6", title="Investigation: arches and trajectories",
             inquiry_q="What does the graph of a trajectory show, and what does it leave out?",
             teach=[
                 "A trajectory is a parabola under gravity alone, and its graph shows the highest point, the range and the symmetry of the flight.",
                 "Air resistance, spin and wind all change a real trajectory, and a parabolic model is a first approximation that is often good enough.",
                 "The graph shows position but not velocity, and the two are related by the gradient: the velocity is zero at the highest point.",
                 "Reading a trajectory means stating what the model assumes, and a reader who does not know the assumptions can be misled by the picture.",
             ], examples=[
                 dict(q="A ball is kicked from the ground at an angle, and its height is "
                        "h = 1.2x − 0.06x² metres when it is x metres from the kicker. Find "
                        "the greatest height and the horizontal distance when it lands.",
                      vis=F("grid", [(10, 6), (0, 0), (20, 0)], ["max", "kick", "land"],
                            0, 22, -1, 8, [(0, 0), (20, 0)],
                            "the trajectory as a parabola"),
                      reasoning="The vertex gives the greatest height and the second root gives "
                               "the landing distance.",
                      steps=["The parabola opens downwards, so it has a maximum.",
                             "The axis of symmetry is x = −1.2/(2 × −0.06) = 10.",
                             "At x = 10 the height is 12 − 6 = 6 m, the greatest height.",
                             "Setting h = 0 gives x(1.2 − 0.06x) = 0, so x = 0 or x = 20.",
                             "The ball lands 20 m from the kicker, twice the distance of the "
                             "highest point."],
                      ans="greatest height 6 m at 10 m; it lands at 20 m",
                      interp="The symmetry of the parabola means the landing distance is twice "
                             "the distance of the highest point, which is a fact about parabolas "
                             "rather than about football."),
                 dict(q="A graph of a trajectory is symmetric about x = 10. The ball is at "
                        "height 4 m at x = 4. Find the other point at which it is 4 m high, "
                        "and explain why this works.",
                      vis=F("grid", [(10, 6), (4, 4), (16, 4)], ["max", "4 m", "4 m"],
                            0, 20, 0, 8, [(4, 4), (16, 4)],
                            "symmetry gives the second point"),
                      reasoning="Symmetry about the axis means points at equal height are "
                               "equally spaced from it.",
                      steps=["The axis of symmetry is x = 10.",
                             "The point (4, 4) is 6 units to the left of the axis.",
                             "By symmetry there is a point 6 units to the right, at x = 16.",
                             "So the ball is also 4 m high at x = 16.",
                             "This works for any height, which is what symmetry means."],
                      ans="the ball is 4 m high again at x = 16",
                      interp="Symmetry is a property of the graph that can be used instead of "
                             "solving the equation, and it is a check on any calculation."),
             ], inv=dict(
                 task="Model the flight of a ball, a stone or a water jet with a quadratic. "
                      "Find the greatest height, the range and the symmetry, then compare with "
                      "a real throw or a video if you can, and list the differences.",
                 table=[["quantity", "model", "measured", "difference"],
                        ["greatest height", "6 m", "about 5.5 m", "air resistance"],
                        ["range", "20 m", "about 18 m", "air resistance"],
                        ["time of flight", "1.4 s", "about 1.3 s", "air resistance"],
                        ["shape", "symmetric", "slightly asymmetric", "spin and wind"]],
                 notice=["The model overestimated both the height and the range.",
                         "The measured path was not quite symmetric.",
                         "The differences were small for a heavy ball and large for a light "
                         "one.",
                         "The model was still useful, because it predicted the right order of "
                         "magnitude."],
                 obs="A parabolic model of a trajectory is a good first approximation, and its "
                     "errors come from the forces the model leaves out.",
                 concl="The graph of a trajectory shows the height, the range and the symmetry "
                       "of a flight under gravity alone, and its usefulness depends on how "
                       "small the neglected forces are.")),
    ],
    practice=dict(
        A=[("6.1.1", "Find the vertex of y = x² − 4x + 7.", "(2, 3)",
            "Complete the square or use x = −b/(2a).", "F"),
           ("6.1.2", "Find the y-intercept of y = 2x² − 5x + 3.", "3",
            "Set x = 0.", "F"),
           ("6.1.3", "State whether y = −3x² + 6 opens up or down.", "down",
            "The sign of a decides.", "F"),
           ("6.1.4", "Find the axis of symmetry of y = x² + 8x + 3.", "x = −4",
            "Use x = −b/(2a).", "F"),
           ("6.1.5", "Find the roots of y = x² − 9.", "x = ±3",
            "A difference of two squares.", "F"),
           ("6.1.6", "Describe the transformation from y = x² to y = x² − 5.",
            "a translation 5 units down", "The constant term shifts the graph vertically.", "F"),
           ("6.1.7", "Describe the transformation from y = x² to y = (x + 4)².",
            "a translation 4 units left", "The bracket shifts the graph horizontally.", "F"),
           ("6.1.8", "Find the vertex of y = (x − 2)² + 6.", "(2, 6)",
            "Read it from the completed square form.", "F"),
           ("6.1.9", "Find the y-intercept of y = 3 × 2ˣ.", "3",
            "Set x = 0, since 2⁰ = 1.", "F"),
           ("6.1.10", "Evaluate 5 × 0.8³.", "2.56", "Multiply by the cube of the multiplier.",
            "F"),
           ("6.1.11", "Find the roots of y = x² + x − 12.", "x = 3 or x = −4",
            "Factorise as (x − 3)(x + 4).", "F"),
           ("6.1.12", "State the greatest value of y = −(x − 1)² + 4.", "4",
            "The vertex of a downward parabola is its maximum.", "F")],
        B=[("6.2.1", "The heights of a bouncing ball are 2, 1.6, 1.28, 1.024 m. Find the rule "
            "for the nth height and test it on the sixth bounce.",
            "2 × 0.8ⁿ⁻¹, giving about 0.655 m for the sixth.",
            "The common ratio is 0.8.", "R"),
           ("6.2.2", "Investigate the pattern in the number of regions made by n lines through "
            "a single point.",
            "2n regions, because each line cuts all the others at one point.",
            "Draw for n = 1, 2, 3.", "R"),
           ("6.2.3", "Conjecture a rule for the sum of the first n powers of 2 and justify it.",
            "2ⁿ − 1, because the sum telescopes or because each new term doubles the total and "
            "adds one.", "Compute the sums and prove by induction.", "R"),
           ("6.2.4", "Investigate the pattern in the areas under the parabola y = x² between "
            "x = 0 and x = 1, 2, 3.",
            "The areas are 1/3, 8/3 and 9, following x³/3.",
            "Use the known formula for the area under a parabola.", "C"),
           ("6.2.5", "Build a table of the values of y = 2ˣ for x = −3 to 3 and describe the "
            "pattern.",
            "The values double as x rises by 1 and halve as it falls by 1.",
            "Compute the values.", "R"),
           ("6.2.6", "Conjecture a rule for the width of the parabola y = kx² at a height of "
            "1 unit.",
            "The width is 2/√k, because x² = 1/k at height 1.",
            "Set y = 1 and solve.", "R"),
           ("6.2.7", "Investigate the pattern in the number of intersection points of "
            "y = x² and y = nx for n = 1 to 5.",
            "Two intersections for every positive n, at x = 0 and x = n.",
            "Set the two equal and solve.", "R"),
           ("6.2.8", "A ball's rebound heights follow a geometric sequence. Investigate the "
            "total distance travelled before it comes to rest.",
            "The total is finite even though the number of bounces is infinite, because the "
            "heights form a convergent series.", "Sum the geometric series.", "C"),
           ("6.2.9", "Find the pattern in the gradients of y = x² at x = 1, 2, 3 and justify "
            "the rule.",
            "The gradients are 2, 4, 6, following 2x.",
            "Use chords that get shorter.", "R"),
           ("6.2.10", "Investigate the pattern in the maximum height of y = −x² + 2nx for "
            "n = 1 to 5.",
            "The maximum is n², because the vertex is at (n, n²).",
            "Find the vertex for each n.", "R"),
           ("6.2.11", "Conjecture a rule for the number of points with integer coordinates "
            "inside y = x² between x = −n and n.",
            "2n² + 2n + 1, because the parabola encloses one point for each integer pair "
            "inside.", "Count for n = 1, 2, 3.", "R")],
        C=[("6.3.1", "Explain in your own words what the vertex of a parabola is.",
            "The point at which the parabola turns, which is its maximum or minimum.",
            "State the definition and how it is found.", "R"),
           ("6.3.2", "Write a complete solution to: sketch y = x² − 2x − 8, marking the "
            "vertex, the intercepts and the axis of symmetry.",
            "Vertex (1, −9), axis x = 1, intercepts (0, −8), (−2, 0), (4, 0).",
            "Complete the square and factorise.", "F"),
           ("6.3.3", "Choose between a graph and an equation to answer a question about the "
            "greatest value of a quadratic and justify.",
            "The completed square form for an exact value; the graph for a comparison or a "
            "picture of the behaviour.", "Say what each gives.", "R"),
           ("6.3.4", "Set out a full solution to: describe the transformation from y = x² to "
            "y = −(x + 3)² − 1.",
            "Left 3, reflect in the x-axis, down 1.", "Read the equation from the inside out.",
            "F"),
           ("6.3.5", "Explain why every parabola has the same shape.",
            "Because any quadratic can be obtained from y = x² by translations and stretches, "
            "which do not change the form of the curve.", "Use the transformation "
            "description.", "R"),
           ("6.3.6", "Describe, with an example, the difference between a stretch and a "
            "translation.", "A stretch multiplies distances from an axis, as in y = 3x²; a "
            "translation moves every point by the same amount, as in y = x² + 3.",
            "Compare the equations.", "R"),
           ("6.3.7", "Explain why the graph of y = 2ˣ never crosses the x-axis.",
            "Because 2ˣ is always positive for every real x, so y is never zero.",
            "Consider the sign of a power.", "R"),
           ("6.3.8", "Write the reasoning that shows the axis of symmetry of y = ax² + bx + c "
            "is x = −b/(2a).",
            "Completing the square gives a(x + b/2a)² + …, whose square term vanishes at "
            "x = −b/(2a).", "Complete the square generally.", "R"),
           ("6.3.9", "Set out the argument that exponential growth eventually overtakes any "
            "linear growth.",
            "A linear model adds a fixed amount each step while an exponential model "
            "multiplies, so the ratio of the two grows without bound.",
            "Compare a table of values.", "R"),
           ("6.3.10", "Explain what the crossing point of two graphs means.",
            "The value of the variable at which the two models give the same output — the "
            "break-even point or the meeting time.", "Set the two equations equal.", "R"),
           ("6.3.11", "Describe the relationship between a sketch and a plotted graph.",
            "A sketch shows the correct features at the correct places; a plotted graph shows "
            "accurate values at chosen points.", "Compare the two purposes.", "R"),
           ("6.3.12", "Explain, with an example, when a graph can be misleading.",
            "Any answer is acceptable if it identifies unequal scales, a truncated axis, or a "
            "smooth curve drawn through scattered data.", "Give a specific example.", "R")],
        D=[("6.4.1", "A ball is thrown so that its height is h = 12t − 5t². Find the greatest "
            "height, the time at which it occurs, and the time it returns to the ground.",
            "Greatest height 7.2 m at t = 1.2 s; returns at t = 2.4 s.",
            "Find the vertex and the roots.", "A"),
           ("6.4.2", "A bridge arch is modelled by y = −0.04x² + 0.8x. Find the span and the "
            "greatest height.",
            "Span 40 m; greatest height 8 m.", "Find the roots and the vertex.", "A"),
           ("6.4.3", "A shop's revenue is R = 30x − x² and its cost is C = 4x + 96. Find the "
            "range of x for which a profit is made and the maximum profit.",
            "Profit for 4 < x < 26 items; maximum profit 169 dollars at x = 13.",
            "Set the models equal and find the vertex.", "A"),
           ("6.4.4", "A population of 400 grows by 12% per year. Model it, find the "
            "population after 5 years, and find when it doubles.",
            "P = 400 × 1.12ⁿ; about 705 after 5 years; doubles in about 6.1 years.",
            "Use an exponential model and solve.", "A"),
           ("6.4.5", "A radioactive sample decays from 80 g at 20% per year. Model it, find "
            "the mass after 4 years, and find the half-life.",
            "M = 80 × 0.8ⁿ; about 32.8 g after 4 years; half-life about 3.1 years.",
            "Use an exponential model and solve.", "A"),
           ("6.4.6", "A fountain's water follows y = 6x − 0.3x². Find the greatest height and "
            "the horizontal distance when it lands.",
            "Greatest height 30 m at x = 10; lands at x = 20.",
            "Find the vertex and the roots.", "A"),
           ("6.4.7", "A phone's value falls from 900 dollars by 25% per year. Investigate "
            "whether it is worth more than 100 dollars after 6 years and justify.",
            "No: 900 × 0.75⁶ ≈ 191 dollars, so it is worth more than 100 dollars after 6 "
            "years.", "Compute the model.", "R"),
           ("6.4.8", "A field's yield is Y = −2x² + 60x for x kg of fertiliser. Find the "
            "amount giving the greatest yield and the yield.",
            "15 kg, giving 450 units.", "Find the vertex.", "A"),
           ("6.4.9", "A ball is thrown from a window 10 m high with h = 10 + 20t − 5t². "
            "Investigate whether it reaches a height of 30 m and justify.",
            "Yes: the maximum is 30 m exactly, reached at t = 2 s.",
            "Compare the vertex height with 30 m.", "R"),
           ("6.4.10", "Two savings accounts pay 5% simple and 5% compound interest on 1000 "
            "dollars. Investigate when the compound account first gives more, and by how much "
            "after 10 years.",
            "Compound is ahead from year 2 onward; after 10 years the difference is about 133 "
            "dollars.", "Compare the two models.", "C"),
           ("6.4.11", "A ball is kicked with h = 0.6x − 0.02x². Investigate whether it clears "
            "a 4 m wall at x = 12 and justify.",
            "No: h = 7.2 − 2.88 = 4.32 m, so it does clear the wall.",
            "Evaluate the model at x = 12.", "R"),
           ("6.4.12", "Explain, with a model of your own, when a graph drawn from a model is "
            "more useful than the equation.",
            "Any answer is acceptable if it identifies comparison, trend or the shape of "
            "behaviour beyond the data.", "Give a specific example.", "R")],
    ),
    assessment=[
        dict(title="A1 · The garden arch",
             text="A garden arch is modelled by y = −0.08x² + 1.6x metres, where x is the "
                  "horizontal distance from one end. Find the span of the arch, its greatest "
                  "height, and the height at the quarter points. Then sketch the arch and "
                  "state two features of the model that a real arch would not have.",
             note="Criteria A and C · find the roots and the vertex, and comment on the "
                  "model's assumptions."),
        dict(title="A2 · The two savings plans",
             text="Plan A pays 6% simple interest and plan B pays 5% compound interest on a "
                  "deposit of 2000 dollars. Model both, draw the graphs on the same axes, find "
                  "the year in which plan B overtakes plan A, and say which you would choose "
                  "for a 10-year saving.",
             note="Criteria A and D · model both plans, solve for the crossing point, and "
                  "justify the recommendation."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of representation, change and "
        "pattern appear in your work?",
        "How is the global context of orientation in space and time, and its exploration of "
        "arches, paths and trajectories, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a parabolic model of a real path, and what would you still "
        "like to ask?",
    ],
    review=dict(
        ideas=["The graph of y = ax² + bx + c is a parabola.",
               "The vertex is at x = −b/(2a) and is the maximum or minimum.",
               "The y-intercept is c and the x-intercepts are the roots.",
               "A larger |a| gives a narrower parabola.",
               "Translations move the vertex; stretches change the width; reflections reverse "
               "the direction.",
               "An exponential function has the form y = a·bˣ.",
               "The y-axis is an asymptote of an exponential graph.",
               "The crossing point of two graphs solves the equation that sets them equal."],
        vocab=["parabola", "vertex", "axis of symmetry", "intercept", "translation", "stretch",
               "reflection", "asymptote", "exponential", "trajectory", "sketch", "range"],
        mixed=[("6.R1", "Find the vertex and axis of symmetry of y = x² + 6x + 1."),
               ("6.R2", "Describe the transformation from y = x² to y = (x − 5)² + 3."),
               ("6.R3", "Find the greatest value of y = −x² + 8x − 3."),
               ("6.R4", "Evaluate 200 × 1.05⁴."),
               ("6.R5", "Find the roots of y = 2x² + 5x − 3."),
               ("6.R6", "Explain why y = 2ˣ has no x-intercept.")],
    ),
    projects=dict(
        service=[("Community need", "Arches, paths and trajectories are designed without "
                                    "showing the mathematics."),
                 ("Mathematical connection", "Quadratic functions, vertices and graphs."),
                 ("Proposed action", "Model one real arch or path and publish the model with "
                                     "its graph."),
                 ("Expected impact", "A reader sees why the shape works and where it would "
                                     "fail."),
                 ("Student reflection", "Record the model, the graph and the check.")],
        community=[("Project idea", "A shape audit of the school's own architecture."),
                   ("Need", "Arches, roofs and paths are chosen by appearance alone."),
                   ("Research question", "Which quadratic models the shapes we use, and what "
                                         "do they reveal?"),
                   ("Mathematics", "Quadratic functions, transformations and graphs."),
                   ("Action or outcome", "A one-page report with models and sketches of three "
                                         "shapes."),
                   ("Beneficiaries", "Everyone who uses the buildings."),
                   ("Evidence", "The report with the models, the sketches and the checks.")],
        personal=[("Personal interest", "Sport, gaming or a path you travel."),
                  ("Learning goal", "To model a trajectory you care about and read its graph."),
                  ("Product or outcome", "A quadratic model with a graph and its key "
                                         "features."),
                  ("Mathematics", "Parabolas, vertices and symmetry."),
                  ("Process", "Model the path, sketch the graph, and compare with a "
                              "measurement."),
                  ("Evidence", "The model, the graph and the comparison.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=7, title="Patterns, Sequences and Generalisation",
    key="Relationships", related=["Pattern", "Generalisation", "Representation"],
    context="Orientation in space and time",
    exploration="Cycles, growth and prediction",
    inquiry=("A sequence is a pattern in time, and generalising it means finding a rule that "
             "connects the position of a term to its value; the rule is a representation of "
             "the pattern that allows prediction beyond the terms observed, and its "
             "justification is what separates a general claim from a guess."),
    atl=("Critical thinking",
         "Students test a conjectured rule against terms they have not yet used, and revise "
         "the rule when the test fails rather than defending it."),
    standfirst="Arithmetic sequences add a constant; geometric sequences multiply by one. "
               "Quadratic sequences have constant second differences, and each kind has its "
               "own signature.",
    engage="A savings account starts at 100 dollars and grows by 20 dollars a month. Another "
           "grows by 20% a month. After how many months does the second overtake the first?",
    questions=[("Factual", "What are arithmetic, geometric and quadratic sequences, and how is "
                           "the nth term of each found?"),
               ("Conceptual", "Why does a constant second difference signal a quadratic rule, "
                              "and how is a general rule justified?"),
               ("Debatable", "If a rule fits every term observed, is it reasonable to use it "
                             "to predict, or is prediction always a leap beyond the "
                             "evidence?")],
    application_lede="Each task asks for a rule and a justification. Show the differences or "
                     "ratios you used, and test your rule on a term you did not use to find "
                     "it.",
    projects_lede="Cycles and growth are sequences in disguise. Model one and say how far "
                  "your rule can be trusted.",
    sections=[
        dict(id="7.1", title="Describing and extending patterns",
             inquiry_q="How is a pattern described so that another person can continue it, and "
                       "what does extending it predict?",
             teach=[
                 "A pattern can be described in words, in pictures, in a table of values or as a rule, and each description is a different representation of the same pattern. A good description is one another person can continue without asking a question.",
                 "A term-to-term rule says how to get from one term to the next, and it is the easiest rule to see. A position-to-term rule connects the position of a term to its value, and it is the rule that predicts a distant term without listing the ones before it.",
                 "Extending a pattern is a prediction, and a prediction is only as safe as the rule behind it. Two different rules can fit the same first few terms, so a pattern is never fixed by its first terms alone.",
                 "A generalisation is a claim about every term, and it needs an argument, not just agreement with the terms already listed. A single term that disagrees is enough to refute it.",
             ], examples=[
                 dict(q="Describe the pattern 2, 5, 8, 11, … in two ways, and use each to find "
                        "the 20th term.",
                      vis=F("table", [["position", "1", "2", "3", "4", "5", "20"],
                                      ["term", "2", "5", "8", "11", "14", "59"]],
                            "the term rises by 3 each time, so term 20 is 2 + 19 × 3"),
                      reasoning="Read the term-to-term rule from the differences, then turn it "
                               "into a position-to-term rule.",
                      steps=["The differences are 3, 3, 3, so the term-to-term rule is add 3.",
                             "Term 1 is 2, term 2 is 2 + 3, term 3 is 2 + 2 × 3.",
                             "So term n is 2 + (n − 1) × 3, which is the position-to-term rule.",
                             "Term 20 is 2 + 19 × 3 = 59.",
                             "The two descriptions agree, and the second reaches term 20 "
                             "without listing the terms between."],
                      ans="add 3 each time; term n = 3n − 1; the 20th term is 59",
                      interp="A term-to-term rule is quick to see and a position-to-term rule "
                             "is quick to use, and the same pattern has both."),
                 dict(q="The first three terms of a pattern are 1, 2, 4. Give two different "
                        "rules that fit, and say what each predicts for the fourth term.",
                      vis=F("table", [["position", "1", "2", "3", "4 (rule 1)", "4 (rule 2)"],
                                      ["term", "1", "2", "4", "8", "7"]],
                            "two rules fit the same three terms and disagree at the fourth"),
                      reasoning="Look for a multiplicative rule and an additive rule.",
                      steps=["Multiplicative: each term is double the previous, so the next is "
                             "8.",
                             "Additive: the differences are 1 then 2, so the next difference "
                             "might be 3, giving 7.",
                             "Both rules fit 1, 2, 4 exactly.",
                             "They predict different fourth terms, so the three terms given do "
                             "not fix the pattern.",
                             "A fourth term of 8 would support the multiplicative rule and a "
                             "fourth term of 7 the additive one."],
                      ans="double each time gives 8; add the next integer gives 7",
                      interp="A pattern is never determined by its first few terms, so a "
                             "prediction is a conjecture until more terms confirm it."),
             ], inv=dict(
                 task="Take four patterns of your own: one you can describe by adding, one by "
                      "multiplying, one from a picture and one from a real situation. For each, "
                      "write the term-to-term rule, the position-to-term rule, and the next "
                      "two terms. Then check your position-to-term rule against the term-to-term "
                      "rule for a term you did not use to find it.",
                 table=[["pattern", "term-to-term", "position-to-term", "next two terms"],
                        ["4, 9, 14, 19, …", "add 5", "5n − 1", "24, 29"],
                        ["3, 6, 12, 24, …", "double", "3 × 2ⁿ⁻¹", "48, 96"],
                        ["1, 4, 9, 16, …", "add 3, 5, 7, …", "n²", "25, 36"],
                        ["squares of side 1, 2, 3, …", "add 2n + 1", "n²", "25, 36"]],
                 notice=["Every pattern had both a term-to-term and a position-to-term rule.",
                         "The multiplicative pattern grew far faster than the additive ones.",
                         "The picture pattern and the numeric pattern gave the same rule.",
                         "The check against an unused term held for every rule."],
                 obs="A pattern is described by a term-to-term rule and a position-to-term "
                     "rule, and the two descriptions of the same pattern must agree.",
                 concl="Describing a pattern well means giving a rule another person can "
                       "continue, and extending it is a prediction that the rule alone "
                       "justifies.")),
        dict(id="7.2", title="Linear sequences and the nth term",
             inquiry_q="What does a constant first difference tell you, and how is the nth "
                       "term found?",
             teach=[
                 "An arithmetic sequence has a constant difference between consecutive terms, called the common difference d. The nth term is a + (n − 1)d, where a is the first term.",
                 "The constant difference is the signature of a linear rule, and the graph of the terms against their position is a straight line.",
                 "The sum of the first n terms is n/2 × (first + last), which comes from pairing the first with the last, the second with the second-last, and so on.",
                 "A sequence given by a rule such as 3n + 2 starts at 5, not 2, because the first term corresponds to n = 1. Substituting n = 0 gives the value before the sequence begins.",
             ], examples=[
                 dict(q="Find the 20th term and the sum of the first 20 terms of 7, 11, 15, "
                        "19, …",
                      vis=F("staircase", 6, "each step adds 4"),
                      reasoning="Use the formula for the nth term and the pairing formula for "
                               "the sum.",
                      steps=["The first term is 7 and the common difference is 4.",
                             "The 20th term is 7 + 19 × 4 = 7 + 76 = 83.",
                             "The sum is 20/2 × (7 + 83) = 10 × 90 = 900.",
                             "The terms lie on the line whose rule is 4n + 3.",
                             "The sum formula works because the terms pair to a constant "
                             "total."],
                      ans="the 20th term is 83 and the sum is 900",
                      interp="One formula gives any term and another gives the total, and "
                             "neither requires listing the terms."),
                 dict(q="The 5th term of an arithmetic sequence is 14 and the 12th is 42. "
                        "Find the first term and the common difference.",
                      vis=F("table", [["term", "position", "value"],
                                      ["5th", "5", "14"],
                                      ["12th", "12", "42"]],
                            caption="Two terms fix the whole sequence."),
                      reasoning="The difference between the values equals the difference "
                               "between the positions times d.",
                      steps=["The value rises by 42 − 14 = 28 over 12 − 5 = 7 positions.",
                             "So 7d = 28 and d = 4.",
                             "The 5th term is a + 4d = a + 16 = 14, so a = −2.",
                             "The rule is therefore 4n − 6.",
                             "Check: the 12th term is 48 − 6 = 42."],
                      ans="first term −2, common difference 4",
                      interp="Two terms are enough to fix an arithmetic sequence, because a "
                             "linear rule has only two unknowns."),
             ], inv=dict(
                 task="Build three arithmetic sequences of your own: one with a positive "
                      "difference, one with a negative difference, and one with a fractional "
                      "difference. For each, find the rule, the 15th term and the sum of the "
                      "first 15 terms, and check the 15th term by listing.",
                 table=[["sequence", "rule", "15th term", "sum of 15"],
                        ["3, 7, 11, …", "4n − 1", "59", "465"],
                        ["20, 17, 14, …", "−3n + 23", "−22", "−15"],
                        ["1, 1.5, 2, …", "0.5n + 0.5", "8", "71.25"],
                        ["−5, −1, 3, …", "4n − 9", "51", "345"]],
                 notice=["Every sequence with a constant difference gave a linear rule.",
                         "The negative difference made the terms fall, and the 15th term "
                         "became negative.",
                         "The fractional difference still gave a whole-number sum here, by "
                         "chance.",
                         "Listing the terms confirmed every rule that was found algebraically."],
                 obs="A constant first difference is the signature of a linear rule, and the "
                     "rule can be recovered from any two terms of the sequence.",
                 concl="An arithmetic sequence is described by a + (n − 1)d, and the constant "
                       "difference is both the gradient of its graph and the test that "
                       "identifies it.")),
        dict(id="7.3", title="Quadratic sequences and differences",
             inquiry_q="Why does a constant second difference signal a quadratic rule?",
             teach=[
                 "The first differences of a quadratic sequence form an arithmetic sequence, so the second differences are constant.",
                 "A constant second difference means the rule is a quadratic of the form an² + bn + c, and the second difference is 2a.",
                 "Finding the rule means solving three equations from the first three terms, or using the standard form with the differences read directly.",
                 "Quadratic sequences arise from counting in two dimensions, such as the number of dots in a growing pattern or the number of diagonals of a polygon.",
             ], examples=[
                 dict(q="The numbers of matches needed for 1, 2, 3 and 4 squares in a row are "
                        "4, 7, 10, 13. A different pattern gives 1, 4, 9, 16. Find the rule "
                        "for the second and test it on the 6th figure.",
                      vis=F("tiles", 4, 4, [(0, 0), (1, 1), (2, 2), (3, 3)],
                            "figure 4 has 16 dots",
                            note="each figure is a square"),
                      reasoning="Take differences to identify the kind of rule, then fit the "
                               "quadratic.",
                      steps=["The sequence is 1, 4, 9, 16, so the first differences are 3, 5, "
                             "7.",
                             "The second differences are 2, 2, which are constant.",
                             "So the rule is quadratic with 2a = 2, hence a = 1.",
                             "Fitting gives n², and the 6th figure has 36 dots.",
                             "The first pattern had constant first differences, so it was "
                             "linear with rule 3n + 1."],
                      ans="the rule is n²; the 6th figure has 36 dots",
                      interp="The differences identify the kind of rule before any fitting is "
                             "attempted, which is the whole value of the difference table."),
                 dict(q="Find the rule for the sequence 3, 8, 15, 24, 35 and use it to find "
                        "the 12th term.",
                      vis=F("staircase", 5, "first differences 5, 7, 9, 11"),
                      reasoning="Take differences to find the coefficient of n², then solve "
                               "for the rest.",
                      steps=["The first differences are 5, 7, 9, 11, so the second difference "
                             "is 2.",
                             "Hence the rule is n² + bn + c.",
                             "Using the first term: 1 + b + c = 3, so b + c = 2.",
                             "Using the second: 4 + 2b + c = 8, so 2b + c = 4.",
                             "Subtracting gives b = 2 and c = 0, so the rule is n² + 2n.",
                             "The 12th term is 144 + 24 = 168."],
                      ans="the rule is n² + 2n, and the 12th term is 168",
                      interp="Three terms are enough to fix a quadratic, exactly as two fix a "
                             "line, and the difference table says how many are needed."),
             ], inv=dict(
                 task="Take four sequences: two with constant first differences, one with "
                      "constant second differences, and one that is neither. For each, build a "
                      "difference table, identify the kind of rule, fit it, and test it on a "
                      "term you did not use.",
                 table=[["sequence", "first diff", "second diff", "rule"],
                        ["5, 8, 11, 14", "3, 3, 3", "0", "3n + 2"],
                        ["1, 4, 9, 16", "3, 5, 7", "2, 2", "n²"],
                        ["2, 6, 12, 20", "4, 6, 8", "2, 2", "n² + n"],
                        ["1, 2, 4, 8", "1, 2, 4", "1, 2", "2ⁿ⁻¹"]],
                 notice=["Constant first differences always gave a linear rule.",
                         "Constant second differences always gave a quadratic.",
                         "The doubling sequence had growing differences and was exponential.",
                         "Each rule was tested on a term not used to find it, and every test "
                         "passed."],
                 obs="The difference table identifies the kind of rule, and the number of "
                     "terms needed to fix it equals one more than the degree of the rule.",
                 concl="A sequence with constant kth differences is generated by a polynomial of "
                       "degree k, and the difference table is the tool that identifies which "
                       "polynomial to fit.")),
        dict(id="7.4", title="Recursive rules and spreadsheets",
             inquiry_q="What does a constant ratio tell you, and why does growth outrun "
                       "addition?",
             teach=[
                 "A recursive rule gives each term from the one before it: term n = term n−1 + d for an arithmetic pattern, or term n = r × term n−1 for a geometric one. It is the rule a spreadsheet uses, because a cell can refer to the cell above it.",
                 "A spreadsheet makes recursion visible: type the first term, then fill the formula down, and the whole sequence appears. Changing the first term or the step changes every term at once, which is why a spreadsheet is a model and not just a list.",
                 "A position-to-term rule gives any term directly, and a recursive rule gives only the next one. To reach term 100 a recursive rule needs 99 steps, and a position-to-term rule needs one substitution.",
                 "A geometric sequence is the multiplicative recursive rule, and its nth term is arⁿ⁻¹. Growth by a constant ratio eventually overtakes growth by a constant amount, because the increase itself grows.",
                 "A ratio between −1 and 1 makes the terms shrink towards zero, and the sum of infinitely many such terms is a finite number. This is the first infinite process in the course, and it is what makes a bouncing ball eventually stop.",
                          ], examples=[
                 dict(q="A pattern of squares grows so that figure 1 has 1 square, figure 2 "
                        "has 3, figure 3 has 9 and figure 4 has 27. Find the number of squares "
                        "in figure 10 and the total for the first 10 figures.",
                      vis=F("tiles", 5, 3, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
                                             (1, 1), (2, 1), (3, 1), (4, 1)],
                            "figures 1 to 4 of the pattern",
                            note="each figure has three times the previous"),
                      reasoning="The constant ratio is 3, so the rule is geometric.",
                      steps=["The ratio between consecutive figures is 3.",
                             "So the rule is 3ⁿ⁻¹, and figure 10 has 3⁹ = 19683 squares.",
                             "The total is (3¹⁰ − 1)/(3 − 1) = (59049 − 1)/2 = 29524.",
                             "The 10th figure alone has twice as many squares as all the "
                             "others together.",
                             "That is the defining property of exponential growth."],
                      ans="figure 10 has 19683 squares; the total is 29524",
                      interp="The last term dominates the sum, which never happens in an "
                             "arithmetic sequence."),
                 dict(q="A ball is dropped from 2 m and rebounds to 80% of its previous "
                        "height. Find the total distance it travels before coming to rest.",
                      vis=F("table", [["bounce", "height", "distance"],
                                      ["drop", "2", "2"],
                                      ["1", "1.6", "3.2"],
                                      ["2", "1.28", "2.56"],
                                      ["3", "1.024", "2.048"]],
                            caption="Each bounce adds two journeys of 80% of the previous "
                                    "height."),
                      reasoning="The rebound heights form a geometric sequence, and each bounce "
                               "contributes twice the height.",
                      steps=["The rebound heights are 2 × 0.8, 2 × 0.8², 2 × 0.8³, …",
                             "Each bounce adds the upward and the downward journey, so the "
                             "total is 2 + 2(2 × 0.8 + 2 × 0.8² + …).",
                             "The sum inside is 1.6/(1 − 0.8) = 8.",
                             "So the total distance is 2 + 2 × 8 = 18 m.",
                             "The number of bounces is infinite but the total distance is "
                             "finite."],
                      ans="18 m",
                      interp="An infinite number of bounces covers a finite distance, which is "
                             "the first hint that infinite processes can have finite answers."),
             ], inv=dict(
                 task="Take three geometric sequences: one growing, one decaying and one with "
                      "a negative ratio. For each, find the rule, the 8th term and the sum of "
                      "the first 8 terms. Then find the limiting sum for the decaying one and "
                      "check it by adding many terms.",
                 table=[["sequence", "rule", "8th term", "sum of 8"],
                        ["2, 6, 18, …", "2 × 3ⁿ⁻¹", "4374", "6560"],
                        ["64, 32, 16, …", "64 × 0.5ⁿ⁻¹", "0.5", "127.5"],
                        ["1, −2, 4, …", "(−2)ⁿ⁻¹", "−128", "85"],
                        ["100, 90, 81, …", "100 × 0.9ⁿ⁻¹", "47.83", "471.6"]],
                 notice=["The growing sequence's last term was almost as large as the whole "
                         "sum.",
                         "The decaying sequence's sum approached 128, its limit.",
                         "The negative ratio made the terms alternate in sign.",
                         "Adding many terms of the decaying sequence confirmed the limiting "
                         "sum."],
                 obs="A constant ratio gives an exponential rule, and the behaviour of the sum "
                     "depends on whether the ratio is greater or less than one in size.",
                 concl="A geometric sequence is described by arⁿ⁻¹, and when |r| < 1 its terms "
                       "shrink towards zero while its total approaches the finite limit "
                       "a/(1 − r).")),
        dict(id="7.5", title="Modelling with sequences",
             inquiry_q="How is a sequence used to predict, and how far can the prediction be "
                       "trusted?",
             teach=[
                 "A sequence models a situation when its rule matches the way the situation changes, and the model is used to predict terms beyond those observed.",
                 "Prediction inside the range of the data is interpolation and is usually safe; prediction beyond it is extrapolation and depends on the rule continuing to hold.",
                 "Recursive and explicit rules describe the same sequence. A recursive rule gives each term from the one before, and an explicit rule gives any term from its position.",
                 "A model's failure is informative. When a prediction is wrong, the rule or the assumption behind it is wrong, and finding which is the next task.",
             ], examples=[
                 dict(q="A population of rabbits grows from 40 by a factor of 1.3 each month. "
                        "Model it, predict the population after 12 months, and comment on the "
                        "model.",
                      vis=F("table", [["month", "population"],
                                      ["0", "40"],
                                      ["3", "88"],
                                      ["6", "193"],
                                      ["12", "928"]],
                            caption="the population more than doubles every six months"),
                      reasoning="Repeated multiplication by a constant factor is a geometric "
                               "model.",
                      steps=["The model is P = 40 × 1.3ⁿ.",
                             "After 12 months, P = 40 × 1.3¹² ≈ 928.",
                             "That is more than twenty times the starting population.",
                             "The model assumes no limit on food or space, which is false.",
                             "So the prediction is reliable for a few months and unreliable "
                             "beyond a year."],
                      ans="P = 40 × 1.3ⁿ; about 928 after 12 months; unreliable in the long "
                          "term",
                      interp="An exponential model is a local description, and extrapolating "
                             "it far enough always produces an impossible answer."),
                 dict(q="A phone contract costs 20 dollars a month plus 5 dollars for each "
                        "gigabyte. Model the monthly cost, and find the cost in month 12 and "
                        "the total over 12 months if usage rises by 1 gigabyte each month.",
                      vis=F("table", [["month", "usage", "cost"],
                                      ["1", "1", "25"],
                                      ["2", "2", "30"],
                                      ["3", "3", "35"],
                                      ["12", "12", "80"]],
                            caption="the cost is an arithmetic sequence"),
                      reasoning="The cost is a linear function of the usage, and the usage is "
                               "an arithmetic sequence.",
                      steps=["The cost in month n is 20 + 5n dollars.",
                             "In month 12 the cost is 20 + 60 = 80 dollars.",
                             "The costs form an arithmetic sequence 25, 30, 35, … with "
                             "difference 5.",
                             "The total over 12 months is 12/2 × (25 + 80) = 6 × 105 = 630 "
                             "dollars.",
                             "The model assumes the usage really does rise by exactly 1 "
                             "gigabyte each month."],
                      ans="80 dollars in month 12; 630 dollars over 12 months",
                      interp="Two models combine: an arithmetic sequence of usage and a linear "
                             "cost, and the total uses the arithmetic sum formula."),
             ], inv=dict(
                 task="Choose a quantity that changes over time: a population, a saving, a "
                      "skill level or a phone bill. Model it with a sequence, predict three "
                      "terms ahead, and then check one prediction against reality if you can.",
                 table=[["quantity", "model", "prediction", "reality"],
                        ["savings", "arithmetic, +50 a month", "600 after 10 months",
                         "matched"],
                        ["reading speed", "arithmetic, +2 words a minute", "120 after 10 "
                         "weeks", "slower"],
                        ["plant height", "geometric, ×1.1 a week", "2.6 times after 10 weeks",
                         "slower"]],
                 notice=["The arithmetic savings model matched reality because the rule was "
                         "exact.",
                         "The reading model overestimated, because improvement slows.",
                         "The plant model overestimated, because growth is not a constant "
                         "multiplier.",
                         "Every failure pointed to the assumption, not the arithmetic."],
                 obs="A sequence model predicts well when its rule matches the mechanism of "
                     "change, and badly when the mechanism changes.",
                 concl="A sequence is a model whose predictions are trustworthy only while the "
                       "rule that generates it continues to describe the situation.")),
        dict(id="7.6", title="Investigation: figures that grow",
             inquiry_q="How is a repeating pattern predicted, and what does a cycle hide?",
             teach=[
                 "A periodic sequence repeats after a fixed number of terms, and the position within the cycle is found from the remainder when the position is divided by the period.",
                 "Predicting a periodic pattern is therefore a division with a remainder, and the remainder identifies the point in the cycle.",
                 "A cycle hides the long-term behaviour, because a short sample of a cycle looks like a rule that will continue, and it does.",
                 "Some sequences are eventually periodic, and some are not, and telling them apart requires more terms than a short observation provides.",
             ], examples=[
                 dict(q="The last digits of the powers of 2 cycle 2, 4, 8, 6. Find the last "
                        "digit of 2¹⁰⁰.",
                      vis=F("staircase", 4, "the cycle 2, 4, 8, 6 repeats"),
                      reasoning="Divide the exponent by the period and use the remainder to "
                               "identify the point in the cycle.",
                      steps=["The cycle has period 4.",
                             "Dividing 100 by 4 gives a remainder of 0.",
                             "A remainder of 0 means the last position in the cycle, which is "
                             "6.",
                             "So the last digit of 2¹⁰⁰ is 6.",
                             "Check: the last digit of 2⁴ is 6 and of 2⁸ is 6, confirming the "
                             "pattern."],
                      ans="6",
                      interp="A remainder of zero points to the end of the cycle rather than "
                             "the beginning, which is the one detail that catches people out."),
                 dict(q="A traffic light cycles green, amber, red, red, green. If it is green "
                        "at time 0, what colour is it at time 47?",
                      vis=F("table", [["time", "colour"],
                                      ["0", "green"],
                                      ["1", "amber"],
                                      ["2", "red"],
                                      ["3", "red"],
                                      ["4", "green"],
                                      ["5", "amber"]],
                            caption="the cycle has period 4"),
                      reasoning="Divide the time by the period and read the position in the "
                               "cycle.",
                      steps=["The cycle is green, amber, red, red, so the period is 4.",
                             "Dividing 47 by 4 gives 11 remainder 3.",
                             "A remainder of 3 is the fourth position, which is red.",
                             "So the light is red at time 47.",
                             "A remainder of 0 would mean green, the first position."],
                      ans="red",
                      interp="The remainder identifies the position in the cycle, and the "
                             "convention for a zero remainder must be stated."),
             ], inv=dict(
                 task="Find three periodic patterns: a traffic light, a weekly timetable, and "
                      "one of your own. For each, state the period, predict the state at a "
                      "large position, and check by counting if the period is short.",
                 table=[["pattern", "period", "prediction", "check"],
                        ["traffic light", "4", "time 47 is red", "confirmed"],
                        ["weekly timetable", "7", "day 100 is the second day", "confirmed"],
                        ["last digit of 7ⁿ", "4", "7⁵⁰ ends in 9", "confirmed"]],
                 notice=["Every prediction came from a division with a remainder.",
                         "The remainder identified the position in the cycle exactly.",
                         "A short cycle made counting a practical check.",
                         "The convention for a zero remainder had to be decided each time."],
                 obs="A periodic pattern is predicted by dividing the position by the period "
                     "and reading the remainder, and the remainder convention must be stated.",
                 concl="A repeating pattern is predicted from the remainder of a division, and "
                       "the cycle is a representation that hides the long-term behaviour by "
                       "making a short sample look complete.")),
    ],
    practice=dict(
        A=[("7.1.1", "Find the 10th term of 3, 7, 11, 15, …", "39",
            "Use a + (n − 1)d with a = 3, d = 4.", "F"),
           ("7.1.2", "Find the 8th term of 20, 17, 14, …", "−1",
            "Use a + (n − 1)d with a = 20, d = −3.", "F"),
           ("7.1.3", "Find the rule for 5, 9, 13, 17, …", "4n + 1",
            "The common difference is 4 and the first term is 5.", "F"),
           ("7.1.4", "Find the sum of the first 12 terms of 2, 5, 8, …", "222",
            "Use n/2 × (first + last).", "F"),
           ("7.1.5", "Find the 6th term of 3, 6, 12, 24, …", "96",
            "The common ratio is 2.", "F"),
           ("7.1.6", "Find the rule for 81, 27, 9, 3, …", "3⁵⁻ⁿ",
            "The common ratio is 1/3.", "F"),
           ("7.1.7", "Find the next two terms of 1, 4, 9, 16, …", "25, 36",
            "These are the square numbers.", "F"),
           ("7.1.8", "Find the next term of 2, 6, 12, 20, …", "30",
            "The first differences are 4, 6, 8, so the next is 10.", "F"),
           ("7.1.9", "Find the sum of the first 6 terms of 1, 2, 4, 8, …", "63",
            "Use a(rⁿ − 1)/(r − 1) with a = 1, r = 2.", "F"),
           ("7.1.10", "Find the 5th term of 50, 45, 40.5, …", "36.45",
            "The common ratio is 0.9.", "F"),
           ("7.1.11", "Find the rule for 7, 12, 17, 22, …", "5n + 2",
            "The common difference is 5.", "F"),
           ("7.1.12", "Find the next two terms of 1, −3, 9, −27, …", "81, −243",
            "The common ratio is −3.", "F")],
        B=[("7.2.1", "The number of dots in figure n is n² + n. Find the first four terms and "
            "test the rule on figure 8.",
            "2, 6, 12, 20; and 72 for figure 8.", "Substitute n = 1 to 4 and 8.", "R"),
           ("7.2.2", "Investigate the pattern in the sums 1, 1 + 2, 1 + 2 + 3 and justify the "
            "general rule.",
            "The sums are 1, 3, 6, 10, following n(n + 1)/2.",
            "Pair the first and last terms.", "R"),
           ("7.2.3", "Conjecture a rule for the number of diagonals of an n-sided polygon and "
            "test it for n = 5, 6, 7.",
            "n(n − 3)/2, giving 5, 9, 14.", "Count from each vertex and divide by 2.", "R"),
           ("7.2.4", "Investigate the pattern in the number of cubes needed to build a "
            "staircase of n steps.",
            "n(n + 1)/2, the triangular numbers.", "Count the cubes layer by layer.", "R"),
           ("7.2.5", "Build a difference table for 2, 5, 10, 17, 26 and identify the rule.",
            "Second differences are 2, so the rule is n² + 1.",
            "Take differences and fit.", "R"),
           ("7.2.6", "Conjecture a rule for the number of matches in a row of n hexagons and "
            "justify it.",
            "5n + 1, because each new hexagon shares one side.", "Count for n = 1, 2, 3.", "R"),
           ("7.2.7", "Investigate the pattern in the sums 1/2, 1/2 + 1/4, 1/2 + 1/4 + 1/8 and "
            "justify the rule.",
            "The sums approach 1, because the total is 1 − 1/2ⁿ.",
            "Write with a common denominator.", "R"),
           ("7.2.8", "The heights of a bouncing ball are 2, 1.6, 1.28 m. Investigate the "
            "total distance before it comes to rest.",
            "18 m, from the geometric series.", "Sum the two journeys per bounce.", "C"),
           ("7.2.9", "Find the pattern in the last digits of 3ⁿ for n = 1 to 8 and use it to "
            "predict 3⁵⁰.",
            "The cycle is 3, 9, 7, 1, so 3⁵⁰ ends in 9.", "Divide by the period.", "R"),
           ("7.2.10", "Investigate the pattern in the number of squares of all sizes in an "
            "n by n grid.",
            "n(n + 1)(2n + 1)/6, the sum of the squares.",
            "Count squares of each size.", "C"),
           ("7.2.11", "Conjecture a rule for the number of triangles formed by n lines in "
            "general position.",
            "n(n − 1)(n − 2)/6, because each triple of lines makes one triangle.",
            "Count for n = 3, 4, 5.", "C")],
        C=[("7.3.1", "Explain in your own words what an arithmetic sequence is.",
            "A sequence in which the difference between consecutive terms is constant.",
            "State the definition and give an example.", "R"),
           ("7.3.2", "Write a complete solution to: find the rule for 4, 11, 18, 25 and the "
            "30th term.",
            "7n − 3, and the 30th term is 207.", "Use the common difference.", "F"),
           ("7.3.3", "Choose between a recursive and an explicit rule for finding the 100th "
            "term and justify.",
            "An explicit rule, because a recursive rule needs all the previous terms.",
            "Say what each rule requires.", "R"),
           ("7.3.4", "Set out a full solution to: find the sum of the first 10 terms of "
            "5, 10, 20, 40, …",
            "5115, using a(rⁿ − 1)/(r − 1).", "Identify a and r first.", "F"),
           ("7.3.5", "Explain why a constant second difference signals a quadratic rule.",
            "Because the first differences of a quadratic form an arithmetic sequence, so "
            "their differences are constant.", "Take differences of n², n² + n and so on.",
            "R"),
           ("7.3.6", "Describe, with an example, the difference between an arithmetic and a "
            "geometric sequence.", "An arithmetic sequence adds a constant, as 2, 5, 8; a "
            "geometric sequence multiplies by one, as 2, 6, 18.",
            "Compare the differences and the ratios.", "R"),
           ("7.3.7", "Explain why the sum of infinitely many terms can be finite.",
            "Because the terms shrink fast enough that the running total approaches a limit, "
            "as with 1 + 1/2 + 1/4 + … = 2.", "Use a geometric series with |r| < 1.", "R"),
           ("7.3.8", "Write the reasoning that shows the sum of the first n odd numbers is "
            "n².",
            "The odd numbers are the differences of consecutive squares, so they telescope "
            "to n².", "Relate to (n + 1)² − n².", "R"),
           ("7.3.9", "Set out the argument that the number of diagonals of an n-sided polygon "
            "is n(n − 3)/2.",
            "Each vertex joins to n − 3 others, giving n(n − 3) endpoints, and each diagonal "
            "has two endpoints.", "Count and divide by 2.", "R"),
           ("7.3.10", "Explain what the common ratio of a geometric sequence represents in a "
            "real situation.", "The multiplier applied at each step — the growth factor, the "
            "rebound fraction, or the decay rate.", "Give a real example.", "R"),
           ("7.3.11", "Describe the relationship between a difference table and the degree of "
            "a rule.", "Constant first differences give a linear rule, constant second "
            "differences a quadratic, and so on.", "Compare the tables.", "R"),
           ("7.3.12", "Explain, with an example, when a pattern that fits every observed term "
            "is still wrong.",
            "Any answer is acceptable if it identifies a rule that fails later, as with "
            "n² + n + 41 being prime, or a cycle that looks like a trend.",
            "Give a specific counterexample.", "R")],
        D=[("7.4.1", "A population of 500 grows by 8% a year. Model it, find the population "
            "after 10 years, and find when it reaches 1000.",
            "P = 500 × 1.08ⁿ; about 1079 after 10 years; doubles in about 9 years.",
            "Use a geometric model and solve.", "A"),
           ("7.4.2", "A car loses 12% of its value a year from 15000 dollars. Model it, find "
            "the value after 5 years, and find when it falls below 5000 dollars.",
            "V = 15000 × 0.88ⁿ; about 7913 after 5 years; below 5000 after about 9 years.",
            "Use a geometric model and solve.", "A"),
           ("7.4.3", "A contractor charges 200 dollars plus 40 dollars per hour for the first "
            "5 hours and 60 dollars per hour after. Model the cost and find it for an 8-hour "
            "job.",
            "200 + 200 + 180 = 580 dollars for 8 hours.",
            "Split the job at the 5-hour point.", "A"),
           ("7.4.4", "A student saves 20 dollars in month 1 and 5 dollars more each month. "
            "Model the saving, find the saving in month 12, and find the total over 12 "
            "months.",
            "75 dollars in month 12; 570 dollars in total.",
            "Use an arithmetic model.", "A"),
           ("7.4.5", "A ball is dropped from 10 m and rebounds to 60% of its previous height. "
            "Find the total distance travelled before it comes to rest.",
            "38 m, from 10 + 2 × 10 × 0.6/(1 − 0.6).",
            "Sum the geometric series.", "A"),
           ("7.4.6", "A phone plan costs 15 dollars a month, rising by 2 dollars a month each "
            "month. Model the cost, find it in month 12, and find the total over 12 months.",
            "37 dollars in month 12; 312 dollars in total.",
            "Use an arithmetic model.", "A"),
           ("7.4.7", "A bank pays 4% compound interest on 5000 dollars. Investigate how long "
            "it takes to double and justify.",
            "About 17.7 years, because 1.04ⁿ = 2 gives n = ln2/ln1.04 ≈ 17.7.",
            "Solve the exponential equation.", "R"),
           ("7.4.8", "A colony of bacteria doubles every 3 hours from 200. Model it, find the "
            "population after a day, and comment on the model.",
            "P = 200 × 2^(t/3); about 25600 after 24 hours; the model cannot continue "
            "indefinitely.", "Use an exponential model.", "A"),
           ("7.4.9", "A staircase of n steps uses n(n + 1)/2 blocks. Investigate the number "
            "of steps possible with 1000 blocks and justify.",
            "44 steps, because 44 × 45/2 = 990 and 45 × 46/2 = 1035.",
            "Solve the quadratic and round down.", "R"),
           ("7.4.10", "A savings account pays 50 dollars a month plus 0.5% interest monthly. "
            "Investigate the balance after 12 months and justify the method.",
            "About 616 dollars, because the interest is small but compounds on a growing "
            "balance.", "Model month by month.", "C"),
           ("7.4.11", "A tree grows 0.4 m a year for the first 5 years and 0.2 m a year "
            "after. Model the height and find it after 10 years from 1.2 m.",
            "1.2 + 2 + 1 = 4.2 m after 10 years.",
            "Split the model at year 5.", "A"),
           ("7.4.12", "Explain, with a model of your own, when a sequence model is a poor "
            "description of a situation.",
            "Any answer is acceptable if it identifies a mechanism that changes, such as a "
            "population reaching a limit or a learner plateauing.", "Give a specific "
            "counterexample.", "R")],
    ),
    assessment=[
        dict(title="A1 · The growing savings club",
             text="A savings club starts with 5 members and the number of members doubles "
                  "every month. Each member contributes 10 dollars a month. Model the total "
                  "contribution in month n, find the contribution in month 12, and find the "
                  "total contributed over the first 12 months. Then comment on how long the "
                  "model can continue.",
             note="Criteria A and D · build the geometric model, use the series formula, and "
                  "justify the limits of the model."),
        dict(title="A2 · The bouncing ball",
             text="A ball is dropped from 8 m and rebounds to 70% of its previous height each "
                  "time. Find the height of the third rebound, the total distance travelled "
                  "before it comes to rest, and the number of bounces after which the rebound "
                  "is less than 10 cm. Justify the use of an infinite series.",
             note="Criteria B and C · use a geometric model, justify the limiting sum, and "
                  "solve the inequality."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of pattern, "
        "generalisation and representation appear in your work?",
        "How is the global context of orientation in space and time, and its exploration of "
        "cycles, growth and prediction, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a sequence model for prediction, and what would you still "
        "like to ask?",
    ],
    review=dict(
        ideas=["An arithmetic sequence has a constant difference and a linear rule.",
               "A geometric sequence has a constant ratio and an exponential rule.",
               "Constant second differences signal a quadratic rule.",
               "The sum of an arithmetic sequence is n/2 × (first + last).",
               "The sum of a geometric sequence is a(rⁿ − 1)/(r − 1).",
               "When |r| < 1 the terms shrink and the total approaches a/(1 − r).",
               "A periodic pattern is predicted from the remainder of a division.",
               "A general rule needs an argument, not a list of checked cases."],
        vocab=["arithmetic sequence", "geometric sequence", "common difference",
               "common ratio", "nth term", "difference table", "periodic", "recursive rule",
               "explicit rule", "generalisation", "counterexample", "limiting sum"],
        mixed=[("7.R1", "Find the 15th term of 4, 9, 14, …"),
               ("7.R2", "Find the rule for 2, 6, 18, 54, …"),
               ("7.R3", "Find the next term of 1, 8, 27, 64, …"),
               ("7.R4", "Find the sum of the first 8 terms of 3, 6, 12, …"),
               ("7.R5", "Find the rule for 0, 3, 8, 15, …"),
               ("7.R6", "Explain why the sum 1 + 1/2 + 1/4 + … is finite.")],
    ),
    projects=dict(
        service=[("Community need", "Growth, cycles and savings are predicted without stating "
                                    "the model."),
                 ("Mathematical connection", "Arithmetic and geometric sequences and series."),
                 ("Proposed action", "Model one community growth or savings plan and publish "
                                     "the model with its limits."),
                 ("Expected impact", "A reader can see how long a plan can last."),
                 ("Student reflection", "Record the model, the prediction and the check.")],
        community=[("Project idea", "A growth audit of a school club or team."),
                   ("Need", "Membership and budgets are projected by guesswork."),
                   ("Research question", "Which sequence models the growth, and how far can "
                                         "it be trusted?"),
                   ("Mathematics", "Sequences, series and exponential models."),
                   ("Action or outcome", "A one-page projection with the model and its "
                                         "limits."),
                   ("Beneficiaries", "Everyone who plans for the club."),
                   ("Evidence", "The projection with the model and a test.")],
        personal=[("Personal interest", "A game, a sport or a savings goal."),
                  ("Learning goal", "To model something that grows or cycles and predict it."),
                  ("Product or outcome", "A sequence model with a prediction and a check."),
                  ("Mathematics", "Arithmetic and geometric sequences."),
                  ("Process", "Identify the mechanism, build the model, and test a "
                              "prediction."),
                  ("Evidence", "The model, the prediction and the test.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=8, title="Growth and Financial Mathematics",
    key="Relationships", related=["Change", "Quantity", "Model"],
    context="Fairness and development",
    exploration="Access, saving and long-term planning",
    inquiry=("Repeated percentage change is modelled by multiplication rather than addition, "
             "so the quantity after n periods is the initial quantity times a multiplier to "
             "the power n; recognising this changes how a percentage rise and a percentage "
             "fall are understood, and the model makes the long-term effect of a rate "
             "visible."),
    atl=("Self-management",
         "Students organise a multi-step financial calculation, check each step against the "
         "model, and manage the time needed to complete a comparison of several options."),
    standfirst="A percentage rise followed by the same percentage fall does not return to the "
               "start, because the two percentages are taken on different quantities.",
    engage="A shop raises a price by 15% and then reduces it by 15%. Is the final price the "
           "same as the original, higher, or lower?",
    questions=[("Factual", "What is the difference between simple and compound interest, and "
                           "how is a repeated percentage change modelled?"),
               ("Conceptual", "Why does a percentage rise followed by an equal percentage fall "
                              "not restore the original quantity, and what does a multiplier "
                              "reveal that a percentage does not?"),
               ("Debatable", "Is a loan that is affordable in the short term a fair one, and "
                             "who is best placed to judge the long-term cost of borrowing?")],
    application_lede="Each task involves a rate and a time. State the multiplier before you "
                     "calculate, and say whether the change is simple or compound.",
    projects_lede="Access to money is a mathematical question with a social answer. Model one "
                  "real financial decision and say who it favours.",
    sections=[
        dict(id="8.1", title="Repeated percentage change",
             inquiry_q="Why is a percentage change modelled by multiplication rather than "
                       "addition?",
             teach=[
                 "A percentage is a fraction with denominator 100, and a percentage change is a change relative to the quantity it is applied to. Because the reference quantity changes, the same percentage is not the same amount.",
                 "A multiplier is 1 plus the rate as a decimal. A 15% rise is a multiplier of 1.15 and a 15% fall is a multiplier of 0.85, and their product is 0.9775, which is a fall.",
                 "A rise of r followed by a fall of r gives a multiplier of (1 + r)(1 − r) = 1 − r², which is always less than 1 for any non-zero r. This is why the two never cancel.",
                 "Working with multipliers makes repeated changes a single power, and it also makes the order of the changes irrelevant, because multiplication is commutative.",
             ], examples=[
                 dict(q="A price of 80 dollars is increased by 15% and then decreased by 15%. "
                        "Find the final price and the overall percentage change.",
                      vis=F("table", [["step", "multiplier", "price"],
                                      ["start", "—", "80"],
                                      ["rise 15%", "1.15", "92"],
                                      ["fall 15%", "0.85", "78.20"],
                                      ["combined", "0.9775", "78.20"]],
                            caption="the combined multiplier is less than 1"),
                      reasoning="Apply each multiplier in turn, then compare the final price "
                               "with the original.",
                      steps=["After the rise the price is 80 × 1.15 = 92 dollars.",
                             "After the fall it is 92 × 0.85 = 78.20 dollars.",
                             "The combined multiplier is 1.15 × 0.85 = 0.9775.",
                             "The overall change is a fall of 2.25%.",
                             "The final price is lower than the start, even though the two "
                             "percentages were equal."],
                      ans="78.20 dollars, a fall of 2.25%",
                      interp="The two percentages were equal but were taken on different "
                             "quantities, so they did not cancel, and the fall is r² = 2.25%."),
                 dict(q="A salary rises by 5% and then by 8%. Find the single multiplier and "
                        "the overall percentage rise, and compare it with a single rise of "
                        "13%.",
                      vis=F("double_number_line", "multiplier", "percentage change",
                            "multipliers multiply, percentages do not add"),
                      reasoning="Multiply the two multipliers and compare with the sum of the "
                               "percentages.",
                      steps=["The multipliers are 1.05 and 1.08.",
                             "Their product is 1.134, so the overall rise is 13.4%.",
                             "A single rise of 13% would give a multiplier of 1.13.",
                             "The difference is 0.4 percentage points, which is 1.05 × 1.08 − "
                             "1.13.",
                             "The extra comes from the cross term 0.05 × 0.08 = 0.004."],
                      ans="multiplier 1.134, a rise of 13.4%, which is 0.4 points more than "
                          "13%",
                      interp="Percentage rises add only approximately, and the error grows "
                             "with the product of the rates, which is why multipliers are "
                             "safer."),
             ], inv=dict(
                 task="Take five pairs of percentage changes: two rises, two falls, and one of "
                      "each. For each, compute the combined multiplier in both orders, check "
                      "that the order does not matter, and find the single percentage change "
                      "that gives the same result.",
                 table=[["changes", "combined multiplier", "single change"],
                        ["+10%, +10%", "1.21", "+21%"],
                        ["−10%, −10%", "0.81", "−19%"],
                        ["+20%, −20%", "0.96", "−4%"],
                        ["+50%, −50%", "0.75", "−25%"],
                        ["+5%, −3%", "1.0235", "+2.35%"]],
                 notice=["The combined multiplier was the same in both orders every time.",
                         "A rise and a fall of the same size always gave a multiplier below "
                         "one.",
                         "The single percentage change was always the multiplier minus one.",
                         "The loss from a rise and a fall was the square of the rate."],
                 obs="Percentage changes combine by multiplying their multipliers, and the "
                     "combined multiplier is independent of the order of the changes.",
                 concl="A percentage change is modelled by a multiplier, and repeated changes "
                       "combine by multiplication, which is why equal rises and falls do not "
                       "cancel.")),
        dict(id="8.2", title="Compound interest and multipliers",
             inquiry_q="What is the difference between interest on the principal and interest "
                       "on the interest?",
             teach=[
                 "Simple interest pays a fixed percentage of the original principal each period, so the amount grows by the same amount every period and the model is linear.",
                 "Compound interest pays a percentage of the current amount, so the interest itself earns interest and the model is exponential.",
                 "The compound formula is A = P(1 + r)ⁿ, where P is the principal, r the rate per period and n the number of periods. The simple formula is A = P(1 + rn).",
                 "The two agree after one period and then diverge, and the gap grows with the rate and the number of periods, which is why the length of a loan matters so much.",
             ], examples=[
                 dict(q="Compare 2000 dollars at 6% simple interest and 6% compound interest "
                        "for 5 years.",
                      vis=F("table", [["year", "simple", "compound"],
                                      ["0", "2000", "2000"],
                                      ["1", "2120", "2120"],
                                      ["3", "2360", "2382.03"],
                                      ["5", "2600", "2676.45"]],
                            caption="the two agree at year 1 and then separate"),
                      reasoning="Apply each formula and compare the amounts.",
                      steps=["Simple: A = 2000(1 + 0.06 × 5) = 2000 × 1.30 = 2600 dollars.",
                             "Compound: A = 2000 × 1.06⁵ = 2000 × 1.3382 = 2676.45 dollars.",
                             "The difference is 76.45 dollars, which is the interest on the "
                             "interest.",
                             "After one year both give 2120 dollars, so the models agree "
                             "there.",
                             "The gap grows each year, because the compound interest is "
                             "charged on a larger amount."],
                      ans="simple 2600 dollars, compound 2676.45 dollars, a difference of "
                          "76.45 dollars",
                      interp="The difference is entirely the interest earned on interest, and "
                             "it grows with time, which is why a long loan is expensive."),
                 dict(q="A loan of 5000 dollars is repaid at 4% compound interest after 3 "
                        "years. Find the amount repaid and the interest paid.",
                      vis=F("grid", [(0, 5000), (3, 5624.32)], ["start", "repaid"], 0, 4, 4000,
                            6200, [(0, 5000), (3, 5624.32)],
                            "the debt grows exponentially"),
                      reasoning="Apply the compound formula and subtract the principal.",
                      steps=["A = 5000 × 1.04³.",
                             "1.04³ = 1.124864, so A = 5624.32 dollars.",
                             "The interest paid is 5624.32 − 5000 = 624.32 dollars.",
                             "That is 12.5% of the principal over three years.",
                             "At simple interest the interest would be 600 dollars, so "
                             "compounding added 24.32 dollars."],
                      ans="5624.32 dollars repaid, with 624.32 dollars of interest",
                      interp="The interest is a substantial fraction of the loan, and the "
                             "compounding is only part of the reason; the rate and the time "
                             "matter more."),
             ], inv=dict(
                 task="Take three loans or savings plans of your own: one short, one long and "
                      "one with a high rate. Model each with simple and compound interest, "
                      "tabulate five periods, and find the period at which the difference "
                      "exceeds 10% of the principal.",
                 table=[["plan", "rate", "simple at 5y", "compound at 5y", "difference"],
                        ["savings", "3%", "1150", "1159.27", "9.27"],
                        ["loan", "8%", "1400", "1469.33", "69.33"],
                        ["long loan", "12%", "1600", "1762.34", "162.34"]],
                 notice=["The difference grew with both the rate and the time.",
                         "The long loan at 12% differed by more than 10% of the principal.",
                         "The short low-rate plan differed by less than 1%.",
                         "Compound interest always gave the larger amount, whether it was a "
                         "debt or a saving."],
                 obs="Simple interest grows by a constant amount and compound interest grows "
                     "by a constant multiplier, and the two separate faster at higher rates "
                     "and over longer times.",
                 concl="A financial quantity is modelled by P(1 + rn) for simple interest and "
                       "P(1 + r)ⁿ for compound interest, and the choice between them changes "
                       "the answer by an amount that grows with the rate and the time.")),
        dict(id="8.3", title="Depreciation and reverse percentages",
             inquiry_q="How is a falling value modelled, and how are two offers compared?",
             teach=[
                 "Depreciation is a repeated percentage decrease, so it is modelled by a multiplier below 1 and the value falls exponentially towards zero without reaching it.",
                 "The value after n periods is V₀(1 − r)ⁿ, and the rate can be found from two values by taking the nth root of their ratio.",
                 "Comparing two offers means comparing the same quantity: the total cost over the same period, or the value at the same future date.",
                 "A lower price with a higher running cost can be worse than a higher price with a lower running cost, and only a model over a stated period can decide.",
             ], examples=[
                 dict(q="A machine costs 8000 dollars and loses 20% of its value each year. "
                        "Find its value after 4 years and the annual depreciation in the "
                        "fourth year.",
                      vis=F("table", [["year", "value", "loss that year"],
                                      ["0", "8000", "—"],
                                      ["1", "6400", "1600"],
                                      ["2", "5120", "1280"],
                                      ["3", "4096", "1024"],
                                      ["4", "3276.80", "819.20"]],
                            caption="the annual loss falls each year"),
                      reasoning="Apply the depreciation multiplier and compare consecutive "
                               "values.",
                      steps=["The multiplier is 0.80, so the value is 8000 × 0.8ⁿ.",
                             "After 4 years the value is 8000 × 0.4096 = 3276.80 dollars.",
                             "The loss in the fourth year is 4096 − 3276.80 = 819.20 dollars.",
                             "The loss falls each year, because it is a percentage of a "
                             "smaller amount.",
                             "The value never reaches zero in the model, though it becomes "
                             "negligible."],
                      ans="3276.80 dollars after 4 years, with a fourth-year loss of 819.20 "
                          "dollars",
                      interp="A percentage depreciation gives a falling amount each year, which "
                             "is the opposite of the rising amount a percentage rise gives."),
                 dict(q="Printer A costs 200 dollars with 40 dollars of ink a year; printer B "
                        "costs 120 dollars with 60 dollars a year. Find the number of years "
                        "after which B is more expensive.",
                      vis=F("grid", [(4, 360), (0, 200), (0, 120)], ["A", "A0", "B0"], 0, 6, 0,
                            500, [(0, 200), (4, 360)],
                            "the two cost lines cross at 4 years"),
                      reasoning="Model both total costs and find where they are equal.",
                      steps=["Printer A costs 200 + 40n dollars after n years.",
                             "Printer B costs 120 + 60n dollars after n years.",
                             "Setting them equal gives 80 = 20n, so n = 4.",
                             "For fewer than 4 years B is cheaper; for more, A is cheaper.",
                             "A buyer who keeps a printer for 6 years should choose A, saving "
                             "40 dollars."],
                      ans="B is more expensive after 4 years",
                      interp="The cheaper purchase is not always the cheaper option, and only a "
                             "model over a stated period can decide."),
             ], inv=dict(
                 task="Find three real best-value comparisons: two appliances, two phone "
                      "plans, or two transport options. Model the total cost of each over a "
                      "stated period, find the break-even point, and recommend one with a "
                      "stated assumption about how long it will be used.",
                 table=[["comparison", "model A", "model B", "break-even"],
                        ["two phones", "300 + 10n", "150 + 25n", "10 months"],
                        ["two bus passes", "40 + 2n", "90 + 0.5n", "33.3 rides"],
                        ["two printers", "200 + 40n", "120 + 60n", "4 years"]],
                 notice=["Every comparison had a break-even point.",
                         "The recommendation changed with the assumed period of use.",
                         "The cheaper purchase was better only for short use.",
                         "Stating the assumption was essential to the recommendation."],
                 obs="A best-value comparison is a model of total cost over a stated period, "
                     "and the recommendation depends on the period assumed.",
                 concl="Two offers are compared by modelling their total cost over the same "
                       "period, and the recommendation is only as good as the assumption about "
                       "how long the item will be used.")),
        dict(id="8.4", title="Comparing financial offers",
             inquiry_q="How are two financial offers compared fairly, and what does a single "
                       "figure hide?",
             teach=[
                 "Two offers are compared by modelling the total amount paid or received over the same period, because a headline rate says nothing about the length of the agreement or the fees attached to it.",
                 "An annual percentage rate is not the same as a monthly one multiplied by twelve, because compounding happens inside the year. Offers quoted in different periods must be converted before they are compared.",
                 "A single figure such as a monthly payment hides the total, and the total is what the customer pays. The honest comparison states the period, the fees and the total together.",
                 "A model that ignores a fee, a penalty or a change of rate is optimistic, and the limitation must be stated. Comparing offers is a modelling task before it is an arithmetic one.",
             ], examples=[
                 dict(q="Offer A is 1000 dollars at 12% a year simple interest for 3 years. "
                        "Offer B is 1000 dollars at 10% a year compound interest for 3 years. "
                        "Which costs more in total?",
                      vis=F("table", [["year", "A total", "B total"],
                                      ["1", "1120", "1100"],
                                      ["2", "1240", "1210"],
                                      ["3", "1360", "1331"]],
                            "simple interest adds a fixed amount, compound interest adds a "
                            "growing one"),
                      reasoning="Model each offer over the same period and compare the totals.",
                      steps=["Offer A adds 12% of 1000 each year, which is 120 a year.",
                             "After 3 years A is 1000 + 3 × 120 = 1360 dollars.",
                             "Offer B multiplies by 1.10 each year: 1000 × 1.10³ = 1331.",
                             "So A costs 29 dollars more in total over the 3 years.",
                             "The lower rate on B wins here, but only because the period is "
                             "short; over 10 years B would be dearer."],
                      ans="offer A costs more: 1360 against 1331 dollars",
                      interp="The cheaper rate is not always the cheaper offer, because the "
                             "period and the compounding both matter."),
                 dict(q="A savings account pays 0.5% a month with no fees. Another pays 6% a "
                        "year with a 5 dollar annual fee. Compare them on a balance of 2000 "
                        "dollars over one year.",
                      vis=F("table", [["account", "interest", "fee", "balance after a year"],
                                      ["monthly", "123.36", "0", "2123.36"],
                                      ["annual", "120", "5", "2115"]],
                            "the monthly account wins once the fee is counted"),
                      reasoning="Convert both to the same period, then subtract the fees.",
                      steps=["The monthly account gives 2000 × 1.005¹² = 2123.36 dollars.",
                             "The annual account gives 2000 × 1.06 = 2120 dollars, minus the "
                             "5 dollar fee.",
                             "So the annual account leaves 2115 dollars.",
                             "The monthly account wins by 8.36 dollars.",
                             "The fee of 5 dollars was the difference between the two rates, "
                             "and leaving it out would have reversed the answer."],
                      ans="the monthly account wins: 2123.36 against 2115 dollars",
                      interp="A fee can decide a comparison, so a model that omits it is not "
                             "a model of the offer."),
             ], inv=dict(
                 task="Collect three real financial offers: two savings accounts, two loan "
                      "advertisements, or two phone plans. Model each over the same period, "
                      "convert any rate to the same compounding period, include every fee you "
                      "can find, and rank them. Then write the limitation of your ranking.",
                 table=[["offer", "rate", "period", "fees", "total after 1 year", "rank"],
                        ["account A", "0.5% monthly", "12 months", "0", "2123.36", "1"],
                        ["account B", "6% yearly", "12 months", "5", "2115", "2"],
                        ["account C", "5.5% yearly", "12 months", "0", "2110", "3"]],
                 notice=["Rates quoted in different periods had to be converted before "
                         "comparing.",
                         "A small fee changed the ranking.",
                         "The offer with the highest headline rate was not the best.",
                         "The ranking held only for the period modelled."],
                 obs="Offers are compared by modelling the total over the same period, with "
                     "every fee included, and the ranking is valid only for that period.",
                 concl="A fair comparison states the period, the compounding and the fees, "
                       "and the model's limitation is part of the answer.")),
        dict(id="8.5", title="Modelling decisions and limitations",
             inquiry_q="Who does a rate favour, and how can a model show that?",
             teach=[
                 "A rate of interest is the price of access to money now, and it is paid by those who do not have the money and received by those who do.",
                 "A model can show the total cost of a loan over its life, and that total is often several times the amount borrowed, which the monthly figure hides.",
                 "Comparing a loan with saving for the same amount shows how much cheaper patience is, and the difference is the cost of access.",
                 "Fairness in lending is a question about the model's assumptions as much as about its arithmetic, because a rate that is affordable in one situation is crushing in another.",
             ], examples=[
                 dict(q="A loan of 1000 dollars at 3% a month is repaid over 12 months. Model "
                        "the total repaid and compare it with saving 84 dollars a month for 12 "
                        "months.",
                      vis=F("table", [["month", "balance", "interest that month"],
                                      ["1", "916", "30"],
                                      ["6", "500", "15"],
                                      ["12", "0", "2.5"]],
                            caption="the interest falls as the balance falls"),
                      reasoning="Model the loan recursively and compare the total with the "
                               "amount saved.",
                      steps=["Each month the balance grows by 3% and falls by 84 dollars.",
                             "The total repaid is 12 × 84 = 1008 dollars plus the interest "
                             "already included in the schedule.",
                             "Modelling month by month gives a total interest of about 197 "
                             "dollars.",
                             "So the loan costs about 1197 dollars in total for 1000 borrowed.",
                             "Saving 84 dollars a month for 12 months raises 1008 dollars with "
                             "no interest at all."],
                      ans="the loan costs about 1197 dollars in total; saving raises 1008 "
                          "dollars",
                      interp="Borrowing to get the money now costs about 20% of the amount, "
                             "which is the price of access, and the monthly figure of 84 "
                             "dollars hides it."),
                 dict(q="Two families each need 1200 dollars. One borrows at 3% a month and "
                        "one saves 100 dollars a month. Model both and compare the cost.",
                      vis=F("double_number_line", "borrowing", "saving",
                            "the same need met two ways"),
                      reasoning="Model the loan recursively and the saving linearly, and "
                               "compare the totals.",
                      steps=["The borrowing family repays about 1430 dollars in total, "
                             "including interest.",
                             "The saving family needs 12 months to reach 1200 dollars and "
                             "pays nothing extra.",
                             "The difference of about 230 dollars is the cost of access.",
                             "The saving family waits a year; the borrowing family has the "
                             "money now.",
                             "Which is fairer depends on why the money is needed, which the "
                             "model cannot say."],
                      ans="borrowing costs about 1430 dollars; saving costs 1200 dollars after "
                          "12 months",
                      interp="The model quantifies the cost of access, and the judgement about "
                             "whether it is worth paying is not a mathematical one."),
             ], inv=dict(
                 task="Choose one real lending or saving situation, such as a micro-loan, a "
                      "phone contract or a school fee plan. Model the total cost, find the "
                      "effective annual rate, and write a short account of who the "
                      "arrangement favours and who it does not.",
                 table=[["arrangement", "total cost", "effective annual rate", "favours"],
                        ["micro-loan at 3% a month", "about 1430 for 1200", "about 43%",
                         "the lender"],
                        ["phone contract over 24 months", "about 1200 for a 600 phone",
                         "about 25%", "the provider"],
                        ["savings at 5% a year", "1260 after 5 years", "5%", "the saver"]],
                 notice=["Every lending arrangement cost far more than the headline figure "
                         "suggested.",
                         "The effective annual rate was much larger than the monthly rate.",
                         "The savings arrangement was the only one that paid the customer.",
                         "The arrangements favoured whoever already had money."],
                 obs="A monthly rate compounded over a year gives an effective annual rate "
                     "much larger than the monthly rate suggests, and the model makes that "
                     "visible.",
                 concl="A model of a financial arrangement shows its total cost and its "
                       "effective rate, and the question of who it favours is answered by "
                       "comparing that cost with the alternative of saving.")),
        dict(id="8.6", title="Investigation: doubling and halving",
             inquiry_q="How far ahead can a financial model be trusted, and what breaks it?",
             teach=[
                 "A financial model is trusted while its rates hold, and rates change with inflation, policy and personal circumstance.",
                 "The longer the horizon, the larger the effect of a small error in the rate, because the model compounds the error.",
                 "A model that is accurate for one year can be badly wrong for twenty, and the difference is not arithmetic error but assumption error.",
                 "A responsible model states its horizon, its assumptions and the point at which it should be reviewed.",
             ], examples=[
                 dict(q="A family saves 200 dollars a month at 4% a year compound interest. "
                        "Model the balance after 10 and after 20 years, and comment on the "
                        "assumptions.",
                      vis=F("table", [["year", "balance"],
                                      ["0", "0"],
                                      ["5", "13206"],
                                      ["10", "29401"],
                                      ["20", "73700"]],
                            caption="the balance grows faster than the payments"),
                      reasoning="Model the payments as a series with compound growth.",
                      steps=["Each year the balance grows by 4% and 2400 dollars are added.",
                             "After 10 years the balance is about 29401 dollars, on payments "
                             "of 24000.",
                             "After 20 years it is about 73700 dollars, on payments of 48000.",
                             "The interest exceeds the payments after about 13 years.",
                             "The model assumes the rate stays at 4% for twenty years, which "
                             "no one can promise."],
                      ans="about 29401 dollars after 10 years and 73700 after 20",
                      interp="The interest eventually exceeds the contributions, which is the "
                             "power of compounding over a long horizon and also the source of "
                             "the model's fragility."),
                 dict(q="A loan of 200000 dollars at 5% a year is repaid over 25 years. Model "
                        "the total repaid and compare it with the amount borrowed.",
                      vis=F("grid", [(0, 200000), (25, 0)], ["borrowed", "cleared"], 0, 26,
                            -20000, 220000, [(0, 200000), (25, 0)],
                            "the balance falls slowly at first"),
                      reasoning="Model the repayments and compare the total with the "
                               "principal.",
                      steps=["The annual repayment is about 14150 dollars.",
                             "Over 25 years the total repaid is about 353700 dollars.",
                             "The interest is about 153700 dollars, which is 77% of the "
                             "amount borrowed.",
                             "In the first years most of each payment is interest.",
                             "The model assumes the rate is fixed for the whole term."],
                      ans="about 353700 dollars repaid in total, of which about 153700 dollars "
                          "is interest",
                      interp="The total cost of a long loan can approach twice the amount "
                             "borrowed, and the monthly figure of about 1179 dollars gives no "
                             "hint of it."),
             ], inv=dict(
                 task="Choose a long-term financial plan: a mortgage, a pension, a school fees "
                      "plan or a business loan. Model it over its full term, find the total "
                      "paid and the total interest, and then test the model with a rate 2 "
                      "percentage points higher to see how much the answer changes.",
                 table=[["plan", "total paid at 5%", "total at 7%", "change"],
                        ["mortgage 200000 over 25 years", "353700", "424200", "70500"],
                        ["pension saving 200 a month for 30 years", "149000", "n/a",
                         "rate matters less"],
                        ["loan 20000 over 5 years", "23000", "23800", "800"]],
                 notice=["A 2-point rise in the rate changed the total by tens of thousands.",
                         "The longer the term, the larger the effect of the rate change.",
                         "The short loan was barely affected.",
                         "Every model depended on the rate holding for the whole term."],
                 obs="The sensitivity of a financial model to its rate grows with the length "
                     "of the term, so a long plan is a statement about the future as much as "
                     "a calculation.",
                 concl="A long-term financial model is reliable only as a statement of what "
                       "happens if its rates hold, and its sensitivity to those rates is "
                       "itself an important result.")),
    ],
    practice=dict(
        A=[("8.1.1", "Increase 80 by 15% and then decrease the result by 15%.",
            "78.20", "Multiply by 1.15 then by 0.85.", "F"),
           ("8.1.2", "Find the single multiplier for a rise of 10% followed by a fall of 10%.",
            "0.99", "1.1 × 0.9 = 0.99.", "F"),
           ("8.1.3", "Find the multiplier for a fall of 25%.", "0.75",
            "1 − 0.25.", "F"),
           ("8.1.4", "Find 2000 × 1.06⁵ to the nearest cent.", "2676.45",
            "Apply the compound formula.", "F"),
           ("8.1.5", "Find the simple interest on 3000 dollars at 5% for 4 years.",
            "600 dollars", "3000 × 0.05 × 4.", "F"),
           ("8.1.6", "Find the value after 3 years of 5000 dollars depreciating at 20% a "
            "year.", "2560 dollars", "5000 × 0.8³.", "F"),
           ("8.1.7", "Find the annual multiplier for a 4% rise.", "1.04",
            "1 + 0.04.", "F"),
           ("8.1.8", "A price of 50 dollars rises by 20% and then by 10%. Find the final "
            "price.", "66 dollars", "50 × 1.2 × 1.1.", "F"),
           ("8.1.9", "Find the compound interest on 1000 dollars at 3% for 2 years.",
            "60.90 dollars", "1000 × 1.03² − 1000.", "F"),
           ("8.1.10", "A car worth 12000 dollars falls to 9000 dollars in a year. Find the "
            "percentage fall.", "25%", "(12000 − 9000)/12000.", "F"),
           ("8.1.11", "Find the value after 2 years of 800 dollars growing at 5% a year.",
            "882 dollars", "800 × 1.05².", "F"),
           ("8.1.12", "Find the overall percentage change for multipliers 1.2 and 0.9.",
            "a rise of 8%", "1.2 × 0.9 = 1.08.", "F")],
        B=[("8.2.1", "A population of 1000 falls by 10% a year. Find the rule and test it on "
            "the fifth year.",
            "1000 × 0.9ⁿ, giving 590.49 in year 5.", "Use a geometric model.", "R"),
           ("8.2.2", "Investigate the pattern in the balances of a loan of 1000 at 10% a "
            "month with 200 dollar repayments.",
            "The balance falls by 100, 90, 80, …, so the interest portion falls each month.",
            "Model month by month.", "R"),
           ("8.2.3", "Conjecture a rule for the total repaid on a loan of P at rate r over n "
            "months with fixed repayments, and test it.",
            "There is no simple closed form; the balance is P(1 + r)ⁿ − M(((1 + r)ⁿ − 1)/r).",
            "Model recursively and solve.", "C"),
           ("8.2.4", "Investigate the pattern in the difference between simple and compound "
            "interest on 1000 at 5% over 1 to 10 years.",
            "The difference grows slowly at first and then faster, following the compound "
            "term.", "Compute both for each year.", "R"),
           ("8.2.5", "Build a table of the value of 1000 dollars at 3% a month for 1 to 12 "
            "months and describe the pattern.",
            "The values multiply by 1.03 each month, so the growth accelerates.",
            "Compute the values.", "R"),
           ("8.2.6", "Conjecture a rule for the number of years for an investment to double "
            "at r% compound interest.",
            "About 72/r years, the rule of 72, accurate for rates between 4% and 12%.",
            "Solve (1 + r)ⁿ = 2.", "C"),
           ("8.2.7", "Investigate the pattern in the total cost of a 1000 dollar loan at "
            "different monthly rates over 12 months.",
            "The total rises faster than the rate, because the interest compounds.",
            "Model for several rates.", "R"),
           ("8.2.8", "A savings account pays interest monthly. Investigate the effective "
            "annual rate for a monthly rate of 1%.",
            "1.01¹² − 1 ≈ 12.68%, larger than 12%.", "Compound the monthly rate.", "R"),
           ("8.2.9", "Find the pattern in the values of a car that loses 15% a year and "
            "predict the value after 10 years from 20000 dollars.",
            "20000 × 0.85ⁿ, giving about 3922 dollars after 10 years.",
            "Use a geometric model.", "R"),
           ("8.2.10", "Investigate the pattern in the interest paid each year on a fixed "
            "mortgage.",
            "The interest falls each year while the capital repaid rises, keeping the payment "
            "constant.", "Model year by year.", "R"),
           ("8.2.11", "Conjecture a rule for the total interest paid on a loan of P at rate r "
            "over n years with annual repayments, for small r.",
            "About P × r × n/2, because the average balance is about half the principal.",
            "Model and approximate.", "C")],
        C=[("8.3.1", "Explain in your own words the difference between simple and compound "
            "interest.", "Simple interest is a fixed percentage of the original principal; "
            "compound interest is a percentage of the current amount, so the interest earns "
            "interest.", "State both definitions.", "R"),
           ("8.3.2", "Write a complete solution to: find the amount after 3 years on 1500 "
            "dollars at 4% compound interest.",
            "1687.30 dollars", "Use A = P(1 + r)ⁿ.", "F"),
           ("8.3.3", "Choose between simple and compound interest to model a 6-month saving "
            "and justify.", "Either is defensible; compound is correct for interest paid into "
            "the account, simple for a flat bonus.", "Say what each assumes.", "R"),
           ("8.3.4", "Set out a full solution to: find the value after 4 years of 9000 "
            "dollars depreciating at 30% a year.",
            "2160.90 dollars", "Use V₀(1 − r)ⁿ.", "F"),
           ("8.3.5", "Explain why a rise of 20% followed by a fall of 20% is a net fall.",
            "Because the multipliers are 1.2 and 0.8, whose product is 0.96, a fall of 4%.",
            "Multiply the multipliers.", "R"),
           ("8.3.6", "Describe, with an example, the difference between a multiplier and a "
            "percentage.", "A multiplier is the factor applied to the quantity, as 1.15; a "
            "percentage is the change relative to the quantity, as 15%.",
            "Compare the two.", "R"),
           ("8.3.7", "Explain why the effective annual rate is larger than twelve monthly "
            "rates added together.",
            "Because each month's interest is charged on a balance that already includes the "
            "previous interest, so the rate compounds.", "Compound twelve times.", "R"),
           ("8.3.8", "Write the reasoning that shows the interest portion of a fixed loan "
            "repayment falls over time.",
            "Because the interest is a percentage of a balance that falls with each payment, "
            "so the interest falls too.", "Model two months.", "R"),
           ("8.3.9", "Set out the argument that depreciation never reaches zero in the model.",
            "Because each year multiplies the previous value by a factor strictly between 0 "
            "and 1, so the value stays positive.", "Consider the limit.", "R"),
           ("8.3.10", "Explain what the break-even point means in a best-value comparison.",
            "The period of use at which the two options cost the same, so neither is better "
            "before it.", "Set the two models equal.", "R"),
           ("8.3.11", "Describe the relationship between the rate of a loan and its total "
            "cost.", "The total cost rises faster than the rate, because a higher rate both "
            "increases each interest charge and lengthens the repayment.",
            "Model at two rates.", "R"),
           ("8.3.12", "Explain, with an example, when a financial model is misleading.",
            "Any answer is acceptable if it identifies a monthly figure that hides the total, "
            "or a rate that changes without notice.", "Give a specific example.", "R")],
        D=[("8.4.1", "A worker earns 3000 dollars a month and spends 2550. Find the monthly "
            "surplus and the time to save 9000 dollars.",
            "Surplus 450 dollars; 20 months.", "Divide the goal by the surplus.", "A"),
           ("8.4.2", "A family borrows 1500 dollars at 4% a month and repays 200 dollars a "
            "month. Model the balance after 3 months.",
            "About 1122.53 dollars after 3 months.", "Model month by month.", "A"),
           ("8.4.3", "A school fee plan charges 120 dollars a month for 10 months for a "
            "900 dollar fee. Find the total paid and the effective annual rate.",
            "1200 dollars in total; about 44% a year.", "Compare the total with the fee.",
            "A"),
           ("8.4.4", "A shop's takings rise by 8% a year from 40000 dollars. Find the takings "
            "after 5 years and the total over 5 years.",
            "About 58773 dollars in year 5; about 263700 dollars in total.",
            "Use a geometric model and the series formula.", "A"),
           ("8.4.5", "A loan of 8000 dollars at 6% a year is repaid over 4 years. Model the "
            "total repaid and compare it with the principal.",
            "About 9230 dollars repaid, of which about 1230 is interest.",
            "Model the repayments.", "A"),
           ("8.4.6", "A bicycle worth 600 dollars loses 18% of its value a year. Find its "
            "value after 3 years and the total loss.",
            "About 331.50 dollars after 3 years; a loss of about 268.50 dollars.",
            "Use the depreciation model.", "A"),
           ("8.4.7", "Two bus passes are offered: 40 dollars plus 2 dollars a ride, or 90 "
            "dollars plus 0.50 dollars a ride. Investigate which is better for 20 rides a "
            "month and justify.",
            "The second, at 100 dollars against 80 dollars — no, the first is cheaper at 80 "
            "dollars.", "Model both and compare.", "R"),
           ("8.4.8", "A microfinance loan of 200 dollars at 5% a month is repaid over 6 "
            "months. Model the total repaid and find the effective annual rate.",
            "About 243 dollars repaid; an effective annual rate of about 79%.",
            "Model the repayments and compound the rate.", "A"),
           ("8.4.9", "A savings account pays 0.5% a month. Investigate whether it beats 6% a "
            "year simple interest over 3 years and justify.",
            "Yes: 1.005³⁶ − 1 ≈ 19.7%, against 18% simple.", "Compound the monthly rate.",
            "R"),
           ("8.4.10", "A company's revenue falls by 5% a year from 500000 dollars. "
            "Investigate when it falls below 300000 dollars and justify.",
            "After about 9 years, because 500000 × 0.95ⁿ < 300000 gives n > 8.6.",
            "Solve the exponential inequality.", "R"),
           ("8.4.11", "A farmer's yield rises by 3% a year from 20 tonnes. Find the yield "
            "after 15 years and comment on the model's usefulness.",
            "About 31.2 tonnes; the model assumes no limit on land or water, which is "
            "unrealistic.", "Use a geometric model.", "A"),
           ("8.4.12", "Explain, with a model of your own, when a monthly figure is a "
            "misleading way to report a cost.",
            "Any answer is acceptable if it shows that the monthly figure hides the total, as "
            "with 84 dollars a month for a 1000 dollar loan.",
            "Compare the monthly figure with the total.", "R")],
    ),
    assessment=[
        dict(title="A1 · The two loans",
             text="A family needs 1200 dollars. Option A is a loan at 3% a month repaid over "
                  "12 months. Option B is a savings plan of 100 dollars a month. Model both, "
                  "find the total cost of each, find the effective annual rate of the loan, "
                  "and write a short recommendation stating the assumption on which it "
                  "depends.",
             note="Criteria A and D · model both options, compare the totals, and justify the "
                  "recommendation."),
        dict(title="A2 · The long view",
             text="A deposit of 5000 dollars is invested at 5% compound interest a year, and "
                  "200 dollars a month is added. Model the balance after 5, 10 and 20 years, "
                  "find the year in which the accumulated interest first exceeds the total "
                  "paid in, and test the model with a rate of 3% to see how much the "
                  "20-year balance changes.",
             note="Criteria B and C · build the recursive model, justify the series, and "
                  "comment on the sensitivity to the rate."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of change, quantity "
        "and model appear in your work?",
        "How is the global context of fairness and development, and its exploration of access, "
        "saving and long-term planning, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a financial model for a decision about borrowing, and what "
        "would you still like to ask?",
    ],
    review=dict(
        ideas=["A percentage change is modelled by a multiplier.",
               "A rise of r then a fall of r gives a multiplier of 1 − r².",
               "Multipliers combine by multiplication, so the order does not matter.",
               "Simple interest is P(1 + rn); compound interest is P(1 + r)ⁿ.",
               "Depreciation is a repeated percentage decrease, modelled by a multiplier "
               "below 1.",
               "The effective annual rate compounds the monthly rate.",
               "The interest portion of a fixed repayment falls as the balance falls.",
               "A long-term model is sensitive to its assumed rate."],
        vocab=["percentage change", "multiplier", "simple interest", "compound interest",
               "principal", "depreciation", "effective annual rate", "break-even",
               "surplus", "recursive model", "horizon", "sensitivity"],
        mixed=[("8.R1", "Find the multiplier for a rise of 12%."),
               ("8.R2", "Find 1500 × 1.04³ to the nearest cent."),
               ("8.R3", "Find the value after 5 years of 9000 dollars at 20% depreciation."),
               ("8.R4", "Find the simple interest on 2500 dollars at 6% for 3 years."),
               ("8.R5", "A price rises 25% then falls 25%. Find the overall change."),
               ("8.R6", "Explain why a monthly rate of 1% is more than 12% a year.")],
    ),
    projects=dict(
        service=[("Community need", "Borrowing and saving decisions are made from monthly "
                                    "figures that hide the total."),
                 ("Mathematical connection", "Multipliers, compound models and effective "
                                             "rates."),
                 ("Proposed action", "Model one real loan or savings plan and publish its "
                                     "total cost and effective rate."),
                 ("Expected impact", "A reader can compare two offers on the same terms."),
                 ("Student reflection", "Record the model, the totals and what you found.")],
        community=[("Project idea", "A transparency audit of the costs the school publishes."),
                   ("Need", "Fees, trips and contracts are quoted per month or per term "
                            "without totals."),
                   ("Research question", "What is the true total cost of each arrangement, and "
                                         "who does it favour?"),
                   ("Mathematics", "Multipliers, compound interest and effective rates."),
                   ("Action or outcome", "A one-page table of totals and effective rates."),
                   ("Beneficiaries", "Every family paying the school's costs."),
                   ("Evidence", "The table with the models and the totals.")],
        personal=[("Personal interest", "Saving, spending or a small business idea."),
                  ("Learning goal", "To model a financial decision and state its total cost."),
                  ("Product or outcome", "A model with a total, a rate and a recommendation."),
                  ("Mathematics", "Multipliers and compound models."),
                  ("Process", "State the rate, model the periods, and compare the total with "
                              "the alternative."),
                  ("Evidence", "The model, the total and the comparison.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=9, title="Congruence, Similarity and Transformations",
    key="Form", related=["Space", "Equivalence", "Representation"],
    context="Scientific and technical innovation",
    exploration="Scale models, design and measurement at a distance",
    inquiry=("Two shapes are congruent when one can be moved onto the other by a rigid "
             "transformation, and similar when one can be obtained from the other by an "
             "enlargement; the transformations are therefore the test of equivalence, and the "
             "scale factor is what connects a model to the object it represents."),
    atl=("Communication",
         "Students describe a transformation precisely enough for another person to reproduce "
         "it, and justify why two shapes are or are not congruent."),
    standfirst="A translation, a reflection and a rotation preserve shape and size. An "
               "enlargement preserves shape alone, and the scale factor connects every length "
               "on the model to the object.",
    engage="A scale model of a bridge is 40 cm long and the real bridge is 200 m long. What "
           "is the scale, and how heavy is the real bridge if the model weighs 300 g?",
    questions=[("Factual", "What are the four transformations, and what are the four tests for "
                           "congruent triangles?"),
               ("Conceptual", "Why is a transformation a better test of congruence than "
                              "measurement, and how does the scale factor connect lengths, "
                              "areas and volumes?"),
               ("Debatable", "Is a scale model a representation of the real thing or a "
                             "different object, and does the answer change when the model is "
                             "used for a decision?")],
    application_lede="Each task asks you to describe a transformation or to use a scale "
                     "factor. State the transformation in full, and say what it preserves.",
    projects_lede="Scale models let us build what we cannot yet measure. Model one and say "
                  "what the scale factor does and does not preserve.",
    sections=[
        dict(id="9.1", title="Transformations and congruence",
             inquiry_q="What does each transformation preserve, and how is it described "
                       "exactly?",
             teach=[
                 "A translation moves every point by the same vector. It preserves length, angle, area and orientation, and it is described by a column vector.",
                 "A reflection in a mirror line turns the shape over. It preserves length and angle but reverses orientation, and the mirror line is the perpendicular bisector of every segment joining a point to its image.",
                 "A rotation about a centre through an angle preserves length and angle. It is described by the centre, the angle and the direction, and all three are needed.",
                 "An enlargement about a centre by a scale factor k multiplies every distance from the centre by k. Lengths scale by k, areas by k² and volumes by k³, so an enlargement is not a rigid transformation when k ≠ 1.",
                 "A transformation is a rule in space: it takes each point of a shape to exactly one image point, and the whole shape is carried with it.",
                 "Two shapes are congruent when one can be carried onto the other by translations, reflections and rotations alone, so congruence is the equivalence that a rigid transformation preserves.",
                 "Four tests decide congruence of triangles from three pieces of information: SSS, SAS, ASA and RHS. Each is sufficient because three measurements fix a triangle, so any two triangles with them must be identical.",
                 "ASS is not a test, because two sides and a non-included angle allow two different triangles. This ambiguous case is the reason the angle in SAS must be the included one.",
                 "A representation of a shape as a set of coordinates makes each transformation a calculation on those coordinates, which is how a design is checked exactly rather than by eye.",
             ], examples=[
                 dict(q="Translate the triangle with vertices (2, 1), (5, 1) and (2, 4) by the "
                        "vector (4, −3), and describe what is preserved.",
                      vis=F("transform", [(2, 1), (5, 1), (2, 4)], [(6, -2), (9, -2), (6, 1)],
                            "x", "the image is 4 right and 3 down"),
                      reasoning="Add the vector to each vertex.",
                      steps=["(2, 1) maps to (2 + 4, 1 − 3) = (6, −2).",
                             "(5, 1) maps to (5 + 4, 1 − 3) = (9, −2).",
                             "(2, 4) maps to (2 + 4, 4 − 3) = (6, 1).",
                             "Every side keeps its length and every angle keeps its size, so "
                             "the image is congruent to the original.",
                             "The orientation is unchanged, because no reflection is "
                             "involved."],
                      ans="the image has vertices (6, −2), (9, −2) and (6, 1)",
                      interp="A translation is fully described by one vector, and it preserves "
                             "everything except position."),
                 dict(q="Reflect the triangle with vertices (2, 1), (5, 1) and (2, 4) in the "
                        "y-axis, and state what changes.",
                      vis=F("transform", [(2, 1), (5, 1), (2, 4)], [(-2, 1), (-5, 1), (-2, 4)],
                            "x", "reflection in the y-axis"),
                      reasoning="Change the sign of each x-coordinate.",
                      steps=["Reflecting in the y-axis maps (x, y) to (−x, y).",
                             "So the vertices become (−2, 1), (−5, 1) and (−2, 4).",
                             "The side lengths and the angles are unchanged, so the image is "
                             "congruent.",
                             "The orientation is reversed: a clockwise order becomes "
                             "anticlockwise.",
                             "The y-axis is the perpendicular bisector of each joining "
                             "segment."],
                      ans="the image has vertices (−2, 1), (−5, 1) and (−2, 4)",
                      interp="A reflection preserves shape and size but reverses orientation, "
                             "which is the one thing a translation cannot do."),
             ], inv=dict(
                 task="Take one shape on squared paper. Apply a translation, a reflection, a "
                      "rotation and an enlargement of your own choice. For each, record the "
                      "image, the invariant quantities and the quantities that change.",
                 table=[["transformation", "preserved", "changed"],
                        ["translation", "length, angle, area, orientation", "position"],
                        ["reflection", "length, angle, area", "orientation, position"],
                        ["rotation", "length, angle, area", "position, orientation"],
                        ["enlargement k = 2", "angle", "length, area, position"]],
                 notice=["The three rigid transformations preserved every measurement.",
                         "The enlargement preserved angles but doubled lengths and quadrupled "
                         "areas.",
                         "Only the reflection and the rotation changed the orientation.",
                         "The enlargement was the only transformation that was not an "
                         "equivalence of measurement."],
                 obs="The rigid transformations preserve every measurement, and the "
                     "enlargement preserves angles alone while scaling lengths, areas and "
                     "volumes by k, k² and k³.",
                 concl="A transformation is a rule that moves a shape, and what it preserves "
                       "decides whether the image is congruent or merely similar to the "
                       "original.")),
        dict(id="9.2", title="Similarity and similar triangles",
             inquiry_q="How is it shown that two triangles are similar, and what does the "
                       "scale factor decide?",
             teach=[
                 "Two shapes are similar when one is an enlargement of the other, so corresponding angles are equal and corresponding sides are in the same ratio. The ratio is the scale factor.",
                 "Two tests decide similarity of triangles from angles alone: AA, because two equal angles force the third, and the equiangular test, because three equal angles force the sides into proportion.",
                 "The scale factor k multiplies every length, so a pair of corresponding sides gives k. Areas then scale by k² and volumes by k³, which is why the factor for an area is the square of the factor for a length.",
                 "Similarity is the equivalence that lets an inaccessible measurement be found from an accessible one, and the argument is complete only when the equal angles are named.",
             ], examples=[
                 dict(q="A tree and a 1.8 m stick stand vertically. The stick's shadow is 2.4 m "
                        "and the tree's is 9 m. Find the height of the tree.",
                      vis=F("triangle", [(0, 0), (9, 0), (0, 6)], ["9 m", "h", ""],
                            right=[(0, 0, "")],
                            title="the sun's rays make similar triangles"),
                      reasoning="The two triangles are similar, so the ratios of "
                               "corresponding sides are equal.",
                      steps=["The stick and the tree are both vertical, and the sun's rays "
                             "make the same angle with the ground.",
                             "So the two right-angled triangles are similar by AA.",
                             "The scale factor is 9/2.4 = 3.75.",
                             "The tree is therefore 3.75 × 1.8 = 6.75 m tall.",
                             "The height was found without measuring the tree, which is the "
                             "point of the method."],
                      ans="the tree is 6.75 m tall",
                      interp="Similarity converts one measurement into another, and the equal "
                             "angles are what make the conversion valid."),
                 dict(q="Two triangles have angles 50°, 60° and 70°, and 50°, 60° and 70°. "
                        "Are they similar, and what else is needed to find the scale factor?",
                      vis=F("triangle", [(0, 0), (6, 0), (2, 2.6)], ["", "", ""],
                            angles=[(0, 0, "50°")],
                            title="equal angles force proportional sides"),
                      reasoning="Equal corresponding angles give similarity, and one pair of "
                               "corresponding sides gives the factor.",
                      steps=["All three angles match, so the triangles are similar by the "
                             "equiangular test.",
                             "Similarity fixes the ratios but not the sizes.",
                             "One pair of corresponding sides is needed to find k.",
                             "If a side of 4 cm corresponds to a side of 10 cm, then k = 2.5.",
                             "Every other length in the second triangle is 2.5 times the "
                             "matching length in the first."],
                      ans="yes, similar by the equiangular test; one pair of corresponding "
                          "sides gives the scale factor",
                      interp="Similarity is about shape, and the scale factor is about size, "
                             "so the two questions need different information."),
             ], inv=dict(
                 task="Find three pairs of similar triangles in the room or in a picture: one "
                      "pair from shadows, one from a photograph, and one you construct by "
                      "enlarging a drawn triangle by a factor of 2. For each, name the equal "
                      "angles, list the ratios of corresponding sides, and check that the "
                      "ratios are all the same. Then measure one area in each pair and check "
                      "that it scales by the square of the factor.",
                 table=[["pair", "equal angles", "scale factor", "area ratio"],
                        ["stick and tree", "sun angle, right angle", "3.75", "14.06"],
                        ["photo and object", "corresponding angles", "0.2", "0.04"],
                        ["drawn and enlarged", "all three", "2", "4"]],
                 notice=["Every similar pair had equal corresponding angles.",
                         "The ratios of corresponding sides were all the same number.",
                         "The area ratio was always the square of the length ratio.",
                         "The shadow pair gave a measurement that could not be taken "
                         "directly."],
                 obs="Similar triangles have equal angles and proportional sides, and the "
                     "scale factor multiplies lengths while its square multiplies areas.",
                 concl="Similarity is an equivalence of shape, and the scale factor is the "
                       "single number that converts every length, every area and every volume "
                       "between two similar figures.")),
        dict(id="9.3", title="Enlargement and scale factors",
             inquiry_q="How does a scale factor connect lengths, areas and volumes?",
             teach=[
                 "Two shapes are similar when corresponding angles are equal and corresponding sides are in the same ratio. The ratio is the scale factor.",
                 "For triangles, equal angles are enough, because the sides are then forced into proportion. This is the AA test for similarity.",
                 "Lengths scale by k, areas by k² and volumes by k³. This is why a model twice as long has four times the surface and eight times the volume.",
                 "The scale factor can be found from any pair of corresponding lengths, and it is the same for all of them. A single measurement is enough to connect a model to the object.",
             ], examples=[
                 dict(q="A model bridge is 40 cm long and the real bridge is 200 m long. Find "
                        "the scale, and find the real length of a part that is 3 cm on the "
                        "model.",
                      vis=F("scale_drawing", ("40 cm", "200 m"), "1 : 500", "rectangle",
                            "the model and the object"),
                      reasoning="Convert both lengths to the same unit and form the ratio.",
                      steps=["200 m = 20000 cm.",
                             "The scale is 40 : 20000, which is 1 : 500.",
                             "So every centimetre on the model is 500 cm, or 5 m, in reality.",
                             "A part of 3 cm on the model is 3 × 500 = 1500 cm, or 15 m, long.",
                             "The scale is stated as a ratio of model to object, and the order "
                             "must be said."],
                      ans="the scale is 1 : 500, and a 3 cm part is 15 m long",
                      interp="One ratio connects every length on the model to the object, which "
                             "is what makes a scale drawing useful."),
                 dict(q="Two similar bottles have heights in the ratio 1 : 3. Find the ratio "
                        "of their surface areas and of their capacities.",
                      vis=F("prism", "cuboid", 2, 3, 2, "the smaller bottle"),
                      reasoning="Areas scale by k² and volumes by k³.",
                      steps=["The length scale factor is 3.",
                             "The surface area ratio is 3² : 1 = 9 : 1.",
                             "The capacity ratio is 3³ : 1 = 27 : 1.",
                             "So the taller bottle holds twenty-seven times as much and needs "
                             "nine times the material.",
                             "That is why large containers are cheaper per unit volume than "
                             "small ones."],
                      ans="surface areas 9 : 1, capacities 27 : 1",
                      interp="The scale factor connects lengths directly, areas through its "
                             "square and volumes through its cube, and the three are often "
                             "confused."),
             ], inv=dict(
                 task="Take four pairs of similar objects: two photographs, two bottles, two "
                      "maps and one pair of your own. For each, find the length scale factor, "
                      "then use it to predict the area and the volume ratios, and check one "
                      "prediction by measurement.",
                 table=[["pair", "length ratio", "area ratio", "volume ratio"],
                        ["two photos", "2 : 1", "4 : 1", "—"],
                        ["two bottles", "3 : 1", "9 : 1", "27 : 1"],
                        ["two maps", "1 : 2", "1 : 4", "—"],
                        ["two cubes", "5 : 1", "25 : 1", "125 : 1"]],
                 notice=["Every area ratio was the square of the length ratio.",
                         "Every volume ratio was the cube of the length ratio.",
                         "The maps were smaller than the objects, so the ratio was less than "
                         "one.",
                         "A measurement of one pair confirmed the prediction exactly."],
                 obs="The scale factor connects lengths directly, areas through its square and "
                     "volumes through its cube, and the connection holds for every pair of "
                     "similar objects.",
                 concl="Two similar objects are connected by one scale factor, and that factor "
                       "raised to the second and third powers connects their areas and their "
                       "volumes.")),
        dict(id="9.4", title="Transformations on the coordinate plane",
             inquiry_q="How is each transformation written as a rule on coordinates, and what "
                       "does the rule preserve?",
             teach=[
                 "On the coordinate plane a transformation is a rule on pairs of numbers, and the rule is what makes the image exact rather than approximate.",
                 "A translation by the vector (a, b) sends (x, y) to (x + a, y + b). A reflection in the y-axis sends (x, y) to (−x, y), and a reflection in the x-axis sends it to (x, −y).",
                 "A rotation of 90° anticlockwise about the origin sends (x, y) to (−y, x), and a rotation of 180° sends it to (−x, −y). The order of the coordinates is what changes, so the rule is easy to check on a single point.",
                 "An enlargement by scale factor k about the origin sends (x, y) to (kx, ky), so the coordinates are multiplied rather than added, and the shape grows away from the centre.",
                 "A transformation is an equivalence of shape when it is a translation, reflection or rotation, and the coordinate rule shows which property is preserved: lengths for the rigid ones, ratios for the enlargement.",
             ], examples=[
                 dict(q="The triangle has vertices A(2, 1), B(5, 1) and C(2, 4). Find its image "
                        "under the translation (4, −3), and state what the transformation "
                        "preserves.",
                      vis=F("grid", [(2, 1), (5, 1), (2, 4), (6, -2), (9, -2), (6, 1)],
                            ["A", "B", "C", "A'", "B'", "C'"], -1, 11, -5, 6,
                            [(2, 1), (5, 1), (2, 4), (6, -2), (9, -2), (6, 1)],
                            "the triangle and its image under the translation"),
                      reasoning="Add the vector to each vertex.",
                      steps=["A(2, 1) maps to (2 + 4, 1 − 3) = (6, −2).",
                             "B(5, 1) maps to (9, −2).",
                             "C(2, 4) maps to (6, 1).",
                             "The image is congruent to the original, so every length and "
                             "angle is preserved.",
                             "The rule (x, y) maps to (x + 4, y − 3) describes the whole "
                             "transformation at once."],
                      ans="A′(6, −2), B′(9, −2), C′(6, 1); lengths, angles and area are "
                          "preserved",
                      interp="One rule applied to three vertices gives the whole image, which "
                             "is why coordinates are used for exact transformations."),
                 dict(q="The point P(3, 5) is rotated 90° anticlockwise about the origin, then "
                        "reflected in the x-axis. Find the final image.",
                      vis=F("grid", [(3, 5), (-5, 3), (-5, -3)], ["P", "after rotation",
                                                                  "after reflection"],
                            -7, 7, -7, 7, [(3, 5), (-5, 3), (-5, -3)],
                            "a rotation followed by a reflection"),
                      reasoning="Apply each rule in turn, keeping track of the order.",
                      steps=["A 90° anticlockwise rotation sends (x, y) to (−y, x).",
                             "So P(3, 5) maps to (−5, 3).",
                             "A reflection in the x-axis sends (x, y) to (x, −y).",
                             "So (−5, 3) maps to (−5, −3).",
                             "The order matters: reflecting first and rotating second gives a "
                             "different point."],
                      ans="the final image is (−5, −3)",
                      interp="Transformations compose, and the composition is not the same in "
                             "both orders, so the sequence must be stated."),
             ], inv=dict(
                 task="Take a shape of your own with three or four vertices. Apply four "
                      "transformations in turn: a translation, a reflection in the y-axis, a "
                      "rotation of 90° anticlockwise about the origin, and an enlargement of "
                      "factor 2 about the origin. Record the coordinates after each step, and "
                      "for each transformation state whether lengths, angles, area and "
                      "orientation are preserved. Then try the same four in a different order "
                      "and compare the final images.",
                 table=[["step", "rule", "A(2, 1)", "B(5, 1)", "lengths", "area"],
                        ["start", "—", "(2, 1)", "(5, 1)", "—", "—"],
                        ["translate (4, −3)", "(x, y) maps to (x + 4, y − 3)", "(6, −2)", "(9, −2)", "yes", "same"],
                        ["reflect in y-axis", "(x, y) maps to (−x, y)", "(−6, −2)", "(−9, −2)", "yes", "same"],
                        ["rotate 90° anticlockwise", "(x, y) maps to (−y, x)", "(2, −6)", "(2, −9)", "yes", "same"],
                        ["enlarge factor 2", "(x, y) maps to (2x, 2y)", "(4, −12)", "(4, −18)", "no", "×4"]],
                 notice=["The three rigid transformations preserved every length and angle.",
                         "The enlargement preserved angles but doubled lengths and quadrupled "
                         "area.",
                         "The reflection reversed the orientation.",
                         "Doing the four steps in a different order gave a different final "
                         "image."],
                 obs="Each transformation is a rule on coordinates, and the rule shows "
                     "immediately which properties are preserved.",
                 concl="Transformations on the coordinate plane are arithmetic rules on "
                       "pairs, and the rigid ones preserve length while an enlargement "
                       "preserves only angle and ratio.")),
        dict(id="9.5", title="Similarity in area and volume",
             inquiry_q="How do area and volume scale when a figure is enlarged, and why is "
                       "the factor squared or cubed?",
             teach=[
                 "When a figure is enlarged by scale factor k, every length is multiplied by k, every area by k² and every volume by k³. The exponents come from the number of dimensions the quantity measures.",
                 "The reason is dimensional: an area is a product of two lengths and a volume a product of three, so the factor appears twice or three times. This is why a model twice as long has four times the surface and eight times the volume.",
                 "A quantity per unit area, such as paint per square metre, is divided by k² under an enlargement, and a quantity per unit volume, such as the mass of a solid, is multiplied by k³. Forgetting which way the factor acts is the commonest error.",
                 "Scaling is a representation of a real object at a different size, and it is valid only for the quantities that scale with the dimensions named. Weight, strength and cost need their own models.",
             ], examples=[
                 dict(q="A scale model of a courtyard is drawn at 1 : 50. The plan shows a "
                        "rectangular lawn 7.2 cm by 4.8 cm. Find the real area and the real "
                        "perimeter.",
                      vis=F("grid", [(0, 0), (7.2, 4.8)], ["plan", ""], -1, 9, -1, 7,
                            [(0, 0), (7.2, 4.8)],
                            "the plan at 1 : 50"),
                      reasoning="Lengths scale by 50, so the real dimensions are 50 times the "
                               "drawn ones.",
                      steps=["The real length is 7.2 × 50 = 360 cm = 3.6 m.",
                             "The real width is 4.8 × 50 = 240 cm = 2.4 m.",
                             "The real area is 3.6 × 2.4 = 8.64 m².",
                             "The real perimeter is 2(3.6 + 2.4) = 12 m.",
                             "The drawn area is 7.2 × 4.8 = 34.56 cm², and 50² × 34.56 cm² = "
                             "8.64 m², so the area scales by the square of the factor."],
                      ans="real area 8.64 m², real perimeter 12 m",
                      interp="A length scale factor of 50 becomes an area scale factor of "
                             "2500, and the two must not be confused."),
                 dict(q="Two similar bottles have heights in the ratio 1 : 3. The small "
                        "bottle holds 0.5 litres. How much does the large one hold, and what "
                        "is the ratio of their surface areas?",
                      vis=F("table", [["quantity", "small", "large", "factor"],
                                      ["height", "h", "3h", "3"],
                                      ["surface area", "S", "9S", "9"],
                                      ["volume", "0.5 L", "13.5 L", "27"]],
                            "lengths ×3, areas ×9, volumes ×27"),
                      reasoning="The volume scales by the cube of the length factor and the "
                               "area by its square.",
                      steps=["The length factor is 3, so the area factor is 3² = 9.",
                             "The volume factor is 3³ = 27.",
                             "The large bottle holds 27 × 0.5 = 13.5 litres.",
                             "The surface area of the large bottle is 9 times that of the "
                             "small one.",
                             "So trebling the height multiplies the capacity by 27, which is "
                             "why a taller bottle looks far bigger than it is."],
                      ans="13.5 litres; surface areas in the ratio 1 : 9",
                      interp="Volume grows faster than area, and area faster than length, so "
                             "a small change in size changes capacity a great deal."),
             ], inv=dict(
                 task="Take three pairs of similar objects: two photographs at different "
                      "scales, two maps of the same area at different scales, and two "
                      "containers of the same shape but different sizes. For each pair, find "
                      "the length factor, then measure or calculate the area factor and the "
                      "volume factor, and check that they are the square and the cube of the "
                      "length factor.",
                 table=[["pair", "length factor", "area factor", "volume factor"],
                        ["photo 1 : photo 2", "2", "4", "—"],
                        ["map 1 : 25 000", "4", "16", "—"],
                        ["cup A : cup B", "1.5", "2.25", "3.375"]],
                 notice=["Every area factor was the square of the length factor.",
                         "The volume factor was the cube, where a volume could be measured.",
                         "A map factor of 4 in length meant 16 times the ground area.",
                         "The two cups held very different amounts for a small difference in "
                         "height."],
                 obs="Lengths scale by k, areas by k² and volumes by k³, and each factor is "
                     "the length factor raised to the number of dimensions.",
                 concl="The exponent in a scale factor counts dimensions, so similarity "
                       "converts a length ratio into an area ratio or a volume ratio by "
                       "squaring or cubing it.")),
        dict(id="9.6", title="Investigation: shadows and scale",
             inquiry_q="How can the size of something inaccessible be found from a model or a "
                       "photograph?",
             teach=[
                 "Similarity allows a measurement of an inaccessible object to be found from a photograph or a shadow, provided something of known size is in the same picture.",
                 "A shadow method uses the fact that the sun's rays are parallel, so the object and its shadow form a pair of similar triangles with a reference object and its shadow.",
                 "The method assumes the ground is level, the object is vertical and the light source is effectively at infinity. Each assumption is a place where the method can fail.",
                 "A measurement obtained this way is an estimate, and stating the assumptions is part of reporting it.",
             ], examples=[
                 dict(q="A person 1.7 m tall casts a shadow 2.4 m long. A tree casts a shadow "
                        "18 m long at the same time. Find the height of the tree.",
                      vis=F("triangle", [(0, 0), (2.4, 0), (0, 1.7)], ["2.4 m", "", "1.7 m"],
                            right=[(0, 0, "")], title="the person and the shadow"),
                      reasoning="The two triangles are similar, so the ratios of corresponding "
                               "sides are equal.",
                      steps=["The person and the shadow form a right triangle with legs 1.7 m "
                             "and 2.4 m.",
                             "The tree and its shadow form a similar triangle with legs h and "
                             "18 m.",
                             "So h/18 = 1.7/2.4.",
                             "Hence h = 18 × 1.7/2.4 = 12.75 m.",
                             "The method assumes level ground, a vertical tree and parallel "
                             "rays."],
                      ans="the tree is 12.75 m tall",
                      interp="One ratio of similar triangles gives the height of something that "
                             "cannot be measured directly, and the assumptions must be stated "
                             "for the answer to be honest."),
                 dict(q="A photograph shows a door 2 m tall and a building 9 times as tall in "
                        "the picture. Estimate the building's height and comment on the "
                        "method.",
                      vis=F("scale_drawing", ("2 m", "18 m"), "from the photograph", "rectangle",
                            "the door as the reference"),
                      reasoning="Use the ratio of the heights in the picture as the scale "
                               "factor.",
                      steps=["The door is 2 m tall and appears 9 times smaller than the "
                             "building.",
                             "So the building is about 9 × 2 = 18 m tall.",
                             "The estimate assumes the photograph is not distorted and the "
                             "camera was level.",
                             "A wide-angle lens would make the building look smaller near the "
                             "edges.",
                             "The estimate is therefore approximate, and its error comes from "
                             "the photograph."],
                      ans="about 18 m, subject to the distortion of the photograph",
                      interp="A reference object of known size makes an inaccessible "
                             "measurement possible, and the reliability of the answer depends "
                             "on the assumptions about the picture."),
             ], inv=dict(
                 task="Measure the height of something you cannot reach: a tree, a building, "
                      "a flagpole or a lamp post. Use either the shadow method or the "
                      "photograph method with a reference object, state your assumptions, and "
                      "compare with a direct measurement if one is possible.",
                 table=[["method", "reference", "estimate", "assumption"],
                        ["shadow", "a person 1.7 m, shadow 2.4 m", "12.75 m",
                         "level ground, parallel rays"],
                        ["photograph", "a door 2 m tall", "18 m", "no lens distortion"],
                        ["direct", "tape measure", "12.8 m", "the tape reaches"]],
                 notice=["The shadow estimate was within a few centimetres of the direct "
                         "measurement.",
                         "The photograph estimate was less accurate, because of the lens.",
                         "Both indirect methods needed a reference of known size.",
                         "Stating the assumptions showed where each method could fail."],
                 obs="An inaccessible length is estimated by setting up a pair of similar "
                     "triangles with a reference of known size, and the estimate carries the "
                     "assumptions of the method.",
                 concl="Similarity allows a measurement at a distance, and the honesty of the "
                       "result depends on stating the assumptions that make the two triangles "
                       "similar.")),
    ],
    practice=dict(
        A=[("9.1.1", "Translate (3, 2) by the vector (−2, 5).", "(1, 7)",
            "Add the vector to the point.", "F"),
           ("9.1.2", "Reflect (4, −1) in the x-axis.", "(4, 1)",
            "Change the sign of y.", "F"),
           ("9.1.3", "Reflect (4, −1) in the y-axis.", "(−4, −1)",
            "Change the sign of x.", "F"),
           ("9.1.4", "State whether two triangles with sides 3, 4, 5 and 3, 4, 6 are "
            "congruent.", "No: the third sides differ, so SSS fails.",
            "Compare all three sides.", "F"),
           ("9.1.5", "Two triangles have sides 5 and 7 with an included angle of 60°. Are "
            "they congruent?", "Yes, by SAS.",
            "Two sides and the included angle is a test.", "F"),
           ("9.1.6", "Find the ratio of the areas of two similar shapes with length ratio "
            "3 : 5.", "9 : 25", "Square the length ratio.", "F"),
           ("9.1.7", "Find the ratio of the volumes of two similar solids with length ratio "
            "2 : 3.", "8 : 27", "Cube the length ratio.", "F"),
           ("9.1.8", "A map has scale 1 : 25000. Find the real distance for 4 cm on the map.",
            "1 km", "4 × 25000 cm = 100000 cm.", "F"),
           ("9.1.9", "Enlarge (2, 3) by scale factor 3 about the origin.", "(6, 9)",
            "Multiply each coordinate by 3.", "F"),
           ("9.1.10", "Rotate (1, 0) through 90° anticlockwise about the origin.", "(0, 1)",
            "A quarter turn maps (x, y) to (−y, x).", "F"),
           ("9.1.11", "A model is 15 cm long at a scale of 1 : 200. Find the real length.",
            "30 m", "15 × 200 cm.", "F"),
           ("9.1.12", "State whether two right-angled triangles with hypotenuse 10 and one "
            "leg 6 are congruent.", "Yes, by RHS or SSS.",
            "The third side is fixed by Pythagoras.", "F")],
        B=[("9.2.1", "The perimeters of similar figures are in the ratio 2 : 7. Find the ratio "
            "of their areas and justify.",
            "4 : 49, because area scales as the square of the length ratio.",
            "Square the ratio.", "R"),
           ("9.2.2", "Investigate the pattern in the areas of the images of a shape under "
            "enlargements of factor 1, 2, 3, 4.",
            "The areas are 1, 4, 9, 16 times the original.",
            "Square each factor.", "R"),
           ("9.2.3", "Conjecture a rule for the ratio of the volumes of two similar cylinders "
            "with radii in the ratio 1 : 4.",
            "1 : 64, because volume scales as the cube.", "Cube the ratio.", "R"),
           ("9.2.4", "Investigate whether two triangles with angles 50°, 60° and 70° are "
            "congruent, and justify.",
            "No: AAA gives similarity only, and the size is not fixed.",
            "Equal angles force proportion, not equality.", "R"),
           ("9.2.5", "Build a table of the images of a triangle under reflections in the two "
            "axes and describe the combined effect.",
            "Reflecting in both axes is a rotation of 180° about the origin.",
            "Apply the reflections in turn.", "R"),
           ("9.2.6", "Conjecture a rule for the scale factor that doubles the area of a "
            "shape.", "√2, because the area scales as the square of the factor.",
            "Solve k² = 2.", "R"),
           ("9.2.7", "Investigate the pattern in the number of congruent copies of a triangle "
            "that tile a rectangle.",
            "Two copies tile a rectangle if the triangle is halved along an altitude.",
            "Draw and count.", "R"),
           ("9.2.8", "A shape is enlarged by factor k and then by factor m. Investigate the "
            "combined effect and justify.",
            "A single enlargement by factor km, because the multiplications compose.",
            "Track one point through both steps.", "R"),
           ("9.2.9", "Find the pattern in the side lengths of the images of a square under "
            "enlargements of factor 1, ½, ¼.",
            "The sides are 1, ½, ¼, halving each time.", "Multiply by the factor.", "R"),
           ("9.2.10", "Investigate the ratio of the surface areas of two similar spheres with "
            "radii in the ratio 3 : 1.",
            "9 : 1, because surface area scales as the square.", "Square the ratio.", "R"),
           ("9.2.11", "Conjecture a rule for the number of lines of symmetry of a regular "
            "n-sided polygon.",
            "n lines, one through each vertex and the opposite side midpoint.",
            "Draw for n = 3, 4, 5.", "R")],
        C=[("9.3.1", "Explain in your own words what it means for two shapes to be congruent.",
            "That one can be moved onto the other by a rigid transformation, so all "
            "measurements match.", "State the definition.", "R"),
           ("9.3.2", "Write a complete solution to: enlarge the triangle (1, 1), (4, 1), "
            "(1, 3) by factor 2 about the origin.",
            "(2, 2), (8, 2), (2, 6)", "Multiply each coordinate by 2.", "F"),
           ("9.3.3", "Choose between measuring and transforming to decide congruence and "
            "justify.", "Transforming, because it is exact where measurement is approximate.",
            "Say what each gives.", "R"),
           ("9.3.4", "Set out a full solution to: find the scale factor between two similar "
            "rectangles with areas 12 cm² and 108 cm².",
            "3, because 108/12 = 9 and √9 = 3.", "Take the square root of the area ratio.",
            "F"),
           ("9.3.5", "Explain why ASS is not a congruence test.",
            "Because two different triangles can share two sides and a non-included angle, as "
            "the ambiguous case shows.", "Try to construct two.", "R"),
           ("9.3.6", "Describe, with an example, the difference between congruence and "
            "similarity.", "Congruent shapes are identical in size and shape, as two copies "
            "of the same triangle; similar shapes have the same shape but may differ in size, "
            "as two photographs of different sizes.", "Compare the definitions.", "R"),
           ("9.3.7", "Explain why the area scale factor is the square of the length scale "
            "factor.",
            "Because an area is a product of two lengths, and each length is multiplied by "
            "the factor.", "Consider a rectangle.", "R"),
           ("9.3.8", "Write the reasoning that shows reflecting in both axes is a half turn.",
            "Reflecting in the y-axis maps (x, y) to (−x, y) and then in the x-axis to "
            "(−x, −y), which is a rotation of 180° about the origin.",
            "Track one point.", "R"),
           ("9.3.9", "Set out the argument that RHS is a congruence test for right-angled "
            "triangles.", "The hypotenuse and one leg fix the third leg by Pythagoras, so the "
            "test reduces to SSS.", "Apply Pythagoras.", "R"),
           ("9.3.10", "Explain what a tolerance is and why it is an interval.",
            "The permitted difference between a measurement and its specification, stated as "
            "a band either side of the nominal value.", "Give an example.", "R"),
           ("9.3.11", "Describe the relationship between a scale drawing and the object it "
            "represents.", "They are similar, with the scale factor connecting every "
            "corresponding length, its square connecting areas and its cube connecting "
            "volumes.", "State the three connections.", "R"),
           ("9.3.12", "Explain, with an example, when a model is a misleading representation "
            "of an object.",
            "Any answer is acceptable if it identifies a property a model cannot show, such "
            "as weight, strength, cost or the feel of a material.", "Give a specific "
            "example.", "R")],
        D=[("9.4.1", "A map has a scale of 1 : 50000. A field measures 6 cm by 4 cm on the "
            "map. Find its real area in hectares.",
            "600 hectares, because 6 × 4 × 50000² cm² = 6 × 10¹⁰ cm².",
            "Scale both lengths, then the area.", "A"),
           ("9.4.2", "Two similar bottles have heights 12 cm and 18 cm. The smaller holds "
            "500 ml. Find the capacity of the larger.",
            "1687.5 ml, because the volume factor is (18/12)³ = 3.375.",
            "Cube the length ratio.", "A"),
           ("9.4.3", "A model car is 20 cm long at a scale of 1 : 20. Find the real length "
            "and the ratio of the real and model surface areas.",
            "4 m long; the area ratio is 400 : 1.", "Scale the length, then square.", "A"),
           ("9.4.4", "A photograph is enlarged from 10 cm by 15 cm to 25 cm by 37.5 cm. Find "
            "the scale factor and the ratio of the areas.",
            "Scale factor 2.5; the area ratio is 6.25 : 1.", "Scale the length, then square.",
            "A"),
           ("9.4.5", "A part is specified as 25.0 mm with a tolerance of ±0.1 mm. Investigate "
            "whether measurements of 24.95 and 25.12 mm are acceptable.",
            "24.95 is acceptable; 25.12 is not.", "Compare with the interval.", "A"),
           ("9.4.6", "A tree casts a shadow 15 m long while a 1.6 m post casts a shadow 2 m "
            "long. Find the height of the tree and state one assumption.",
            "12 m, assuming level ground and parallel rays.",
            "Use similar triangles.", "A"),
           ("9.4.7", "Two similar solids have volumes in the ratio 1 : 64. Find the ratio of "
            "their surface areas and justify.",
            "1 : 16, because the length ratio is the cube root of 64, which is 4, and the "
            "area ratio is 4².", "Take the cube root, then square.", "R"),
           ("9.4.8", "A scale model of a room is built at 1 : 25. The model has a floor area "
            "of 0.32 m². Find the real floor area and comment on the model's limits.",
            "200 m²; the model says nothing about the height of the ceiling or the "
            "materials.", "Square the scale factor.", "A"),
           ("9.4.9", "A photograph shows a 1.8 m door and a wall 6.5 times as tall. "
            "Investigate the wall's height and comment on the reliability.",
            "About 11.7 m, subject to the distortion of the lens and the level of the camera.",
            "Multiply the reference height by the ratio.", "R"),
           ("9.4.10", "A company makes a cup in two sizes with heights in the ratio 1 : 1.5. "
            "Investate whether the larger uses 2.25 times the material and justify.",
            "Yes for the surface area, but only 3.375 times the capacity, because area scales "
            "as k² and volume as k³.", "Square and cube the ratio.", "C"),
           ("9.4.11", "A map has a scale of 1 : 200000. A lake measures 3.5 cm by 2 cm on the "
            "map. Find its real area in square kilometres and state one limitation of the "
            "method.", "140 km², but the outline on a map is a simplification of the real "
            "shore.", "Scale both lengths, then the area.", "A"),
           ("9.4.12", "Explain, with an example, when using a scale factor directly on an "
            "area gives a wrong answer.",
            "Any answer is acceptable if it shows that areas need the square and volumes the "
            "cube, as with a model wing area at 1 : 50.", "Give a specific counterexample.",
            "R")],
    ),
    assessment=[
        dict(title="A1 · The model bridge",
             text="A scale model of a footbridge is built at 1 : 75. The model is 48 cm long "
                  "and its deck area is 0.031 m². Find the real length and the real deck area, "
                  "estimate the real volume of concrete if the model used 0.0004 m³, and "
                  "comment on two properties of the real bridge that the model cannot "
                  "establish.",
             note="Criteria A and C · use the scale factor, its square and its cube, and "
                  "justify the limits of the model."),
        dict(title="A2 · The two triangles",
             text="Two triangles are described. Triangle P has sides 7 cm and 9 cm with an "
                  "included angle of 50°. Triangle Q has sides 7 cm and 9 cm with an angle of "
                  "50° opposite the 7 cm side. Decide, with a full justification, whether each "
                  "pair of triangles with these descriptions must be congruent, and explain "
                  "the difference between the two descriptions.",
             note="Criteria B and D · apply the congruence tests and justify why one "
                  "description decides the shape and the other does not."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of space, equivalence and "
        "representation appear in your work?",
        "How is the global context of scientific and technical innovation, and its exploration of "
        "scale models, design and measurement at a distance, visible in the investigations and "
        "examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a scale model for a decision about a real object, and what "
        "would you still like to ask?",
    ],
    review=dict(
        ideas=["A translation, a reflection and a rotation preserve length and angle.",
               "An enlargement by k scales lengths by k, areas by k² and volumes by k³.",
               "SSS, SAS, ASA and RHS are tests for congruent triangles.",
               "ASS and AAA are not congruence tests.",
               "Similar shapes have equal angles and sides in proportion.",
               "The scale factor connects a model to the object it represents.",
               "A tolerance defines an interval of acceptable measurements.",
               "An inaccessible length can be estimated from similar triangles."],
        vocab=["translation", "vector", "reflection", "rotation", "enlargement",
               "scale factor", "congruent", "similar", "tolerance", "invariant",
               "orientation", "ambiguous case"],
        mixed=[("9.R1", "Reflect (3, −5) in the y-axis."),
               ("9.R2", "Enlarge (2, −4) by factor 3 about the origin."),
               ("9.R3", "Find the ratio of the areas of similar shapes with length ratio "
                        "4 : 7."),
               ("9.R4", "A map has scale 1 : 100000. Find the real length of 5 cm."),
               ("9.R5", "Two triangles have sides 6, 8 and 10. Are they congruent to a "
                        "3, 4, 5 triangle?"),
               ("9.R6", "Explain why a scale factor of 2 quadruples the area.")],
    ),
    projects=dict(
        service=[("Community need", "Scale models and maps are used for decisions without "
                                    "stating what they cannot show."),
                 ("Mathematical connection", "Transformations, similarity and scale factors."),
                 ("Proposed action", "Build or analyse one scale model and publish what it "
                                     "establishes and what it does not."),
                 ("Expected impact", "A reader knows which questions a model can answer."),
                 ("Student reflection", "Record the model, the scale factor and the limits.")],
        community=[("Project idea", "A scale model of one community space."),
                   ("Need", "Plans for a garden, a market or a classroom are discussed "
                            "without a shared picture."),
                   ("Research question", "What does a scale model establish about the space, "
                                         "and what does it leave out?"),
                   ("Mathematics", "Transformations, similarity and area scaling."),
                   ("Action or outcome", "A scale model or drawing with a stated scale and a "
                                         "list of its limits."),
                   ("Beneficiaries", "Everyone who will use the space."),
                   ("Evidence", "The model, the scale and the list of limits.")],
        personal=[("Personal interest", "A model, a map or a design you enjoy."),
                  ("Learning goal", "To build or analyse a scale model and state its limits."),
                  ("Product or outcome", "A scale model with a stated factor and a "
                                         "justification."),
                  ("Mathematics", "Transformations and similarity."),
                  ("Process", "Choose a scale, build or analyse the model, and test one "
                              "prediction."),
                  ("Evidence", "The model, the scale and the test.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=10, title="Pythagoras, Trigonometry and Measurement",
    key="Relationships", related=["Space", "Measurement", "Equivalence"],
    context="Scientific and technical innovation",
    exploration="Surveying, navigation and safe design",
    inquiry=("The sides and angles of a right-angled triangle are related by Pythagoras' "
             "theorem and by the trigonometric ratios, so knowing two of them decides the "
             "rest; these relations turn an inaccessible length or angle into a measurement, "
             "and the equivalence between the theorem and the ratios is what makes surveying "
             "possible."),
    atl=("Thinking",
         "Students select the appropriate relation for a given right-angled triangle, "
         "justify the choice, and check the answer by a second route."),
    standfirst="Pythagoras connects the three sides. The sine, cosine and tangent connect the "
               "angles to the sides. Together they decide every right-angled triangle from "
               "two pieces of information.",
    engage="A ladder leans against a wall. Its foot is 1.5 m from the wall and its top is "
           "3.6 m up. How long is the ladder, and what angle does it make with the ground?",
    questions=[("Factual", "What does Pythagoras' theorem state, and what are the three "
                           "trigonometric ratios?"),
               ("Conceptual", "Why is the choice of ratio decided by which sides are known, "
                              "and how do the theorem and the ratios relate to each other?"),
               ("Debatable", "When a measurement is used to decide whether a structure is "
                             "safe, is a calculation enough, or must the measurement itself "
                             "be justified?")],
    application_lede="Each task involves a right-angled triangle. Draw it, label the sides "
                     "relative to the angle you are using, and state which relation you apply.",
    projects_lede="Surveying and navigation turn inaccessible distances into measurements. "
                  "Model one and say how accurate your answer is.",
    sections=[
        dict(id="10.1", title="Pythagoras' theorem and proof",
             inquiry_q="How does the theorem connect the three sides of a right-angled "
                       "triangle?",
             teach=[
                 "In a right-angled triangle the square on the hypotenuse equals the sum of the squares on the other two sides: a² + b² = c², where c is the hypotenuse.",
                 "The hypotenuse is the side opposite the right angle and is always the longest side. The other two sides are the legs.",
                 "A right-angled triangle is the simplest figure in space that has a fixed shape once two measurements are known, which is why it is used to measure distances that cannot be reached.",
                 "The theorem is used forwards to find a missing side and backwards to test whether a triangle is right-angled: if a² + b² = c² then the angle opposite c is a right angle.",
                 "The converse is a test, and it is the reason a builder can check a corner is square by measuring 3, 4 and 5 units along the two edges and the diagonal.",
             ], examples=[
                 dict(q="A right-angled triangle has legs 9 cm and 12 cm. Find the "
                        "hypotenuse.",
                      vis=F("pythagoras", 9, 12, "legs 9 and 12"),
                      reasoning="Apply a² + b² = c² and take the square root.",
                      steps=["Let c be the hypotenuse. Then c² = 9² + 12².",
                             "So c² = 81 + 144 = 225.",
                             "Hence c = √225 = 15 cm.",
                             "The hypotenuse is longer than either leg, as expected.",
                             "This is the 3-4-5 triangle scaled by 3, which is why the answer "
                             "is a whole number."],
                      ans="15 cm",
                      interp="The theorem converts two known sides into the third, and the "
                             "answer is checked by the fact that it exceeds both legs."),
                 dict(q="A ladder reaches 3.6 m up a wall with its foot 1.5 m from the wall. "
                        "Find the length of the ladder.",
                      vis=F("triangle", [(0, 0), (1.5, 0), (0, 3.6)], ["1.5 m", "", "3.6 m"],
                            right=[(0, 0, "")], title="the ladder, the wall and the ground"),
                      reasoning="The ladder is the hypotenuse of a right-angled triangle whose "
                               "legs are known.",
                      steps=["The ladder is the hypotenuse, and the legs are 1.5 m and 3.6 m.",
                             "So L² = 1.5² + 3.6² = 2.25 + 12.96 = 15.21.",
                             "Hence L = √15.21 = 3.9 m.",
                             "The ladder is longer than the height it reaches, as it must be.",
                             "The angle with the ground is about 67.4°, found in section 10.2."],
                      ans="the ladder is 3.9 m long",
                      interp="A length that cannot be measured directly is found from two "
                             "measurements that can, which is the practical value of the "
                             "theorem."),
             ], inv=dict(
                 task="Measure the diagonal and the two sides of five rectangles, including a "
                      "sheet of paper, a book, a door and a screen. Check Pythagoras' theorem "
                      "on each, and then use it to predict the diagonal of a rectangle you "
                      "cannot measure.",
                 table=[["object", "sides", "diagonal", "check"],
                        ["sheet of paper", "21.0, 29.7", "36.3", "21² + 29.7² ≈ 36.3²"],
                        ["book", "15.0, 21.0", "25.8", "15² + 21² ≈ 25.8²"],
                        ["door", "0.8, 2.0", "2.15", "0.8² + 2² ≈ 2.15²"],
                        ["screen", "0.45, 0.80", "0.92", "0.45² + 0.8² ≈ 0.92²"]],
                 notice=["The theorem held on every rectangle, within the precision of the "
                         "ruler.",
                         "The predicted diagonal of the unmeasured rectangle was within a "
                         "centimetre.",
                         "The diagonal was always longer than either side and shorter than "
                         "their sum.",
                         "The small disagreements came from rounding the measurements, not "
                         "from the theorem."],
                 obs="The square on the diagonal equals the sum of the squares on the sides, "
                     "and the agreement is as close as the measurements allow.",
                 concl="Pythagoras' theorem connects the three sides of a right-angled "
                       "triangle, and it works in both directions: it finds a missing side and "
                       "it tests whether an angle is right.")),
        dict(id="10.2", title="Pythagoras in three dimensions",
             inquiry_q="How is Pythagoras' theorem used inside a three-dimensional solid?",
             teach=[
                 "Pythagoras' theorem applies to any right-angled triangle, including one drawn inside a solid, so a three-dimensional problem is solved by finding the right triangle first.",
                 "The diagonal of a rectangle of sides a and b is √(a² + b²), and the space diagonal of a cuboid of sides a, b and c is √(a² + b² + c²), which is Pythagoras applied twice.",
                 "The longest rod that fits in a box is the space diagonal, so the theorem decides what can be carried through a doorway or stored in a container.",
                 "A two-dimensional cross-section is a representation of a three-dimensional problem, and choosing the cross-section that contains the right angle is the whole skill.",
             ], examples=[
                 dict(q="A cuboid measures 6 cm by 8 cm by 24 cm. Find the length of its space "
                        "diagonal.",
                      vis=F("prism", "cuboid", 6, 8, 24,
                            "a cuboid of 6 cm, 8 cm and 24 cm"),
                      reasoning="Apply Pythagoras twice: first to a face, then to the "
                               "cross-section.",
                      steps=["The face diagonal is √(6² + 8²) = √100 = 10 cm.",
                             "This diagonal and the third side form a right-angled triangle "
                             "whose hypotenuse is the space diagonal.",
                             "So the space diagonal is √(10² + 24²) = √676 = 26 cm.",
                             "Equivalently √(6² + 8² + 24²) = √676 = 26 cm.",
                             "The two routes agree, which is the check."],
                      ans="26 cm",
                      interp="Pythagoras used twice turns a three-dimensional measurement into "
                             "two two-dimensional ones."),
                 dict(q="A cone has height 12 cm and base radius 5 cm. Find its slant height.",
                      vis=F("cone", 5, 12, "radius 5 cm and height 12 cm"),
                      reasoning="The vertical cross-section through the axis is an isosceles "
                               "triangle, and half of it is right-angled.",
                      steps=["The cross-section through the axis contains the height, the "
                             "radius and the slant height.",
                             "The height is perpendicular to the radius at the centre of the "
                             "base.",
                             "So the slant height is the hypotenuse: √(5² + 12²) = √169.",
                             "Hence the slant height is 13 cm.",
                             "The slant height is what is needed for the curved surface area."],
                      ans="13 cm",
                      interp="A solid is measured by choosing the cross-section that contains "
                             "the right angle, and the cone's cross-section is a right "
                             "triangle."),
             ], inv=dict(
                 task="Take four solids: a cuboid, a cone, a cylinder and a pyramid. For each, "
                      "draw or describe the cross-section that contains a right angle, and use "
                      "Pythagoras to find the internal length named: the space diagonal of the "
                      "cuboid, the slant height of the cone and the pyramid, and the longest "
                      "rod that fits inside the cylinder lying flat.",
                 table=[["solid", "cross-section", "Pythagoras on", "result"],
                        ["cuboid 3, 4, 12", "face then body", "√(3²+4²+12²)", "13"],
                        ["cone r = 6, h = 8", "through the axis", "√(6² + 8²)", "10"],
                        ["cylinder r = 5, h = 12", "through the axis", "√(5² + 12²)", "13"],
                        ["pyramid square base 6, height 4", "through apex and mid-edge",
                         "√(3² + 4²)", "5"]],
                 notice=["Every solid gave a right-angled triangle in some cross-section.",
                         "The cuboid needed Pythagoras twice, the others once.",
                         "The slant heights were all whole numbers because the triangles were "
                         "Pythagorean triples.",
                         "The cylinder's longest flat rod was its space diagonal, not its "
                         "height."],
                 obs="A three-dimensional length is found by choosing the cross-section that "
                     "contains a right angle, and Pythagoras then applies unchanged.",
                 concl="Pythagoras' theorem is not limited to a flat page: it applies to every "
                       "right-angled triangle, including those hidden inside a solid.")),
        dict(id="10.3", title="Trigonometric ratios",
             inquiry_q="How do the sine, cosine and tangent connect an angle to the sides?",
             teach=[
                 "In a right-angled triangle, sin θ = opposite/hypotenuse, cos θ = adjacent/hypotenuse and tan θ = opposite/adjacent, where the sides are named relative to the angle θ.",
                 "The ratios depend only on the angle, not on the size of the triangle, which is why similar triangles give the same values and a table of ratios serves every triangle.",
                 "Choosing a ratio is decided by which sides are known and which is wanted. If the hypotenuse is involved, use sine or cosine; if not, use tangent.",
                 "The inverse ratios recover the angle: if sin θ = 0.6 then θ = 37°, and the two questions — finding a side and finding an angle — use the same three relations.",
             ], examples=[
                 dict(q="A right-angled triangle has hypotenuse 10 cm and an angle of 35°. "
                        "Find the side opposite and the side adjacent to the angle.",
                      vis=F("triangle", [(0, 0), (8.2, 0), (8.2, 5.7)], ["10 cm", "", ""],
                            right=[(8.2, 0, "")], angles=[(0, 0, "35°")],
                            title="opposite, adjacent and hypotenuse"),
                      reasoning="Use sine for the opposite side and cosine for the adjacent "
                               "side.",
                      steps=["sin 35° = opposite/10, so the opposite side is 10 × sin 35°.",
                             "sin 35° ≈ 0.5736, so the opposite side is about 5.74 cm.",
                             "cos 35° = adjacent/10, so the adjacent side is 10 × cos 35°.",
                             "cos 35° ≈ 0.8192, so the adjacent side is about 8.19 cm.",
                             "Check: 5.74² + 8.19² ≈ 100, as Pythagoras requires."],
                      ans="opposite 5.74 cm, adjacent 8.19 cm",
                      interp="One angle and the hypotenuse fix the whole triangle, and the two "
                             "ratios give the two legs."),
                 dict(q="A ramp rises 1.2 m over a horizontal distance of 6 m. Find the angle "
                        "the ramp makes with the ground.",
                      vis=F("elevation", 11, 6, "a ramp of gradient 1.2 in 6"),
                      reasoning="The tangent relates the rise to the run, so use the inverse "
                               "tangent.",
                      steps=["The rise is opposite the angle and the run is adjacent.",
                             "So tan θ = 1.2/6 = 0.2.",
                             "Hence θ = arctan(0.2) ≈ 11.3°.",
                             "A gradient of 1 in 5 is a gentle slope, as the angle shows.",
                             "Building regulations often limit ramps to about 1 in 12, which "
                             "is about 4.8°."],
                      ans="about 11.3°",
                      interp="The tangent of the angle of elevation is the gradient, which "
                             "connects trigonometry to the linear models of chapter 4."),
             ], inv=dict(
                 task="Measure five right-angled triangles of your own: a set square, a "
                      "leaning ladder, a roof pitch, a ramp and one of your own. For each, "
                      "compute the three ratios for one acute angle, then use them to find "
                      "the other sides and check with Pythagoras.",
                 table=[["triangle", "angle", "sin", "cos", "tan"],
                        ["set square", "30°", "0.5", "0.866", "0.577"],
                        ["ladder", "67.4°", "0.923", "0.385", "2.4"],
                        ["roof pitch", "22.6°", "0.385", "0.923", "0.417"],
                        ["ramp", "11.3°", "0.196", "0.981", "0.2"]],
                 notice=["The three ratios for the same angle agreed across triangles of "
                         "different sizes.",
                         "sin θ and cos θ swapped when the two acute angles were exchanged.",
                         "The tangent was the ratio of the other two, in every case.",
                         "Pythagoras was satisfied by every triangle, within measurement "
                         "error."],
                 obs="The three ratios depend on the angle alone, so a table of values serves "
                     "every right-angled triangle of the same shape.",
                 concl="The sine, cosine and tangent of an angle are the three ratios of the "
                       "sides of a right-angled triangle, and any one of them connects a known "
                       "side to an unknown one.")),
        dict(id="10.4", title="Solving right-angled triangles",
             inquiry_q="How is a right-angled triangle solved when two pieces of information "
                       "are given?",
             teach=[
                 "Solving a right-angled triangle means finding every unknown side and angle from the information given, and two pieces of information are enough because the right angle is already known.",
                 "The choice of ratio depends on what is given and what is wanted: the tangent uses the two legs, the sine uses the opposite and the hypotenuse, and the cosine uses the adjacent and the hypotenuse.",
                 "Finding a side uses multiplication by a ratio, and finding an angle uses the inverse ratio. Writing the equation before substituting is what stops the two being confused.",
                 "The two acute angles of a right-angled triangle add to 90°, so one angle can be found from the other, and this is a useful check on a calculation.",
             ], examples=[
                 dict(q="A right-angled triangle has legs 9 cm and 12 cm. Find the hypotenuse "
                        "and the two acute angles.",
                      vis=F("triangle", [(0, 0), (12, 0), (12, 9)], ["9 cm", "12 cm", ""],
                            right=[(0, 0, "")],
                            title="a 9-12-? triangle"),
                      reasoning="Pythagoras gives the hypotenuse, then a ratio gives an angle.",
                      steps=["The hypotenuse is √(9² + 12²) = √225 = 15 cm.",
                             "For the angle opposite the 9 cm side, tan A = 9/12.",
                             "So A = tan⁻¹(0.75) ≈ 36.9°.",
                             "The other angle is 90° − 36.9° = 53.1°.",
                             "Check: 36.9 + 53.1 = 90, as the two acute angles must."],
                      ans="hypotenuse 15 cm; angles 36.9° and 53.1°",
                      interp="Pythagoras finds the sides and the ratios find the angles, and "
                             "the two acute angles check each other."),
                 dict(q="A ladder 8 m long leans against a wall with its foot 2 m from the "
                        "wall. Find the angle the ladder makes with the ground.",
                      vis=F("triangle", [(0, 0), (2, 0), (2, 7.75)], ["8 m", "2 m", ""],
                            right=[(2, 0, "")],
                            title="the ladder, wall and ground"),
                      reasoning="The hypotenuse and the adjacent side are known, so use the "
                               "cosine.",
                      steps=["The hypotenuse is 8 m and the side adjacent to the angle is "
                             "2 m.",
                             "So cos θ = 2/8 = 0.25.",
                             "Hence θ = cos⁻¹(0.25) ≈ 75.5°.",
                             "The height reached is √(8² − 2²) = √60 ≈ 7.75 m.",
                             "A steeper angle would give a greater height, so the answer is "
                             "sensible."],
                      ans="about 75.5° to the ground",
                      interp="Choosing the ratio that uses the two known quantities is the "
                             "first step, and it is decided by what is given, not by what is "
                             "wanted."),
             ], inv=dict(
                 task="Solve six right-angled triangles of your own: two given two legs, two "
                      "given a leg and the hypotenuse, and two given an angle and a side. For "
                      "each, state which ratio you used and why, find every unknown, and "
                      "check by a second route such as Pythagoras or the sum of the angles.",
                 table=[["given", "ratio used", "found", "check"],
                        ["legs 5 and 12", "Pythagoras then tan", "hypotenuse 13, angles 22.6°, 67.4°", "5² + 12² = 13²"],
                        ["leg 7, hypotenuse 25", "sin then Pythagoras", "angles 16.3°, 73.7°", "7² + 24² = 25²"],
                        ["angle 40°, hypotenuse 10", "sin and cos", "legs 6.43 and 7.66", "6.43² + 7.66² ≈ 100"],
                        ["angle 55°, leg 6", "tan and cos", "hypotenuse 10.49", "6/10.49 ≈ cos 55°"]],
                 notice=["The ratio used was always the one containing the two known "
                         "quantities.",
                         "Finding a side multiplied; finding an angle used an inverse ratio.",
                         "Pythagoras checked every side and the angle sum checked every angle.",
                         "The two acute angles always added to 90°."],
                 obs="A right-angled triangle is solved by choosing the ratio that uses the "
                     "two known quantities, then checking by a second route.",
                 concl="Two pieces of information fix a right-angled triangle, and the choice "
                       "of ratio depends on which two they are.")),
        dict(id="10.5", title="Angles of elevation, depression and bearings",
             inquiry_q="How is an inaccessible height found from an angle and a distance?",
             teach=[
                 "The angle of elevation is the angle above the horizontal at which an object is seen, and the angle of depression is the angle below the horizontal from which it is seen.",
                 "The two angles are equal when the lines of sight are parallel, which is why a person on a cliff and a person on the ground see each other at the same angle.",
                 "A height is found from the tangent of the angle of elevation and the horizontal distance, and the observer's own height must be added if the angle was measured at eye level.",
                 "A clinometer or a phone app measures the angle, and the distance along the ground is measured separately. The two measurements combine in the tangent ratio.",
                 "A bearing is the angle measured clockwise from north, written with three figures, and it is the convention that makes a direction unambiguous. Without it, two people can mean different things by the same words.",
                 "A back bearing differs from the forward bearing by 180°, because reversing a direction turns it through a half turn, and a journey of two legs is combined by Pythagoras or trigonometry on the triangle the legs form.",
                 "A measured angle carries an error interval, and a height calculated from it carries one too. A small error in an angle can produce a large error in a height, so an answer near a safety limit needs a margin.",
             ], examples=[
                 dict(q="From 40 m away, the angle of elevation to the top of a tree is 28°. "
                        "The observer's eye is 1.6 m above the ground. Find the height of the "
                        "tree.",
                      vis=F("elevation", 28, 40, "the tree from 40 m away"),
                      reasoning="Use the tangent of the angle of elevation, then add the "
                               "observer's height.",
                      steps=["tan 28° = height above eye/40.",
                             "So the height above eye level is 40 × tan 28°.",
                             "tan 28° ≈ 0.5317, so the height above eye level is about 21.3 m.",
                             "Adding the observer's height gives 21.3 + 1.6 = 22.9 m.",
                             "The tree is about 22.9 m tall."],
                      ans="about 22.9 m",
                      interp="The measurement gives the height above the observer's eye, and "
                             "forgetting to add the eye level is the commonest error in this "
                             "calculation."),
                 dict(q="From the top of a 30 m cliff, the angle of depression to a boat is "
                        "12°. Find the distance of the boat from the base of the cliff.",
                      vis=F("elevation", 12, 30, "the cliff and the boat"),
                      reasoning="The angle of depression equals the angle of elevation from "
                               "the boat, so the same triangle is used.",
                      steps=["The angle of elevation from the boat is also 12°.",
                             "tan 12° = 30/d, where d is the distance from the base.",
                             "So d = 30/tan 12°.",
                             "tan 12° ≈ 0.2126, so d ≈ 141 m.",
                             "The boat is about 141 m from the base of the cliff."],
                      ans="about 141 m",
                      interp="The equality of the two angles lets one measurement serve both "
                             "observers, which is why the method is used in navigation."),

                 dict(q="A ship sails 20 km on a bearing of 030° and then 15 km on a bearing "
                        "of 120°. Find its distance and bearing from the start.",
                      vis=F("grid", [(0, 0), (17.3, 10), (-7.5, 13)],
                            ["start", "after 20 km", "final"], -12, 22, -4, 18,
                            [(0, 0), (17.3, 10), (-7.5, 13)],
                            "two legs and the resultant"),
                      reasoning="Draw the two displacements, find the resultant by components, "
                               "then convert back to distance and bearing.",
                      steps=["The first leg has components 20 sin 30° = 10 km east and 20 cos "
                             "30° = 17.3 km north.",
                             "The second leg has components 15 sin 120° = 13 km east and 15 "
                             "cos 120° = −7.5 km north.",
                             "Adding gives 23 km east and 9.8 km north.",
                             "The distance is √(23² + 9.8²) ≈ 25 km.",
                             "The bearing is arctan(23/9.8) ≈ 067°."],
                      ans="about 25 km on a bearing of 067°",
                      interp="Two legs combine into one resultant, and the components make the "
                             "combination a matter of addition."),
                 dict(q="A walker goes 8 km on a bearing of 060°. Find the bearing of the "
                        "return journey.",
                      vis=F("grid", [(0, 0), (6.9, 4)], ["start", "turn"], -2, 10, -2, 8,
                            [(0, 0), (6.9, 4)],
                            "the return bearing is 240°"),
                      reasoning="A back bearing differs by 180°.",
                      steps=["The forward bearing is 060°.",
                             "Adding 180° gives 240°.",
                             "So the return bearing is 240°.",
                             "This is the same line travelled in the opposite direction.",
                             "If the sum exceeds 360°, subtract 360° instead."],
                      ans="240°",
                      interp="A back bearing is found by adding or subtracting 180°, and the "
                             "three-figure form keeps 240° distinct from 024°.")
             ], inv=dict(
                 task="Measure the height of three objects you cannot reach: a tree, a "
                      "building and a flagpole. For each, measure the horizontal distance and "
                      "the angle of elevation with a clinometer or a phone, compute the "
                      "height, and add the observer's eye level.",
                 table=[["object", "distance", "angle", "height"],
                        ["tree", "18 m", "32°", "13.1 m"],
                        ["building", "25 m", "41°", "23.3 m"],
                        ["flagpole", "12 m", "55°", "18.7 m"]],
                 notice=["Every height needed the observer's eye level added.",
                         "A small error in the angle produced a large error in the height, "
                         "because the tangent is steep.",
                         "The ground was not perfectly level, which added a further error.",
                         "The method worked because the distance along the ground could be "
                         "measured."],
                 obs="A height is found from the tangent of the angle of elevation and the "
                     "horizontal distance, and the accuracy of the answer is limited by the "
                     "accuracy of the angle.",
                 concl="An inaccessible height is measured by combining an angle of elevation "
                       "with a measured horizontal distance, and the observer's own height "
                       "must be included.")),
        dict(id="10.6", title="Investigation: measuring the inaccessible",
             inquiry_q="How is a real site measured and drawn, and what does the drawing "
                       "decide?",
             teach=[
                 "A site is surveyed by measuring distances and bearings between points, and the points are then plotted by resolving each measurement into components.",
                 "A survey is a representation that fixes the shape and the size of a site, and it is the basis of every decision made from a plan.",
                 "The survey's accuracy is limited by the instruments, and the errors accumulate along a chain of measurements, which is why a survey closes back on its starting point.",
                 "A drawing made from a survey is a model, and a decision taken from it inherits the survey's errors as well as its assumptions.",
             ], examples=[
                 dict(q="A triangular plot has sides 40 m, 55 m and 70 m. Show that it is not "
                        "right-angled, and find its largest angle.",
                      vis=F("triangle", [(0, 0), (70, 0), (18.6, 35.7)], ["40 m", "70 m",
                                                                          "55 m"],
                            angles=[(0, 0, "118°")], title="a scalene triangle"),
                      reasoning="Test Pythagoras first, then use the cosine rule for the "
                               "largest angle.",
                      steps=["The longest side is 70 m, and 40² + 55² = 1600 + 3025 = 4625.",
                             "But 70² = 4900, which is not 4625, so the triangle is not "
                             "right-angled.",
                             "The largest angle is opposite the 70 m side.",
                             "cos C = (40² + 55² − 70²)/(2 × 40 × 55) = (4625 − 4900)/4400 = "
                             "−0.0625.",
                             "So C ≈ 93.6°, an obtuse angle."],
                      ans="not right-angled; the largest angle is about 93.6°",
                      interp="The converse of Pythagoras rules out a right angle, and the "
                             "cosine rule then finds the actual angle."),
                 dict(q="A surveyor measures three sides of a plot as 30 m, 40 m and 50 m and "
                        "closes the traverse. Find the area of the plot.",
                      vis=F("grid", [], [], 0, 55, 0, 45, [(0, 0), (50, 0), (0, 40)],
                            "a right-angled plot"),
                      reasoning="The sides satisfy Pythagoras, so the plot is right-angled and "
                               "the area is half the product of the legs.",
                      steps=["30² + 40² = 900 + 1600 = 2500 = 50².",
                             "So the plot is right-angled with legs 30 m and 40 m.",
                             "The area is ½ × 30 × 40 = 600 m².",
                             "The hypotenuse of 50 m is the diagonal of the plot.",
                             "The right angle means no angle measurement was needed."],
                      ans="600 m²",
                      interp="A side measurement that satisfies Pythagoras also establishes a "
                             "right angle, which is why a builder's 3-4-5 check works."),
             ], inv=dict(
                 task="Survey a small area: a classroom, a garden or a playground. Measure "
                      "four distances and four bearings, plot the points, check that the "
                      "traverse closes, and draw the plan to a stated scale. Then find the "
                      "area and comment on the largest source of error.",
                 table=[["point", "distance", "bearing", "east", "north"],
                        ["A to B", "6.0 m", "090°", "6.00", "0.00"],
                        ["B to C", "4.0 m", "180°", "0.00", "−4.00"],
                        ["C to D", "6.0 m", "270°", "−6.00", "0.00"],
                        ["D to A", "4.0 m", "000°", "0.00", "4.00"],
                        ["closure", "—", "—", "0.00", "0.00"]],
                 notice=["The traverse closed exactly, because the measurements were chosen to "
                         "do so.",
                         "The plot was a rectangle, which the bearings showed directly.",
                         "The area was 24 m², found from the two side lengths.",
                         "In a real survey the closure would not be exact, and the "
                         "discrepancy would estimate the error."],
                 obs="A survey is a set of distances and bearings whose components must close "
                     "back on the start, and the closure error estimates the accuracy of the "
                     "whole survey.",
                 concl="A site is measured by distances and bearings, plotted by components, "
                       "and checked by closure, and the plan drawn from it carries the "
                       "survey's accuracy.")),
    ],
    practice=dict(
        A=[("10.1.1", "Find the hypotenuse of a right-angled triangle with legs 6 cm and "
            "8 cm.", "10 cm", "√(36 + 64) = √100.", "F"),
           ("10.1.2", "Find the hypotenuse when the legs are 9 cm and 12 cm.", "15 cm",
            "√(81 + 144) = √225.", "F"),
           ("10.1.3", "A right-angled triangle has hypotenuse 13 cm and one leg 5 cm. Find "
            "the other leg.", "12 cm", "√(169 − 25) = √144.", "F"),
           ("10.1.4", "Find sin 30°.", "0.5", "The ratio of the opposite side to the "
            "hypotenuse in a 30-60-90 triangle.", "F"),
           ("10.1.5", "Find cos 60°.", "0.5", "The ratio of the adjacent side to the "
            "hypotenuse.", "F"),
           ("10.1.6", "Find tan 45°.", "1", "The opposite and adjacent sides are equal.", "F"),
           ("10.1.7", "A right-angled triangle has hypotenuse 10 and an angle of 30°. Find "
            "the opposite side.", "5", "10 × sin 30°.", "F"),
           ("10.1.8", "A right-angled triangle has an adjacent side of 8 and an angle of 40°. "
            "Find the opposite side.", "6.71", "8 × tan 40°.", "F"),
           ("10.1.9", "Find the angle whose sine is 0.5.", "30°",
            "The inverse sine of 0.5.", "F"),
           ("10.1.10", "A ladder 5 m long leans with its foot 3 m from a wall. Find the "
            "height it reaches.", "4 m", "√(25 − 9).", "F"),
           ("10.1.11", "Find the back bearing of 137°.", "317°",
            "Add 180° to the forward bearing.", "F"),
           ("10.1.12", "A triangle has sides 5, 12 and 13. Show that it is right-angled.",
            "25 + 144 = 169, so the converse of Pythagoras applies.",
            "Check a² + b² = c².", "F")],
        B=[("10.2.1", "The diagonals of a rectangle are 13 cm and the sides are in the ratio "
            "5 : 12. Find the sides and justify.",
            "5 cm and 12 cm, because 25 + 144 = 169.", "Scale the 5-12-13 triangle.", "R"),
           ("10.2.2", "Investigate the pattern in the values of sin θ and cos θ for θ = 0°, "
            "30°, 45°, 60°, 90°.",
            "sin rises 0, 0.5, 0.707, 0.866, 1 while cos falls 1, 0.866, 0.707, 0.5, 0.",
            "Compute the ratios in special triangles.", "R"),
           ("10.2.3", "Conjecture a rule connecting sin θ and cos θ and justify it.",
            "sin² θ + cos² θ = 1, by dividing Pythagoras by the hypotenuse squared.",
            "Use Pythagoras on the ratios.", "R"),
           ("10.2.4", "Investigate the pattern in the height reached by a 5 m ladder as its "
            "foot moves from 0 to 5 m from a wall.",
            "The height falls from 5 m to 0 m, following √(25 − x²).",
            "Apply Pythagoras for each position.", "R"),
           ("10.2.5", "Build a table of the gradients of lines making angles of 0° to 90° "
            "with the horizontal and describe the pattern.",
            "The gradients are the tangents, rising from 0 to infinity.",
            "Compute tan θ for each angle.", "R"),
           ("10.2.6", "Conjecture a rule for the angle of elevation that doubles the height "
            "seen at a fixed distance.",
            "There is no such angle, because the height is proportional to tan θ, not to θ.",
            "Compare tan θ for several angles.", "R"),
           ("10.2.7", "Investigate the pattern in the areas of right-angled triangles with a "
            "fixed hypotenuse of 10 cm.",
            "The area is greatest for the isosceles triangle, at 25 cm².",
            "Write the area as a quadratic in one leg.", "C"),
           ("10.2.8", "A ship sails 30 km east and then 40 km north. Investigate the direct "
            "distance and bearing home.",
            "50 km on a bearing of 233°.", "Use Pythagoras and the tangent.", "R"),
           ("10.2.9", "Find the pattern in the back bearings of 000°, 045°, 090°, 135°, 180°.",
            "180°, 225°, 270°, 315°, 000°; each differs by 180°.",
            "Add 180° and reduce modulo 360°.", "R"),
           ("10.2.10", "Investigate the error in a height computed from an angle of 89° and "
            "a distance of 10 m when the angle is out by 1°.",
            "The error is large, because tan θ is steep near 90°.",
            "Compare tan 89° and tan 88°.", "R"),
           ("10.2.11", "Conjecture a rule for the distance to the horizon from a height h.",
            "About 3.57√h km, from the tangent to a sphere of radius 6371 km.",
            "Use Pythagoras with the Earth's radius.", "C")],
        C=[("10.3.1", "Explain in your own words what Pythagoras' theorem states.",
            "That in a right-angled triangle the square on the hypotenuse equals the sum of "
            "the squares on the other two sides.", "State the theorem.", "R"),
           ("10.3.2", "Write a complete solution to: find the hypotenuse of a triangle with "
            "legs 7 cm and 24 cm.",
            "25 cm", "√(49 + 576) = √625.", "F"),
           ("10.3.3", "Choose between Pythagoras and a trigonometric ratio to find a missing "
            "side and justify.", "Pythagoras when two sides are known; a ratio when one side "
            "and one acute angle are known.", "Say what each needs.", "R"),
           ("10.3.4", "Set out a full solution to: find the angle of elevation of a slope "
            "that rises 2 m over 5 m.",
            "About 21.8°, from arctan(2/5).", "Use the inverse tangent.", "F"),
           ("10.3.5", "Explain why the choice of trigonometric ratio depends on which sides "
            "are known.", "Because sine involves the hypotenuse, cosine involves the "
            "hypotenuse and tangent does not, so the ratio must match the sides available.",
            "List the three ratios.", "R"),
           ("10.3.6", "Describe, with an example, the difference between an angle of "
            "elevation and an angle of depression.", "Elevation is measured upwards from the "
            "horizontal to an object above; depression is measured downwards to an object "
            "below.", "Draw both.", "R"),
           ("10.3.7", "Explain why the angle of elevation equals the angle of depression for "
            "two observers.",
            "Because the horizontal lines are parallel and the line of sight is a "
            "transversal, so the alternate angles are equal.", "Draw the two horizontals.",
            "R"),
           ("10.3.8", "Write the reasoning that shows sin² θ + cos² θ = 1.",
            "Dividing a² + b² = c² by c² gives (a/c)² + (b/c)² = 1, which is sin² θ + cos² θ.",
            "Divide Pythagoras by c².", "R"),
           ("10.3.9", "Set out the argument that a triangle with sides satisfying a² + b² = "
            "c² is right-angled.",
            "By the converse of Pythagoras, the angle opposite c is a right angle, because "
            "the triangle with those sides must be the right-angled one.", "Use the converse.",
            "R"),
           ("10.3.10", "Explain what a bearing is and why it is written in three figures.",
            "An angle measured clockwise from north; three figures prevent 05° and 50° from "
            "being confused.", "State the convention.", "R"),
           ("10.3.11", "Describe the relationship between a back bearing and a forward "
            "bearing.", "They differ by 180°, because reversing a direction turns it through "
            "a half turn.", "Add or subtract 180°.", "R"),
           ("10.3.12", "Explain, with an example, when a trigonometric calculation is not "
            "enough for a decision.",
            "Any answer is acceptable if it identifies a safety limit that the error interval "
            "crosses, as with a slope measured at 30° against a limit of 28°.",
            "Give a specific example.", "R")],
        D=[("10.4.1", "A tree is 18 m from an observer whose eye is 1.5 m above the ground. "
            "The angle of elevation to the top is 31°. Find the height of the tree.",
            "About 12.3 m, from 18 × tan 31° + 1.5.", "Use the tangent and add the eye level.",
            "A"),
           ("10.4.2", "From a cliff 45 m high, the angle of depression to a boat is 9°. Find "
            "the distance of the boat from the base.",
            "About 284 m, from 45/tan 9°.", "Use the tangent.", "A"),
           ("10.4.3", "A ramp must rise no more than 1 m in 12. Find the greatest angle and "
            "the length of a ramp that rises 0.9 m.",
            "About 4.8°; the ramp is about 10.8 m long.",
            "Use the inverse tangent and Pythagoras.", "A"),
           ("10.4.4", "A ship sails 25 km on a bearing of 040° and then 20 km on a bearing of "
            "130°. Find the distance and bearing from the start.",
            "About 30 km on a bearing of about 079°.",
            "Resolve each leg into components.", "A"),
           ("10.4.5", "A television mast is supported by a wire from a point 30 m from its "
            "base. The wire makes an angle of 62° with the ground. Find the height of the "
            "mast and the length of the wire.",
            "About 56.4 m high; the wire is about 64 m long.",
            "Use the tangent and then Pythagoras.", "A"),
           ("10.4.6", "A plane flies 300 km north and then 400 km east. Find the direct "
            "distance and bearing from the start.",
            "500 km on a bearing of about 127°.",
            "Use Pythagoras and the tangent.", "A"),
           ("10.4.7", "A roof has a rise of 2.4 m and a run of 6 m. Investigate whether it "
            "meets a rule limiting the pitch to 25° and justify.",
            "No: the pitch is arctan(0.4) ≈ 21.8°, so it does meet the rule.",
            "Compare the angle with the limit.", "R"),
           ("10.4.8", "A surveyor measures a plot as 25 m, 39 m and 56 m on a traverse that "
            "closes. Investigate whether the plot contains a right angle and justify.",
            "25² + 39² = 625 + 1521 = 2146, and 56² = 3136, so no right angle is present.",
            "Test Pythagoras on the longest side.", "R"),
           ("10.4.9", "A ladder must reach a window 5 m up with its foot no more than 1.8 m "
            "from the wall. Investigate whether a 5.5 m ladder is suitable and justify.",
            "Yes: √(25 + 3.24) = 5.31 m, so a 5.5 m ladder reaches with the foot at 1.8 m.",
            "Apply Pythagoras.", "R"),
           ("10.4.10", "A drone flies 200 m on a bearing of 315° and then 150 m on a bearing "
            "of 045°. Investigate the final position and justify.",
            "About 288 m north and 35 m west of the start, so the displacement is about 290 m "
            "on a bearing of about 353°.", "Resolve into components.", "C"),
           ("10.4.11", "A height is measured from 50 m with an angle of 20°. Investigate the "
            "effect on the height of an error of 1° in the angle.",
            "The height changes from 17.6 m to 19.4 m, an error of about 1.8 m or 10%.",
            "Compare tan 20° and tan 21°.", "R"),
           ("10.4.12", "Explain, with a measurement of your own, when a measurement is too "
            "imprecise for the decision being made.",
            "Any answer is acceptable if it shows that the error interval crosses the limit "
            "that the decision depends on.", "Give a specific example.", "R")],
    ),
    assessment=[
        dict(title="A1 · The flagpole",
             text="A flagpole stands on level ground. From a point 22 m from its base the "
                  "angle of elevation to the top is 34°, measured with a clinometer held 1.5 m "
                  "above the ground. Find the height of the flagpole, find the error interval "
                  "if the distance is 22 ± 0.3 m, and state whether the flagpole is certainly "
                  "taller than 16 m.",
             note="Criteria A and C · use the tangent ratio, carry the bounds through, and "
                  "justify the conclusion."),
        dict(title="A2 · The two bearings",
             text="A fishing boat sails 18 km on a bearing of 065° and then 24 km on a "
                  "bearing of 155°. Find its distance and bearing from the harbour, find the "
                  "bearing of the direct route home, and explain how the errors in the two "
                  "bearings would affect the final position.",
             note="Criteria B and D · resolve into components, find the resultant, and comment "
                  "on the accumulation of error."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of space, "
        "measurement and equivalence appear in your work?",
        "How is the global context of scientific and technical innovation, and its exploration of "
        "surveying, navigation and safe design, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a measurement-based calculation for a safety decision, and "
        "what would you still like to ask?",
    ],
    review=dict(
        ideas=["a² + b² = c² connects the sides of a right-angled triangle.",
               "The hypotenuse is opposite the right angle and is the longest side.",
               "sin θ = opposite/hypotenuse, cos θ = adjacent/hypotenuse, tan θ = "
               "opposite/adjacent.",
               "The ratios depend on the angle alone, so one table serves every triangle.",
               "sin² θ + cos² θ = 1, from dividing Pythagoras by c².",
               "A bearing is measured clockwise from north in three figures.",
               "A back bearing differs by 180°.",
               "Errors in the inputs combine in the answer, and relative errors add."],
        vocab=["hypotenuse", "leg", "converse", "sine", "cosine", "tangent", "inverse ratio",
               "angle of elevation", "angle of depression", "bearing", "back bearing",
               "traverse"],
        mixed=[("10.R1", "Find the hypotenuse when the legs are 8 cm and 15 cm."),
               ("10.R2", "Find tan 30° to three significant figures."),
               ("10.R3", "A triangle has hypotenuse 20 and an angle of 50°. Find the opposite "
                        "side."),
               ("10.R4", "Find the angle whose tangent is 0.75."),
               ("10.R5", "Find the back bearing of 246°."),
               ("10.R6", "Explain why the sine and cosine of complementary angles swap.")],
    ),
    projects=dict(
        service=[("Community need", "Heights, slopes and routes are estimated without stating "
                                    "the accuracy."),
                 ("Mathematical connection", "Pythagoras, trigonometry and error intervals."),
                 ("Proposed action", "Measure one inaccessible height or slope and publish the "
                                     "result with its error interval."),
                 ("Expected impact", "A reader knows how much to trust the figure."),
                 ("Student reflection", "Record the measurements, the calculation and the "
                                        "interval.")],
        community=[("Project idea", "An accessibility survey of one route or building."),
                   ("Need", "Ramps, steps and paths are used without a check against the "
                            "rules."),
                   ("Research question", "Which slopes and heights on our site meet the "
                                         "accessibility rules, and how sure are we?"),
                   ("Mathematics", "Trigonometric ratios and error intervals."),
                   ("Action or outcome", "A one-page survey with each slope, its angle and a "
                                         "verdict."),
                   ("Beneficiaries", "Everyone who uses the route or building."),
                   ("Evidence", "The survey with the measurements and the intervals.")],
        personal=[("Personal interest", "A climb, a flight path or a sports kick."),
                  ("Learning goal", "To measure something inaccessible and state how accurate "
                                    "the answer is."),
                  ("Product or outcome", "A measurement report with an error interval."),
                  ("Mathematics", "Pythagoras and the trigonometric ratios."),
                  ("Process", "Measure a distance and an angle, calculate, and bound the "
                              "error."),
                  ("Evidence", "The measurements, the calculation and the interval.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=11, title="Surface Area and Volume",
    key="Form", related=["Space", "Measurement", "Quantity"],
    context="Globalisation and sustainability",
    exploration="Packaging, water storage and material efficiency",
    inquiry=("The surface area of a solid is the quantity of material needed to make it and "
             "its volume is the quantity it can hold, and for a fixed volume the shape that "
             "minimises surface area is the one that wastes least; the ratio of the two "
             "therefore decides how efficient a container is."),
    atl=("Transfer",
         "Students transfer the formulae for area and volume between solids, and apply them "
         "to a real packaging or storage problem of their own choice."),
    standfirst="Surface area measures the material; volume measures the space inside. For a "
               "fixed volume, a cube wastes less material than a long thin box, and a sphere "
               "wastes least of all.",
    engage="A drinks company must ship 1 litre of juice. Which container uses least "
           "cardboard: a cube, a tall cylinder, or a flat box?",
    questions=[("Factual", "What are the formulae for the surface area and volume of prisms, "
                           "cylinders, pyramids, cones and spheres?"),
               ("Conceptual", "Why does the surface-area-to-volume ratio change with size, "
                              "and what does that mean for the efficiency of a container?"),
               ("Debatable", "Is the container that uses least material always the one that "
                             "should be used, or do handling, transport and recycling change "
                             "the answer?")],
    application_lede="Each task involves a solid and a quantity. State the formula you use, "
                     "the units of your answer, and whether you are measuring material or "
                     "capacity.",
    projects_lede="Packaging is a mathematical optimisation with an environmental "
                  "consequence. Model one container and say what your model ignores.",
    sections=[
        dict(id="11.1", title="Prisms and cylinders",
             inquiry_q="How are the surface area and volume of a prism found, and why does "
                       "one formula serve them all?",
             teach=[
                 "A prism has a constant cross-section, and its volume is the area of the cross-section times the length. One formula serves every prism, whatever the shape of the section.",
                 "Every formula in this chapter is a rule for measuring space: the volume measures the space enclosed and the surface area measures the material that encloses it.",
                 "The surface area of a prism is twice the area of the cross-section plus the perimeter of the cross-section times the length, because the curved part unrolls into a rectangle.",
                 "A cylinder is a prism with a circular cross-section, so its volume is πr²h and its curved surface area is 2πrh.",
                 "Units must be tracked: an area is in square units and a volume in cubic units, and 1 litre is 1000 cm³, which is the conversion that connects the two.",
             
                 "Density is mass per unit volume, so mass = density × volume, and a capacity in litres is a volume in cubic decimetres because 1 litre = 1000 cm³.",
             ],
             examples=[

                 dict(q="A triangular prism has a right-angled cross-section with legs 3 cm "
                        "and 4 cm, and a length of 10 cm. Find its volume and surface area.",
                      vis=F("prism", "cuboid", 4, 3, 10, "a triangular prism of length 10 cm"),
                      reasoning="Find the cross-section area and perimeter, then apply the two "
                               "prism formulae.",
                      steps=["The cross-section is a right triangle with legs 3 and 4, so its "
                             "area is ½ × 3 × 4 = 6 cm².",
                             "Its hypotenuse is 5 cm, so the perimeter is 3 + 4 + 5 = 12 cm.",
                             "The volume is 6 × 10 = 60 cm³.",
                             "The surface area is 2 × 6 + 12 × 10 = 12 + 120 = 132 cm².",
                             "The two triangular faces contribute only 12 cm² of the 132 cm²."],
                      ans="volume 60 cm³, surface area 132 cm²",
                      interp="The prism formulae reduce a three-dimensional problem to a "
                             "two-dimensional one, which is why they work for every prism."),
                 dict(q="A cylinder has radius 5 cm and height 12 cm. Find its volume and "
                        "total surface area.",
                      vis=F("cone", 5, 12, "a cylinder of radius 5 and height 12"),
                      reasoning="Apply the cylinder formulae.",
                      steps=["The volume is πr²h = π × 25 × 12 = 300π ≈ 942 cm³.",
                             "The curved surface area is 2πrh = 2π × 5 × 12 = 120π ≈ 377 cm².",
                             "The two circular ends contribute 2 × πr² = 50π ≈ 157 cm².",
                             "The total surface area is 170π ≈ 534 cm².",
                             "In litres the volume is about 0.942 litres."],
                      ans="volume about 942 cm³, surface area about 534 cm²",
                      interp="The two ends are a third of the surface area, which is why a "
                             "short wide cylinder uses relatively more material than a tall "
                             "one."),
dict(q="A steel tank is a cylinder of radius 1.2 m and height 2 m, made from "
                        "sheet steel of mass 8 kg per m². Find the mass of the empty tank and "
                        "the mass when full of water.",
                      vis=F("cone", 1.2, 2, "a cylindrical tank"),
                      reasoning="Find the surface area for the mass of the steel, and the "
                               "volume for the mass of the water.",
                      steps=["The surface area is 2πrh + 2πr² = 2π × 1.2 × 2 + 2π × 1.44 = "
                             "4.8π + 2.88π = 7.68π ≈ 24.1 m².",
                             "The mass of the steel is 24.1 × 8 ≈ 193 kg.",
                             "The volume is πr²h = π × 1.44 × 2 = 2.88π ≈ 9.05 m³.",
                             "Water has density 1000 kg/m³, so the water has mass about 9050 "
                             "kg.",
                             "The full tank has mass about 9240 kg, which needs a strong "
                             "support."],
                      ans="about 193 kg empty and about 9240 kg full",
                      interp="The water outweighs the tank by a factor of about 47, which is "
                             "why the support matters more than the material.")
             ],
             inv=dict(
                 task="Take five prisms and cylinders of your own, including one with a "
                      "triangular section, one with a rectangular section and one cylinder. "
                      "For each, compute the volume and the surface area, then compute the "
                      "ratio of surface area to volume and rank them.",
                 table=[["solid", "volume", "surface area", "area/volume"],
                        ["cube, side 4", "64 cm³", "96 cm²", "1.50"],
                        ["cuboid 2 × 4 × 8", "64 cm³", "112 cm²", "1.75"],
                        ["cylinder r = 2, h = 5", "62.8 cm³", "87.9 cm²", "1.40"],
                        ["cylinder r = 4, h = 1.25", "62.8 cm³", "125.7 cm²", "2.00"],
                        ["triangular prism 3-4-5, l = 10", "60 cm³", "132 cm²", "2.20"]],
                 notice=["All five had about the same volume but very different surface areas.",
                         "The cube had the smallest ratio, and the long thin prism the largest.",
                         "The short wide cylinder was worse than the tall narrow one.",
                         "The ratio fell as the solid became more compact."],
                 obs="For a fixed volume the surface area depends on the shape, and the "
                     "compact shapes use least material.",
                 concl="A prism's volume is the area of its cross-section times its length and "
                       "its surface area is twice that area plus the perimeter times the "
                       "length, and the ratio of the two measures how much material a given "
                       "capacity requires.")),
        dict(id="11.2", title="Pyramids and cones",
             inquiry_q="How are the formulae for pyramids, cones and spheres obtained, and "
                       "what do they have in common?",
             teach=[
                 "A pyramid has volume one third of the prism with the same base and height, and a cone has volume one third of the cylinder with the same base and height, so V = (1/3) × base area × height for both.",
                 "The one-third rule can be checked by pouring: a cone holds exactly a third of what a cylinder of the same base and height holds, which is the experimental reason for the factor.",
                 "The curved surface area of a cone is πrl, where l is the slant height, and the slant height, the radius and the height form a right-angled triangle, so Pythagoras finds l from the other two.",
                 "A pyramid's surface area is the base area plus the sum of the triangular faces, and each triangular face is found from the slant height of that face rather than from the vertical height.",
                 "The one-third rule and the slant-height triangle are the two facts that turn a drawing of a solid into a calculation, and both are consequences of a cross-section.",
             ],
             examples=[

                 dict(q="A cone has radius 6 cm and height 8 cm. Find its volume and curved "
                        "surface area.",
                      vis=F("cone", 6, 8, "a cone of radius 6 and height 8"),
                      reasoning="Find the slant height by Pythagoras, then apply the cone "
                               "formulae.",
                      steps=["The slant height is l = √(6² + 8²) = √100 = 10 cm.",
                             "The volume is (1/3)πr²h = (1/3)π × 36 × 8 = 96π ≈ 301 cm³.",
                             "The curved surface area is πrl = π × 6 × 10 = 60π ≈ 188 cm².",
                             "The base area is 36π ≈ 113 cm², so the total is 96π ≈ 301 cm².",
                             "A cylinder with the same base and height would hold 288π ≈ 905 "
                             "cm³, three times as much."],
                      ans="volume 96π ≈ 301 cm³, curved surface area 60π ≈ 188 cm²",
                      interp="The slant height is not the height, and using the height in the "
                             "surface area formula is the commonest error with cones."),
                 dict(q="A sphere has radius 9 cm. Find its volume and surface area, and "
                        "compare with a cube of the same volume.",
                      vis=F("sphere", 9, "a sphere of radius 9"),
                      reasoning="Apply the sphere formulae, then find the cube's side.",
                      steps=["The volume is (4/3)πr³ = (4/3)π × 729 = 972π ≈ 3054 cm³.",
                             "The surface area is 4πr² = 4π × 81 = 324π ≈ 1018 cm².",
                             "A cube of the same volume has side ³√3054 ≈ 14.5 cm.",
                             "Its surface area is 6 × 14.5² ≈ 1262 cm².",
                             "So the sphere uses about 19% less material for the same "
                             "capacity."],
                      ans="volume about 3054 cm³, surface area about 1018 cm², against about "
                          "1262 cm² for the cube",
                      interp="The sphere is the most efficient shape for a given volume, which "
                             "is why balls, tanks and drops are spherical.")
             ],
             inv=dict(
                 task="Take four solids: a cone, a pyramid, a sphere and a cylinder. For each, "
                      "find the volume and the surface area, then arrange them so that all "
                      "have the same volume and compare their surface areas.",
                 table=[["solid", "volume", "surface area", "same volume comparison"],
                        ["cone r = 6, h = 8", "301 cm³", "301 cm²", "—"],
                        ["sphere of volume 301", "301 cm³", "252 cm²", "least material"],
                        ["cylinder of volume 301", "301 cm³", "318 cm²", "—"],
                        ["cube of volume 301", "301 cm³", "381 cm²", "most material"]],
                 notice=["The sphere had the smallest surface area for the same volume.",
                         "The cube had the largest.",
                         "The cone was close to the cylinder, because a cone is a third of "
                         "one.",
                         "The ranking of the shapes was the same for every volume."],
                 obs="For a fixed volume the sphere has the least surface area and the cube "
                     "the most among these shapes, and the ordering does not depend on the "
                     "volume chosen.",
                 concl="The formulae for pyramids, cones and spheres all reduce volume and "
                       "surface area to the base, the height and the radius, and the sphere is "
                       "the shape that encloses a given volume with least surface.")),
        dict(id="11.3", title="Spheres and composite solids",
             inquiry_q="How is the volume of a sphere found, and how is a solid made of "
                       "several parts measured?",
             teach=[
                 "A sphere of radius r has volume (4/3)πr³ and surface area 4πr², and the two formulae are related because a small increase in the radius adds a shell whose volume is approximately the surface area times the thickness.",
                 "The formulae can be checked by experiment: a sphere displaces its own volume of water, and the displacement can be measured in a cylinder, which is the historical reason for the formula.",
                 "A composite solid is measured by adding the volumes of its parts and, for the surface area, adding the exposed faces only. A face where two parts meet is not on the surface and must not be counted.",
                 "Choosing how to cut a solid into parts is a representation of the problem, and a different cutting can make the same calculation much shorter.",
                 "Every quantity in this chapter is a measurement of space: a volume measures the space a solid encloses and a surface area measures the material that encloses it, and the two are reported in different units.",
             ], examples=[
                 dict(q="A solid is a cylinder of radius 3 cm and height 10 cm with a "
                        "hemisphere of radius 3 cm on top. Find its total volume.",
                      vis=F("prism", "cylinder", 3, 10, 6,
                            "a cylinder of radius 3 cm and height 10 cm"),
                      reasoning="Add the volume of the cylinder to half the volume of a sphere.",
                      steps=["The cylinder has volume π × 3² × 10 = 90π cm³.",
                             "A hemisphere of radius 3 has volume half of (4/3)π × 3³ = 18π cm³.",
                             "The total volume is 90π + 18π = 108π ≈ 339.3 cm³.",
                             "The two parts share a circular face, which does not affect the "
                             "volume.",
                             "For the surface area the shared face would be left out, which "
                             "is the difference between the two measures."],
                      ans="108π ≈ 339.3 cm³",
                      interp="A composite volume is a sum, and the shared face matters only "
                             "for the surface area."),
                 dict(q="A sphere of radius 5 cm is dropped into a full cylinder of radius "
                        "5 cm, and the water that overflows is collected. How much water "
                        "overflows?",
                      vis=F("prism", "cylinder", 10, 12, 10,
                            "the sphere displaces its own volume"),
                      reasoning="The overflow is the volume of the sphere.",
                      steps=["The sphere has volume (4/3)π × 5³ = (500/3)π ≈ 523.6 cm³.",
                             "The displaced water has exactly that volume.",
                             "So about 523.6 cm³, or 0.524 litres, overflows.",
                             "The radius of the cylinder does not matter, only that the "
                             "sphere fits.",
                             "This displacement is the experimental check on the formula."],
                      ans="about 523.6 cm³, or 0.524 litres",
                      interp="A volume can be measured by displacement, and the measurement "
                             "is a check on the formula rather than a replacement for it."),
             ], inv=dict(
                 task="Take four composite solids: a cylinder with a hemisphere on top, a "
                      "cuboid with a pyramid on top, a cone with a hemisphere, and a shape of "
                      "your own. For each, find the total volume and the total surface area, "
                      "stating clearly which faces are shared and therefore not counted. Then "
                      "check one volume by displacement in a measuring cylinder.",
                 table=[["solid", "parts", "volume", "shared faces"],
                        ["cylinder r = 3, h = 10 + hemisphere r = 3", "90π + 18π", "108π",
                         "one circle"],
                        ["cuboid 4 × 4 × 6 + pyramid base 4 × 4, h = 3", "96 + 16", "112",
                         "one square"],
                        ["cone r = 3, h = 4 + hemisphere r = 3", "12π + 18π", "30π",
                         "one circle"]],
                 notice=["Every composite volume was the sum of the parts.",
                         "The shared faces were left out of the surface area but made no "
                         "difference to the volume.",
                         "The displacement check agreed with the calculation to within the "
                         "precision of the measuring cylinder.",
                         "A hemisphere is half a sphere, which is why its formula has the "
                         "factor of one half."],
                 obs="A composite solid is measured by adding its parts, and the surface area "
                     "counts only the faces that are actually exposed.",
                 concl="Volumes add and exposed faces add, so a composite solid is measured by "
                       "decomposing it into parts whose formulae are known.")),
        dict(id="11.4", title="Scaling surface area and volume",
             inquiry_q="What happens to the surface area and volume of a solid when every "
                       "length is multiplied?",
             teach=[
                 "When every length of a solid is multiplied by k, the surface area is multiplied by k² and the volume by k³, because an area counts two dimensions and a volume counts three.",
                 "The ratio of surface area to volume is therefore divided by k, so a larger solid of the same shape has proportionally less surface for each unit of volume. This is why large animals cool slowly and large packets are cheaper per litre.",
                 "The cube of the scale factor is the one that surprises: doubling a length multiplies the volume by eight, so a model twice as long as the original needs eight times the material to fill.",
                 "Scaling is a representation of an object at a different size, and it is valid only for the quantities that scale with length. Mass, strength and cost depend on density and price as well, so they need their own model.",
             ], examples=[
                 dict(q="A cube has edges of 2 cm. Find its surface area and volume. Then find "
                        "both for a cube whose edges are three times as long.",
                      vis=F("tiles", 2, 2, [(0, 0), (1, 0), (0, 1), (1, 1)],
                            "a cube of edge 2 cm has 6 faces of 4 cm²",
                            note="surface 24 cm², volume 8 cm³"),
                      reasoning="Apply the scale factor to each measure with the right power.",
                      steps=["The small cube has surface area 6 × 2² = 24 cm² and volume 2³ = "
                             "8 cm³.",
                             "The large cube has edges of 6 cm.",
                             "Its surface area is 6 × 6² = 216 cm², which is 9 times the "
                             "small one.",
                             "Its volume is 6³ = 216 cm³, which is 27 times the small one.",
                             "So a length factor of 3 gave an area factor of 9 and a volume "
                             "factor of 27."],
                      ans="24 cm² and 8 cm³; 216 cm² and 216 cm³",
                      interp="The powers of the scale factor are the number of dimensions in "
                             "the quantity, and confusing them is the commonest error."),
                 dict(q="Two similar bottles have heights in the ratio 1 : 4. The small "
                        "bottle holds 250 ml. How much does the large one hold?",
                      vis=F("table", [["measure", "small", "large", "factor"],
                                      ["height", "h", "4h", "4"],
                                      ["surface area", "S", "16S", "16"],
                                      ["volume", "250 ml", "16 litres", "64"]],
                            "lengths ×4, areas ×16, volumes ×64"),
                      reasoning="The volume scales by the cube of the length factor.",
                      steps=["The length factor is 4.",
                             "The volume factor is 4³ = 64.",
                             "The large bottle holds 64 × 250 ml = 16 000 ml.",
                             "That is 16 litres, which is 64 times the small bottle.",
                             "The surface area is only 16 times as large, so the large bottle "
                             "uses proportionally less material per litre."],
                      ans="16 litres",
                      interp="Capacity grows far faster than height, and faster than the "
                             "material needed to make the bottle."),
             ], inv=dict(
                 task="Take three pairs of similar solids: two cubes of different edge, two "
                      "spheres of different radius, and two cylinders of the same shape but "
                      "different size. For each pair, find the length factor, then measure or "
                      "calculate the surface area factor and the volume factor, and check "
                      "that they are the square and the cube of the length factor. Finally "
                      "compute the surface-area-to-volume ratio for each member of one pair "
                      "and see how it changes with size.",
                 table=[["pair", "length factor", "area factor", "volume factor"],
                        ["cube 1 cm : cube 3 cm", "3", "9", "27"],
                        ["sphere r : sphere 2r", "2", "4", "8"],
                        ["cylinder h : cylinder 2h", "2", "4", "8"],
                        ["ratio for the cubes", "3", "6 : 2", "1 : 27"]],
                 notice=["Every area factor was the square of the length factor.",
                         "Every volume factor was the cube.",
                         "The surface-area-to-volume ratio fell as the solid grew.",
                         "The sphere kept the smallest ratio of the three shapes at every "
                         "size."],
                 obs="Lengths scale by k, areas by k² and volumes by k³, so the "
                     "surface-area-to-volume ratio scales by 1/k.",
                 concl="Scaling multiplies each measure by the scale factor raised to the "
                       "number of dimensions, and the falling surface-to-volume ratio is why "
                       "size changes what is efficient.")),
        dict(id="11.5", title="Packaging, cost and design",
             inquiry_q="How is the efficiency of a container measured, and why does size "
                       "matter?",
             teach=[
                 "The efficiency of a container is measured by the ratio of its surface area to its volume, and a smaller ratio means less material for the same capacity.",
                 "For similar shapes the ratio is proportional to 1/length, so a container twice as large has half the ratio. This is why large containers are cheaper per unit volume.",
                 "A cube of side a has ratio 6/a, a cylinder of radius r and height 2r has ratio 3/r, and a sphere has ratio 3/r. The sphere is the best of the three.",
                 "Efficiency is only one criterion. Handling, stacking, transport and recycling all affect the real choice, and a model of material alone can recommend the wrong container.",
             ], examples=[
                 dict(q="Compare the efficiency of a cube of side 10 cm and a cylinder of "
                        "radius 5 cm and height 10 cm, both holding about 1 litre.",
                      vis=F("prism", "cuboid", 4, 4, 4, "a cube of side 10 cm"),
                      reasoning="Compute both volumes and both surface areas, then the ratios.",
                      steps=["The cube has volume 1000 cm³ and surface area 6 × 100 = 600 "
                             "cm², so the ratio is 0.60.",
                             "The cylinder has volume π × 25 × 10 = 250π ≈ 785 cm³.",
                             "Its surface area is 2π × 5 × 10 + 2 × 25π = 150π ≈ 471 cm², so "
                             "the ratio is 0.60.",
                             "The cylinder holds less, so the comparison is not yet fair.",
                             "Scaling the cylinder to 1000 cm³ gives a height of about 12.7 cm "
                             "and a ratio of about 0.54, so it is more efficient."],
                      ans="the cube has ratio 0.60; the cylinder scaled to the same volume has "
                          "about 0.54",
                      interp="Comparing ratios requires the same volume, and the cylinder wins "
                             "because it is closer to a sphere."),
                 dict(q="A spherical tank and a cubical tank each hold 8 m³. Find the surface "
                        "area of each and the material saved by the sphere.",
                      vis=F("sphere", 1.24, "a sphere holding 8 m³"),
                      reasoning="Find the radius from the volume, then the surface area.",
                      steps=["For the sphere, (4/3)πr³ = 8, so r³ = 6/π and r ≈ 1.24 m.",
                             "The surface area is 4πr² ≈ 4π × 1.54 ≈ 19.4 m².",
                             "The cube has side 2 m and surface area 6 × 4 = 24 m².",
                             "So the sphere saves 24 − 19.4 = 4.6 m² of material.",
                             "That is about 19% less material for the same capacity."],
                      ans="sphere about 19.4 m², cube 24 m², saving about 4.6 m²",
                      interp="The saving is a fifth of the material, which over many tanks is "
                             "a substantial quantity of metal."),
             ], inv=dict(
                 task="Choose a real container: a drinks carton, a tin, a bottle or a water "
                      "tank. Measure or find its dimensions, compute its volume and surface "
                      "area, and compare with the most efficient shape of the same volume. "
                      "Then list the reasons the real container is not the most efficient "
                      "one.",
                 table=[["container", "volume", "surface area", "ratio", "efficient shape "
                                                                        "ratio"],
                        ["drinks carton", "1000 cm³", "630 cm²", "0.63", "0.48"],
                        ["tin", "330 cm³", "290 cm²", "0.88", "0.56"],
                        ["bottle", "500 cm³", "420 cm²", "0.84", "0.53"]],
                 notice=["Every real container used more material than the efficient shape.",
                         "The carton was closest, because it is nearly a cuboid of good "
                         "proportions.",
                         "The tin was worst, because a cylinder taller than it is wide is "
                         "inefficient.",
                         "Handling, stacking and printing all explain the differences."],
                 obs="Real containers use more material than the most efficient shape of the "
                     "same volume, and the difference is explained by constraints other than "
                     "material.",
                 concl="The efficiency of a container is measured by its surface-area-to-"
                       "volume ratio, and the real choice is decided by constraints that a "
                       "material model does not include.")),
        dict(id="11.6", title="Investigation: the most efficient package",
             inquiry_q="Which container for a given capacity uses least material, and what "
                       "does the answer ignore?",
             teach=[
                 "For a given capacity the shape with least surface area is the sphere, and among cylinders the one whose height equals its diameter.",
                 "The optimal proportions can be found by writing the surface area in terms of one variable, using the volume constraint, and minimising.",
                 "A real container must stand, stack, be held and be filled, and each of these adds a constraint that the mathematical optimum ignores.",
                 "A model of material alone is a first step, and a good design report states what the model ignored as well as what it found.",
             ], examples=[
                 dict(q="Find the dimensions of the cylinder of volume 1000 cm³ with the "
                        "least surface area.",
                      vis=F("cone", 5.4, 10.8, "the optimal cylinder has h = 2r"),
                      reasoning="Write the surface area in terms of r alone using the volume "
                               "constraint, then minimise.",
                      steps=["Let the radius be r and the height h, with πr²h = 1000.",
                             "So h = 1000/(πr²).",
                             "The surface area is 2πr² + 2πrh = 2πr² + 2000/r.",
                             "Differentiating and setting to zero gives 4πr = 2000/r², so "
                             "r³ = 500/π.",
                             "Hence r ≈ 5.42 cm and h ≈ 10.8 cm, so h = 2r."],
                      ans="radius about 5.42 cm and height about 10.8 cm, with h = 2r",
                      interp="The optimal cylinder has height equal to its diameter, which is "
                             "a result about shape rather than about size."),
                 dict(q="A drinks company must ship 1 litre in a cylinder that can stand on a "
                        "shelf. Compare the optimal cylinder with a shorter, wider one and "
                        "comment on the choice.",
                      vis=F("prism", "cuboid", 4, 4, 6, "a shorter, wider cylinder"),
                      reasoning="Compare the surface areas of two cylinders of the same "
                               "volume.",
                      steps=["The optimal cylinder has r ≈ 5.42 cm, h ≈ 10.8 cm and surface "
                             "area about 549 cm².",
                             "A cylinder with r = 6 cm has h = 1000/(36π) ≈ 8.84 cm and "
                             "surface area about 559 cm².",
                             "The difference is only about 10 cm², or 2%.",
                             "The shorter can is easier to hold and to stack, which may be "
                             "worth more than the 2% saving.",
                             "So the mathematical optimum is not automatically the best "
                             "design."],
                      ans="the optimal cylinder uses about 549 cm²; the shorter one about 559 "
                          "cm²",
                      interp="A 2% material saving can be outweighed by handling and "
                             "transport, which is why the optimum is a starting point rather "
                             "than an answer."),
             ], inv=dict(
                 task="Design a container for a stated capacity and a stated constraint, such "
                      "as standing on a shelf, fitting in a hand, or stacking in a lorry. "
                      "Model the material used, find the mathematical optimum, then choose a "
                      "design and justify the departure from the optimum.",
                 table=[["design", "capacity", "surface area", "departure from optimum"],
                        ["optimal cylinder", "1000 cm³", "549 cm²", "none"],
                        ["short wide can", "1000 cm³", "559 cm²", "2% more material"],
                        ["cuboid carton", "1000 cm³", "600 cm²", "9% more material"],
                        ["sphere", "1000 cm³", "484 cm²", "12% less, but rolls"]],
                 notice=["The sphere used least material but cannot stand or stack.",
                         "The carton used most but stacks and prints well.",
                         "Every real design departed from the optimum for a stated reason.",
                         "The departure was always justified by a constraint, not by "
                         "ignorance."],
                 obs="The mathematical optimum minimises material alone, and every real design "
                     "departs from it because of constraints the model does not contain.",
                 concl="A container is designed by minimising surface area for a fixed volume "
                       "and then relaxing the optimum to satisfy the constraints of use, and "
                       "the report of a design states both.")),
    ],
    practice=dict(
        A=[("11.1.1", "Find the volume of a cuboid 5 cm by 4 cm by 3 cm.", "60 cm³",
            "Multiply the three dimensions.", "F"),
           ("11.1.2", "Find the surface area of a cube of side 6 cm.", "216 cm²",
            "6 × 6².", "F"),
           ("11.1.3", "Find the volume of a cylinder of radius 3 cm and height 7 cm.",
            "198 cm³", "π × 9 × 7.", "F"),
           ("11.1.4", "Find the curved surface area of a cylinder of radius 4 cm and height "
            "9 cm.", "226 cm²", "2π × 4 × 9.", "F"),
           ("11.1.5", "Find the volume of a cone of radius 3 cm and height 8 cm.",
            "75.4 cm³", "(1/3)π × 9 × 8.", "F"),
           ("11.1.6", "Find the volume of a sphere of radius 6 cm.", "905 cm³",
            "(4/3)π × 216.", "F"),
           ("11.1.7", "Find the surface area of a sphere of radius 5 cm.", "314 cm²",
            "4π × 25.", "F"),
           ("11.1.8", "A triangular prism has cross-section area 12 cm² and length 8 cm. "
            "Find its volume.", "96 cm³", "Area times length.", "F"),
           ("11.1.9", "Convert 2.5 litres to cubic centimetres.", "2500 cm³",
            "1 litre = 1000 cm³.", "F"),
           ("11.1.10", "Find the slant height of a cone of radius 5 cm and height 12 cm.",
            "13 cm", "√(25 + 144).", "F"),
           ("11.1.11", "Find the volume of a pyramid with base area 48 cm² and height 9 cm.",
            "144 cm³", "(1/3) × 48 × 9.", "F"),
           ("11.1.12", "A cuboid has volume 240 cm³ and base area 40 cm². Find its height.",
            "6 cm", "Divide the volume by the base area.", "F")],
        B=[("11.2.1", "The surface areas of similar cubes are in the ratio 4 : 9. Find the "
            "ratio of their volumes and justify.",
            "8 : 27, because the length ratio is 2 : 3 and volume scales as its cube.",
            "Take the square root, then cube.", "R"),
           ("11.2.2", "Investigate the pattern in the surface-area-to-volume ratio of cubes "
            "of side 1 to 6 cm.",
            "The ratios are 6, 3, 2, 1.5, 1.2, 1, halving and then continuing as 6/a.",
            "Compute both for each cube.", "R"),
           ("11.2.3", "Conjecture a rule for the dimensions of the cylinder of fixed volume "
            "with least surface area and justify.",
            "The height equals the diameter, because the optimum has h = 2r.",
            "Write the area in terms of r and minimise.", "C"),
           ("11.2.4", "Investigate the pattern in the volumes of cylinders of fixed surface "
            "area as the radius grows.",
            "The volume rises to a maximum and then falls, with the maximum at h = 2r.",
            "Compute for several radii.", "R"),
           ("11.2.5", "Build a table of the volumes of spheres of radius 1 to 5 and describe "
            "the pattern.",
            "The volumes rise faster than the cube of the radius alone suggests, following "
            "(4/3)πr³.", "Compute each volume.", "R"),
           ("11.2.6", "Conjecture a rule for the ratio of the surface area to the volume of a "
            "sphere of radius r.", "3/r, because 4πr² divided by (4/3)πr³ is 3/r.",
            "Divide the two formulae.", "R"),
           ("11.2.7", "Investigate the pattern in the material needed for 1-litre containers "
            "of different shapes.",
            "The sphere needs least, then the optimal cylinder, then the cube, then the long "
            "box.", "Compute each surface area at 1000 cm³.", "R"),
           ("11.2.8", "A can's height is twice its radius. Investigate the effect on its "
            "surface-area-to-volume ratio of doubling the radius.",
            "The ratio halves, because it is proportional to 1/r for similar shapes.",
            "Compute the ratio at two sizes.", "R"),
           ("11.2.9", "Find the pattern in the number of 1 cm cubes needed to build a cube of "
            "side n cm.", "n³, because the volume is the cube of the side.",
            "Count for n = 1, 2, 3.", "R"),
           ("11.2.10", "Investigate the pattern in the surface area of a stack of n cubes of "
            "side 1 cm.",
            "The area is 6n − 2(n − 1) = 4n + 2, because each new cube hides two faces.",
            "Count for n = 1, 2, 3.", "R"),
           ("11.2.11", "Conjecture a rule for the volume of a solid formed by rotating a "
            "right triangle about one leg.",
            "A cone of volume (1/3)πr²h, with r and h the two legs.",
            "Compare with the cone formula.", "R")],
        C=[("11.3.1", "Explain in your own words the difference between surface area and "
            "volume.", "Surface area measures the material needed to make the surface; "
            "volume measures the space inside.", "State both definitions.", "R"),
           ("11.3.2", "Write a complete solution to: find the volume and surface area of a "
            "cylinder of radius 4 cm and height 10 cm.",
            "Volume 502.7 cm³; surface area 351.9 cm².", "Apply the cylinder formulae.", "F"),
           ("11.3.3", "Choose between surface area and volume to answer a question about how "
            "much a container holds and justify.", "Volume, because capacity is a quantity of "
            "space and surface area is a quantity of material.", "Say what each measures.",
            "R"),
           ("11.3.4", "Set out a full solution to: find the curved surface area of a cone of "
            "radius 5 cm and slant height 13 cm.",
            "204 cm², from π × 5 × 13.", "Use πrl.", "F"),
           ("11.3.5", "Explain why the surface-area-to-volume ratio falls as a container "
            "grows.", "Because surface area scales as the square of the length and volume as "
            "the cube, so the ratio scales as 1/length.", "Compare the powers.", "R"),
           ("11.3.6", "Describe, with an example, the difference between a prism and a "
            "cylinder.", "A prism has a polygonal cross-section and a cylinder a circular "
            "one, but both have volume equal to cross-section area times length.",
            "Compare the two formulae.", "R"),
           ("11.3.7", "Explain why the volume of a cone is one third of the cylinder with the "
            "same base and height.",
            "Because a cone tapers to a point, and experiment or integration shows it fills "
            "exactly one third of the cylinder.", "Compare the two formulae.", "R"),
           ("11.3.8", "Write the reasoning that shows the slant height of a cone is not its "
            "height.", "The slant height is the hypotenuse of the right triangle formed by "
            "the radius, the height and the slant, so l = √(r² + h²).",
            "Apply Pythagoras.", "R"),
           ("11.3.9", "Set out the argument that the sphere encloses a given volume with the "
            "least surface area.", "Any answer is acceptable if it uses the fact that the "
            "sphere is the isoperimetric optimum, verified by comparing the ratio 3/r with "
            "larger ratios for other shapes.", "Compare the ratios.", "C"),
           ("11.3.10", "Explain what density is and how it connects mass to volume.",
            "Mass per unit volume, so mass = density × volume, and the units must match.",
            "State the definition.", "R"),
           ("11.3.11", "Describe the relationship between the mass of a container and its "
            "surface area.", "The material mass is the surface area times the mass per unit "
            "area of the material, so a smaller area means a lighter container.",
            "Multiply area by mass per area.", "R"),
           ("11.3.12", "Explain, with an example, when the most efficient container is not "
            "the best choice.",
            "Any answer is acceptable if it identifies a constraint such as standing, "
            "stacking, holding or printing that the material model ignores.",
            "Give a specific example.", "R")],
        D=[("11.4.1", "A tank is a cylinder of radius 0.8 m and height 1.5 m. Find its "
            "capacity in litres and the material needed for its curved surface.",
            "About 3016 litres; the curved surface is about 7.54 m².",
            "Use the cylinder formulae.", "A"),
           ("11.4.2", "A box measures 30 cm by 20 cm by 15 cm. Find its volume, its surface "
            "area, and the amount of cardboard for 100 boxes with 10% extra for joins.",
            "9000 cm³; 2700 cm²; about 297 m² for 100 boxes.",
            "Apply the cuboid formulae and add 10%.", "A"),
           ("11.4.3", "A spherical tank holds 10 m³. Find its radius and the material needed "
            "for its surface.",
            "Radius about 1.34 m; surface about 22.5 m².",
            "Solve (4/3)πr³ = 10.", "A"),
           ("11.4.4", "A cone-shaped funnel has radius 6 cm and height 10 cm. Find its "
            "capacity in millilitres and the area of tin needed for its curved surface.",
            "About 377 ml; the curved surface is about 204 cm².",
            "Use the cone formulae and 1 ml = 1 cm³.", "A"),
           ("11.4.5", "A manufacturer must package 2 litres. Compare the material for a cube, "
            "an optimal cylinder and a sphere, and recommend one with a reason.",
            "Cube about 934 cm²; cylinder about 774 cm²; sphere about 484 cm². The cylinder "
            "is recommended because it stands and stacks.", "Compute each surface area at "
            "2000 cm³.", "A"),
           ("11.4.6", "A glass jar holds 750 ml. Its surface area is 480 cm² and the glass "
            "has mass 0.5 g per cm². Find the mass of the empty jar and the fraction of the "
            "full mass that is glass.",
            "Empty 240 g; the glass is about 24% of the full mass of about 990 g.",
            "Add the contents mass to the glass mass.", "A"),
           ("11.4.7", "A concrete pipe is a cylinder of outer radius 0.5 m, inner radius 0.4 "
            "m and length 2 m. Investigate the volume of concrete and the mass at 2400 kg "
            "per m³.",
            "Volume about 1.13 m³; mass about 2707 kg.",
            "Subtract the inner cylinder from the outer.", "R"),
           ("11.4.8", "A grain silo is a cylinder of radius 3 m and height 8 m with a "
            "hemispherical roof. Find its capacity and its external surface area.",
            "About 282.7 m³; the external area is about 197.8 m².",
            "Add the cylinder and hemisphere formulae.", "A"),
           ("11.4.9", "A company ships balls of radius 4 cm in cuboid boxes of 8 cm by 8 cm "
            "by 8 cm. Investigate the fraction of the box volume occupied and the material "
            "wasted.", "The ball occupies about 52% of the box, so about 48% of the shipped "
            "volume is air.", "Compare the two volumes.", "R"),
           ("11.4.10", "A water tank is a cuboid 2 m by 1.5 m by 1 m. Investigate the "
            "dimensions of a cylinder of the same capacity with the least surface area.",
            "Radius about 0.86 m and height about 1.72 m, so h = 2r.",
            "Write the area in terms of r and minimise.", "C"),
           ("11.4.11", "A packet of biscuits is a cuboid 20 cm by 12 cm by 6 cm. Investigate "
            "the material saved by reducing the height to 5 cm and keeping the volume.",
            "The new box is about 19.2 cm by 12.5 cm by 5 cm, saving about 60 cm² of "
            "cardboard.", "Keep the volume fixed and recompute.", "C"),
           ("11.4.12", "Explain, with a container of your own, when a material model is not "
            "enough to choose a design.",
            "Any answer is acceptable if it identifies transport, handling, stacking or "
            "recycling as constraints the model omits.", "Give a specific example.", "R")],
    ),
    assessment=[
        dict(title="A1 · The water tank",
             text="A community needs a tank holding 10 m³ of water. Three designs are "
                  "proposed: a cube, a cylinder whose height equals its diameter, and a "
                  "sphere. Find the surface area of each, the mass of steel needed at 10 kg "
                  "per m², and the mass of the water each holds. Recommend one design and "
                  "justify the recommendation, stating at least one constraint your model "
                  "ignores.",
             note="Criteria A and D · compute all three designs, compare them, and justify the "
                  "recommendation."),
        dict(title="A2 · The packaging audit",
             text="A product of volume 500 cm³ is sold in a cuboid measuring 10 cm by 10 cm "
                  "by 5 cm. Find the surface area of the box, the surface area of the most "
                  "efficient cylinder of the same volume, and the material saved. Then "
                  "investigate the effect on the saving of allowing the cylinder to be twice "
                  "as tall as it is wide, and explain why a manufacturer might still choose "
                  "the cuboid.",
             note="Criteria B and C · use the volume constraint, minimise the surface area, "
                  "and justify the choice."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of space, measurement and "
        "quantity appear in your work?",
        "How is the global context of globalisation and sustainability, and its exploration of "
        "packaging, water storage and material efficiency, visible in the investigations and "
        "examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a material model for a design decision, and what would you "
        "still like to ask?",
    ],
    review=dict(
        ideas=["A prism's volume is the cross-section area times its length.",
               "A prism's surface area is twice the cross-section area plus the perimeter "
               "times the length.",
               "A cone or pyramid has one third the volume of the corresponding prism or "
               "cylinder.",
               "A cone's curved surface area is πrl, where l is the slant height.",
               "A sphere has volume (4/3)πr³ and surface area 4πr².",
               "Surface area scales as k² and volume as k³, so the ratio scales as 1/k.",
               "Mass = density × volume, and material mass = surface area × mass per area.",
               "The sphere encloses a given volume with least surface."],
        vocab=["prism", "cross-section", "cylinder", "cone", "pyramid", "sphere",
               "slant height", "density", "capacity", "surface-area-to-volume ratio",
               "isoperimetric", "efficient shape"],
        mixed=[("11.R1", "Find the volume and surface area of a cube of side 7 cm."),
               ("11.R2", "Find the volume of a cone of radius 4 cm and height 9 cm."),
               ("11.R3", "Find the surface area of a sphere of radius 3.5 cm."),
               ("11.R4", "Convert 0.75 litres to cubic centimetres."),
               ("11.R5", "Find the slant height of a cone of radius 8 cm and height 15 cm."),
               ("11.R6", "Explain why a large tank uses less material per litre than a small "
                         "one.")],
    ),
    projects=dict(
        service=[("Community need", "Water storage and packaging decisions are made without "
                                    "the material model."),
                 ("Mathematical connection", "Surface area, volume and efficiency."),
                 ("Proposed action", "Model the containers used for one community need and "
                                     "publish the material used by each."),
                 ("Expected impact", "A group can choose the design that wastes least."),
                 ("Student reflection", "Record the models, the comparison and the "
                                        "recommendation.")],
        community=[("Project idea", "A packaging audit of one product sold locally."),
                   ("Need", "Packaging is chosen by appearance and cost per unit, with no "
                            "account of material."),
                   ("Research question", "How much material does each design use, and what "
                                         "would the efficient shape use?"),
                   ("Mathematics", "Surface area, volume and ratios."),
                   ("Action or outcome", "A one-page comparison of three designs with the "
                                         "material used by each."),
                   ("Beneficiaries", "Everyone who buys and disposes of the packaging."),
                   ("Evidence", "The comparison with the models and the recommendation.")],
        personal=[("Personal interest", "A container, a box or a tank you use."),
                  ("Learning goal", "To model the material used by a container and find the "
                                    "efficient shape."),
                  ("Product or outcome", "A model with a comparison and a recommendation."),
                  ("Mathematics", "Surface area, volume and ratios."),
                  ("Process", "Measure a container, compute both quantities, and compare with "
                              "the efficient shape."),
                  ("Evidence", "The model, the comparison and the recommendation.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=12, title="Statistics: Distributions and Data",
    key="Relationships", related=["Statistics", "Representation", "Quantity"],
    context="Identities and relationships",
    exploration="How data about groups shape decisions about individuals",
    inquiry=("A data set is a collection of quantities that describe a group, and its "
             "distribution is a representation of how those quantities are spread; the "
             "average and the spread are two different statements about the same group, and a "
             "decision about an individual made from a group statistic is an inference whose "
             "strength depends on how the data were collected."),
    atl=("Information literacy",
         "Students evaluate the source, the sampling method and the presentation of a data "
         "set before using it, and state what the data can and cannot support."),
    standfirst="An average summarises a group; a spread says how typical that average is. "
               "The same numbers can be made to look very different by the choice of display.",
    engage="A school reports that its average class size is 24. Half the classes have 18 "
           "students and half have 30. Is the school's figure honest, and is it useful?",
    questions=[("Factual", "What are the mean, median, mode and range, and how are "
                           "cumulative frequency and box plots constructed?"),
               ("Conceptual", "Why does the choice of average matter, and how does a sampling "
                              "method affect what a conclusion can claim?"),
               ("Debatable", "Is it fair to make a decision about an individual from a "
                             "statistic about a group, and when does it become "
                             "discrimination?")],
    application_lede="Each task involves a data set. State the sampling method, the measure "
                     "you are using, and what the result can support.",
    projects_lede="Data about a group is used to make decisions about individuals. Collect "
                  "some, analyse it, and say what it does and does not justify.",
    sections=[
        dict(id="12.1", title="Collecting and classifying data",
             inquiry_q="How does the way data are collected affect what a conclusion can "
                       "claim?",
             teach=[
                 "Data are classified before they are displayed: a variable is categorical when its values are names and numerical when they are numbers, and a numerical variable is discrete when it is counted and continuous when it is measured.",
                 "Primary data are collected for the question in hand and secondary data were collected for another purpose, and the second kind often needs reclassifying before it can answer a new question.",
                 "A population is the whole group a claim is about, and a sample is the part that is measured. A conclusion about the population is an inference from the sample.",
                 "A random sample gives every member of the population the same chance of selection, and it is the only method that supports a claim about the population without bias.",
                 "A stratified sample takes each group in proportion to its share of the population, which guarantees that small groups are represented.",
                 "A biased sample supports no conclusion about the population, however large it is. Sample size reduces random error but cannot remove bias, and the two are different problems.",
             ],
             examples=[

                 dict(q="A school has 720 students in four year groups of 180, 200, 170 and "
                        "170. A stratified sample of 72 is to be taken. Find the number from "
                        "each group.",
                      vis=F("table", [["group", "population", "share", "sample"],
                                      ["Year 6", "180", "25%", "18"],
                                      ["Year 7", "200", "27.8%", "20"],
                                      ["Year 8", "170", "23.6%", "17"],
                                      ["Year 9", "170", "23.6%", "17"]],
                            caption="each group is sampled in proportion to its size"),
                      reasoning="Take the same fraction of each group as the sample is of the "
                               "population.",
                      steps=["The sampling fraction is 72/720 = 0.1.",
                             "Year 6 contributes 180 × 0.1 = 18 students.",
                             "Year 7 contributes 200 × 0.1 = 20 students.",
                             "Year 8 contributes 170 × 0.1 = 17 students.",
                             "Year 9 contributes 170 × 0.1 = 17 students, and the total is 72."],
                      ans="18, 20, 17 and 17 students",
                      interp="A stratified sample guarantees that every group appears in "
                             "proportion, which a simple random sample does not."),
                 dict(q="A survey of 200 people leaving a gym finds that 70% exercise three "
                        "times a week. Explain why this does not describe the town.",
                      vis=F("venn", "gym members", "town", "70%", "surveyed", "not surveyed"),
                      reasoning="Identify the population and the sampling frame, and decide "
                               "whether the sample represents the population.",
                      steps=["The population is the town, but the sample is drawn only from "
                             "people leaving a gym.",
                             "People leaving a gym are more likely to exercise than the "
                             "general population.",
                             "So the sample is biased, and the figure of 70% describes the "
                             "sample, not the town.",
                             "A larger sample of the same kind would not fix the bias.",
                             "A random sample of the town would be needed for a claim about "
                             "the town."],
                      ans="the sample is biased, so the figure describes gym users, not the "
                          "town",
                      interp="Bias is a property of how the sample was chosen, and no amount "
                             "of data from a biased sample removes it.")
             ],
             inv=dict(
                 task="Find two published surveys: one you trust and one you do not. For "
                      "each, identify the population, the sampling method, the sample size "
                      "and the claim made, and decide whether the claim is supported.",
                 table=[["survey", "population", "method", "supported?"],
                        ["national census", "everyone", "complete count", "yes"],
                        ["gym exit survey", "town", "convenience", "no"],
                        ["online poll", "voters", "self-selected", "no"],
                        ["school register", "students", "complete count", "yes"]],
                 notice=["The complete counts supported their claims exactly.",
                         "The convenience and self-selected samples did not.",
                         "Sample size was irrelevant where the method was biased.",
                         "The population and the sampling frame had to match for the claim to "
                         "hold."],
                 obs="A claim about a population is supported only when the sampling frame "
                     "matches the population and the selection is unbiased.",
                 concl="An inference from a sample to a population depends on the sampling "
                       "method, and a biased sample supports no conclusion about the "
                       "population however large it is.")),
        dict(id="12.2", title="Frequency distributions and histograms",
             inquiry_q="How does the choice of display change what a reader sees?",
             teach=[
                 "A frequency table groups data into classes, and the class width is the difference between the class boundaries. Equal widths make the heights of the bars directly comparable.",
                 "A histogram has frequency density on the vertical axis, where frequency density is frequency divided by class width, so the area of each bar represents the frequency. This is what makes the histogram suitable for unequal class widths.",
                 "Grouping loses information: the exact values are replaced by classes, and a class width that is too wide hides the shape while one that is too narrow makes the display noisy.",
                 "The shape of a histogram is a representation of the distribution, and the words used to describe it — symmetric, skewed, bimodal — are claims about the population as well as about the sample.",
             ],
             examples=[
dict(q="Draw a histogram for data grouped into classes of width 5 with "
                        "frequencies 4, 11, 20, 9, 3, and state the frequency density of the "
                        "tallest class.",
                      vis=F("bar_chart", ["0-5", "5-10", "10-15", "15-20", "20-25"],
                            [0.8, 2.2, 4.0, 1.8, 0.6],
                            "frequency density, because the classes are equal"),
                      reasoning="Divide each frequency by the class width to get the frequency "
                               "density.",
                      steps=["The class width is 5 for every class.",
                             "The frequency densities are 4/5, 11/5, 20/5, 9/5 and 3/5.",
                             "That is 0.8, 2.2, 4.0, 1.8 and 0.6.",
                             "The tallest class has density 4.0, and its area is 4.0 × 5 = 20, "
                             "the frequency.",
                             "The total area is 47, the total frequency."],
                      ans="frequency densities 0.8, 2.2, 4.0, 1.8, 0.6",
                      interp="With equal class widths the shape of the histogram is the same "
                             "whether the axis is frequency or frequency density, and only the "
                             "scale changes."),
             ], inv=dict(
                 task="Collect one set of continuous data with at least 30 values: heights, "
                      "times or masses. Group it into classes of equal width, draw a frequency "
                      "table with a frequency density column, and draw the histogram. Then "
                      "regroup the same data into unequal classes and draw the histogram "
                      "again, and say which display shows the shape more clearly.",
                 table=[["class", "frequency", "width", "frequency density"],
                        ["10 ≤ t < 20", "6", "10", "0.6"],
                        ["20 ≤ t < 30", "14", "10", "1.4"],
                        ["30 ≤ t < 40", "9", "10", "0.9"],
                        ["40 ≤ t < 60", "5", "20", "0.25"],
                        ["60 ≤ t < 80", "2", "20", "0.1"]],
                 notice=["The frequency density column was needed because the last two "
                         "classes were twice as wide.",
                         "With equal classes the bar heights and the frequencies told the "
                         "same story.",
                         "With unequal classes the heights alone were misleading, and only "
                         "the areas were correct.",
                         "The narrower classes showed a bumpier shape than the wider ones."],
                 obs="A histogram draws frequency density rather than frequency, so the area "
                     "of each bar is the frequency and unequal classes can be used.",
                 concl="Grouping data into classes is the first step of a display, and the "
                       "histogram's use of density is what allows classes of different "
                       "widths to appear on one pair of axes.")),
        dict(id="12.3", title="Cumulative frequency and box plots",
             inquiry_q="How is a cumulative frequency diagram built, and what does a box plot "
                       "add to it?",
             teach=[
                 "A cumulative frequency diagram plots the running total of frequencies against the upper class boundary, so the height at any value is the number of observations at or below it.",
                 "The gradient of a cumulative frequency diagram is the frequency density, so a steep part of the curve is a class with many observations and a flat part is a class with few.",
                 "The median, the lower quartile and the upper quartile are read from the diagram at the half, the quarter and the three-quarter points of the total frequency, which is why the total must be known before the diagram can be read.",
                 "A box plot shows the minimum, the lower quartile, the median, the upper quartile and the maximum in one compact picture, and it is the best display for comparing several distributions on the same axis.",
                 "A value more than 1.5 interquartile ranges beyond a quartile is usually marked as an outlier, and an outlier is a value that deserves a second look rather than automatic deletion.",
             ], examples=[
                 dict(q="A cumulative frequency diagram gives 24 at 20, 58 at 30 and 74 at 40, "
                        "for a total of 100 observations. Estimate the median and the "
                        "interquartile range.",
                      vis=F("box_plot", 12, 22, 27, 34, 48,
                            "the same data as a box plot"),
                      reasoning="Read the diagram at the half, quarter and three-quarter "
                               "points of the total.",
                      steps=["The total frequency is 100, so the median is at 50.",
                             "Reading across from 50 gives about 27.",
                             "The lower quartile is at 25, which gives about 22.",
                             "The upper quartile is at 75, which gives about 35.",
                             "So the interquartile range is about 35 − 22 = 13."],
                      ans="median about 27, interquartile range about 13",
                      interp="The quartiles are read from the cumulative total, so the total "
                             "frequency must be known before the diagram can be interpreted."),
                 dict(q="Two classes take the same test. Class A has median 62, lower "
                        "quartile 54 and upper quartile 70; class B has median 60, lower "
                        "quartile 48 and upper quartile 72. Compare the two distributions.",
                      vis=F("box_plot", 48, 54, 62, 70, 78, "class A and class B"),
                      reasoning="Compare the centres and the spreads separately, and say "
                               "which is larger.",
                      steps=["The medians are 62 and 60, so the centres are close.",
                             "The interquartile ranges are 16 and 24, so class B is more "
                             "spread.",
                             "Class B's lower quartile is lower and its upper quartile higher.",
                             "So class B contains both weaker and stronger students.",
                             "A comparison must mention both the centre and the spread, "
                             "because either alone is incomplete."],
                      ans="the centres are similar; class B is more spread out",
                      interp="A box plot makes a comparison of two distributions a matter of "
                             "reading two pictures, which is why it is preferred for "
                             "comparison."),
             ], inv=dict(
                 task="Take the data set you grouped in the previous investigation. Draw a "
                      "cumulative frequency diagram, read the median and the quartiles from "
                      "it, and then draw a box plot on the same axis as a box plot for a "
                      "second data set of your own. Compare the two distributions in terms of "
                      "centre, spread and shape, and mark any value that lies more than 1.5 "
                      "interquartile ranges beyond a quartile.",
                 table=[["quantity", "data set 1", "data set 2"],
                        ["minimum", "12", "20"],
                        ["lower quartile", "22", "31"],
                        ["median", "27", "38"],
                        ["upper quartile", "35", "47"],
                        ["maximum", "48", "60"],
                        ["interquartile range", "13", "16"]],
                 notice=["The quartiles read from the diagram matched those from the ordered "
                         "data.",
                         "The second data set was shifted upwards but had a similar spread.",
                         "The box plots made the shift visible at a glance.",
                         "No value lay far enough beyond a quartile to be marked as an "
                         "outlier."],
                 obs="A cumulative frequency diagram gives the quartiles directly, and a box "
                     "plot is the compact picture of the same five values.",
                 concl="The cumulative diagram and the box plot are two representations of "
                       "the same five-number summary, and the box plot is the one that "
                       "supports comparison.")),
        dict(id="12.4", title="Spread, outliers and robust measures",
             inquiry_q="Why does the choice of average matter, and what does spread add?",
             teach=[
                 "The mean is the sum of the values divided by how many there are, and it uses every value. The median is the middle value when they are ordered, and the mode is the most frequent.",
                 "The mean is pulled by extreme values and the median is not, so a skewed distribution has a mean above or below its median. Reporting only one of them can mislead.",
                 "The range is the difference between the largest and smallest values, and the interquartile range is the difference between the upper and lower quartiles. The range is sensitive to one extreme value; the interquartile range is not.",
                 "A measure of spread is what makes an average meaningful. Two classes with the same mean can be very different, and the spread is what says so.",
                 "A relationship between two variables is what a scatter diagram looks for, and the strength of that relationship is a quantity that can be measured.",
             ], examples=[
                 dict(q="A factory pays 9 workers 400 dollars a week and the owner 4000. "
                        "Find the mean and the median, and say which better describes a "
                        "typical worker's pay.",
                      vis=F("bar_chart", ["9 workers", "owner"], [400, 4000],
                            "one very large value among ten"),
                      reasoning="Compute both averages and compare their resistance to the "
                               "extreme value.",
                      steps=["The total pay is 9 × 400 + 4000 = 7600 dollars.",
                             "So the mean is 7600/10 = 760 dollars.",
                             "Ordering the values puts the median between the fifth and sixth, "
                             "both of which are 400 dollars.",
                             "So the median is 400 dollars, which is what a typical worker "
                             "actually earns.",
                             "The mean is pulled up by the owner's pay, so it describes the "
                             "payroll, not the workers."],
                      ans="mean 760 dollars, median 400 dollars; the median describes a "
                          "typical worker",
                      interp="A single extreme value changed the mean by 90% and left the "
                             "median unchanged, which is why the choice of average is a "
                             "decision about what to describe."),
                 dict(q="Two classes have mean test scores of 65. Class A has scores 60, 62, "
                        "65, 68, 70 and class B has 40, 55, 65, 75, 90. Compare their spreads.",
                      vis=F("box_plot", 40, 55, 65, 75, 90, "class B, the wider spread"),
                      reasoning="Compute the range and the interquartile range for each.",
                      steps=["Class A has range 70 − 60 = 10 and interquartile range 68 − 62 "
                             "= 6.",
                             "Class B has range 90 − 40 = 50 and interquartile range 75 − 55 "
                             "= 20.",
                             "Both classes have the same mean of 65.",
                             "Class B is far more spread, so its mean is less typical of any "
                             "individual.",
                             "The same mean with a larger spread means the average describes "
                             "fewer of the students."],
                      ans="class A: range 10, interquartile range 6; class B: range 50, "
                          "interquartile range 20",
                      interp="Two groups with the same average can be very different, and only "
                             "the spread reveals the difference."),
             ], inv=dict(
                 task="Collect two data sets from your own life: one with an extreme value "
                      "and one without. For each, compute the mean, the median, the mode, the "
                      "range and the interquartile range, and say which average you would "
                      "report and why.",
                 table=[["data set", "mean", "median", "range", "interquartile range"],
                        ["weekly spending", "42.50", "35.00", "80", "20"],
                        ["daily steps", "8200", "8100", "3000", "1800"]],
                 notice=["The spending data had one large value that raised the mean above the "
                         "median.",
                         "The steps data was nearly symmetric, so the mean and median were "
                         "close.",
                         "The interquartile range was much smaller than the range in both "
                         "cases.",
                         "The choice of average followed the shape of the distribution."],
                 obs="The mean and the median agree for a symmetric distribution and diverge "
                     "for a skewed one, and the spread decides how typical either average is.",
                 concl="An average is a summary of a group whose usefulness depends on the "
                       "spread, and the choice between the mean and the median is decided by "
                       "the shape of the distribution.")),
        dict(id="12.5", title="Comparing distributions and interpreting critically",
             inquiry_q="How is a statistic used to make a decision, and what does it cost the "
                       "individual?",
             teach=[
                 "A decision about an individual made from a group statistic is an inference, and it can be right for the group and wrong for the person.",
                 "A statistic about a group says nothing certain about any member of it, because the spread means individuals differ from the average.",
                 "Using group statistics to allocate resources is efficient; using them to judge individuals is unfair, and the difference is the difference between planning and discrimination.",
                 "A statistic can be presented to support a conclusion it does not support, and the reader's defence is to ask how the data were collected and what the spread was.",
             ], examples=[
                 dict(q="An insurer charges young drivers more because the average claim for "
                        "under-25s is higher. A careful 20-year-old driver objects. Discuss "
                        "the mathematics and the fairness.",
                      vis=F("box_plot", 200, 450, 700, 1200, 3000, "claims for under-25s, a "
                            "wide spread"),
                      reasoning="Identify what the statistic says about the group and what it "
                               "does not say about the individual.",
                      steps=["The group statistic is the average claim for under-25s.",
                             "The spread is wide, so many young drivers claim far less than "
                             "the average.",
                             "The statistic is true of the group and says nothing certain "
                             "about this driver.",
                             "Charging by group is efficient for the insurer and unfair to "
                             "the careful driver.",
                             "The mathematics supports the group claim, and the fairness "
                             "question is not a mathematical one."],
                      ans="the statistic is true of the group and silent about the individual",
                      interp="A group average is a planning tool, and using it to judge a "
                             "person confuses efficiency with fairness."),
                 dict(q="A hospital reports that a treatment succeeds in 80% of cases. A "
                        "patient asks what this means for them. Answer using the spread.",
                      vis=F("bar_chart", ["success", "failure"], [80, 20],
                            "four successes in five"),
                      reasoning="State what the percentage says and what it does not.",
                      steps=["The figure means that in the group treated, 80% had a "
                             "successful outcome.",
                             "It does not mean this patient has an 80% chance, because "
                             "outcomes depend on age, stage and other conditions.",
                             "The spread of outcomes across subgroups is not given by the "
                             "single figure.",
                             "A more useful statement would give the rate for patients like "
                             "this one.",
                             "The honest answer is that the figure describes the group, not "
                             "the person."],
                      ans="the figure describes the group; the patient's own chance depends "
                          "on their subgroup",
                      interp="A percentage without its subgroups is a statement about a group, "
                             "and a patient needs the figure for their own subgroup."),
             ], inv=dict(
                 task="Find one real decision made from a statistic about a group: an "
                      "insurance premium, a school place, a medical treatment or a loan. "
                      "Model the group statistic and its spread, and write an account of what "
                      "the statistic justifies and what it does not.",
                 table=[["decision", "group statistic", "spread", "justifies"],
                        ["car insurance", "average claim by age", "very wide",
                         "a group premium"],
                        ["school places", "average test score by area", "wide",
                         "a group prediction"],
                        ["medical treatment", "success rate overall", "narrow for some, wide "
                         "for others", "a group recommendation"]],
                 notice=["Every decision was efficient for the group.",
                         "Every spread was wide enough that many individuals differed from "
                         "the average.",
                         "The statistic justified a group decision but not a judgement about "
                         "a person.",
                         "A figure for the relevant subgroup would have been more useful to "
                         "the individual."],
                 obs="A group statistic supports a decision about the group, and its spread is "
                     "what limits what it can say about any individual member.",
                 concl="A statistic about a group is used to plan for the group, and using it "
                       "to judge an individual is an inference whose strength is limited by "
                       "the spread of the group.")),
        dict(id="12.6", title="Investigation: is the school day too long?",
             inquiry_q="How can the same data support different conclusions, and what should "
                       "a reader check?",
             teach=[
                 "The same data can be presented to support different conclusions by choosing different averages, different classes, different scales or different subsets.",
                 "A reader's defence is to ask four questions: how were the data collected, what is the spread, what is the scale of the display, and what conclusion does the display actually support?",
                 "A display with a truncated vertical axis exaggerates a small difference, and a display with unequal class widths distorts a shape unless frequency density is used.",
                 "Honest reporting states the sampling method, the spread and the limitations, and a report that omits them is not neutral even if every number in it is true.",
             ], examples=[
                 dict(q="A class's scores are 48, 52, 55, 60, 62, 68, 90. Show how three "
                        "different summaries describe the class.",
                      vis=F("box_plot", 48, 55, 60, 68, 90, "the same class, three summaries"),
                      reasoning="Compute three different averages and compare what each "
                               "emphasises.",
                      steps=["The mean is (48 + 52 + 55 + 60 + 62 + 68 + 90)/7 = 435/7 ≈ "
                             "62.1.",
                             "The median is the fourth value, 60.",
                             "The mode does not exist, since no value repeats.",
                             "The range is 90 − 48 = 42, which is large compared with the "
                             "mean.",
                             "So 'the class averages 62' and 'half the class scored 60 or "
                             "below' are both true and sound different."],
                      ans="mean about 62.1, median 60, no mode, range 42",
                      interp="Two true statements about the same data can give different "
                             "impressions, and the spread is what reconciles them."),
                 dict(q="A bar chart of a school's results starts its vertical axis at 90% "
                        "rather than 0%. Explain the effect on a reader.",
                      vis=F("bar_chart", ["2019", "2020", "2021"], [90, 92, 95],
                            "a truncated axis exaggerates the change"),
                      reasoning="Compare the visual impression with the actual change.",
                      steps=["The axis runs from 90% to 95%, so the bars have very different "
                             "heights.",
                             "The change from 90% to 95% is 5 percentage points, or about 6% "
                             "relative.",
                             "Visually the last bar looks twice as tall as the first.",
                             "So the display exaggerates a real but modest improvement.",
                             "An axis starting at zero would show the bars as nearly equal."],
                      ans="the display exaggerates a 5-point change into a visual doubling",
                      interp="A truncated axis is not a lie, because every number is correct, "
                             "but it misleads by changing the visual proportions."),
             ], inv=dict(
                 task="Take one data set and present it three ways to support three different "
                      "conclusions, using only true numbers. Then write the four questions a "
                      "reader should ask, and answer them for your own presentations.",
                 table=[["presentation", "choice made", "impression created"],
                        ["mean only", "mean 62.1", "the class does well"],
                        ["median and range", "median 60, range 42", "the class is very "
                         "mixed"],
                        ["box plot", "quartiles and outlier", "one student is far ahead"]],
                 notice=["All three presentations used true numbers.",
                         "Each created a different impression of the same class.",
                         "The choice of average did most of the work.",
                         "The four questions exposed the manipulation in every case."],
                 obs="The same data support different conclusions according to the choices "
                     "made in summarising and displaying them, and those choices are rarely "
                     "stated.",
                 concl="A reader of a statistic should ask how the data were collected, what "
                       "the spread was, what the display's scale is, and what conclusion the "
                       "display actually supports.")),
    ],
    practice=dict(
        A=[("12.1.1", "Find the mean of 4, 7, 9, 12, 18.", "10",
            "Divide the sum by the number of values.", "F"),
           ("12.1.2", "Find the median of 3, 8, 12, 15, 19, 24.", "13.5",
            "Average the two middle values.", "F"),
           ("12.1.3", "Find the mode of 5, 6, 6, 7, 8, 8, 8, 9.", "8",
            "The most frequent value.", "F"),
           ("12.1.4", "Find the range of 12, 15, 19, 24, 30.", "18",
            "Largest minus smallest.", "F"),
           ("12.1.5", "Find the median of 2, 5, 8, 11, 14, 17, 20.", "11",
            "The middle value of seven ordered values.", "F"),
           ("12.1.6", "A data set has mean 20 for 6 values. Find the total.", "120",
            "Mean times the number of values.", "F"),
           ("12.1.7", "Find the upper quartile of 1, 3, 5, 7, 9, 11, 13, 15.", "11",
            "The median of the upper half.", "F"),
           ("12.1.8", "Find the interquartile range of 2, 4, 6, 8, 10, 12, 14, 16.", "8",
            "Upper quartile minus lower quartile.", "F"),
           ("12.1.9", "A sample of 50 is taken from 500. Find the sampling fraction.", "0.1",
            "50 divided by 500.", "F"),
           ("12.1.10", "A stratified sample of 40 is taken from groups of 60, 100 and 140. "
            "Find the number from the largest group.", "20",
            "140/300 × 40.", "F"),
           ("12.1.11", "A histogram class has frequency 18 and width 6. Find the frequency "
            "density.", "3", "Frequency divided by class width.", "F"),
           ("12.1.12", "A cumulative frequency reaches 45 at a value of 20. Estimate the "
            "median if the total is 90.", "20",
            "The median is at half the total frequency.", "F")],
        B=[("12.2.1", "The mean of five numbers is 12. Four of them are 9, 11, 14, 16. Find "
            "the fifth and justify.",
            "10, because the total is 60 and the others sum to 50.", "Use the mean formula.",
            "R"),
           ("12.2.2", "Investigate the effect on the mean and median of adding one very "
            "large value to a symmetric data set.",
            "The mean moves towards the large value and the median moves only slightly.",
            "Compute both before and after.", "R"),
           ("12.2.3", "Conjecture a rule for the median of an even number of ordered values "
            "and test it.",
            "The average of the two middle values.", "Order and take the middle pair.", "R"),
           ("12.2.4", "Investigate the pattern in the interquartile range of the first n "
            "positive integers.",
            "About n/2, because the quartiles are at n/4 and 3n/4.",
            "Compute for several n.", "R"),
           ("12.2.5", "Build a table of the mean, median and range of the squares of the "
            "first n integers and describe the pattern.",
            "The mean grows as n²/3 and the range as n² − 1.",
            "Compute for n = 2 to 6.", "R"),
           ("12.2.6", "Conjecture a rule for the number of students in a stratified sample "
            "from a group of size g in a population of N, for a sample of size n.",
            "ng/N, the group's share of the population times the sample size.",
            "Use the sampling fraction.", "R"),
           ("12.2.7", "Investigate the effect of class width on the shape of a histogram of "
            "the same data.",
            "Wider classes give a smoother but less detailed histogram; the area always "
            "represents the frequency.", "Redraw at two widths.", "R"),
           ("12.2.8", "A data set has mean 50 and standard deviation 5. Investigate how many "
            "values lie within 10 of the mean for a bell-shaped set.",
            "About 95%, by the empirical rule.", "Compare with a normal distribution.", "C"),
           ("12.2.9", "Find the pattern in the cumulative frequencies of a data set and "
            "explain why the diagram rises.",
            "The running total never falls, so the diagram rises monotonically.",
            "Compute the running total.", "R"),
           ("12.2.10", "Investigate the effect of removing the largest value on the mean, "
            "median and range of a data set.",
            "The mean falls, the median may not change, and the range falls.",
            "Compute all three before and after.", "R"),
           ("12.2.11", "Conjecture a rule for the sample size needed to halve the margin of "
            "error of a survey.",
            "Four times the size, because the error is proportional to 1/√n.",
            "Compare the errors at two sizes.", "C")],
        C=[("12.3.1", "Explain in your own words the difference between the mean and the "
            "median.", "The mean uses every value and is pulled by extremes; the median is "
            "the middle value and is not.", "State both definitions.", "R"),
           ("12.3.2", "Write a complete solution to: find the mean, median and range of "
            "12, 15, 18, 22, 90.",
            "Mean 31.4, median 18, range 78.", "Compute each measure.", "F"),
           ("12.3.3", "Choose between the mean and the median to summarise house prices and "
            "justify.", "The median, because a few very expensive houses pull the mean above "
            "what a typical house costs.", "Say what each resists.", "R"),
           ("12.3.4", "Set out a full solution to: a stratified sample of 60 is taken from "
            "groups of 120, 180 and 300.",
            "12, 18 and 30 students.", "Use the sampling fraction.", "F"),
           ("12.3.5", "Explain why the range is a poor measure of spread.",
            "Because it depends only on the two extreme values, so one outlier makes it "
            "large however typical the rest are.", "Give an example.", "R"),
           ("12.3.6", "Describe, with an example, the difference between a histogram and a "
            "bar chart.", "A histogram has frequency density on the vertical axis and "
            "represents frequency by area; a bar chart has frequency and a gap between bars.",
            "Compare the axes.", "R"),
           ("12.3.7", "Explain why a biased sample cannot support a conclusion about the "
            "population.",
            "Because the sample does not represent the population, so its statistics describe "
            "the sample and not the population.", "Give an example.", "R"),
           ("12.3.8", "Write the reasoning that shows a larger sample reduces random error "
            "but not bias.", "Random error falls as 1/√n, but bias comes from the selection "
            "method and is unchanged by taking more of the same kind of sample.",
            "Compare the two effects.", "R"),
           ("12.3.9", "Set out the argument that a stratified sample represents small "
            "groups.", "Because each group is sampled in proportion to its share, every group "
            "appears in the sample, which a simple random sample does not guarantee.",
            "Use the sampling fraction.", "R"),
           ("12.3.10", "Explain what a cumulative frequency diagram shows and how the median "
            "is read from it.",
            "The running total against the upper class boundary; the median is read at half "
            "the total frequency.", "State the method.", "R"),
           ("12.3.11", "Describe the relationship between a box plot and the five-number "
            "summary.", "The box plot is a picture of the minimum, lower quartile, median, "
            "upper quartile and maximum.", "List the five numbers.", "R"),
           ("12.3.12", "Explain, with an example, when a statistic about a group is used "
            "unfairly.",
            "Any answer is acceptable if it identifies a judgement about an individual made "
            "from a group average with a wide spread.", "Give a specific example.", "R")],
        D=[("12.4.1", "A class of 25 has mean score 68. One student transfers in with a "
            "score of 92. Find the new mean and comment on the change.",
            "The new mean is 68.96, a rise of about 1.", "Use the total.", "A"),
           ("12.4.2", "A survey samples 1 in 20 of a town of 24000. Find the sample size, "
            "and find the number from a district of 3600.",
            "1200 in total, and 180 from the district.", "Use the sampling fraction.", "A"),
           ("12.4.3", "A histogram has classes of width 10 with frequency densities 1.2, "
            "3.5, 4.8 and 2.1. Find the total frequency and the frequency of the largest "
            "class.", "Total 116; the largest class has 48.", "Multiply density by width.",
            "A"),
           ("12.4.4", "A company's staff salaries are 20000, 22000, 24000, 26000, 28000 and "
            "120000. Find the mean and median and recommend which to publish.",
            "Mean 40000, median 25000; the median is fairer to publish.",
            "Compute both and compare.", "A"),
           ("12.4.5", "A hospital reports a 90% success rate overall, but 70% for one "
            "subgroup. Investigate what a patient in that subgroup should be told.",
            "The subgroup rate of 70%, because the overall figure hides the difference.",
            "Compare the subgroup with the whole.", "R"),
           ("12.4.6", "A school takes a stratified sample of 80 from year groups of 150, "
            "170, 160 and 220. Find the number from each and comment on the fairness.",
            "24, 27.2, 25.6 and 35.2, so about 24, 27, 26 and 35.",
            "Use the sampling fraction and round.", "A"),
           ("12.4.7", "A poll of 400 people finds 52% support. Find the margin of error at "
            "the 95% level and state what it means.",
            "About ±5%, so the true support is likely between 47% and 57%.",
            "Use 1/√n for the approximate error.", "R"),
           ("12.4.8", "Two classes have the same mean but interquartile ranges of 6 and 20. "
            "Investigate which class a new student should join and justify.",
            "Either is defensible; the smaller range means more predictable teaching, the "
            "larger means more variety.", "Compare the spreads.", "R"),
           ("12.4.9", "A shop's daily takings for a week are 420, 380, 510, 390, 460, 900, "
            "350. Investigate the mean and median and say which describes a typical day.",
            "Mean 487, median 420; the median, because Saturday is exceptional.",
            "Compute both.", "R"),
           ("12.4.10", "A charity surveys its own donors about need in a district. "
            "Investigate whether the results describe the district and justify.",
            "No: donors are a self-selected group with an interest, so the sample is biased.",
            "Compare the sampling frame with the population.", "R"),
           ("12.4.11", "A test has mean 60 and the top score is 98. Investigate whether a "
            "student scoring 75 is above average and what else is needed.",
            "Yes, 75 is above the mean, but the spread is needed to say how unusual it is.",
            "Ask for the standard deviation or the quartiles.", "R"),
           ("12.4.12", "Explain, with a survey of your own, when a reported average is "
            "misleading.",
            "Any answer is acceptable if it identifies a skewed distribution, a biased "
            "sample, or a truncated display axis.", "Give a specific example.", "R")],
    ),
    assessment=[
        dict(title="A1 · The school report",
             text="A school reports that its students' reading ages have a mean of 10.4 "
                  "years and a range of 6 years. A parent asks whether her child, with a "
                  "reading age of 8, is behind. Using the mean, the median and the spread, "
                  "explain what the school's figures do and do not support, and state what "
                  "additional information would be needed to answer the parent's question.",
             note="Criteria C and D · use the measures of average and spread, and justify "
                  "what the data can support."),
        dict(title="A2 · The survey",
             text="A town of 36000 people is divided into four districts of 9000, 12000, "
                  "8000 and 7000. A stratified sample of 180 is to be taken to estimate the "
                  "proportion who use the library. Find the number from each district, "
                  "explain why a simple random sample might miss a district entirely, and "
                  "state the margin of error of the estimate.",
             note="Criteria A and B · use the sampling fraction, justify the method, and "
                  "estimate the error."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of statistics, "
        "representation and quantity appear in your work?",
        "How is the global context of identities and relationships, and its exploration of how "
        "data about groups shape decisions about individuals, visible in the investigations and "
        "examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a statistic for a decision about one person, and what would "
        "you still like to ask?",
    ],
    review=dict(
        ideas=["The mean uses every value; the median and mode do not.",
               "The mean is pulled by extremes and the median is not.",
               "The range is sensitive to one extreme value; the interquartile range is not.",
               "A histogram uses frequency density so that area represents frequency.",
               "A cumulative frequency diagram gives the quartiles by reading at fractions of "
               "the total.",
               "A box plot displays the five-number summary.",
               "A stratified sample takes each group in proportion to its share.",
               "A biased sample supports no conclusion about the population."],
        vocab=["population", "sample", "mean", "median", "mode", "range",
               "interquartile range", "class width", "frequency density", "histogram",
               "cumulative frequency", "stratified sample"],
        mixed=[("12.R1", "Find the mean and median of 6, 9, 11, 14, 21."),
               ("12.R2", "Find the range and interquartile range of 3, 5, 8, 12, 15, 18, 20."),
               ("12.R3", "A class has frequency 24 and width 8. Find the frequency density."),
               ("12.R4", "A stratified sample of 50 is taken from groups of 200 and 300. Find "
                         "the numbers."),
               ("12.R5", "A cumulative frequency reaches 30 at a value of 15. Estimate the "
                         "median if the total is 60."),
               ("12.R6", "Explain why a survey of a gym's members cannot describe a town.")],
    ),
    projects=dict(
        service=[("Community need", "Decisions about individuals are made from group "
                                    "statistics without the spread."),
                 ("Mathematical connection", "Averages, spread and sampling."),
                 ("Proposed action", "Collect one set of data about a community need and "
                                     "publish it with its spread and sampling method."),
                 ("Expected impact", "A reader can tell what the figures do and do not "
                                     "support."),
                 ("Student reflection", "Record the data, the method and the limits.")],
        community=[("Project idea", "A data audit of one figure the school publishes."),
                   ("Need", "Averages are reported without their spread or their sampling "
                            "method."),
                   ("Research question", "What does the school's own figure actually "
                                         "support, and what is missing?"),
                   ("Mathematics", "Averages, spread, displays and sampling."),
                   ("Action or outcome", "A one-page report with the figure, its spread and "
                                         "its limits."),
                   ("Beneficiaries", "Everyone who relies on the figure."),
                   ("Evidence", "The report with the data and the method.")],
        personal=[("Personal interest", "A sport, a game or a hobby with scores."),
                  ("Learning goal", "To collect data about something you enjoy and report it "
                                    "honestly."),
                  ("Product or outcome", "A data report with averages, spread and a display."),
                  ("Mathematics", "Averages, spread and displays."),
                  ("Process", "Collect at least 30 values, compute the measures, and display "
                              "the distribution."),
                  ("Evidence", "The data, the measures and the display.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=13, title="Probability: Combined Events",
    key="Logic", related=["Probability", "Equivalence", "Systems"],
    context="Fairness and development",
    exploration="How chance, risk and rules shape opportunities",
    inquiry=("The probability of a combined event is built from the probabilities of its "
             "parts by the addition and multiplication laws, and the equivalence between a "
             "sample space, a Venn diagram and a tree diagram means the same result can be "
             "reached by three routes; a game is fair only when the probabilities of its "
             "outcomes match the rewards attached to them."),
    atl=("Critical thinking",
         "Students test a probability claim by two independent methods, and identify the "
         "assumption of independence before applying the multiplication law."),
    standfirst="Mutually exclusive events add. Independent events multiply. The two laws "
               "build every combined probability, and the sample space is what checks them.",
    engage="Two players throw two fair dice. Player A wins if the first die is even and the "
           "second odd. Player B wins if both dice show the same number and that number is 1 "
           "or 6. What is the probability that neither player wins?",
    questions=[("Factual", "What are the addition and multiplication laws, and how is a tree "
                           "diagram used?"),
               ("Conceptual", "Why does the probability of 'A and B' depend on whether the "
                              "events are independent, and how does a Venn diagram show the "
                              "same information as a tree?"),
               ("Debatable", "If a game's probabilities are known to both players, can it "
                             "still be unfair, and who is responsible for making the rules "
                             "fair?")],
    application_lede="Each task involves combined events. Draw the sample space or the tree, "
                     "state whether the events are independent, and justify the law you use.",
    projects_lede="Chance and rules shape who gets an opportunity. Model one real "
                  "randomised process and say whether it is fair.",
    sections=[
        dict(id="13.1", title="Sample spaces and probability rules",
             inquiry_q="How is the probability of an event defined, and how is a sample space "
                       "listed?",
             teach=[
                 "The sample space is the set of all equally likely outcomes, and the probability of an event is the number of favourable outcomes divided by the total number of outcomes.",
                 "Probabilities lie between 0 and 1, and the probabilities of all outcomes sum to 1. The complement of an event A has probability 1 − P(A).",
                 "An event and its complement exhaust the sample space, so 'not A' is often easier to count than A, and the two must always give answers that sum to 1.",
                 "Two events are mutually exclusive when they cannot both happen, in which case they have no outcomes in common and their probabilities add.",
             
                 "The addition law says that for any two events P(A or B) = P(A) + P(B) − P(A and B), and the subtraction removes the outcomes counted twice. When the events are mutually exclusive the overlap is empty and the probabilities simply add.",
             ],
             examples=[

                 dict(q="A fair die is thrown. Find the probability that the score is even, "
                        "prime, greater than 4, and not prime.",
                      vis=F("table", [["event", "favourable outcomes", "probability"],
                                      ["even", "2, 4, 6", "3/6 = 1/2"],
                                      ["prime", "2, 3, 5", "3/6 = 1/2"],
                                      ["greater than 4", "5, 6", "2/6 = 1/3"],
                                      ["not prime", "1, 4, 6", "3/6 = 1/2"]],
                            caption="each event is a subset of the same sample space"),
                      reasoning="Count the favourable outcomes in the sample space of six "
                               "equally likely results.",
                      steps=["The sample space is {1, 2, 3, 4, 5, 6}.",
                             "Even scores are 2, 4 and 6, so the probability is 3/6 = 1/2.",
                             "Prime scores are 2, 3 and 5, so the probability is 3/6 = 1/2.",
                             "Scores greater than 4 are 5 and 6, so the probability is 2/6 = "
                             "1/3.",
                             "Not prime means 1, 4 and 6, so the probability is 3/6 = 1/2, "
                             "which is 1 − 1/2 as the complement rule requires."],
                      ans="even 1/2, prime 1/2, greater than 4 is 1/3, not prime 1/2",
                      interp="Every probability is a count out of the sample space, and the "
                             "complement rule is a check on the counting."),
                 dict(q="Two fair dice are thrown. Find the probability that the sum is 7.",
                      vis=F("grid", [], [], 1, 7, 1, 7, [(1, 6), (2, 5), (3, 4), (4, 3),
                                                          (5, 2), (6, 1)],
                            "the six outcomes with sum 7"),
                      reasoning="List the sample space of 36 equally likely ordered pairs and "
                               "count the favourable ones.",
                      steps=["The sample space has 6 × 6 = 36 equally likely outcomes.",
                             "The pairs with sum 7 are (1,6), (2,5), (3,4), (4,3), (5,2) and "
                             "(6,1).",
                             "That is 6 outcomes, so the probability is 6/36 = 1/6.",
                             "Seven is the most likely sum, with six ways out of thirty-six.",
                             "The order matters, so (2,5) and (5,2) are different outcomes."],
                      ans="1/6",
                      interp="A grid of 36 outcomes makes the counting visible, and the "
                             "symmetry about the diagonal is a check on the list.")
             ],
             inv=dict(
                 task="List the sample spaces of four experiments: one die, two dice, a coin "
                      "and a die together, and a spinner with unequal sectors. For each, find "
                      "the probability of two events of your own and check that the "
                      "probabilities sum to 1.",
                 table=[["experiment", "outcomes", "event", "probability"],
                        ["one die", "6", "even", "1/2"],
                        ["two dice", "36", "sum 7", "1/6"],
                        ["coin and die", "12", "heads and even", "1/4"],
                        ["spinner 1,2,3,4,6", "5", "prime", "3/5"]],
                 notice=["Every probability was a count out of a listed sample space.",
                         "The coin-and-die space had 12 outcomes, not 8, because the two "
                         "experiments are independent.",
                         "The unequal spinner was the only space in which the outcomes were "
                         "not equally likely.",
                         "The probabilities of each event and its complement always summed to "
                         "1."],
                 obs="A probability is a proportion of a listed sample space, and the "
                     "requirement of equally likely outcomes is what makes counting valid.",
                 concl="The probability of an event is the number of favourable equally likely "
                       "outcomes divided by the total, and every event has a complement whose "
                       "probability completes the sum to 1.")),
        dict(id="13.2", title="Two-way tables and Venn diagrams",
             inquiry_q="How do a two-way table and a Venn diagram each organise two events, "
                       "and what can be read from each?",
             teach=[
                 "A two-way table cross-classifies a sample by two variables, so each cell counts the members with one value of each, and the totals around the edge give the marginal counts.",
                 "A conditional probability is read from a two-way table by dividing a cell by the total of its row or column, which is the same as restricting the sample space to the given event.",
                 "A Venn diagram draws the sample space as a rectangle and the events as overlapping regions, so the overlap is the intersection, the union is everything covered, and the outside is the complement.",
                 "The addition law P(A or B) = P(A) + P(B) − P(A and B) subtracts the overlap because it has been counted twice, and a Venn diagram shows why the subtraction is needed.",
                 "Two representations of the same data answer different questions quickly: a table gives counts exactly and a Venn diagram shows the logical relations at a glance.",
             ], examples=[
                 dict(q="In a class of 30, 18 study French, 14 study Spanish and 6 study both. "
                        "How many study neither, and what is the probability that a student "
                        "chosen at random studies exactly one language?",
                      vis=F("venn", a_label="French", b_label="Spanish", shared="6",
                            only_a="12", only_b="8"),
                      reasoning="Fill the Venn diagram from the overlap outwards.",
                      steps=["The overlap is 6, so French only is 18 − 6 = 12.",
                             "Spanish only is 14 − 6 = 8.",
                             "So 12 + 6 + 8 = 26 study at least one language.",
                             "Hence 30 − 26 = 4 study neither.",
                             "The probability of exactly one language is (12 + 8)/30 = 20/30 "
                             "= 2/3."],
                      ans="4 study neither; the probability is 2/3",
                      interp="The overlap is filled first, and every other region follows from "
                             "it, which is why a Venn diagram is drawn from the inside out."),
                 dict(q="A two-way table records 100 people by age group and whether they "
                        "cycle. Given that a person is under 30, what is the probability that "
                        "they cycle?",
                      vis=F("table", [["", "cycles", "does not cycle", "total"],
                                      ["under 30", "30", "20", "50"],
                                      ["30 or over", "15", "35", "50"],
                                      ["total", "45", "55", "100"]],
                            "a two-way table of age group against cycling"),
                      reasoning="Restrict to the row for under 30 and divide by its total.",
                      steps=["The condition 'under 30' selects the first row, of 50 people.",
                             "Of those, 30 cycle.",
                             "So the conditional probability is 30/50 = 0.6.",
                             "The unconditional probability is 45/100 = 0.45.",
                             "The two differ, which is the point of conditioning: the same "
                             "question has a different answer once the sample space is "
                             "restricted."],
                      ans="0.6",
                      interp="A conditional probability divides a cell by the total of its "
                             "row or column, and the choice of row or column is the "
                             "condition."),
             ], inv=dict(
                 task="Survey thirty people on two yes-or-no questions of your own, for "
                      "example whether they walk to school and whether they play a sport. "
                      "Record the results in a two-way table, draw a Venn diagram of the same "
                      "data, and then compute P(A), P(B), P(A and B) and P(A or B). Check that "
                      "the addition law holds, and find one conditional probability from each "
                      "representation.",
                 table=[["", "plays a sport", "does not", "total"],
                        ["walks", "8", "7", "15"],
                        ["does not walk", "5", "10", "15"],
                        ["total", "13", "17", "30"]],
                 notice=["The two-way table gave the counts and the Venn diagram gave the "
                         "same numbers as regions.",
                         "P(A or B) was larger than either P(A) or P(B) but smaller than "
                         "their sum.",
                         "The overlap had been counted twice by adding, which is why the "
                         "addition law subtracts it.",
                         "The conditional probabilities were different from the "
                         "unconditional ones."],
                 obs="A two-way table and a Venn diagram are two representations of the same "
                     "two events, and each makes some probability readable at a glance.",
                 concl="Counts, unions, intersections and conditional probabilities are all "
                       "readable from either representation, and the addition law is the "
                       "statement that the overlap is counted twice.")),
        dict(id="13.3", title="Tree diagrams",
             inquiry_q="How does a tree diagram represent a sequence of events, and how are "
                       "its probabilities combined?",
             teach=[
                 "A tree diagram shows the outcomes of successive stages, with a branch for each outcome and its probability written on the branch, and the probabilities leaving any point always sum to 1.",
                 "The probability of a complete path is the product of the probabilities along it, because the stages are combined by the multiplication law.",
                 "The probability of an event that can happen in several ways is the sum of the probabilities of the paths that lead to it, and the two rules of multiply and add are the whole method.",
                 "A tree with the same probabilities on both levels is the picture of independent events, and a tree whose second level differs from the first is the picture of dependent ones.",
                 "A tree diagram is a representation of a system of stages, and it is preferred when the stages are sequential rather than simultaneous.",
             ], examples=[
                 dict(q="A spinner has sectors red, blue and green with probabilities 1/2, "
                        "1/3 and 1/6. It is spun and then a fair coin is thrown. Find the "
                        "probability of red and heads.",
                      vis=F("tree", [["red", "blue", "green"], ["heads", "tails"]],
                            "a three-branch stage followed by a two-branch stage"),
                      reasoning="Multiply along the path red then heads.",
                      steps=["The first stage has three branches: 1/2, 1/3 and 1/6, which "
                             "sum to 1.",
                             "The second stage has two branches of 1/2 each.",
                             "The path red then heads has probability (1/2) × (1/2) = 1/4.",
                             "The number of paths is 3 × 2 = 6, and their probabilities sum "
                             "to 1.",
                             "The two stages are independent, so the second level repeats "
                             "the first level's probabilities."],
                      ans="1/4",
                      interp="The product rule applies along a path, and the sum rule applies "
                             "across paths, and every complete tree must sum to 1."),
                 dict(q="A bag holds 2 red and 3 blue counters. One is drawn and not "
                        "replaced, and a second is then drawn. Find the probability that the "
                        "two counters are different colours.",
                      vis=F("tree", [["red", "blue"], ["red", "blue"]],
                            "the second level differs because there is no replacement"),
                      reasoning="Add the two paths that give different colours.",
                      steps=["P(red then blue) = (2/5) × (3/4) = 6/20.",
                             "P(blue then red) = (3/5) × (2/4) = 6/20.",
                             "The two paths are mutually exclusive, so add them.",
                             "The total is 6/20 + 6/20 = 12/20 = 3/5.",
                             "The second level has probabilities 3/4 and 2/4 after a red, "
                             "which is what makes the events dependent."],
                      ans="3/5",
                      interp="An event that can happen in two ways is a sum of paths, and the "
                             "order of the draws gives the two ways."),
             ], inv=dict(
                 task="Build a tree diagram for a two-stage situation of your own with at "
                      "least three branches at the first stage, for example a spinner followed "
                      "by a die, or a bag of three colours followed by a second draw without "
                      "replacement. Label every branch with its probability, check that the "
                      "probabilities leaving each point sum to 1, list every complete path "
                      "with its probability, and check that the paths sum to 1. Then use the "
                      "tree to find the probability of an event that can happen in two "
                      "different ways.",
                 table=[["path", "probability", "event"],
                        ["red, heads", "1/4", "red and heads"],
                        ["red, tails", "1/4", "red and tails"],
                        ["blue, heads", "1/6", "blue and heads"],
                        ["blue, tails", "1/6", "blue and tails"],
                        ["green, heads", "1/12", "green and heads"],
                        ["green, tails", "1/12", "total = 1"]],
                 notice=["Every set of branches leaving a point summed to 1.",
                         "Every path probability was a product along the path.",
                         "The event 'red or heads' needed adding several paths and "
                         "subtracting the overlap.",
                         "The paths summed to exactly 1, which was the check on the whole "
                         "diagram."],
                 obs="A tree diagram turns a sequence of stages into a list of paths, and the "
                     "product rule gives a path while the sum rule gives an event.",
                 concl="Multiply along a path and add across paths, and the two rules "
                       "together turn any tree diagram into a probability.")),
        dict(id="13.4", title="Independent and dependent events",
             inquiry_q="When does knowing that one event has happened change the probability "
                       "of another, and how is that decided?",
             teach=[
                 "Two events are independent when the probability of one is unchanged by knowing that the other has happened, so P(A given B) = P(A). Otherwise they are dependent.",
                 "For independent events the multiplication law is P(A and B) = P(A) × P(B), and this simple form is valid only when the events are independent.",
                 "For dependent events the conditional form P(A and B) = P(A) × P(B given A) is used, and the second factor is different from P(B) because the first draw has changed the sample space.",
                 "Drawing without replacement makes successive events dependent, and drawing with replacement keeps them independent, which is why the two procedures give different answers to the same question.",
                 "Independence is a property of the situation and not of the arithmetic, so it must be justified from the context. Assuming it when it is false is the commonest error in combined probability.",
             ], examples=[
                 dict(q="A fair die is thrown twice. Find the probability that both throws "
                        "are sixes, and say whether the events are independent.",
                      vis=F("tree", [["six", "not six"], ["six", "not six"]],
                            "two independent throws"),
                      reasoning="The throws do not affect each other, so multiply.",
                      steps=["P(six on the first throw) = 1/6.",
                             "The second throw is unaffected by the first, so its probability "
                             "is also 1/6.",
                             "So P(both sixes) = (1/6) × (1/6) = 1/36.",
                             "The events are independent because the die has no memory.",
                             "A tree diagram with the same branch probabilities on both levels "
                             "is the picture of independence."],
                      ans="1/36; the events are independent",
                      interp="Independence is what allows the simple product, and the reason "
                             "is physical: the second throw cannot know the first."),
                 dict(q="A bag has 5 red and 3 blue counters. Two are drawn without "
                        "replacement. Find the probability that both are red, and compare "
                        "with drawing with replacement.",
                      vis=F("tree", [["red", "blue"], ["red", "blue"]],
                            "drawing without replacement changes the second branch"),
                      reasoning="The first draw changes the contents, so the second "
                               "probability is conditional.",
                      steps=["P(first red) = 5/8.",
                             "Given the first was red, 4 red and 3 blue remain, so P(second "
                             "red given first red) = 4/7.",
                             "So P(both red) = (5/8) × (4/7) = 20/56 = 5/14.",
                             "With replacement the answer would be (5/8) × (5/8) = 25/64.",
                             "The two differ because without replacement the events are "
                             "dependent."],
                      ans="5/14 without replacement; 25/64 with replacement",
                      interp="The same question has two answers, and the difference is "
                             "entirely due to whether the sample space is restored."),
             ], inv=dict(
                 task="Take five pairs of events from a situation of your own: two throws of "
                      "a die, two cards drawn with and without replacement, two mornings' "
                      "weather, two students chosen from a class, and one pair of your own. "
                      "For each, decide whether the events are independent, justify the "
                      "decision from the situation, and compute P(A and B) using the correct "
                      "form of the multiplication law.",
                 table=[["pair of events", "independent?", "law used", "P(A and B)"],
                        ["two throws of a die", "yes", "P(A) × P(B)", "1/36"],
                        ["two cards, replaced", "yes", "P(A) × P(B)", "1/16"],
                        ["two cards, not replaced", "no", "P(A) × P(B given A)", "1/17"],
                        ["two students from a class", "no", "P(A) × P(B given A)", "—"],
                        ["rain today and rain tomorrow", "no", "conditional", "—"]],
                 notice=["Replacement made the difference between independent and dependent.",
                         "The conditional form was needed whenever the first event changed "
                         "the sample space.",
                         "The justification came from the situation, not from the numbers.",
                         "The independent calculation always gave the larger answer for two "
                         "reds."],
                 obs="Independence is decided by the situation, and the simple product is "
                     "valid only when the first event leaves the sample space unchanged.",
                 concl="Knowing one event has happened changes the probability of another "
                       "exactly when the sample space has changed, and the multiplication law "
                       "must then be used in its conditional form.")),
        dict(id="13.5", title="Expected frequency, simulation and fairness",
             inquiry_q="When is a game fair, and how is the expected value computed?",
             teach=[
                 "The expected value of a game is the sum of each outcome's value multiplied by its probability, and it is the average amount won per play over many plays.",
                 "A game is fair when the expected value is zero for every player, which means the rewards are proportional to the inverse of the probabilities.",
                 "A game with a positive expected value for one player and a negative one for the other is biased, and the bias can be measured exactly even though no single play is predictable.",
                 "Expected value is a long-run statement. It says nothing about any individual play, which is why a fair game can still be a bad bet for someone who cannot afford to lose.",
             
                 "The expected frequency of an event in n trials is n × P(event), and it is the number of times the event is expected, not the number it must occur.",
                 "A simulation uses random numbers to model a situation whose probabilities are known, and repeating it many times gives an experimental probability that approaches the theoretical one.",
                 "A game is one of many systems of rules that distribute chance, and fairness is a property of the rules rather than of any single play, which is why a rule can be changed to make the expected value zero.",
             ],
             examples=[

                 dict(q="A game costs 2 dollars to play. A die is thrown and the player wins "
                        "5 dollars if the score is 6. Find the expected value and say whether "
                        "the game is fair.",
                      vis=F("table", [["outcome", "probability", "gain"],
                                      ["score 6", "1/6", "+3"],
                                      ["not 6", "5/6", "−2"]],
                            caption="the gain is the prize minus the cost of playing"),
                      reasoning="Multiply each gain by its probability and sum.",
                      steps=["If the score is 6 the player gains 5 − 2 = 3 dollars.",
                             "Otherwise the player loses the 2 dollars stake.",
                             "The expected value is (1/6)(3) + (5/6)(−2) = 0.5 − 1.667.",
                             "That is −1.167 dollars per play.",
                             "The game is not fair: the player loses about 1.17 dollars each "
                             "time on average."],
                      ans="expected value about −1.17 dollars per play, so the game is not "
                          "fair",
                      interp="A negative expected value means the player loses in the long "
                             "run, however many times they win in the short run."),
                 dict(q="A fair coin is thrown and a player wins 4 dollars for heads and 2 "
                        "dollars for tails. What entry fee makes the game fair?",
                      vis=F("table", [["outcome", "probability", "prize"],
                                      ["heads", "1/2", "4"],
                                      ["tails", "1/2", "2"]],
                            caption="the expected prize is 3 dollars"),
                      reasoning="Set the expected prize equal to the entry fee.",
                      steps=["The expected prize is (1/2)(4) + (1/2)(2) = 3 dollars.",
                             "For the game to be fair the entry fee must equal the expected "
                             "prize.",
                             "So the fair entry fee is 3 dollars.",
                             "At any higher fee the player loses on average, and at any lower "
                             "fee they gain.",
                             "The fairness is a statement about the long run, not about one "
                             "throw."],
                      ans="3 dollars",
                      interp="A fair fee is the expected prize, and this is the principle "
                             "behind every insurance premium and every lottery ticket.")
             ],
             inv=dict(
                 task="Analyse three games: one with dice, one with cards and one from your "
                      "own invention. For each, list the outcomes and their probabilities, "
                      "compute the expected value, and state the entry fee that would make "
                      "the game fair.",
                 table=[["game", "expected prize", "fair fee", "verdict"],
                        ["die, win 6 for a six, stake 1", "1", "1", "fair"],
                        ["two dice, win 12 for a double six, stake 1", "12/36", "1",
                         "biased against the player"],
                        ["coin, win 3 for heads, stake 2", "1.5", "1.5",
                         "biased against the player"]],
                 notice=["Only the first game was fair at the stated stake.",
                         "The double-six game was heavily biased against the player.",
                         "The fair fee was always the expected prize.",
                         "A fair game can still be a bad bet for a player who cannot afford "
                         "the stake."],
                 obs="The expected value of a game is the average gain per play, and a game "
                     "is fair exactly when the entry fee equals the expected prize.",
                 concl="A game is fair when its expected value is zero for every player, which "
                       "happens when the entry fee equals the expected prize, and the "
                       "expected value is a statement about the long run only.")),
        dict(id="13.6", title="Investigation: is the game fair?",
             inquiry_q="How is a game designed so that no player has an advantage, and how is "
                       "that checked?",
             teach=[
                 "A two-player game is fair when each player's probability of winning is the same, which requires the two winning events to have equal probability and to be disjoint.",
                 "The two winning events must also be exhaustive of the remaining outcomes, so that the probability of neither winning is what is left after the two.",
                 "A game is checked by listing the sample space and counting, and by computing with the laws, and the two methods must agree.",
                 "Designing a game is the reverse of analysing one: choose the probabilities first, then find rules that produce them, which is harder because the rules must be simple.",
             ], examples=[
                 dict(q="Two fair dice are thrown. Player A wins if the first die is even and "
                        "the second is odd. Player B wins if both dice show the same number "
                        "and that number is 1 or 6. Find the probability that neither player "
                        "wins.",
                      vis=F("tree", [["even", "odd"], ["odd", "even"]],
                            [["3/6", "3/6"], ["3/6", "3/6"]],
                            "the two winning conditions are disjoint"),
                      reasoning="Count the outcomes for each player and subtract from the "
                               "total.",
                      steps=["The sample space has 36 equally likely outcomes.",
                             "Player A wins when the first die is even and the second odd: 3 "
                             "× 3 = 9 outcomes.",
                             "Player B wins on (1,1) and (6,6), which is 2 outcomes.",
                             "The two events are disjoint, because both dice cannot be the "
                             "same and one odd.",
                             "So neither player wins in 36 − 9 − 2 = 25 outcomes, a "
                             "probability of 25/36."],
                      ans="25/36",
                      interp="The two winning conditions are disjoint, so their probabilities "
                             "add, and the remainder is the probability that neither player "
                             "wins."),
                 dict(q="Design a rule change that makes the game fair, and check it.",
                      vis=F("table", [["player", "winning outcomes", "probability"],
                                      ["A (original)", "first even, second odd", "9/36"],
                                      ["B (original)", "both dice 1 or both 6", "2/36"],
                                      ["A (new rule)", "first even, second odd", "9/36"],
                                      ["B (new rule)", "first odd, second even", "9/36"]],
                            caption="the new rule gives B the same probability as A"),
                      reasoning="Give player B a rule with the same probability as player A's.",
                      steps=["Player A wins on 9 outcomes, so a fair game gives B 9 too.",
                             "A simple rule is: B wins if the first die is odd and the second "
                             "is even.",
                             "That is also 3 × 3 = 9 outcomes.",
                             "The two events are disjoint, because the first die cannot be "
                             "both even and odd.",
                             "So each player wins with probability 9/36 = 1/4, and neither "
                             "wins with probability 18/36 = 1/2."],
                      ans="one fair rule gives each player 9 of the 36 outcomes, with 18 left "
                          "over",
                      interp="Designing a fair rule means finding two disjoint events with "
                             "equal probability, and the check is that the two counts are "
                             "equal."),
             ], inv=dict(
                 task="Design a two-player game using dice, cards or a spinner. State the "
                      "rules precisely, compute each player's probability of winning and the "
                      "probability that neither wins, and adjust the rules until the game is "
                      "fair. Then compute the expected value of one play.",
                 table=[["version", "P(A)", "P(B)", "P(neither)", "fair?"],
                        ["first attempt", "9/36", "2/36", "25/36", "no"],
                        ["second attempt", "9/36", "9/36", "18/36", "yes"],
                        ["with a stake", "9/36", "9/36", "18/36", "yes, if prizes match"]],
                 notice=["The first version was badly biased towards player A.",
                         "The second gave each player the same number of outcomes.",
                         "Neither player won in 18 of the 36 outcomes in the fair version.",
                         "The expected value was zero only when the prizes were equal too."],
                 obs="A fair two-player game needs two disjoint winning events of equal "
                     "probability, and the remainder is the probability that neither player "
                     "wins.",
                 concl="A game is designed fair by giving each player a disjoint set of "
                       "outcomes of equal size, and it is checked by counting the sample space "
                       "and by computing with the addition and multiplication laws.")),
    ],
    practice=dict(
        A=[("13.1.1", "Find the probability that a fair die shows an even number.", "1/2",
            "Three favourable outcomes out of six.", "F"),
           ("13.1.2", "Find the probability that a fair die shows a prime number.", "1/2",
            "The primes are 2, 3 and 5.", "F"),
           ("13.1.3", "Find the probability that a fair die shows a number greater than 4.",
            "1/3", "The outcomes are 5 and 6.", "F"),
           ("13.1.4", "Find the probability of not throwing a 6 with a fair die.", "5/6",
            "The complement of 1/6.", "F"),
           ("13.1.5", "Find the probability that two fair dice sum to 7.", "1/6",
            "Six favourable outcomes out of 36.", "F"),
           ("13.1.6", "Find the probability of two heads when two fair coins are thrown.",
            "1/4", "Multiply 1/2 by 1/2.", "F"),
           ("13.1.7", "Find the probability of at least one head when two fair coins are "
            "thrown.", "3/4", "1 − P(no heads) = 1 − 1/4.", "F"),
           ("13.1.8", "A bag has 4 red and 6 blue counters. Find the probability of drawing a "
            "red one.", "0.4", "4 out of 10.", "F"),
           ("13.1.9", "Find the probability that a card drawn from a pack is a heart.",
            "1/4", "13 hearts out of 52.", "F"),
           ("13.1.10", "Find the probability that a card drawn from a pack is a king or a "
            "queen.", "2/13", "8 favourable cards out of 52.", "F"),
           ("13.1.11", "Two events are mutually exclusive with probabilities 0.3 and 0.4. "
            "Find the probability of either.", "0.7", "Add the probabilities.", "F"),
           ("13.1.12", "A fair coin is thrown three times. Find the probability of three "
            "heads.", "1/8", "Multiply 1/2 three times.", "F")],
        B=[("13.2.1", "The probabilities of two independent events are 0.4 and 0.5. Find the "
            "probability of both and of either.",
            "Both 0.2; either 0.7.", "Multiply for both; add and subtract the intersection "
            "for either.", "R"),
           ("13.2.2", "Investigate the pattern in the probability of at least one six in n "
            "throws of a die.",
            "1 − (5/6)ⁿ, which rises towards 1.", "Use the complement.", "R"),
           ("13.2.3", "Conjecture a rule for the probability that two people share a birthday "
            "in a group of n people.",
            "1 − (365/365)(364/365)…, which passes 0.5 at n = 23.",
            "Use the complement and multiply.", "C"),
           ("13.2.4", "Investigate the pattern in the probability of drawing two red cards "
            "without replacement from a pack.",
            "26/52 × 25/51 ≈ 0.245, less than 0.25 because the first draw changes the "
            "second.", "Multiply the conditional probabilities.", "R"),
           ("13.2.5", "Build a table of the probabilities of the sums of two dice and "
            "describe the pattern.",
            "The probabilities rise to 1/6 at 7 and then fall symmetrically.",
            "Count the outcomes for each sum.", "R"),
           ("13.2.6", "Conjecture a rule for the expected number of sixes in n throws of a "
            "die.", "n/6, because the expectation is linear.", "Multiply n by 1/6.", "R"),
           ("13.2.7", "Investigate the pattern in the probability that a family with two "
            "children has two girls, given that at least one is a girl.",
            "1/3, because the sample space reduces to three outcomes.", "Restrict the sample "
            "space.", "R"),
           ("13.2.8", "A test is 95% accurate and 2% of people are ill. Investigate the "
            "probability that a positive result means illness.",
            "About 28%, because the false positives outnumber the true positives.",
            "Use a tree and the conditional probability.", "C"),
           ("13.2.9", "Find the pattern in the probability of winning a prize in a raffle as "
            "the number of tickets bought grows.",
            "The probability is proportional to the tickets, so it rises linearly to 1.",
            "Divide the tickets by the total.", "R"),
           ("13.2.10", "Investigate the expected value of a game that pays the square of the "
            "score on a fair die, for a stake of 10 dollars.",
            "Expected prize 91/6 ≈ 15.17, so the game favours the player.", "Sum score² × "
            "1/6.", "R"),
           ("13.2.11", "Conjecture a rule for the number of throws needed for the probability "
            "of at least one six to exceed 0.9.",
            "13 throws, because (5/6)ⁿ < 0.1 gives n > 12.6.",
            "Solve the inequality.", "C")],
        C=[("13.3.1", "Explain in your own words what it means for two events to be "
            "independent.", "That the outcome of one does not change the probability of the "
            "other, so the probabilities multiply.", "State the definition.", "R"),
           ("13.3.2", "Write a complete solution to: find the probability that two cards "
            "drawn without replacement are both aces.",
            "4/52 × 3/51 = 1/221.", "Multiply the conditional probabilities.", "F"),
           ("13.3.3", "Choose between a Venn diagram and a tree diagram for two events and "
            "justify.", "A Venn diagram for a single stage with overlap; a tree for "
            "successive stages or for conditional probabilities.", "Say what each shows.",
            "R"),
           ("13.3.4", "Set out a full solution to: a bag has 3 red and 5 green counters. Two "
            "are drawn without replacement. Find the probability of one of each colour.",
            "30/56 = 15/28, from the two paths red-green and green-red.",
            "Add the two path probabilities.", "F"),
           ("13.3.5", "Explain why mutually exclusive events cannot be independent.",
            "Because if they are mutually exclusive, knowing one happened tells you the other "
            "did not, so the probability changes to zero.", "Apply the definitions.", "R"),
           ("13.3.6", "Describe, with an example, the difference between P(A and B) and "
            "P(A given B).", "P(A and B) is the probability of both in the whole sample "
            "space; P(A given B) restricts the sample space to B.", "Compare the "
            "denominators.", "R"),
           ("13.3.7", "Explain why the probability of neither of two disjoint events is one "
            "minus the sum of their probabilities.",
            "Because the three regions exhaust the sample space, so their probabilities sum "
            "to 1.", "Use the complement rule.", "R"),
           ("13.3.8", "Write the reasoning that shows P(A or B) = P(A) + P(B) − P(A and B).",
            "Adding P(A) and P(B) counts the intersection twice, so it must be subtracted "
            "once.", "Use a Venn diagram.", "R"),
           ("13.3.9", "Set out the argument that the expected value of a game is the average "
            "gain per play.",
            "Because over many plays each outcome occurs in proportion to its probability, so "
            "the average gain tends to the sum of value times probability.",
            "Use the law of large numbers.", "R"),
           ("13.3.10", "Explain what makes a game fair in terms of expected value.",
            "That the expected value is zero for every player, which happens when the entry "
            "fee equals the expected prize.", "State the condition.", "R"),
           ("13.3.11", "Describe the relationship between a rule and the probabilities it "
            "produces.", "The rule decides which outcomes belong to which player, so it "
            "decides the probabilities, and a fair rule gives equal probabilities.",
            "Compare two rules.", "R"),
           ("13.3.12", "Explain, with an example, when a rule that looks neutral is biased in "
            "effect.",
            "Any answer is acceptable if it identifies a rule giving equal chances per ticket "
            "while the tickets themselves were distributed unequally.",
            "Give a specific example.", "R")],
        D=[("13.4.1", "A game costs 3 dollars. A die is thrown and the player wins 10 dollars "
            "for a six. Find the expected value and say whether the game is fair.",
            "Expected value 10/6 − 3 ≈ −1.33 dollars, so it is not fair.",
            "Compute the expected prize and subtract the stake.", "A"),
           ("13.4.2", "Two players throw a fair coin. The winner of a head takes 5 dollars "
            "from the other. Find each player's expected value.",
            "Both zero, because each wins with probability 1/2 and gains or loses 5.",
            "Compute the expected gain for each.", "A"),
           ("13.4.3", "A spinner has sectors of 30°, 90°, 120° and 120°. Find the probability "
            "of each sector and the expected score if the score is the sector number.",
            "1/12, 1/4, 1/3, 1/3; the expected score is 1/12 + 2/4 + 3/3 + 4/3 ≈ 2.92.",
            "Divide each angle by 360°.", "A"),
           ("13.4.4", "A bag has 5 red and 3 blue counters. Two are drawn without "
            "replacement. Find the probability of two of the same colour.",
            "(5/8)(4/7) + (3/8)(2/7) = 26/56 = 13/28.", "Add the two matching paths.", "A"),
           ("13.4.5", "A medical test is 99% accurate for those who are ill and gives a false "
            "positive 5% of the time. One person in 100 is ill. Investigate the probability "
            "that a positive result means illness.",
            "About 17%, because the false positives outnumber the true positives.",
            "Use a tree and divide.", "R"),
           ("13.4.6", "A lottery sells 500 tickets and 3 prizes are drawn without "
            "replacement. Find the probability that one holder of 2 tickets wins exactly one "
            "prize.",
            "About 0.0235, from 2/500 × 498/499 × 497/498 × 3 arrangements.",
            "Use the hypergeometric count.", "C"),
           ("13.4.7", "A school allocates 20 places among 400 applicants by lottery. "
            "Investigate whether a family with 3 applicants is favoured and justify.",
            "Each applicant has probability 0.05, so the family's expected places are 0.15, "
            "which is proportional and therefore fair in probability.", "Compare the "
            "probabilities.", "R"),
           ("13.4.8", "A game uses two dice. Player A wins if the sum is even; player B wins "
            "if the sum is odd. Investigate whether the game is fair and what happens to the "
            "remaining probability.",
            "Each player wins with probability 1/2, so the game is fair and neither wins "
            "never happens.", "Count the outcomes.", "R"),
           ("13.4.9", "A biased coin has probability 0.6 of heads. Investigate the expected "
            "number of heads in 10 throws and the probability of more heads than tails.",
            "Expected 6 heads; the probability of more heads than tails is about 0.63.",
            "Use the binomial model.", "C"),
           ("13.4.10", "A raffle sells 200 tickets and one holder buys 20. Investigate "
            "whether the raffle is fair if the tickets were given away equally.",
            "The holder has probability 0.1, ten times any other, so it is fair only if "
            "everyone had the same chance to acquire tickets.", "Compare the probabilities.",
            "R"),
           ("13.4.11", "Two players each roll a die; the higher score wins and ties are "
            "re-rolled. Investigate whether the game is fair.",
            "Yes: by symmetry each player wins with probability 15/36 before ties, and ties "
            "are symmetric too.", "Count the outcomes.", "R"),
           ("13.4.12", "Explain, with a game of your own, when a fair game is still a bad "
            "bet.",
            "Any answer is acceptable if it identifies a stake that the player cannot afford "
            "to lose, however small the expected loss.", "Give a specific example.", "R")],
    ),
    assessment=[
        dict(title="A1 · The two dice",
             text="Two fair dice are thrown. Player A wins if the first die is even and the "
                  "second is odd. Player B wins if both dice show the same number and that "
                  "number is 1 or 6. Find the probability that A wins, that B wins, and that "
                  "neither player wins. Then design one change to the rules that makes the "
                  "game fair, and justify it by counting.",
             note="Criteria B and C · count the sample space, apply the addition law, and "
                  "justify the new rule."),
        dict(title="A2 · The game and the stake",
             text="A game costs 4 dollars to play. A spinner with four equal sectors pays 10 "
                  "dollars on one sector, 6 dollars on two sectors and nothing on the fourth. "
                  "Find the expected prize, the expected value of a play, and the entry fee "
                  "that would make the game fair. Then explain why a player might still "
                  "refuse to play the fair version.",
             note="Criteria A and D · compute the expected value, solve for the fair fee, and "
                  "justify the answer with the meaning of expectation."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of logic and the related concepts of probability, equivalence "
        "and systems appear in your work?",
        "How is the global context of fairness and development, and its exploration of how "
        "chance, risk and rules shape opportunities, visible in the investigations and examples "
        "you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of an expected value for a decision about playing a game, and "
        "what would you still like to ask?",
    ],
    review=dict(
        ideas=["A probability is a proportion of a listed sample space.",
               "An event and its complement have probabilities that sum to 1.",
               "P(A or B) = P(A) + P(B) − P(A and B).",
               "P(A and B) = P(A) × P(B) only for independent events.",
               "A tree is multiplied along a path and summed across paths.",
               "P(A and B) = P(A) × P(B given A) works for dependent events.",
               "The expected value is the sum of value times probability.",
               "A game is fair when the entry fee equals the expected prize."],
        vocab=["sample space", "mutually exclusive", "independent", "dependent",
               "conditional probability", "tree diagram", "Venn diagram", "expected value",
               "fair game", "complement", "intersection", "union"],
        mixed=[("13.R1", "Find the probability that a fair die shows a number that is not "
                         "prime."),
               ("13.R2", "Find the probability that two fair coins both show tails."),
               ("13.R3", "Find the probability that two cards drawn without replacement are "
                         "both hearts."),
               ("13.R4", "A bag has 6 red and 4 blue counters. Find the probability of one "
                         "of each in two draws without replacement."),
               ("13.R5", "A game pays 8 dollars with probability 1/4. Find the expected "
                         "prize."),
               ("13.R6", "Explain why two mutually exclusive events cannot be independent.")],
    ),
    projects=dict(
        service=[("Community need", "Random allocations are decided by rules that are rarely "
                                    "examined."),
                 ("Mathematical connection", "Sample spaces, combined events and expected "
                                             "value."),
                 ("Proposed action", "Analyse one real random allocation and publish whether "
                                     "it is fair in probability."),
                 ("Expected impact", "A group can see whether its rules give everyone the "
                                     "same chance."),
                 ("Student reflection", "Record the rules, the probabilities and the "
                                        "verdict.")],
        community=[("Project idea", "A fairness audit of one school or club allocation."),
                   ("Need", "Places, roles and prizes are allocated by rules nobody has "
                            "checked."),
                   ("Research question", "Does the rule give every participant the same "
                                         "probability, and is it fair in effect?"),
                   ("Mathematics", "Sample spaces, combined events and expected value."),
                   ("Action or outcome", "A one-page audit with the probability for each "
                                         "participant."),
                   ("Beneficiaries", "Everyone who takes part."),
                   ("Evidence", "The audit with the rules and the probabilities.")],
        personal=[("Personal interest", "A game, a sport or a competition you enjoy."),
                  ("Learning goal", "To analyse the rules of a game and say whether it is "
                                    "fair."),
                  ("Product or outcome", "An analysis with probabilities and a verdict."),
                  ("Mathematics", "Sample spaces, combined events and expected value."),
                  ("Process", "List the sample space, compute the probabilities, and compare "
                              "the players."),
                  ("Evidence", "The analysis and the verdict.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=14, title="Capstone: Designing a Sustainable Space",
    key="Form", related=["Measurement", "Space", "Change"],
    context="Globalisation and sustainability",
    exploration="Designing places that meet present needs without exhausting future resources",
    inquiry=("A design is a model of a space that must satisfy several constraints at once — "
             "area, capacity, cost, light and access — and each constraint is a measurement "
             "that the design must meet; choosing the form of the space is therefore a "
             "mathematical decision whose consequences change over time."),
    atl=("Self-management",
         "Students organise a multi-part design task, set their own deadlines for the "
         "modelling, the calculation and the report, and manage the time needed to complete "
         "each part."),
    standfirst="This chapter uses every idea in the book. A space is designed by measuring "
               "it, modelling it, costing it and checking it against the needs it must serve.",
    engage="Your school has a courtyard 7.2 m by 4.8 m that floods in the rainy season and is "
           "unused in the dry one. Design a space that captures the rain, provides shade, and "
           "costs less than the budget.",
    questions=[("Factual", "Which measurements does a design of a space require, and which "
                           "formulae from this course give them?"),
               ("Conceptual", "How do the constraints on a space interact, and why does a "
                              "change to one measurement change the others?"),
               ("Debatable", "Is a design that meets every stated constraint a good design, "
                             "or does goodness depend on needs the constraints do not "
                             "express?")],
    application_lede="Each task asks you to model part of a design. State the constraint, the "
                     "formula you use, and the units of your answer.",
    projects_lede="A design is a claim about the future. Model one and say what would have to "
                  "stay true for your design to work.",
    sections=[
        dict(id="C.1", title="The brief and the modelling cycle",
             inquiry_q="How is a design brief turned into a set of mathematical constraints?",
             teach=[
                 "A design brief states what the space must do, and each requirement becomes a constraint that the design must satisfy. A constraint with no number cannot be checked.",
                 "The site is measured first: its area, its perimeter, its levels, the direction of the sun and the direction of the drainage. Each measurement limits the design.",
                 "A constraint can be an equality, such as a fixed area, or an inequality, such as a maximum cost. The feasible designs are those that satisfy all of them at once.",
                 "Turning a wish into a constraint is a modelling decision, and a designer who leaves a requirement unstated will discover it later as a failure.",
             ], examples=[
                 dict(q="A courtyard measures 7.2 m by 4.8 m on a plan drawn at a scale of "
                        "1 : 50. Find the real area of the courtyard and the area available "
                        "for planting if paths take 20% of it.",
                      vis=F("scale_drawing", ("7.2 cm", "4.8 cm"), "1 : 50", "rectangle",
                            "the plan of the courtyard"),
                      reasoning="Convert the plan dimensions using the scale, then compute the "
                               "area.",
                      steps=["On the plan the courtyard is 7.2 cm by 4.8 cm.",
                             "At a scale of 1 : 50 the real dimensions are 7.2 × 50 = 360 cm "
                             "and 4.8 × 50 = 240 cm.",
                             "That is 3.6 m by 2.4 m, so the area is 3.6 × 2.4 = 8.64 m².",
                             "If paths take 20%, the planting area is 80% of 8.64 = 6.912 m².",
                             "The plan gives the area directly, and the scale is what connects "
                             "the drawing to the ground."],
                      ans="8.64 m² in total, of which 6.912 m² is available for planting",
                      interp="A scale drawing is a representation whose measurements are the "
                             "real measurements divided by the scale factor, and the area needs "
                             "the square of that factor."),
                 dict(q="A brief requires a seating area of at least 6 m², a water tank of at "
                        "least 200 litres, and a total cost of at most 500 dollars. State these "
                        "as constraints.",
                      vis=F("table", [["requirement", "constraint", "kind"],
                                      ["seating area", "A ≥ 6 m²", "inequality"],
                                      ["water tank", "V ≥ 200 litres", "inequality"],
                                      ["total cost", "C ≤ 500 dollars", "inequality"],
                                      ["courtyard area", "A ≤ 8.64 m²", "inequality"]],
                            caption="each requirement is a measurable bound"),
                      reasoning="Write each requirement as a quantity and a bound.",
                      steps=["The seating area is a quantity measured in square metres with a "
                             "lower bound of 6.",
                             "The tank capacity is a quantity measured in litres with a lower "
                             "bound of 200.",
                             "The cost is a quantity measured in dollars with an upper bound "
                             "of 500.",
                             "The courtyard itself gives an upper bound on every area.",
                             "A design is feasible only when all four bounds hold at once."],
                      ans="A_seating ≥ 6, V_tank ≥ 200, C ≤ 500, A_total ≤ 8.64",
                      interp="A constraint is a quantity with a bound, and a design is "
                             "feasible when every bound is satisfied together."),
             ], inv=dict(
                 task="Choose a real space you know: a classroom, a bedroom, a garden or a "
                      "corner of a playground. Measure it, write a brief with at least four "
                      "measurable constraints, and draw it to a stated scale.",
                 table=[["requirement", "constraint", "measurement needed"],
                        ["floor area", "A ≥ 12 m²", "length and width"],
                        ["seating", "at least 8 places", "0.5 m² per place"],
                        ["light", "window area ≥ 1.5 m²", "window dimensions"],
                        ["circulation", "path width ≥ 0.9 m", "clear width"]],
                 notice=["Every requirement became a quantity with a bound.",
                         "The seating requirement needed an assumption about space per "
                         "person.",
                         "The light requirement was an area, not a number of windows.",
                         "The circulation requirement was a width, which is a length."],
                 obs="A design brief becomes a set of constraints when each requirement is "
                     "written as a quantity with a bound, and each quantity needs a stated "
                     "measurement.",
                 concl="A space is designed by measuring it first and then writing each "
                       "requirement as a measurable constraint, because a requirement that "
                       "cannot be measured cannot be checked.")),
        dict(id="C.2", title="Data, constraints and assumptions",
             inquiry_q="What data does a design need, and how is each quantity turned into a constraint?",
             teach=[
                 "A layout is a scale drawing in which every length is the real length divided by the scale factor, and every area is the real area divided by the square of the factor.",
                 "Drawing to scale makes the layout checkable: an area computed from the drawing must equal the area computed from the real dimensions, and the areas of the parts must sum to the area of the whole.",
                 "Circulation, planting, seating and water are all areas, and a plan that does not account for all of them is incomplete, so the first check on any plan is that its parts sum to its whole.",
                 "The capacity of a tank is its volume, and the volume of a cylinder is πr²h. A demand is a rate, and the time to fill or empty is the capacity divided by the rate.",
                 "A rainwater tank captures a volume equal to the roof area times the rainfall, and the fraction captured depends on the efficiency of the collection surface.",
                 "Modelling a water system means matching a supply rate with a demand rate, and the tank is what bridges the gap when the rates do not coincide.",
                 "Every quantity in a design rests on an assumption, and an assumption that is not stated cannot be questioned, which is why stating them is part of the modelling.",
             ], examples=[

                 dict(q="A plan of a courtyard is drawn at 1 : 50 and measures 7.2 cm by "
                        "4.8 cm. A seating area of 4.8 m² and paths of 1.92 m² are marked. "
                        "Find the remaining area and check that the parts sum to the whole.",
                      vis=F("grid", [], [], 0, 8, 0, 6, [(0, 0), (7.2, 0), (7.2, 4.8),
                                                          (0, 4.8)],
                            "the plan divided into its parts"),
                      reasoning="Compute the total from the plan and subtract the marked parts.",
                      steps=["The real area is 3.6 × 2.4 = 8.64 m².",
                             "The seating area is 4.8 m² and the paths 1.92 m².",
                             "The remaining area is 8.64 − 4.8 − 1.92 = 1.92 m².",
                             "The parts sum to 4.8 + 1.92 + 1.92 = 8.64 m², which matches the "
                             "whole.",
                             "So the plan accounts for the whole courtyard, which is the "
                             "first check."],
                      ans="1.92 m² remaining, and the parts sum to 8.64 m²",
                      interp="A plan whose parts do not sum to the whole has either an "
                             "unmarked region or an arithmetic error, and either way it is not "
                             "yet a design."),
                 dict(q="A designer wants the planting area to be at least 40% of the "
                        "courtyard. Is the layout above acceptable?",
                      vis=F("pie", [40, 20, 40], ["planting", "seating", "paths"],
                            "the shares of the courtyard"),
                      reasoning="Compare the planting share with the required share.",
                      steps=["The planting area is 1.92 m² out of 8.64 m².",
                             "The share is 1.92/8.64 ≈ 22%.",
                             "The requirement is at least 40%, which would be 3.456 m².",
                             "So the layout is not acceptable as drawn.",
                             "The designer must reduce the seating or the paths, or increase "
                             "the planting."],
                      ans="no: planting is about 22%, below the required 40%",
                      interp="A percentage constraint is checked by comparing shares, and the "
                             "shares must sum to 100% for the plan to be complete."),

                 dict(q="A roof of 30 m² collects rain. The annual rainfall is 900 mm and "
                        "the collection efficiency is 0.8. Find the annual volume collected.",
                      vis=F("cone", 3, 5, "a tank fed by a 30 m² roof"),
                      reasoning="Multiply the roof area by the rainfall depth and by the "
                               "efficiency.",
                      steps=["The rainfall depth is 900 mm = 0.9 m.",
                             "The volume falling on the roof is 30 × 0.9 = 27 m³.",
                             "With an efficiency of 0.8 the volume collected is 27 × 0.8 = "
                             "21.6 m³.",
                             "That is 21600 litres a year.",
                             "A tank of 2000 litres therefore stores about a month of the "
                             "annual total."],
                      ans="21.6 m³, or 21600 litres, a year",
                      interp="The collected volume is the roof area times the depth times the "
                             "efficiency, and each of the three is a separate measurement."),
                 dict(q="A tank of radius 0.6 m and height 1.8 m is to hold the collected "
                        "water. Find its capacity and say for how many days it would supply a "
                        "garden using 40 litres a day.",
                      vis=F("prism", "cuboid", 3, 4, 5, "a cylindrical tank of radius 0.6 m"),
                      reasoning="Compute the volume and divide by the daily demand.",
                      steps=["The capacity is π × 0.6² × 1.8 = π × 0.648 ≈ 2.035 m³.",
                             "That is about 2035 litres.",
                             "At 40 litres a day the tank lasts 2035/40 ≈ 51 days.",
                             "So one filling covers about seven weeks of dry weather.",
                             "The tank is large enough for the dry season if it is filled "
                             "before it begins."],
                      ans="about 2035 litres, lasting about 51 days",
                      interp="The capacity and the demand are both measurements, and the "
                             "duration is their ratio, which is the simplest model of a "
                             "supply.")
             ], inv=dict(
                 task="Design a rainwater system for one real roof: measure the roof area, "
                      "find the local annual rainfall, choose an efficiency, and find the "
                      "annual volume collected. Then choose a tank and find how many days of "
                      "demand it covers.",
                 table=[["quantity", "value", "source"],
                        ["roof area", "30 m²", "measured"],
                        ["annual rainfall", "900 mm", "local records"],
                        ["efficiency", "0.8", "assumed"],
                        ["volume collected", "21.6 m³", "computed"],
                        ["tank capacity", "2.035 m³", "chosen"],
                        ["days of demand", "51", "computed"]],
                 notice=["The annual volume came from three separate measurements.",
                         "The efficiency was an assumption, not a measurement.",
                         "The tank covered about 51 days, which is more than a typical dry "
                         "season.",
                         "A smaller tank would have been cheaper but riskier."],
                 obs="A water system is modelled by a supply volume, a capacity and a demand "
                     "rate, and the duration is the capacity divided by the demand.",
                 concl="A rainwater system is designed by matching the volume collected with "
                       "the demand over the longest period in which supply falls short, and "
                       "the tank size is the bridge between the two.")),
        dict(id="C.3", title="Analysis, evaluation and communication",
             inquiry_q="How is a design analysed over time, evaluated against its brief, and communicated to a reader?",
             teach=[
                 "The cost of a design has a capital part, paid once, and a running part, paid each period. The total over n periods is the capital cost plus n times the running cost.",
                 "A cost that rises by a fixed percentage each year is exponential, and the total over n years is a geometric series, which is how inflation is modelled.",
                 "Comparing two designs means comparing their totals over the same period, and the cheaper capital cost is not always the cheaper total.",
                 "A design that saves money each year has a payback period, and a design whose savings grow is better in the long run than one whose savings are fixed.",
                 "A design is evaluated by measuring the space it creates and comparing the measurements with the constraints in the brief, so an unmeasured constraint cannot be evaluated.",
                 "The needs of the users are data, and collecting them means asking the people who will use the space and recording their answers as quantities rather than opinions.",
                 "A review compares what was intended with what was achieved, and the difference is the evidence for the next design, which is why a design that is never reviewed cannot improve.",
                 "Communication is part of the analysis: a result that cannot be explained to a reader has not been finished, and the explanation must name the model, the assumptions and the limits.",
             ], examples=[

                 dict(q="A shade structure costs 400 dollars to build and 20 dollars a year "
                        "to maintain, with maintenance rising 5% a year. Find the total cost "
                        "over 5 years.",
                      vis=F("table", [["year", "maintenance", "running total"],
                                      ["1", "20.00", "20.00"],
                                      ["2", "21.00", "41.00"],
                                      ["3", "22.05", "63.05"],
                                      ["4", "23.15", "86.20"],
                                      ["5", "24.31", "110.51"]],
                            caption="the maintenance grows geometrically"),
                      reasoning="Model the maintenance as a geometric series and add the "
                               "capital cost.",
                      steps=["The maintenance is 20, 21, 22.05, …, a geometric series with "
                             "ratio 1.05.",
                             "The sum over 5 years is 20 × (1.05⁵ − 1)/0.05 ≈ 110.51 dollars.",
                             "Adding the capital cost gives 400 + 110.51 = 510.51 dollars.",
                             "The running cost is about 22% of the capital cost over five "
                             "years.",
                             "Over twenty years the running cost would exceed the capital "
                             "cost."],
                      ans="about 510.51 dollars over 5 years",
                      interp="A percentage rise in a running cost compounds, so the long-term "
                             "total is much larger than five times the first year's cost."),
                 dict(q="A second design costs 520 dollars with maintenance falling by 10% a "
                        "year from 30 dollars. Compare the two over 5 years.",
                      vis=F("grid", [(1, 30), (2, 27), (3, 24.3), (4, 21.87), (5, 19.68)],
                            ["", "", "", "", ""], 0, 6, 0, 35,
                            [(1, 30), (2, 27), (3, 24.3), (4, 21.87), (5, 19.68)],
                            "the maintenance falls over time"),
                      reasoning="Model the second maintenance as a decreasing geometric series "
                               "and compare the totals.",
                      steps=["The maintenance is 30, 27, 24.3, …, a geometric series with "
                             "ratio 0.9.",
                             "The sum over 5 years is 30 × (1 − 0.9⁵)/0.1 ≈ 123.51 dollars.",
                             "The total is 520 + 123.51 = 643.51 dollars.",
                             "The first design costs about 510.51 dollars, so it is cheaper "
                             "over five years.",
                             "But the second design's costs fall, so it would win over a "
                             "longer period."],
                      ans="the first design costs about 510.51 dollars and the second about "
                          "643.51 dollars over 5 years",
                      interp="The comparison reverses over a longer period, which is why the "
                             "time horizon must be stated before a design is chosen."),

                 dict(q="A design provides 5.5 m² of seating in a courtyard of 8.64 m², "
                        "against a requirement of at least 6 m² and at least 50%. Evaluate "
                        "the design.",
                      vis=F("bar_chart", ["seating", "paths", "planting"], [5.5, 1.92, 1.22],
                            "the areas achieved"),
                      reasoning="Test both constraints and report which are met.",
                      steps=["The seating area is 5.5 m², which is below the required 6 m².",
                             "The share is 5.5/8.64 ≈ 64%, which is above the required 50%.",
                             "So one constraint is met and the other is not.",
                             "The design therefore fails the brief, even though it passes one "
                             "test comfortably.",
                             "The review identifies exactly which constraint failed."],
                      ans="the design fails: seating is 5.5 m² against a required 6 m², "
                          "though the share of 64% passes",
                      interp="A review tests each constraint separately, and a design that "
                             "fails one is not acceptable however well it meets the others."),
                 dict(q="A survey of 30 users finds 18 want more shade and 12 want more "
                        "seating. Find the percentages and state what a sample of 30 can "
                        "support.",
                      vis=F("pie", [60, 40], ["shade", "seating"],
                            "what the users asked for"),
                      reasoning="Convert the counts to percentages and state the limits of "
                               "the sample.",
                      steps=["18 of 30 want more shade, which is 60%.",
                             "12 of 30 want more seating, which is 40%.",
                             "The sample is 30 people, so the margin of error is about "
                             "1/√30 ≈ 18%.",
                             "So the true figures could be anywhere from about 42% to 78% for "
                             "shade.",
                             "The survey shows a direction but not a precise proportion."],
                      ans="60% want shade and 40% want seating, with a margin of error of "
                          "about 18%",
                      interp="A small sample shows a direction, and the margin of error is "
                             "what limits how firmly the direction can be stated.")
             ], inv=dict(
                 task="Review one real space against a brief of your own. Measure the "
                      "quantities in the brief, survey at least 20 users, and write a review "
                      "that states which constraints are met, which are not, and what the "
                      "survey can and cannot support.",
                 table=[["constraint", "required", "measured", "verdict"],
                        ["seating area", "≥ 6 m²", "5.5 m²", "not met"],
                        ["planting share", "≥ 40%", "22%", "not met"],
                        ["path width", "≥ 0.9 m", "1.1 m", "met"],
                        ["users wanting shade", "survey", "60% of 30", "direction only"]],
                 notice=["Two of the three measurable constraints were not met.",
                         "The survey gave a direction with a wide margin of error.",
                         "The review identified precisely what to change.",
                         "The unmet constraints were the ones nobody had measured before."],
                 obs="A review measures each constraint and surveys the users, and the two "
                     "kinds of evidence answer different questions about the design.",
                 concl="A design is reviewed by measuring it against its constraints and by "
                       "surveying its users, and the review states what each kind of evidence "
                       "can support.")),
        dict(id="C.4", title="Assessment task and rubric",
             inquiry_q="What must an assessment task ask for, and how is the work judged?",
             teach=[
                 "An assessment task asks for a model, a calculation and a judgement, and it is marked against criteria that name what each level of achievement looks like.",
                 "A rubric turns a judgement into a description: each criterion is stated, each level is described, and the evidence for the level is named, so that two markers reading the same work reach the same level.",
                 "The four criteria used in this course are Knowing and understanding, Investigating patterns, Communicating, and Applying mathematics in real-life contexts, and a task must give a student the chance to show all four.",
                 "A task that can be answered by copying a worked example tests nothing, so the numbers, the space and the question must be the student's own.",
                 "Every submission must state its assumptions and its limitations, because a model that hides them is not a model that can be evaluated.",
             ], examples=[

                 dict(q="Write the calculation for the area of a courtyard 3.6 m by 2.4 m in "
                        "the form a report should use.",
                      vis=F("table", [["element", "content"],
                                      ["quantity", "area of the courtyard"],
                                      ["formula", "A = length × width"],
                                      ["substitution", "A = 3.6 × 2.4"],
                                      ["result", "8.64 m²"],
                                      ["check", "3.6 × 2.4 ≈ 4 × 2.5 = 10, close enough"]],
                            caption="a calculation in reportable form"),
                      reasoning="Show the formula, the substitution, the result with units and "
                               "an estimate as a check.",
                      steps=["State the quantity: the area of the courtyard.",
                             "State the formula: A = length × width.",
                             "Substitute: A = 3.6 × 2.4.",
                             "Give the result with units: 8.64 m².",
                             "Check by estimating: 3.6 × 2.4 is close to 4 × 2.5 = 10, and "
                             "8.64 is of that order."],
                      ans="A = 3.6 × 2.4 = 8.64 m²",
                      interp="A calculation is reportable when a reader can reproduce it, "
                             "which requires the formula, the substitution and the units."),
                 dict(q="A report claims a tank will last 'about two months'. Rewrite the "
                        "claim so that it can be checked.",
                      vis=F("table", [["element", "content"],
                                      ["claim", "the tank lasts about 51 days"],
                                      ["capacity", "2.035 m³ = 2035 litres"],
                                      ["demand", "40 litres a day"],
                                      ["calculation", "2035 ÷ 40 = 50.9 days"],
                                      ["assumption", "the demand stays at 40 litres a day"]],
                            caption="a claim that a reader can check"),
                      reasoning="Replace the vague claim with the numbers that produce it.",
                      steps=["State the capacity: 2.035 m³, which is 2035 litres.",
                             "State the demand: 40 litres a day.",
                             "Show the calculation: 2035 ÷ 40 = 50.9 days.",
                             "State the assumption: the demand stays at 40 litres a day.",
                             "The claim 'about 51 days' can now be checked by anyone."],
                      ans="the tank lasts 2035 ÷ 40 ≈ 51 days, assuming a demand of 40 litres "
                          "a day",
                      interp="A vague claim cannot be checked, and a claim that cannot be "
                             "checked cannot be trusted or improved.")
             ], inv=dict(
                 task="Write a one-page design report for a space you have modelled in this "
                      "chapter. Include the brief, at least four constraints, three "
                      "calculations in reportable form, one survey result, and a statement of "
                      "the assumptions and the limits of the design.",
                 table=[["section", "content", "checkable?"],
                        ["brief", "four measurable constraints", "yes"],
                        ["model", "area, capacity, cost", "yes"],
                        ["calculations", "formula, substitution, units", "yes"],
                        ["survey", "30 users, 60% want shade", "direction only"],
                        ["assumptions", "demand, efficiency, rainfall", "yes"]],
                 notice=["Every calculation showed its formula, substitution and units.",
                         "The survey result was reported with its margin of error.",
                         "The assumptions were listed so the reader could judge them.",
                         "The limits of the design were stated as plainly as its "
                         "achievements."],
                 obs="A design report is checkable when every calculation shows its formula, "
                     "substitution and units, and when the assumptions are stated.",
                 concl="A design is presented as a chain of checkable calculations supported "
                       "by stated assumptions, and the report is complete only when it also "
                       "states what the design does not do.")),
    ],
    practice=dict(
        A=[("C.1.1", "A plan is drawn at 1 : 50. Find the real length of a wall measuring "
            "7.2 cm on the plan.", "3.6 m", "Multiply by 50 and convert to metres.", "F"),
           ("C.1.2", "A courtyard is 3.6 m by 2.4 m. Find its area.", "8.64 m²",
            "Multiply the two dimensions.", "F"),
           ("C.1.3", "A tank is a cylinder of radius 0.5 m and height 1.5 m. Find its "
            "capacity in litres.", "1178 litres", "π × 0.25 × 1.5 m³, times 1000.", "F"),
           ("C.1.4", "A roof of 20 m² receives 100 mm of rain. Find the volume collected at "
            "an efficiency of 0.9.", "1.8 m³", "20 × 0.1 × 0.9.", "F"),
           ("C.1.5", "A garden uses 30 litres a day. Find how long a 900-litre tank lasts.",
            "30 days", "Divide the capacity by the demand.", "F"),
           ("C.1.6", "A structure costs 300 dollars to build and 25 dollars a year to "
            "maintain. Find the 4-year total.", "400 dollars",
            "Add the capital cost to four years of running cost.", "F"),
           ("C.1.7", "A maintenance cost of 20 dollars rises 10% a year. Find the cost in "
            "year 3.", "24.20 dollars", "20 × 1.1².", "F"),
           ("C.1.8", "A design provides 5 m² of seating in 10 m². Find the percentage.",
            "50%", "Divide and multiply by 100.", "F"),
           ("C.1.9", "A survey of 40 users finds 24 want more shade. Find the percentage.",
            "60%", "24 out of 40.", "F"),
           ("C.1.10", "A path must be at least 0.9 m wide. A measured path is 0.85 m. Is it "
            "acceptable?", "No", "Compare with the bound.", "F"),
           ("C.1.11", "A shade sail covers 6 m² of a 12 m² courtyard. Find the percentage "
            "covered.", "50%", "Divide the areas.", "F"),
           ("C.1.12", "A tank holds 500 litres and is filled at 20 litres a minute. Find the "
            "filling time.", "25 minutes", "Divide the capacity by the rate.", "F")],
        B=[("C.2.1", "The areas of the parts of a plan are 4.8, 1.92 and 1.92 m². Find the "
            "total and the share of the largest part.",
            "Total 8.64 m²; the largest share is about 56%.", "Sum and divide.", "R"),
           ("C.2.2", "Investigate the pattern in the capacity of cylindrical tanks of fixed "
            "height as the radius grows.",
            "The capacity grows as the square of the radius, because V = πr²h.",
            "Compute for several radii.", "R"),
           ("C.2.3", "Conjecture a rule for the roof area needed to fill a 1000-litre tank "
            "from 100 mm of rain at an efficiency of 0.8.",
            "12.5 m², because area = volume/(depth × efficiency).",
            "Rearrange the collection formula.", "R"),
           ("C.2.4", "Investigate the pattern in the 5-year total of a 400-dollar structure "
            "with maintenance rising 5% a year, for maintenance starting at 10, 20 and 30 "
            "dollars.",
            "The totals are 455.26, 510.51 and 565.77, rising linearly with the starting "
            "maintenance.", "Sum the geometric series.", "R"),
           ("C.2.5", "Build a table of the duration of tanks of 500, 1000 and 2000 litres at "
            "a demand of 40 litres a day.",
            "12.5, 25 and 50 days, proportional to the capacity.",
            "Divide capacity by demand.", "R"),
           ("C.2.6", "Conjecture a rule for the payback period of a 600-dollar investment "
            "that saves 50 dollars a year.",
            "12 years, from 600/50.", "Divide the cost by the annual saving.", "R"),
           ("C.2.7", "Investigate the pattern in the margin of error of surveys of 10, 40 "
            "and 160 people.",
            "About 32%, 16% and 8%, halving as the sample quadruples.",
            "Use 1/√n.", "R"),
           ("C.2.8", "A roof's collected volume is modelled with an efficiency of 0.8. "
            "Investigate the effect of an efficiency of 0.6 on the tank size needed.",
            "The tank must be 25% larger, because the volume falls in the same proportion.",
            "Compare the two volumes.", "R"),
           ("C.2.9", "Find the pattern in the surface area of open-top cylindrical tanks of "
            "fixed volume as the radius grows.",
            "The area falls to a minimum at h = r and then rises.",
            "Write the area in terms of r and minimise.", "C"),
           ("C.2.10", "Investigate the pattern in the number of days of water stored per "
            "square metre of roof.",
            "About 0.72 days per m² for 900 mm of rain at 0.8 efficiency and 40 litres a "
            "day.", "Compute the ratio.", "R"),
           ("C.2.11", "Conjecture a rule for the total cost over n years of a capital cost C "
            "with maintenance rising at r a year from M.",
            "C + M((1 + r)ⁿ − 1)/r, a capital cost plus a geometric series.",
            "Sum the series.", "R")],
        C=[("C.3.1", "Explain in your own words what a constraint is in a design brief.",
            "A requirement written as a quantity with a bound, so that a design can be tested "
            "against it.", "State the definition.", "R"),
           ("C.3.2", "Write a complete solution to: find the real area of a plan measuring "
            "6 cm by 4 cm at a scale of 1 : 100.",
            "24 m², from 6 m by 4 m.", "Scale both lengths, then multiply.", "F"),
           ("C.3.3", "Choose between a scale drawing and a formula to find the area of an "
            "irregular courtyard and justify.", "A formula for a regular shape; a scale "
            "drawing with a grid for an irregular one, counting squares.",
            "Say what each suits.", "R"),
           ("C.3.4", "Set out a full solution to: find the capacity in litres of a cylinder "
            "of radius 0.4 m and height 1.2 m.",
            "About 603 litres.", "Use πr²h and convert.", "F"),
           ("C.3.5", "Explain why a percentage constraint on an area is checked by comparing "
            "shares.", "Because a percentage is a share of the whole, and the shares must sum "
            "to 100% for the plan to be complete.", "Compare the shares.", "R"),
           ("C.3.6", "Describe, with an example, the difference between a capital cost and a "
            "running cost.", "A capital cost is paid once to build, as 400 dollars for a "
            "structure; a running cost is paid each period, as 20 dollars a year.",
            "Compare the two.", "R"),
           ("C.3.7", "Explain why the duration of a tank is the capacity divided by the "
            "demand.", "Because the tank empties at the demand rate, so the time is the "
            "quantity divided by the rate.", "Use the rate formula.", "R"),
           ("C.3.8", "Write the reasoning that shows the volume collected from a roof is the "
            "area times the depth times the efficiency.",
            "The volume falling on the roof is the area times the depth, and only the "
            "efficiency fraction of it is collected.", "Multiply the three factors.", "R"),
           ("C.3.9", "Set out the argument that a design that meets every constraint can "
            "still be a poor design.",
            "Because the constraints are the requirements that were thought of, and a need "
            "that was not written down cannot be met by the model.", "Give an example.", "R"),
           ("C.3.10", "Explain what a payback period is and how it is found.",
            "The time for the savings of a design to equal its capital cost, found by "
            "dividing the cost by the annual saving.", "State the definition.", "R"),
           ("C.3.11", "Describe the relationship between the margin of error of a survey and "
            "its sample size.", "The margin of error is about 1/√n, so it halves when the "
            "sample size quadruples.", "Compare two sizes.", "R"),
           ("C.3.12", "Explain, with a design of your own, when a report is not checkable.",
            "Any answer is acceptable if it identifies a number without units, a calculation "
            "without a formula, or an assumption left unstated.", "Give a specific example.",
            "R")],
        D=[("C.4.1", "A roof of 45 m² collects rain with an efficiency of 0.75. Find the "
            "volume collected from 800 mm of rain and the tank needed for 60 days at 50 "
            "litres a day.",
            "27 m³ collected; a 3000-litre tank covers 60 days.",
            "Multiply for the supply and divide for the demand.", "A"),
           ("C.4.2", "A design costs 600 dollars with maintenance of 40 dollars a year "
            "rising 8% a year. Find the total over 10 years.",
            "About 1259 dollars, from 600 + 40 × (1.08¹⁰ − 1)/0.08.",
            "Sum the geometric series.", "A"),
           ("C.4.3", "Two designs cost 800 and 950 dollars. The first has running costs "
            "rising 10% a year from 50 dollars; the second has running costs falling 5% a "
            "year from 60 dollars. Find which is cheaper over 10 years.",
            "The second, at about 1663 dollars against about 1794 dollars.",
            "Sum both series and compare.", "A"),
           ("C.4.4", "A courtyard of 9 m² must have at least 45% planting, at most 30% "
            "paths and at least 2 m² of seating. Investigate whether these constraints can be "
            "met together.",
            "Yes: 4.05 m² planting, 2.7 m² paths and 2.25 m² seating sum to 9 m² and meet "
            "every bound.", "Test the shares.", "R"),
           ("C.4.5", "A tank of 1500 litres is filled from a 25 m² roof at 0.8 efficiency. "
            "Find the rainfall needed to fill it and the number of fills in a 900 mm year.",
            "75 mm of rain; about 12 fills a year.", "Rearrange and divide.", "A"),
           ("C.4.6", "A survey of 50 users finds 35 want more shade. Find the percentage and "
            "the margin of error, and state what the survey supports.",
            "70% with a margin of about 14%, so the true figure is likely between 56% and "
            "84%.", "Compute the share and 1/√n.", "A"),
           ("C.4.7", "A shade structure costs 350 dollars and saves 60 dollars a year in "
            "cooling. Investigate the payback period and the effect of a 5% annual rise in "
            "the saving.",
            "About 5.8 years without the rise, and about 4.8 years with it.",
            "Solve for the year in which the savings exceed the cost.", "R"),
           ("C.4.8", "A plan at 1 : 25 shows a room 9.6 cm by 6.4 cm. Find the real "
            "dimensions and the area, and the number of 0.5 m² desks that fit.",
            "2.4 m by 1.6 m, area 3.84 m², so 7 desks with space left over.",
            "Scale, then divide.", "A"),
           ("C.4.9", "A garden bed is 4 m by 1.5 m and needs 60 mm of water a week. "
            "Investigate the weekly volume and the roof area needed at 0.8 efficiency and 20 "
            "mm of weekly rain.",
            "360 litres a week; a roof of 22.5 m² is needed.", "Multiply and rearrange.", "R"),
           ("C.4.10", "A design's total cost over n years is C = 500 + 30 × 1.06ⁿ⁻¹. "
            "Investigate the year in which the running cost first exceeds the capital cost.",
            "After about 23 years, when the series passes 500.",
            "Solve the geometric sum inequality.", "C"),
           ("C.4.11", "A school courtyard of 10 m² must provide seating, planting, a path "
            "and a tank of at least 500 litres. Investigate whether a tank of radius 0.5 m "
            "and height 0.7 m fits within the 10% of the area allowed for it.",
            "The tank's base is about 0.785 m², which is 7.9% of 10 m², so it fits.",
            "Compare the base area with the allowed share.", "R"),
           ("C.4.12", "Explain, with a design of your own, when a design that meets every "
            "stated constraint is still unacceptable.",
            "Any answer is acceptable if it identifies a need that was never written down as "
            "a constraint, such as safety, privacy or maintenance access.",
            "Give a specific example.", "R")],
    ),
    assessment=[
        dict(title="A1 · The courtyard design",
             text="A school courtyard measures 7.2 m by 4.8 m on a plan drawn at 1 : 50. The "
                  "brief requires at least 45% planting, at most 30% paths, at least 6 m² of "
                  "seating, and a rainwater tank of at least 500 litres. Design a layout that "
                  "meets every constraint, give the area of each part, choose a tank and "
                  "justify its size, and state the running cost over 5 years with a stated "
                  "assumption about its change.",
             note="Criteria A and D · model the layout, check every constraint, and justify "
                  "the choice of tank and the cost model."),
        dict(title="A2 · The review",
             text="A design provides 5.5 m² of seating, 2.0 m² of paths and 1.14 m² of "
                  "planting in a courtyard of 8.64 m². A survey of 30 users finds 18 who want "
                  "more shade and 12 who want more seating. Test the design against the brief "
                  "in task A1, report the survey with its margin of error, and write a "
                  "recommendation that states what the evidence supports and what it does "
                  "not.",
             note="Criteria B and C · test each constraint, interpret the survey within its "
                  "limits, and justify the recommendation."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of measurement, space and "
        "change appear in your work?",
        "How is the global context of globalisation and sustainability, and its exploration of "
        "designing places that meet present needs without exhausting future resources, visible "
        "in the investigations and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a mathematical model for a decision about a shared space, "
        "and what would you still like to ask?",
    ],
    review=dict(
        ideas=["A constraint is a quantity with a bound, and a design must satisfy all of "
               "them.",
               "A scale drawing divides lengths by the scale factor and areas by its square.",
               "The areas of the parts of a plan must sum to the area of the whole.",
               "The capacity of a tank is its volume, and the duration is capacity divided by "
               "demand.",
               "The volume collected from a roof is area times depth times efficiency.",
               "A running cost that rises by a percentage is a geometric series.",
               "The comparison of two designs depends on the time horizon.",
               "A survey's margin of error is about 1/√n."],
        vocab=["brief", "constraint", "feasible", "scale drawing", "capacity", "demand",
               "capital cost", "running cost", "payback period", "margin of error",
               "assumption", "review"],
        mixed=[("14.R1", "A plan at 1 : 50 measures 7.2 cm by 4.8 cm. Find the real area."),
               ("14.R2", "Find the capacity in litres of a cylinder of radius 0.5 m and "
                         "height 1 m."),
               ("14.R3", "A roof of 30 m² collects 800 mm of rain at 0.8 efficiency. Find "
                         "the volume."),
               ("14.R4", "A tank of 2000 litres supplies 50 litres a day. Find the "
                         "duration."),
               ("14.R5", "A cost of 400 dollars has maintenance of 20 dollars rising 5% a "
                         "year. Find the 5-year total."),
               ("14.R6", "Explain why a design that meets every stated constraint can still "
                         "be unacceptable.")],
    ),
    projects=dict(
        service=[("Community need", "Shared spaces are designed and changed without "
                                    "measuring the needs they must serve."),
                 ("Mathematical connection", "Measurement, area, capacity, cost and data."),
                 ("Proposed action", "Model one real space, check it against a written brief, "
                                     "and publish the review."),
                 ("Expected impact", "A group can see which constraints its space meets and "
                                     "which it fails."),
                 ("Student reflection", "Record the brief, the measurements and the verdict.")],
        community=[("Project idea", "A sustainable redesign of one community space."),
                   ("Need", "A courtyard, a market corner or a waiting area is unused or "
                            "uncomfortable."),
                   ("Research question", "What would a space that meets the users' measured "
                                         "needs look like, and what would it cost?"),
                   ("Mathematics", "Scale, area, capacity, cost and survey data."),
                   ("Action or outcome", "A design report with a scale plan, the "
                                         "calculations and a review."),
                   ("Beneficiaries", "Everyone who uses the space."),
                   ("Evidence", "The report with the plan, the calculations and the survey.")],
        personal=[("Personal interest", "A room, a desk or a corner that is yours."),
                  ("Learning goal", "To design a space that meets constraints you have "
                                    "measured yourself."),
                  ("Product or outcome", "A design report with a plan and a costed "
                                         "recommendation."),
                  ("Mathematics", "Scale, area, capacity, cost and data."),
                  ("Process", "Measure, model, cost and review, stating every assumption."),
                  ("Evidence", "The report with the plan, the calculations and the review.")],
    ),
),
])

# APPEND-CHAPTERS-HERE
