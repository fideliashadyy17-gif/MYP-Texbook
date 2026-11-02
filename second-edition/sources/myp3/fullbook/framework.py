#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Authored editorial framework for the MYP 3 second-edition coursebook.

Content reference: the pre-rewrite MYP 3 chapter and subtopic audit
(``second-edition/audit/chapter-audits/myp3-audit.md`` and the chapter and
subtopic registers). Chapter scope and teaching order follow that audit; the
teaching sequence, investigations, worked examples, practice sets, assessment
tasks and project connections are author-designed material written for this
second edition.

Every chapter is built as a complete MYP unit from the start: an official global
context with its official exploration, a statement of inquiry that names the key
concept and the related concepts, three question categories derived from the
same elements, an inquiry question opening every investigation, and Criterion
A-D practice written to exercise that unit rather than to repeat a drill.
"""
import diagrams2

LEVEL = 3
AUTHOR = "SADIKOU MOUKODDIM"

SERIES = dict(
    name="MYP Mathematics",
    line="MYP Mathematics · Student coursebook",
    edition="Second edition",
)

# Five-volume collection. MYP 1 and MYP 2 are produced; MYP 3 is the volume in
# hand; MYP 4 and MYP 5 do not exist yet and are shown as coordinated cover
# concepts only.
COLLECTION = [
    dict(level=1, status="published", theme="Year 1 · number, algebra, shape and data"),
    dict(level=2, status="published", theme="Year 2 · ratio, algebra, geometry, probability"),
    dict(level=3, status="this volume", theme="Year 3 · proof, models and evidence"),
    dict(level=4, status="forthcoming", theme="Year 4 · inquiry, practice, assessment"),
    dict(level=5, status="forthcoming", theme="Year 5 · modelling, proof, transition"),
]

PARTS = {
    1: "Part I · Number and abstraction",
    2: "Part I · Number and abstraction",
    3: "Part II · Algebra and models",
    4: "Part II · Algebra and models",
    5: "Part II · Algebra and models",
    6: "Part III · Shape, space and proof",
    7: "Part III · Shape, space and proof",
    8: "Part III · Shape, space and proof",
    9: "Part IV · Data and evidence",
    10: "Part IV · Data and evidence",
}

CRITERIA = {
    "A": ("Knowing and understanding", "a"),
    "B": ("Investigating patterns", "b"),
    "C": ("Communicating", "c"),
    "D": ("Applying mathematics in real-life contexts", "d"),
}

# ------------------------------------------------------------------ formula bank
FORMULAS = [
    ("The real number system", [
        ("Rational number", "any number that can be written as a/b with integers a, b and b ≠ 0; its decimal either terminates or recurs."),
        ("Irrational number", "a number that cannot be written as a fraction; its decimal neither terminates nor recurs."),
        ("Surd", "an exact irrational root, such as √2 or 3√5."),
        ("Absolute value", "|x| is the distance of x from 0 on a number line."),
        ("Interval notation", "[a, b] includes both ends; (a, b) excludes both; [a, b) includes a only."),
        ("Set notation", "A ∪ B is the union, A ∩ B the intersection, A′ the complement."),
    ]),
    ("Powers, roots and notation", [
        ("Product law", "aᵐ × aⁿ = aᵐ⁺ⁿ."),
        ("Quotient law", "aᵐ ÷ aⁿ = aᵐ⁻ⁿ for a ≠ 0."),
        ("Power law", "(aᵐ)ⁿ = aᵐⁿ."),
        ("Zero and negative indices", "a⁰ = 1 for a ≠ 0; a⁻ⁿ = 1/aⁿ."),
        ("Rational index", "a^(1/n) is the nth root of a; a^(m/n) = (ⁿ√a)ᵐ."),
        ("Scientific notation", "a × 10ⁿ with 1 ≤ a < 10."),
        ("Significant figures", "the digits that carry measured meaning, counted from the first non-zero digit."),
    ]),
    ("Algebra and functions", [
        ("Function", "a rule that gives exactly one output for each input in its domain."),
        ("Domain and range", "the set of permitted inputs and the set of resulting outputs."),
        ("Expanding", "a(b + c) = ab + ac."),
        ("Difference of squares", "a² − b² = (a − b)(a + b)."),
        ("Perfect square", "a² + 2ab + b² = (a + b)²."),
        ("Rearranging a formula", "apply the same inverse operation to both sides to isolate the wanted letter."),
        ("nth term", "a linear sequence has term = mn + c; a quadratic sequence has constant second difference."),
    ]),
    ("Linear models and systems", [
        ("Straight line", "y = mx + c, where m is the gradient and c the y-intercept."),
        ("Gradient", "m = (y₂ − y₁) ÷ (x₂ − x₁), the change in y per unit change in x."),
        ("Direct proportion", "y = kx, a straight line through the origin."),
        ("Simultaneous equations", "solve by substitution or elimination; check in both equations."),
        ("Inequality", "multiplying or dividing by a negative number reverses the inequality sign."),
    ]),
    ("Shape, space and trigonometry", [
        ("Congruence", "SSS, SAS, ASA, RHS for triangles."),
        ("Similarity", "corresponding angles equal and corresponding sides in the same ratio."),
        ("Pythagoras", "a² + b² = c² for the hypotenuse c of a right-angled triangle."),
        ("Trigonometric ratios", "sin θ = opposite/hypotenuse, cos θ = adjacent/hypotenuse, tan θ = opposite/adjacent."),
        ("Angles of elevation and depression", "measured from the horizontal, and equal by alternate angles."),
        ("Prism", "volume = area of cross-section × length; surface area is the sum of the face areas."),
        ("Cylinder", "volume = πr²h; curved surface area = 2πrh; total surface area = 2πrh + 2πr²."),
        ("Pyramid", "volume = ⅓ × base area × perpendicular height."),
        ("Cone", "volume = ⅓πr²h; curved surface area = πrl, where l is the slant height."),
        ("Sphere", "volume = ⁴⁄₃πr³; surface area = 4πr²."),
        ("Density", "density = mass ÷ volume."),
    ]),
    ("Data, probability and evidence", [
        ("Bivariate data", "paired measurements of two variables for the same subject."),
        ("Correlation", "the strength and direction of a linear association, measured by r with −1 ≤ r ≤ 1."),
        ("Line of best fit", "a line drawn through the middle of a scatter so that the residuals are balanced."),
        ("Interpolation and extrapolation", "predicting inside or outside the range of the collected data."),
        ("Causation", "correlation alone never establishes cause; a mechanism or a controlled study is required."),
        ("Probability of an event", "P(event) = favourable outcomes ÷ total equally likely outcomes."),
        ("Compound events", "P(A and B) = P(A) × P(B) for independent events; P(A or B) = P(A) + P(B) − P(A and B)."),
        ("Sample and population", "a sample estimates a population parameter; bias makes the estimate unreliable."),
        ("Base rate", "the underlying frequency of an event in the whole population, needed to interpret a test result."),
    ]),
]

# ---------------------------------------------------------------------- glossary
GLOSSARY = [
    ("Absolute value", "The distance of a number from zero on a number line, written |x|.", 1),
    ("Base rate", "The frequency of an event in the whole population, before any test result is known.", 10),
    ("Bias", "A systematic error that makes a sample unrepresentative of the population.", 10),
    ("Bivariate data", "Paired measurements of two variables recorded for the same subject.", 9),
    ("Causation", "A relationship in which changing one variable produces the change in the other.", 9),
    ("Complement (probability)", "The set of outcomes that are not in the event; P(not A) = 1 − P(A).", 10),
    ("Composite solid", "A solid made by joining two or more simpler solids.", 8),
    ("Congruent", "Identical in shape and size; for triangles, SSS, SAS, ASA or RHS proves it.", 6),
    ("Conjecture", "A mathematical claim believed to be true but not yet justified.", 1),
    ("Continuous data", "Numerical data that can take any value in an interval.", 9),
    ("Correlation", "The strength and direction of a linear association between two variables.", 9),
    ("Correlation coefficient", "A number r between −1 and 1 that measures linear association.", 9),
    ("Cross-section", "The shape exposed when a solid is cut parallel to a face.", 8),
    ("Density", "Mass per unit volume, in g/cm³ or kg/m³.", 8),
    ("Direct proportion", "A relationship y = kx whose graph is a straight line through the origin.", 4),
    ("Discrete data", "Numerical data that counts separate values.", 9),
    ("Domain", "The set of permitted inputs of a function.", 3),
    ("Elimination", "Solving simultaneous equations by adding or subtracting to remove one variable.", 5),
    ("Function", "A rule that gives exactly one output for each permitted input.", 3),
    ("Gradient", "The change in y per unit change in x; the steepness of a line.", 4),
    ("Interpolation", "Predicting a value inside the range of the collected data.", 9),
    ("Interval", "A continuous set of numbers between two endpoints, written with square or round brackets.", 1),
    ("Irrational number", "A number that cannot be written as a fraction; its decimal neither terminates nor recurs.", 1),
    ("Line of best fit", "A line drawn through the middle of a scatter so that the residuals balance.", 9),
    ("Mutually exclusive", "Events that cannot both happen, so P(A or B) = P(A) + P(B).", 10),
    ("nth term", "A rule that gives the term in any position of a sequence.", 3),
    ("Population", "The whole group a claim is about.", 10),
    ("Pythagoras' theorem", "In a right-angled triangle, a² + b² = c² for the hypotenuse c.", 7),
    ("Range (of a function)", "The set of outputs a function can produce.", 3),
    ("Rational number", "A number that can be written as a fraction of two integers.", 1),
    ("Sample", "The part of a population that is actually measured.", 10),
    ("Scatter plot", "A graph of paired data used to look for association.", 9),
    ("Scientific notation", "A number written as a × 10ⁿ with 1 ≤ a < 10.", 2),
    ("Significant figures", "The digits of a measurement that carry meaning, counted from the first non-zero digit.", 2),
    ("Similar", "Same shape, possibly different size: corresponding angles equal, sides in ratio.", 7),
    ("Simultaneous equations", "Two or more equations that must be true at the same time.", 5),
    ("Slant height", "The distance from the apex of a cone or pyramid to the edge of its base.", 8),
    ("Substitution", "Replacing a variable by a value or by an equal expression.", 3),
    ("Surd", "An exact irrational root left in root form, such as √2.", 1),
    ("Tessellation", "A covering of the plane by shapes that meet edge to edge with no gaps.", 6),
    ("Trigonometric ratio", "Sine, cosine or tangent: a ratio of two sides of a right-angled triangle.", 7),
    ("Union and intersection", "A ∪ B contains what is in either set; A ∩ B only what is in both.", 1),
    ("y-intercept", "The value of y where a line crosses the y-axis.", 4),
]

FRONT = dict(
    cover=dict(
        kicker="MYP Mathematics · Student coursebook",
        edition="Second edition",
        title="Mathematics",
        level="3",
        level_text="Student coursebook",
        level_note="MYP 3 · Year 3 · ten chapters in four parts",
        standfirst="A concept-driven inquiry course in number, algebra, shape and space, "
                   "trigonometry, data and probability. You investigate, justify and prove, "
                   "then reason, communicate and apply.",
        topics=["The real number system", "Powers and notation", "Functions and expressions",
                "Linear models", "Equations and systems", "Transformations and congruence",
                "Similarity and trigonometry", "Three-dimensional solids", "Bivariate data",
                "Probability and evidence"],
        criteria=[("A", "Knowing and understanding"), ("B", "Investigating patterns"),
                  ("C", "Communicating"), ("D", "Applying mathematics in real-life contexts")],
        inquiry_label="How this book works",
        inquiry="Every chapter opens with a task. You investigate, notice a pattern, state a "
                "mathematical conclusion and justify it before you meet the formal explanation.",
        author=AUTHOR,
        series="MYP Mathematics · Volume 3 of 5",
    ),
    imprint=dict(
        title="About this edition",
        credit="Author",
        author=AUTHOR,
        body=[
            "This is the second edition of the MYP 3 mathematics coursebook. It was rebuilt from the pre-rewrite MYP 3 audit, which recorded the chapter scope, the key and related concepts, the global contexts and the inquiry questions of the earlier edition, and identified where the teaching had to be strengthened.",
            "The edition keeps that chapter scope and the visual identity of the collection, and rebuilds the teaching sequence around inquiry: engagement, inquiry questions, investigation, observation, mathematical conclusion, formal development, worked examples, extensive visual practice, and application, assessment and reflection.",
            "Year 3 asks more of Criterion C than Year 2: reasoning must now be organised into a logical structure, and Criterion B moves from recognising and verifying a pattern to justifying a generalisation. The chapters train both explicitly.",
            "All classroom data sets are simulated and are labelled as such. Real data would require provenance, so no claim in this book rests on unverified statistics.",
            "No publisher, ISBN, print specification or commercial print-readiness claim is made in this file. The book is produced as an A4 review copy: fonts are embedded, pagination is continuous and every page has been checked for overflow.",
        ],
    ),
    howto=dict(
        title="How to use this book",
        intro="Each chapter follows the same sequence, so you always know what is coming next. The "
              "sequence is deliberate: you investigate before you are told the rule, because a rule "
              "you have discovered is a rule you can defend — and defending it is what Year 3 asks of you.",
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
            ("B · Investigating patterns", "Investigate relationships, describe patterns, formulate a conjecture, test it and justify the generalisation — at Year 3 level a justification is a logical argument, not a list of examples."),
            ("C · Communicating", "Use correct mathematical language, notation and complete representations, and organise reasoning into a coherent structure that a reader can follow."),
            ("D · Applying mathematics in real-life contexts", "Apply mathematics to authentic situations, identify relevant information, and comment on the accuracy and sense of the result."),
        ],
        notes=[
            "Practice is separated by criterion so that you can see which skill a task is training. Criterion B practice is additional genuine pattern investigation, not a repeat of the teaching.",
            "Visuals are part of the mathematics. Where a task supplies a diagram, grid, table, number line or model, use it; where it asks you to sketch, your drawing is part of the answer.",
            "Answers and student-facing reasoning are collected at the back of the book, with a formula bank, a glossary and references.",
            "Every chapter ends with project connections: a Service as Action opportunity, a Community Project connection and a Personal Project connection for MYP 5.",
        ],
    ),
    intro=dict(
        title="MYP mathematics and this coursebook",
        paras=[
            "The IB Middle Years Programme asks students to inquire into concepts through global contexts, to develop approaches to learning (ATL) skills, and to act on what they learn through service as action. In mathematics this means more than practising procedures: students investigate patterns, justify generalisations, communicate with precise language and apply mathematics to situations that matter to them.",
            "MYP mathematics is organised into four branches — number, algebra, geometry and trigonometry, and statistics and probability — and the programme recommends at least 50 hours of teaching per subject each year. This coursebook covers the Year 3 content of those branches across ten chapters, grouped into four parts.",
            "Year 3 is the level at which justification becomes central. A pattern spotted in three cases is a conjecture; a pattern shown to follow from something already established is a theorem. The chapters in this book keep that distinction visible, and the practice under each criterion says which kind of thinking it is training.",
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
            "Ten chapters that take the real number system, powers and notation, functions, linear models, systems, transformations, similarity, trigonometry, three-dimensional measurement, bivariate data and probability from first ideas to justified use. Each chapter opens with a task: you investigate, notice a pattern, state a mathematical conclusion you can defend, and only then meet the formal explanation — with worked examples that model a complete solution and practice separated into Criterion A, B, C and D sets so you can see which skill each task trains.",
            "Year 3 reasoning is organised, not just correct: Criterion C tasks ask you to structure an argument, and Criterion B tasks ask you to justify a generalisation rather than to list cases. Every chapter closes with a reflection that returns to the statement of inquiry.",
            "Every chapter also closes with a Service as Action opportunity, a Community Project connection and a Personal Project extension for MYP 5. The back of the book carries complete student-facing answers with reasoning, a formula bank, a glossary and references.",
        ],
        collection_heading="MYP Mathematics · the five-volume collection",
        collection_note="One inquiry-led course from Year 1 to Year 5. Volumes 1 and 2 are "
                        "produced; volumes 4 and 5 are in preparation. The covers shown here are "
                        "coordinated collection designs, not published volumes.",
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
    num=1, title="The real number system",
    key="Form", related=["Quantity", "Equivalence"],
    context="Orientation in space and time",
    exploration="Natural and human landscapes and resources",
    inquiry=("The form of the real number system, and the equivalence between fractions, "
             "terminating decimals and recurring decimals, allow any position between two "
             "reference points to be described exactly, while the logic of proof shows that some "
             "positions on that line can never be written as a fraction."),
    atl=("Critical thinking",
         "In order for a student to evaluate a claim about all numbers, students must test the "
         "claim on several cases, search for a counterexample, and then decide whether a "
         "counterexample disproves the claim or widens the definition."),
    standfirst="Every fraction is a terminating or a recurring decimal. The converse is false, and "
               "the numbers that escape the fractions are the ones that make the number line "
               "continuous.",
    engage="A surveyor measures a plot of land and records 12.7 m, then 12.73 m, then 12.732 m. "
           "Each measurement is better, and none of them is the true length. What kind of number is "
           "the true length?",
    questions=[("Factual", "Which numbers can be written as fractions, and what are the only two "
                           "decimal forms a fraction can take?"),
               ("Conceptual", "Why can every fraction be written as a terminating or recurring "
                              "decimal, and why is the converse false?"),
               ("Debatable", "When a land boundary is recorded to the nearest centimetre, is the "
                             "recorded number the same number as the true distance, and does the "
                             "difference matter?")],
    application_lede="These tasks use fraction-decimal conversion, ordering, absolute value, "
                     "intervals, surds and set notation. State whether your answer is exact or a "
                     "rounded claim.",
    projects_lede="Land, resource and boundary problems are real-number problems. Use exact forms "
                  "where they exist, and say when a rounded value is the honest answer.",
    sections=[
        dict(id="1.1", title="Rational numbers and decimal form",
             inquiry_q=("How can every fraction be written as a decimal, and what are the only two "
                        "forms that decimal can take?"), teach=[
            "A rational number is any number that can be written as a/b where a and b are integers and b is not zero. Every integer is rational, because n = n/1.",
            "Dividing the numerator by the denominator gives a decimal that either stops (terminating) or settles into a repeating block (recurring). Nothing else can happen: the remainders in a long division can only take b different values, so one of them must eventually repeat.",
            "A terminating decimal is a fraction whose denominator has only the prime factors 2 and 5. A recurring decimal comes from any other denominator. This is why 3/8 terminates (8 = 2³) but 1/3 recurs.",
            "A recurring decimal is converted back to a fraction by multiplying by a power of 10 and subtracting, which cancels the repeating block.",
        ], examples=[
            dict(q="Write 5/8 and 7/12 as decimals, and say which one terminates and why.",
                 vis=F("table", [["fraction", "denominator", "prime factors", "decimal"],
                                 ["5/8", "8", "2 × 2 × 2", "0.625"],
                                 ["7/12", "12", "2 × 2 × 3", "0.5833…"]],
                       caption="Only the prime factors 2 and 5 give a terminating decimal."),
                 reasoning="A decimal terminates exactly when the denominator in simplest form has no prime factor other than 2 or 5.",
                 steps=["5/8: 8 = 2³, so 5 ÷ 8 = 0.625, which stops.",
                        "7/12: 12 = 2² × 3, and the factor 3 forces repetition.",
                        "7 ÷ 12 = 0.58333… = 0.58·3·, with the digit 3 repeating."],
                 ans="5/8 = 0.625 terminates; 7/12 = 0.58·3· recurs",
                 interp="The shape of the denominator decides the shape of the decimal, so the "
                        "fraction form carries information the decimal form hides."),
            dict(q="Convert 0.4·5· back to a fraction.",
                 vis=F("number_line", 0, 1, 0.1, [0.45], "0.45…", ""),
                 reasoning="Multiplying by a power of 10 shifts the repeating block, and subtracting removes it.",
                 steps=["Let x = 0.4555….",
                        "10x = 4.555…, and 100x = 45.555….",
                        "100x − 10x = 41, so 90x = 41.",
                        "x = 41/90."],
                 ans="0.4·5· = 41/90",
                 interp="Every recurring decimal is rational, so the recurring bar is a claim about "
                        "exactness, not about approximation."),
        ], inv=dict(
            task="Take the fractions 1/2, 1/3, 1/4, 1/6, 1/7, 1/8, 1/9, 1/11 and 1/12. Divide each "
                 "one out to at least eight decimal places and record whether the decimal stops, "
                 "repeats a single digit, or repeats a block of several digits. Then look at the "
                 "denominators.",
            fig=F("table", [["denominator", "prime factors", "decimal"],
                            ["2", "2", "0.5 stops"],
                            ["3", "3", "0.333… repeats"],
                            ["4", "2 × 2", "0.25 stops"],
                            ["6", "2 × 3", "0.1666… repeats"]],
                  caption="Terminating decimals come from denominators built only from 2s and 5s."),
            table=[["fraction", "decimal", "stops or repeats", "denominator factors"],
                   ["1/2", "0.5", "stops", "2"],
                   ["1/3", "0.333…", "repeats one digit", "3"],
                   ["1/4", "0.25", "stops", "2 × 2"],
                   ["1/6", "0.1666…", "repeats one digit", "2 × 3"],
                   ["1/7", "0.142857…", "repeats six digits", "7"],
                   ["1/8", "0.125", "stops", "2 × 2 × 2"],
                   ["1/9", "0.111…", "repeats one digit", "3 × 3"],
                   ["1/11", "0.0909…", "repeats two digits", "11"],
                   ["1/12", "0.08333…", "repeats one digit", "2 × 2 × 3"]],
            notice=["Every fraction gave either a stopping decimal or a repeating one — never a "
                    "decimal that wandered without repeating.",
                    "The denominators that stop are built only from the primes 2 and 5.",
                    "1/7 repeats a block of six digits, and 7 − 1 = 6, which is not a coincidence."],
            obs="Long division of a fraction can only leave a limited number of remainders, so the "
                "decimal must stop or repeat.",
            concl="Every fraction can be written as a decimal, and that decimal is either "
                  "terminating or recurring — a terminating decimal exactly when the denominator "
                  "in simplest form has no prime factor other than 2 or 5.")),
        dict(id="1.2", title="Irrational numbers and surds",
             inquiry_q=("How can we show that a number exists on the number line that is not a "
                        "fraction?"), teach=[
            "An irrational number cannot be written as a/b for any integers a and b. Its decimal neither stops nor repeats, so it can never be written down in full — only named exactly (√2) or described (1.41421… to five decimal places).",
            "The standard proof that √2 is irrational is a proof by contradiction: assume √2 = a/b in simplest form, square both sides, and show that a and b must both be even, which contradicts simplest form.",
            "The parity argument is the engine of the proof. If a² = 2b² then a² is even, so a is even (because the square of an odd number is odd), so a = 2c, so 4c² = 2b², so b² is even, so b is even too.",
            "A surd is an exact irrational root left in root form. Keeping √2 as √2 is exact; writing 1.41 is a rounded claim that will not survive being squared.",
        ], examples=[
            dict(q="Prove that √2 is irrational.",
                 vis=F("number_line", 1, 2, 0.1, [1.4142], "√2", ""),
                 reasoning="Assume the opposite and derive a contradiction; a claim that leads to a "
                          "contradiction must be false.",
                 steps=["Suppose √2 = a/b with a and b integers, b ≠ 0, and the fraction in "
                        "simplest form.",
                        "Squaring gives 2 = a²/b², so a² = 2b².",
                        "Then a² is even, so a is even: write a = 2c.",
                        "Substituting: 4c² = 2b², so b² = 2c², so b² is even and b is even.",
                        "Both a and b are even, contradicting simplest form."],
                 ans="√2 is irrational",
                 interp="The contradiction came from the parity of a square, which is why no "
                        "fraction can land exactly on √2."),
            dict(q="Show that √3 is irrational, using the same structure of argument.",
                 vis=F("number_line", 1, 2, 0.1, [1.732], "√3", ""),
                 reasoning="The same contradiction argument works with any prime under the root, "
                          "because a prime dividing a square must divide the number itself.",
                 steps=["Suppose √3 = a/b in simplest form, so a² = 3b².",
                        "Then 3 divides a², and since 3 is prime, 3 divides a: write a = 3c.",
                        "Substituting gives 9c² = 3b², so b² = 3c², so 3 divides b.",
                        "Both a and b are divisible by 3, contradicting simplest form."],
                 ans="√3 is irrational",
                 interp="The argument transfers because the key fact — a prime dividing a square "
                        "divides the root — holds for every prime."),
        ], inv=dict(
            task="Draw a square of side 1 unit on grid paper and draw its diagonal. Use Pythagoras' "
                 "theorem to find the length of the diagonal, then try to write that length as a "
                 "fraction by testing denominators up to 20. Record how close each fraction gets.",
            fig=F("pythagoras", 1, 1, "a unit square and its diagonal"),
            table=[["fraction a/b", "value", "square of the value", "error against 2"],
                   ["7/5", "1.4", "1.96", "0.04"],
                   ["17/12", "1.41666…", "2.00694…", "0.00694…"],
                   ["41/29", "1.41379…", "1.99881…", "0.00119…"],
                   ["99/70", "1.41428…", "2.00020…", "0.00020…"],
                   ["239/169", "1.41420…", "1.99997…", "0.00003…"]],
            notice=["Every fraction lands close to the diagonal, and then misses it.",
                    "The errors get smaller, but they never reach zero.",
                    "The fractions that get close have larger and larger denominators."],
            obs="Fractions can approach the diagonal as closely as we like without ever landing on "
                "it, so the length of the diagonal is not a fraction.",
            concl="A proof by contradiction shows that no fraction can equal the diagonal of a unit "
                  "square, so √2 exists on the number line and is irrational.")),
        dict(id="1.3", title="Order, absolute value and intervals",
             inquiry_q=("How can every position on a line be described, and how does an interval "
                        "decide which positions are included?"), teach=[
            "The real numbers fill the number line with no gaps: every point is a real number and every real number is a point. Quantity and order are therefore the same idea on a line: to compare two quantities is to compare their positions. Rational and irrational numbers are both dense — between any two there is another of each kind.",
            "Absolute value measures distance from zero, so |x| = x when x ≥ 0 and |x| = −x when x < 0. It turns an ordering question into a distance question.",
            "An interval is the set of numbers between two endpoints. Square brackets include the endpoint, round brackets exclude it, and mixing them gives a half-open interval.",
            "Interval and set notation are two languages for the same object: [1, 4) is {x : 1 ≤ x < 4}, and the complement of that set is everything outside it.",
        ], examples=[
            dict(q="Solve |x − 3| < 2 and write the answer as an interval.",
                 vis=F("number_line", 0, 6, 1, [3], "|x − 3| < 2", ""),
                 reasoning="Absolute value measures distance, so |x − 3| < 2 means x is less than 2 "
                          "units from 3.",
                 steps=["|x − 3| < 2 means −2 < x − 3 < 2.",
                        "Add 3 to all three parts: 1 < x < 5.",
                        "As an interval: (1, 5)."],
                 ans="x ∈ (1, 5)",
                 interp="Reading absolute value as distance turns an inequality into a picture of a "
                        "line segment."),
            dict(q="Write {x : −3 ≤ x < 2} in interval notation, and describe its complement.",
                 vis=F("number_line", -4, 3, 1, [-3, 2], "[−3, 2)", ""),
                 reasoning="A square bracket keeps the endpoint and a round bracket removes it, so "
                          "the notation records inclusion directly.",
                 steps=["−3 is included and 2 is excluded, so the interval is [−3, 2).",
                        "The complement is everything outside: x < −3 or x ≥ 2.",
                        "In interval notation: (−∞, −3) ∪ [2, ∞)."],
                 ans="[−3, 2), with complement (−∞, −3) ∪ [2, ∞)",
                 interp="The two notations disagree only about the endpoints, which is exactly the "
                        "information a surveyor needs."),
        ], inv=dict(
            task="On a number line from −4 to 6, mark the intervals [−3, 1], (−3, 1], [−3, 1) and "
                 "(−3, 1). For each one, list three numbers that belong to it and one number that "
                 "does not. Then find two intervals whose union is [−4, 6] and whose intersection is "
                 "a single number.",
            fig=F("number_line", -4, 6, 1, [-3, 1], "two endpoints, four intervals", ""),
            table=[["interval", "includes −3", "includes 1", "an example inside", "an example outside"],
                   ["[−3, 1]", "yes", "yes", "−3", "1.5"],
                   ["(−3, 1]", "no", "yes", "0", "−3"],
                   ["[−3, 1)", "yes", "no", "−2.5", "1"],
                   ["(−3, 1)", "no", "no", "0.5", "1"]],
            notice=["The four intervals differ only at the two endpoints.",
                    "Every interval contains infinitely many numbers, including irrationals.",
                    "The union of [−3, 1] and (1, 6] is [−3, 6], and their intersection is empty."],
            obs="Square and round brackets record exactly which endpoints belong, and the union and "
                "intersection of intervals follow from that.",
            concl="An interval is the set of numbers between two endpoints, and the bracket type "
                  "decides inclusion: [a, b] includes both ends, (a, b) excludes both, and the mixed "
                  "forms include exactly one.")),
        dict(id="1.4", title="Working with surds",
             inquiry_q=("How can an irrational quantity be written exactly and still be calculated "
                        "with?"), teach=[
            "Surds obey the same rules as powers with fractional indices: √a × √b = √(ab), and √a ÷ √b = √(a/b) for non-negative a and b.",
            "Simplifying a surd means taking out the largest square factor: √72 = √(36 × 2) = 6√2. The simplified form is unique, which makes it a good form for comparing.",
            "Rationalising a denominator replaces a surd in a denominator by an integer, by multiplying top and bottom by a conjugate. (1 + √2)(1 − √2) = 1 − 2 = −1, so the surd disappears.",
            "Adding surds needs like surds: 3√2 + 5√2 = 8√2, but 3√2 + 5√3 cannot be simplified. Treating √2 as if it were √3 is the standard error.",
        ], examples=[
            dict(q="Simplify √200 and rationalise 6/√3.",
                 vis=F("table", [["expression", "square factors", "simplified"],
                                 ["√200", "200 = 100 × 2", "10√2"],
                                 ["6/√3", "× √3/√3", "2√3"]],
                       caption="Take out the largest square factor, then clear the surd denominator."),
                 reasoning="Simplifying removes square factors, and multiplying by a conjugate "
                          "clears a surd from a denominator without changing the value.",
                 steps=["√200 = √(100 × 2) = 10√2.",
                        "6/√3 = (6 × √3)/(√3 × √3) = 6√3/3.",
                        "6√3/3 = 2√3."],
                 ans="√200 = 10√2 and 6/√3 = 2√3",
                 interp="Both answers are exact; writing 1.732… would lose the ability to check the "
                        "work by squaring."),
            dict(q="Show that (2 + √3)(2 − √3) = 1, and use it to rationalise 5/(2 + √3).",
                 vis=F("table", [["pair", "product"],
                                 ["2 + √3 and 2 − √3", "4 − 3 = 1"],
                                 ["5/(2 + √3)", "5(2 − √3) = 10 − 5√3"]],
                       caption="Conjugate pairs differ only in the sign between the terms."),
                 reasoning="The product of a conjugate pair is rational, so multiplying by the "
                          "conjugate is a legitimate way to clear a surd denominator.",
                 steps=["(2 + √3)(2 − √3) = 4 − 2√3 + 2√3 − 3 = 1.",
                        "5/(2 + √3) = 5(2 − √3)/((2 + √3)(2 − √3)).",
                        "= 5(2 − √3)/1 = 10 − 5√3."],
                 ans="5/(2 + √3) = 10 − 5√3",
                 interp="The conjugate works because the cross terms cancel, leaving only rational "
                        "numbers."),
        ], inv=dict(
            task="Take the surds √8, √18, √50 and √72. Simplify each one, then add them in pairs. "
                 "Then try to simplify √2 + √3 and record what happens. Finally, find a fraction "
                 "with denominator 3 + √2 that has an integer denominator.",
            table=[["surd", "largest square factor", "simplified"],
                   ["√8", "4", "2√2"],
                   ["√18", "9", "3√2"],
                   ["√50", "25", "5√2"],
                   ["√72", "36", "6√2"],
                   ["√2 + √3", "none", "cannot be simplified"]],
            notice=["All four surds simplify to a multiple of √2.",
                    "2√2 + 3√2 + 5√2 + 6√2 = 16√2, but only because they are all like surds.",
                    "√2 + √3 resists simplification because the surds are different.",
                    "Multiplying 1/(3 + √2) by (3 − √2)/(3 − √2) gives (3 − √2)/7."],
            obs="Only like surds combine, and a surd denominator can always be cleared by "
                "multiplying by the conjugate.",
            concl="A surd can be written exactly and calculated with by taking out square factors, "
                  "collecting like surds and rationalising with a conjugate — and the simplified "
                  "form is unique.")),
        dict(id="1.5", title="Sets, logic and proof",
             inquiry_q=("How can a claim about all numbers be proved rather than tested?"), teach=[
            "A set is a collection of objects, described by listing its elements or by a rule. The universal set is everything under discussion, and the complement of A is everything in the universal set that is not in A.",
            "Union gathers what is in either set; intersection keeps only what is in both. These two operations behave like 'or' and 'and' in logic, and Venn diagrams make the difference visible.",
            "A universal claim ('every fraction has a recurring or terminating decimal') cannot be proved by examples. It needs an argument that works for all cases, and a single counterexample destroys it.",
            "Proof by contradiction assumes the claim is false and derives an impossible consequence. It is the tool that proves √2 is irrational, and it is used again in Chapter 7 to prove Pythagoras-related results.",
        ], examples=[
            dict(q="A = {x : x is a factor of 12} and B = {x : x is a factor of 18}. List A ∪ B and A ∩ B.",
                 vis=F("venn", "A", "B", "1", "2, 3, 4, 6, 12", "9, 18"),
                 reasoning="Union collects everything in either set; intersection keeps only the "
                          "common elements.",
                 steps=["A = {1, 2, 3, 4, 6, 12} and B = {1, 2, 3, 6, 9, 18}.",
                        "A ∪ B = {1, 2, 3, 4, 6, 9, 12, 18}.",
                        "A ∩ B = {1, 2, 3, 6}."],
                 ans="A ∪ B = {1, 2, 3, 4, 6, 9, 12, 18}; A ∩ B = {1, 2, 3, 6}",
                 interp="The intersection is the common structure the two sets share, which is why "
                        "it is the useful part for comparing."),
            dict(q="Show that the claim 'the product of two irrational numbers is irrational' is "
                   "false.",
                 vis=F("table", [["first number", "second number", "product"],
                                 ["√2", "√2", "2"],
                                 ["√2", "2√2", "4"]],
                       caption="One counterexample is enough to destroy a universal claim."),
                 reasoning="A universal claim fails if a single case contradicts it, so a "
                          "counterexample is a complete refutation.",
                 steps=["The claim says: for all irrational a and b, ab is irrational.",
                        "Take a = √2 and b = √2. Both are irrational.",
                        "ab = √2 × √2 = 2, which is rational.",
                        "So the claim is false."],
                 ans="False — √2 × √2 = 2",
                 interp="Finding one counterexample is faster than testing many cases, and it is "
                        "decisive."),
        ], inv=dict(
            task="Test four claims about numbers. For each one, either find a counterexample or "
                 "write down why you believe it is true for every case: (1) the sum of two rational "
                 "numbers is rational; (2) the sum of two irrational numbers is irrational; (3) a "
                 "non-zero rational number times an irrational number is irrational; (4) there is a "
                 "rational number between any two rational numbers.",
            table=[["claim", "counterexample or argument", "verdict"],
                   ["rational + rational is rational", "a/b + c/d = (ad + bc)/bd, a fraction", "true for all"],
                   ["irrational + irrational is irrational", "√2 + (−√2) = 0", "false"],
                   ["rational × irrational is irrational", "if qr = s then r = s/q is rational", "true for q ≠ 0"],
                   ["a rational lies between any two rationals", "(p/q + r/s)/2 is rational and between them", "true for all"]],
            notice=["Two claims were destroyed by a single counterexample each.",
                    "Two claims survived because an argument covered every case.",
                    "The average of two numbers always lies between them, which is why the rationals "
                    "are dense."],
            obs="Examples can disprove a universal claim but never prove one; proving requires an "
                "argument that covers every case.",
            concl="A universal claim is proved by an argument that works for all cases and "
                  "disproved by one counterexample, which is why proof and counterexample are "
                  "complementary tools.")),
    ],
    practice=dict(
        A=[("1.1.1", "Write 7/8, 5/6 and 11/40 as decimals and say which terminate and why.",
            "0.875 stops; 0.8·3· recurs; 0.275 stops",
            "Denominators of only 2s and 5s terminate: 8 = 2³ and 40 = 2³ × 5.", "F"),
           ("1.1.2", "Convert 0.·2·7· into a fraction.",
            "3/11", "Let x = 0.2727…; 100x − x = 27, so 99x = 27.", "F"),
           ("1.1.3", "Explain why 1/7 must produce a recurring decimal.",
            "The remainder in the division can only be 0–6, so one must repeat.",
            "Only seven remainders are possible, so the decimal cannot go on without repeating.", "R"),
           ("1.1.4", "A land record gives a boundary as 0.3·7· m. Write this as a fraction.",
            "37/99 m", "0.3737… = 37/99.", "F"),
           ("1.1.5", "Is 0.10100100010000… rational? Justify your answer.",
            "No — the blocks grow, so the decimal never repeats.",
            "A rational decimal either stops or repeats a fixed block.", "R"),
           ("1.1.6", "Write 22/7 as a decimal to four places and state whether it is exact.",
            "3.1429 (rounded); the exact value is 22/7",
            "22/7 recurs, so any finite decimal is a rounded claim.", "A"),
           ("1.1.7", "Sort these into rational and irrational: 0.25, √5, 7/3, π, −4, 0.·1·.",
            "Rational: 0.25, 7/3, −4, 0.·1·; irrational: √5, π",
            "Recurring and terminating decimals are rational; π and √5 are not fractions.", "F"),
           ("1.1.8", "Find a fraction between 1/3 and 1/2, and explain how you know it is between them.",
            "5/12", "1/3 = 4/12 and 1/2 = 6/12, so 5/12 lies between.", "R"),
           ("1.1.9", "A resource of 3/5 of a hectare is recorded as 0.6 ha. Is this exact?",
            "Yes — 3/5 = 0.6 exactly",
            "The denominator 5 gives a terminating decimal.", "A"),
           ("1.1.10", "Explain the difference between 0.·9· and 0.9999.",
            "0.·9· = 1 exactly; 0.9999 is a rounded value below 1.",
            "A recurring decimal is exact, while a finite decimal is a claim about rounding.", "R"),
           ("1.1.11", "Convert 0.0·4·5· into a fraction.",
            "1/22",
            "Let x = 0.04545…; then 100x = 4.5454… and 10x = 0.4545…, so 90x = 4.0909… − 0.4545… "
            "= 3.6363… = 40/11 and x = 1/22.", "C"),
           ("1.1.12", "Why is every integer a rational number?",
            "Because n = n/1", "The definition only requires a quotient of two integers.", "F")],
        B=[("1.2.1", "Prove that √5 is irrational.",
            "Assume √5 = a/b in simplest form; then 5 divides a², so 5 divides a, so 5 divides b — a contradiction.",
            "A prime dividing a square divides the number itself.", "R"),
           ("1.2.2", "Investigate: is √(2/3) rational or irrational? Justify.",
            "Irrational", "If √(2/3) were rational, its square 2/3 would have a rational square root, which would make 6 rational after clearing denominators.", "R"),
           ("1.2.3", "Find a counterexample to 'the square of an irrational number is irrational'.",
            "√2 × √2 = 2", "One counterexample refutes the claim.", "R"),
           ("1.2.4", "Investigate the sequence of approximations 1, 1.4, 1.41, 1.414, 1.4142 to √2. What is happening to the error?",
            "The error falls by roughly a factor of 10 each time, but never reaches zero.",
            "Each added decimal place improves the approximation tenfold.", "R"),
           ("1.2.5", "Test the claim: between any two irrational numbers there is a rational number.",
            "True — take the average of the two numbers and round it to a nearby fraction, or use a decimal truncation of the left-hand number.",
            "The rationals are dense on the number line.", "R"),
           ("1.2.6", "Investigate: is 2√3 greater than, equal to or less than 3√2? Justify without a calculator.",
            "2√3 = √12 and 3√2 = √18, so 2√3 < 3√2.",
            "Squaring both sides preserves the order for positive numbers.", "R"),
           ("1.2.7", "Generalise: what can you say about √n when n is not a perfect square?",
            "√n is irrational", "The contradiction proof works for any non-square integer n.", "R"),
           ("1.2.8", "Investigate the pattern √4, √9, √16, √25, √36. Write the next two terms and a rule.",
            "√49 = 7, √64 = 8; the rule is √(n²) = n",
            "Each term is the square root of a perfect square.", "F"),
           ("1.2.9", "Find two irrational numbers whose sum is rational, and explain what this shows.",
            "√2 and −√2, whose sum is 0",
            "Irrational numbers are not closed under addition.", "R"),
           ("1.2.10", "Test the claim: if x is irrational then 1/x is irrational.",
            "True for x ≠ 0 — otherwise 1/x = p/q would make x = q/p rational.",
            "The rationals are closed under division by a non-zero rational.", "R"),
           ("1.2.11", "Investigate: how many irrational numbers lie between 1 and 2?",
            "Infinitely many — for example 1 + √2/n for any positive integer n.",
            "Adding an irrational to a rational gives an irrational.", "R")],
        C=[("1.3.1", "Solve |x + 2| ≤ 5 and write the answer as an interval.",
            "−7 ≤ x ≤ 3, so [−7, 3]",
            "|x + 2| ≤ 5 means −5 ≤ x + 2 ≤ 5.", "F"),
           ("1.3.2", "Explain in words what |a − b| measures, and give an example with two towns.",
            "The distance between a and b on the number line",
            "Absolute value removes the direction and keeps the size of the gap.", "R"),
           ("1.3.3", "Write (−∞, 3) ∪ (3, ∞) in set notation and say what is missing.",
            "{x : x ≠ 3}; the single number 3 is excluded",
            "Union gathers both sides and the endpoint is in neither.", "F"),
           ("1.3.4", "Simplify √75 + √12 and explain why the two surds can be collected.",
            "7√3", "√75 = 5√3 and √12 = 2√3, and both are multiples of √3.", "F"),
           ("1.3.5", "Rationalise 4/(√5 − 1) and explain the role of the conjugate.",
            "√5 + 1", "(√5 + 1)(√5 − 1) = 4, so the product clears the surd.", "F"),
           ("1.3.6", "Explain why √2 + √3 cannot be simplified, using the definition of like surds.",
            "They are not multiples of the same surd.",
            "Only like surds combine, in the same way as like terms.", "R"),
           ("1.3.7", "A survey gives a distance as 3.6 m to one decimal place. Write the interval of "
                    "possible true distances.",
            "[3.55, 3.65) m",
            "Rounding to one decimal place includes the lower bound and excludes the upper.", "A"),
           ("1.3.8", "Explain the difference between 3.6 m and 3.60 m as a record of measurement.",
            "3.60 m claims precision to the nearest centimetre; 3.6 m claims only the nearest 10 cm.",
            "Trailing zeros record the precision of the instrument.", "R"),
           ("1.3.9", "Draw a Venn diagram for A = {even numbers} and B = {multiples of 3} inside the "
                     "universal set of the first 12 positive integers, and list A ∩ B.",
            "{6, 12}",
            "The intersection holds only the numbers with both properties.", "F"),
           ("1.3.10", "Explain why a proof by contradiction is not the same as finding a "
                      "counterexample.",
            "A counterexample disproves a universal claim; a contradiction proves one by ruling out "
            "the alternative.",
            "The two tools work in opposite directions.", "R"),
           ("1.3.11", "Write the complement of [−2, 5] in interval notation and describe it in words.",
            "(−∞, −2) ∪ (5, ∞)",
            "The complement keeps everything outside the interval, excluding both endpoints.", "F"),
           ("1.3.12", "A resource estimate is given as 4 × 10³ kg to one significant figure. Write the "
                      "interval of possible true values.",
            "[3500, 4500) kg",
            "One significant figure rounds to the nearest thousand, including the lower bound.", "A")],
        D=[("1.4.1", "A plot of land measures √50 m by √18 m. Find its exact area and a decimal "
                     "estimate to two places.",
            "30 m² exactly (√50 × √18 = √900 = 30)",
            "Multiplying surds multiplies the numbers under the root.", "A"),
           ("1.4.2", "A boundary is recorded as 12.7 m to the nearest 10 cm. Write the interval of "
                     "possible true lengths and say how wide it is.",
            "[12.65, 12.75) m, width 0.1 m",
            "Rounding to one decimal place gives an interval of width 0.1.", "A"),
           ("1.4.3", "Two farms measure 0.4·3· km² and 0.43 km². Which is larger, and by how much? "
                     "Give an exact answer.",
            "0.4·3· = 43/99 ≈ 0.4343, so it is larger by 1/99 − 0.43 ≈ 0.0043 km²",
            "Convert the recurring decimal to a fraction before comparing.", "R"),
           ("1.4.4", "A reservoir holds 3.5 × 10⁶ litres. A second holds 3.5 × 10⁵ litres. How many "
                     "times larger is the first, and what does this say about reporting?",
            "10 times larger",
            "The powers of 10 differ by 1, so the quantities differ by a factor of 10.", "A"),
           ("1.4.5", "A path is measured as 25 m to the nearest metre. Explain why the true length "
                     "cannot be known from this record, and state the best interval you can give.",
            "[24.5, 25.5) m",
            "The record fixes the length only to within half a metre either side.", "R"),
           ("1.4.6", "A metal rod is √27 cm long. A slot is 5.1 cm wide to one decimal place. Will "
                     "the rod fit? Justify with an exact comparison.",
            "√27 ≈ 5.196 cm, which is greater than 5.1, so it will not fit",
            "Compare the exact surd with the rounded measurement, and state the uncertainty.", "A"),
           ("1.4.7", "A field is 0.6·1· hectares. Convert this to a fraction and find the area to "
                     "the nearest square metre, given 1 ha = 10 000 m².",
            "61/99 ha ≈ 0.6162 ha ≈ 6162 m²",
            "Convert the recurring decimal to a fraction, then multiply.", "A"),
           ("1.4.8", "Explain, with a calculation, why a builder should not order material from a "
                     "measurement rounded to the nearest metre.",
            "The error can be up to 0.5 m per measurement, and errors add up over several "
            "measurements.",
            "Rounding errors accumulate, so the total can be far from the true amount.", "R"),
           ("1.4.9", "A map scale is 1 : 25 000. A lake measures √8 cm on the map. Find the real "
                     "width in exact form and to the nearest metre.",
            "25000√8 cm = 50000√2 cm ≈ 70 710 cm ≈ 707 m",
            "Multiply by the scale factor, then convert units and round.", "A"),
           ("1.4.10", "Two land records give areas 1.4·9· km² and 1.49 km². Show which is larger "
                      "and find the difference as a fraction.",
            "1.4·9· = 148/99 ≈ 1.4949, so it is larger by 1/1980 km²",
            "Write both as fractions over a common denominator before subtracting.", "R"),
           ("1.4.11", "A water tank holds 2√3 × 10³ litres. A second holds 3000 litres. Which holds "
                      "more, and by how much, exactly?",
            "2√3 × 10³ ≈ 3464 litres, so the first holds more by 1000(2√3 − 3) litres",
            "Compare the exact surd form with the integer, then subtract.", "A"),
           ("1.4.12", "Explain why an exact surd is preferred to a decimal when a measurement will "
                      "be used in a further calculation.",
            "The surd keeps the value exact, while a rounded decimal introduces an error that grows "
            "through the calculation.",
            "Rounding before calculating compounds the error.", "R")],
    ),
    assessment=[
        dict(title="A1 · The boundary of a plot",
             text="A triangular plot has sides √20 m, √45 m and √80 m. Find the exact perimeter, a "
                  "decimal estimate to one decimal place, and the interval in which the true "
                  "perimeter must lie if each side is measured to the nearest 0.1 m.",
             note="Criteria A and C · state which answers are exact and which are rounded."),
        dict(title="A2 · The recurring record",
             text="An archive records a yield as 0.2·7· tonnes per hectare. Convert this to a "
                  "fraction, then find the yield of 4 hectares exactly and to the nearest tonne.",
             note="Criteria A and D · show the conversion, and comment on the precision of the "
                  "original record."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of quantity and equivalence "
        "appear in your work?",
        "How is the global context of orientation in space and time, and its exploration of natural "
        "and human landscapes and resources, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a measurement that is rounded, and what would you still like "
        "to ask?",
    ],
    review=dict(
        ideas=["A rational number is a fraction of integers; its decimal stops or recurs.",
               "A decimal terminates exactly when the denominator has no prime factor but 2 and 5.",
               "An irrational number cannot be written as a fraction; √2 is proved irrational by "
               "contradiction.",
               "Absolute value measures distance from zero, so it turns order into distance.",
               "An interval records which endpoints are included, using square and round brackets.",
               "Surds are simplified by taking out square factors and rationalised by multiplying "
               "by a conjugate.",
               "A universal claim is proved by an argument for all cases, or disproved by one "
               "counterexample."],
        vocab=["rational", "irrational", "terminating decimal", "recurring decimal", "surd",
               "absolute value", "interval", "union", "intersection", "complement",
               "proof by contradiction", "counterexample", "conjugate"],
        mixed=[("1.R1", "Write 5/12 as a decimal and say whether it terminates."),
               ("1.R2", "Convert 0.·4·5· into a fraction."),
               ("1.R3", "Simplify √98."),
               ("1.R4", "Solve |x − 1| < 3 and write the answer as an interval."),
               ("1.R5", "Is the sum of two irrational numbers always irrational? Justify."),
               ("1.R6", "Write the complement of (2, 7] in interval notation.")],
    ),
    projects=dict(
        service=[("Community need", "Land and water records in the community are kept to different "
                                    "precisions, which makes sharing decisions hard to check."),
                 ("Mathematical connection", "Exact and rounded values, intervals and unit "
                                             "conversion."),
                 ("Proposed action", "Re-record one shared resource to an agreed precision and "
                                     "publish the interval of uncertainty with it."),
                 ("Expected impact", "Decisions about the resource are made from numbers everyone "
                                     "can interpret the same way."),
                 ("Student reflection", "Record the precision you chose, why, and what changed when "
                                        "the record was made consistent.")],
        community=[("Project idea", "A precision audit of the school's measurements."),
                   ("Need", "The field, the hall and the garden are all measured to different "
                            "precisions."),
                   ("Research question", "What precision does each use of the school's spaces "
                                         "actually need?"),
                   ("Mathematics", "Rounding intervals, significant figures, unit conversion and "
                                   "error accumulation."),
                   ("Action or outcome", "A measurement register with an agreed precision and an "
                                         "uncertainty interval for each space."),
                   ("Beneficiaries", "Anyone planning events, seating or planting in those spaces."),
                   ("Evidence", "The register, the method and a photograph of the measuring.")],
        personal=[("Personal interest", "Mapping, hiking or gardening."),
                  ("Learning goal", "To record a real measurement honestly, with its uncertainty."),
                  ("Product or outcome", "A measured plan of a route or a bed, with intervals."),
                  ("Mathematics", "Scale, surds, rounding and interval notation."),
                  ("Process", "Measure, convert to a common unit, then state the interval."),
                  ("Evidence", "The plan, the measurements and the stated uncertainty.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=2, title="Powers, roots and scientific notation",
    key="Form", related=["Quantity", "Representation", "Patterns"],
    context="Scientific and technical innovation",
    exploration="Precision, accuracy and measurement",
    inquiry=("The form of a number written in index form, and the equivalence between index form "
             "and root form, allow any quantity to be represented compactly and compared across "
             "scales, while the pattern in the exponent laws makes those representations safe to "
             "manipulate."),
    atl=("Research",
         "In order for a student to use an index law correctly in an unfamiliar problem, students "
         "must test the law on small cases, record where it breaks, and state the conditions under "
         "which the law holds."),
    standfirst="Index form is a representation that carries the size of a quantity in its shape. "
               "The exponent laws are patterns in that shape, and they are what make large and "
               "small numbers calculable.",
    engage="A drop of seawater contains about 10²² atoms. A red blood cell is about 10⁻⁵ m wide. "
           "Writing these in full is impossible; writing them in index form is not, and the "
           "comparison becomes immediate.",
    questions=[("Factual", "What do the exponent laws say, and how do you write a root as a power?"),
               ("Conceptual", "Why does multiplying powers of the same base add the indices, and "
                              "what does that reveal about the form of a number in index notation?"),
               ("Debatable", "When a measurement is reported to a certain number of significant "
                             "figures, does the extra precision of a longer decimal make the claim "
                             "more scientific?")],
    application_lede="These tasks use index laws, rational indices, scientific notation, orders of "
                     "magnitude and significant figures. State the precision of every answer you "
                     "report.",
    projects_lede="Innovation runs on measurement at very different scales. Use index form to keep "
                  "the scales visible, and significant figures to keep the claims honest.",
    sections=[
        dict(id="2.1", title="Integer exponents and the exponent laws",
             inquiry_q=("How can the pattern in repeated multiplication be written once, as a rule "
                        "that works for every case?"), teach=[
            "An index records repeated multiplication: 2⁵ = 2 × 2 × 2 × 2 × 2. The base is 2 and the index is 5, and the index is a count of factors, not a multiplier.",
            "Multiplying powers of the same base adds the indices, because the factors simply accumulate: 2³ × 2⁴ = 2⁷. Dividing subtracts them, because division removes factors.",
            "A power of a power multiplies the indices, because each of the factors is itself a repeated multiplication: (2³)⁴ = 2¹².",
            "The laws hold for every integer index once a⁰ = 1 and a⁻ⁿ = 1/aⁿ are defined. Those definitions are chosen so the patterns in the exponent laws continue without a break, and the same patterns extend to roots.",
        ], examples=[
            dict(q="Simplify (3x⁴)³ ÷ (9x²) and write the answer with positive indices.",
                 vis=F("table", [["expression", "law used", "result"],
                                 ["(3x⁴)³", "power of a power", "27x¹²"],
                                 ["27x¹² ÷ 9x²", "quotient law", "3x¹⁰"]],
                       caption="Each law changes only the form, never the value."),
                 reasoning="The power law multiplies the indices inside the bracket, and the quotient "
                          "law subtracts them, with the coefficients handled separately.",
                 steps=["(3x⁴)³ = 3³ × (x⁴)³ = 27x¹².",
                        "27x¹² ÷ 9x² = (27 ÷ 9) × x¹²⁻².",
                        "= 3x¹⁰."],
                 ans="3x¹⁰",
                 interp="The coefficient and the variable part obey different laws, so keeping them "
                        "separate avoids the commonest error."),
            dict(q="Evaluate 5⁻² × 5⁵ ÷ 5⁰.",
                 vis=F("number_line", -3, 6, 1, [], "adding and subtracting indices", ""),
                 reasoning="Negative and zero indices are defined so that the same laws continue to "
                          "work, so they can be used in the same calculation.",
                 steps=["5⁻² × 5⁵ = 5⁻²⁺⁵ = 5³.",
                        "5⁰ = 1 by definition.",
                        "5³ ÷ 1 = 125."],
                 ans="125",
                 interp="The definitions of a⁰ and a⁻ⁿ are not arbitrary: they are exactly what the "
                        "pattern in the laws requires."),
        ], inv=dict(
            task="Compute 2² × 2³, 2³ × 2⁴, 2⁵ × 2⁵ and 2² × 2⁵ both as products of factors and as "
                 "single powers of 2. Then do the same for division, and for (2²)³ and (2³)². "
                 "Record the pattern you see in the indices.",
            fig=F("table", [["expression", "as repeated factors", "as one power"],
                            ["2² × 2³", "2 × 2 × 2 × 2 × 2", "2⁵"],
                            ["2³ × 2⁴", "seven factors of 2", "2⁷"],
                            ["2⁵ ÷ 2²", "five factors with two removed", "2³"],
                            ["(2²)³", "three groups of two factors", "2⁶"]],
                  caption="The index law is a statement about counting factors."),
            table=[["calculation", "written out", "answer", "what happened to the indices"],
                   ["2² × 2³", "2×2×2×2×2", "2⁵", "2 + 3 = 5"],
                   ["2³ × 2⁴", "seven factors", "2⁷", "3 + 4 = 7"],
                   ["2⁵ ÷ 2²", "five minus two factors", "2³", "5 − 2 = 3"],
                   ["(2²)³", "three groups of two", "2⁶", "2 × 3 = 6"],
                   ["(2³)²", "two groups of three", "2⁶", "3 × 2 = 6"],
                   ["2⁰", "no factors at all", "1", "the pattern needs it to be 1"]],
            notice=["Multiplying adds the indices, and the reason is that the factors pile up.",
                    "Dividing subtracts them, because division removes factors.",
                    "A power of a power multiplies the indices, because each factor is itself a "
                    "repeated multiplication.",
                    "2⁵ ÷ 2⁵ must equal 1, and the pattern says 2⁵⁻⁵ = 2⁰, so 2⁰ = 1."],
            obs="Each law is the same statement about counting factors, written in index form.",
            concl="aᵐ × aⁿ = aᵐ⁺ⁿ, aᵐ ÷ aⁿ = aᵐ⁻ⁿ and (aᵐ)ⁿ = aᵐⁿ, and these patterns are what force "
                  "the definitions a⁰ = 1 and a⁻ⁿ = 1/aⁿ.")),
        dict(id="2.2", title="Roots and rational exponents",
             inquiry_q=("How can a root be written as a power, and why are the two forms "
                        "equivalent?"), teach=[
            "The nth root of a number is the value that, raised to the nth power, gives the number back: ⁿ√a = a^(1/n). The two notations are equivalent because (a^(1/n))ⁿ = a.",
            "Writing roots as fractional indices lets the exponent laws apply to roots as well: √a × √b = a^(1/2) × b^(1/2) = (ab)^(1/2) = √(ab).",
            "A rational index a^(m/n) means the nth root raised to the mth power, and the order of the two operations does not matter for non-negative a.",
            "Negative indices give reciprocals, so a^(−1/2) = 1/√a. Keeping the sign separate from the fraction is what prevents sign errors.",
        ], examples=[
            dict(q="Write ³√(8x⁶) using index notation, then simplify.",
                 vis=F("table", [["expression", "index form", "simplified"],
                                 ["³√8", "8^(1/3)", "2"],
                                 ["³√(x⁶)", "(x⁶)^(1/3)", "x²"]],
                       caption="A root is a fractional index, so the power law applies."),
                 reasoning="The cube root is the power 1/3, and the power law multiplies indices, "
                          "so 6 × 1/3 = 2.",
                 steps=["³√(8x⁶) = (8x⁶)^(1/3).",
                        "= 8^(1/3) × (x⁶)^(1/3).",
                        "8^(1/3) = 2 and (x⁶)^(1/3) = x^(6/3) = x²."],
                 ans="2x²",
                 interp="Index form turns a root problem into an exponent problem, which is why it "
                        "is the preferred form for manipulation."),
            dict(q="Simplify (16/81)^(−3/4).",
                 vis=F("table", [["step", "law", "result"],
                                 ["(16/81)^(−3/4)", "negative index", "(81/16)^(3/4)"],
                                 ["(81/16)^(3/4)", "root then power", "(3/2)³ = 27/8"]],
                       caption="Handle the sign, then the fraction, then the index."),
                 reasoning="A negative index inverts the fraction, and a fractional index takes a "
                          "root before applying the power.",
                 steps=["(16/81)^(−3/4) = (81/16)^(3/4).",
                        "(81/16)^(3/4) = (⁴√81 / ⁴√16)³ = (3/2)³.",
                        "(3/2)³ = 27/8."],
                 ans="27/8",
                 interp="Doing the sign first, then the root, then the power keeps each step "
                        "checkable."),
        ], inv=dict(
            task="Take the numbers 4, 8, 27 and 32. Write each as a power of its smallest possible "
                 "base, then write each root ⁿ√a as a fractional index. Finally, test whether √(ab) "
                 "= √a × √b holds for a = 9, b = 16 and for a = −9, b = 16, and record what you "
                 "find.",
            table=[["number", "as a power", "root as an index"],
                   ["4", "2²", "√4 = 4^(1/2) = 2"],
                   ["8", "2³", "³√8 = 8^(1/3) = 2"],
                   ["27", "3³", "³√27 = 27^(1/3) = 3"],
                   ["32", "2⁵", "⁵√32 = 32^(1/5) = 2"]],
            notice=["Every root could be written as a fractional index.",
                    "√(9 × 16) = √144 = 12, and √9 × √16 = 3 × 4 = 12, so the law holds.",
                    "√(−9 × 16) is not a real number, so the law cannot be tested there.",
                    "Writing numbers as powers of the smallest base makes roots easy to see."],
            obs="A root and a fractional index are two notations for the same operation, so the "
                "exponent laws apply to roots too.",
            concl="ⁿ√a = a^(1/n), so a^(m/n) = (ⁿ√a)ᵐ and the exponent laws extend to roots — for "
                  "non-negative a when n is even.")),
        dict(id="2.3", title="Scientific notation",
             inquiry_q=("How can very large and very small quantities be written so that their size "
                        "is visible at a glance?"), teach=[
            "Scientific notation writes a number as a × 10ⁿ with 1 ≤ a < 10 and n an integer. The exponent counts how many places the decimal point has moved, so it carries the size of the quantity.",
            "The form is a representation choice: 6 300 000 and 6.3 × 10⁶ are the same number, but only the second makes the order of magnitude visible.",
            "Multiplying in scientific notation multiplies the coefficients and adds the exponents. Dividing does the reverse. This is the exponent law applied to a representation.",
            "The form also prevents a common reporting error. A measurement written as 0.00042 m has hidden its scale; 4.2 × 10⁻⁴ m has not.",
        ], examples=[
            dict(q="Write 0.0000042 and 3 500 000 000 in scientific notation, then multiply them.",
                 vis=F("table", [["number", "scientific notation"],
                                 ["0.0000042", "4.2 × 10⁻⁶"],
                                 ["3 500 000 000", "3.5 × 10⁹"]],
                       caption="The exponent records the position of the decimal point."),
                 reasoning="Move the decimal point until the coefficient lies between 1 and 10, then "
                          "count the places moved to fix the exponent.",
                 steps=["0.0000042: move the point 6 places right → 4.2 × 10⁻⁶.",
                        "3 500 000 000: move the point 9 places left → 3.5 × 10⁹.",
                        "Multiply: (4.2 × 3.5) × 10⁻⁶⁺⁹ = 14.7 × 10³.",
                        "Restore the form: 1.47 × 10⁴."],
                 ans="4.2 × 10⁻⁶ and 3.5 × 10⁹; their product is 1.47 × 10⁴",
                 interp="The exponents add exactly as the index law says, and the coefficient is "
                        "adjusted at the end to keep the form."),
            dict(q="A red blood cell is 7.5 × 10⁻⁶ m wide and a grain of sand is 2 × 10⁻⁴ m wide. "
                   "How many times wider is the grain?",
                 vis=F("table", [["object", "width"],
                                 ["red blood cell", "7.5 × 10⁻⁶ m"],
                                 ["grain of sand", "2 × 10⁻⁴ m"]],
                       caption="Dividing in scientific notation subtracts the exponents."),
                 reasoning="Dividing divides the coefficients and subtracts the exponents, which "
                          "gives the comparison directly.",
                 steps=["(2 × 10⁻⁴) ÷ (7.5 × 10⁻⁶) = (2 ÷ 7.5) × 10⁻⁴⁻⁽⁻⁶⁾.",
                        "= 0.2666… × 10².",
                        "= 2.666… × 10¹ ≈ 27."],
                 ans="about 27 times wider",
                 interp="The subtraction of exponents gives the factor of 100 immediately, before any "
                        "coefficient arithmetic."),
        ], inv=dict(
            task="Collect six quantities from science or geography at very different scales, write "
                 "each in scientific notation, and order them from smallest to largest. Then "
                 "multiply the smallest and the largest, and divide the largest by the smallest, "
                 "without using a calculator for the exponents.",
            table=[["quantity", "ordinary form", "scientific notation"],
                   ["width of a hair", "0.00008 m", "8 × 10⁻⁵ m"],
                   ["mass of a grain of rice", "0.000025 kg", "2.5 × 10⁻⁵ kg"],
                   ["height of a room", "3 m", "3 × 10⁰ m"],
                   ["distance to the moon", "384 000 000 m", "3.84 × 10⁸ m"],
                   ["mass of the Earth", "5 970 000 000 000 000 000 000 000 kg", "5.97 × 10²⁴ kg"],
                   ["speed of light", "300 000 000 m/s", "3 × 10⁸ m/s"]],
            notice=["Ordering by the exponent gives the correct order immediately.",
                    "The product of the smallest and largest had exponent −5 + 24 = 19.",
                    "The quotient had exponent 24 − (−5) = 29, so the two differ by 29 orders of "
                    "magnitude.",
                    "Every coefficient stayed between 1 and 10, which is what makes the form "
                    "readable."],
            obs="The exponent carries the size of the quantity, so comparing, multiplying and "
                "dividing become operations on the exponents.",
            concl="Scientific notation is a × 10ⁿ with 1 ≤ a < 10, and multiplying or dividing such "
                  "numbers adds or subtracts the exponents — which is the exponent law applied to a "
                  "representation.")),
        dict(id="2.4", title="Orders of magnitude and estimation",
             inquiry_q=("How can an order of magnitude decide whether a calculation is worth doing "
                        "in detail?"), teach=[
            "The order of magnitude of a quantity is the power of 10 nearest to it. Two quantities within a factor of 10 of each other share an order of magnitude.",
            "Estimation by order of magnitude replaces every number by its leading digit times a power of 10, then works with the exponents. The answer is never exact, but it is always in the right scale.",
            "An estimate is a check on a calculation. If a calculator answer is not within a factor of a few of the estimate, the calculation is wrong.",
            "Rounding to one significant figure before calculating is the practical version of this idea, and it is the standard way to check a long computation.",
        ], examples=[
            dict(q="Estimate 4.9 × 10⁷ × 6.1 × 10⁻³ ÷ (2.0 × 10²) by order of magnitude, then compare "
                   "with the calculator value.",
                 vis=F("table", [["quantity", "rounded to one significant figure"],
                                 ["4.9 × 10⁷", "5 × 10⁷"],
                                 ["6.1 × 10⁻³", "6 × 10⁻³"],
                                 ["2.0 × 10²", "2 × 10²"]],
                       caption="Round the coefficients, then work with the exponents."),
                 reasoning="Rounding each quantity to one significant figure keeps the exponent exact "
                          "and makes the arithmetic mental.",
                 steps=["Rounded: (5 × 10⁷) × (6 × 10⁻³) ÷ (2 × 10²).",
                        "Coefficients: 5 × 6 ÷ 2 = 15.",
                        "Exponents: 7 − 3 − 2 = 2.",
                        "Estimate: 15 × 10² = 1.5 × 10³.",
                        "Calculator: 1.4975 × 10³, so the estimate is close."],
                 ans="about 1.5 × 10³, against a calculator value of 1.4975 × 10³",
                 interp="The estimate caught no error this time, but it would have caught a decimal "
                        "point slip of two places."),
            dict(q="A city of 2.4 × 10⁵ people uses 1.8 × 10¹⁰ litres of water a year. Estimate the "
                   "use per person.",
                 vis=F("table", [["quantity", "value"],
                                 ["population", "2.4 × 10⁵"],
                                 ["water used", "1.8 × 10¹⁰ litres"]],
                       caption="Division subtracts the exponents."),
                 reasoning="Dividing the total by the population gives the per-person value, and the "
                          "exponents give the scale.",
                 steps=["(1.8 × 10¹⁰) ÷ (2.4 × 10⁵) = (1.8 ÷ 2.4) × 10⁵.",
                        "1.8 ÷ 2.4 = 0.75, so the answer is 0.75 × 10⁵.",
                        "= 7.5 × 10⁴ litres per person per year."],
                 ans="about 7.5 × 10⁴ litres per person per year",
                 interp="That is roughly 205 litres a day, which is a plausible order of magnitude "
                        "for domestic use."),
        ], inv=dict(
            task="Estimate each of these without a calculator, then check with one: the number of "
                 "heartbeats in a year, the number of seconds in a school day, the number of grains "
                 "of rice in a 1 kg bag, and the number of litres of water a class uses in a week. "
                 "Record the order of magnitude of each estimate.",
            table=[["quantity", "estimate", "order of magnitude", "calculator value"],
                   ["heartbeats in a year", "70 × 60 × 24 × 365", "10⁷", "3.68 × 10⁷"],
                   ["seconds in a school day", "6 × 60 × 60 × 6", "10⁵", "1.296 × 10⁵"],
                   ["grains in 1 kg of rice", "1000 g ÷ 0.02 g", "10⁵", "5 × 10⁴ to 1 × 10⁵"],
                   ["litres used by a class in a week", "30 × 200 × 7", "10⁵", "4.2 × 10⁴"]],
            notice=["Every estimate landed within a factor of 10 of the true value.",
                    "Estimating first made the calculator check meaningful.",
                    "The exponent of the estimate matched the exponent of the true value in three of "
                    "the four cases.",
                    "The rice estimate was the least reliable, because the mass of one grain is a "
                    "guess."],
            obs="An order-of-magnitude estimate fixes the scale of an answer, which is enough to "
                "catch most errors.",
            concl="The order of magnitude of a quantity is the power of 10 nearest to it, and "
                  "estimating by orders of magnitude gives a value that is right in scale even when "
                  "it is not right in detail.")),
        dict(id="2.5", title="Significant figures and precision",
             inquiry_q=("How many digits of a measurement actually carry meaning?"), teach=[
            "Significant figures are the digits of a measurement that carry meaning, counted from the first non-zero digit. Leading zeros are placeholders and are never significant; trailing zeros after a decimal point always are.",
            "The number of significant figures records the precision of the instrument. A length of 3.6 m claims the nearest 10 cm; 3.60 m claims the nearest centimetre.",
            "Rounding to a given number of significant figures follows the usual rule, but the count starts at the first non-zero digit, which is why 0.00452 to three significant figures is 0.00452 and to two is 0.0045.",
            "When measurements are combined, the result cannot be more precise than the least precise input. Reporting more digits than the data supports is a false claim of precision.",
        ], examples=[
            dict(q="Round 0.0040529 to three significant figures, and 604 512 to two.",
                 vis=F("table", [["number", "significant figures", "rounded"],
                                 ["0.0040529", "3", "0.00405"],
                                 ["604 512", "2", "600 000 = 6.0 × 10⁵"]],
                       caption="Counting starts at the first non-zero digit."),
                 reasoning="The count begins at the first non-zero digit, so leading zeros are "
                          "ignored and the decision digit is the one after the last significant "
                          "figure.",
                 steps=["0.0040529: the first non-zero digit is 4, so the three significant "
                        "figures are 4, 0, 5 and the next digit is 2.",
                        "2 < 5, so 0.0040529 → 0.00405 to three significant figures.",
                        "604 512: the first two significant figures are 6 and 0, and the next "
                        "digit is 4, which does not round up.",
                        "So 604 512 → 600 000 = 6.0 × 10⁵ to two significant figures."],
                 ans="0.00405 and 6.0 × 10⁵",
                 interp="Writing 600 000 loses the claim about precision, so scientific notation is "
                        "used to keep it."),
            dict(q="A rectangle measures 4.2 m by 3.65 m. Find the area, reporting it to a sensible "
                   "precision.",
                 vis=F("table", [["side", "measurement", "significant figures"],
                                 ["length", "4.2 m", "2"],
                                 ["width", "3.65 m", "3"]],
                       caption="The area cannot be more precise than the least precise side."),
                 reasoning="Multiplying measurements combines their errors, so the result is "
                          "reported to the precision of the least precise input.",
                 steps=["Area = 4.2 × 3.65 = 15.33 m².",
                        "The least precise side has two significant figures, so report to two.",
                        "15.33 m² → 15 m² to two significant figures."],
                 ans="15 m² (to two significant figures)",
                 interp="Reporting 15.33 m² would claim a precision that neither measurement "
                        "supports."),
        ], inv=dict(
            task="Take the measurements 0.0042 m, 4.20 m, 42 m, 4200 m and 0.042 m. For each one, "
                 "state the number of significant figures and the interval of possible true values. "
                 "Then multiply 4.2 by 3.65 and decide how many digits of the answer are "
                 "meaningful.",
            table=[["measurement", "significant figures", "interval of true values"],
                   ["0.0042 m", "2", "[0.00415, 0.00425)"],
                   ["4.20 m", "3", "[4.195, 4.205)"],
                   ["42 m", "2", "[41.5, 42.5)"],
                   ["4200 m", "2 or 4 — ambiguous without a note", "[4150, 4250) if two"],
                   ["0.042 m", "2", "[0.0415, 0.0425)"]],
            notice=["Trailing zeros before a decimal point are ambiguous, which is why scientific "
                    "notation is preferred.",
                    "0.0042 and 0.042 both have two significant figures, even though one is ten "
                    "times larger.",
                    "4.20 has three significant figures and a narrower interval than 4.2.",
                    "4.2 × 3.65 = 15.33, but only two of those digits are meaningful."],
            obs="Significant figures count the digits that carry measured meaning, and the interval "
                "of true values gets narrower as the count rises.",
            concl="The number of significant figures records the precision of a measurement, and a "
                  "calculated result cannot honestly be reported to more significant figures than "
                  "the least precise value that went into it.")),
    ],
    practice=dict(
        A=[("2.1.1", "Simplify 4a³ × 5a⁴.",
            "20a⁷", "Multiply the coefficients and add the indices.", "F"),
           ("2.1.2", "Evaluate 2⁻³.",
            "1/8", "A negative index gives the reciprocal.", "F"),
           ("2.1.3", "Write 3⁰ and state why the definition is needed.",
            "1, so that aᵐ ÷ aᵐ = a⁰ continues to work",
            "The exponent laws require a⁰ = 1.", "R"),
           ("2.1.4", "Simplify (2x²y)³.",
            "8x⁶y³", "The power law multiplies every index by 3.", "F"),
           ("2.1.5", "Evaluate (1/2)⁻².",
            "4", "A negative index inverts the fraction before squaring.", "F"),
           ("2.1.6", "Simplify 12x⁵y³ ÷ 4x²y.",
            "3x³y²", "Divide coefficients and subtract matching indices.", "F"),
           ("2.1.7", "Write 10⁵ ÷ 10⁻³ as a single power of 10.",
            "10⁸", "5 − (−3) = 8.", "F"),
           ("2.1.8", "Explain why (a + b)² is not a² + b², using index laws.",
            "Squaring is not distributive over addition; (a + b)² = a² + 2ab + b².",
            "The exponent applies to the whole bracket, not to each term separately.", "R"),
           ("2.1.9", "Simplify (3² × 3⁵) ÷ 3⁴.",
            "3³", "2 + 5 − 4 = 3.", "F"),
           ("2.1.10", "A quantity doubles every hour, starting at 5 units. Write its size after n "
                      "hours.",
            "5 × 2ⁿ", "Repeated doubling is a power.", "A"),
           ("2.1.11", "Simplify x⁰ + x⁻¹ for x = 4.",
            "1 + 1/4 = 5/4", "x⁰ = 1 and x⁻¹ = 1/x.", "F"),
           ("2.1.12", "Explain the difference between 2x³ and (2x)³.",
            "2x³ = 2 × x³; (2x)³ = 8x³",
            "The bracket changes which parts the index applies to.", "R")],
        B=[("2.2.1", "Investigate: does aᵐ × bᵐ = (ab)ᵐ hold for negative m? Test with a = 2, b = 3, m = −1.",
            "Yes: 2⁻¹ × 3⁻¹ = 1/6 and (6)⁻¹ = 1/6.",
            "The law holds for every integer index.", "R"),
           ("2.2.2", "Write √(x⁸) as a single power and state the condition on x.",
            "x⁴, for any real x", "√(x⁸) = (x⁸)^(1/2) = x⁴, and an even power is never negative.", "R"),
           ("2.2.3", "Investigate the pattern 2¹, 2⁰, 2⁻¹, 2⁻², 2⁻³ and generalise it.",
            "Each step divides by 2; the rule is 2⁻ⁿ = 1/2ⁿ.",
            "Extending the pattern backwards forces the negative index rule.", "R"),
           ("2.2.4", "Test the claim: a^(−1/2) = −√a. Find a counterexample or confirm it.",
            "False: 4^(−1/2) = 1/2, not −2.",
            "A negative index gives a reciprocal, not a sign change.", "R"),
           ("2.2.5", "Investigate: for which values of n is √(xⁿ) equal to x when x is negative?",
            "None — the square root is not a real number for negative x.",
            "An even root of a negative number is not real.", "R"),
           ("2.2.6", "Simplify 8^(2/3) + 27^(2/3) and describe the pattern you used.",
            "4 + 9 = 13", "Take the cube root first, then square: 2² + 3².", "R"),
           ("2.2.7", "Investigate: is (x^a)^b = (x^b)^a? Test with x = 2, a = 3, b = 5.",
            "Yes: both give x^(ab).",
            "Multiplication of indices is commutative, so the order does not matter.", "R"),
           ("2.2.8", "Generalise a rule for x^(1/n) × x^(1/m).",
            "x^((m + n)/nm)", "Adding fractional indices requires a common denominator.", "R"),
           ("2.2.9", "Investigate whether x⁰ = 1 is true for x = 0, and report what you find.",
            "0⁰ is undefined, so the law is stated for non-zero bases.",
            "The division that gives a⁰ is not available when a = 0.", "R"),
           ("2.2.10", "Find a counterexample to 'a^m ÷ a^n = a^(m÷n)'.",
            "2⁴ ÷ 2² = 4, but 2^(4÷2) = 4 — try 3⁵ ÷ 3² = 27 while 3^(5÷2) ≈ 15.6.",
            "Division subtracts indices; it never divides them.", "R"),
           ("2.2.11", "Investigate the sequence 1, 4, 9, 16, 25 written as powers. State a rule.",
            "n², so the nth term is the square of n",
            "Each term is a perfect square.", "F")],
        C=[("2.3.1", "Write 0.000000047 m in scientific notation.",
            "4.7 × 10⁻⁸ m", "Move the decimal point 8 places to the right.", "F"),
           ("2.3.2", "Explain in words why the exponent in scientific notation can be negative.",
            "It counts places the decimal point moves left, which happens for quantities smaller "
            "than 1.",
            "A small quantity has many leading zeros after the point.", "R"),
           ("2.3.3", "Multiply (2.5 × 10⁶) by (4 × 10⁻⁹) and write the answer in scientific notation.",
            "1.0 × 10⁻²", "2.5 × 4 = 10 and 6 − 9 = −3, so 10 × 10⁻³ = 1.0 × 10⁻².", "F"),
           ("2.3.4", "Explain the difference between 4 × 10³ and 4.0 × 10³ as a record of precision.",
            "4 × 10³ claims one significant figure; 4.0 × 10³ claims two.",
            "The number of significant digits in the coefficient records precision.", "R"),
           ("2.3.5", "Divide (9 × 10¹²) by (3 × 10⁻²) and explain the step on the exponents.",
            "3 × 10¹⁴", "12 − (−2) = 14.", "F"),
           ("2.3.6", "A cell is 1.2 × 10⁻⁵ m long. Write this in ordinary form and explain the "
                    "representation.",
            "0.000012 m", "The exponent −5 moves the point five places left.", "F"),
           ("2.3.7", "Explain why 6.3 × 10⁶ is a better representation than 6 300 000 for a "
                     "measurement.",
            "It shows the order of magnitude and the precision at once.",
            "The coefficient carries the significant digits and the exponent carries the scale.", "R"),
           ("2.3.8", "Add (3 × 10⁴) and (4 × 10³) and write the answer in scientific notation.",
            "3.4 × 10⁴", "Rewrite 4 × 10³ as 0.4 × 10⁴, then add the coefficients.", "F"),
           ("2.3.9", "Explain why 2.5 × 10⁻³ is not the same as 2.5 × 10³, using the exponent.",
            "The exponents differ by 6, so the quantities differ by a factor of 10⁶.",
            "The exponent fixes the position of the decimal point.", "R"),
           ("2.3.10", "Write the speed of light, 299 792 458 m/s, in scientific notation to three "
                      "significant figures.",
            "3.00 × 10⁸ m/s", "Round to three significant figures, keeping the trailing zeros.", "F"),
           ("2.3.11", "A mass is recorded as 5 × 10⁻⁷ kg. State its order of magnitude and explain "
                      "what that means.",
            "10⁻⁷ kg, so it is between 10⁻⁷ and 10⁻⁶ kg",
            "The order of magnitude is the nearest power of 10.", "R"),
           ("2.3.12", "Explain how scientific notation makes it possible to compare the mass of an "
                      "electron with the mass of the Earth.",
            "Both are written as a × 10ⁿ, so comparing the exponents gives the comparison directly.",
            "The exponents differ by about 55, so the Earth is about 10⁵⁵ times heavier.", "R")],
        D=[("2.4.1", "Estimate the number of seconds in a school year of 180 days, 6 hours a day.",
            "about 3.9 × 10⁶ s",
            "180 × 6 × 3600 ≈ 3.888 × 10⁶, so about 4 × 10⁶.", "A"),
           ("2.4.2", "A city of 3 × 10⁵ people each uses 200 litres of water a day. Estimate the "
                     "daily total.",
            "6 × 10⁷ litres", "3 × 10⁵ × 2 × 10² = 6 × 10⁷.", "A"),
           ("2.4.3", "A factory makes 4.5 × 10⁵ bottles a day. Estimate the yearly output.",
            "about 1.6 × 10⁸ bottles", "4.5 × 10⁵ × 365 ≈ 1.64 × 10⁸.", "A"),
           ("2.4.4", "Explain how an order-of-magnitude estimate can catch an error in a calculator "
                     "answer.",
            "If the calculator answer is not within about a factor of 10 of the estimate, the "
            "calculation is wrong.",
            "The estimate fixes the scale, which is where most errors live.", "R"),
           ("2.4.5", "A spacecraft is 2.4 × 10⁸ km from Earth and travels at 4 × 10⁴ km/h. Estimate "
                     "the journey time.",
            "about 6 × 10³ hours", "2.4 × 10⁸ ÷ 4 × 10⁴ = 6 × 10³.", "A"),
           ("2.4.6", "A phone battery holds 3 × 10³ mAh and a charger delivers 2 × 10⁰ A. Estimate "
                     "the charging time and comment on its sense.",
            "about 3 × 10³ hours if the current were 1 A — the sense is wrong, so the units need "
            "converting: 2 A = 2000 mA gives about 1.5 hours.",
            "Converting to the same unit before dividing is what makes the answer sensible.", "R"),
           ("2.4.7", "A lake holds 8.2 × 10⁹ litres and a town draws 1.5 × 10⁷ litres a day. "
                     "Estimate how many days the lake lasts.",
            "about 5.5 × 10² days", "8.2 × 10⁹ ÷ 1.5 × 10⁷ ≈ 5.5 × 10².", "A"),
           ("2.4.8", "Explain why reporting a measurement to more significant figures than the "
                     "instrument allows is dishonest.",
            "It claims precision that was never measured, so the extra digits are invented.",
            "Precision must match the instrument.", "R"),
           ("2.4.9", "A field measures 42 m by 38 m, both to the nearest metre. Estimate the area "
                     "and give the interval in which the true area must lie.",
            "about 1600 m², within roughly 1400 m² and 1800 m²",
            "Using 41.5 and 37.5 gives the low bound and 42.5 and 38.5 the high one.", "A"),
           ("2.4.10", "A vaccine dose is 5 × 10⁻⁴ litres. How many doses from 2 × 10⁻¹ litres?",
            "400 doses", "2 × 10⁻¹ ÷ 5 × 10⁻⁴ = 0.4 × 10³ = 400.", "A"),
           ("2.4.11", "Two measurements are 3.6 × 10⁴ and 2.4 × 10⁵. Estimate their product and "
                      "explain the order of magnitude of the answer.",
            "about 8.6 × 10⁹, of order 10¹⁰",
            "3.6 × 2.4 ≈ 8.6 and 4 + 5 = 9.", "R"),
           ("2.4.12", "Explain, with an example, when it is better to round before calculating "
                      "rather than after.",
            "For a mental check, rounding first keeps the arithmetic simple and the exponent exact.",
            "Rounding first is a checking strategy, not a reporting strategy.", "R")],
    ),
    assessment=[
        dict(title="A1 · The water use audit",
             text="A school of 1.2 × 10³ students uses 4.5 × 10⁷ litres of water in a year. "
                  "Estimate the use per student per day, report it to a sensible precision, and "
                  "explain what the number of significant figures in your answer claims.",
             note="Criteria A and D · show the calculation in scientific notation and comment on "
                  "precision."),
        dict(title="A2 · The two scales",
             text="A virus is 1.2 × 10⁻⁷ m across and a football pitch is 1.05 × 10² m long. How "
                  "many viruses fit across the pitch? Report your answer in scientific notation.",
             note="Criteria A and C · state the order of magnitude of your answer and what it "
                  "means."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of quantity, representation and "
        "patterns appear in your work?",
        "How is the global context of scientific and technical innovation, and its exploration of "
        "precision, accuracy and measurement, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a reported measurement, and what would you still like to ask?",
    ],
    review=dict(
        ideas=["An index counts repeated multiplication, so multiplying powers adds indices.",
               "a⁰ = 1 and a⁻ⁿ = 1/aⁿ are defined so that the exponent laws continue without a break.",
               "A root is a fractional index: ⁿ√a = a^(1/n).",
               "Scientific notation a × 10ⁿ with 1 ≤ a < 10 makes the scale of a quantity visible.",
               "Multiplying or dividing in scientific notation adds or subtracts the exponents.",
               "The order of magnitude of a quantity is the nearest power of 10.",
               "Significant figures record precision, counted from the first non-zero digit."],
        vocab=["index", "base", "exponent law", "zero index", "negative index", "fractional index",
               "scientific notation", "order of magnitude", "significant figure", "precision"],
        mixed=[("2.R1", "Simplify (2x³)² × x⁻¹."),
               ("2.R2", "Write 0.00000082 in scientific notation."),
               ("2.R3", "Evaluate 27^(2/3)."),
               ("2.R4", "Round 0.007236 to three significant figures."),
               ("2.R5", "Estimate (6.1 × 10⁵) × (2.9 × 10⁻³)."),
               ("2.R6", "Explain why 2⁰ = 1 follows from the exponent laws.")],
    ),
    projects=dict(
        service=[("Community need", "Water and energy meters in the school are read and reported "
                                    "with inconsistent precision, so savings are hard to prove."),
                 ("Mathematical connection", "Scientific notation, orders of magnitude and "
                                             "significant figures."),
                 ("Proposed action", "Agree a single reporting precision for the school's meter "
                                     "readings and publish a weekly estimate."),
                 ("Expected impact", "Savings become visible and checkable instead of disputed."),
                 ("Student reflection", "Record the precision you chose, why, and what the "
                                        "published figures changed.")],
        community=[("Project idea", "A one-week energy audit of the school."),
                   ("Need", "The school does not know which activities use the most energy."),
                   ("Research question", "Where does the school's energy actually go, and what "
                                         "would save the most?"),
                   ("Mathematics", "Powers, scientific notation, estimation and proportional "
                                   "reasoning."),
                   ("Action or outcome", "A ranked list of savings with estimated daily impact."),
                   ("Beneficiaries", "The whole school community."),
                   ("Evidence", "Meter readings, the estimates and the ranked list.")],
        personal=[("Personal interest", "Photography, music or fitness tracking."),
                  ("Learning goal", "To use index form and precision language to describe a "
                                    "measurement you care about."),
                  ("Product or outcome", "A one-page data sheet for a personal measurement."),
                  ("Mathematics", "Scientific notation, significant figures and estimation."),
                  ("Process", "Measure, convert, write in scientific notation, then state the "
                              "precision."),
                  ("Evidence", "The data sheet and the stated uncertainty.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=3, title="Functions, expressions and algebraic reasoning",
    key="Relationships", related=["Generalisation", "Equivalence"],
    context="Identities and relationships",
    exploration="Relationships and communities",
    inquiry=("The relationship between two quantities can be generalised as a function, and the "
             "equivalence of the different algebraic forms of that relationship allows it to be "
             "rearranged, compared and used to predict."),
    atl=("Thinking",
         "In order for a student to select an algebraic strategy for an unfamiliar expression, "
         "students must identify which form the problem is already in, decide which equivalent "
         "form the answer needs, and justify the choice."),
    standfirst="A letter stands for a quantity that changes. A function is the relationship that "
               "gives each input one output, and equivalent forms of its rule reveal different "
               "things about that relationship.",
    engage="A phone plan costs 12 dollars a month plus 0.05 dollars a minute. For one month the "
           "bill depends entirely on the number of minutes used. What is the relationship, and how "
           "can it be written once for every month?",
    questions=[("Factual", "What is a function, what are its domain and range, and how do you "
                           "expand and factorise a quadratic expression?"),
               ("Conceptual", "Why do equivalent forms of the same expression reveal different "
                              "information about the relationship they describe?"),
               ("Debatable", "Is a formula that has been rearranged a different formula, or the "
                             "same formula in a different form — and does the difference matter?")],
    application_lede="These tasks use substitution, function notation, expansion, factorisation, "
                     "rearranging formulas and sequences. State the form of your answer and why "
                     "you chose it.",
    projects_lede="Relationships between quantities govern budgets, plans and schedules. Use "
                  "algebra to make a relationship explicit enough to act on.",
    sections=[
        dict(id="3.1", title="Variables, expressions and substitution",
             inquiry_q=("How can a changing quantity be represented by a letter, and what does "
                        "substitution actually do?"), teach=[
            "A variable is a letter standing for a number that can change. It is not an unknown to be found: it is a quantity that takes different values in different situations.",
            "An expression is a recipe built from variables, numbers and operations. 3n + 5 is a recipe that takes a number n, triples it and adds 5. The order of operations fixes what the recipe does.",
            "Substitution replaces a variable by a value and evaluates. It is the point at which a general relationship becomes a specific number.",
            "Two expressions that give the same value for every substitution are equivalent. Testing a few values suggests equivalence but never proves it; expansion or factorisation proves it.",
        ], examples=[
            dict(q="A taxi charges 3.50 dollars plus 1.80 dollars per kilometre. Write the cost as "
                   "an expression and find the cost of a 12 km trip.",
                 vis=F("function_machine", [(0, 3.5), (5, 12.5), (12, 25.1)],
                       "kilometres → cost", "cost = 1.8k + 3.5"),
                 reasoning="The cost has a fixed part and a variable part, so the expression is a "
                          "linear recipe in the number of kilometres.",
                 steps=["Let k be the number of kilometres.",
                        "Cost = 3.50 + 1.80k.",
                        "For k = 12: cost = 3.50 + 1.80 × 12 = 3.50 + 21.60.",
                        "= 25.10 dollars."],
                 ans="C = 3.50 + 1.80k; a 12 km trip costs 25.10 dollars",
                 interp="The expression works for every trip, not just this one, which is why it is "
                        "worth writing."),
            dict(q="Show that 4(x + 3) and 4x + 12 are equivalent.",
                 vis=F("bar_model", 7, [4, 3], [0], "four groups of (x + 3)"),
                 reasoning="Expanding the bracket shows the two forms have the same value for every "
                          "x, which is what equivalence means.",
                 steps=["4(x + 3) means four copies of (x + 3).",
                        "Four copies of x give 4x, and four copies of 3 give 12.",
                        "So 4(x + 3) = 4x + 12.",
                        "Check with x = 2: 4 × 5 = 20 and 8 + 12 = 20."],
                 ans="4(x + 3) = 4x + 12 for every value of x",
                 interp="The expanded form is easier to evaluate; the factorised form is easier to "
                        "read. Equivalence lets us choose."),
        ], inv=dict(
            task="A pattern of tiles has 1 tile in position 1, 4 in position 2, 7 in position 3 and "
                 "10 in position 4. Write the number of tiles as an expression in the position "
                 "number n, then test it for n = 10 and n = 100. Then find a second, different "
                 "expression that gives the same values.",
            fig=F("staircase", 4, "position 1, 2, 3, 4", cell=20),
            table=[["position n", "tiles", "3n − 2", "check"],
                   ["1", "1", "1", "3 × 1 − 2 = 1"],
                   ["2", "4", "4", "3 × 2 − 2 = 4"],
                   ["3", "7", "7", "3 × 3 − 2 = 7"],
                   ["4", "10", "10", "3 × 4 − 2 = 10"],
                   ["10", "28", "28", "3 × 10 − 2 = 28"],
                   ["100", "298", "298", "3 × 100 − 2 = 298"]],
            notice=["The number of tiles rises by 3 each time, so the expression contains 3n.",
                    "Subtracting 2 makes the expression work from position 1 rather than position 0.",
                    "The expression 1 + 3(n − 1) gives the same values, and it expands to 3n − 2.",
                    "Both forms predict the same number of tiles at any position."],
            obs="A pattern that grows by a constant amount is described by a linear expression, and "
                "several equivalent expressions can describe it.",
            concl="A generalisation of a growing pattern is an expression that works for every "
                  "position, and equivalent expressions are different forms of the same "
                  "generalisation.")),
        dict(id="3.2", title="Functions, domain and range",
             inquiry_q=("How can a rule that gives each input exactly one output be represented, "
                        "and what are its domain and range?"), teach=[
            "A function is a rule that gives exactly one output for each permitted input. The input is the independent variable and the output is the dependent variable.",
            "Function notation f(x) names the rule and the input together: f(x) = 2x + 1 means the rule is double and add one. f(3) = 7 is the value of the function at x = 3.",
            "The domain is the set of permitted inputs and the range is the set of outputs the rule can produce. The domain is a modelling choice, not a mathematical fact: a rule can be defined for all real numbers but only make sense for positive ones.",
            "A function can be represented as a mapping diagram, a table of values, a graph or a formula. The four representations describe the same relationship, and each one answers a different question about it.",
        ], examples=[
            dict(q="f(x) = 3x − 4. Find f(5), f(−2) and the value of x for which f(x) = 11.",
                 vis=F("function_machine", [(-2, -10), (5, 11), (3, 5)], "x → 3x − 4"),
                 reasoning="Substitution evaluates the function, and solving a linear equation "
                          "reverses it.",
                 steps=["f(5) = 3 × 5 − 4 = 11.",
                        "f(−2) = 3 × (−2) − 4 = −10.",
                        "3x − 4 = 11 gives 3x = 15, so x = 5."],
                 ans="f(5) = 11, f(−2) = −10, and f(x) = 11 when x = 5",
                 interp="Evaluating and solving are opposite operations on the same relationship."),
            dict(q="A function is defined by the rule 'add 6 then divide by 2'. Write it as a "
                   "formula, state a sensible domain, and find its range.",
                 vis=F("function_machine", [(0, 3), (4, 5), (10, 8)], "x → (x + 6) ÷ 2"),
                 reasoning="Translating a verbal rule into a formula makes the domain and range "
                          "explicit.",
                 steps=["g(x) = (x + 6)/2.",
                        "The formula is defined for every real x, so the domain is all real numbers.",
                        "Every real y can be produced, because x = 2y − 6 is real for any y.",
                        "So the range is also all real numbers."],
                 ans="g(x) = (x + 6)/2, domain and range both all real numbers",
                 interp="A formula with no division by a variable and no root usually has the "
                        "widest possible domain."),
        ], inv=dict(
            task="Take the rule 'multiply by 3, then subtract 1'. Build a table of values for "
                 "inputs −2, −1, 0, 1, 2, 3 and 4, draw the mapping diagram, plot the points on a "
                 "grid, and write the formula. Then change the rule to 'multiply by 3, then "
                 "subtract a number of your choice' and repeat.",
            fig=F("function_machine", [(-2, -7), (-1, -4), (0, -1), (1, 2), (2, 5), (3, 8), (4, 11)],
                  "x → 3x − 1"),
            table=[["input x", "3x", "3x − 1", "point on the graph"],
                   ["−2", "−6", "−7", "(−2, −7)"],
                   ["−1", "−3", "−4", "(−1, −4)"],
                   ["0", "0", "−1", "(0, −1)"],
                   ["1", "3", "2", "(1, 2)"],
                   ["2", "6", "5", "(2, 5)"],
                   ["3", "9", "8", "(3, 8)"],
                   ["4", "12", "11", "(4, 11)"]],
            notice=["The outputs rise by 3 each time the input rises by 1.",
                    "The points lie on a straight line, which is what a linear function looks like.",
                    "Changing the subtracted number moves the line up or down but does not change "
                    "its steepness.",
                    "Every input gave exactly one output, so the rule is a function."],
            obs="A rule that gives one output per input is a function, and a linear function gives "
                "outputs that change by a constant amount.",
            concl="A function assigns exactly one output to each permitted input; its domain is the "
                  "set of permitted inputs and its range the set of outputs, and both are choices "
                  "the modeller makes.")),
        dict(id="3.3", title="Expanding and factorising",
             inquiry_q=("How can equivalent forms of the same expression reveal different "
                        "information about it?"), teach=[
            "Expanding removes brackets by distributing: a(b + c) = ab + ac. It is the form that is easiest to evaluate and to collect like terms in.",
            "Factorising is the reverse: it puts a common factor or a product of factors back in. The factorised form makes zeros and roots visible, which the expanded form hides.",
            "Three products are worth knowing by sight: (x + a)(x + b) = x² + (a + b)x + ab, (a + b)² = a² + 2ab + b² and a² − b² = (a − b)(a + b).",
            "The difference of two squares is the most useful of the three, because it converts an addition into a product and is used again in Chapter 1 to rationalise a denominator.",
        ], examples=[
            dict(q="Expand and simplify (x + 5)(x − 3), then factorise x² + 7x + 10.",
                 vis=F("table", [["form", "expression", "what it shows"],
                                 ["factorised", "(x + 5)(x − 3)", "the two zeros"],
                                 ["expanded", "x² + 2x − 15", "the coefficients"],
                                 ["factorised", "(x + 2)(x + 5)", "the same zeros again"]],
                       caption="The same relationship, written in two forms."),
                 reasoning="Expanding distributes each term of one bracket over the other, and "
                          "factorising looks for two numbers with the right sum and product.",
                 steps=["(x + 5)(x − 3) = x² − 3x + 5x − 15 = x² + 2x − 15.",
                        "For x² + 7x + 10, find two numbers with product 10 and sum 7: 2 and 5.",
                        "x² + 7x + 10 = (x + 2)(x + 5)."],
                 ans="(x + 5)(x − 3) = x² + 2x − 15 and x² + 7x + 10 = (x + 2)(x + 5)",
                 interp="The expanded form shows the shape of the quadratic; the factorised form "
                        "shows where it equals zero."),
            dict(q="Factorise 6x² + 9x completely, and use the result to solve 6x² + 9x = 0.",
                 vis=F("bar_model", 15, [6, 9], [0], "the common factor 3x"),
                 reasoning="Taking out the highest common factor leaves a product, and a product "
                          "equals zero only when one of its factors does.",
                 steps=["6x² + 9x = 3x(2x + 3).",
                        "So 3x(2x + 3) = 0.",
                        "Either 3x = 0, giving x = 0, or 2x + 3 = 0, giving x = −3/2."],
                 ans="6x² + 9x = 3x(2x + 3); the solutions are x = 0 and x = −3/2",
                 interp="The factorised form solved an equation that the expanded form did not make "
                        "easy."),
        ], inv=dict(
            task="Expand (x + 2)(x + 3), (x + 2)(x + 5), (x + 4)(x + 5) and (x + 2)(x − 3). Record "
                 "the coefficient of x and the constant term in each case, and look for a pattern "
                 "that connects them to the numbers inside the brackets.",
            table=[["product", "expanded", "coefficient of x", "constant"],
                   ["(x + 2)(x + 3)", "x² + 5x + 6", "5", "6"],
                   ["(x + 2)(x + 5)", "x² + 7x + 10", "7", "10"],
                   ["(x + 4)(x + 5)", "x² + 9x + 20", "9", "20"],
                   ["(x + 2)(x − 3)", "x² − x − 6", "−1", "−6"]],
            notice=["The coefficient of x is always the sum of the two numbers in the brackets.",
                    "The constant term is always the product of those two numbers.",
                    "A negative number in a bracket can give a negative coefficient or constant.",
                    "The pattern works in reverse, which is exactly what factorising does."],
            obs="The expanded form of a product of two linear factors has coefficients that are the "
                "sum and product of the bracket numbers.",
            concl="(x + a)(x + b) = x² + (a + b)x + ab, so the expanded and factorised forms carry "
                  "the same information in different arrangements, and factorising reads the "
                  "pattern backwards.")),
        dict(id="3.4", title="Rearranging formulas",
             inquiry_q=("How can a formula be rewritten so that a different quantity is the "
                        "subject?"), teach=[
            "Rearranging a formula means applying the same operation to both sides until the wanted letter is isolated. Every step must keep the statement true.",
            "The operations are undone in the reverse of the order they were applied. To undo 'multiply by 3 then add 5', subtract 5 then divide by 3.",
            "A formula rearranged into a different subject is not a different formula. It is the same relationship in a form that answers a different question.",
            "Rearranging is the algebraic version of changing perspective: the same relationship, read from the other end.",
        ], examples=[
            dict(q="The formula for the area of a trapezium is A = ½(a + b)h. Make h the subject.",
                 vis=F("table", [["step", "operation", "result"],
                                 ["A = ½(a + b)h", "multiply by 2", "2A = (a + b)h"],
                                 ["2A = (a + b)h", "divide by (a + b)", "h = 2A/(a + b)"]],
                       caption="Undo the operations in the reverse order."),
                 reasoning="The height is multiplied by (a + b) and by ½, so both are undone by "
                          "reversing the order.",
                 steps=["A = ½(a + b)h.",
                        "Multiply both sides by 2: 2A = (a + b)h.",
                        "Divide both sides by (a + b): h = 2A/(a + b)."],
                 ans="h = 2A/(a + b)",
                 interp="The rearranged formula answers 'how high must it be' instead of 'what is "
                        "the area', using the same relationship."),
            dict(q="Make x the subject of y = (3x + 2)/(x − 1).",
                 vis=F("table", [["step", "operation", "result"],
                                 ["y = (3x + 2)/(x − 1)", "multiply by (x − 1)", "y(x − 1) = 3x + 2"],
                                 ["yx − y = 3x + 2", "collect x terms", "yx − 3x = y + 2"],
                                 ["x(y − 3) = y + 2", "divide by (y − 3)", "x = (y + 2)/(y − 3)"]],
                       caption="When the wanted letter appears twice, collect it on one side."),
                 reasoning="Clearing the denominator first, then collecting every term containing "
                          "x, isolates the wanted letter by factorising.",
                 steps=["y(x − 1) = 3x + 2.",
                        "yx − y = 3x + 2.",
                        "yx − 3x = y + 2.",
                        "x(y − 3) = y + 2.",
                        "x = (y + 2)/(y − 3), for y ≠ 3."],
                 ans="x = (y + 2)/(y − 3)",
                 interp="The restriction y ≠ 3 appears because x would then be undefined, which the "
                        "original formula also hides."),
        ], inv=dict(
            task="Take the relationship d = 5t + 20, where d is a distance in metres and t is a "
                 "time in seconds. Make t the subject, then find the time when d = 100. Then make a "
                 "formula of your own with two letters and rearrange it the other way round.",
            table=[["form", "expression", "what it answers"],
                   ["original", "d = 5t + 20", "how far in a given time"],
                   ["rearranged", "t = (d − 20)/5", "how long for a given distance"],
                   ["evaluated", "t = (100 − 20)/5 = 16", "the time for 100 m"]],
            notice=["Rearranging did not change the relationship; it changed the question.",
                    "Every step was the same operation on both sides.",
                    "The constant 20 was removed by subtraction, which is the inverse of addition.",
                    "The rearranged form is easier when the distance is known and the time is not."],
            obs="Rearranging applies inverse operations to both sides, so the relationship is "
                "preserved while the subject changes.",
            concl="A formula can be rearranged into any subject by applying inverse operations to "
                  "both sides in the reverse of the original order, and the rearranged formula is "
                  "the same relationship answering a different question.")),
        dict(id="3.5", title="Sequences, patterns and generalisation",
             inquiry_q=("How can a pattern in a sequence be written as a rule that works for any "
                        "term?"), teach=[
            "A sequence is an ordered list of numbers. The term-to-term rule says how to get from one term to the next; the position-to-term rule gives the term in any position directly.",
            "A linear sequence has a constant difference, so its nth term is an + b. The difference gives a and substituting one term gives b.",
            "A quadratic sequence has a constant second difference, so its nth term contains n². The second difference is twice the coefficient of n².",
            "A generalisation is a claim about every term, not just the ones listed. Checking the first five terms supports a generalisation; it does not prove it, and a counterexample at the sixth term destroys it.",
        ], examples=[
            dict(q="Find the nth term of the sequence 7, 11, 15, 19, 23, … and use it to find the "
                   "50th term.",
                 vis=F("staircase", 5, "7, 11, 15, 19, 23", cell=18),
                 reasoning="A constant difference means the rule is linear, so the nth term is an + b.",
                 steps=["The common difference is 4, so a = 4.",
                        "The nth term is 4n + b.",
                        "The first term is 7, so 4 × 1 + b = 7, giving b = 3.",
                        "The nth term is 4n + 3, and the 50th term is 4 × 50 + 3 = 203."],
                 ans="the nth term is 4n + 3; the 50th term is 203",
                 interp="The position-to-term rule gives any term without listing all the previous "
                        "ones."),
            dict(q="The nth term of a sequence is n² − 2n. Find the first four terms and the "
                   "second difference.",
                 vis=F("table", [["n", "n²", "−2n", "term"],
                                 ["1", "1", "−2", "−1"],
                                 ["2", "4", "−4", "0"],
                                 ["3", "9", "−6", "3"],
                                 ["4", "16", "−8", "8"]],
                       caption="A quadratic rule gives a constant second difference."),
                 reasoning="Substituting each position gives the terms, and the constant second "
                          "difference confirms the quadratic form.",
                 steps=["n = 1: 1 − 2 = −1.",
                        "n = 2: 4 − 4 = 0.",
                        "n = 3: 9 − 6 = 3.",
                        "n = 4: 16 − 8 = 8.",
                        "First differences: 1, 3, 5; second difference: 2."],
                 ans="the first four terms are −1, 0, 3, 8 and the second difference is 2",
                 interp="The second difference of 2 matches the coefficient of n², which is the "
                        "signature of a quadratic."),
        ], inv=dict(
            task="Build three sequences from patterns of your own: one with a constant difference, "
                 "one with a constant second difference, and one that is neither. For each, find "
                 "the nth term and test it on two terms that were not in your original list.",
            table=[["sequence", "type", "nth term", "test"],
                   ["3, 7, 11, 15, 19", "linear", "4n − 1", "n = 6 gives 23"],
                   ["1, 4, 9, 16, 25", "quadratic", "n²", "n = 7 gives 49"],
                   ["1, 2, 4, 7, 11", "neither", "differences 1, 2, 3, 4", "n = 6 gives 16 by the "
                    "difference pattern"]],
            notice=["The linear sequence had a constant difference of 4.",
                    "The quadratic sequence had a constant second difference of 2.",
                    "The third sequence had differences that grew by 1 each time, so it is not "
                    "linear or quadratic.",
                    "Each nth term predicted a term that was not in the original list."],
            obs="The pattern of first and second differences identifies the form of the nth term.",
            concl="A generalisation is a rule that works for every position, and it is identified by "
                  "the pattern of differences: a constant first difference gives a linear rule and "
                  "a constant second difference gives a quadratic one.")),
    ],
    practice=dict(
        A=[("3.1.1", "If f(x) = 4x − 7, find f(3) and f(−1).",
            "f(3) = 5 and f(−1) = −11", "Substitute each value and evaluate.", "F"),
           ("3.1.2", "Expand 5(2x − 3).",
            "10x − 15", "Distribute the 5 over both terms.", "F"),
           ("3.1.3", "Factorise 12x + 18.",
            "6(2x + 3)", "Take out the highest common factor.", "F"),
           ("3.1.4", "Expand and simplify (x + 4)(x − 2).",
            "x² + 2x − 8", "The coefficient of x is 4 − 2 and the constant is −8.", "F"),
           ("3.1.5", "Find the nth term of 5, 8, 11, 14, …",
            "3n + 2", "The common difference is 3 and the first term is 5.", "F"),
           ("3.1.6", "State the domain of f(x) = 1/(x − 2).",
            "all real numbers except x = 2",
            "Division by zero is undefined, so x = 2 is excluded.", "R"),
           ("3.1.7", "Simplify 3(x + 2) + 2(x − 5).",
            "5x − 4", "Expand both brackets, then collect like terms.", "F"),
           ("3.1.8", "Factorise x² − 9.",
            "(x + 3)(x − 3)", "A difference of two squares.", "F"),
           ("3.1.9", "If g(x) = x² − 3x, find g(4).",
            "4", "16 − 12 = 4.", "F"),
           ("3.1.10", "A sequence has nth term 2n² − 1. Find its first three terms.",
            "1, 7, 17", "Substitute n = 1, 2, 3.", "F"),
           ("3.1.11", "Make x the subject of y = 4x + 9.",
            "x = (y − 9)/4", "Subtract 9, then divide by 4.", "F"),
           ("3.1.12", "Explain the difference between a term-to-term rule and a position-to-term "
                      "rule.",
            "The term-to-term rule links consecutive terms; the position-to-term rule gives any "
            "term from its position.",
            "Only the position-to-term rule can jump directly to a distant term.", "R")],
        B=[("3.2.1", "Investigate: does the sequence 2, 4, 8, 16, 32 have a constant difference or "
                     "second difference?",
            "Neither — the first differences are 2, 4, 8, 16.",
            "The differences themselves grow, so the rule is not linear or quadratic.", "R"),
           ("3.2.2", "Test the claim: every sequence with a constant second difference is "
                     "quadratic.",
            "True — a constant second difference is the signature of an n² term.",
            "The second difference equals twice the coefficient of n².", "R"),
           ("3.2.3", "Investigate the sequence 1, 4, 9, 16, 25. Find the nth term and the next "
                     "term.",
            "n²; the next term is 36", "The terms are the perfect squares.", "F"),
           ("3.2.4", "Generalise: what is the nth term of 1, 8, 27, 64?",
            "n³", "The terms are the perfect cubes.", "R"),
           ("3.2.5", "Investigate whether 3n + 1 and 4n + 1 ever give the same value.",
            "No — they differ by n for every n.",
            "Setting them equal gives n = 0, which is not a position in the sequence.", "R"),
           ("3.2.6", "Test the claim: the product of three consecutive integers is always "
                     "divisible by 6.",
            "True — among any three consecutive integers one is divisible by 3 and at least one is "
            "even.",
            "The argument covers every case, not just the ones tested.", "R"),
           ("3.2.7", "Investigate the pattern of triangular numbers 1, 3, 6, 10, 15 and find the "
                     "nth term.",
            "n(n + 1)/2", "Each term adds the next integer, which sums to n(n + 1)/2.", "R"),
           ("3.2.8", "Find a counterexample to 'a sequence with a constant difference has a "
                     "positive nth term'.",
            "−3, −1, 1, 3 has a constant difference of 2 and a negative first term, so the nth "
            "term is 2n − 5.",
            "A constant difference fixes the form but not the sign of every term.", "R"),
           ("3.2.9", "Investigate: is (x + y)² ever equal to x² + y²?",
            "Only when x = 0 or y = 0, since (x + y)² = x² + 2xy + y².",
            "The extra 2xy term disappears only when one factor is zero.", "R"),
           ("3.2.10", "Generalise the pattern 1 × 1, 2 × 3, 3 × 5, 4 × 7 into an nth-term rule.",
            "n(2n − 1)", "The first factor is n and the second rises by 2 from 1.", "R"),
           ("3.2.11", "Investigate whether the nth term of 4, 9, 16, 25 is linear.",
            "No — the differences are 5, 7, 9 and the second difference is constant at 2.",
            "A constant second difference means the rule is quadratic.", "R")],
        C=[("3.3.1", "Explain in words why 2(x + 3) and 2x + 6 are the same expression.",
            "Expanding distributes the 2 over both terms inside the bracket.",
            "Distribution preserves the value for every x.", "R"),
           ("3.3.2", "Explain the difference between an equation and an expression, with an "
                     "example of each.",
            "An expression is a recipe with no equals sign; an equation states that two "
            "expressions are equal.",
            "Only equations have solutions.", "R"),
           ("3.3.3", "Write f(x) = 2x + 5 in words, and explain what f(0) means.",
            "Double the input and add 5; f(0) is the value of the function at input 0.",
            "Function notation names the rule and the input together.", "R"),
           ("3.3.4", "Explain why a table of values and a formula can describe the same function.",
            "Each table row is a pair (input, output) that the formula produces.",
            "The table is a finite sample of the rule.", "R"),
           ("3.3.5", "Explain why (x + 3)² is not x² + 9.",
            "The middle term 6x is missing: (x + 3)² = x² + 6x + 9.",
            "The bracket is multiplied by itself, so every term meets every term.", "R"),
           ("3.3.6", "A formula is written as C = 2πr. Explain what rearranging it to r = C/(2π) "
                     "changes.",
            "Nothing about the relationship; it changes which quantity is the subject.",
            "Rearranging preserves the relationship and changes the perspective.", "R"),
           ("3.3.7", "Explain why the domain of 'height of a plant after t days' is not all real "
                     "numbers.",
            "Time must be non-negative, and in practice it is limited to the growing season.",
            "A domain is a modelling choice, not a mathematical fact.", "R"),
           ("3.3.8", "Describe two representations of the function f(x) = x² and say what each "
                     "one shows best.",
            "A table shows values; a graph shows the shape and symmetry.",
            "Different representations answer different questions.", "R"),
           ("3.3.9", "Explain why factorising is useful for solving an equation.",
            "A product equals zero only when a factor is zero, so factorising finds the solutions.",
            "The expanded form hides the zeros.", "R"),
           ("3.3.10", "Explain the difference between a conjecture and a generalisation.",
            "A conjecture is a claim believed to be true; a generalisation is a claim shown to "
            "hold for every case.",
            "The difference is the justification, not the wording.", "R"),
           ("3.3.11", "Write the rule 'subtract 4, then square' as a formula and explain the order "
                      "of operations.",
            "f(x) = (x − 4)², and the subtraction happens first because of the brackets.",
            "Brackets fix the order in which operations are applied.", "R"),
           ("3.3.12", "Explain why the range of f(x) = x² is not all real numbers.",
            "A square is never negative, so the range is y ≥ 0.",
            "The range is limited by the operation, not by the domain.", "R")],
        D=[("3.4.1", "A plumber charges 40 dollars plus 55 dollars an hour. Write the cost "
                     "expression and find the cost of a 4.5-hour job.",
            "C = 40 + 55h; 287.50 dollars",
            "Substitute h = 4.5: 40 + 247.50.", "A"),
           ("3.4.2", "A phone plan costs 15 dollars a month plus 0.04 dollars a minute. How many "
                     "minutes can be used for a 30-dollar bill?",
            "375 minutes", "0.04m = 15, so m = 375.", "A"),
           ("3.4.3", "A taxi fare is 3 dollars plus 1.5 dollars per kilometre. Two riders travel 9 "
                     "km and 14 km. Find the difference in their fares.",
            "7.50 dollars", "1.5 × (14 − 9) = 7.50.", "A"),
           ("3.4.4", "A rectangular garden has length (x + 3) m and width (x − 1) m. Find the area "
                     "in expanded form and its value when x = 6.",
            "x² + 2x − 3; 45 m²", "36 + 12 − 3 = 45.", "A"),
           ("3.4.5", "A community group pays 80 dollars to hire a hall and 6 dollars per person "
                     "for food. Write the total cost for n people and find the cost per person.",
            "T = 80 + 6n; cost per person = 80/n + 6",
            "Dividing the total by n gives the per-person cost, which falls as n rises.", "A"),
           ("3.4.6", "A water tank fills at 12 litres a minute from an initial 50 litres. Write a "
                     "formula for the volume after t minutes and find when it reaches 350 litres.",
            "V = 50 + 12t; t = 25 minutes", "350 − 50 = 300 and 300 ÷ 12 = 25.", "A"),
           ("3.4.7", "A square has side (2x + 1). Find its area and its perimeter, then find x if "
                     "the perimeter is 30 cm.",
            "Area = (2x + 1)², perimeter = 8x + 4; x = 13/4",
            "8x + 4 = 30 gives x = 26/8 = 13/4.", "A"),
           ("3.4.8", "A delivery charge is 5 dollars plus 0.80 dollars per kilogram. Find the "
                     "weight that gives a total charge of 21 dollars.",
            "20 kg", "0.8w = 16, so w = 20.", "A"),
           ("3.4.9", "Explain whether a service that charges 20 dollars plus 2 dollars per item is "
                     "ever cheaper than one that charges 4 dollars per item.",
            "Yes — the fixed charge is recovered once the number of items exceeds 10.",
            "20 + 2n < 4n gives n > 10.", "R"),
           ("3.4.10", "A pattern of tiles has 2n + 3 tiles in row n. How many tiles are in rows 1 "
                      "to 5 altogether?",
            "45 tiles", "The terms are 5, 7, 9, 11, 13, which sum to 45.", "A"),
           ("3.4.11", "A savings account pays 5% simple interest on P dollars for t years. Write "
                      "the formula, make P the subject, and find the amount needed for 100 dollars "
                      "of interest in 2 years.",
            "I = 0.05Pt, so P = I/(0.05t); P = 1000 dollars",
            "100 ÷ (0.05 × 2) = 1000.", "A"),
           ("3.4.12", "Explain why a linear model of a phone bill is only sensible for a limited "
                      "range of minutes.",
            "Plans usually include a monthly allowance, so the fixed part changes once the "
            "allowance is used up.",
            "A model is valid only over the range where its assumptions hold.", "R")],
    ),
    assessment=[
        dict(title="A1 · The community event budget",
             text="A community event has a fixed cost of 250 dollars and a cost of 8 dollars per "
                  "attendee. Write the total cost as a formula, make the number of attendees the "
                  "subject, and find how many can attend if the budget is 1 000 dollars.",
             note="Criteria A and C · show the rearrangement and state the form of your answer."),
        dict(title="A2 · The tile pattern",
             text="A courtyard is tiled with a pattern in which row n has 3n + 2 tiles. Find the "
                  "number of tiles in row 20, the total for the first 20 rows, and explain whether "
                  "the pattern can continue indefinitely.",
             note="Criteria A and D · justify your total and comment on the limits of the model."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of generalisation and "
        "equivalence appear in your work?",
        "How is the global context of identities and relationships, and its exploration of "
        "relationships and communities, visible in the investigations and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a linear model of a real relationship, and what would you "
        "still like to ask?",
    ],
    review=dict(
        ideas=["A variable stands for a changing quantity, and an expression is a recipe built "
               "from variables.",
               "A function gives exactly one output for each permitted input.",
               "The domain is the set of permitted inputs and the range is the set of outputs.",
               "Expanding and factorising produce equivalent forms of the same expression.",
               "A difference of two squares factorises: a² − b² = (a − b)(a + b).",
               "Rearranging applies inverse operations to both sides, preserving the relationship.",
               "A constant first difference gives a linear rule; a constant second difference gives "
               "a quadratic rule."],
        vocab=["variable", "expression", "substitution", "function", "domain", "range",
               "function notation", "expand", "factorise", "subject of a formula", "sequence",
               "nth term", "generalisation"],
        mixed=[("3.R1", "Expand and simplify (x − 3)(x + 7)."),
               ("3.R2", "Factorise x² − 16."),
               ("3.R3", "Find the nth term of 6, 10, 14, 18, …"),
               ("3.R4", "Make t the subject of v = u + at."),
               ("3.R5", "If h(x) = x² − 4x, find h(6)."),
               ("3.R6", "Explain why a function cannot give two outputs for one input.")],
    ),
    projects=dict(
        service=[("Community need", "Community groups plan events without a shared way to estimate "
                                    "costs, so budgets are guessed."),
                 ("Mathematical connection", "Linear functions, substitution and rearranging "
                                             "formulas."),
                 ("Proposed action", "Build a simple cost model for one community event and publish "
                                     "it as a reusable formula."),
                 ("Expected impact", "The group can plan within a known budget instead of "
                                     "discovering the cost afterwards."),
                 ("Student reflection", "Record the formula, the assumptions it makes, and where "
                                        "they failed.")],
        community=[("Project idea", "A cost model for a school fair stall."),
                   ("Need", "Stall holders set prices without knowing their break-even point."),
                   ("Research question", "What price covers the costs of a stall, and what does a "
                                         "profit of a given size require?"),
                   ("Mathematics", "Linear functions, substitution and rearranging formulas."),
                   ("Action or outcome", "A one-page cost model and a recommended price."),
                   ("Beneficiaries", "Stall holders and the groups they raise money for."),
                   ("Evidence", "The model, the calculation and the recommended price.")],
        personal=[("Personal interest", "Gaming, sport or music practice."),
                  ("Learning goal", "To model a personal routine with a formula and use it to "
                                    "make a decision."),
                  ("Product or outcome", "A training or practice plan with a cost or time model."),
                  ("Mathematics", "Linear functions, sequences and substitution."),
                  ("Process", "Record data, fit a linear rule, then use it to predict."),
                  ("Evidence", "The data, the formula and the prediction.")],
    ),
),
])

CHAPTERS.extend([
dict(
    num=4, title="Linear relationships and graphs",
    key="Relationships", related=["Change", "Representation"],
    context="Fairness and development",
    exploration="Distribution of resources",
    inquiry=("The relationship between two quantities that change at a constant rate can be "
             "represented as a straight line, and the equivalence between a table, a graph and an "
             "equation allows that relationship to be used to predict — and the prediction to be "
             "judged."),
    atl=("Communication",
         "In order for a student to explain a linear relationship to an audience, students must "
         "choose a representation that suits that audience, label the axes and the units, and "
         "justify the choice of representation in the explanation."),
    standfirst="Two quantities that change together at a constant rate produce a straight line. "
               "The gradient is the rate of change and the intercept is where the line starts.",
    engage="A village water point is filled by two pumps. Pump A delivers 40 litres a minute and "
           "pump B delivers 55 litres a minute, starting 5 minutes later. Both graphs are straight "
           "lines. When does B overtake A, and what does the crossing point mean?",
    questions=[("Factual", "How do you find the gradient of a line from two points, and how do "
                           "you write its equation?"),
               ("Conceptual", "Why does a constant rate of change always produce a straight-line "
                              "graph, and what does the y-intercept represent in a real situation?"),
               ("Debatable", "Is a prediction made by extending a straight-line graph beyond the "
                             "collected data a mathematical fact or an assumption?")],
    application_lede="These tasks use tables, gradients, equations of lines, direct proportion and "
                     "linear models. State the representation you used and why it was the "
                     "clearest one.",
    projects_lede="Resource distribution is a linear-modelling problem. Use the model to plan, and "
                  "say plainly where the model stops being valid.",
    sections=[
        dict(id="4.1", title="From tables to straight lines",
             inquiry_q=("How can a table of paired values show that a relationship is linear, and "
                        "what does the graph add?"), teach=[
            "A table of values lists matching input and output pairs. If the output changes by the same amount whenever the input changes by the same amount, the relationship is linear.",
            "Plotting the pairs turns the table into a picture. Linear pairs give points that lie on a straight line, which is the visual signature of a constant rate of change, and this graph representation answers questions the table cannot.",
            "The graph shows what the table hides: where the line crosses the axes, how steep it is, and where it crosses another line. Those features are answers to questions the table cannot answer directly.",
            "Reading a graph back into a table is the reverse process, and it is the standard way to check that a plotted line has been drawn correctly.",
        ], examples=[
            dict(q="A car hire costs 30 dollars plus 12 dollars a day. Complete the table for 0 to "
                   "5 days and plot the points.",
                 vis=F("table", [["days d", "cost C = 30 + 12d"],
                                 ["0", "30"], ["1", "42"], ["2", "54"], ["3", "66"], ["4", "78"],
                                 ["5", "90"]],
                       caption="A constant difference of 12 means the points lie on a straight line."),
                 reasoning="Each extra day adds the same 12 dollars, so the first differences are "
                          "constant and the graph is linear.",
                 steps=["C = 30 + 12d.",
                        "d = 0 gives 30, and each further day adds 12.",
                        "The values are 30, 42, 54, 66, 78, 90.",
                        "Plotted, they lie on a straight line with gradient 12."],
                 ans="the costs are 30, 42, 54, 66, 78 and 90 dollars",
                 interp="The constant difference of 12 dollars is the rate of change, and it becomes "
                        "the gradient of the line."),
            dict(q="A table gives (1, 5), (2, 8), (3, 11), (4, 14). Is the relationship linear, "
                   "and what is its rule?",
                 vis=F("grid", [(1, 5), (2, 8), (3, 11), (4, 14)], ["A", "B", "C", "D"],
                       xmin=0, xmax=5, ymin=0, ymax=16, title="four points, one line"),
                 reasoning="Constant first differences mean a linear rule, and the rule can be read "
                          "from the pattern of the values.",
                 steps=["The x-values rise by 1 and the y-values rise by 3 each time.",
                        "A constant difference of 3 means the relationship is linear.",
                        "The rule is y = 3x + b, and x = 1 gives y = 5, so b = 2.",
                        "The rule is y = 3x + 2."],
                 ans="yes, the relationship is linear and the rule is y = 3x + 2",
                 interp="The graph confirms the rule: four points that lie on one line cannot "
                        "disagree."),
        ], inv=dict(
            task="Measure how far a toy car travels when it is released from ramps of different "
                 "heights. Record five pairs of values, plot them, and decide whether the "
                 "relationship is linear. Then use your graph to predict the distance for a ramp "
                 "height you did not test.",
            fig=F("grid", [(2, 18), (4, 31), (6, 45), (8, 58), (10, 72)],
                  ["", "", "", "", ""], xmin=0, xmax=12, ymin=0, ymax=80,
                  title="ramp height against distance"),
            table=[["ramp height (cm)", "distance (cm)", "first difference"],
                   ["2", "18", "—"],
                   ["4", "31", "13"],
                   ["6", "45", "14"],
                   ["8", "58", "13"],
                   ["10", "72", "14"]],
            notice=["The first differences are all close to 13 or 14 cm.",
                    "The points nearly lie on a straight line, so the relationship is approximately "
                    "linear.",
                    "Small departures from the line come from measurement error, not from a "
                    "different rule.",
                    "Extending the line predicts about 86 cm for a 12 cm ramp."],
            obs="A roughly constant difference gives points that nearly lie on a straight line, "
                "which is what real measurement data looks like.",
            concl="A relationship is linear when equal changes in the input give equal changes in "
                  "the output, and the graph of such a relationship is a straight line whose "
                  "gradient is that equal change.")),
        dict(id="4.2", title="Gradient as a rate of change",
             inquiry_q=("What does the gradient of a line measure, and how is it computed from two "
                        "points?"), teach=[
            "The gradient of a line is the change in y divided by the change in x between any two points on it: m = (y₂ − y₁)/(x₂ − x₁). It is a rate of change.",
            "A positive gradient rises left to right, a negative gradient falls, and a zero gradient is horizontal. A vertical line has no gradient at all.",
            "Because the gradient is the same between any two points on a line, it is enough to know two points to draw the line. This is what makes the equation of a line a complete description of it.",
            "Parallel lines have equal gradients. Perpendicular lines have gradients whose product is −1, which is met formally in MYP 4.",
        ], examples=[
            dict(q="Find the gradient of the line through (2, 7) and (6, 19), and interpret it.",
                 vis=F("grid", [(2, 7), (6, 19)], ["(2, 7)", "(6, 19)"],
                       xmin=0, xmax=8, ymin=0, ymax=22, title="gradient = 12 ÷ 4 = 3"),
                 reasoning="The gradient is the change in y over the change in x, which is the rate "
                          "of change of y with respect to x.",
                 steps=["Change in y = 19 − 7 = 12.",
                        "Change in x = 6 − 2 = 4.",
                        "Gradient = 12/4 = 3.",
                        "So y rises by 3 units for every 1 unit rise in x."],
                 ans="the gradient is 3",
                 interp="The gradient is the rate of change, so it answers 'how fast' rather than "
                        "'how much'."),
            dict(q="A line falls from (0, 20) to (8, 4). Find its gradient and say what it means.",
                 vis=F("grid", [(0, 20), (8, 4)], ["(0, 20)", "(8, 4)"],
                       xmin=0, xmax=10, ymin=0, ymax=24, title="gradient = −16 ÷ 8 = −2"),
                 reasoning="A falling line has a negative gradient, because the change in y is "
                          "negative.",
                 steps=["Change in y = 4 − 20 = −16.",
                        "Change in x = 8 − 0 = 8.",
                        "Gradient = −16/8 = −2.",
                        "So y falls by 2 units for every 1 unit rise in x."],
                 ans="the gradient is −2",
                 interp="The negative sign is the direction of the change, and the 2 is its size."),
        ], inv=dict(
            task="Draw four lines on the same grid: one rising, one falling, one horizontal and one "
                 "vertical. For each, choose two points and compute the gradient. Then draw a line "
                 "parallel to the rising line and check whether the gradients agree.",
            fig=F("grid", [(0, 0), (4, 8), (4, 0), (0, 8)], ["", "", "", ""],
                  xmin=0, xmax=10, ymin=0, ymax=10, title="four lines, four gradients"),
            table=[["line", "two points", "change in y", "change in x", "gradient"],
                   ["rising", "(0, 0) and (4, 8)", "8", "4", "2"],
                   ["falling", "(0, 8) and (4, 0)", "−8", "4", "−2"],
                   ["horizontal", "(0, 4) and (8, 4)", "0", "8", "0"],
                   ["vertical", "(4, 0) and (4, 8)", "8", "0", "undefined"]],
            notice=["The rising line has a positive gradient and the falling line a negative one.",
                    "The horizontal line has gradient 0 because y does not change.",
                    "The vertical line has no gradient, because the change in x is zero.",
                    "The parallel line through (0, 1) and (4, 9) also has gradient 2."],
            obs="The gradient is the change in y per unit change in x, and it is the same for every "
                "pair of points on a line.",
            concl="The gradient of a line is m = (y₂ − y₁)/(x₂ − x₁) for any two points on it, and "
                  "it measures the rate of change of y with respect to x.")),
        dict(id="4.3", title="The equation of a straight line",
             inquiry_q=("How can one equation describe every point on a line?"), teach=[
            "The equation y = mx + c describes every point on the line with gradient m and y-intercept c. Substituting any x gives the matching y, and every such pair lies on the line.",
            "The gradient-intercept form is the fastest to write when both are known. The point-gradient form y − y₁ = m(x − x₁) is faster when a point and the gradient are known.",
            "Two lines with the same gradient never meet. Two lines with different gradients meet exactly once, and the intersection is the point that satisfies both equations.",
            "The equation is a complete description of the line: drawing it, reading a value from it, and finding where it crosses another line are all consequences of the same two numbers m and c.",
        ], examples=[
            dict(q="Find the equation of the line through (1, 4) with gradient −3.",
                 vis=F("grid", [(1, 4), (2, 1), (0, 7)], ["(1, 4)", "(2, 1)", "(0, 7)"],
                       xmin=-1, xmax=4, ymin=0, ymax=9, title="y = −3x + 7"),
                 reasoning="One point and the gradient are enough to fix the line, and substituting "
                          "the point into y = mx + c gives c.",
                 steps=["m = −3, so the equation is y = −3x + c.",
                        "The point (1, 4) lies on it: 4 = −3 × 1 + c.",
                        "So c = 7.",
                        "The equation is y = −3x + 7."],
                 ans="y = −3x + 7",
                 interp="The intercept 7 is where the line meets the y-axis, and it is the value of "
                        "y when x = 0."),
            dict(q="Find where y = 2x + 1 meets y = −x + 7.",
                 vis=F("grid", [(0, 1), (2, 5), (0, 7), (3, 4)], ["", "", "", ""],
                       xmin=-1, xmax=5, ymin=0, ymax=9, title="the crossing point (2, 5)"),
                 reasoning="The intersection satisfies both equations, so solving them together "
                          "gives the point.",
                 steps=["2x + 1 = −x + 7.",
                        "3x = 6, so x = 2.",
                        "y = 2 × 2 + 1 = 5.",
                        "The lines meet at (2, 5)."],
                 ans="the lines meet at (2, 5)",
                 interp="The crossing point is the only pair of values that makes both equations "
                        "true at once."),
        ], inv=dict(
            task="Take the equation y = 2x − 1. Build a table for x from −2 to 3, plot the points, "
                 "then change the equation to y = 2x + 3 and repeat on the same grid. Then try "
                 "y = −2x − 1. Record what changed and what stayed the same.",
            fig=F("grid", [(-2, -5), (-1, -3), (0, -1), (1, 1), (2, 3), (3, 5)],
                  ["", "", "", "", "", ""], xmin=-3, xmax=4, ymin=-7, ymax=7,
                  title="three lines from one gradient"),
            table=[["equation", "gradient", "y-intercept", "what it shows"],
                   ["y = 2x − 1", "2", "−1", "rises, crossing y at −1"],
                   ["y = 2x + 3", "2", "3", "rises the same way, crossing y at 3"],
                   ["y = −2x − 1", "−2", "−1", "falls, crossing y at −1"]],
            notice=["Changing the constant moved the line up without changing its steepness.",
                    "Changing the sign of the gradient turned the rising line into a falling one.",
                    "The first two lines are parallel because their gradients are equal.",
                    "All three lines pass through the y-axis at the value of c."],
            obs="The gradient fixes the steepness and the constant fixes the position, and together "
                "they fix the line completely.",
            concl="Every straight line has an equation y = mx + c, where m is the gradient and c is "
                  "the y-intercept, and two numbers describe the whole line.")),
        dict(id="4.4", title="Direct proportion",
             inquiry_q=("When does a linear relationship pass through the origin, and what does "
                        "that mean?"), teach=[
            "Direct proportion is the relationship y = kx for a constant k. Its graph is a straight line through the origin, because y = 0 when x = 0.",
            "The constant k is the constant of proportionality. It is the gradient of the line and the value of y when x = 1.",
            "A relationship is directly proportional exactly when y/x is the same for every pair. This is the test, and it is a division rather than a subtraction.",
            "Direct proportion is the model behind unit prices, exchange rates and scale drawings. Recognising it saves work, because one pair of values gives the whole rule.",
        ], examples=[
            dict(q="5 identical books weigh 11 kg. Find the weight of 8 books, and the constant of "
                   "proportionality.",
                 vis=F("double_number_line", ["5", "10"], ["11", "22"], "books : mass"),
                 reasoning="Identical items give a directly proportional relationship, so one unit "
                          "value scales to any number of items.",
                 steps=["Mass per book = 11 ÷ 5 = 2.2 kg.",
                        "So the constant of proportionality is 2.2.",
                        "For 8 books: 8 × 2.2 = 17.6 kg."],
                 ans="17.6 kg, with a constant of proportionality of 2.2 kg per book",
                 interp="The graph of mass against number of books is a straight line through the "
                        "origin."),
            dict(q="Is y directly proportional to x for the pairs (3, 15), (5, 25), (7, 34)?",
                 vis=F("table", [["x", "y", "y ÷ x"],
                                 ["3", "15", "5"],
                                 ["5", "25", "5"],
                                 ["7", "34", "4.857…"]],
                       caption="Direct proportion needs the same quotient every time."),
                 reasoning="The quotient y/x must be constant, and one different value is enough to "
                          "rule the relationship out.",
                 steps=["15 ÷ 3 = 5.",
                        "25 ÷ 5 = 5.",
                        "34 ÷ 7 = 4.857…, which is not 5.",
                        "The quotients are not all equal, so y is not directly proportional to x."],
                 ans="no, because the quotients are not constant",
                 interp="The third pair breaks the pattern, which is why the test is a check on "
                        "every pair."),
        ], inv=dict(
            task="Collect five pairs of values for a directly proportional relationship of your own "
                 "(for example, cost against number of identical items). Compute y ÷ x for each "
                 "pair, plot the points, and check whether the line passes through the origin. Then "
                 "add a fixed delivery charge and repeat.",
            fig=F("grid", [(1, 4), (2, 8), (3, 12), (4, 16), (5, 20)], ["", "", "", "", ""],
                  xmin=0, xmax=6, ymin=0, ymax=24, title="a line through the origin"),
            table=[["x", "y (no charge)", "y ÷ x", "y (with 5 charge)", "y ÷ x"],
                   ["1", "4", "4", "9", "9"],
                   ["2", "8", "4", "13", "6.5"],
                   ["3", "12", "4", "17", "5.67"],
                   ["4", "16", "4", "21", "5.25"],
                   ["5", "20", "4", "25", "5"]],
            notice=["Without the charge, y ÷ x was 4 every time and the line passed through the "
                    "origin.",
                    "With the charge, the quotients changed and the line crossed the y-axis at 5.",
                    "The fixed charge is a y-intercept, and it is what breaks direct proportion.",
                    "Both graphs are straight lines, so both are linear — but only one is "
                    "proportional."],
            obs="Direct proportion is the special linear case where the quotient y/x is constant, "
                "which is why the line passes through the origin.",
            concl="y is directly proportional to x exactly when y = kx for a constant k, which "
                  "means the graph passes through the origin and the quotient y/x is the same for "
                  "every pair.")),
        dict(id="4.5", title="Linear models, prediction and fairness",
             inquiry_q=("When is a prediction from a linear model justified, and when is it not?"), teach=[
            "A linear model assumes that the rate of change stays constant. Inside the range of the collected data this is often reasonable; outside it, the model is an assumption.",
            "Interpolation is prediction inside the range of the data, and it is usually safe. Extrapolation is prediction outside it, and it can fail badly.",
            "A good model states its assumptions. 'Cost = 30 + 12 per day for the first 10 days' is honest; 'cost = 30 + 12 per day' is not, because eventually the rate changes.",
            "Linear models are used to allocate resources, and a model that fits one group can be unfair to another. Checking the residuals — the gaps between the model and the data — is part of judging the model.",
        ], examples=[
            dict(q="A plumber's call-out cost follows C = 45 + 38h for the first 4 hours. Predict "
                   "the cost of a 3-hour job, and comment on using the model for 12 hours.",
                 vis=F("table", [["hours", "model cost", "comment"],
                                 ["1", "83", "inside the range"],
                                 ["3", "159", "inside the range"],
                                 ["4", "197", "the last reliable value"],
                                 ["12", "501", "outside the stated range"]],
                       caption="A model is reliable only where its assumptions hold."),
                 reasoning="Interpolation inside the stated range is reliable; extrapolation beyond "
                          "it assumes the rate continues, which the model does not claim.",
                 steps=["For 3 hours: C = 45 + 38 × 3 = 159 dollars.",
                        "This is inside the stated range, so the prediction is reliable.",
                        "For 12 hours: C = 45 + 38 × 12 = 501 dollars.",
                        "But the model was stated for the first 4 hours only, so this is "
                        "extrapolation."],
                 ans="159 dollars for 3 hours; the 12-hour figure of 501 dollars is an extrapolation "
                     "beyond the model's stated range",
                 interp="The mathematics is correct in both cases; only the justification differs."),
            dict(q="Two shops charge for printing. Shop A: C = 2 + 0.10n. Shop B: C = 0.40n. For "
                   "how many pages are they equal, and which is cheaper below that?",
                 vis=F("grid", [(0, 2), (10, 3), (0, 0), (10, 4)], ["A", "A", "B", "B"],
                       xmin=0, xmax=12, ymin=0, ymax=5, title="the crossing point"),
                 reasoning="The two models are equal where their graphs cross, and the cheaper shop "
                          "is the one with the lower value at that quantity.",
                 steps=["2 + 0.10n = 0.40n.",
                        "2 = 0.30n, so n = 6.67.",
                        "For fewer than about 7 pages, shop A is cheaper.",
                        "For more than about 7 pages, shop B is cheaper."],
                 ans="equal at about 6.67 pages; shop A is cheaper below that and shop B above",
                 interp="The crossing point is the decision boundary, and it comes from solving two "
                        "linear models together."),
        ], inv=dict(
            task="Model the growth of a plant over six weeks by measuring its height each week. "
                 "Fit a straight line by eye, use it to predict the height at week 10, and then "
                 "measure the plant again in a later week if you can. Record how far the prediction "
                 "was from the measurement.",
            fig=F("grid", [(1, 4), (2, 7), (3, 11), (4, 15), (5, 18), (6, 22)],
                  ["", "", "", "", "", ""], xmin=0, xmax=10, ymin=0, ymax=32,
                  title="height against week"),
            table=[["week", "height (cm)", "predicted by the line", "residual"],
                   ["1", "4", "3.8", "0.2"],
                   ["2", "7", "7.4", "−0.4"],
                   ["3", "11", "11.0", "0.0"],
                   ["4", "15", "14.6", "0.4"],
                   ["5", "18", "18.2", "−0.2"],
                   ["6", "22", "21.8", "0.2"]],
            notice=["The residuals are small and both positive and negative, so the line fits well.",
                    "The predicted height at week 10 was about 37 cm.",
                    "Real plants stop growing, so the week-10 prediction is an assumption rather "
                    "than a fact.",
                    "The residuals are the gaps between the model and the data."],
            obs="A linear model fits when its residuals are small and balanced, and its predictions "
                "are only as trustworthy as that fit.",
            concl="A linear model predicts reliably inside the range of the collected data, and "
                  "outside that range it states an assumption about the rate of change continuing "
                  "— which is why the range must be reported with the prediction.")),
    ],
    practice=dict(
        A=[("4.1.1", "Find the gradient of the line through (1, 3) and (5, 15).",
            "3", "Change in y is 12 and change in x is 4.", "F"),
           ("4.1.2", "Write the equation of the line with gradient 4 and y-intercept −2.",
            "y = 4x − 2", "Use y = mx + c.", "F"),
           ("4.1.3", "Find the gradient of the horizontal line through (2, 7) and (9, 7).",
            "0", "The change in y is zero.", "F"),
           ("4.1.4", "A line passes through (0, 5) and (4, 13). Find its equation.",
            "y = 2x + 5", "The gradient is 8 ÷ 4 = 2 and the intercept is 5.", "F"),
           ("4.1.5", "Is y directly proportional to x for the pairs (2, 6), (4, 12), (6, 18)?",
            "Yes — the quotient is 3 throughout",
            "Direct proportion needs a constant quotient.", "F"),
           ("4.1.6", "Find the y-intercept of y = −3x + 8.",
            "8", "The intercept is the constant term.", "F"),
           ("4.1.7", "Find the equation of the line through (2, 1) with gradient −5.",
            "y = −5x + 11", "1 = −10 + c gives c = 11.", "F"),
           ("4.1.8", "A table gives (0, 4), (2, 10), (4, 16). Find the gradient and the equation.",
            "gradient 3, y = 3x + 4", "Each step of 2 in x gives 6 in y.", "F"),
           ("4.1.9", "Where do y = x + 1 and y = 5 − x meet?",
            "(2, 3)", "x + 1 = 5 − x gives x = 2.", "F"),
           ("4.1.10", "A line has gradient 0.5 and passes through (6, 8). Find its equation.",
            "y = 0.5x + 5", "8 = 3 + c gives c = 5.", "F"),
           ("4.1.11", "Find the gradient of the line through (−2, 4) and (3, −6).",
            "−2", "−10 ÷ 5 = −2.", "F"),
           ("4.1.12", "Explain why a vertical line has no gradient.",
            "The change in x is zero, so the quotient is undefined.",
            "Division by zero is not defined.", "R")],
        B=[("4.2.1", "Investigate: do the lines y = 2x + 1 and y = 2x − 7 ever meet? Justify.",
            "No — they have the same gradient, so they are parallel.",
            "Lines with equal gradients and different intercepts never meet.", "R"),
           ("4.2.2", "Test the claim: if two lines have the same y-intercept they must meet.",
            "False — y = 2x and y = 3x both pass through the origin and meet there, but y = 2x + 1 "
            "and y = 2x + 1 are the same line. A counterexample is y = x and y = x + 1, which do "
            "not share an intercept at all.",
            "Sharing an intercept means sharing a point, so the lines do meet there.", "R"),
           ("4.2.3", "Investigate the gradients of the lines y = 3x, y = 3x + 5 and y = −3x. What "
                     "do they have in common?",
            "The first two have the same gradient 3 and are parallel; the third has gradient −3.",
            "Only the gradient controls steepness.", "R"),
           ("4.2.4", "Generalise: what is the gradient of the line through (a, b) and (c, d)?",
            "(d − b)/(c − a)", "The gradient is the change in y over the change in x.", "R"),
           ("4.2.5", "Investigate whether the points (1, 2), (3, 6) and (5, 10) lie on one line.",
            "Yes — the gradient is 2 between each consecutive pair.",
            "A constant gradient between consecutive points means collinearity.", "R"),
           ("4.2.6", "Test the claim: a line with a negative gradient must have a negative "
                     "y-intercept.",
            "False — y = −2x + 5 has gradient −2 and intercept 5.",
            "The gradient and the intercept are independent.", "R"),
           ("4.2.7", "Investigate: for what value of k do y = kx and y = x + 4 meet at x = 8?",
            "k = 1.5", "y = 12 at x = 8, so 8k = 12.", "R"),
           ("4.2.8", "Generalise a rule for the gradient of a line perpendicular to a line of "
                     "gradient m.",
            "−1/m", "The product of the gradients is −1.", "R"),
           ("4.2.9", "Investigate the pattern 2, 5, 8, 11, … as points (n, term). What is the "
                     "gradient of the line through them?",
            "3", "The common difference is the gradient.", "R"),
           ("4.2.10", "Test the claim: two lines that meet must have different gradients.",
            "True — equal gradients give parallel lines, which never meet.",
            "Distinct meeting lines must have different gradients.", "R"),
           ("4.2.11", "Investigate whether the line through (0, 0) and (3, −9) has the same "
                      "gradient as the line through (1, 1) and (4, −8).",
            "Yes — both have gradient −3.",
            "Equal gradients mean the lines are parallel or identical.", "R")],
        C=[("4.3.1", "Explain in words what the gradient of a line represents in a real situation.",
            "The rate of change of the vertical quantity per unit of the horizontal quantity.",
            "The gradient is a rate, so it carries units.", "R"),
           ("4.3.2", "Explain the difference between interpolation and extrapolation.",
            "Interpolation predicts inside the range of the data; extrapolation predicts outside "
            "it.",
            "Only the first is supported by the evidence.", "R"),
           ("4.3.3", "Explain why a straight-line graph through the origin indicates direct "
                     "proportion.",
            "Because y = kx gives y = 0 when x = 0.",
            "The origin corresponds to both quantities being zero.", "R"),
           ("4.3.4", "Describe two ways to find the equation of a line, and say when each is "
                     "quickest.",
            "Use two points for the gradient, or use a point and the gradient directly.",
            "The choice depends on what information is given.", "R"),
           ("4.3.5", "Explain what a residual is and what it tells you about a model.",
            "The gap between the model's prediction and the measured value.",
            "Small balanced residuals indicate a good fit.", "R"),
           ("4.3.6", "Explain why the equation y = mx + c is a complete description of a line.",
            "It fixes both the steepness and the position, which determine the line uniquely.",
            "Two numbers are enough to fix a straight line.", "R"),
           ("4.3.7", "A graph of cost against distance has a positive y-intercept. Explain what "
                     "that means for a customer.",
            "There is a fixed charge payable even for zero distance.",
            "The intercept is the value at zero input.", "R"),
           ("4.3.8", "Explain why parallel lines have equal gradients, using the definition of "
                     "gradient.",
            "Equal gradients mean equal rates of change, so the lines can never meet.",
            "The gradient is the same everywhere on a line.", "R"),
           ("4.3.9", "Describe how you would check whether three points lie on one straight line.",
            "Compute the gradient between consecutive pairs and check they are equal.",
            "A constant gradient between consecutive points means collinearity.", "R"),
           ("4.3.10", "Explain the difference between a linear relationship and a directly "
                      "proportional one.",
            "Direct proportion is the special case whose line passes through the origin.",
            "A linear relationship may have a non-zero intercept.", "R"),
           ("4.3.11", "Explain why a model that fits one community's data may not be fair to "
                      "another.",
            "The gradient and intercept describe that community's situation, not a universal rule.",
            "A model inherits the range and the population it was fitted to.", "R"),
           ("4.3.12", "Describe how you would use a graph to compare two service charges.",
            "Plot both lines and find the crossing point, which is the break-even quantity.",
            "The crossing point is the decision boundary.", "R")],
        D=[("4.4.1", "A school pays 120 dollars for a hall and 7 dollars per chair. Write the cost "
                     "model and find the cost for 45 chairs.",
            "C = 120 + 7n; 435 dollars", "120 + 7 × 45 = 435.", "A"),
           ("4.4.2", "A taxi charges 4 dollars plus 1.60 dollars per kilometre. Find the fare for "
                     "11 km and the distance that costs 20 dollars.",
            "21.60 dollars; 10 km", "20 − 4 = 16 and 16 ÷ 1.6 = 10.", "A"),
           ("4.4.3", "Two phone plans: A costs 10 dollars plus 0.05 dollars a minute, B costs 25 "
                     "dollars plus 0.02 dollars a minute. Find the number of minutes at which they "
                     "cost the same.",
            "500 minutes", "10 + 0.05m = 25 + 0.02m gives 0.03m = 15.", "A"),
           ("4.4.4", "A water tank is filled at 15 litres a minute and already holds 60 litres. "
                     "Find the time to reach 360 litres and sketch the graph.",
            "20 minutes", "360 − 60 = 300 and 300 ÷ 15 = 20.", "A"),
           ("4.4.5", "A farmer sells maize at 0.35 dollars a kilogram and pays 50 dollars to "
                     "transport it. Write a model for the profit and find the break-even mass.",
            "P = 0.35m − 50; about 143 kg", "0.35m = 50 gives m ≈ 142.9.", "A"),
           ("4.4.6", "Explain whether a model that charges a fixed fee plus a per-minute rate is "
                     "directly proportional.",
            "No — the fixed fee gives a non-zero intercept, so the line does not pass through the "
            "origin.",
            "Direct proportion requires the line to pass through the origin.", "R"),
           ("4.4.7", "A cyclist covers 12 km in 40 minutes at a constant speed. Find the speed and "
                     "the distance covered in 75 minutes.",
            "18 km/h; 22.5 km", "12 ÷ (40/60) = 18 and 18 × 1.25 = 22.5.", "A"),
           ("4.4.8", "A printing firm charges 15 dollars setup plus 0.08 dollars per page. Find "
                     "the number of pages that makes the cost 47 dollars.",
            "400 pages", "47 − 15 = 32 and 32 ÷ 0.08 = 400.", "A"),
           ("4.4.9", "A village shares a water allowance in proportion to household size. Model "
                     "the allocation and comment on whether the model is fair.",
            "allowance = (household size ÷ total size) × total water; fairness depends on whether "
            "size is the agreed basis.",
            "A proportional model is only fair if the basis is agreed.", "R"),
           ("4.4.10", "A linear model predicts a school roll of 620 in five years. The roll is "
                      "growing by 20 a year. Find the current roll and comment on the assumption.",
            "520 now; the assumption is that the growth rate stays at 20 a year",
            "620 − 5 × 20 = 520.", "R"),
           ("4.4.11", "Two delivery services charge 8 dollars plus 0.50 dollars a kilogram and 3 "
                      "dollars plus 0.75 dollars a kilogram. Find the mass at which they cost the "
                      "same and say which is cheaper above it.",
            "20 kg; the first service is cheaper above it",
            "8 + 0.5m = 3 + 0.75m gives 5 = 0.25m.", "A"),
           ("4.4.12", "Explain why extrapolating a linear model of plant growth beyond the "
                      "growing season gives an unreasonable answer.",
            "Plants stop growing, so the constant-rate assumption fails.",
            "A model is valid only where its assumptions hold.", "R")],
    ),
    assessment=[
        dict(title="A1 · The two water pumps",
             text="Pump A delivers 40 litres a minute into an empty tank. Pump B delivers 55 litres "
                  "a minute but starts 5 minutes later. Model both with linear equations, find when "
                  "B overtakes A, and sketch both graphs on the same axes.",
             note="Criteria A and C · label the axes with units and state what the crossing point "
                  "means."),
        dict(title="A2 · The shared water allowance",
             text="A village of 240 households shares 60 000 litres of water a week in proportion "
                  "to household size. Model the allocation, find the allowance for a household of "
                  "6, and discuss whether the model is fair to households of 1.",
             note="Criteria A and D · justify the model and comment on its limits."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of change and "
        "representation appear in your work?",
        "How is the global context of fairness and development, and its exploration of the "
        "distribution of resources, visible in the investigations and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the chapter? "
        "Explain how.",
        "What are the limitations of a linear model for sharing resources, and what would you still "
        "like to ask?",
    ],
    review=dict(
        ideas=["A table with constant first differences describes a linear relationship.",
               "The gradient is the change in y per unit change in x: m = (y₂ − y₁)/(x₂ − x₁).",
               "Every straight line has an equation y = mx + c.",
               "Parallel lines have equal gradients.",
               "Direct proportion is y = kx, a line through the origin.",
               "The intersection of two lines satisfies both equations.",
               "Interpolation is reliable; extrapolation states an assumption."],
        vocab=["gradient", "y-intercept", "rate of change", "linear", "direct proportion",
               "constant of proportionality", "parallel", "intersection", "interpolation",
               "extrapolation", "residual", "model"],
        mixed=[("4.R1", "Find the gradient of the line through (2, 5) and (7, 20)."),
               ("4.R2", "Write the equation of the line through (0, −3) with gradient 4."),
               ("4.R3", "Where do y = 3x − 2 and y = x + 4 meet?"),
               ("4.R4", "Is y directly proportional to x for the pairs (2, 7), (4, 14), (5, 20)?"),
               ("4.R5", "A line has gradient −2 and passes through (3, 1). Find its equation."),
               ("4.R6", "Explain the difference between a gradient and a y-intercept.")],
    ),
    projects=dict(
        service=[("Community need", "Water and food distribution in the community is decided "
                                    "without a shared model, so some households are missed."),
                 ("Mathematical connection", "Linear models, gradients and direct proportion."),
                 ("Proposed action", "Build a proportional allocation model for one shared resource "
                                     "and publish it with its assumptions."),
                 ("Expected impact", "Allocations become predictable and open to challenge."),
                 ("Student reflection", "Record the model, the assumptions, and what happened when "
                                        "it was used.")],
        community=[("Project idea", "A water-allowance model for the school."),
                   ("Need", "The school's water allowance is shared by guesswork."),
                   ("Research question", "What allocation rule is both proportional to need and "
                                         "agreed by everyone?"),
                   ("Mathematics", "Linear functions, direct proportion and graph reading."),
                   ("Action or outcome", "A written allocation rule with a graph of the "
                                         "allocations."),
                   ("Beneficiaries", "Every household or class using the supply."),
                   ("Evidence", "The model, the graph and the agreed rule.")],
        personal=[("Personal interest", "Travel, sport or a savings goal."),
                  ("Learning goal", "To use a linear model to make a personal decision."),
                  ("Product or outcome", "A savings or travel plan with a graph and a prediction."),
                  ("Mathematics", "Gradients, equations of lines and extrapolation."),
                  ("Process", "Collect the data, fit a line, then predict and check."),
                  ("Evidence", "The graph, the model and the prediction.")],
    ),
),
])
