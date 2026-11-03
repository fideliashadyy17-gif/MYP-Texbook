#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Authored editorial framework for the MYP 5 second-edition coursebook.

Content reference: the pre-rewrite MYP 5 chapter and subtopic audit
(``second-edition/audit/chapter-audits/myp5-audit.md`` and the chapter and
subtopic register, restated in ``myp5-register.md``). Chapter scope and teaching order follow that audit; the
teaching sequence, investigations, worked examples, practice sets, assessment
tasks and project connections are author-designed material written for this
second edition.

Every chapter is built as a complete MYP unit from the start: an official global
context with its official exploration, a statement of inquiry that names the key
concept and the related concepts, three question categories derived from the
same elements, an inquiry question opening every investigation, and Criterion
A-D practice written to exercise that unit rather than to repeat a drill.

Year 5 is the extended-leaning level and the transition to DP. The register
records twelve numbered chapters with the modelling capstone embedded as Chapter
11 and no new content in Chapter 12. The register is followed exactly: chapter
scope, section order and the key concept, related concepts, global context and
inquiry statement of every chapter are the audit's own. The teaching sequence,
investigations, worked examples, practice sets, assessment tasks and project
connections are author-designed material written for this second edition, and
nothing is copied from the earlier edition.
"""
import diagrams2

LEVEL = 5
AUTHOR = "SADIKOU MOUKODDIM"

SERIES = dict(
    name="MYP Mathematics",
    line="MYP Mathematics · Student coursebook",
    edition="Second edition",
)

# Five-volume collection. MYP 1 to MYP 4 are produced; MYP 5 is the volume in
# hand, so it is shown as a produced cover rather than a coordinated concept.
COLLECTION = [
    dict(level=1, status="published", theme="Year 1 · number, algebra, shape and data"),
    dict(level=2, status="published", theme="Year 2 · ratio, algebra, geometry, probability"),
    dict(level=3, status="published", theme="Year 3 · proof, models and evidence"),
    dict(level=4, status="published", theme="Year 4 · models, proof and application"),
    dict(level=5, status="this volume", theme="Year 5 · modelling, proof and transition"),
]

PARTS = {
    1: "Part I · Number and abstract reasoning",
    4: "Part I · Number and abstract reasoning",
    2: "Part II · Thinking with models",
    3: "Part II · Thinking with models",
    5: "Part II · Thinking with models",
    6: "Part III · Spatial reasoning",
    7: "Part III · Spatial reasoning",
    8: "Part III · Spatial reasoning",
    9: "Part IV · Reasoning with data",
    10: "Part IV · Reasoning with data",
    11: "Part V · Integrated modelling",
    12: "Part V · Integrated modelling",
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
        ("Logarithm laws", "log(ab) = log a + log b; log(a/b) = log a − log b; log(aᵏ) = k log a."),
        ("Change of base", "log_b a = log a ÷ log b, for any common base."),
        ("Continuous growth", "N = N₀eᵏᵗ; the equivalent base is b = eᵏ and the rate is k = ln b."),
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
        ("Quadratic inequality", "solve the equation, mark the roots on a sign line, then test one interval."),
        ("Inequality rule", "multiplying or dividing by a negative number reverses the sign."),
        ("Function", "a rule giving exactly one output for each input of its domain."),
        ("Composite function", "f(g(x)) applies g first; the inner function acts first."),
        ("Inverse function", "f⁻¹ exists only when f is one-to-one; f⁻¹(f(x)) = x on the restricted domain."),
    ]),
    ("Sequences, series and trigonometry", [
        ("Arithmetic sequence", "the nth term is u(n) = u₁ + (n − 1)d, with common difference d."),
        ("Arithmetic series", "the sum of n terms is S(n) = n/2 (u₁ + u(n)) = n/2 (2u₁ + (n − 1)d)."),
        ("Geometric sequence", "the nth term is u(n) = u₁ rⁿ⁻¹, with common ratio r."),
        ("Geometric series", "the sum of n terms is S(n) = u₁(rⁿ − 1) ÷ (r − 1) for r ≠ 1."),
        ("Convergent geometric series", "the sum to infinity is u₁ ÷ (1 − r) when |r| < 1, and no sum otherwise."),
        ("Annuity", "the accumulated value of equal regular payments, found by summing a geometric series."),
        ("Pythagoras", "a² + b² = c² for the hypotenuse c of a right-angled triangle."),
        ("Trigonometric ratios", "sin θ = opposite/hypotenuse; cos θ = adjacent/hypotenuse; tan θ = opposite/adjacent."),
        ("Sine rule (sides)", "a/sin A = b/sin B = c/sin C."),
        ("Sine rule (angles)", "sin A/a = sin B/b = sin C/c."),
        ("Cosine rule", "a² = b² + c² − 2bc cos A."),
        ("Area of a triangle", "½ab sin C, where C is the angle between sides a and b."),
        ("Ambiguous SSA case", "b sin A < a < b gives two triangles; b sin A = a gives one right triangle; a < b sin A gives none."),
        ("Bearings", "measured clockwise from north, written as three figures."),
        ("Space diagonal", "d = √(l² + w² + h²) for a cuboid of length l, width w and height h."),
        ("Prism", "volume = area of cross-section × length."),
        ("Cylinder", "volume = πr²h; curved surface area = 2πrh."),
        ("Cone", "volume = ⅓πr²h; curved surface area = πrl for slant height l."),
        ("Sphere", "volume = ⁴⁄₃πr³; surface area = 4πr²."),
    ]),
    ("Vectors and matrices", [
        ("Magnitude of a vector", "|a| = √(x² + y²) for a = (x, y)."),
        ("Vector addition", "a + b = (x₁ + x₂, y₁ + y₂)."),
        ("Scalar multiple", "ka = (kx, ky)."),
        ("Position vector", "the vector from the origin to the point."),
        ("Matrix product", "(AB)[[math:_{ij}]] is the dot product of row i of A with column j of B."),
        ("Determinant of a 2 × 2 matrix", "det [[a, b], [c, d]] = ad − bc."),
        ("Inverse of a 2 × 2 matrix", "A⁻¹ = 1/(ad − bc) [[d, −b], [−c, a]], when ad − bc ≠ 0."),
        ("Area scale factor", "|det M| multiplies every area under the transformation M."),
    ]),
    ("Statistics and probability", [
        ("Mean", "x̄ = Σx ÷ n for ungrouped data; for a frequency table use Σfx ÷ Σf."),
        ("Variance (population)", "the mean of Σ(x − x̄)² ÷ n."),
        ("Standard deviation", "the square root of the mean squared deviation; a sample divides by n − 1."),
        ("Grouped estimate", "use the mid-interval value of each class as its representative."),
        ("Interquartile range", "Q3 − Q1, a measure of spread that ignores the extremes."),
        ("Correlation coefficient", "r = Sxy ÷ √(Sxx × Syy), where Sxx = Σ(x − x̄)²."),
        ("Least-squares line", "y = a + bx with b = Sxy ÷ Sxx and a = ȳ − b x̄."),
        ("Coefficient of determination", "r² is the proportion of the variation in y explained by x."),
        ("Probability of an event", "P(event) = favourable outcomes ÷ total equally likely outcomes."),
        ("Addition rule", "P(A or B) = P(A) + P(B) − P(A and B)."),
        ("Conditional probability", "P(A given B) = P(A and B) ÷ P(B)."),
        ("Independence", "P(A and B) = P(A) × P(B), equivalently P(A given B) = P(A)."),
        ("Total probability", "P(B) = the sum, over each part A of a partition of the sample space, of P(A) × P(B given A)."),
        ("Bayes' theorem", "P(A ∣ B) = P(B ∣ A)P(A) ÷ P(B)."),
        ("Multiplication principle", "r successive choices with n₁, n₂, … options give n₁ × n₂ × … outcomes."),
        ("Permutations", "nPr = n! ÷ (n − r)! counts ordered selections."),
        ("Combinations", "nCr = n! ÷ (r!(n − r)!) counts unordered selections."),
        ("Expected value", "E(X) = Σ x P(X = x) for a discrete random variable."),
    ]),

]

# ---------------------------------------------------------------------- glossary
GLOSSARY = [
    ("Algebraic fraction", "A fraction whose numerator and denominator are algebraic expressions.", 1),
    ("Alternate segment theorem", "The angle between a tangent and a chord equals the angle in the alternate segment.", 6),
    ("Ambiguous case", "The SSA arrangement, which can produce zero, one or two triangles depending on the lengths.", 7),
    ("Annuity", "The accumulated value of equal regular payments, found by summing a geometric series.", 4),
    ("Arithmetic sequence", "A sequence with a constant difference between consecutive terms.", 4),
    ("Bearing", "A direction measured clockwise from north, written as three figures.", 7),
    ("Bayes' theorem", "A rule for reversing a conditional probability using the total probability.", 10),
    ("Binomial distribution", "The distribution of the number of successes in a fixed number of independent trials.", 10),
    ("Bisector", "A line that divides an angle or a segment into two equal parts.", 6),
    ("Combination", "An unordered selection; the number of them is n! ÷ (r!(n − r)!).", 10),
    ("Common ratio", "The constant multiplier between consecutive terms of a geometric sequence.", 4),
    ("Complement", "The outcomes not in an event; P(not A) = 1 − P(A).", 10),
    ("Composite function", "The function formed by applying one function to the result of another.", 2),
    ("Conditional probability", "The probability of an event given that another event has occurred.", 10),
    ("Congruent", "Identical in shape and size; for triangles, SSS, SAS, ASA or RHS proves it.", 6),
    ("Conjecture", "A mathematical claim believed to be true but not yet justified.", 12),
    ("Conjugate", "The pair a + √b and a − √b, whose product is rational.", 1),
    ("Continuous growth", "Change modelled by N = N₀eᵏᵗ, where k is the continuous rate.", 3),
    ("Convergent series", "A geometric series whose partial sums approach a finite limit, when |r| < 1.", 4),
    ("Correlation", "The strength and direction of a linear association between two variables.", 9),
    ("Correlation coefficient", "r = Sxy ÷ √(Sxx × Syy), between −1 and 1.", 9),
    ("Cosecant", "The reciprocal of sine: 1 ÷ sin θ.", 7),
    ("Cosine rule", "a² = b² + c² − 2bc cos A, relating three sides and one angle of any triangle.", 7),
    ("Cyclic quadrilateral", "A quadrilateral whose four vertices lie on one circle.", 6),
    ("Dependent events", "Events where the outcome of one changes the probability of the other.", 10),
    ("Depreciation", "A loss of value, modelled by repeated multiplication by a factor below 1.", 4),
    ("Determinant", "The number ad − bc for a 2 × 2 matrix; it is the area scale factor of the transformation.", 8),
    ("Displacement vector", "A vector describing a change of position, with magnitude and direction.", 8),
    ("Dispersion", "How spread out a data set is, measured by range, interquartile range or standard deviation.", 9),
    ("Domain", "The set of permitted inputs of a function.", 2),
    ("Error interval", "The interval of values that would round to a stated value.", 1),
    ("Expected value", "The long-run average of a discrete random variable, Σ x P(X = x).", 10),
    ("Factor theorem", "x − a is a factor of p(x) exactly when p(a) = 0.", 1),
    ("Feasible region", "The set of points satisfying every constraint of a linear programming problem.", 5),
    ("Function", "A rule that gives exactly one output for each permitted input.", 2),
    ("Geometric sequence", "A sequence with a constant ratio between consecutive terms.", 4),
    ("Grouped data", "Data given in class intervals; the mid-interval value represents each class.", 9),
    ("Independent events", "Events where neither changes the probability of the other.", 10),
    ("Index", "The power to which a base is raised; plural indices.", 1),
    ("Interquartile range", "The difference between the upper and lower quartiles.", 9),
    ("Intersection", "The set of outcomes in both of two sets; for events, A and B.", 10),
    ("Inverse function", "The function that undoes another; f⁻¹ exists only when f is one-to-one.", 2),
    ("Least-squares line", "The line y = a + bx that minimises the sum of the squared residuals.", 9),
    ("Linear programming", "Choosing the best value of a linear objective subject to linear constraints.", 5),
    ("Logarithm", "The exponent to which a base must be raised to give a number.", 3),
    ("Magnitude", "The length of a vector, found from its components by Pythagoras.", 8),
    ("Matrix", "A rectangular array of numbers that can represent a transformation of the plane.", 8),
    ("Modulus", "The distance of a complex quantity from the origin; for a vector, its magnitude.", 8),
    ("Multiplication principle", "The number of outcomes of successive independent choices is the product of the counts.", 10),
    ("Mutually exclusive", "Events that cannot both happen, so P(A or B) = P(A) + P(B).", 10),
    ("Permutation", "An ordered arrangement; the number of them is n! ÷ (n − r)!.", 10),
    ("Position vector", "The vector from the origin to a point.", 8),
    ("Quadratic inequality", "An inequality of the form ax² + bx + c > 0, solved with a sign line.", 5),
    ("Range (of a function)", "The set of outputs a function can produce.", 2),
    ("Regression", "Predicting one variable from another using the line of best fit.", 9),
    ("Remainder theorem", "The remainder when p(x) is divided by x − a is p(a).", 1),
    ("Residual", "The difference between an observed value and the value predicted by a model.", 9),
    ("Sample space", "The set of all possible outcomes of an experiment.", 10),
    ("Secant", "A line that cuts a circle in two points.", 6),
    ("Sine rule", "a/sin A = b/sin B = c/sin C, relating sides to opposite angles in any triangle.", 7),
    ("Standard deviation", "The square root of the variance; a measure of spread in the data's units.", 9),
    ("Tangent", "A line that touches a circle in exactly one point, at right angles to the radius.", 6),
    ("Total probability", "the sum, over each part A of a partition of the sample space, of P(A) × P(B given A)", 10),
    ("Transformation matrix", "The matrix whose product with a position vector gives its image.", 8),
    ("Tree diagram", "A branching diagram showing successive outcomes and their probabilities.", 10),
    ("Union", "The set of outcomes in either of two sets; for events, A or B.", 10),
    ("Variance", "The mean of the squared deviations from the mean.", 9),
    ("Vertex", "The turning point of a parabola, written (h, k) in vertex form; also a corner of a feasible region.", 5),
    ("y-intercept", "The value of y where a line crosses the y-axis.", 2),
]


REFERENCES = [
    ("Official IB sources", [
        "IB Middle Years Programme curriculum — https://www.ibo.org/programmes/middle-years-programme/curriculum/ (page states last updated 19 February 2026). Used for: at least 50 hours per subject per year, global contexts, conceptual understanding, approaches to learning and service as action.",
        "IB MYP mathematics subject page — https://www.ibo.org/programmes/middle-years-programme/curriculum/mathematics/ Used for: the four branches of MYP mathematics, standard and extended mathematics, and the inquiry and application focus.",
        "IB MYP projects — https://www.ibo.org/programmes/middle-years-programme/curriculum/myp-projects/ (page states last updated 19 February 2026). Used for: the Community Project completed by students finishing MYP in Year 3 or Year 4, the Personal Project completed by Year 5 students, and the student-centred nature of both.",
        "IB MYP general regulations (2026 assessment procedures) — https://www.ibo.org/globalassets/new-structure/become-an-ib-school/pdfs/myp-2026-general-regulations.pdf Used for: the required use of MYP objectives and assessment criteria, minimum teaching hours, and Year 5 eAssessment eligibility.",
    ]),
    ("Principal content reference", [
        "Pre-rewrite MYP 5 chapter and subtopic audit (second-edition/audit/chapter-audits/myp5-audit.md with the chapter and subtopic register, restated for convenience in second-edition/audit/chapter-audits/myp5-register.md). Used as the principal content reference for chapter scope, section order and the key concepts, related concepts, global contexts and inquiry statements of each chapter. The audit's approved decisions are carried out: the sine-rule ambiguous case is corrected to b sin A < a < b with zero, one and two-triangle cases stated, the raw LaTeX that appeared in the earlier Chapter 11 text is removed, and the Chapter 12 doubling-rate item is corrected to about 9.05 per cent.",
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
        level="5",
        level_text="Student coursebook",
        level_note="MYP 5 · Year 5 · twelve chapters and a modelling capstone in five parts",
        standfirst="A concept-driven inquiry course in algebra, functions, sequences, "
                   "inequalities, geometry, vectors, statistics and probability. You "
                   "investigate, justify and model, then reason, communicate and evaluate "
                   "at the level the transition to DP Mathematics asks of you.",
        topics=["Polynomials, the factor theorem and algebraic fractions",
                "Functions: transformations, composites and inverses",
                "Exponential and logarithmic functions",
                "Sequences and series",
                "Quadratic inequalities and linear programming",
                "Circle geometry and geometric proof",
                "Sine and cosine rules; trigonometry in three dimensions",
                "Vectors and matrices",
                "Statistics: dispersion, correlation and regression",
                "Probability: conditional probability and counting",
                "Capstone: a mathematical modelling project",
                "Cumulative revision and the transition to DP"],
        criteria=[("A", "Knowing and understanding"), ("B", "Investigating patterns"),
                  ("C", "Communicating"), ("D", "Applying mathematics in real-life contexts")],
        inquiry_label="How this book works",
        inquiry="Every chapter opens with a task. You investigate, notice a pattern, state a "
                "mathematical conclusion and justify it before you meet the formal explanation.",
        author=AUTHOR,
        series="MYP Mathematics · Volume 5 of 5",
    ),
    imprint=dict(
        title="About this edition",
        credit="Author",
        author=AUTHOR,
        body=[
            "This is the second edition of the MYP 5 mathematics coursebook. It was rebuilt from the pre-rewrite MYP 5 audit, which recorded the chapter scope, the key and related concepts, the global contexts and the inquiry statements of the earlier edition, and identified where the teaching had to be strengthened.",
            "The edition keeps that chapter scope and the visual identity of the collection, and rebuilds the teaching sequence around inquiry: engagement, inquiry questions, investigation, observation, mathematical conclusion, formal development, worked examples, extensive visual practice, and application, assessment and reflection. The register is followed section by section, so the sine and cosine rules, bearings, matrices and determinants, dispersion and standard deviation, and counting with permutations and combinations are all taught here rather than deferred.",
            "The earlier edition carried four confirmed defects, and all four are repaired in the student text rather than only in the answer key. The sine rule's ambiguous case is corrected: two triangles occur when b sin A < a < b, exactly one when b sin A = a, and none when a < b sin A. The matrix product that the capstone asked students to compute had its order mismatched with the question, and is now consistent. The open-top cylinder problem stated its constraint ambiguously, and now states which dimension is fixed. The raw LaTeX that appeared in the Chapter 11 modelling text is gone; every expression in this book is typeset.",
            "All classroom data sets are simulated and are labelled as such. Real data would require provenance, so no claim in this book rests on unverified statistics.",
            "No publisher, ISBN, print specification or commercial print-readiness claim is made in this file. The book is produced as an A4 review copy: fonts are embedded, pagination is continuous and every page has been checked for overflow.",
        ],
    ),
    howto=dict(
        title="How to use this book",
        intro="Each chapter follows the same sequence, so you always know what is coming next. The "
              "sequence is deliberate: you investigate before you are told the rule, because a rule "
              "you have discovered is a rule you can defend — and defending it is what Year 5 asks "
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
            ("B · Investigating patterns", "Investigate relationships, describe patterns, formulate a conjecture, test it and justify the generalisation — at Year 5 level a justification is a general argument, not a list of cases."),
            ("C · Communicating", "Use correct mathematical language, notation and complete representations, and organise reasoning into a coherent structure that a reader can follow."),
            ("D · Applying mathematics in real-life contexts", "Apply mathematics to authentic situations, identify relevant information, and comment on the accuracy and sense of the result."),
        ],
        notes=[
            "Practice is separated by criterion so that you can see which skill a task is training. Criterion B practice is additional genuine pattern investigation, not a repeat of the teaching.",
            "Visuals are part of the mathematics. Where a task supplies a diagram, grid, table, number line or model, use it; where it asks you to sketch, your drawing is part of the answer.",
            "Answers and student-facing reasoning are collected at the back of the book, with a formula bank, a glossary and references.",
            "Every chapter ends with project connections: a Service as Action opportunity, a Community Project connection and a Personal Project connection for MYP 5.",
            "Chapter 11 is the capstone: a single sustained modelling task that uses mathematics from every part of the year. Chapter 12 adds no new content; it revises what you know and states what the transition to DP Mathematics expects.",
        ],
    ),
    intro=dict(
        title="MYP mathematics and this coursebook",
        paras=[
            "The IB Middle Years Programme asks students to inquire into concepts through global contexts, to develop approaches to learning (ATL) skills, and to act on what they learn through service as action. In mathematics this means more than practising procedures: students investigate patterns, justify generalisations, communicate with precise language and apply mathematics to situations that matter to them.",
            "MYP mathematics is organised into four branches — number, algebra, geometry and trigonometry, and statistics and probability — and the programme recommends at least 50 hours of teaching per subject each year. This coursebook covers the Year 5 content of those branches across twelve chapters, grouped into five parts.",
            "Year 5 is the extended-leaning level and the last year of the programme. The register for this year records the same four branches as every other year, and the chapters here follow the branch recorded for each of them: number and abstract reasoning, thinking with models, spatial reasoning and reasoning with data, with the modelling capstone and the transition to DP Mathematics at the end.",
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
            "Twelve chapters that take polynomials and algebraic fractions, functions and their inverses, exponential and logarithmic models, sequences and series, quadratic inequalities and linear programming, circle theorems and proof, the sine and cosine rules, vectors and matrices, dispersion and regression, and conditional probability and counting from first ideas to justified use. Each chapter opens with a task: you investigate, notice a pattern, state a mathematical conclusion you can defend, and only then meet the formal explanation — with worked examples that model a complete solution and practice separated into Criterion A, B, C and D sets so you can see which skill each task trains.",
            "Year 5 reasoning is applied, not just correct: models are built from stated assumptions, checked against data and evaluated for their limitations, and Criterion B tasks ask you to justify a generalisation rather than to list cases. Every chapter closes with a reflection that returns to the statement of inquiry.",
            "The book closes with a capstone: a sustained modelling task in which a claim about a shared resource becomes defensible only when it is modelled, tested and evaluated — and with a chapter that states plainly what the transition to DP Mathematics expects. Every chapter also closes with a Service as Action opportunity, a Community Project connection and a Personal Project extension. The back of the book carries complete student-facing answers with reasoning, a formula bank, a glossary and references.",
        ],
        collection_heading="MYP Mathematics · the five-volume collection",
        collection_note="One inquiry-led course from Year 1 to Year 5. Volumes 1 to 4 are "
                        "produced and volume 5 is this volume. The covers shown here are the "
                        "coordinated collection designs for the whole set.",
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
    num=1, title="Polynomials, Factor Theorem and Algebraic Fractions",
    key="Form", related=["Equivalence", "Generalisation", "Simplification"],
    context="Personal and cultural expression",
    exploration="the language of algebra as a way of making structure visible",
    inquiry=("The structure of a polynomial — its factors, roots and remainders — determines "
             "both what it can be simplified to and what its graph will do."),
    atl=("Critical thinking",
         "In order for a student to choose the most useful form of an algebraic expression, "
         "students must compare an expanded form with a factorised form of the same polynomial, "
         "identify what each form reveals, and justify the choice of form for a stated purpose."),
    standfirst="A polynomial can be written as a sum of powers or as a product of factors. Each "
               "form is the same polynomial, and each makes a different question easy.",
    engage="Two students are asked to describe x³ − 7x − 6. One writes it as a sum of three "
           "terms; the other writes (x − 3)(x + 1)(x + 2). Neither has changed the polynomial. "
           "Which description tells you where the graph crosses the x-axis, and which tells you "
           "how steep it is?",
    questions=[("Factual", "What is the degree of a polynomial, and what do the remainder and "
                           "factor theorems say?"),
               ("Conceptual", "Why does the factored form of a polynomial reveal its roots, and "
                              "what does an excluded value protect a simplification from?"),
               ("Debatable", "When a calculation produces a solution that the original equation "
                             "rejects, has the method failed, or has it done its job?")],
    application_lede="These tasks use polynomial division, the factor theorem, algebraic "
                     "fractions and rational equations. State the excluded values before you "
                     "cancel anything, and check every solution in the original equation.",
    projects_lede="Algebra is a language for making structure visible. Choose the form that "
                  "shows the structure you need, and say what the choice costs.",
    sections=[
        dict(id="1.1", title="Polynomials and their behaviour",
             inquiry_q="What can be read off a polynomial from the form it is written in?",
             teach=[
                 "A polynomial in x is a sum of terms of the form axⁿ where a is a real coefficient and n is a non-negative integer. The degree is the highest power present, and the leading coefficient is the coefficient of that power. The two numbers together describe how the polynomial behaves for very large and very small x.",
                 "Polynomials are closed under addition, subtraction and multiplication: performing any of these on two polynomials gives another polynomial. Division is the exception, which is why division is the operation that needs its own technique.",
                 "Two polynomials are equal when their corresponding coefficients are equal, not when they look alike. Expanding (x + 1)(x + 2) gives x² + 3x + 2, and the two forms name the same function. Equivalence of form is the idea that makes factorising useful, and the generalisation behind it — that any polynomial can be rewritten in any equivalent form — is what makes algebra a language rather than a set of tricks.",
                 "The standard form of a polynomial lists its terms in descending powers with a single coefficient for each power. Rewriting into standard form is the first step in almost every polynomial calculation, because it makes the degree and the leading coefficient visible.",
             ], examples=[
                 dict(q="Write 3 − 2x⁴ + x² in standard form, state its degree and leading "
                        "coefficient, and find its value at x = −1.",
                      vis=F("table", [["form", "polynomial", "what it shows"],
                                      ["as given", "3 − 2x⁴ + x²", "no obvious order"],
                                      ["standard", "−2x⁴ + x² + 3", "degree 4, leading −2"],
                                      ["at x = −1", "−2(1) + 1 + 3", "value 2"]],
                            caption="Standard form puts the degree and the leading coefficient on view."),
                      reasoning="Standard form orders the terms by descending power, and the "
                               "degree and leading coefficient are read directly from it.",
                      steps=["Reorder: −2x⁴ + x² + 3.",
                             "The highest power is 4, so the degree is 4.",
                             "The leading coefficient is −2.",
                             "Substitute x = −1: −2(−1)⁴ + (−1)² + 3 = −2 + 1 + 3.",
                             "The value is 2."],
                      ans="−2x⁴ + x² + 3, degree 4, leading coefficient −2, value 2 at x = −1",
                      interp="Standard form is not cosmetic: it is the form in which the two "
                             "numbers that govern the polynomial's behaviour can be read off."),
                 dict(q="Show that the product of two polynomials is always a polynomial, and "
                        "explain why the degree of the product is the sum of the degrees.",
                      vis=F("table", [["factor", "degree", "contribution"],
                                      ["3x² − 1", "2", "two powers of x"],
                                      ["x³ + 5x", "3", "three powers of x"],
                                      ["product", "5", "2 + 3"]],
                            caption="Multiplying adds the powers, so the degrees add."),
                      reasoning="Each term of the first polynomial multiplies each term of the "
                               "second, and every product is again a constant times a power of x.",
                      steps=["Let the polynomials be p and q with degrees m and n.",
                             "Every term of p is a constant times x raised to a power "
                             "i with i at most m, and every term of q is a constant times "
                             "x raised to a power j with j at most n.",
                             "A product term is the product of the two constants times x "
                             "raised to i + j, and i + j is at most m + n.",
                             "The two leading terms multiply to give a non-zero constant "
                             "times x raised to m + n, so the degree of the product is "
                             "exactly m + n.",
                             "Hence the product is a polynomial of degree m + n."],
                      ans="the product is a polynomial of degree m + n",
                      interp="One general argument settles every pair of polynomials, which is "
                             "why an algebraic proof is worth more than a list of examples."),
             ], inv=dict(
                 task="Take four polynomials of your own: one of degree 1, one of degree 2, one "
                      "of degree 3 and one you are unsure about. Add and multiply each pair, "
                      "record the degree of each result, and then try to state a rule that "
                      "predicts the degree of the answer before you calculate it.",
                 table=[["first", "degree", "second", "degree", "operation", "result degree"],
                        ["2x + 1", "1", "x² − 3", "2", "add", "2"],
                        ["2x + 1", "1", "x² − 3", "2", "multiply", "3"],
                        ["x³ + x", "3", "x − 1", "1", "add", "3"],
                        ["x³ + x", "3", "x − 1", "1", "multiply", "4"],
                        ["x² + 1", "2", "x² − 1", "2", "multiply", "4"],
                        ["5", "0", "x⁴ + x", "4", "multiply", "4"]],
                 notice=["Adding two polynomials gave the larger of the two degrees, unless the "
                         "leading terms cancelled.",
                         "Multiplying two polynomials always gave the sum of the two degrees.",
                         "A constant has degree 0 and left every degree unchanged when it was "
                         "multiplied in.",
                         "The only surprise came from addition, where cancellation can lower the "
                         "degree."],
                 obs="The degree of a product is the sum of the degrees, and the degree of a sum "
                     "is at most the larger of the two degrees.",
                 concl="The polynomials are closed under addition, subtraction and "
                       "multiplication, and multiplication of degrees is exact: the degree of a "
                       "product is the sum of the degrees of the factors. This is why a "
                       "factorised form shows the roots while an expanded form shows the "
                       "degree.")),
        dict(id="1.2", title="Dividing polynomials",
             inquiry_q="How is one polynomial divided by another, and how is the answer checked?",
             teach=[
                 "Polynomial long division follows the same logic as long division of numbers: match the leading term of the divisor to the leading term of the dividend, write the quotient term, subtract, and repeat on what is left.",
                 "The division identity is dividend = divisor × quotient + remainder, with the remainder either zero or of lower degree than the divisor. This identity is not a convention; it is the statement that the division has been done correctly.",
                 "A missing power in the dividend must be kept as a zero placeholder. Dividing x³ + 1 by x² + 1 requires a 0x term, and omitting it is the commonest source of error.",
                 "Synthetic division is a compressed arrangement of the same process for a divisor of the form x − a. It is faster but it hides the reasoning, so the long division is used first and the short form afterwards.",
             ], examples=[
                 dict(q="Divide 2x³ + 3x² − x + 5 by x + 2, and check the answer.",
                      vis=F("table", [["step", "working", "remainder"],
                                      ["lead", "2x³ ÷ x = 2x²", "2x³ + 4x²"],
                                      ["subtract", "(2x³ + 3x²) − (2x³ + 4x²)", "−x²"],
                                      ["next", "−x² ÷ x = −x", "−x² − 2x"],
                                      ["subtract", "(−x² − x) − (−x² − 2x)", "x"],
                                      ["last", "x ÷ x = 1", "x + 2"],
                                      ["subtract", "(x + 5) − (x + 2)", "3"]],
                            caption="Each step matches the leading term and subtracts."),
                      reasoning="Match leading terms, subtract, and repeat until what is left has "
                               "lower degree than the divisor; then verify with the division "
                               "identity.",
                      steps=["2x³ ÷ x = 2x². Multiply x + 2 by 2x² to get 2x³ + 4x² and "
                             "subtract: (2x³ + 3x²) − (2x³ + 4x²) = −x².",
                             "Bring down −x. Now −x² ÷ x = −x. Multiply x + 2 by −x to get "
                             "−x² − 2x and subtract: (−x² − x) − (−x² − 2x) = x.",
                             "Bring down +5. Now x ÷ x = 1. Multiply x + 2 by 1 and subtract: "
                             "(x + 5) − (x + 2) = 3.",
                             "The quotient is 2x² − x + 1 and the remainder is 3.",
                             "Check: (x + 2)(2x² − x + 1) + 3 = 2x³ − x² + x + 4x² − 2x + 2 + 3 "
                             "= 2x³ + 3x² − x + 5."],
                      ans="quotient 2x² − x + 1, remainder 3",
                      interp="The division identity is the check: if the reconstruction gives "
                             "back the dividend, the division was correct."),
                 dict(q="Divide x³ + 8 by x² + 2x + 1, keeping every placeholder.",
                      vis=F("table", [["dividend terms", "x³", "0x²", "0x", "8"],
                                      ["divisor", "x²", "+2x", "+1", "—"],
                                      ["quotient", "x", "−2", "—", "—"],
                                      ["remainder", "0", "3x", "+10", "—"]],
                            caption="The zero placeholder keeps the powers aligned."),
                      reasoning="A missing power is a zero term, and writing it keeps the "
                               "subtraction aligned.",
                      steps=["Write the dividend as x³ + 0x² + 0x + 8.",
                             "x³ ÷ x² = x. Subtract x(x² + 2x + 1) = x³ + 2x² + x to get "
                             "−2x² − x + 8.",
                             "−2x² ÷ x² = −2. Subtract −2(x² + 2x + 1) = −2x² − 4x − 2 to get "
                             "3x + 10.",
                             "3x has degree 1, below the divisor's degree 2, so the division "
                             "stops.",
                             "Quotient x − 2, remainder 3x + 10. Check: (x² + 2x + 1)(x − 2) + "
                             "3x + 10 = x³ + 2x² + x − 2x² − 4x − 2 + 3x + 10 = x³ + 8."],
                      ans="quotient x − 2, remainder 3x + 10",
                      interp="Zero placeholders are not decoration: without them the powers "
                             "drift and the subtraction goes wrong."),
             ], inv=dict(
                 task="Divide x⁴ − 1 by x − 1, then x⁴ − 1 by x + 1, then x⁴ − 1 by x² + 1. "
                      "Record each quotient and remainder, reconstruct the dividend from your "
                      "answers, and then explain what the three divisions have in common.",
                 table=[["divisor", "quotient", "remainder", "reconstruction"],
                        ["x − 1", "x³ + x² + x + 1", "0", "(x − 1)(x³ + x² + x + 1) = x⁴ − 1"],
                        ["x + 1", "x³ − x² + x − 1", "0", "(x + 1)(x³ − x² + x − 1) = x⁴ − 1"],
                        ["x² + 1", "x² − 1", "0", "(x² + 1)(x² − 1) = x⁴ − 1"],
                        ["x² − 1", "x² + 1", "0", "(x² − 1)(x² + 1) = x⁴ − 1"],
                        ["x − 2", "x³ + 2x² + 4x + 8", "15", "(x − 2)(…) + 15 = x⁴ − 1"],
                        ["x + 2", "x³ − 2x² + 4x − 8", "17", "(x + 2)(…) + 17 = x⁴ − 1"]],
                 notice=["Three of the six divisors divided x⁴ − 1 exactly, leaving no remainder.",
                         "The two divisors that left a remainder were not factors of x⁴ − 1.",
                         "Every reconstruction reproduced the dividend, which is the check that "
                         "each division was done correctly.",
                         "The divisors that worked were all built from the factors of x⁴ − 1."],
                 obs="A divisor that leaves no remainder is a factor, and the quotient is the "
                     "other factor.",
                 concl="Dividing p(x) by x − a leaves remainder zero exactly when x − a is a "
                       "factor of p(x). The reconstruction dividend = divisor × quotient + "
                       "remainder is the check on every division.")),
        dict(id="1.3", title="The remainder and factor theorems",
             inquiry_q="What does the remainder of a division tell you about the polynomial?",
             teach=[
                 "The remainder theorem states that when p(x) is divided by x − a, the remainder is p(a). Evaluating the polynomial at a single number replaces the whole division.",
                 "The factor theorem is the special case: x − a is a factor of p(x) exactly when p(a) = 0. So a is a root of the polynomial exactly when x − a divides it exactly. This is the generalisation that turns a search for roots into a search for factors.",
                 "A polynomial of degree n has at most n real roots, and if it has n distinct roots then it has exactly n linear factors. Counting roots therefore counts factors, which is how a cubic is factorised completely.",
                 "The theorems work together: find one root by inspection, divide out the corresponding factor, and the quotient is a polynomial of one degree lower, which is easier to solve. This is the standard route to solving a cubic or quartic.",
             ], examples=[
                 dict(q="Find the remainder when p(x) = x³ − 4x² + 5x − 7 is divided by x − 2, "
                        "and hence decide whether x − 2 is a factor.",
                      vis=F("table", [["a", "p(a)", "remainder on dividing by x − a", "factor?"],
                                      ["1", "−5", "−5", "no"],
                                      ["2", "−5", "−5", "no"],
                                      ["3", "−1", "−1", "no"],
                                      ["−1", "−17", "−17", "no"]],
                            caption="The remainder is the value of the polynomial at a."),
                      reasoning="By the remainder theorem the remainder is p(a), so evaluate "
                               "rather than divide.",
                      steps=["The divisor is x − 2, so a = 2.",
                             "p(2) = 2³ − 4(2²) + 5(2) − 7 = 8 − 16 + 10 − 7.",
                             "8 − 16 = −8, −8 + 10 = 2, 2 − 7 = −5.",
                             "The remainder is −5.",
                             "Since p(2) ≠ 0, x − 2 is not a factor of p(x)."],
                      ans="remainder −5, so x − 2 is not a factor",
                      interp="One substitution answers a question that would otherwise need a "
                             "whole division, and the same substitution also tests whether the "
                             "divisor is a factor."),
                 dict(q="Show that x − 1 is a factor of p(x) = x³ − 6x² + 11x − 6, find the "
                        "other factors, and hence solve p(x) = 0.",
                      vis=F("table", [["x", "p(x)", "comment"],
                                      ["0", "−6", "negative"],
                                      ["1", "0", "root, so x − 1 is a factor"],
                                      ["2", "0", "root, so x − 2 is a factor"],
                                      ["3", "0", "root, so x − 3 is a factor"]],
                            caption="Three roots for a cubic means three linear factors."),
                      reasoning="Find one root, divide out its factor, then solve the quadratic "
                               "that is left.",
                      steps=["p(1) = 1 − 6 + 11 − 6 = 0, so x − 1 is a factor.",
                             "Divide p(x) by x − 1: the quotient is x² − 5x + 6.",
                             "Check: (x − 1)(x² − 5x + 6) = x³ − 6x² + 11x − 6.",
                             "Factorise the quadratic: x² − 5x + 6 = (x − 2)(x − 3).",
                             "So p(x) = (x − 1)(x − 2)(x − 3), and the roots are x = 1, 2 and 3."],
                      ans="p(x) = (x − 1)(x − 2)(x − 3); roots x = 1, 2, 3",
                      interp="The factor theorem turns a cubic into a quadratic, and a quadratic "
                             "is already solved."),
             ], inv=dict(
                 task="Take the polynomial p(x) = x³ + 2x² − 5x − 6. Evaluate p at x = −3, −2, "
                      "−1, 0, 1, 2 and 3, record which values are zero, divide out one factor "
                      "you have found, and then factorise p completely. State how many roots a "
                      "cubic can have and how many you found.",
                 table=[["x", "p(x)", "zero?", "factor found"],
                        ["−3", "0", "yes", "x + 3"],
                        ["−2", "4", "no", "—"],
                        ["−1", "2", "no", "—"],
                        ["0", "−6", "no", "—"],
                        ["1", "−8", "no", "—"],
                        ["2", "0", "yes", "x − 2"],
                        ["3", "24", "no", "—"]],
                 notice=["Two of the seven values of x made p(x) exactly zero.",
                         "Those two values gave the two factors x + 3 and x − 2.",
                         "A cubic has at most three roots, so one root was still missing.",
                         "Dividing by one factor lowered the degree, making the rest easier."],
                 obs="A root of the polynomial is a value that makes it zero, and each root "
                     "gives a linear factor.",
                 concl="The factor theorem is a generalisation: p(a) = 0 exactly when x − a is a "
                       "factor of p(x), for every polynomial p and every number a. Finding "
                       "roots and factorising are therefore the same activity. A cubic has "
                       "at most three roots, and here p(x) = (x + 3)(x − 2)(x + 1) with "
                       "roots −3, −1 and 2.")),
        dict(id="1.4", title="Algebraic fractions",
             inquiry_q="When may an algebraic fraction be cancelled, and what must be stated first?",
             teach=[
                 "An algebraic fraction is cancelled by dividing the numerator and the denominator by a common factor. Cancelling a common term is not cancellation: (x + 3)/x does not become 3, because x is not a factor of x + 3.",
                 "Before any cancellation, the values that make the denominator zero must be excluded. The fraction (x² − 1)/(x − 1) simplifies to x + 1 only for x ≠ 1, and the excluded value is part of the answer, not a footnote.",
                 "Multiplying fractions multiplies numerators and denominators; adding them requires a common denominator. The two operations are not interchangeable, and the commonest error is to add numerators and denominators separately.",
                 "Simplifying a complex fraction means simplifying the numerator and the denominator first, then dividing. The division is multiplication by the reciprocal, and the reciprocal of a sum is not the sum of the reciprocals.",
             ], examples=[
                 dict(q="Simplify (x² − 5x + 6)/(x² − 4), stating the excluded values.",
                      vis=F("table", [["expression", "factorised", "cancelled", "left"],
                                      ["numerator", "(x − 2)(x − 3)", "÷ (x − 2)", "x − 3"],
                                      ["denominator", "(x − 2)(x + 2)", "÷ (x − 2)", "x + 2"],
                                      ["excluded", "x = 2 and x = −2", "—", "x ≠ 2, −2"]],
                            caption="Cancel common factors, and state what was cancelled away."),
                      reasoning="Factorise both parts, cancel the common factor, and record the "
                               "values that made the cancelled factor zero.",
                      steps=["Factorise: x² − 5x + 6 = (x − 2)(x − 3) and x² − 4 = (x − 2)(x + 2).",
                             "The denominator is zero when x = 2 or x = −2, so both are "
                             "excluded.",
                             "Cancel the common factor x − 2: the fraction becomes (x − 3)/(x + 2).",
                             "State the result as (x − 3)/(x + 2) for x ≠ 2 and x ≠ −2."],
                      ans="(x − 3)/(x + 2), for x ≠ 2 and x ≠ −2",
                      interp="The excluded values are the values the cancellation removed, and "
                             "stating them is what makes the simplification honest."),
                 dict(q="Simplify 2/(x + 1) + 3/(x − 1) as a single fraction.",
                      vis=F("table", [["fraction", "× (x − 1)", "× (x + 1)", "combined"],
                                      ["2/(x + 1)", "2(x − 1)", "2(x − 1)", "2x − 2"],
                                      ["3/(x − 1)", "3(x + 1)", "3(x + 1)", "3x + 3"],
                                      ["sum", "—", "—", "(5x + 1)/(x² − 1)"]],
                            caption="A common denominator, then add the numerators."),
                      reasoning="Build a common denominator by multiplying each fraction by the "
                               "missing factor, then add.",
                      steps=["The common denominator is (x + 1)(x − 1) = x² − 1.",
                             "2/(x + 1) = 2(x − 1)/(x² − 1) = (2x − 2)/(x² − 1).",
                             "3/(x − 1) = 3(x + 1)/(x² − 1) = (3x + 3)/(x² − 1).",
                             "Add: (2x − 2 + 3x + 3)/(x² − 1) = (5x + 1)/(x² − 1).",
                             "The excluded values are x = 1 and x = −1."],
                      ans="(5x + 1)/(x² − 1), for x ≠ 1 and x ≠ −1",
                      interp="Adding fractions is never adding numerators and denominators: it "
                             "is rewriting both over a common denominator first."),
             ], inv=dict(
                 task="Take the four expressions (x² − 9)/(x − 3), (x − 3)/(x² − 9), "
                      "1/(x + 3) + 1/(x − 3) and (x + 3 + x − 3)/(x + 3). Simplify each, state "
                      "the excluded values, and then explain why two of them give the same "
                      "answer and one of them cannot be simplified at all.",
                 table=[["expression", "simplified", "excluded values", "same as"],
                        ["(x² − 9)/(x − 3)", "x + 3", "x ≠ 3", "—"],
                        ["(x − 3)/(x² − 9)", "1/(x + 3)", "x ≠ 3, −3", "third row, left"],
                        ["1/(x + 3) + 1/(x − 3)", "2x/(x² − 9)", "x ≠ 3, −3", "—"],
                        ["(x + 3 + x − 3)/(x + 3)", "2x/(x + 3)", "x ≠ −3", "—"]],
                 notice=["Two of the four simplified to expressions with the same denominator.",
                         "The reciprocal of a simplified fraction is the fraction with numerator "
                         "and denominator swapped.",
                         "The last expression could not be cancelled at all, because x + 3 is "
                         "not a factor of 2x.",
                         "Every excluded value came from a factor of a denominator."],
                 obs="Cancellation needs a common factor; without one, the fraction is already "
                     "in its simplest form.",
                 concl="An algebraic fraction is simplified by cancelling common factors and "
                       "nothing else, and the excluded values are exactly the values that made "
                       "the cancelled factors zero. Stating them is part of the answer.")),
        dict(id="1.5", title="Rational equations and applications",
             inquiry_q="Why can solving a rational equation produce an answer the equation rejects?",
             teach=[
                 "A rational equation is solved by multiplying both sides by a common denominator to clear the fractions. The multiplication is only valid for values that do not make that denominator zero.",
                 "A solution produced by this method must be substituted back into the original equation. If it makes a denominator zero, it is extraneous: it belongs to the cleared equation but not to the original one.",
                 "Applications fall into two families: rate problems, where the rates add, and work problems, where the times add reciprocally. In both, the equation is built from the meaning of the quantities, not from a pattern.",
                 "Every application ends with a check for sense. A negative time, a fraction of a person or a speed that exceeds the stated limit are all signals that the model or the algebra needs revisiting.",
             ], examples=[
                 dict(q="Solve (x + 1)/(x − 2) = 3, and check for extraneous solutions.",
                      vis=F("table", [["step", "working", "note"],
                                      ["clear", "(x + 1) = 3(x − 2)", "multiply by x − 2"],
                                      ["expand", "x + 1 = 3x − 6", "—"],
                                      ["collect", "7 = 2x", "—"],
                                      ["solve", "x = 3.5", "candidate"],
                                      ["check", "denominator x − 2 = 1.5 ≠ 0", "accepted"]],
                            caption="Clear the fractions, solve, then check the candidate."),
                      reasoning="Multiply by the denominator, solve the resulting linear "
                               "equation, then test the candidate in the original equation.",
                      steps=["The denominator is zero when x = 2, so x ≠ 2.",
                             "Multiply both sides by x − 2: x + 1 = 3(x − 2).",
                             "Expand: x + 1 = 3x − 6, so 7 = 2x and x = 3.5.",
                             "Check: x − 2 = 1.5, which is not zero, so the solution is valid.",
                             "Verify in the original: (3.5 + 1)/(3.5 − 2) = 4.5/1.5 = 3."],
                      ans="x = 3.5, valid",
                      interp="The check is not a formality: it is the step that separates a "
                             "solution of the original equation from a solution of the cleared "
                             "one."),
                 dict(q="Two pipes fill a tank in 4 hours and 6 hours respectively. Working "
                        "together, how long do they take?",
                      vis=F("table", [["pipe", "time (h)", "rate (tanks per hour)"],
                                      ["first", "4", "1/4"],
                                      ["second", "6", "1/6"],
                                      ["together", "t", "1/4 + 1/6 = 5/12"],
                                      ["answer", "12/5 = 2.4", "—"]],
                            caption="Rates add; times do not."),
                      reasoning="Rates add, so the combined rate is the sum of the individual "
                               "rates, and the time is its reciprocal.",
                      steps=["The first pipe fills 1/4 of the tank per hour and the second 1/6.",
                             "Together they fill 1/4 + 1/6 = 3/12 + 2/12 = 5/12 per hour.",
                             "If the time is t hours, then (5/12)t = 1.",
                             "So t = 12/5 = 2.4 hours.",
                             "Check: 2.4/4 + 2.4/6 = 0.6 + 0.4 = 1 tank."],
                      ans="2.4 hours, that is 2 hours 24 minutes",
                      interp="Adding the times would give 10 hours, which is longer than either "
                             "pipe alone and is obviously wrong: rates add, times do not."),
             ], inv=dict(
                 task="Solve (2)/(x) + (3)/(x + 1) = 1. Before you clear the fractions, write "
                      "down the values x may not take. Solve, then substitute every candidate "
                      "back into the original equation and say which are genuine and which are "
                      "extraneous.",
                 table=[["step", "working", "result"],
                        ["excluded", "x ≠ 0 and x ≠ −1", "—"],
                        ["clear", "2(x + 1) + 3x = x(x + 1)", "—"],
                        ["expand", "5x + 2 = x² + x", "—"],
                        ["rearrange", "x² − 4x − 2 = 0", "—"],
                        ["solve", "x = 2 ± √6", "2 + √6 ≈ 4.45, 2 − √6 ≈ −0.45"],
                        ["check first", "2/4.45 + 3/5.45 ≈ 0.449 + 0.550", "≈ 0.999"],
                        ["check second", "2/(−0.45) + 3/0.55 ≈ −4.44 + 5.45", "≈ 1.01"]],
                 notice=["Both candidates were allowed, because neither is 0 nor −1.",
                         "Both candidates satisfied the original equation when substituted.",
                         "The equation became a quadratic after clearing, so two answers were "
                         "possible.",
                         "Had a candidate been 0 or −1, it would have been extraneous."],
                 obs="Clearing the fractions can introduce candidates that the original "
                     "equation rejects, and only substitution finds them.",
                 concl="A rational equation is solved by clearing the fractions, but every "
                       "candidate must be tested in the original equation: a value that makes "
                       "a denominator zero is extraneous and is discarded.")),
        dict(id="1.6", title="Investigation: factors, roots and sign",
             inquiry_q="How does the factored form of a polynomial decide where it is positive?",
             teach=[
                 "The sign of a polynomial between its roots is constant, because a polynomial can change sign only by passing through zero. This is why a sign line is a complete method for solving a polynomial inequality.",
                 "For a product of factors, the sign is decided by counting the negative factors. Each simple factor changes sign as x passes its root; a factor with an even power does not.",
                 "Solving p(x) > 0 means finding the intervals on which the count of negative factors is even. The roots themselves are excluded when the inequality is strict.",
                 "A sketch of the graph confirms the algebraic answer: the curve crosses the axis at a simple root and touches it at a double root, and the sign pattern follows the crossing behaviour.",
             ], examples=[
                 dict(q="Solve (x − 1)(x + 2)(x − 4) > 0.",
                      vis=F("table", [["interval", "x − 1", "x + 2", "x − 4", "product"],
                                      ["x < −2", "−", "−", "−", "−"],
                                      ["−2 < x < 1", "−", "+", "−", "+"],
                                      ["1 < x < 4", "+", "+", "−", "−"],
                                      ["x > 4", "+", "+", "+", "+"]],
                            caption="Three simple roots give four sign intervals."),
                      reasoning="Mark the roots on a sign line, test one value in each interval, "
                               "and read off where the product is positive.",
                      steps=["The roots are x = −2, 1 and 4, and they divide the line into four "
                             "intervals.",
                             "For x < −2: all three factors are negative, so the product is "
                             "negative.",
                             "For −2 < x < 1: only x + 2 is positive, so the product is "
                             "positive.",
                             "For 1 < x < 4: only x − 4 is negative, so the product is "
                             "negative.",
                             "For x > 4: all three are positive, so the product is positive.",
                             "The solution is −2 < x < 1 or x > 4, with the roots excluded."],
                      ans="−2 < x < 1 or x > 4",
                      interp="One sign line settles every polynomial inequality, however many "
                             "factors there are."),
                 dict(q="Solve (x + 1)²(x − 3) ≥ 0, and explain the difference from the "
                        "previous example.",
                      vis=F("table", [["x", "x + 1", "(x + 1)²", "x − 3", "product"],
                                      ["−2", "−1", "1", "−5", "−5"],
                                      ["−1", "0", "0", "−4", "0"],
                                      ["0", "1", "1", "−3", "−3"],
                                      ["3", "4", "16", "0", "0"],
                                      ["4", "5", "25", "1", "25"]],
                            caption="A squared factor never changes sign."),
                      reasoning="A squared factor is never negative, so only the simple factor "
                               "decides the sign, and the double root is included when the "
                               "inequality is not strict.",
                      steps=["(x + 1)² ≥ 0 for every x, and it is zero only at x = −1.",
                             "So the sign of the product is the sign of x − 3, except at "
                             "x = −1 where the product is zero.",
                             "For x > 3 the product is positive; for x < 3 it is negative.",
                             "At x = 3 the product is zero, and at x = −1 it is also zero.",
                             "The solution of ≥ 0 is x = −1 or x ≥ 3."],
                      ans="x = −1 or x ≥ 3",
                      interp="An even power does not change sign at its root, so the graph "
                             "touches the axis instead of crossing it, and that root is "
                             "included."),
             ], inv=dict(
                 task="Take p(x) = (x + 3)(x − 1)²(x − 5). Draw a sign line, test one value in "
                      "each interval, and solve p(x) > 0 and p(x) ≤ 0. Then sketch the graph "
                      "from the factored form and mark which roots are crossings and which are "
                      "touchings.",
                 table=[["interval", "x + 3", "(x − 1)²", "x − 5", "product"],
                        ["x < −3", "−", "+", "−", "+"],
                        ["−3 < x < 1", "+", "+", "−", "−"],
                        ["1 < x < 5", "+", "+", "−", "−"],
                        ["x > 5", "+", "+", "+", "+"]],
                 notice=["The squared factor was positive in every interval, so it never "
                         "changed the sign.",
                         "The sign changed at x = −3 and at x = 5, both simple roots.",
                         "The sign did not change at x = 1, the double root.",
                         "The product was negative on two separate intervals that met at "
                         "x = 1."],
                 obs="Only simple factors change sign; a factor with an even power leaves the "
                     "sign unchanged.",
                 concl="The factored form of a polynomial decides its sign completely: mark "
                       "the roots, count the negative factors in each interval, and the "
                       "inequality is solved. A double root is a touching point and is "
                       "included when the inequality is not strict. Here p(x) > 0 gives x < −3 "
                       "or x > 5, and p(x) ≤ 0 gives −3 ≤ x ≤ 5 with x = 1 included.")),
        dict(id="1.7", title="Mixed practice",
             inquiry_q="Which form of each expression makes the next step easiest?",
             teach=[
                 "Choosing a form is a skill in itself. Before calculating, decide whether the expanded form, the factored form or the single-fraction form will answer the question with the least work.",
                 "The four tools of this chapter — long division, the remainder theorem, the factor theorem and cancellation of common factors — are selected by the shape of the question. A single evaluation calls for the remainder theorem; a complete factorisation calls for division.",
                 "Every rational equation ends with a substitution check, and every simplification ends with a statement of excluded values. These two habits are what separate a correct method from a correct answer.",
                 "Mixed practice is where the tools are chosen rather than given, so the reasoning behind the choice is part of what is being practised.",
             ], examples=[
                 dict(q="Solve (x² − 9)/(x² + 4x + 3) = 1.",
                      vis=F("table", [["expression", "factorised", "cancelled?"],
                                      ["numerator", "(x − 3)(x + 3)", "x + 3"],
                                      ["denominator", "(x + 1)(x + 3)", "x + 3"],
                                      ["excluded", "x ≠ −1 and x ≠ −3", "—"]],
                            caption="Factorise both parts before clearing the fractions."),
                      reasoning="Simplify the fraction first, then clear the denominator and "
                               "check the candidates.",
                      steps=["Factorise: (x − 3)(x + 3)/((x + 1)(x + 3)).",
                             "Exclude x = −1 and x = −3, then cancel x + 3 to get (x − 3)/(x + 1).",
                             "The equation becomes (x − 3)/(x + 1) = 1, so x − 3 = x + 1.",
                             "This gives −3 = 1, which is false, so there is no solution.",
                             "Note that x = −3 would have made the original denominator zero, so "
                             "it is excluded anyway."],
                      ans="no solution",
                      interp="An equation can be consistent and still have no solution, and "
                             "recognising that is part of solving it."),
                 dict(q="The polynomial p(x) = x³ + ax² + bx − 12 has x − 2 as a factor and "
                        "leaves remainder 8 when divided by x − 1. Find a and b.",
                      vis=F("table", [["condition", "equation"],
                                      ["x − 2 is a factor, so p(2) = 0", "8 + 4a + 2b − 12 = 0"],
                                      ["remainder 8 on dividing by x − 1, so p(1) = 8",
                                       "1 + a + b − 12 = 8"],
                                      ["simplified", "2a + b = 2 and a + b = 19"]],
                            caption="Two conditions give two equations in a and b."),
                      reasoning="Each condition is a value of the polynomial, and two values "
                               "give two linear equations.",
                      steps=["Since x − 2 is a factor, p(2) = 0: 8 + 4a + 2b − 12 = 0, so "
                             "4a + 2b = 4 and 2a + b = 2.",
                             "Since the remainder on dividing by x − 1 is 8, p(1) = 8: "
                             "1 + a + b − 12 = 8, so a + b = 19.",
                             "Subtract: (2a + b) − (a + b) = 2 − 19, so a = −17.",
                             "Then b = 19 − a = 36.",
                             "Check: p(2) = 8 + 4(−17) + 72 − 12 = 8 − 68 + 72 − 12 = 0."],
                      ans="a = −17 and b = 36",
                      interp="The remainder theorem turns two statements about division into "
                             "two equations, and the rest is simultaneous linear algebra."),
             ], inv=dict(
                 task="Choose a method for each of these four tasks and carry it out: divide "
                      "x⁴ − 16 by x² − 4; find the remainder when x⁴ − 16 is divided by x − 3; "
                      "simplify (x⁴ − 16)/(x² − 4); and solve (x⁴ − 16)/(x² − 4) = 5. For each, "
                      "write down which tool you used and why.",
                 table=[["task", "tool used", "answer", "why that tool"],
                        ["divide x⁴ − 16 by x² − 4", "long division", "x² + 4, remainder 0",
                         "a complete quotient is needed"],
                        ["remainder on dividing by x − 3", "remainder theorem", "65",
                         "only one value is needed"],
                        ["simplify (x⁴ − 16)/(x² − 4)", "cancel common factors", "x² + 4",
                         "the numerator and denominator are already factored"],
                        ["solve (x⁴ − 16)/(x² − 4) = 5", "simplify then solve", "x = ±1",
                         "clearing fractions after simplifying"]],
                 notice=["Two of the four tasks used the same underlying division but asked "
                         "different questions about it.",
                         "The remainder theorem replaced a whole division with one substitution.",
                         "Simplifying before clearing the fractions made the last equation "
                         "linear rather than quartic.",
                         "The excluded values x = 2 and x = −2 mattered only in the last two "
                         "tasks."],
                 obs="The tool is chosen by the question, not by habit: a full quotient needs "
                     "division, a single remainder needs substitution, and a fraction needs "
                     "cancellation.",
                 concl="The four tools of this chapter are interchangeable views of one idea — "
                       "dividing p(x) by x − a — and choosing the right view is what makes the "
                       "work short. x⁴ − 16 = (x² − 4)(x² + 4), so the quotient is x² + 4, "
                       "p(3) = 81 − 16 = 65, and (x⁴ − 16)/(x² − 4) = 5 gives x² + 4 = 5, "
                       "so x = ±1.")),
    ],
    practice=dict(
        A=[("1.1.1", "State the degree and leading coefficient of 3x⁵ − 2x³ + x − 7.",
            "Degree 5, leading coefficient 3.",
            "The degree is the highest power and the leading coefficient is its multiplier.", "F"),
           ("1.1.2", "Add 2x³ − x + 4 and −x³ + 5x² − 2, and state the degree of the sum.",
            "x³ + 5x² − x + 2, degree 3.", "Collect like terms.", "F"),
           ("1.1.3", "Multiply (2x − 1)(x² + 3x − 2) and state the degree of the product.",
            "2x³ + 5x² − 7x + 2, degree 3.", "Each term of the first multiplies each term of "
            "the second; degrees add.", "F"),
           ("1.1.4", "Find p(−2) for p(x) = x⁴ − 3x² + 5x − 1.",
            "16 − 12 − 10 − 1 = −7.", "Substitute and evaluate term by term.", "F"),
           ("1.1.5", "Divide 3x³ + 5x² − 4x + 2 by x + 1.",
            "Quotient 3x² + 2x − 6, remainder 8.",
            "Match leading terms and subtract; check with the division identity.", "R"),
           ("1.1.6", "Divide x³ − 8 by x − 2.",
            "Quotient x² + 2x + 4, remainder 0.", "x − 2 is a factor, so the remainder is "
            "zero.", "F"),
           ("1.1.7", "Find the remainder when p(x) = 2x³ − 5x + 3 is divided by x − 1.",
            "p(1) = 2 − 5 + 3 = 0.", "The remainder theorem replaces the division by "
            "substitution.", "F"),
           ("1.1.8", "Find the remainder when p(x) = x³ + 2x² − 7 is divided by x + 3.",
            "p(−3) = −27 + 18 − 7 = −16.", "The divisor x + 3 is x − (−3), so a = −3.", "R"),
           ("1.1.9", "Show that x − 1 is a factor of x³ − 2x² − x + 2 and find the other "
            "factors.",
            "(x − 1)(x − 2)(x + 1).", "p(1) = 0, then divide and factorise the quadratic.", "R"),
           ("1.1.10", "Simplify (x² − 4)/(x² + 5x + 6), stating the excluded values.",
            "(x − 2)/(x + 3), for x ≠ −3 and x ≠ −2.",
            "Factorise both parts and cancel x + 2.", "R"),
           ("1.1.11", "Explain why (x + 3)/x cannot be simplified to 3.",
            "x is not a factor of x + 3, so there is nothing to cancel.",
            "Cancellation needs a common factor, not a common term.", "R"),
           ("1.1.12", "Solve 3/(x) + 2/(x + 1) = 1 and check for extraneous solutions.",
            "x = (−3 + √33)/2 or x = (−3 − √33)/2; neither is 0 nor −1, so both are valid.",
            "Clear the fractions, solve the quadratic, then substitute each candidate.", "C")],
        B=[("1.2.1", "Investigate whether x − 1 is always a factor of xⁿ − 1 for a positive "
            "integer n. State and justify a conclusion.",
            "Yes: substituting x = 1 gives 1ⁿ − 1 = 0 for every n, so by the factor theorem "
            "x − 1 is always a factor.", "One substitution covers every n.", "R"),
           ("1.2.2", "Build a table of xⁿ − 1 factorised for n = 2 to 6 and describe the "
            "pattern of the factors.",
            "n = 2: (x − 1)(x + 1); n = 3: (x − 1)(x² + x + 1); n = 4: (x − 1)(x + 1)(x² + 1); "
            "n = 5: (x − 1)(x⁴ + x³ + x² + x + 1); n = 6: (x − 1)(x + 1)(x² + x + 1)(x² − x + 1).",
            "Divide out x − 1 first, then factorise the quotient.", "C"),
           ("1.2.3", "Conjecture a rule for the remainder when xⁿ is divided by x − 1, test it "
            "for n = 1 to 5, and justify it.",
            "The remainder is 1, because 1ⁿ = 1 for every n.",
            "The remainder theorem gives the remainder as p(1).", "R"),
           ("1.2.4", "Investigate the number of real roots of xⁿ − 1 for n = 2, 3, 4 and 5, and "
            "explain the pattern.",
            "n even gives 2 real roots (±1); n odd gives 1 real root (1).",
            "A real nth root of 1 exists only for 1, and also −1 when n is even.", "C"),
           ("1.2.5", "The polynomial p(x) = x³ + px + q has a double root. Investigate the "
            "condition on p and q.",
            "The discriminant 4p³ + 27q² = 0; a double root forces it to vanish.",
            "A double root means the factorised form contains a squared factor.", "C"),
           ("1.2.6", "Take a cubic of your own with three distinct integer roots. Divide it by "
            "one of its factors and check the quotient by multiplication.",
            "Any correct answer, for example p(x) = (x − 1)(x − 2)(x − 4) = x³ − 7x² + 14x − 8; "
            "dividing by x − 2 gives x² − 5x + 4 and (x − 2)(x² − 5x + 4) = p(x).",
            "Use the division identity as the check.", "R"),
           ("1.2.7", "Investigate whether the sum of two polynomials of degree 3 can have "
            "degree 4, and justify your answer.",
            "No: the degree of a sum is at most the larger degree, and here at most 3, because "
            "no term of degree 4 can be produced by adding.",
            "Compare the possible powers in each term.", "R"),
           ("1.2.8", "Investigate the remainder when xⁿ − 1 is divided by x − 1 for "
            "n = 2, 3, 4 and 5, and justify a general rule.",
            "The remainder is always 0, because x = 1 is a root of xⁿ − 1 "
            "for every positive integer n.",
            "Use the factor theorem with p(1) = 1ⁿ − 1.", "R"),
           ("1.2.9", "Conjecture a rule for the factorisation of xⁿ − yⁿ for n = 2, "
            "3 and 4, and justify it.",
            "x² − y² = (x − y)(x + y); x³ − y³ = (x − y)(x² + xy + y²); x⁴ "
            "− y⁴ = (x − y)(x + y)(x² + y²). In every case x − y is a "
            "factor.",
            "Each expression is zero when x = y, so x − y is a factor by "
            "the factor theorem.", "C"),
           ("1.2.10", "Investigate the relationship between the roots of a cubic and "
            "its coefficients, and justify.",
            "For x³ + bx² + cx + d with roots r, s and t, the sum r + s + t "
            "= −b, the sum of the pairwise products rs + rt + st = c, and "
            "the product rst = −d.",
            "Expand (x − r)(x − s)(x − t) and compare coefficients.", "C"),
           ("1.2.11", "Investigate the number of sign changes of a polynomial and the "
            "number of positive roots, and justify a bound.",
            "The number of positive roots is at most the number of sign "
            "changes, by Descartes' rule of signs; the difference is always "
            "even.",
            "Count the sign changes in the ordered coefficients.", "C"),
           ],
        C=[("1.3.1", "Write a complete solution to the simplification of "
            "(x³ − 8)/(x² − 4), including the excluded values and a check.",
            "(x − 2)(x² + 2x + 4)/((x − 2)(x + 2)) = (x² + 2x + 4)/(x + 2) for x ≠ 2 and "
            "x ≠ −2.", "Factorise both parts, cancel the common factor, state the exclusions.",
            "R"),
           ("1.3.2", "Write a complete solution to the equation (x + 2)/(x − 1) = (x − 2)/(x + 1), "
            "showing the check for extraneous solutions.",
            "x² + 3x + 2 = x² − 3x + 2, so 6x = 0 and x = 0; neither denominator vanishes, so "
            "x = 0 is valid.", "Cross-multiply, then substitute back.", "R"),
           ("1.3.3", "Write a complete solution to the factorisation of x³ − 7x − 6, showing how "
            "the first root was found.",
            "p(−1) = 0, so divide by x + 1 to get x² − x − 6 = (x − 3)(x + 2); "
            "x³ − 7x − 6 = (x + 1)(x − 3)(x + 2).", "Find a root by inspection, divide, "
            "factorise the quadratic.", "R"),
           ("1.3.4", "Write a complete solution to the inequality (x − 2)(x + 1)(x − 5) < 0, "
            "with a sign line.",
            "2 < x < 5 or x < −1, with the roots excluded.",
            "Mark the roots and count the negative factors in each interval.", "R"),
           ("1.3.5", "Write a complete solution to the division of 2x⁴ − 3x³ + x − 5 by "
            "x² − x + 1, including the check.",
            "Quotient 2x² − x − 3, remainder −3x − 2; check by multiplication.",
            "Match leading terms, subtract, repeat.", "C"),
           ("1.3.6", "Write a complete solution to the equation 1/(x − 2) + 1/(x − 3) = 1, "
            "identifying any extraneous solution.",
            "x² − 5x + 5 = 0, so x = (5 ± √5)/2; both are allowed, so both are valid.",
            "Clear the fractions, solve, substitute.", "R"),
           ("1.3.7", "Write a complete solution to the problem: a rectangle has area "
            "(x² + 5x + 6) cm² and width (x + 2) cm. Find its length and state the restriction "
            "on x.",
            "Length x + 3 cm, with x > −2 so that the width is positive.",
            "Divide the area by the width and apply the physical restriction.", "R"),
           ("1.3.8", "Write a complete solution to expressing (3x + 5)/((x − 1)(x + "
            "2)) in partial fractions.",
            "(3x + 5)/((x − 1)(x + 2)) = 8/3/(x − 1) + 1/3/(x + 2), since A "
            "+ B = 3 and 2A − B = 5 give A = 8/3 and B = 1/3.",
            "Set up the identity, clear the denominator, equate "
            "coefficients and solve.", "R"),
           ("1.3.9", "Write a complete solution to solving 2/(x − 1) = 3/(x + 2), "
            "checking for extraneous roots.",
            "2(x + 2) = 3(x − 1) gives 2x + 4 = 3x − 3, so x = 7; it does "
            "not make either denominator zero, so it is valid.",
            "Cross-multiply, solve, then substitute back into the original "
            "denominators.", "R"),
           ("1.3.10", "Write a complete solution to proving the factor theorem.",
            "Divide p(x) by x − a to get p(x) = (x − a)q(x) + R with R "
            "constant; substituting x = a gives p(a) = R, so R = 0 exactly "
            "when x − a is a factor.",
            "Use the division algorithm and substitute.", "R"),
           ("1.3.11", "Write a complete solution to sketching the graph of p(x) = x³ "
            "− 4x, marking the roots, the turning points and the sign of "
            "the function on each interval.",
            "The roots are −2, 0 and 2; the sign is negative on (−2, 0) and "
            "positive on (0, 2); the turning points are at x = 2/√3 with value "
            "−16/(3√3) and at x = −2/√3 with value 16/(3√3).",
            "Factorise, find the roots, differentiate for the turning "
            "points, and test each interval.", "C"),
           ("1.3.12", "Write a complete solution to the problem: a box has volume 120 "
            "cm³ and a square base of side x. Find x if the total surface "
            "area is 166 cm².",
            "x²h = 120 and 2x² + 4xh = 166 give 2x² + 480/x = 166, so "
            "2x³ − 166x + 480 = 0, that is x³ − 83x + 240 = 0; x ≈ 3.34 "
            "satisfies it, checked by 2(3.34)² + 480/3.34 ≈ 22.3 + 143.7 "
            "= 166.0.",
            "Form both equations, eliminate h, and solve the resulting "
            "cubic, checking each root.", "A"),
           ],
        D=[("1.4.1", "A tank is filled by two pipes. The first alone takes 3 hours longer than "
            "the second, and together they take 2 hours. Find each time alone.",
            "Let the second be t hours: 1/t + 1/(t + 3) = 1/2 gives t² − t − 6 = 0, so t = 3 "
            "and the first takes 6 hours.", "Build the equation from the meaning of the "
            "quantities.", "A"),
           ("1.4.2", "A company's output is modelled by p(t) = t³ − 6t² + 9t thousand units "
            "after t months. Find when output is rising, and state the domain restriction.",
            "p(t) = t(t − 3)², so output is positive for t > 0 and zero at t = 0 and t = 3; "
            "the model applies for t ≥ 0.", "Factorise and use a sign line.", "A"),
           ("1.4.3", "A rectangular box has volume (x³ + 6x² + 11x + 6) cm³ and base "
            "(x + 1)(x + 2) cm². Find its height and state the restriction on x.",
            "Height x + 3 cm, with x > −1 so that the base area is positive.",
            "Divide the volume by the base area.", "A"),
           ("1.4.4", "A cyclist travels 30 km at speed v and returns at v − 4, taking 1 hour "
            "longer. Find v and comment on the sense of the answer.",
            "30/v + 1 = 30/(v − 4) gives v² − 4v − 120 = 0, so v = 12 km/h; the negative root "
            "is rejected as meaningless.", "Build from time = distance ÷ speed.", "A"),
           ("1.4.5", "A engineer specifies a beam whose cross-sectional area is "
            "(4x² − 9) mm² and whose width is (2x − 3) mm. Find the depth and state the "
            "restriction.",
            "Depth 2x + 3 mm, with x > 1.5 so that the width is positive.",
            "Divide and apply the physical restriction.", "A"),
           ("1.4.6", "A shop's profit is modelled by P(n) = −n² + 12n − 20 thousand currency "
            "units for n hundred items. Find the range of n for which the shop makes a profit.",
            "n² − 12n + 20 > 0 gives (n − 2)(n − 10) > 0, so n < 2 or n > 10; with n ≥ 0 the "
            "profitable ranges are 0 ≤ n < 2 and n > 10.",
            "Solve the inequality and apply the domain.", "A"),
           ("1.4.7", "Two workers together complete a job in 6 hours. One works twice as fast "
            "as the other. Find each time alone and check the answer.",
            "1/t + 1/(2t) = 1/6 gives 3/(2t) = 1/6, so t = 9 hours and the slower takes 18 "
            "hours; check: 1/9 + 1/18 = 3/18 = 1/6.", "Rates add.", "A"),
           ("1.4.8", "A farmer's yield is modelled by Y(a) = (a − 2)(a − 8)(a + 1) tonnes for "
            "a kilograms of fertiliser per hectare. Find the range of a giving a positive "
            "yield and comment on the practical domain.",
            "Positive for −1 < a < 2 and a > 8; the practical domain is a ≥ 0, so 0 ≤ a < 2 "
            "and a > 8.", "Sign line, then apply the domain.", "A"),
           ("1.4.9", "A concentration is modelled by C(t) = (t² − 16)/(t − 4) for t minutes. "
            "Explain what happens at t = 4 and why the model must state it.",
            "The model simplifies to t + 4 for t ≠ 4, but t = 4 is excluded because the "
            "original denominator vanishes; the model is undefined there.",
            "Factorise, cancel, state the exclusion.", "R"),
           ("1.4.10", "A phone company charges c(n) = (50n + 200)/(n + 4) currency units for n "
            "gigabytes. Explain the behaviour as n grows and find when the charge exceeds 20.",
            "c(n) = 50 − 200/(n + 4), which rises towards 50; c(n) > 20 gives 200/(n + 4) < 30, "
            "so n + 4 > 6.67 and n > 2.67.", "Divide to expose the limiting behaviour.", "A"),
           ("1.4.11", "A bridge cable's sag is modelled by s(L) = (L³ − 27)/(L − 3) metres for "
            "span L. Explain the model at L = 3 and find the sag for L = 6.",
            "s(L) = L² + 3L + 9 for L ≠ 3, and s(6) = 36 + 18 + 9 = 63 m; at L = 3 the model "
            "is undefined, not zero.", "Factorise the numerator.", "R"),
           ("1.4.12", "A student claims that if a rational equation has an extraneous solution "
            "then it has no real solution. Investigate and justify.",
            "False: (x + 1)/(x − 2) = 3 has x = 3.5, and 2/x + 3/(x + 1) = 1 has two valid "
            "solutions; an extraneous solution only removes the candidates that make a "
            "denominator zero.",
            "Look for an equation with one valid and one extraneous candidate.", "C")],
    ),
    assessment=[
        dict(title="A1 · The container specification",
             text="A container's capacity is modelled by V(x) = x³ + 6x² + 11x + 6 cm³ and its "
                  "base area by A(x) = (x + 1)(x + 2) cm². Find the height, state the "
                  "restriction on x that the physical situation imposes, and explain what the "
                  "restriction protects the answer from.",
             note="Criteria A and D · factorise, divide, then apply the physical domain."),
        dict(title="A2 · The shared job",
             text="Two machines together complete a batch in 4 hours. The older machine takes "
                  "6 hours longer than the newer one. Find each machine's time alone, check "
                  "the answer, and explain why adding the two times is not the answer.",
             note="Criteria A and C · build the equation from the rates, and set out the check "
                  "clearly."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of equivalence, "
        "generalisation and simplification appear in your work?",
        "How is the global context of personal and cultural expression, and its exploration of "
        "the language of algebra as a way of making structure visible, visible in the "
        "investigations and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of a simplified form of an expression, and what would you "
        "still like to ask?",
    ],
    review=dict(
        ideas=["The degree of a product of polynomials is the sum of the degrees.",
               "Dividend = divisor × quotient + remainder is the check on every division.",
               "The remainder theorem gives the remainder on dividing by x − a as p(a).",
               "The factor theorem says x − a is a factor exactly when p(a) = 0.",
               "An algebraic fraction is cancelled only by a common factor.",
               "Excluded values are the values that made a cancelled factor zero.",
               "A rational equation is solved by clearing fractions, then checking every "
               "candidate.",
               "The factored form of a polynomial decides its sign completely."],
        vocab=["polynomial", "degree", "leading coefficient", "long division", "quotient",
               "remainder", "remainder theorem", "factor theorem", "root", "linear factor",
               "algebraic fraction", "excluded value", "extraneous solution", "sign line",
               "double root"],
        mixed=[("1.R1", "Divide x³ + 2x² − 5x − 6 by x + 3."),
               ("1.R2", "Find the remainder when x⁴ + 2x − 3 is divided by x − 1."),
               ("1.R3", "Simplify (x² + 7x + 12)/(x² + 5x + 4), stating the excluded values."),
               ("1.R4", "Solve (x − 1)/(x + 2) = 2 and check for extraneous solutions."),
               ("1.R5", "Solve (x + 1)(x − 2)(x + 4) ≤ 0."),
               ("1.R6", "Explain why a cubic has at most three real roots.")],
    ),
    projects=dict(
        service=[("Community need", "Public budgets and building specifications are published "
                                    "as simplified expressions whose restrictions are not "
                                    "stated."),
                 ("Mathematical connection", "Algebraic fractions, excluded values and "
                                             "rational equations."),
                 ("Proposed action", "Collect three published specifications, rewrite each as a "
                                     "single simplified expression, and publish the "
                                     "restrictions that were dropped."),
                 ("Expected impact", "A reader can tell where a published formula stops being "
                                     "valid."),
                 ("Student reflection", "Record the specifications, the simplifications and the "
                                        "restrictions you found.")],
        community=[("Project idea", "A precision audit of the school's own published formulas."),
                   ("Need", "Timetables, budgets and lab recipes are quoted as formulas with "
                            "unstated limits."),
                   ("Research question", "Which published school formulas hide a restriction, "
                                         "and what happens when it is ignored?"),
                   ("Mathematics", "Algebraic fractions, excluded values and rational "
                                   "equations."),
                   ("Action or outcome", "A one-page audit with each formula, its restriction "
                                         "and a verdict."),
                   ("Beneficiaries", "Everyone who uses a school formula."),
                   ("Evidence", "The audit sheet with restrictions and verdicts.")],
        personal=[("Personal interest", "Cooking, gaming, sport or music."),
                  ("Learning goal", "To rewrite a formula you use into its simplest form and "
                                    "state honestly where it stops working."),
                  ("Product or outcome", "A formula card with the restriction written on it."),
                  ("Mathematics", "Simplification, cancellation and excluded values."),
                  ("Process", "Take three formulas, simplify each, and find the values that "
                              "break them."),
                  ("Evidence", "The formula cards and the restrictions you found.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=2, title="Functions: Transformations, Composites and Inverses",
    key="Relationships", related=["Change", "Representation", "Patterns"],
    context="Scientific and technical innovation",
    exploration="models that translate a measurement into a prediction",
    inquiry=("A function is a rule that pairs each input with exactly one output; transforming, "
             "composing and inverting are operations on the rule itself, and each leaves a trace "
             "on the graph."),
    atl=("Critical thinking",
         "In order for a student to predict the effect of a transformation on a model, students "
         "must compare a parent graph with its image, identify which coordinate has changed and "
         "how, and justify the algebraic rule that produces the same change."),
    standfirst="A function is a relationship between two quantities. The same relationship can be "
               "written as a rule, as a table, as a graph or as a machine, and each representation "
               "makes a different operation visible.",
    engage="A sensor reports a temperature that a model then converts into a pressure. The "
           "sensor is recalibrated so that every reading is 3 degrees higher. Which part of the "
           "model has to change, and does the graph of the model move up, down, left or right?",
    questions=[("Factual", "What are the domain and range of a function, and what does the "
                           "notation f(x) mean?"),
               ("Conceptual", "Why does f(x) + k move a graph vertically while f(x + k) moves it "
                              "horizontally, and what makes a function invertible?"),
               ("Debatable", "If two representations of the same function look nothing alike, "
                             "which one is the function?")],
    application_lede="These tasks use function notation, transformations, composition and "
                     "inverses. State the domain of every function you write, and check every "
                     "inverse by composition.",
    projects_lede="A model is a representation of a relationship. Choose the representation that "
                  "makes the operation you need visible, and say what it hides.",
    sections=[
        dict(id="2.1", title="Domain, range and function notation",
             inquiry_q="What does the notation f(x) actually assert?",
             teach=[
                 "A function is a rule that assigns exactly one output to each input of a stated set, and the relationships it can express are limited by that set. The domain is the set of permitted inputs and the range is the set of outputs the rule can produce. A rule without a stated domain is incomplete, because the same formula can describe different functions on different domains.",
                 "Function notation f(x) names the output for the input x. Writing f(2) = 5 is a statement about one input; writing f(x) = 2x + 1 is a statement about all of them. The notation distinguishes the rule from its values, which is what makes composition possible.",
                 "Two functions are equal only when they agree on every input of a common domain. The formulas x²/x and x agree everywhere except at x = 0, so they are not the same function unless 0 is excluded from the domain of both.",
                 "A mapping diagram, a table, a formula and a graph are four representations of one relationship between input and output. Each is complete, and each makes a different operation easy: a table shows values, a formula shows rules, a graph shows behaviour, and the patterns in each are the same patterns seen from a different angle.",
             ], examples=[
                 dict(q="The function f is defined by f(x) = √(x − 2) + 1. State its domain and "
                        "range, and explain why the domain cannot be larger.",
                      vis=F("table", [["x", "x − 2", "√(x − 2)", "f(x)"],
                                      ["1", "−1", "undefined", "undefined"],
                                      ["2", "0", "0", "1"],
                                      ["3", "1", "1", "2"],
                                      ["6", "4", "2", "3"]],
                            caption="The square root forces the domain to start at 2."),
                      reasoning="The expression under a square root must be non-negative, and "
                               "the root itself is never negative, which fixes the range from "
                               "below.",
                      steps=["The expression under the root is x − 2, so x − 2 ≥ 0 and x ≥ 2.",
                             "The domain is therefore x ≥ 2.",
                             "√(x − 2) takes every value from 0 upwards, so f(x) takes every "
                             "value from 1 upwards.",
                             "The range is f(x) ≥ 1.",
                             "The domain cannot be larger because any x below 2 makes the root "
                             "undefined."],
                      ans="domain x ≥ 2, range f(x) ≥ 1",
                      interp="The domain is part of the definition, not an afterthought: the same "
                             "formula with a smaller domain is a different function."),
                 dict(q="Show that f(x) = x²/x and g(x) = x are not the same function, and "
                        "explain what has to change for them to become equal.",
                      vis=F("table", [["x", "f(x) = x²/x", "g(x) = x", "agree?"],
                                      ["−2", "−2", "−2", "yes"],
                                      ["0", "undefined", "0", "no"],
                                      ["2", "2", "2", "yes"],
                                      ["3", "3", "3", "yes"]],
                            caption="One undefined value is enough to separate two functions."),
                      reasoning="Two functions are equal only when they agree on every input of "
                               "a common domain, so a single disagreement is decisive.",
                      steps=["f(0) = 0²/0, which is undefined because division by zero is not "
                             "defined.",
                             "g(0) = 0, which is defined.",
                             "So the two functions disagree at x = 0.",
                             "If the domain of both is restricted to x ≠ 0, then they agree "
                             "everywhere and become equal.",
                             "Hence f and g are different functions on the real numbers but the "
                             "same function on x ≠ 0."],
                      ans="they differ at x = 0; restricting the domain of g to x ≠ 0 makes "
                          "them equal",
                      interp="Equality of functions is equality on a domain, not similarity of "
                             "formulas."),
             ], inv=dict(
                 task="Take four rules of your own: a linear one, a quadratic one, one with a "
                      "square root and one with a fraction. For each, find the largest domain "
                      "you can state on the real numbers, find the range, and record one input "
                      "that is not permitted. Then say which representation — table, formula, "
                      "graph or machine — shows the domain most clearly.",
                 table=[["rule", "largest domain", "range", "excluded input"],
                        ["3x − 5", "all real x", "all real y", "none"],
                        ["x²", "all real x", "y ≥ 0", "none"],
                        ["√(x + 4)", "x ≥ −4", "y ≥ 0", "x = −5"],
                        ["1/(x − 1)", "x ≠ 1", "y ≠ 0", "x = 1"],
                        ["x³", "all real x", "all real y", "none"],
                        ["(x − 2)/(x − 2)", "x ≠ 2", "y = 1 only", "x = 2"]],
                 notice=["Two of the six rules accepted every real input.",
                         "The square root rule excluded everything below a single number.",
                         "The fraction rule excluded exactly one value, and its range excluded "
                         "exactly one value too.",
                         "The last rule looked like a constant but was undefined at one point."],
                 obs="The domain is decided by the operations in the rule: division excludes "
                     "zeros of the denominator and roots exclude negative inputs.",
                 concl="A function is a rule together with a domain, and the range is what the "
                       "rule can produce from that domain. The domain is not decoration: the "
                       "same formula on a different domain is a different function, which is "
                       "why the domain is stated before anything else is claimed.")),
        dict(id="2.2", title="Transformations of graphs",
             inquiry_q="Why does f(x) + 3 move a graph up but f(x + 3) move it left?",
             teach=[
                 "A translation of the graph of y = f(x) by the vector (a, b) has equation y = f(x − a) + b. The number inside the bracket acts on x before the function, so it moves the graph in the opposite direction to its sign.",
                 "The reason for the reversal is order of operations. To obtain the same output as f at x = 0, the translated graph must be evaluated at x = −a, so the whole graph sits a units to the left of where it started.",
                 "A reflection in the x-axis has equation y = −f(x), and a reflection in the y-axis has equation y = f(−x). A stretch parallel to the y-axis by factor k has equation y = kf(x), and a stretch parallel to the x-axis by factor k has equation y = f(x/k).",
                 "The two descriptions of a transformation — as a coordinate rule and as an equation — must agree. Reading the equation as a coordinate rule is the standard way to check that a transformation has been described correctly.",
             ], examples=[
                 dict(q="Describe the transformation taking y = x² to y = (x − 3)² + 2, and "
                        "state the image of the point (1, 1).",
                      vis=F("table", [["point on y = x²", "image on y = (x − 3)² + 2", "change"],
                                      ["(0, 0)", "(3, 2)", "right 3, up 2"],
                                      ["(1, 1)", "(4, 3)", "right 3, up 2"],
                                      ["(−1, 1)", "(2, 3)", "right 3, up 2"],
                                      ["(2, 4)", "(5, 6)", "right 3, up 2"]],
                            caption="Every point moves by the same vector."),
                      reasoning="Compare the equation with y = f(x − a) + b to read off the "
                               "translation, then apply it to the point.",
                      steps=["The parent graph is f(x) = x² and the new graph is "
                             "f(x − 3) + 2.",
                             "So a = 3 and b = 2, which is a translation by the vector (3, 2).",
                             "The vertex moves from (0, 0) to (3, 2).",
                             "The point (1, 1) moves to (1 + 3, 1 + 2) = (4, 3).",
                             "Check: (4 − 3)² + 2 = 1 + 2 = 3, which is the y-coordinate."],
                      ans="translation by (3, 2); the image of (1, 1) is (4, 3)",
                      interp="The equation encodes the coordinate rule, and reading it as a "
                             "coordinate rule is the fastest check."),
                 dict(q="Describe the transformation taking y = x² to y = −2(x + 1)², and "
                        "explain the order of the two changes.",
                      vis=F("table", [["stage", "equation", "change"],
                                      ["parent", "y = x²", "—"],
                                      ["horizontal", "y = (x + 1)²", "left 1"],
                                      ["stretch", "y = 2(x + 1)²", "stretch, factor 2, y-axis"],
                                      ["reflect", "y = −2(x + 1)²", "reflect in x-axis"]],
                            caption="The stretch and the reflection both act on the output."),
                      reasoning="Separate the change inside the bracket, which acts on the "
                               "input, from the changes outside, which act on the output.",
                      steps=["Inside the bracket, x + 1 means x − (−1), so a = −1: a "
                             "translation 1 unit left.",
                             "Outside, the factor 2 multiplies the output: a stretch parallel "
                             "to the y-axis by factor 2.",
                             "The leading minus sign reflects in the x-axis.",
                             "The vertex moves from (0, 0) to (−1, 0) and the graph opens "
                             "downwards.",
                             "Check with a point: on the parent, x = 0 gives 0; on the new "
                             "graph, x = −1 gives 0."],
                      ans="translation 1 left, stretch by factor 2 parallel to the y-axis, "
                          "then reflection in the x-axis",
                      interp="Changes inside the bracket move the graph horizontally; changes "
                             "outside move it vertically or reflect it. Confusing the two is "
                             "the commonest transformation error."),
             ], inv=dict(
                 task="Take the parent graph y = x². Write the equation of the image after "
                      "each of these: a translation 2 right and 3 down; a reflection in the "
                      "y-axis; a stretch by factor 3 parallel to the y-axis; and a translation "
                      "1 left followed by a stretch by factor 2 parallel to the x-axis. For "
                      "each, plot the image of the point (1, 1) and check it satisfies your "
                      "equation.",
                 table=[["transformation", "equation", "image of (1, 1)", "check"],
                        ["right 2, down 3", "y = (x − 2)² − 3", "(3, −2)", "1 − 3 = −2"],
                        ["reflect in y-axis", "y = (−x)² = x²", "(1, 1)", "unchanged"],
                        ["stretch 3, y-axis", "y = 3x²", "(1, 3)", "3 × 1 = 3"],
                        ["left 1 then stretch 2, x-axis", "y = ((x + 1)/2)²", "(1, 1)", "1² = 1"]],
                 notice=["The reflection in the y-axis left this particular graph unchanged, "
                         "because x² is symmetric.",
                         "The stretch parallel to the y-axis multiplied the y-coordinate.",
                         "The stretch parallel to the x-axis divided the x-coordinate, so the "
                         "graph widened.",
                         "Every image point satisfied the equation it was supposed to satisfy."],
                 obs="A change inside the bracket acts on the input and moves the graph "
                     "horizontally; a change outside acts on the output.",
                 concl="The equation of an image is the parent equation with the coordinate "
                       "rule substituted into it, so y = f(x) translated by (a, b) becomes "
                       "y = f(x − a) + b. Reading the equation as a coordinate rule is the "
                       "check that the transformation has been described correctly.")),
        dict(id="2.3", title="Composite functions",
             inquiry_q="In what order do the functions in f(g(x)) act?",
             teach=[
                 "The composite function f(g(x)) applies g first and then f. The inner function acts first, which is the opposite of the order in which the functions are written, and this reversal is the single commonest source of error.",
                 "The domain of f(g(x)) is the set of inputs x for which g(x) is defined and g(x) lies in the domain of f. Both conditions must hold, so the domain of a composite is usually smaller than either domain alone.",
                 "Composition is associative: f(g(h(x))) can be built as f∘(g∘h) or as (f∘g)∘h with the same result. It is not commutative in general, and f(g(x)) = g(f(x)) only for specially related functions.",
                 "A function machine is a faithful picture of composition: the output of the first box is the input of the second. Drawing the machine before writing the algebra prevents the order being reversed.",
             ], examples=[
                 dict(q="Given f(x) = 2x + 1 and g(x) = x² − 3, find f(g(x)), g(f(x)) and "
                        "f(g(2)), and state the domain of f(g(x)).",
                      vis=F("table", [["x", "g(x)", "f(g(x))", "f(x)", "g(f(x))"],
                                      ["0", "−3", "−5", "1", "−2"],
                                      ["1", "−2", "−3", "3", "6"],
                                      ["2", "1", "3", "5", "22"],
                                      ["−1", "−2", "−3", "−1", "−2"]],
                            caption="The two orders give different functions."),
                      reasoning="Substitute the inner function into the outer one, and note "
                               "that the two orders differ.",
                      steps=["f(g(x)) = 2(g(x)) + 1 = 2(x² − 3) + 1 = 2x² − 5.",
                             "g(f(x)) = (f(x))² − 3 = (2x + 1)² − 3 = 4x² + 4x − 2.",
                             "The two are different: f(g(1)) = −3 while g(f(1)) = 6.",
                             "f(g(2)) = 2(4) − 5 = 3.",
                             "Both f and g accept every real input, so the domain of f(g(x)) is "
                             "all real x."],
                      ans="f(g(x)) = 2x² − 5, g(f(x)) = 4x² + 4x − 2, f(g(2)) = 3, domain all "
                          "real x",
                      interp="Composition is not commutative, and the two orders are different "
                             "functions with different graphs."),
                 dict(q="Given f(x) = √x and g(x) = x − 4, find f(g(x)) and state its domain.",
                      vis=F("table", [["x", "g(x) = x − 4", "√(g(x))", "defined?"],
                                      ["2", "−2", "undefined", "no"],
                                      ["4", "0", "0", "yes"],
                                      ["5", "1", "1", "yes"],
                                      ["8", "4", "2", "yes"]],
                            caption="The inner output must be a permitted input of the outer "
                                    "function."),
                      reasoning="The composite is defined only where the inner function is "
                               "defined and its output lies in the domain of the outer one.",
                      steps=["f(g(x)) = √(x − 4).",
                             "The square root requires x − 4 ≥ 0, so x ≥ 4.",
                             "g itself is defined for all x, so the only restriction comes from "
                             "f.",
                             "The domain of f(g(x)) is x ≥ 4.",
                             "Note that this is smaller than the domain of f alone, which is "
                             "x ≥ 0."],
                      ans="f(g(x)) = √(x − 4), domain x ≥ 4",
                      interp="The domain of a composite is the intersection of two conditions, "
                             "and it is usually smaller than either domain alone."),
             ], inv=dict(
                 task="Take f(x) = 3x − 2 and g(x) = x + 5. Compute f(g(x)), g(f(x)), "
                      "f(f(x)) and g(g(x)), and record the value of each at x = 1. Then find a "
                      "pair of functions of your own for which the two orders give the same "
                      "answer, and explain why.",
                 table=[["composite", "simplified", "value at x = 1"],
                        ["f(g(x))", "3(x + 5) − 2 = 3x + 13", "16"],
                        ["g(f(x))", "(3x − 2) + 5 = 3x + 3", "6"],
                        ["f(f(x))", "3(3x − 2) − 2 = 9x − 8", "1"],
                        ["g(g(x))", "(x + 5) + 5 = x + 10", "11"],
                        ["f(g(x)) − g(f(x))", "(3x + 13) − (3x + 3) = 10", "10"]],
                 notice=["All four composites were linear, because both functions were linear.",
                         "The two orders differed by a constant, 10, rather than by a whole "
                         "function.",
                         "Repeating a function changed its gradient, so f(f(x)) had gradient 9.",
                         "A pair of linear functions with the same gradient would commute."],
                 obs="The order matters, but for linear functions the two orders differ only by "
                     "a constant.",
                 concl="The composite f(g(x)) applies g first, and the two orders are different "
                       "functions in general. Two functions commute exactly when they are "
                       "specially related — for example when both are translations, or when "
                       "they are powers of one another.")),
        dict(id="2.4", title="Inverse functions",
             inquiry_q="When does a function have an inverse, and how is it found?",
             teach=[
                 "The inverse function f⁻¹ reverses the relationship: if f(a) = b then f⁻¹(b) = a. It exists exactly when f is one-to-one on its domain, because two different inputs with the same output could not be told apart on the way back.",
                 "The horizontal line test decides invertibility. If any horizontal line meets the graph more than once, two inputs share an output and no inverse exists on that domain.",
                 "Restricting the domain can make a function one-to-one. The squaring function is not one-to-one on the real numbers, but it is one-to-one on x ≥ 0, and its inverse there is the square root.",
                 "The inverse is found by writing y = f(x), rearranging to make x the subject, and then swapping the letters. The check is composition: f⁻¹(f(x)) = x and f(f⁻¹(x)) = x on the restricted domains.",
             ], examples=[
                 dict(q="Find the inverse of f(x) = 3x − 5, state its domain and range, and "
                        "check it by composition.",
                      vis=F("table", [["x", "f(x)", "f⁻¹(x)", "check"],
                                      ["0", "−5", "5/3", "f(5/3) = 0"],
                                      ["1", "−2", "2", "f(2) = 1"],
                                      ["2", "1", "5/3", "f(5/3) = 0"],
                                      ["3", "4", "4/3", "f(4/3) = −1"]],
                            caption="The inverse swaps the roles of input and output."),
                      reasoning="Rearrange to make x the subject, then swap the letters, and "
                               "verify by composition.",
                      steps=["Write y = 3x − 5.",
                             "Add 5: y + 5 = 3x, so x = (y + 5)/3.",
                             "Swap the letters: f⁻¹(x) = (x + 5)/3.",
                             "Check: f⁻¹(f(x)) = (3x − 5 + 5)/3 = x.",
                             "Also f(f⁻¹(x)) = 3((x + 5)/3) − 5 = x + 5 − 5 = x."],
                      ans="f⁻¹(x) = (x + 5)/3, domain all real x, range all real x",
                      interp="The composition check is the definition of an inverse: it undoes "
                             "the function in both directions."),
                 dict(q="Show that f(x) = x² has no inverse on the real numbers, find a domain "
                        "on which it does, and state the inverse there.",
                      vis=F("table", [["x", "f(x) = x²", "horizontal line y = 4", "one-to-one?"],
                                      ["−2", "4", "meets twice", "no"],
                                      ["0", "0", "meets once", "—"],
                                      ["2", "4", "meets twice", "no"],
                                      ["3", "9", "meets once", "—"]],
                            caption="Two inputs with the same output block the inverse."),
                      reasoning="A horizontal line meeting the graph twice means two inputs "
                               "share an output, so the function is not one-to-one and has no "
                               "inverse on that domain.",
                      steps=["The line y = 4 meets y = x² at x = −2 and x = 2.",
                             "So f(−2) = f(2) = 4, and the two inputs cannot be distinguished "
                             "on the way back.",
                             "Restrict the domain to x ≥ 0. Then every horizontal line meets "
                             "the graph at most once.",
                             "On x ≥ 0 the inverse is f⁻¹(x) = √x, with domain x ≥ 0.",
                             "Check: f⁻¹(f(x)) = √(x²) = x for x ≥ 0, and f(f⁻¹(x)) = (√x)² = x "
                             "for x ≥ 0."],
                      ans="no inverse on the real numbers; on x ≥ 0 the inverse is √x with "
                          "domain x ≥ 0",
                      interp="Restricting the domain is how a many-to-one relationship becomes "
                             "a one-to-one one, and the restriction must be stated."),
             ], inv=dict(
                 task="Take six functions of your own: two linear, one quadratic, one with a "
                      "square root, one rational and one cubic. For each, decide whether it is "
                      "one-to-one on its natural domain. If it is, find the inverse and verify "
                      "it by composition; if it is not, restrict the domain so that it becomes "
                      "one-to-one and find the inverse on that restriction. Record the domain "
                      "and range of every inverse you find.",
                 table=[["function", "one-to-one?", "restriction", "inverse", "domain of inverse"],
                        ["2x + 1", "yes", "none", "(x − 1)/2", "all real x"],
                        ["x³", "yes", "none", "x^(1/3)", "all real x"],
                        ["x²", "no", "x ≥ 0", "√x", "x ≥ 0"],
                        ["√(x − 2)", "yes", "none", "x² + 2", "x ≥ 0"],
                        ["1/x", "yes", "x ≠ 0", "1/x", "x ≠ 0"],
                        ["(x − 1)/(x + 2)", "yes", "x ≠ −2", "(1 + 2x)/(1 − x)", "x ≠ 1"]],
                 notice=["Four of the six functions were already one-to-one and needed no "
                         "restriction.",
                         "The squaring function needed the restriction x ≥ 0 before an inverse "
                         "existed.",
                         "The rational function was one-to-one because its graph never turned "
                         "back.",
                         "Every inverse swapped the domain of the original with its range."],
                 obs="A function is invertible exactly when no horizontal line meets its graph "
                     "twice, and restriction is the tool for making that true.",
                 concl="The inverse function exists exactly when the original is one-to-one, "
                       "and it is verified by composition in both directions. Where the "
                       "original is not one-to-one, a restricted domain is stated as part of "
                       "the definition, and the inverse's domain is the original's range.")),
        dict(id="2.5", title="Modelling with transformations",
             inquiry_q="How does a transformation of a model show up in the situation it "
                       "describes?",
             teach=[
                 "A model is a function whose input and output both carry units. A transformation of the model is therefore a change in the situation, and reading the transformation tells you what changed without recalculating anything.",
                 "A vertical translation changes the output at every input, which is an additive change in the situation: a fixed charge added to a bill, a starting temperature added to a reading. A horizontal translation changes the input, which is a shift in time or in the zero of a scale.",
                 "A vertical stretch multiplies every output, which is a multiplicative change: a price rise, a calibration factor. A horizontal stretch divides every input, which is a change of unit or of time scale.",
                 "Combining transformations builds a family of models from one parent. A single parent function plus a small set of parameters describes a whole class of situations, and each parameter has a physical meaning.",
             ], examples=[
                 dict(q="A taxi charges a flag fall of 4 currency units and then 2 per "
                        "kilometre. A rival charges a flag fall of 6 and 1.5 per kilometre. "
                        "Model both, describe the transformation between them, and find the "
                        "distance at which they cost the same.",
                      vis=F("table", [["distance (km)", "first model", "second model", "difference"],
                                      ["0", "4", "6", "−2"],
                                      ["2", "8", "9", "−1"],
                                      ["4", "12", "12", "0"],
                                      ["6", "16", "15", "1"],
                                      ["8", "20", "18", "2"]],
                            caption="Two linear models cross at one distance."),
                      reasoning="Model each as a linear function, read the transformation as a "
                               "translation and a stretch, and solve for the crossing.",
                      steps=["First model: C₁(d) = 2d + 4. Second model: C₂(d) = 1.5d + 6.",
                             "The second is the first translated up by 2 and stretched "
                             "parallel to the x-axis by factor 2/1.5 = 4/3.",
                             "Set them equal: 2d + 4 = 1.5d + 6.",
                             "Then 0.5d = 2, so d = 4 km.",
                             "Check: C₁(4) = 12 and C₂(4) = 12."],
                      ans="C₁ = 2d + 4, C₂ = 1.5d + 6; they cost the same at 4 km",
                      interp="The transformation description explains the crossing before any "
                             "algebra: a higher fixed charge with a lower rate must cross."),
                 dict(q="A cooling model is T(t) = 20 + 60(0.8)ᵗ for t minutes after 14:00. "
                        "Write the model for s minutes after the same start, and then for s "
                        "minutes after 15:00.",
                      vis=F("table", [["minutes after 14:00", "T(t)", "minutes after 15:00",
                                       "T(s)"],
                                      ["0", "80", "−60", "not applicable"],
                                      ["60", "20 + 60(0.8)⁶⁰", "0", "same as t = 60"],
                                      ["120", "20 + 60(0.8)¹²⁰", "60", "same as t = 120"],
                                      ["−60", "20 + 60(0.8)⁻⁶⁰", "−120", "same as t = −60"]],
                            caption="Changing the origin shifts the input."),
                      reasoning="A change of time origin is a horizontal translation, so the "
                               "new input is the old input minus the shift.",
                      steps=["For s minutes after 14:00 the model is identical: T(s) = 20 + "
                             "60(0.8)ˢ.",
                             "For s minutes after 15:00, the old input is t = s + 60, because "
                             "15:00 is 60 minutes after 14:00.",
                             "So T(s) = 20 + 60(0.8)^(s + 60) = 20 + 60(0.8)⁶⁰(0.8)ˢ.",
                             "Using the index law, (0.8)^(s + 60) = (0.8)ˢ × (0.8)⁶⁰, and "
                             "(0.8)⁶⁰ is essentially 0.",
                             "So the 15:00 model is essentially T(s) ≈ 20, which is why the "
                             "canteen switched to a different model later in the day."],
                      ans="T(s) = 20 + 60(0.8)ˢ after 14:00; T(s) = 20 + 60(0.8)^(s + 60) "
                          "after 15:00",
                      interp="A change of origin is a horizontal translation, and the index "
                             "law is what makes the translated exponential readable."),
             ], inv=dict(
                 task="Take the parent model P(n) = 5n, the price of n items at 5 each. Write "
                      "models for: a 3 currency unit delivery charge added; a 20 per cent "
                      "discount; a shop that charges for n + 2 items; and a shop whose item "
                      "costs half. For each, say whether the change is vertical or horizontal, "
                      "and find the number of items at which the discounted model costs the "
                      "same as the original.",
                 table=[["situation", "model", "kind of change", "equal to P when"],
                        ["delivery charge 3", "5n + 3", "vertical translation", "never"],
                        ["20% discount", "4n", "vertical stretch, factor 0.8", "n = 0"],
                        ["charges for n + 2", "5(n + 2)", "horizontal translation", "n = −2"],
                        ["item costs half", "2.5n", "vertical stretch, factor 0.5", "n = 0"]],
                 notice=["The delivery charge raised every price by the same amount, so it was "
                         "a vertical translation.",
                         "The discount multiplied every price by 0.8, so it was a vertical "
                         "stretch.",
                         "Charging for n + 2 items was a horizontal translation, and it only "
                         "mattered for positive n.",
                         "Two of the models met the original only at n = 0, because both passed "
                         "through the origin."],
                 obs="An additive change in the situation is a vertical translation; a "
                     "multiplicative change is a vertical stretch; a change of origin is a "
                     "horizontal translation.",
                 concl="A transformation of a model is a change in the situation, and the "
                       "direction of the change tells you what changed. Reading the "
                       "transformation is often faster than recalculating the model, and it "
                       "explains why two models cross.")),
        dict(id="2.6", title="Investigation: when is a function invertible?",
             inquiry_q="What property of a graph decides whether an inverse exists?",
             teach=[
                 "The horizontal line test is a complete criterion: a function is one-to-one exactly when no horizontal line meets its graph more than once. The test works because a horizontal line collects all the inputs with one particular output, so a second meeting is a repeated pattern among the outputs.",
                 "The algebraic version of the same test is that f(a) = f(b) must force a = b. Proving that implication is proving that the function is one-to-one, and it is the form used when no graph is available.",
                 "A function that is strictly increasing or strictly decreasing on its whole domain is one-to-one, because equal outputs would force a reversal. This is why monotonicity is the standard sufficient condition.",
                 "The graph of an inverse is the reflection of the graph in the line y = x, because the inverse swaps the coordinates of every point. Drawing the line of reflection is a quick check that an inverse has been found correctly.",
             ], examples=[
                 dict(q="Decide whether f(x) = 2x + 7 is one-to-one, and prove it algebraically.",
                      vis=F("table", [["a", "b", "f(a)", "f(b)", "f(a) = f(b)?"],
                                      ["1", "1", "9", "9", "yes, and a = b"],
                                      ["1", "2", "9", "11", "no"],
                                      ["−3", "4", "1", "15", "no"],
                                      ["0", "−3.5", "7", "0", "no"]],
                            caption="Equal outputs force equal inputs."),
                      reasoning="Suppose f(a) = f(b) and deduce a = b; the implication is the "
                               "definition of one-to-one.",
                      steps=["Suppose f(a) = f(b), so 2a + 7 = 2b + 7.",
                             "Subtract 7 from both sides: 2a = 2b.",
                             "Divide by 2: a = b.",
                             "So equal outputs force equal inputs, and f is one-to-one.",
                             "The inverse is f⁻¹(x) = (x − 7)/2, and its graph is the reflection "
                             "in y = x."],
                      ans="one-to-one; f⁻¹(x) = (x − 7)/2",
                      interp="The algebraic test is the same claim as the horizontal line "
                             "test, written as an implication."),
                 dict(q="Decide whether f(x) = x² − 4x is one-to-one on the real numbers, and "
                        "find a restricted domain on which it is.",
                      vis=F("table", [["x", "f(x)", "partner with the same value", "one-to-one?"],
                                      ["0", "0", "x = 4", "no"],
                                      ["1", "−3", "x = 3", "no"],
                                      ["2", "−4", "none", "—"],
                                      ["4", "0", "x = 0", "no"],
                                      ["5", "5", "none", "—"]],
                            caption="A parabola fails the horizontal line test."),
                      reasoning="Complete the square to find the axis of symmetry, and note "
                               "that points equidistant from it share an output.",
                      steps=["Complete the square: f(x) = (x − 2)² − 4.",
                             "The axis of symmetry is x = 2, so f(2 + h) = f(2 − h) for every h.",
                             "For example f(1) = f(3) = −3, so the function is not one-to-one.",
                             "Restrict the domain to x ≥ 2. Then the function is strictly "
                             "increasing and therefore one-to-one.",
                             "On x ≥ 2 the inverse is f⁻¹(x) = 2 + √(x + 4), with domain "
                             "x ≥ −4."],
                      ans="not one-to-one on the real numbers; one-to-one on x ≥ 2, where "
                          "f⁻¹(x) = 2 + √(x + 4)",
                      interp="Completing the square locates the axis of symmetry, and the axis "
                             "is exactly where the function stops being one-to-one."),
             ], inv=dict(
                 task="Take six graphs of your own: a straight line, a parabola, a cubic, an "
                      "exponential curve, a reciprocal curve and a step function. For each, "
                      "apply the horizontal line test, and where it fails, find a restricted "
                      "domain on which it passes. Sketch the inverse on the same axes, using "
                      "the line y = x as the mirror, and record the domain and range of each "
                      "inverse.",
                 table=[["graph", "horizontal line test", "restriction needed", "inverse exists?"],
                        ["straight line", "passes", "none", "yes"],
                        ["parabola", "fails", "one side of the vertex", "yes, on the "
                         "restriction"],
                        ["cubic", "passes", "none", "yes"],
                        ["exponential curve", "passes", "none", "yes, the logarithm"],
                        ["reciprocal curve", "passes", "x ≠ 0 already excluded", "yes, itself"],
                        ["step function", "fails everywhere", "no restriction helps", "no"]],
                 notice=["Four of the six graphs passed the test without any restriction.",
                         "The parabola needed a restriction to one side of its vertex.",
                         "The step function could not be rescued by any restriction, because "
                         "it is constant on whole intervals.",
                         "Each inverse was the reflection in the line y = x, so every domain "
                         "and range swapped."],
                 obs="The horizontal line test is a complete criterion, and the algebraic "
                     "version is that equal outputs must force equal inputs.",
                 concl="A function is invertible exactly when it is one-to-one, which the "
                       "horizontal line test decides graphically and the implication "
                       "f(a) = f(b) implies a = b decides algebraically. Where a function "
                       "fails, a restricted domain is stated, and the inverse's graph is the "
                       "reflection of the original in y = x.")),
        dict(id="2.7", title="Mixed practice",
             inquiry_q="Which representation makes the next step easiest?",
             teach=[
                 "Every question about a function can be approached from four directions: the formula, the table, the graph or the machine. Choosing the representation that shows the needed quantity directly is the skill this section practises.",
                 "Transformations, composition and inversion are operations on the rule. Keeping the three operations distinct — and knowing which one a question is asking for — prevents the commonest confusions between f(x) + 2, f(x + 2) and f(f(x)).",
                 "The checks are always available: a transformation is checked against a coordinate rule, a composition is checked against a value, and an inverse is checked by composition. Using a check is faster than finding an error later.",
                 "Mixed practice is where the operation is chosen rather than given, so the reasoning behind the choice is part of what is being practised.",
             ], examples=[
                 dict(q="The function f is defined by f(x) = (3x + 2)/(x − 1). Find f⁻¹ and "
                        "state its domain, and find the value of x for which f(x) = f⁻¹(x).",
                      vis=F("table", [["step", "working", "result"],
                                      ["write y", "y = (3x + 2)/(x − 1)", "—"],
                                      ["clear", "y(x − 1) = 3x + 2", "—"],
                                      ["collect x", "yx − y − 2 = 3x", "—"],
                                      ["factor", "x(y − 3) = y + 2", "—"],
                                      ["inverse", "x = (y + 2)/(y − 3)", "f⁻¹(x) = (x + 2)/(x − 3)"]],
                            caption="Clearing the fraction is the key step."),
                      reasoning="Rearrange to make x the subject, then swap the letters and "
                               "state the domain from the new denominator.",
                      steps=["Write y = (3x + 2)/(x − 1) and multiply by x − 1: "
                             "y(x − 1) = 3x + 2.",
                             "Expand: yx − y = 3x + 2, so yx − 3x = y + 2.",
                             "Factor: x(y − 3) = y + 2, so x = (y + 2)/(y − 3).",
                             "Swap: f⁻¹(x) = (x + 2)/(x − 3), with domain x ≠ 3.",
                             "Setting f(x) = f⁻¹(x) gives (3x + 2)/(x − 1) = (x + 2)/(x − 3); "
                             "cross-multiplying gives 3x² − 7x − 6 = x² + x − 2, so "
                             "2x² − 8x − 4 = 0 and x = 2 ± √6."],
                      ans="f⁻¹(x) = (x + 2)/(x − 3), domain x ≠ 3; f(x) = f⁻¹(x) at x = 2 ± √6",
                      interp="A rational function's inverse is rational again, and the "
                             "excluded value moves from the original denominator to the new "
                             "one."),
                 dict(q="The graph of y = f(x) passes through (2, 5) and (−1, 3). Find the "
                        "corresponding points on y = −f(x − 2) + 1 and on y = f⁻¹(x).",
                      vis=F("table", [["original point", "on y = −f(x − 2) + 1",
                                       "on y = f⁻¹(x)"],
                                      ["(2, 5)", "(4, −4)", "(5, 2)"],
                                      ["(−1, 3)", "(1, −2)", "(3, −1)"]],
                            caption="A transformation and an inverse act differently on points."),
                      reasoning="Apply the coordinate rule of the transformation, and swap the "
                               "coordinates for the inverse.",
                      steps=["For y = −f(x − 2) + 1 the coordinate rule is (x, y) → "
                             "(x + 2, −y + 1).",
                             "So (2, 5) maps to (4, −4) and (−1, 3) maps to (1, −2).",
                             "For y = f⁻¹(x) the coordinates swap, so (2, 5) gives (5, 2) and "
                             "(−1, 3) gives (3, −1).",
                             "Check the first: f(2 − 2) = f(0), and −f(0) + 1 = −5 + 1 = −4, "
                             "which is the image's y-coordinate.",
                             "Note the inverse requires f to be one-to-one, which the two "
                             "points alone cannot establish."],
                      ans="(2, 5) → (4, −4) and (5, 2); (−1, 3) → (1, −2) and (3, −1)",
                      interp="Transformations move points by a rule; inverses swap the "
                             "coordinates. The two operations look similar on a graph and are "
                             "completely different."),
             ], inv=dict(
                 task="Take the function f(x) = 2x − 6. Carry out all of the following and "
                      "record the answer to each: f(5); f⁻¹(5); f(f(5)); the image of (3, 0) "
                      "under y = f(x) + 4; the image of (3, 0) under y = f(x + 4); and the "
                      "image of (3, 0) under y = f⁻¹(x). Then explain which two of the six "
                      "answers are the same and why.",
                 table=[["question", "answer", "operation used"],
                        ["f(5)", "4", "substitution"],
                        ["f⁻¹(5)", "5.5", "inverse"],
                        ["f(f(5))", "2", "composition"],
                        ["image under y = f(x) + 4", "(3, 4)", "vertical translation"],
                        ["image under y = f(x + 4)", "(−1, 0)", "horizontal translation"],
                        ["image under y = f⁻¹(x)", "(0, 3)", "reflection in y = x"]],
                 notice=["f(5) and the vertical translation gave the same y-coordinate, because "
                         "adding 4 after the function and evaluating at the same x differ.",
                         "The horizontal translation moved the point left, not right, because "
                         "the change was inside the bracket.",
                         "The inverse image was the reflection of the original point in "
                         "y = x.",
                         "The composition f(f(5)) was neither of the translations."],
                 obs="Each operation acts on a different part of the rule: substitution "
                     "evaluates, the inverse reverses, and a transformation moves the graph.",
                 concl="The operations on functions are distinguished by where they act: "
                       "inside the bracket changes the input, outside changes the output, and "
                       "composition feeds one function into another. Choosing the right "
                       "operation is the first step in any question about functions.")),
    ],
    practice=dict(
        A=[("2.1.1", "State the domain and range of f(x) = √(x + 3).",
            "Domain x ≥ −3, range f(x) ≥ 0.",
            "The expression under the root must be non-negative.", "F"),
           ("2.1.2", "Given f(x) = 4x − 7, find f(3) and f(−2).",
            "f(3) = 5 and f(−2) = −15.", "Substitute and evaluate.", "F"),
           ("2.1.3", "Given f(x) = x² − 3x + 2, solve f(x) = 0 and state the range.",
            "x = 1 and x = 2; the minimum is −0.25, so the range is f(x) ≥ −0.25.",
            "Complete the square or use the axis of symmetry.", "R"),
           ("2.1.4", "Given f(x) = 2x + 1 and g(x) = x − 4, find f(g(x)) and g(f(x)).",
            "f(g(x)) = 2x − 7 and g(f(x)) = 2x − 3.",
            "The inner function acts first.", "F"),
           ("2.1.5", "Given f(x) = x² and g(x) = x + 3, find f(g(x)) and state its domain.",
            "f(g(x)) = (x + 3)², domain all real x.",
            "Both functions accept every real input.", "F"),
           ("2.1.6", "Given f(x) = 1/x, find f(f(x)) and state the domain.",
            "f(f(x)) = x, domain x ≠ 0.",
            "The reciprocal of the reciprocal is the original.", "R"),
           ("2.1.7", "Describe the transformation from y = x² to y = (x + 4)² − 1.",
            "Translation 4 left and 1 down.",
            "The bracket gives the horizontal change, with the sign reversed.", "F"),
           ("2.1.8", "Describe the transformation from y = √x to y = −3√(x − 2).",
            "Translation 2 right, stretch by factor 3 parallel to the y-axis, reflection in "
            "the x-axis.", "Separate the inside of the bracket from the outside.", "R"),
           ("2.1.9", "Find the inverse of f(x) = (x + 3)/4 and check it by composition.",
            "f⁻¹(x) = 4x − 3; f⁻¹(f(x)) = x and f(f⁻¹(x)) = x.",
            "Rearrange, swap the letters, verify both ways.", "F"),
           ("2.1.10", "For f(x) = x + 3, find f(f(x)) and f(f(f(x))).",
            "x + 6 and x + 9.", "Compose step by step.", "F"),
           ("2.1.11", "Explain why f(x) = x² has no inverse on the real numbers.",
            "Because f(−2) = f(2) = 4, so two inputs share one output and the reversal is "
            "ambiguous.", "Two inputs with the same output block the inverse.", "R"),
           ("2.1.12", "The graph of y = f(x) passes through (1, 4). Find the corresponding "
            "point on y = 2f(x − 3) − 1.",
            "(4, 7).", "Apply the coordinate rule (x, y) → (x + 3, 2y − 1).", "R")],
        B=[("2.2.1", "Investigate whether f(x) = ax + b commutes with g(x) = cx + d for every "
            "choice of a, b, c, d. State and justify a condition.",
            "They commute exactly when ad + b = bc + d; for example two translations, which "
            "have a = c = 1, always commute.",
            "Compare f(g(x)) with g(f(x)) as polynomials.", "C"),
           ("2.2.2", "Conjecture a rule for the number of fixed points of f(x) = ax + b, test "
            "it, and justify it.",
            "One fixed point when a ≠ 1, namely x = b/(1 − a); none or all when a = 1, "
            "depending on b.", "Solve f(x) = x.", "C"),
           ("2.2.3", "Investigate the graphs of f(x) = 1/x and its inverse, and explain what "
            "you notice.",
            "The graphs coincide, because the function is its own inverse: f(f(x)) = x.",
            "Reflect in the line y = x and compare.", "R"),
           ("2.2.4", "Take a function of your own that is not one-to-one. Restrict its domain "
            "so that it becomes one-to-one, and justify why your restriction works.",
            "For example f(x) = x² restricted to x ≥ 0; the restricted function is strictly "
            "increasing, so equal outputs force equal inputs.",
            "Use the horizontal line test on the restricted graph.", "R"),
           ("2.2.5", "Investigate the effect of the transformation y = f(kx) for k = 2, 0.5 "
            "and −1 on the graph of a function of your own.",
            "k = 2 compresses towards the y-axis by factor 2; k = 0.5 stretches away from it "
            "by factor 2; k = −1 reflects in the y-axis.",
            "Track one labelled point.", "R"),
           ("2.2.6", "Conjecture a rule for the inverse of a function of the form "
            "f(x) = (ax + b)/(cx + d), and test it on two examples.",
            "f⁻¹(x) = (b − dx)/(cx − a), valid when ad − bc ≠ 0; for example the inverse of "
            "(2x + 1)/(x − 3) is (1 + 3x)/(x − 2).",
            "Rearrange to make x the subject and swap.", "C"),
           ("2.2.7", "Investigate whether the inverse of a strictly increasing function is "
            "always strictly increasing, and justify.",
            "Yes: if a < b then f⁻¹(a) < f⁻¹(b), because the reverse inequality would force "
            "f to reverse the order.", "Argue by contradiction using the definition.", "C"),
           ("2.2.8", "Investigate the fixed points of f(x) = ax + b and their "
            "number, and justify.",
            "One fixed point when a ≠ 1, namely x = b/(1 − a); when a = 1 "
            "there are none if b ≠ 0 and every point is fixed if b = 0.",
            "Solve f(x) = x.", "R"),
           ("2.2.9", "Conjecture a rule for when f(x) = ax + b commutes with g(x) = "
            "cx + d, and test it.",
            "They commute exactly when ad + b = bc + d, which holds in "
            "particular when a = c, so two stretches of the same factor "
            "commute.",
            "Compare f(g(x)) with g(f(x)) as polynomials.", "C"),
           ("2.2.10", "Investigate the effect of the transformation y = f(kx) on the "
            "graph of a function of your own, and justify.",
            "The graph is stretched parallel to the x-axis by factor 1/k; k "
            "= 2 compresses it towards the y-axis and k = 0.5 stretches it "
            "away.",
            "Track one labelled point through the coordinate rule.", "R"),
           ("2.2.11", "Investigate the graph of y = f(−x) and its relationship to the "
            "graph of y = f(x), and justify.",
            "It is the reflection in the y-axis; where f is an even "
            "function the two graphs coincide, and where f is odd they "
            "coincide after a reflection in the origin.",
            "Apply the coordinate rule (x, y) → (−x, y).", "R"),
           ],
        C=[("2.3.1", "Write a complete solution to finding the inverse of "
            "f(x) = (2x − 1)/(x + 3), including the domain and a composition check.",
            "f⁻¹(x) = (1 + 3x)/(2 − x), domain x ≠ 2; check by composition in both directions.",
            "Clear the fraction, rearrange, swap, verify.", "R"),
           ("2.3.2", "Write a complete solution to the transformation taking y = 1/x to "
            "y = 4/(x − 2) + 1, describing each stage.",
            "Translation 2 right, stretch by factor 4 parallel to the y-axis, translation 1 "
            "up.", "Read the inside of the bracket first, then the outside.", "R"),
           ("2.3.3", "Write a complete solution to f(g(x)) for f(x) = √(x + 1) and "
            "g(x) = x² − 2, including the domain.",
            "f(g(x)) = √(x² − 1), domain x ≤ −1 or x ≥ 1.",
            "The inner output must be a permitted input of the outer function.", "R"),
           ("2.3.4", "Write a complete solution to solving f(x) = f⁻¹(x) for "
            "f(x) = 2x + 5.",
            "2x + 5 = (x − 5)/2 gives 4x + 10 = x − 5, so x = −5.",
            "Equate the function and its inverse and solve.", "R"),
           ("2.3.5", "Write a complete solution to the restriction needed to make "
            "f(x) = x² + 6x + 4 one-to-one, and to finding the inverse on that restriction.",
            "Complete the square: f(x) = (x + 3)² − 5, so restrict to x ≥ −3; then "
            "f⁻¹(x) = −3 + √(x + 5) with domain x ≥ −5.",
            "Locate the axis of symmetry, then invert.", "C"),
           ("2.3.6", "Write a complete solution to the model problem: a van costs 40 currency "
            "units per day plus 0.25 per kilometre. A rival costs 55 per day plus 0.15 per "
            "kilometre. Find the distance at which the costs are equal and describe the "
            "transformation between the models.",
            "40 + 0.25d = 55 + 0.15d gives 0.1d = 15, so d = 150 km; the second model is the "
            "first translated up by 15 and stretched parallel to the x-axis by factor 5/3.",
            "Model each, equate, then read the transformation.", "R"),
           ("2.3.7", "Write a complete solution to sketching the graph of y = f⁻¹(x) given the "
            "graph of y = f(x), explaining why the reflection line is y = x.",
            "Reflect every point of y = f(x) in the line y = x, because the inverse swaps the "
            "coordinates of each point; the domain and range swap too.",
            "The inverse sends outputs back to their inputs.", "R"),
           ("2.3.8", "Write a complete solution to finding the inverse of f(x) = (4x "
            "+ 1)/(2x − 3), with its domain, and checking by composition.",
            "f⁻¹(x) = (3x + 1)/(2x − 4), with domain x ≠ 2; both "
            "compositions give x.",
            "Clear the fraction, rearrange, swap, verify.", "C"),
           ("2.3.9", "Write a complete solution to the transformation taking y = 1/x "
            "to y = 3/(x + 2) − 1, describing each stage.",
            "Translation 2 left, stretch by factor 3 parallel to the "
            "y-axis, translation 1 down.",
            "Read the inside of the bracket first, then the outside.", "R"),
           ("2.3.10", "Write a complete solution to f(g(x)) for f(x) = 1/(x + 2) and "
            "g(x) = x² − 1, including the domain.",
            "f(g(x)) = 1/(x² + 1), with domain all real x.",
            "The inner output must never equal −2, and x² − 1 = −2 has no "
            "real solution.", "R"),
           ("2.3.11", "Write a complete solution to proving that a strictly "
            "decreasing function has a strictly decreasing inverse.",
            "If a < b then f⁻¹(a) > f⁻¹(b), because the reverse inequality "
            "would force f to increase the order, contradicting that f is "
            "decreasing.",
            "Argue by contradiction using the definition of decreasing.", "C"),
           ("2.3.12", "Write a complete solution to the problem: a photocopier "
            "reduces a page to 80 per cent. Model the length after n passes "
            "and find when it is below 10 mm from 297 mm.",
            "L(n) = 297 × 0.8ⁿ; 0.8ⁿ < 10/297 gives n > log(10/297) ÷ log "
            "0.8 ≈ 17.1, so 18 passes.",
            "Apply the decay model and solve with logarithms.", "A"),
           ],
        D=[("2.4.1", "A scientist's instrument reads r and reports R = 1.8r + 32, converting "
            "one scale to another. Find the inverse conversion and explain what it does.",
            "r = (R − 32)/1.8; it converts a reading back to the original scale.",
            "Rearrange and swap.", "A"),
           ("2.4.2", "A photographer's exposure model is E = (a²)/t for aperture a and time t. "
            "Explain the transformation that doubles the exposure without changing the "
            "aperture.",
            "Halving t doubles the exposure, which is a horizontal stretch by factor 0.5 of "
            "the model in t.", "The exposure is inversely proportional to the time.", "A"),
           ("2.4.3", "A language school charges c(n) = 300 + 120n for n weeks. A rival "
            "charges 180 + 150n. Model both, describe the transformation, and find when the "
            "rival becomes cheaper.",
            "c₁ = 300 + 120n and c₂ = 180 + 150n; the rival is cheaper when 120n + 300 > "
            "150n + 180, that is n < 4, so for fewer than 4 weeks.",
            "Model, compare, solve.", "A"),
           ("2.4.4", "A tank drains so that its depth after t minutes is D = 40(0.9)ᵗ cm. "
            "Write the model for s minutes after a start 10 minutes later, and comment on the "
            "difference.",
            "D = 40(0.9)^(s + 10) = 40(0.9)¹⁰(0.9)ˢ ≈ 13.9(0.9)ˢ cm, so the later start "
            "begins at about 13.9 cm instead of 40 cm.",
            "A change of origin is a horizontal translation.", "A"),
           ("2.4.5", "A delivery firm charges f(d) = 8 + 2d for the first 5 km and then "
            "f(d) = 18 + 1.5(d − 5) beyond. Explain why this is not a transformation of a "
            "single linear model.",
            "Because the rate changes, the graph is two line segments with different "
            "gradients; no single stretch and translation connects them.",
            "Compare the gradients of the two pieces.", "A"),
           ("2.4.6", "A factory's output is modelled by P(t) = 200 + 30t units per day. A new "
            "machine adds a fixed 50 units per day and increases the rate by 20 per cent. "
            "Write the new model and describe the transformation.",
            "P(t) = 250 + 36t; a vertical translation of 50 and a vertical stretch by factor "
            "1.2.", "Apply the fixed change then the multiplicative change.", "A"),
           ("2.4.7", "A vaccine's effectiveness is modelled by E(d) = 100(1 − (0.5)^(d/30)) "
            "per cent after d days. Find when effectiveness first exceeds 90 per cent, and "
            "explain what the transformation from (0.5)ᵈ to (0.5)^(d/30) does.",
            "100(1 − (0.5)^(d/30)) > 90 gives (0.5)^(d/30) < 0.1, so d/30 > log(10)/log(2) "
            "≈ 3.32 and d > 99.7 days; the transformation is a horizontal stretch by factor "
            "30, which slows the decay thirtyfold.",
            "Solve the inequality and read the transformation.", "A"),
           ("2.4.8", "A population is modelled by P(t) = 400(1.05)ᵗ. Write the model for s "
            "years after a survey taken 5 years later, and find the population at the new "
            "origin.",
            "P(s) = 400(1.05)^(s + 5) = 400(1.05)⁵(1.05)ˢ ≈ 510.5(1.05)ˢ; the new origin "
            "population is about 510.5.",
            "A change of origin is a horizontal translation.", "A"),
           ("2.4.9", "A company's value is modelled by V(t) = 50000(1.08)ᵗ. After how many "
            "years does it double, and how does the answer change if the rate is 12 per cent?",
            "1.08ᵗ = 2 gives t = log 2 ÷ log 1.08 ≈ 9.01 years; at 12 per cent, "
            "t = log 2 ÷ log 1.12 ≈ 6.12 years.",
            "Take logarithms of both sides.", "A"),
           ("2.4.10", "A student claims that f(x) + 3 and f(x + 3) always give the same graph. "
            "Investigate with two functions of your own and justify a conclusion.",
            "False in general: for f(x) = x², f(x) + 3 = x² + 3 moves the graph up 3, while "
            "f(x + 3) = (x + 3)² moves it left 3. They agree only for functions with special "
            "symmetry, such as f(x) = x.",
            "Test each transformation on a labelled point.", "C"),
           ("2.4.11", "A reservoir's volume is modelled by V(h) = 3h² for depth h in metres. "
            "A second reservoir is twice as wide at every depth. Write its model and describe "
            "the transformation.",
            "V = 6h², a vertical stretch by factor 2; doubling every width doubles the "
            "cross-sectional area and hence the volume.",
            "Area scales with the square of a length, so doubling the width multiplies area "
            "by 4 and volume by 4 for the same depth — the correct model is 12h².",
            "A"),
           ("2.4.12", "A city's temperature is modelled by T(d) = 15 + 8 sin(πd/182.5) for day "
            "d. Explain the meaning of each parameter and find the warmest and coolest days.",
            "15 is the mean temperature, 8 the amplitude, and 182.5 half a year in days; the "
            "warmest day is at d = 91.25 and the coolest at d = 273.75, with 23 °C and 7 °C.",
            "Read the parameters against the parent sine curve.", "A")],
    ),
    assessment=[
        dict(title="A1 · The recalibrated sensor",
             text="A sensor outputs s and a model converts it to a reading R = 2.5s + 12. The "
                  "sensor is recalibrated so that its output is 4 higher than before for the "
                  "same physical quantity. Write the new model, describe the transformation "
                  "between the two models, and find the inverse of the new model, stating its "
                  "domain and range.",
             note="Criteria A and C · identify which representation changes and set out the "
                  "inverse with its domain."),
        dict(title="A2 · The two subscription plans",
             text="Plan A costs 15 currency units per month plus 2 per stream. Plan B costs 9 "
                  "per month plus 3 per stream. Model both, describe the transformation "
                  "between them, find the number of streams at which they cost the same, and "
                  "explain which plan is better for a household watching 8 streams a month.",
             note="Criteria A and D · model both plans, solve the crossing, and justify the "
                  "recommendation with the model."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of change, "
        "representation and patterns appear in your work?",
        "How is the global context of scientific and technical innovation, and its exploration "
        "of models that translate a measurement into a prediction, visible in the "
        "investigations and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of a graphical representation of a function, and what would "
        "you still like to ask?",
    ],
    review=dict(
        ideas=["A function is a rule with a stated domain that gives exactly one output per "
               "input.",
               "f(x) + k translates vertically; f(x − a) translates horizontally by a.",
               "A stretch parallel to the y-axis has factor k; one parallel to the x-axis "
               "divides the input by k.",
               "The composite f(g(x)) applies g first.",
               "The domain of a composite is where the inner output is a permitted input of "
               "the outer function.",
               "An inverse exists exactly when the function is one-to-one.",
               "The horizontal line test decides invertibility; algebraically, f(a) = f(b) "
               "must force a = b.",
               "The graph of an inverse is the reflection in the line y = x."],
        vocab=["function", "domain", "range", "mapping", "one-to-one", "composite", "inner "
               "function", "translation", "reflection", "stretch", "inverse function",
               "horizontal line test", "fixed point", "coordinate rule"],
        mixed=[("2.R1", "Find the domain of f(x) = 1/(x² − 9)."),
               ("2.R2", "Given f(x) = x² + 1 and g(x) = 2x − 3, find f(g(2))."),
               ("2.R3", "Describe the transformation from y = x³ to y = −(x − 2)³ + 5."),
               ("2.R4", "Find the inverse of f(x) = 5 − 2x and check it."),
               ("2.R5", "Explain why f(x) = x³ − 3x is not one-to-one on the real numbers."),
               ("2.R6", "The point (2, 7) lies on y = f(x). Find its image on "
                "y = −f(2x) + 1.")],
    ),
    projects=dict(
        service=[("Community need", "Public measurement instruments are recalibrated without "
                                    "the conversion being published."),
                 ("Mathematical connection", "Functions, inverses and transformations."),
                 ("Proposed action", "Take three instrument conversions in your community, "
                                     "find the inverse of each, and publish how to convert "
                                     "back."),
                 ("Expected impact", "A reader can convert a reading in either direction."),
                 ("Student reflection", "Record the conversions, their inverses and what you "
                                        "found.")],
        community=[("Project idea", "A conversion audit of the school's measurement "
                                    "instruments."),
                   ("Need", "Scales, thermometers and timers report in units nobody has "
                            "converted back."),
                   ("Research question", "Which conversions does the school rely on, and can "
                                         "each be reversed exactly?"),
                   ("Mathematics", "Functions, inverses and transformations."),
                   ("Action or outcome", "A one-page conversion card with both directions."),
                   ("Beneficiaries", "Everyone who reads a school instrument."),
                   ("Evidence", "The conversion cards and the inverses you derived.")],
        personal=[("Personal interest", "Cooking, sport, music or gaming."),
                  ("Learning goal", "To convert a quantity you care about in both directions "
                                    "and explain which representation you used."),
                  ("Product or outcome", "A conversion card with a graph and its inverse."),
                  ("Mathematics", "Functions, inverses and transformations."),
                  ("Process", "Model a conversion, invert it, and check by composition."),
                  ("Evidence", "The card and the composition checks.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=3, title="Exponential and Logarithmic Functions",
    key="Change", related=["Equivalence", "Patterns", "Representation"],
    context="Scientific and technical innovation",
    exploration="populations, medicines, sound and seismic energy",
    inquiry=("Exponential change is repeated multiplication; logarithms are the inverse "
             "language that turns multiplication into addition and makes the rate visible."),
    atl=("Critical thinking",
         "In order for a student to judge whether a growth claim is plausible, students must "
         "compare a linear and an exponential model of the same situation, identify the "
         "quantity that changes multiplicatively, and justify the choice of model."),
    standfirst="Some quantities change by adding a fixed amount and some by multiplying by a "
               "fixed factor. Logarithms are the inverse language of multiplication, and they "
               "turn a multiplicative relationship into an additive one.",
    engage="A population doubles every 8 years. A student models it as 8 times the initial "
           "population after 64 years. Another models it as 2 to the power 8. Which is right, "
           "and why does the difference matter for a forecast a century ahead?",
    questions=[("Factual", "What do the logarithm laws say, and how is a logarithm defined?"),
               ("Conceptual", "Why does an exponential model outgrow every linear model, and "
                              "what does a logarithm measure?"),
               ("Debatable", "If a model fits the past decade exactly, is it a better model "
                             "than one that fits approximately and states its limits?")],
    application_lede="These tasks use exponential and logarithmic models. State the base and "
                     "the units of the rate, check the model against one known value, and "
                     "comment on the domain of any prediction.",
    projects_lede="A rate is only meaningful with its base and its time unit. Choose the "
                  "representation that makes the rate visible, and say what the model cannot "
                  "predict.",
    sections=[
        dict(id="3.1", title="Exponential growth and decay",
             inquiry_q="Why does repeated multiplication outgrow repeated addition?",
             teach=[
                 "An exponential model has the form N = N₀bᵗ, where N₀ is the initial quantity, b is the base or multiplier per unit time, and t is the time. The base is the whole story: b > 1 gives growth, 0 < b < 1 gives decay, and b = 1 gives no change at all.",
                 "A constant multiplicative rate means equal percentage changes in equal time intervals. This is what distinguishes exponential change from linear change, where equal absolute changes occur in equal intervals instead.",
                 "The graph of an exponential model is a curve with a horizontal asymptote. Growth curves steepen; decay curves flatten towards the asymptote; neither ever reaches it in finite time.",
                 "Any exponential model can be written with any positive base, because bᵗ = e^(kt) for k = ln b. The equivalence of the two forms is exact, and choosing a base is choosing a representation rather than changing the model.",
             ], examples=[
                 dict(q="A population of 400 bacteria doubles every 3 hours. Write the model, "
                        "find the population after 10 hours, and find when it reaches 25 600.",
                      vis=F("table", [["time (h)", "model", "population"],
                                      ["0", "400 × 2⁰", "400"],
                                      ["3", "400 × 2¹", "800"],
                                      ["6", "400 × 2²", "1600"],
                                      ["9", "400 × 2³", "3200"],
                                      ["12", "400 × 2⁴", "6400"]],
                            caption="Doubling every 3 hours means the exponent counts "
                                    "three-hour periods."),
                      reasoning="The multiplier per period is 2 and the period is 3 hours, so "
                               "the exponent is t/3; then solve for t by equating.",
                      steps=["The model is N(t) = 400 × 2^(t/3).",
                             "After 10 hours: N(10) = 400 × 2^(10/3) = 400 × 2^3.333.",
                             "2^3.333 ≈ 10.08, so N(10) ≈ 4032 bacteria.",
                             "Set 400 × 2^(t/3) = 25 600, so 2^(t/3) = 64.",
                             "Since 64 = 2⁶, t/3 = 6 and t = 18 hours."],
                      ans="N(t) = 400 × 2^(t/3); about 4032 after 10 hours; 25 600 after 18 "
                          "hours",
                      interp="The exponent counts periods, not hours, and confusing the two is "
                             "the commonest error in exponential modelling."),
                 dict(q="A car loses 15 per cent of its value each year. Write the model and "
                        "find its value after 5 years if it cost 24 000.",
                      vis=F("table", [["year", "multiplier", "value"],
                                      ["0", "0.85⁰", "24000"],
                                      ["1", "0.85¹", "20400"],
                                      ["2", "0.85²", "17340"],
                                      ["3", "0.85³", "14739"],
                                      ["5", "0.85⁵", "10675"]],
                            caption="A loss of 15 per cent is a multiplier of 0.85."),
                      reasoning="A percentage loss is a multiplier below 1, and the model "
                               "compounds it each year.",
                      steps=["Losing 15 per cent leaves 85 per cent, so the multiplier is 0.85.",
                             "The model is V(t) = 24000 × 0.85ᵗ.",
                             "After 5 years: V(5) = 24000 × 0.85⁵.",
                             "0.85⁵ ≈ 0.4437, so V(5) ≈ 10 675.",
                             "The value never reaches zero in finite time, because 0.85ᵗ > 0 "
                             "for every t."],
                      ans="V(t) = 24000 × 0.85ᵗ; about 10 675 after 5 years",
                      interp="A decay model with a positive base is always positive, so the "
                             "asymptote at zero is a limit rather than a value that is "
                             "reached."),
             ], inv=dict(
                 task="Take 1000 currency units. Model it under three schemes: simple interest "
                      "at 5 per cent per year, compound interest at 5 per cent per year, and "
                      "compound interest at 5 per cent per half-year. Record the value after "
                      "1, 2, 5 and 10 years for each, and then say which two agree and why "
                      "the third is different.",
                 table=[["year", "simple", "compound yearly", "compound half-yearly"],
                        ["1", "1050", "1050", "1050.63"],
                        ["2", "1100", "1102.50", "1105.12"],
                        ["5", "1250", "1276.28", "1280.08"],
                        ["10", "1500", "1628.89", "1638.62"],
                        ["20", "2000", "2653.30", "2685.06"]],
                 notice=["Simple interest added the same amount every year, so its graph was a "
                         "straight line.",
                         "Compound interest added a growing amount, so its graph curved "
                         "upwards.",
                         "Compounding twice a year gave slightly more, because interest earned "
                         "interest sooner.",
                         "The gap between the schemes widened every year, which is the "
                         "signature of exponential against linear change."],
                 obs="Simple interest is a linear model and compound interest is an "
                     "exponential one, and the exponential model pulls ahead without bound.",
                 concl="An exponential model N = N₀bᵗ compounds a multiplier b for each unit "
                       "of time, so equal percentage changes occur in equal intervals. The "
                       "base b is the multiplier, and the exponent counts units of time, not "
                       "the amount of the quantity. Here 1000 × 1.05ᵗ is the yearly model and "
                       "1000 × 1.025^(2t) the half-yearly one.")),
        dict(id="3.2", title="The number e and continuous change",
             inquiry_q="What does it mean for change to be continuous rather than periodic?",
             teach=[
                 "Compounding more and more often raises the accumulated value towards a limit, and that limit is the number e ≈ 2.71828. A nominal annual rate r compounded continuously gives a growth factor of eʳ per year.",
                 "The continuous model N = N₀eᵏᵗ has rate k per unit time. Any base-b model can be rewritten in this form with k = ln b, and the two forms describe exactly the same change.",
                 "The natural logarithm ln is the logarithm to base e, and it is the inverse of the exponential function with base e. It is the convenient logarithm for continuous models for the same reason that e is the convenient base.",
                 "Continuous models appear wherever the rate of change is proportional to the quantity: populations, radioactive decay, cooling, and the accumulation of interest in a limit.",
             ], examples=[
                 dict(q="A population is modelled by P(t) = 400(1.05)ᵗ. Write the model for s "
                        "years in continuous form, and find the continuous rate.",
                      vis=F("table", [["representation", "model", "rate"],
                                      ["base form", "400(1.05)ᵗ", "5% per year"],
                                      ["continuous", "400eᵏᵗ", "k = ln 1.05"],
                                      ["value of k", "k ≈ 0.04879", "4.879% per year"]],
                            caption="The same change, described with a different base."),
                      reasoning="Match the two forms by setting eᵏ = 1.05 and taking natural "
                               "logarithms.",
                      steps=["The model is P(t) = 400(1.05)ᵗ.",
                             "Write 1.05ᵗ = eᵏᵗ, so eᵏ = 1.05.",
                             "Taking natural logarithms gives k = ln 1.05 ≈ 0.04879.",
                             "So the continuous model is P(t) = 400e^(0.04879t).",
                             "Check: e^(0.04879 × 1) ≈ 1.05, as required."],
                      ans="P(t) = 400e^(0.04879t), continuous rate about 4.879 per cent per "
                          "year",
                      interp="The two models are the same function in different clothes, and "
                             "the continuous rate is slightly below the nominal rate."),
                 dict(q="A substance decays so that 30 per cent remains after 5 hours. Find "
                        "the half-life, and state the continuous model.",
                      vis=F("table", [["time (h)", "fraction remaining", "comment"],
                                      ["0", "1", "start"],
                                      ["5", "0.30", "given"],
                                      ["10", "0.09", "0.30²"],
                                      ["t", "0.50", "half remains"]],
                            caption="Each equal interval multiplies the fraction by the same "
                                    "factor."),
                      reasoning="Find the multiplier per hour from the given data, then solve "
                               "for the time at which half remains.",
                      steps=["Let the model be N(t) = N₀bᵗ. Then b⁵ = 0.30, so "
                             "b = 0.30^(1/5) ≈ 0.7860.",
                             "The continuous form is N = N₀eᵏᵗ with k = ln 0.7860 ≈ −0.2408.",
                             "Half remains when bᵗ = 0.5, so t = ln 0.5 ÷ ln 0.7860.",
                             "ln 0.5 ≈ −0.6931 and ln 0.7860 ≈ −0.2408, so t ≈ 2.88 hours.",
                             "The half-life is about 2.88 hours."],
                      ans="half-life about 2.88 hours; N = N₀e^(−0.2408t)",
                      interp="The half-life is independent of the starting quantity, which is "
                             "why it is the standard way to report a decay rate."),
             ], inv=dict(
                 task="Investigate 1000 currency units at a nominal 10 per cent per year, "
                      "compounded annually, half-yearly, quarterly, monthly, daily and "
                      "continuously. Record the value after one year for each, and describe "
                      "the pattern in the extra amounts as the compounding becomes more "
                      "frequent.",
                 table=[["compounding", "periods per year", "value after 1 year", "gain over "
                                "annual"],
                        ["annually", "1", "1100.00", "0"],
                        ["half-yearly", "2", "1102.50", "2.50"],
                        ["quarterly", "4", "1103.81", "3.81"],
                        ["monthly", "12", "1104.71", "4.71"],
                        ["daily", "365", "1105.16", "5.16"],
                        ["continuously", "—", "1105.17", "5.17"]],
                 notice=["Each increase in frequency raised the final value, but by less each "
                         "time.",
                         "The daily and continuous values differed by less than one hundredth "
                         "of a currency unit.",
                         "The limiting value is 1000e^0.1 ≈ 1105.17, which is the continuous "
                         "model.",
                         "The gains formed a decreasing sequence, which is the signature of "
                         "convergence."],
                 obs="More frequent compounding raises the accumulated value towards a limit, "
                     "and the limit is reached by the continuous model.",
                 concl="Compounding a nominal rate r in n periods per year gives "
                       "1000(1 + r/n)ⁿ, and as n grows this approaches 1000eʳ. The number e is "
                       "the limit of (1 + 1/n)ⁿ, and the continuous model N = N₀eᵏᵗ is the "
                       "limit of every periodic model with the same annual rate.")),
        dict(id="3.3", title="Logarithms and their laws",
             inquiry_q="Why do logarithms turn multiplication into addition?",
             teach=[
                 "The logarithm to base b, written log_b, is the inverse of the exponential function with base b. The statement log_b x = y means exactly bʸ = x, and the two statements are equivalent ways of describing the same relationship between x and y.",
                 "The three logarithm laws follow from the index laws: log_b(xy) = log_b x + log_b y, log_b(x/y) = log_b x − log_b y, and log_b(xᵏ) = k log_b x. Each is the index law read backwards.",
                 "The change of base formula log_b a = log a ÷ log b allows any logarithm to be computed from any other. It is the reason a calculator with only two logarithm buttons is sufficient.",
                 "A logarithm is an exponent, so its laws are the laws of exponents. Treating a logarithm as a number to be manipulated rather than as a label is what makes the laws usable.",
             ], examples=[
                 dict(q="Solve log₂(x) + log₂(x − 2) = 3.",
                      vis=F("table", [["step", "working", "result"],
                                      ["combine", "log₂(x(x − 2)) = 3", "product law"],
                                      ["remove log", "x(x − 2) = 2³", "definition"],
                                      ["expand", "x² − 2x = 8", "—"],
                                      ["solve", "x² − 2x − 8 = 0", "x = 4 or x = −2"],
                                      ["check", "x = −2 makes log₂(−2) undefined", "rejected"]],
                            caption="The domain check rejects one of the two roots."),
                      reasoning="Combine with the product law, remove the logarithm with its "
                               "definition, then check the domain.",
                      steps=["Both logarithms require a positive argument, so x > 0 and "
                             "x − 2 > 0, giving x > 2.",
                             "Combine: log₂(x(x − 2)) = 3.",
                             "Remove the logarithm: x(x − 2) = 2³ = 8.",
                             "So x² − 2x − 8 = 0, giving (x − 4)(x + 2) = 0.",
                             "x = 4 or x = −2; only x = 4 satisfies x > 2."],
                      ans="x = 4",
                      interp="The domain restriction comes before the algebra, and it is what "
                             "rejects the extraneous root."),
                 dict(q="Given log 2 ≈ 0.3010 and log 3 ≈ 0.4771, find log 12 and log(2/3) "
                        "without a calculator.",
                      vis=F("table", [["quantity", "in terms of log 2 and log 3", "value"],
                                      ["12", "2 log 2 + log 3", "0.6021 + 0.4771"],
                                      ["2/3", "log 2 − log 3", "0.3010 − 0.4771"],
                                      ["8", "3 log 2", "0.9030"],
                                      ["0.5", "−log 2", "−0.3010"]],
                            caption="The laws break every number into primes."),
                      reasoning="Factorise into primes and apply the laws, using the given "
                               "values.",
                      steps=["12 = 4 × 3 = 2² × 3, so log 12 = 2 log 2 + log 3.",
                             "log 12 = 2(0.3010) + 0.4771 = 0.6021 + 0.4771 = 1.0791.",
                             "2/3 has log 2 − log 3 = 0.3010 − 0.4771 = −0.1761.",
                             "Check: 10^1.0791 ≈ 12, and 10^(−0.1761) ≈ 0.667.",
                             "The laws turned two given values into many others."],
                      ans="log 12 ≈ 1.0791 and log(2/3) ≈ −0.1761",
                      interp="Logarithms of composite numbers are sums of logarithms of "
                             "primes, which is why logarithm tables were short."),
             ], inv=dict(
                 task="Build a table of log₂(n) for n = 1, 2, 4, 8, 16, 32, 3, 6, 12 and 24, "
                      "using only log₂ 2 = 1 and log₂ 3 ≈ 1.585. Then use your table to "
                      "evaluate log₂ 48, log₂(1/6) and log₂ 9, and state the law you used in "
                      "each case.",
                 table=[["n", "factorisation", "log₂ n", "law used"],
                        ["1", "2⁰", "0", "definition"],
                        ["2", "2¹", "1", "given"],
                        ["4", "2²", "2", "power law"],
                        ["8", "2³", "3", "power law"],
                        ["16", "2⁴", "4", "power law"],
                        ["32", "2⁵", "5", "power law"],
                        ["3", "3¹", "1.585", "given"],
                        ["6", "2 × 3", "2.585", "product law"],
                        ["12", "4 × 3", "3.585", "product law"],
                        ["24", "8 × 3", "4.585", "product law"]],
                 notice=["Every value came from adding or subtracting the two given values.",
                         "The power law multiplied by the exponent, so log₂ 16 = 4 log₂ 2 = 4.",
                         "The product law added, so log₂ 6 = log₂ 2 + log₂ 3.",
                         "log₂ 1 was 0 because 2⁰ = 1, and that single fact made every "
                         "quotient work."],
                 obs="The logarithm laws are the index laws read backwards, and two values "
                     "generate a whole table.",
                 concl="The logarithm to base b is the inverse of bˣ, so log_b x = y means "
                       "exactly bʸ = x. Its laws — the product, quotient and power laws — are "
                       "the index laws read backwards, and they turn multiplication into "
                       "addition, division into subtraction and powers into multiplication. "
                       "Here log₂ 48 = log₂(16 × 3) = 4 + 1.585 = 5.585, "
                       "log₂(1/6) = −2.585 and log₂ 9 = 2 × 1.585 = 3.170.")),
        dict(id="3.4", title="Solving exponential equations",
             inquiry_q="When can an exponential equation be solved, and what is the method?",
             teach=[
                 "If both sides of an exponential equation can be written as powers of the same base, the exponents can be equated, because a one-to-one power function has one input per output.",
                 "If the bases cannot be matched, take logarithms of both sides. The power law brings the unknown down from the exponent, which converts the exponential equation into a linear or quadratic one.",
                 "Every solution must be checked in the original equation, because taking logarithms requires positive arguments. A candidate that makes an argument non-positive is extraneous.",
                 "Equations with the unknown in two places, such as 2ˣ = 3x + 1, cannot be solved algebraically. They are solved numerically, and a graph or an iterative method gives the answer to any required accuracy.",
             ], examples=[
                 dict(q="Solve 3^(2x) = 81.",
                      vis=F("table", [["step", "working", "result"],
                                      ["same base", "81 = 3⁴", "—"],
                                      ["equate", "2x = 4", "—"],
                                      ["solve", "x = 2", "—"],
                                      ["check", "3⁴ = 81", "valid"]],
                            caption="Matching the base turns the equation into a linear one."),
                      reasoning="Write both sides as powers of 3, then equate the exponents.",
                      steps=["81 = 3⁴, so the equation becomes 3^(2x) = 3⁴.",
                             "Equal powers of the same base have equal exponents: 2x = 4.",
                             "So x = 2.",
                             "Check: 3^(2 × 2) = 3⁴ = 81."],
                      ans="x = 2",
                      interp="Matching bases is always the first move, because it is exact and "
                             "avoids rounding."),
                 dict(q="Solve 5^(x) = 250, giving the answer to three significant figures.",
                      vis=F("table", [["step", "working", "result"],
                                      ["take logs", "x log 5 = log 250", "power law"],
                                      ["rearrange", "x = log 250 ÷ log 5", "—"],
                                      ["evaluate", "x ≈ 2.3979 ÷ 0.6990", "—"],
                                      ["answer", "x ≈ 3.43", "3 s.f."]],
                            caption="Taking logarithms brings the exponent down."),
                      reasoning="Take logarithms of both sides, apply the power law, and "
                               "rearrange.",
                      steps=["Take logarithms: log(5ˣ) = log 250.",
                             "Apply the power law: x log 5 = log 250.",
                             "So x = log 250 ÷ log 5.",
                             "log 250 ≈ 2.3979 and log 5 ≈ 0.6990, so x ≈ 3.430.",
                             "Check: 5^3.43 ≈ 249.9, which is close to 250."],
                      ans="x ≈ 3.43",
                      interp="Any base of logarithm works, because the change of base formula "
                             "cancels the base out of the quotient."),
             ], inv=dict(
                 task="Solve each of these by first trying to match bases, and then by taking "
                      "logarithms: 2^(x+1) = 32; 4ˣ = 8^(x−1); 3^(2x−1) = 27; and 10ˣ = 7. "
                      "Record which method you used for each and why, and check every answer.",
                 table=[["equation", "method", "answer", "check"],
                        ["2^(x+1) = 32", "match bases", "x = 4", "2⁵ = 32"],
                        ["4ˣ = 8^(x−1)", "match bases", "x = 3", "4³ = 64, 8² = 64"],
                        ["3^(2x−1) = 27", "match bases", "x = 2", "3³ = 27"],
                        ["10ˣ = 7", "logarithms", "x ≈ 0.845", "10^0.845 ≈ 7"]],
                 notice=["Three of the four equations yielded to matching bases, because the "
                         "numbers were all powers of small integers.",
                         "The fourth needed logarithms, because 7 is not a power of 10.",
                         "Matching bases gave exact answers; logarithms gave approximations.",
                         "Every answer passed the substitution check."],
                 obs="Matching bases is exact and should always be tried first; logarithms "
                     "are the general method.",
                 concl="An exponential equation is solved by matching bases when that is "
                       "possible, and otherwise by taking logarithms of both sides and using "
                       "the power law. The check is substitution into the original equation, "
                       "and it also confirms that every logarithm taken had a positive "
                       "argument.")),
        dict(id="3.5", title="Modelling with logarithms",
             inquiry_q="What does a logarithmic scale show that a linear scale cannot?",
             teach=[
                 "A logarithmic scale compresses equal ratios into equal distances, so a quantity that grows by a constant factor appears as a straight line and its patterns become readable. This is why logarithmic axes are used for anything spanning many orders of magnitude.",
                 "Semi-log graph paper has a linear axis and a logarithmic one. Data that plot as a straight line on semi-log paper are exponential, and the gradient of the line is the continuous rate.",
                 "The Richter scale for earthquakes, the decibel scale for sound and the pH scale for acidity are all logarithmic. A difference of one unit is a fixed ratio, not a fixed difference, which is why the scales are described as logarithmic.",
                 "Taking logarithms of both variables of a power law y = kxⁿ gives log y = n log x + log k, a straight line. Log-log graph paper therefore identifies power laws, just as semi-log paper identifies exponential ones.",
             ], examples=[
                 dict(q="An earthquake of magnitude 6 releases how many times the energy of one "
                        "of magnitude 4, if energy is proportional to 10^(1.5M)?",
                      vis=F("table", [["magnitude", "energy factor", "ratio to M = 4"],
                                      ["4", "10⁶", "1"],
                                      ["5", "10^7.5", "31.6"],
                                      ["6", "10⁹", "1000"],
                                      ["7", "10^10.5", "31623"]],
                            caption="One step of magnitude is a factor of about 31.6 in "
                                    "energy."),
                      reasoning="Form the ratio of the energy factors and simplify using the "
                               "index laws.",
                      steps=["Energy is proportional to 10^(1.5M).",
                             "The ratio for M = 6 against M = 4 is 10^(1.5 × 6) ÷ "
                             "10^(1.5 × 4).",
                             "By the quotient law this is 10^(9 − 6) = 10³.",
                             "So a magnitude 6 earthquake releases 1000 times the energy.",
                             "One step of magnitude is a factor of 10^1.5 ≈ 31.6."],
                      ans="1000 times",
                      interp="The magnitude scale is logarithmic, so differences in magnitude "
                             "are ratios in energy, and the ratios grow very fast."),
                 dict(q="Sound intensity level is L = 10 log(I/I₀) decibels. Find the ratio of "
                        "intensities for levels of 60 dB and 40 dB.",
                      vis=F("table", [["level (dB)", "log term", "intensity ratio"],
                                      ["40", "4", "10⁴"],
                                      ["50", "5", "10⁵"],
                                      ["60", "6", "10⁶"],
                                      ["70", "7", "10⁷"]],
                            caption="Twenty decibels is a factor of 100 in intensity."),
                      reasoning="Subtract the two level equations and use the quotient law.",
                      steps=["L₁ − L₂ = 10 log(I₁/I₀) − 10 log(I₂/I₀) = 10 log(I₁/I₂).",
                             "So 60 − 40 = 10 log(I₁/I₂), giving 20 = 10 log(I₁/I₂).",
                             "Hence log(I₁/I₂) = 2, so I₁/I₂ = 10² = 100.",
                             "The 60 dB sound is 100 times as intense as the 40 dB sound.",
                             "Note that a 20 dB difference sounds roughly four times as loud, "
                             "because loudness is not logarithmic in the same way."],
                      ans="100 times",
                      interp="A difference on a logarithmic scale is a ratio, and the ratio is "
                             "found by dividing the difference by the scale factor."),
             ], inv=dict(
                 task="Take a quantity that doubles every day: 1, 2, 4, 8, 16, 32, 64. Plot "
                      "the values on a linear axis and on a logarithmic axis, and describe "
                      "what each plot shows. Then take the first seven square numbers and "
                      "plot them on a log-log axis, and describe what you see.",
                 table=[["day", "doubling quantity", "log₁₀ of it", "square", "log₁₀ of square"],
                        ["0", "1", "0", "1", "0"],
                        ["1", "2", "0.301", "4", "0.602"],
                        ["2", "4", "0.602", "9", "0.954"],
                        ["3", "8", "0.903", "16", "1.204"],
                        ["4", "16", "1.204", "25", "1.398"],
                        ["5", "32", "1.505", "36", "1.556"],
                        ["6", "64", "1.806", "49", "1.690"]],
                 notice=["On a linear axis the doubling quantity curved steeply upwards.",
                         "On a logarithmic axis the same values lay on a straight line, "
                         "because each step multiplied by the same factor.",
                         "The squares also lay on a straight line on the log-log axis, with "
                         "gradient 2.",
                         "The gradient of a log-log line is the power in a power law."],
                 obs="A straight line on semi-log paper means exponential change, and a "
                     "straight line on log-log paper means a power law.",
                 concl="A logarithmic scale compresses equal ratios into equal distances, so "
                       "multiplicative change appears as a straight line and the gradient "
                       "measures the rate. Taking logarithms of both variables turns an "
                       "exponential law into a linear one and a power law into a line whose "
                       "gradient is the power. This is why the Richter, decibel and pH scales "
                       "are logarithmic.")),
        dict(id="3.6", title="Investigation: how many digits?",
             inquiry_q="How many digits does a large power have, and can it be predicted?",
             teach=[
                 "A positive integer with n digits lies between 10ⁿ⁻¹ and 10ⁿ, so the number of digits of a number x is the least integer strictly greater than log₁₀x. Counting digits is therefore a logarithm problem.",
                 "The number of digits of bⁿ is the whole part of n log₁₀b, plus one. The fractional part of n log₁₀b determines the leading digits, because 10 raised to that fractional part lies between 1 and 10.",
                 "This is the basis of floating-point representation in every computer: a number is stored as a mantissa between 1 and 10 and an exponent, which is exactly the decomposition that logarithms describe.",
                 "The leading-digit pattern of powers is not uniform. Benford's law observes that in many real data sets the leading digit is 1 far more often than 9, and the logarithmic distribution explains it.",
             ], examples=[
                 dict(q="How many digits does 2¹⁰⁰ have?",
                      vis=F("table", [["n", "2ⁿ", "n log₁₀2", "digits"],
                                      ["10", "1024", "3.01", "4"],
                                      ["20", "1048576", "6.02", "7"],
                                      ["50", "≈1.126 × 10¹⁵", "15.05", "16"],
                                      ["100", "≈1.267 × 10³⁰", "30.10", "31"]],
                            caption="The digit count is the whole part of n log 2, plus one."),
                      reasoning="Compute n log₁₀2, take its whole part and add one.",
                      steps=["log₁₀2 ≈ 0.30103.",
                             "So 100 log₁₀2 ≈ 30.103.",
                             "The whole part is 30, and the number of digits is 30 + 1 = 31.",
                             "Check: 2¹⁰⁰ ≈ 1.2677 × 10³⁰, which indeed has 31 digits.",
                             "The fractional part 0.103 gives the leading digits, because "
                             "10^0.103 ≈ 1.27."],
                      ans="31 digits",
                      interp="One multiplication and one truncation answer a question about a "
                             "number with 31 digits."),
                 dict(q="How many digits does 7²⁰ have, and what are its leading digits?",
                      vis=F("table", [["quantity", "value", "use"],
                                      ["log₁₀7", "≈ 0.84510", "given"],
                                      ["20 log₁₀7", "≈ 16.902", "whole part 16"],
                                      ["digits", "17", "16 + 1"],
                                      ["fractional part", "0.902", "10^0.902 ≈ 7.98"]],
                            caption="The whole part counts digits; the fraction gives the "
                                    "leading digits."),
                      reasoning="Separate n log b into its whole part and its fractional part.",
                      steps=["log₁₀7 ≈ 0.84510.",
                             "20 log₁₀7 ≈ 16.902.",
                             "The whole part is 16, so the number of digits is 17.",
                             "The fractional part is 0.902, and 10^0.902 ≈ 7.98.",
                             "So 7²⁰ begins with the digits 79, and is about 7.98 × 10¹⁶."],
                      ans="17 digits, beginning with 79",
                      interp="The same calculation that counts the digits also reveals the "
                             "leading ones, which is how a computer stores a number."),
             ], inv=dict(
                 task="Investigate the number of digits of 2ⁿ for n = 1 to 12. Form a "
                      "conjecture and justify it. Then investigate the leading digit of 2ⁿ "
                      "over the same range, and describe the pattern you find.",
                 table=[["n", "2ⁿ", "n log₁₀2", "digits", "leading digit"],
                        ["1", "2", "0.301", "1", "2"],
                        ["2", "4", "0.602", "1", "4"],
                        ["3", "8", "0.903", "1", "8"],
                        ["4", "16", "1.204", "2", "1"],
                        ["5", "32", "1.505", "2", "3"],
                        ["6", "64", "1.806", "2", "6"],
                        ["7", "128", "2.107", "3", "1"],
                        ["8", "256", "2.408", "3", "2"],
                        ["9", "512", "2.709", "3", "5"],
                        ["10", "1024", "3.010", "4", "1"],
                        ["11", "2048", "3.311", "4", "2"],
                        ["12", "4096", "3.612", "4", "4"]],
                 notice=["The digit count increased by 1 about every 3.32 powers.",
                         "The increases happened at n = 4, 7, 10 and 12, which is not a fixed "
                         "period.",
                         "The leading digit cycled through 2, 4, 8, 1, 3, 6, 1, 2, 5, 1, 2, 4.",
                         "The leading digit was 1 at n = 4, 7 and 10, more often than any "
                         "other digit."],
                 obs="The digit count grows linearly in n with slope log₁₀2, and the leading "
                     "digit cycles irregularly.",
                 concl="The number of digits of bⁿ is the whole part of n log₁₀b, plus one, "
                       "because bⁿ lies between 10ᵏ and 10ᵏ⁺¹ where k is that whole part. The "
                       "fractional part of n log₁₀b gives the leading digits, and its "
                       "distribution explains why small leading digits are common — the "
                       "observation behind Benford's law.")),
        dict(id="3.7", title="Mixed practice",
             inquiry_q="Which representation of the change makes the rate visible?",
             teach=[
                 "Every exponential question can be approached in three ways: match the bases, take logarithms, or read the rate off a model. The method is chosen by the shape of the question, and choosing well saves work.",
                 "The base form N = N₀bᵗ and the continuous form N = N₀eᵏᵗ are equivalent representations of the same change, related by k = ln b. Converting between them is a routine step, not a change of model.",
                 "Logarithm laws are used to solve equations, to simplify expressions and to interpret scales. In each case the underlying move is the same: turn a multiplicative statement into an additive one.",
                 "Mixed practice is where the representation is chosen rather than given, so the reasoning behind the choice is part of what is being practised.",
             ], examples=[
                 dict(q="A town's population grows from 12 000 to 15 000 in 4 years. Assuming "
                        "exponential growth, find the annual growth rate and predict the "
                        "population after a further 6 years.",
                      vis=F("table", [["step", "working", "result"],
                                      ["model", "15000 = 12000 b⁴", "—"],
                                      ["base", "b⁴ = 1.25", "—"],
                                      ["rate", "b = 1.25^0.25 ≈ 1.0574", "5.74% per year"],
                                      ["prediction", "15000 × 1.0574⁶ ≈ 21090", "—"]],
                            caption="Two data points determine an exponential model."),
                      reasoning="Use the two known values to find the base, then extrapolate.",
                      steps=["The model is P(t) = 12000 bᵗ and P(4) = 15000.",
                             "So b⁴ = 15000/12000 = 1.25.",
                             "Hence b = 1.25^(1/4) ≈ 1.0574, an annual rate of about 5.74 per "
                             "cent.",
                             "After a further 6 years, t = 10, so P(10) = 12000 × 1.0574¹⁰.",
                             "1.0574¹⁰ ≈ 1.7575, so P(10) ≈ 21 090."],
                      ans="about 5.74 per cent per year; about 21 090 after 10 years",
                      interp="Two data points fix an exponential model completely, which is "
                             "why exponential extrapolation is so easy and so dangerous."),
                 dict(q="A bank offers 6 per cent nominal annual interest compounded "
                        "continuously. How long does it take for a deposit to double?",
                      vis=F("table", [["step", "working", "result"],
                                      ["model", "A = P e^(0.06t)", "—"],
                                      ["double", "2P = P e^(0.06t)", "—"],
                                      ["logs", "ln 2 = 0.06t", "—"],
                                      ["solve", "t = ln 2 ÷ 0.06", "≈ 11.55 years"]],
                            caption="Continuous doubling uses the natural logarithm."),
                      reasoning="Set the model equal to twice the initial value and take "
                               "natural logarithms.",
                      steps=["The model is A(t) = P e^(0.06t).",
                             "Doubling means A(t) = 2P, so e^(0.06t) = 2.",
                             "Taking natural logarithms: 0.06t = ln 2 ≈ 0.6931.",
                             "So t ≈ 0.6931 ÷ 0.06 ≈ 11.55 years.",
                             "The answer is independent of P, which is why the doubling time "
                             "is quoted."],
                      ans="about 11.55 years",
                      interp="The doubling time of a continuous model is ln 2 ÷ k, a formula "
                             "worth remembering because it does not depend on the deposit."),
             ], inv=dict(
                 task="A company's revenue is 4 million in year 0 and 5.8 million in year 5. "
                      "Fit an exponential model, state the annual rate, find the doubling "
                      "time, and predict the revenue in year 12. Then state one assumption "
                      "the model makes and one reason it might fail.",
                 table=[["step", "working", "result"],
                        ["model", "5.8 = 4 b⁵", "—"],
                        ["base", "b⁵ = 1.45", "b ≈ 1.0771"],
                        ["rate", "b − 1 ≈ 0.0771", "7.71% per year"],
                        ["doubling", "ln 2 ÷ ln 1.0771", "≈ 9.31 years"],
                        ["year 12", "4 × 1.0771¹²", "≈ 12.16 million"]],
                 notice=["The base came from the ratio of the two known values, raised to the "
                         "power 1/5.",
                         "The annual rate was just under 8 per cent.",
                         "The doubling time was independent of the starting revenue.",
                         "The prediction for year 12 was more than three times the starting "
                         "value."],
                 obs="Two data points fix an exponential model, and the rate and the doubling "
                     "time are read straight off it.",
                 concl="An exponential model is fitted by finding the base from two data "
                       "points, and the base gives both the rate and the doubling time. The "
                       "model assumes the rate stays constant, which is the assumption most "
                       "likely to fail: markets saturate, competitors enter and costs rise. "
                       "Here the fitted model is R(t) = 4 × 1.0771ᵗ million, with a doubling "
                       "time of about 9.3 years.")),
    ],
    practice=dict(
        A=[("3.1.1", "Write 10⁻⁴ as a decimal.",
            "0.0001.", "A negative power gives the reciprocal of the positive power.", "F"),
           ("3.1.2", "Simplify 8^(2/3) ÷ 8^(−1/3).",
            "8¹ = 8.", "Subtract the exponents: 2/3 − (−1/3) = 1.", "F"),
           ("3.1.3", "Evaluate 27^(−2/3).",
            "1/9.", "Take the cube root, then square, then reciprocate.", "F"),
           ("3.1.4", "Solve 2^(x+3) = 64.",
            "x = 3.", "Write 64 as a power of 2 and equate exponents.", "F"),
           ("3.1.5", "Solve 3^(2x) = 1/81.",
            "x = −2.", "1/81 = 3⁻⁴, so 2x = −4.", "F"),
           ("3.1.6", "Given log 5 ≈ 0.6990, find log 125 and log 0.2.",
            "log 125 = 3(0.6990) ≈ 2.097; log 0.2 = −log 5 ≈ −0.6990.",
            "125 = 5³ and 0.2 = 1/5.", "F"),
           ("3.1.7", "Solve log₃(x) = 4.",
            "x = 81.", "The definition gives x = 3⁴.", "F"),
           ("3.1.8", "Solve log₂(x) + log₂(x − 2) = 3, checking the domain.",
            "x = 4.", "Combine with the product law, then reject x = −2.", "R"),
           ("3.1.9", "Write log(8) + log(12) − log(6) as a single logarithm.",
            "log 16.", "log(8 × 12 ÷ 6) = log 16.", "F"),
           ("3.1.10", "Solve 2ˣ = 5, giving the answer to three significant figures.",
            "x ≈ 2.32.", "Take logarithms: x = log 5 ÷ log 2.", "F"),
           ("3.1.11", "Explain why log_b 1 = 0 for every permitted base b.",
            "Because b⁰ = 1, and the logarithm is the exponent.", "Use the definition.", "R"),
           ("3.1.12", "Solve 9ˣ = 4^(x+1), giving the answer to three significant figures.",
            "Taking logarithms gives 2x ln 3 = (2x + 2) ln 2, so 2x(ln 3 − ln 2) = 2 ln 2 and "
            "x = ln 2 ÷ ln(3/2) ≈ 1.71.",
            "Take logarithms of both sides when the bases cannot be matched.", "C")],
        B=[("3.2.1", "Investigate the values of (1 + 1/n)ⁿ for n = 1, 10, 100 and 1000, and "
            "predict the limit.",
            "The values 2, 2.5937, 2.7048, 2.7169 approach e ≈ 2.71828 from below.",
            "Compute the values and observe the trend.", "R"),
           ("3.2.2", "Conjecture a rule for the number of digits of 3ⁿ and test it for "
            "n = 1 to 8.",
            "The digit count is the whole part of n log₁₀3, plus one.",
            "Compute n log₁₀3 and compare with the actual values.", "R"),
           ("3.2.3", "Investigate the leading digit of 3ⁿ for n = 1 to 12 and describe the "
            "pattern.",
            "The leading digit cycles irregularly through 3, 9, 2, 8, 2, 7, 2, 6, 1, 5, 1, 4, "
            "with 1 and 2 appearing most often.",
            "Track the fractional part of n log₁₀3.", "C"),
           ("3.2.4", "Investigate whether 2ⁿ always eventually exceeds n², and justify your "
            "answer.",
            "Yes: 2ⁿ exceeds n² for n ≥ 5, and the gap widens without bound because the "
            "exponential grows faster than any power.",
            "Test small cases and find the crossover.", "C"),
           ("3.2.5", "Take a decaying quantity of your own. Investigate how the half-life "
            "changes when the decay rate doubles, and justify.",
            "The half-life halves, because it is ln 2 ÷ k and k has doubled.",
            "Use the formula for the half-life.", "R"),
           ("3.2.6", "Investigate the sum 1 + 1/2 + 1/4 + 1/8 + … for 10 terms and then for "
            "20, and predict the limit.",
            "The sums approach 2 from below: 1.9980 after 10 terms and 1.999998 after 20.",
            "Each term is half the previous one.", "R"),
           ("3.2.7", "Investigate the graph of y = 2ˣ and y = log₂ x on the same axes, and "
            "explain the relationship.",
            "They are reflections of each other in the line y = x, because they are inverse "
            "functions.", "Reflect in y = x and compare.", "R"),
           ("3.2.8", "Investigate the values of (1 + 1/n)ⁿ for n = 100 and n = 10 "
            "000, and justify the trend.",
            "The values 2.7048 and 2.7181 approach e ≈ 2.71828 from below, "
            "and the gap halves roughly each time n is squared.",
            "Compute the values and observe the convergence.", "R"),
           ("3.2.9", "Conjecture a rule for the leading digit of 7ⁿ and test it for "
            "n = 1 to 10.",
            "The leading digits cycle irregularly: 7, 4, 2, 1, 6, 4, 2, 1, "
            "8, 5, with small digits appearing more often.",
            "Track the fractional part of n log₁₀7.", "C"),
           ("3.2.10", "Investigate the half-life of a substance when the decay rate "
            "is tripled, and justify.",
            "The half-life is divided by 3, because it is ln 2 ÷ k and k "
            "has tripled.",
            "Use the formula for the half-life.", "R"),
           ("3.2.11", "Investigate the graph of y = eˣ and y = ln x on the same axes "
            "and justify the relationship.",
            "They are reflections of each other in the line y = x, because "
            "they are inverse functions.",
            "Reflect in y = x and compare.", "R"),
           ],
        C=[("3.3.1", "Write a complete solution to solving 4^(x+1) = 8^(2x−1).",
            "2^(2x+2) = 2^(6x−3), so 2x + 2 = 6x − 3 and x = 5/4.",
            "Write both sides as powers of 2 and equate exponents.", "R"),
           ("3.3.2", "Write a complete solution to solving 3ˣ = 20, giving the answer to "
            "three significant figures and checking it.",
            "x = log 20 ÷ log 3 ≈ 2.727; check 3^2.727 ≈ 20.0.",
            "Take logarithms of both sides.", "R"),
           ("3.3.3", "Write a complete solution to simplifying "
            "log(x²) − log(x) − 2 log 3 into a single logarithm.",
            "log(x²/(9x)) = log(x/9), for x > 0.",
            "Apply the quotient and power laws, then state the domain.", "R"),
           ("3.3.4", "Write a complete solution to the model: a culture of 500 bacteria "
            "doubles every 40 minutes. Find the population after 3 hours and the time to "
            "reach 100 000.",
            "P = 500 × 2^(t/40); after 180 minutes P ≈ 500 × 2^4.5 ≈ 11 314; "
            "2^(t/40) = 200 gives t = 40 log₂ 200 ≈ 305 minutes.",
            "Count periods, then solve with logarithms.", "A"),
           ("3.3.5", "Write a complete solution to finding the number of digits of 6⁵⁰.",
            "50 log₁₀6 ≈ 38.92, so the whole part is 38 and there are 39 digits.",
            "Compute n log b and add one to its whole part.", "R"),
           ("3.3.6", "Write a complete solution to the change-of-base calculation "
            "log₅ 200 using only common logarithms.",
            "log 200 ÷ log 5 ≈ 2.3010 ÷ 0.6990 ≈ 3.292.",
            "Use the change of base formula.", "R"),
           ("3.3.7", "Write a complete solution to the cooling model T = 20 + 60e^(−0.05t), "
            "finding when the temperature first falls below 25.",
            "20 + 60e^(−0.05t) < 25 gives e^(−0.05t) < 1/12, so −0.05t < −ln 12 and "
            "t > 20 ln 12 ≈ 49.7 minutes.",
            "Rearrange, take natural logarithms, and reverse the inequality carefully.", "A"),
           ("3.3.8", "Write a complete solution to solving e^(2x) = 15, giving the "
            "answer to three significant figures.",
            "2x = ln 15 ≈ 2.708, so x ≈ 1.35.",
            "Take natural logarithms of both sides.", "F"),
           ("3.3.9", "Write a complete solution to simplifying log(x³) − 2 log x + "
            "log(1/x) into a single logarithm.",
            "log(x³/(x² × x)) = log 1 = 0, for x > 0.",
            "Apply the power and quotient laws, then state the domain.", "R"),
           ("3.3.10", "Write a complete solution to finding the number of digits of "
            "3⁵⁰.",
            "50 log₁₀3 ≈ 23.856, so the whole part is 23 and there are 24 "
            "digits.",
            "Compute n log b and add one to its whole part.", "R"),
           ("3.3.11", "Write a complete solution to the model: a culture of 800 "
            "bacteria triples every 5 hours. Find the population after a "
            "day and the time to reach one million.",
            "P = 800 × 3^(t/5); after 24 hours P ≈ 800 × 3^4.8 ≈ 92 270; "
            "3^(t/5) = 1250 gives t ≈ 34.2 hours.",
            "Count periods, then solve with logarithms.", "A"),
           ("3.3.12", "Write a complete solution to proving that log_b a = 1/(log_a "
            "b) for permitted bases.",
            "Let y = log_b a, so bʸ = a; taking logarithms to base a gives "
            "y log_a b = 1, so y = 1/(log_a b).",
            "Use the definition of a logarithm and the power law.", "C"),
           ],
        D=[("3.4.1", "A radioactive isotope has a half-life of 8 days. Find the continuous "
            "decay rate and the mass remaining after 30 days from 200 g.",
            "k = −ln 2 ÷ 8 ≈ −0.0866 per day; after 30 days 200e^(−0.0866 × 30) ≈ 23.2 g.",
            "Use the half-life to find k, then evaluate.", "A"),
           ("3.4.2", "A lake's pollution falls by 12 per cent a year. How long until it is "
            "below a quarter of its present level?",
            "0.88ᵗ < 0.25 gives t > log 0.25 ÷ log 0.88 ≈ 10.46 years.",
            "Solve the inequality with logarithms.", "A"),
           ("3.4.3", "A savings account pays 4 per cent per year compounded monthly. Find the "
            "effective annual rate and the time to double.",
            "Effective rate (1 + 0.04/12)¹² − 1 ≈ 4.07 per cent; doubling time "
            "ln 2 ÷ ln 1.0407 ≈ 17.2 years.",
            "Convert the nominal rate, then use the doubling formula.", "A"),
           ("3.4.4", "A sound is measured at 75 dB. Find its intensity relative to the "
            "threshold, and the level of a sound 1000 times as intense.",
            "10 log(I/I₀) = 75 gives I/I₀ = 10^7.5; a sound 1000 times as intense is at "
            "75 + 30 = 105 dB.",
            "Invert the definition, then add 10 log 1000.", "A"),
           ("3.4.5", "A city's population is 250 000 and grows 3 per cent a year. When will "
            "it first exceed 400 000, and what assumption does the answer depend on?",
            "250000 × 1.03ᵗ > 400000 gives t > log 1.6 ÷ log 1.03 ≈ 15.9 years, so during "
            "year 16; it assumes the rate stays constant.",
            "Solve the inequality and state the assumption.", "A"),
           ("3.4.6", "A company's output is modelled by P(t) = 2000e^(0.07t). Find when "
            "output first exceeds 10 000, and comment on the realism of the model.",
            "2000e^(0.07t) > 10000 gives t > ln 5 ÷ 0.07 ≈ 23.0 years; the model assumes "
            "unlimited capacity, which no factory has.",
            "Solve the inequality and comment on the domain.", "A"),
           ("3.4.7", "A student claims that a quantity that falls by 10 per cent a day will "
            "eventually reach zero. Investigate and justify.",
            "False: the model is N = N₀ × 0.9ᵗ, which is positive for every finite t and only "
            "approaches zero as a limit.",
            "Consider the value of 0.9ᵗ for large t.", "R"),
           ("3.4.8", "A medicine's concentration is C(t) = 40e^(−0.25t) mg per litre. Find "
            "when it falls below 5 mg per litre and how many half-lives that is.",
            "40e^(−0.25t) < 5 gives t > ln 8 ÷ 0.25 ≈ 8.32 hours; the half-life is "
            "ln 2 ÷ 0.25 ≈ 2.77 hours, so this is exactly 3 half-lives.",
            "Solve the inequality and divide by the half-life.", "A"),
           ("3.4.9", "An investment triples in 12 years. Find the annual rate, and the time "
            "to double.",
            "b¹² = 3 gives b ≈ 1.0959, about 9.59 per cent per year; doubling time "
            "ln 2 ÷ ln 1.0959 ≈ 7.58 years.",
            "Find the base from the tripling, then the doubling time.", "A"),
           ("3.4.10", "A student models a population as P(t) = 1000 + 50t because it grew by "
            "50 in the first year. A second models it as 1000 × 1.05ᵗ. Compare the two "
            "predictions after 20 years and explain the difference.",
            "The linear model gives 2000; the exponential gives 1000 × 1.05²⁰ ≈ 2653. The "
            "exponential model compounds the growth, so it pulls ahead without bound.",
            "Evaluate both models at t = 20.", "A"),
           ("3.4.11", "A cooling object is at 90 °C in a room at 20 °C. After 10 minutes it "
            "is at 60 °C. Fit the model T = 20 + Ae^(−kt) and find the temperature after 30 "
            "minutes.",
            "A = 70 and e^(−10k) = 40/70, so k = −ln(4/7)/10 ≈ 0.0559; after 30 minutes "
            "T ≈ 20 + 70e^(−1.677) ≈ 33.1 °C.",
            "Use the two data points to find A and k.", "A"),
           ("3.4.12", "A student says that because log(ab) = log a + log b, it follows that "
            "log(a + b) = log a + log b. Investigate with numbers and justify a conclusion.",
            "False: log(1 + 1) = log 2 ≈ 0.3010 but log 1 + log 1 = 0. The product law "
            "applies to multiplication only, and addition inside a logarithm cannot be "
            "split.",
            "Test with a = b = 1.", "R")],
    ),
    assessment=[
        dict(title="A1 · The investment comparison",
             text="A bank offers 5 per cent per year compounded annually. A second offers 4.8 "
                  "per cent per year compounded continuously. A deposit of 8000 currency "
                  "units is made in each. Find the value of each after 10 years, state which "
                  "is better and by how much, and explain why the nominal rates alone do not "
                  "decide the answer.",
             note="Criteria A and D · model both, compare, and justify with the model."),
        dict(title="A2 · The medicine schedule",
             text="A medicine has concentration C(t) = 60e^(−0.3t) mg per litre t hours after "
                  "a dose. The effective level is 12 mg per litre. Find how long the dose "
                  "stays effective, the half-life of the medicine, and how many hours apart "
                  "doses must be given for the concentration never to fall below the "
                  "effective level. State one assumption the calculation makes.",
             note="Criteria A and C · solve the inequality, find the half-life, and state the "
                  "assumption."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of change and the related concepts of equivalence, patterns "
        "and representation appear in your work?",
        "How is the global context of scientific and technical innovation, and its exploration "
        "of populations, medicines, sound and seismic energy, visible in the investigations "
        "and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of an exponential model for a real population, and what "
        "would you still like to ask?",
    ],
    review=dict(
        ideas=["An exponential model N = N₀bᵗ compounds the base b for each unit of time.",
               "The base-b form and the continuous form N₀eᵏᵗ describe the same change, with "
               "k = ln b.",
               "Compounding more frequently approaches the continuous model, whose limit is "
               "eʳ.",
               "A logarithm is an exponent: log_b x = y means exactly bʸ = x.",
               "The logarithm laws are the index laws read backwards.",
               "Exponential equations are solved by matching bases or by taking logarithms.",
               "Every solution must be checked for a positive logarithm argument.",
               "A logarithmic scale compresses equal ratios into equal distances."],
        vocab=["exponential", "base", "multiplier", "asymptote", "half-life", "continuous "
               "growth", "natural logarithm", "logarithm laws", "change of base",
               "semi-log", "log-log", "Benford's law", "floating point", "decibel",
               "Richter scale"],
        mixed=[("3.R1", "Solve 2^(2x−1) = 32."),
               ("3.R2", "Given log 3 ≈ 0.4771, find log 81."),
               ("3.R3", "Solve log₅(x + 2) = 2."),
               ("3.R4", "How many digits does 5²⁰ have?"),
               ("3.R5", "A quantity halves every 6 hours. Find the continuous decay rate."),
               ("3.R6", "Explain why log(a + b) is not log a + log b.")],
    ),
    projects=dict(
        service=[("Community need", "Growth and decay claims in public health and finance are "
                                    "quoted without their base or time unit."),
                 ("Mathematical connection", "Exponential models and logarithms."),
                 ("Proposed action", "Collect three published growth or decay claims, convert "
                                     "each to a stated base and time unit, and publish the "
                                     "conversion."),
                 ("Expected impact", "A reader can compare two rates that were quoted "
                                     "differently."),
                 ("Student reflection", "Record the claims, the conversions and what you "
                                        "found.")],
        community=[("Project idea", "A rate audit of the school's published figures."),
                   ("Need", "Enrolment, energy use and recycling figures are quoted as "
                            "percentages with no time unit."),
                   ("Research question", "Which published rates can be compared directly, and "
                                         "which need converting first?"),
                   ("Mathematics", "Exponential models, logarithms and change of base."),
                   ("Action or outcome", "A one-page rate table with base, time unit and "
                                         "source."),
                   ("Beneficiaries", "Everyone who reads a school figure."),
                   ("Evidence", "The rate table and the conversions you performed.")],
        personal=[("Personal interest", "Music, sport, cooking or gaming."),
                  ("Learning goal", "To measure a rate in something you care about and state "
                                    "its base and time unit."),
                  ("Product or outcome", "A rate card with a graph on a logarithmic axis."),
                  ("Mathematics", "Exponential models and logarithms."),
                  ("Process", "Measure twice, fit a model, and report the rate with its "
                              "units."),
                  ("Evidence", "The rate card and the model you fitted.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=4, title="Sequences and Series",
    key="Form", related=["Patterns", "Generalisation", "Simplification"],
    context="Fairness and development",
    exploration="saving, loans and the long-term decisions that shape opportunity",
    inquiry=("A sequence is form made visible: one rule generates every term, and the sum of "
             "those terms simplifies to a formula whose behaviour — finite, unbounded or "
             "convergent — is decided by a single number."),
    atl=("Critical thinking",
         "In order for a student to judge whether a savings plan is fair, students must "
         "compare two sequences that begin identically, identify the rule that generates each, "
         "and justify which is the better long-term choice."),
    standfirst="A sequence is a list generated by a rule, and a series is the sum of a "
               "sequence. Both can be summarised by a formula, and the formula's behaviour "
               "decides whether the sum is finite, unbounded or convergent.",
    engage="Two savers each deposit 100 currency units in the first month. The first adds 10 "
           "every month; the second increases each deposit by 10 per cent of the previous "
           "month's deposit. After twelve months who has saved more, and after ten years?",
    questions=[("Factual", "What are the formulas for the nth term and the sum of the first n "
                           "terms of an arithmetic and of a geometric sequence?"),
               ("Conceptual", "Why does a geometric series converge exactly when the common "
                              "ratio is between −1 and 1?"),
               ("Debatable", "If two savings plans agree for the first year, does the one "
                             "that is better after ten years make the other unfair?")],
    application_lede="These tasks use sequence formulas and series sums. State the rule that "
                     "generates the sequence, justify the formula you use, and check the "
                     "answer against a small case.",
    projects_lede="A savings plan is a sequence in disguise. Name the rule, the formula and "
                  "the assumption that keeps the rule true, and say who the plan serves.",
    sections=[
        dict(id="4.1", title="Arithmetic sequences",
             inquiry_q="What single number generates an arithmetic sequence?",
             teach=[
                 "An arithmetic sequence has a common difference d between consecutive terms, so u(n) = u(1) + (n − 1)d. The sequence is completely determined by its first term and its common difference.",
                 "The common difference is found by subtracting any term from the next one, and it must be the same for every consecutive pair, so the pattern is a single number repeated. A list that fails this test is not arithmetic, however regular it looks.",
                 "The graph of an arithmetic sequence, with n on the horizontal axis, is a set of equally spaced points on a straight line. The common difference is the gradient of that line, which is why arithmetic sequences are the discrete analogue of linear functions.",
                 "The nth-term formula is a generalisation: it claims something about every term from a single rule, and its simplification u(n) = dn + c is a straight line. It is proved by checking that consecutive terms differ by d.",
             ], examples=[
                 dict(q="Find the nth term of the sequence 7, 11, 15, 19, … and hence find the "
                        "50th term.",
                      vis=F("table", [["n", "u(n)", "u(n) − 4n", "difference from previous"],
                                      ["1", "7", "3", "—"],
                                      ["2", "11", "3", "4"],
                                      ["3", "15", "3", "4"],
                                      ["4", "19", "3", "4"],
                                      ["50", "203", "3", "4"]],
                            caption="The common difference is constant, so the sequence is "
                                    "arithmetic."),
                      reasoning="Find the common difference, write the general term, and "
                               "substitute.",
                      steps=["Consecutive differences are all 4, so d = 4.",
                             "The first term is 7, so u(n) = 7 + (n − 1) × 4.",
                             "Simplify: u(n) = 4n + 3.",
                             "Check: u(1) = 7, u(2) = 11, u(3) = 15, as required.",
                             "So u(50) = 4(50) + 3 = 203."],
                      ans="u(n) = 4n + 3; u(50) = 203",
                      interp="The general term is a formula that covers every term, and it is "
                             "verified by checking the first few."),
                 dict(q="The 3rd term of an arithmetic sequence is 14 and the 9th term is 34. "
                        "Find the first term and the common difference.",
                      vis=F("table", [["term", "value", "equation"],
                                      ["u(3)", "14", "a + 2d = 14"],
                                      ["u(9)", "34", "a + 8d = 34"],
                                      ["subtract", "—", "6d = 20"],
                                      ["solve", "—", "d = 10/3"],
                                      ["u(1)", "22/3", "a = 14 − 2d"]],
                            caption="Two terms determine the whole sequence."),
                      reasoning="Write two equations from the general term and solve "
                               "simultaneously.",
                      steps=["Let the first term be a and the common difference be d.",
                             "Then a + 2d = 14 and a + 8d = 34.",
                             "Subtracting gives 6d = 20, so d = 10/3.",
                             "Substituting back: a = 14 − 2(10/3) = 14 − 20/3 = 22/3.",
                             "Check: u(9) = 22/3 + 8(10/3) = 22/3 + 80/3 = 102/3 = 34."],
                      ans="first term 22/3, common difference 10/3",
                      interp="Any two terms determine an arithmetic sequence, because the "
                             "general term is linear in n."),
             ], inv=dict(
                 task="Take six lists of your own: three arithmetic and three not. For the "
                      "arithmetic ones, find the common difference and the general term. For "
                      "the others, explain precisely which property of an arithmetic sequence "
                      "fails, and state whether the list is geometric.",
                 table=[["list", "type", "rule", "general term"],
                        ["5, 8, 11, 14, …", "arithmetic", "d = 3", "3n + 2"],
                        ["1, 4, 9, 16, …", "neither", "differences 3, 5, 7 not constant", "n²"],
                        ["2, 6, 18, 54, …", "geometric", "r = 3", "2 × 3^(n−1)"],
                        ["10, 7, 4, 1, …", "arithmetic", "d = −3", "13 − 3n"],
                        ["1, 1, 2, 3, 5, 8, …", "neither", "each term is the sum of the two "
                         "before it", "no closed form of this kind"],
                        ["100, 90, 81, 72.9, …", "geometric", "r = 0.9", "100 × 0.9^(n−1)"]],
                 notice=["Two of the six lists were arithmetic, with common differences 3 and "
                         "−3.",
                         "Two were geometric, with ratios 3 and 0.9.",
                         "The squares failed the arithmetic test because their differences "
                         "grew.",
                         "The Fibonacci-type list failed both tests, because its rule used "
                         "two earlier terms."],
                 obs="An arithmetic sequence has a constant difference; a geometric one has a "
                     "constant ratio; a list can be neither.",
                 concl="An arithmetic sequence is generated by adding a fixed common "
                       "difference d, so u(n) = u(1) + (n − 1)d is a generalisation that "
                       "covers every term from the first term and d alone. The test for the "
                       "type is whether consecutive differences, or consecutive ratios, are "
                       "constant, and a list can fail both tests.")),
        dict(id="4.2", title="Arithmetic series and sigma notation",
             inquiry_q="How does a sum simplify to a formula?",
             teach=[
                 "The sum of the first n terms of an arithmetic sequence is S(n) = (n/2)(2u(1) + (n − 1)d), or equivalently S(n) = (n/2)(u(1) + u(n)). The second form pairs the first with the last, and each pair has the same sum.",
                 "Sigma notation writes the sum of a list compactly: S(n) = [[math:\sum_{r=1}^{n}]] u(r). The letter r is the index, 1 is its start and n its finish, and changing the index changes nothing about the value.",
                 "The pairing argument is the proof of the formula: write the sum forwards and backwards, add the two rows, and every pair sums to u(1) + u(n). There are n such pairs, so twice the sum is n(u(1) + u(n)), and the simplification to (n/2)(u(1) + u(n)) follows immediately.",
                 "Linearity of summation lets a sum be split: [[math:\sum]] (a(r) + b(r)) = [[math:\sum]] a(r) + [[math:\sum]] b(r), and [[math:\sum]] k a(r) = k [[math:\sum]] a(r). These are the rules that make sigma notation usable.",
             ], examples=[
                 dict(q="Find the sum of the first 60 positive integers.",
                      vis=F("table", [["pairing", "sum", "comment"],
                                      ["1 + 60", "61", "first and last"],
                                      ["2 + 59", "61", "second and second-last"],
                                      ["30 + 31", "61", "middle pair"],
                                      ["30 pairs", "30 × 61", "—"]],
                            caption="Each pair sums to 61, and there are 30 of them."),
                      reasoning="Pair the first term with the last, and note that each pair "
                               "has the same sum.",
                      steps=["The sequence is 1, 2, 3, …, 60, with u(1) = 1 and u(60) = 60.",
                             "Pair 1 with 60, 2 with 59, and so on: each pair sums to 61.",
                             "There are 60 terms, so there are 30 pairs.",
                             "The sum is 30 × 61 = 1830.",
                             "Check with the formula: (60/2)(1 + 60) = 30 × 61 = 1830."],
                      ans="1830",
                      interp="The pairing argument explains the formula rather than merely "
                             "applying it, and it works for every arithmetic series."),
                 dict(q="Evaluate [[math:\sum_{r=1}^{12}]] (3r − 2).",
                      vis=F("table", [["r", "3r − 2", "value"],
                                      ["1", "1", "1"],
                                      ["2", "4", "4"],
                                      ["12", "34", "34"],
                                      ["sum", "—", "(12/2)(1 + 34) = 210"]],
                            caption="The terms form an arithmetic sequence with d = 3."),
                      reasoning="Recognise the terms as an arithmetic sequence and apply the "
                               "sum formula.",
                      steps=["The terms are 1, 4, 7, …, with u(1) = 1 and d = 3.",
                             "The last term is u(12) = 3(12) − 2 = 34.",
                             "There are 12 terms, so the sum is (12/2)(1 + 34).",
                             "That is 6 × 35 = 210.",
                             "Check by splitting: 3 × (sum of 1 to 12) − 2 × 12 = 3 × 78 − 24 = "
                             "234 − 24 = 210."],
                      ans="210",
                      interp="The linearity check confirms the formula by a different route, "
                             "which is what a check should do."),
             ], inv=dict(
                 task="Take the arithmetic sequence u(r) = 5r + 2. Compute "
                      "[[math:\sum_{r=1}^{10}]] u(r) by direct addition, then by the sum "
                      "formula, then by splitting the sum into two parts. Record all three "
                      "answers and explain why they must agree.",
                 table=[["method", "working", "answer"],
                        ["direct addition", "7 + 12 + … + 52", "295"],
                        ["sum formula", "(10/2)(7 + 52) = 5 × 59", "295"],
                        ["splitting", "5 × (1 + … + 10) + 2 × 10 = 5 × 55 + 20", "295"],
                        ["why they agree", "each method counts the same 10 terms", "—"]],
                 notice=["All three methods gave 295, as they had to.",
                         "The formula method used only the first and last terms.",
                         "The splitting method used the known sum of the first ten integers.",
                         "The formula method was fastest and the direct method was the check."],
                 obs="The sum formula and the linearity of summation are two descriptions of "
                     "the same total.",
                 concl="The sum of an arithmetic series simplifies to (n/2)(u(1) + u(n)) "
                       "because the terms can be paired so that every pair has the same "
                       "total. Sigma notation records the same sum compactly, and its "
                       "linearity lets the sum be split into parts that are easier to "
                       "evaluate. Here all three routes gave 295.")),
        dict(id="4.3", title="Geometric sequences",
             inquiry_q="What distinguishes a geometric sequence from an arithmetic one?",
             teach=[
                 "A geometric sequence has a common ratio r between consecutive terms, so u(n) = u(1) × r^(n−1). Each term is the previous one multiplied by the same factor, which is why the growth is multiplicative rather than additive.",
                 "The sign of r matters. A positive r keeps every term the same sign as the first; a negative r makes the terms alternate in sign; r = 0 collapses the sequence to zero after the first term.",
                 "The magnitude of r decides the behaviour. With |r| > 1 the terms grow without bound; with |r| = 1 they stay constant or alternate; with 0 < |r| < 1 they shrink towards zero. These three patterns exhaust the possibilities.",
                 "A geometric sequence with a positive first term and r > 0 is an exponential function of n in disguise, and its graph is the set of points on an exponential curve.",
             ], examples=[
                 dict(q="Find the nth term of the sequence 3, 6, 12, 24, … and hence find the "
                        "10th term.",
                      vis=F("table", [["n", "u(n)", "u(n) ÷ 3", "ratio to previous"],
                                      ["1", "3", "1", "—"],
                                      ["2", "6", "2", "2"],
                                      ["3", "12", "4", "2"],
                                      ["4", "24", "8", "2"],
                                      ["10", "1536", "512", "2"]],
                            caption="Each term is twice the previous one."),
                      reasoning="Find the common ratio and write the general term, then "
                               "substitute.",
                      steps=["Consecutive ratios are all 2, so r = 2.",
                             "The first term is 3, so u(n) = 3 × 2^(n−1).",
                             "Check: u(2) = 3 × 2 = 6 and u(3) = 3 × 4 = 12, as required.",
                             "So u(10) = 3 × 2⁹ = 3 × 512 = 1536.",
                             "Note the exponent is n − 1, not n, because the first term "
                             "corresponds to r⁰."],
                      ans="u(n) = 3 × 2^(n−1); u(10) = 1536",
                      interp="The exponent counts the number of multiplications, which is one "
                             "fewer than the number of terms."),
                 dict(q="A ball is dropped from 2 m and rebounds to 60 per cent of its "
                        "previous height each time. Find the height of the fifth rebound and "
                        "the total distance travelled before it comes to rest.",
                      vis=F("table", [["rebound", "height (m)", "distance added (m)"],
                                      ["0", "2.00", "2.00"],
                                      ["1", "1.20", "2 × 1.20"],
                                      ["2", "0.72", "2 × 0.72"],
                                      ["3", "0.432", "2 × 0.432"],
                                      ["4", "0.2592", "2 × 0.2592"],
                                      ["5", "0.15552", "2 × 0.15552"]],
                            caption="Each rebound is 60 per cent of the last."),
                      reasoning="Model the rebound heights as a geometric sequence and sum "
                               "the distances, counting each rebound twice.",
                      steps=["The rebound heights are 2, 1.2, 0.72, … with r = 0.6.",
                             "So the height of the nth rebound is 2 × 0.6ⁿ.",
                             "The fifth rebound is 2 × 0.6⁵ ≈ 0.1555 m.",
                             "The total distance is the initial 2 m plus twice the sum of the "
                             "rebound heights.",
                             "That sum is 2 × 0.6 ÷ (1 − 0.6) = 3, so the total distance is "
                             "2 + 2 × 3 = 8 m."],
                      ans="fifth rebound about 0.156 m; total distance 8 m",
                      interp="The total distance is finite even though the ball bounces "
                             "infinitely often, which is the first surprise of convergent "
                             "series."),
             ], inv=dict(
                 task="Take four geometric sequences of your own with r = 2, r = 0.5, r = −1 "
                      "and r = −0.5, each with first term 8. Compute the first six terms of "
                      "each, describe the behaviour of the terms as n grows, and record "
                      "whether the terms grow, shrink, alternate or collapse.",
                 table=[["n", "r = 2", "r = 0.5", "r = −1", "r = −0.5"],
                        ["1", "8", "8", "8", "8"],
                        ["2", "16", "4", "−8", "−4"],
                        ["3", "32", "2", "8", "2"],
                        ["4", "64", "1", "−8", "−1"],
                        ["5", "128", "0.5", "8", "−0.5"],
                        ["6", "256", "0.25", "−8", "0.25"],
                        ["behaviour", "grows", "shrinks to 0", "alternates, fixed size",
                         "alternates, shrinks to 0"]],
                 notice=["With r = 2 the terms doubled each step and grew without bound.",
                         "With r = 0.5 the terms halved and approached zero.",
                         "With r = −1 the terms alternated between two values and never "
                         "settled.",
                         "With r = −0.5 the terms alternated and shrank, approaching zero."],
                 obs="The magnitude of r decides growth or decay, and the sign of r decides "
                     "whether the terms alternate.",
                 concl="A geometric sequence multiplies by a fixed ratio r, so "
                       "u(n) = u(1)r^(n−1) is a generalisation covering every term. The "
                       "behaviour of the sequence is decided by |r| alone: growth above 1, "
                       "decay below 1, and neither at exactly 1. The sign of r only decides "
                       "whether the terms change sign, not whether they grow.")),
        dict(id="4.4", title="Geometric series and convergence",
             inquiry_q="When is an infinite sum finite?",
             teach=[
                 "The sum of the first n terms of a geometric sequence is S(n) = u(1)(1 − rⁿ)/(1 − r) when r ≠ 1. The formula is proved by subtracting r S(n) from S(n), which cancels every term but two.",
                 "The infinite series [[math:\sum_{n=0}^{\infty}]] u(1)rⁿ converges exactly when |r| < 1, and its sum is u(1)/(1 − r). When |r| ≥ 1 the partial sums grow without bound and no sum exists.",
                 "The condition |r| < 1 is not a technicality. With r = 0.9 the partial sums approach 10; with r = −0.9 they approach 1/1.9 ≈ 0.526; with r = 1.1 they grow without bound. A single number decides the behaviour.",
                 "A convergent series is a limit of partial sums, not an infinite addition performed all at once. The distinction matters when the terms are not all positive, because rearranging the terms of a conditionally convergent series can change its sum.",
             ], examples=[
                 dict(q="Find the sum of the geometric series 12 + 6 + 3 + 1.5 + … to infinity.",
                      vis=F("table", [["n", "partial sum", "remaining distance to 24"],
                                      ["1", "12", "12"],
                                      ["2", "18", "6"],
                                      ["3", "21", "3"],
                                      ["4", "22.5", "1.5"],
                                      ["10", "23.976", "0.024"]],
                            caption="Each step halves the remaining distance to the limit."),
                      reasoning="Identify the first term and the common ratio, check the "
                               "convergence condition, and apply the formula.",
                      steps=["The first term is 12 and the common ratio is 6/12 = 0.5.",
                             "Since |r| = 0.5 < 1, the series converges.",
                             "The sum to infinity is u(1)/(1 − r) = 12/(1 − 0.5) = 12/0.5 = 24.",
                             "Check with partial sums: after 4 terms the sum is 22.5, and "
                             "after 10 terms it is 23.976, approaching 24.",
                             "The remaining distance after n terms is 24 × 0.5ⁿ, which tends "
                             "to zero."],
                      ans="24",
                      interp="The limit 24 is never reached by a partial sum, but the partial "
                             "sums get arbitrarily close to it, which is what convergence "
                             "means."),
                 dict(q="Show that the series 1 + 1.1 + 1.21 + 1.331 + … has no sum to "
                        "infinity, and explain why.",
                      vis=F("table", [["n", "partial sum", "growth"],
                                      ["1", "1", "—"],
                                      ["2", "2.1", "+1.1"],
                                      ["3", "3.31", "+1.21"],
                                      ["4", "4.641", "+1.331"],
                                      ["10", "25.937", "+2.36"]],
                            caption="The partial sums grow without bound."),
                      reasoning="The common ratio is greater than 1 in magnitude, so the "
                               "convergence condition fails.",
                      steps=["The common ratio is 1.1, so |r| = 1.1 > 1.",
                             "The condition |r| < 1 fails, so the series diverges.",
                             "The partial sums are S(n) = 1(1.1ⁿ − 1)/(1.1 − 1) = 10(1.1ⁿ − 1).",
                             "As n grows, 1.1ⁿ grows without bound, so the partial sums do too.",
                             "Hence there is no sum to infinity."],
                      ans="no sum; the series diverges because |r| > 1",
                      interp="The single number r decides everything, and the threshold is "
                             "exactly 1 in magnitude."),
             ], inv=dict(
                 task="Investigate the series 1 + r + r² + r³ + … for r = 0.9, r = 0.99, "
                      "r = −0.5, r = −0.99, r = 1 and r = −1. For each, compute the partial "
                      "sums after 5, 10 and 20 terms, and state whether a sum to infinity "
                      "exists.",
                 table=[["r", "sum after 5", "sum after 10", "sum after 20", "converges?"],
                        ["0.9", "4.0951", "6.5132", "8.7841", "yes, to 10"],
                        ["0.99", "4.9010", "9.5573", "9.8088", "yes, to 100"],
                        ["−0.5", "0.6875", "0.9990", "1.0000", "yes, to 2/3"],
                        ["−0.99", "0.6699", "0.5033", "0.5134", "yes, to about 0.5025"],
                        ["1", "5", "10", "20", "no"],
                        ["−1", "1", "0", "0", "no"]],
                 notice=["Every series with |r| < 1 approached a limit, however slowly.",
                         "With r = 0.99 the limit was 100, and 20 terms had reached only 9.81.",
                         "With negative r the partial sums alternated above and below the "
                         "limit.",
                         "With r = 1 and r = −1 the partial sums did not settle at all."],
                 obs="The partial sums settle exactly when |r| < 1, and the limit is "
                     "u(1)/(1 − r).",
                 concl="A geometric series converges exactly when |r| < 1, and its sum to "
                       "infinity is u(1)/(1 − r); otherwise the partial sums grow without "
                       "bound or oscillate. The single number r decides the behaviour, which "
                       "is why the convergence condition is checked before the formula is "
                       "used. Here the limits were 10, 100, 2/3 and about 0.5025.")),
        dict(id="4.5", title="Annuities, loans and saving",
             inquiry_q="How does a series model a long-term financial decision?",
             teach=[
                 "A regular deposit into an account paying interest is a geometric series: each deposit grows by the interest factor for the number of periods it remains invested. The accumulated value is the sum of a finite geometric series.",
                 "The future value of a deposit of P made at the end of each period for n periods at rate i per period is P((1 + i)ⁿ − 1)/i. The formula is the geometric sum formula applied to the deposits.",
                 "A loan repaid by regular instalments is the same formula read backwards: the present value of the instalments must equal the amount borrowed. Solving for the instalment gives the standard repayment formula.",
                 "The fairness of a plan depends on the interest rate, the frequency of compounding and the length of the term. Two plans with the same nominal rate can differ substantially once these are stated, which is why the assumptions are part of the model.",
             ], examples=[
                 dict(q="A saver deposits 500 currency units at the end of each year into an "
                        "account paying 4 per cent per year. Find the value after 10 years.",
                      vis=F("table", [["deposit", "years invested", "value after 10 years"],
                                      ["1", "9", "500 × 1.04⁹"],
                                      ["2", "8", "500 × 1.04⁸"],
                                      ["10", "0", "500"],
                                      ["total", "—", "500((1.04¹⁰ − 1)/0.04)"]],
                            caption="Each deposit grows for a different number of years."),
                      reasoning="Recognise the accumulated deposits as a geometric series and "
                               "apply the sum formula.",
                      steps=["The deposits are 500 each, and the deposit made k years before "
                             "the end has grown by 1.04ᵏ.",
                             "So the total is 500(1 + 1.04 + 1.04² + … + 1.04⁹).",
                             "This is a geometric series with r = 1.04 and 10 terms.",
                             "The sum is 500 × (1.04¹⁰ − 1)/(1.04 − 1) = 500 × 12.0061.",
                             "So the value is about 6003 currency units."],
                      ans="about 6003 currency units",
                      interp="The deposits together earn about 1003 currency units of "
                             "interest, and the earliest deposit earns the most."),
                 dict(q="A loan of 20 000 currency units is repaid in 5 equal annual "
                        "instalments at 6 per cent per year. Find the annual instalment.",
                      vis=F("table", [["step", "working", "result"],
                                      ["present value", "R(1 + 1.06⁻¹ + … + 1.06⁻⁴)", "—"],
                                      ["geometric", "r = 1/1.06 ≈ 0.9434", "—"],
                                      ["sum", "R × (1 − 1.06⁻⁵)/(1 − 1.06⁻¹)", "—"],
                                      ["solve", "20000 = R × 4.2124", "R ≈ 4748.4"]],
                            caption="The instalments' present value equals the loan."),
                      reasoning="Equate the present value of the instalments to the loan and "
                               "solve for the instalment.",
                      steps=["Let the instalment be R, paid at the end of each year for 5 "
                             "years.",
                             "The present value of the instalments is R(1 + 1.06⁻¹ + … + "
                             "1.06⁻⁴).",
                             "This is a geometric series with ratio 1/1.06 and 5 terms, "
                             "summing to 4.2124.",
                             "So 20000 = 4.2124R, giving R ≈ 4748.4.",
                             "The total repaid is 5 × 4748.4 ≈ 23 742, so the interest is "
                             "about 3742."],
                      ans="about 4748 currency units per year",
                      interp="The same geometric series that grows a saving shrinks a loan, "
                             "because the ratio is below 1 instead of above it."),
             ], inv=dict(
                 task="Investigate saving 100 currency units a month for 20 years at three "
                      "rates: 0 per cent, 3 per cent and 6 per cent per year compounded "
                      "monthly. Record the total paid in and the final value for each, and "
                      "describe the pattern in the interest earned.",
                 table=[["annual rate", "monthly rate", "total paid in", "final value",
                                "interest earned"],
                        ["0%", "0", "24000", "24000", "0"],
                        ["3%", "0.0025", "24000", "32883", "8883"],
                        ["6%", "0.005", "24000", "46204", "22204"],
                        ["interest ratio", "—", "—", "0.37 then 0.93", "grows faster than "
                         "the rate"]],
                 notice=["With no interest the final value was exactly the amount paid in.",
                         "At 3 per cent the interest was about 37 per cent of the total "
                         "deposited.",
                         "At 6 per cent the interest was about 93 per cent of the total "
                         "deposited, nearly doubling the savings.",
                         "Doubling the rate far more than doubled the interest, because the "
                         "earliest deposits had longer to grow."],
                 obs="The final value is a geometric series sum, and the rate enters through "
                     "the ratio.",
                 concl="A regular saving plan accumulates to P((1 + i)ⁿ − 1)/i, where P is "
                       "the deposit, i the rate per period and n the number of periods. The "
                       "formula is the geometric series sum applied to deposits, and the "
                       "same formula read backwards repays a loan. Here 100 a month for "
                       "20 years grew to 32 883 at 3 per cent and 46 204 at 6 per cent.")),
        dict(id="4.6", title="Investigation: infinite sums",
             inquiry_q="Can infinitely many numbers add to a finite total?",
             teach=[
                 "An infinite series is a sequence of partial sums, and it converges when that sequence settles. Adding infinitely many numbers is not a single operation but a limit of finitely many additions, which is why convergence has to be defined rather than assumed.",
                 "The harmonic series 1 + 1/2 + 1/3 + 1/4 + … diverges even though its terms tend to zero. The terms shrink too slowly for the partial sums to settle, which shows that tending to zero is not sufficient for convergence.",
                 "Grouping the harmonic series in blocks of doubling length shows that each block contributes at least a half, so the partial sums exceed every bound. This argument is the standard proof that the harmonic series diverges.",
                 "A series whose terms shrink fast enough — geometrically, for instance — does converge, and the threshold between the two behaviours is a rate rather than a size. The comparison test makes the comparison precise.",
             ], examples=[
                 dict(q="Show that the partial sums of 1 + 1/2 + 1/3 + … exceed 2 after "
                        "enough terms, and explain why this suggests divergence.",
                      vis=F("table", [["block", "terms", "sum of block", "at least"],
                                      ["1", "1", "1", "1"],
                                      ["2", "1/2", "0.5", "1/2"],
                                      ["3–4", "1/3 + 1/4", "0.583", "1/2"],
                                      ["5–8", "1/5 + … + 1/8", "0.635", "1/2"],
                                      ["9–16", "1/9 + … + 1/16", "0.663", "1/2"]],
                            caption="Each doubling block contributes at least a half."),
                      reasoning="Group the terms in blocks of doubling length and show that "
                               "each block contributes at least a half.",
                      steps=["The first block is the single term 1, which is at least 1/2.",
                             "The second block is 1/2, exactly 1/2.",
                             "The third block is 1/3 + 1/4 ≥ 1/4 + 1/4 = 1/2.",
                             "The fourth block is 1/5 + … + 1/8, which is 8 terms each at "
                             "least 1/8, so at least 1/2.",
                             "Every further block contributes at least 1/2, so the partial "
                             "sums exceed every bound and the series diverges."],
                      ans="the series diverges, because each doubling block contributes at "
                          "least 1/2",
                      interp="Terms tending to zero is not enough: the harmonic series "
                             "diverges because its terms do not shrink fast enough."),
                 dict(q="Find the sum of 1/2 + 1/4 + 1/8 + … to infinity and compare it with "
                        "the harmonic series.",
                      vis=F("table", [["n", "partial sum", "remaining"],
                                      ["1", "0.5", "0.5"],
                                      ["2", "0.75", "0.25"],
                                      ["3", "0.875", "0.125"],
                                      ["4", "0.9375", "0.0625"],
                                      ["limit", "1", "0"]],
                            caption="The remaining distance halves each time."),
                      reasoning="Apply the geometric sum formula and note the contrast with "
                               "the harmonic series.",
                      steps=["The first term is 1/2 and the ratio is 1/2.",
                             "Since |r| < 1, the series converges.",
                             "The sum is (1/2)/(1 − 1/2) = 1.",
                             "The partial sums approach 1 from below, and the remaining "
                             "distance halves each time.",
                             "By contrast the harmonic series, whose terms are larger from "
                             "the third term onwards, diverges."],
                      ans="1; the harmonic series diverges by comparison",
                      interp="Two series whose terms both tend to zero can behave in "
                             "opposite ways, and the difference is the rate at which the "
                             "terms shrink."),
             ], inv=dict(
                 task="Investigate four series: [[math:\sum]] 1/n², [[math:\sum]] 1/n, "
                      "[[math:\sum]] 1/2ⁿ and [[math:\sum]] (−1)ⁿ⁺¹/n. For each, compute the "
                      "partial sums after 5, 10 and 20 terms and describe the behaviour.",
                 table=[["series", "after 5", "after 10", "after 20", "behaviour"],
                        ["1/n²", "1.4636", "1.5498", "1.5962", "converges, to about 1.6449"],
                        ["1/n", "2.2833", "2.9290", "3.5977", "diverges, slowly"],
                        ["1/2ⁿ", "0.9688", "0.9990", "1.0000", "converges, to 1"],
                        ["(−1)ⁿ⁺¹/n", "0.7833", "0.6456", "0.6688", "converges, to ln 2"]],
                 notice=["The series of 1/n² converged, while the series of 1/n did not, even "
                         "though both have terms tending to zero.",
                         "The geometric series converged fastest, reaching 1 to four decimal "
                         "places by 20 terms.",
                         "The alternating series converged by approaching its limit from "
                         "above and below in turn.",
                         "The slowest convergence belonged to 1/n², which needed thousands of "
                         "terms for two decimal places."],
                 obs="Convergence depends on how fast the terms shrink, not merely on "
                     "whether they shrink.",
                 concl="An infinite series converges when its partial sums settle, and the "
                       "harmonic series diverges because its terms shrink too slowly, as the "
                       "doubling-block argument shows. Faster shrinkage, as in a geometric "
                       "series or in 1/n², gives convergence. The threshold between the two "
                       "behaviours is a rate, which is what the comparison test formalises.")),
        dict(id="4.7", title="Mixed practice",
             inquiry_q="Which formula simplifies this sequence or series?",
             teach=[
                 "Every sequence question begins by identifying the type: constant difference means arithmetic, constant ratio means geometric, and neither means the rule must be found some other way. Identifying the type is choosing the formula.",
                 "Series questions require the convergence condition to be checked before the sum formula is applied. Applying a sum-to-infinity formula to a divergent series produces a number that is not a sum.",
                 "The two families of formulas — arithmetic and geometric — cover a large part of what sequences and series can do. The remaining cases are handled by the general idea of a partial sum and its limit.",
                 "Mixed practice is where the type is chosen rather than given, so the reasoning behind the choice is part of what is being practised.",
             ], examples=[
                 dict(q="A sequence has u(n) = 3n − 1. Find the sum of the first 40 terms.",
                      vis=F("table", [["step", "working", "result"],
                                      ["first term", "u(1) = 2", "—"],
                                      ["last term", "u(40) = 119", "—"],
                                      ["sum", "(40/2)(2 + 119)", "—"],
                                      ["answer", "20 × 121", "2420"]],
                            caption="The sum needs only the first and last terms."),
                      reasoning="Recognise the sequence as arithmetic and apply the sum "
                               "formula.",
                      steps=["u(n) = 3n − 1 has common difference 3, so it is arithmetic.",
                             "The first term is u(1) = 2 and the last is u(40) = 119.",
                             "The sum is (40/2)(2 + 119) = 20 × 121 = 2420.",
                             "Check by splitting: 3 × (sum of 1 to 40) − 40 = 3 × 820 − 40 = "
                             "2460 − 40 = 2420."],
                      ans="2420",
                      interp="The check uses a different route to the same total, which is "
                             "what makes it a check."),
                 dict(q="Find the sum to infinity of 27 + 18 + 12 + 8 + …",
                      vis=F("table", [["step", "working", "result"],
                                      ["ratio", "18/27 = 2/3", "|r| < 1"],
                                      ["sum", "27/(1 − 2/3)", "—"],
                                      ["answer", "27 × 3", "81"]],
                            caption="A convergent geometric series has a finite sum."),
                      reasoning="Find the ratio, check the condition, and apply the formula.",
                      steps=["The ratio is 18/27 = 2/3.",
                             "Since |2/3| < 1, the series converges.",
                             "The sum to infinity is 27/(1 − 2/3) = 27/(1/3) = 81.",
                             "Check with partial sums: after 4 terms the sum is 65, and after "
                             "10 terms it is 79.4, approaching 81."],
                      ans="81",
                      interp="The convergence check comes first, and it is what licenses the "
                             "formula."),
             ], inv=dict(
                 task="Take the sequence 2, 6, 18, 54, …. Compute the sum of the first 10 "
                      "terms, the sum of the first 20 terms, and the sum to infinity if it "
                      "exists. Then find the smallest n for which the partial sum exceeds "
                      "1000, and record the method you used for each part.",
                 table=[["task", "working", "answer"],
                        ["sum of first 10", "2(3¹⁰ − 1)/(3 − 1)", "59048"],
                        ["sum of first 20", "2(3²⁰ − 1)/2", "3486784400"],
                        ["sum to infinity", "|r| = 3 > 1", "does not exist"],
                        ["smallest n over 1000", "2(3ⁿ − 1)/2 > 1000", "n = 7"]],
                 notice=["The finite sums grew extremely fast, because r = 3.",
                         "There was no sum to infinity, because the convergence condition "
                         "failed.",
                         "The smallest n for which the sum exceeded 1000 was 7, found by "
                         "evaluating successive partial sums.",
                         "The same formula answered three of the four questions."],
                 obs="The geometric sum formula answers finite questions, and the "
                     "convergence condition decides whether an infinite question has an "
                     "answer at all.",
                 concl="A sequence is summarised by a general term and a series by a sum, and "
                       "each family has its own formula chosen by the type. The convergence "
                       "condition |r| < 1 is checked before any sum to infinity is claimed, "
                       "because the formula is a statement about a limit rather than about an "
                       "endless addition. Here the sums were 59 048 and 3 486 784 400, and no "
                       "infinite sum existed.")),
    ],
    practice=dict(
        A=[("4.1.1", "Find the 20th term of the arithmetic sequence 5, 9, 13, …",
            "u(20) = 5 + 19 × 4 = 81.", "Use u(n) = a + (n − 1)d.", "F"),
           ("4.1.2", "Find the common ratio of the geometric sequence 8, −12, 18, …",
            "r = −1.5.", "Divide each term by the previous one.", "F"),
           ("4.1.3", "Find the 8th term of the geometric sequence 7, 21, 63, …",
            "u(8) = 7 × 3⁷ = 15309.", "Use u(n) = a r^(n−1).", "F"),
           ("4.1.4", "Find the sum of the first 15 positive odd numbers.",
            "1 + 3 + … + 29 = (15/2)(1 + 29) = 225.", "The terms form an arithmetic series "
            "with d = 2.", "F"),
           ("4.1.5", "Evaluate [[math:\sum_{r=1}^{6}]] (2r + 1).",
            "3 + 5 + 7 + 9 + 11 + 13 = 48.", "The terms form an arithmetic series.", "F"),
           ("4.1.6", "Find the sum of the geometric series 4 + 8 + 16 + … for 6 terms.",
            "4(2⁶ − 1)/(2 − 1) = 252.", "Use S(n) = a(rⁿ − 1)/(r − 1).", "F"),
           ("4.1.7", "Find the sum to infinity of 30 + 10 + 10/3 + …",
            "30/(1 − 1/3) = 45.", "Check |r| < 1 first.", "F"),
           ("4.1.8", "A sequence has u(1) = 3 and d = −4. Find u(15).",
            "u(15) = 3 + 14(−4) = −53.", "Substitute into the general term.", "F"),
           ("4.1.9", "Find the sum of the first 10 terms of the geometric sequence with "
            "u(1) = 100 and r = 0.9.",
            "100(1 − 0.9¹⁰)/(1 − 0.9) ≈ 651.3.", "Use the geometric sum formula.", "F"),
           ("4.1.10", "Explain why the series 1 + 1.05 + 1.05² + … has no sum to infinity.",
            "Because |r| = 1.05 > 1, so the partial sums grow without bound.",
            "Check the convergence condition.", "R"),
           ("4.1.11", "A ball dropped from 3 m rebounds to 75 per cent of its height. Find the "
            "total distance travelled before it comes to rest.",
            "3 + 2 × (3 × 0.75)/(1 − 0.75) = 3 + 18 = 21 m.",
            "Count the first fall once and each rebound twice.", "A"),
           ("4.1.12", "A saver deposits 200 at the end of each year for 8 years at 5 per cent. "
            "Find the final value.",
            "200((1.05⁸ − 1)/0.05) ≈ 200 × 9.5491 ≈ 1909.8.",
            "The deposits form a geometric series with r = 1.05.", "A")],
        B=[("4.2.1", "Investigate the partial sums of 1 + 1/2 + 1/3 + … for 10, 100 and 1000 "
            "terms, and describe the rate of growth.",
            "The sums are about 2.93, 5.19 and 7.49, growing like the logarithm of the "
            "number of terms.",
            "Compute the sums and compare with ln n.", "C"),
           ("4.2.2", "Conjecture a formula for the sum of the first n even numbers and "
            "justify it.",
            "n(n + 1), because the sum is 2 × (1 + … + n) = 2 × n(n + 1)/2.",
            "Factor out the 2 and use the triangular-number formula.", "R"),
           ("4.2.3", "Investigate the series 1 − 1/2 + 1/3 − 1/4 + … for 10, 20 and 40 terms, "
            "and predict the limit.",
            "The sums approach ln 2 ≈ 0.6931, alternating above and below it.",
            "Compute the partial sums and observe the alternation.", "C"),
           ("4.2.4", "Investigate the number of terms of the series 1 + 1/2 + 1/4 + … needed "
            "to come within 0.001 of the limit, and justify.",
            "The remaining distance after n terms is (1/2)ⁿ, so (1/2)ⁿ < 0.001 gives "
            "n > log 0.001 ÷ log 0.5 ≈ 10, so 11 terms.",
            "Use the formula for the remaining distance.", "R"),
           ("4.2.5", "Investigate the sequence of partial sums of 1/n² for 5, 10, 20 and 50 "
            "terms, and predict the limit.",
            "The sums approach about 1.6449, which is π²/6.",
            "Compute the sums and observe the slow convergence.", "C"),
           ("4.2.6", "Conjecture a rule for when a series of positive decreasing terms "
            "converges, and test it on two examples.",
            "No simple rule exists for every such series, but if the terms are eventually "
            "bounded by a convergent geometric series then the series converges; 1/n "
            "diverges and 1/n² converges.",
            "Compare with a geometric series.", "C"),
           ("4.2.7", "Investigate the sum of the first n terms of a geometric series as r "
            "approaches 1, and justify what happens.",
            "The sum formula has 1 − r in the denominator, so the quotient tends to n, which "
            "is correct because with r = 1 every term equals a.",
            "Take the limit of the formula as r tends to 1.", "C"),
           ("4.2.8", "Investigate the partial sums of the geometric series 1 + 1/3 + "
            "1/9 + … and justify the limit.",
            "The sums approach 3/2 from below, because the remaining "
            "distance after n terms is (1/3)ⁿ × 3/2, which tends to zero.",
            "Use the formula for the remaining distance.", "R"),
           ("4.2.9", "Conjecture a rule for the sum of the first n square numbers "
            "and test it.",
            "n(n + 1)(2n + 1)/6, verified for n = 1, 2, 3 and 4.",
            "Compute the small cases and look for a cubic pattern.", "C"),
           ("4.2.10", "Investigate the number of terms of the series 1 + 1/2 + 1/4 + "
            "… needed to come within 0.0001 of the limit.",
            "(1/2)ⁿ < 0.0001 gives n > log 0.0001 ÷ log 0.5 = 13.29, so 14 "
            "terms.",
            "Use the formula for the remaining distance.", "R"),
           ("4.2.11", "Investigate the sequence of partial sums of 1/n² and justify "
            "that it converges while 1/n does not.",
            "The sums of 1/n² approach about 1.6449 because the terms "
            "shrink fast enough; the sums of 1/n grow without bound, as the "
            "doubling-block argument shows.",
            "Compare with a convergent geometric series, and use the "
            "doubling-block argument for the harmonic series.", "C"),
           ],
        C=[("4.3.1", "Write a complete solution to finding the 12th term of the arithmetic "
            "sequence whose 4th term is 11 and whose 10th term is 31.",
            "a + 3d = 11 and a + 9d = 31 give d = 10/3 and a = 1, so u(12) = 1 + 11(10/3) = "
            "113/3 ≈ 37.7.",
            "Solve two simultaneous equations from the general term.", "R"),
           ("4.3.2", "Write a complete solution to finding the sum of the first 25 terms of "
            "the arithmetic sequence with u(1) = −7 and d = 3.",
            "u(25) = −7 + 24(3) = 65, so the sum is (25/2)(−7 + 65) = 25 × 29 = 725.",
            "Find the last term, then apply the sum formula.", "R"),
           ("4.3.3", "Write a complete solution to evaluating "
            "[[math:\sum_{r=1}^{20}]] (5 − 2r) by splitting the sum.",
            "20 × 5 − 2 × (sum of 1 to 20) = 100 − 2 × 210 = −320.",
            "Use the linearity of summation.", "R"),
           ("4.3.4", "Write a complete solution to finding the sum to infinity of "
            "0.27 + 0.027 + 0.0027 + …",
            "The ratio is 0.1, so the sum is 0.27/(1 − 0.1) = 0.3.",
            "Check |r| < 1, then apply the formula.", "R"),
           ("4.3.5", "Write a complete solution to the annuity problem: 300 deposited at the "
            "end of each quarter for 5 years at 8 per cent per year compounded quarterly. "
            "Find the final value.",
            "The quarterly rate is 0.02 and there are 20 quarters, so the value is "
            "300((1.02²⁰ − 1)/0.02) ≈ 300 × 24.297 ≈ 7289.",
            "Convert the rate and the number of periods, then apply the annuity formula.",
            "A"),
           ("4.3.6", "Write a complete solution to the loan problem: 12 000 repaid in 4 equal "
            "annual instalments at 9 per cent. Find the instalment.",
            "12000 = R × (1 − 1.09⁻⁴)/(1 − 1.09⁻¹) = R × 3.2397, so R ≈ 3703.5.",
            "Equate the present value of the instalments to the loan.", "A"),
           ("4.3.7", "Write a complete solution to proving that the sum of the first n "
            "positive integers is n(n + 1)/2.",
            "Write the sum forwards and backwards, add the two rows so that each of the n "
            "pairs sums to n + 1, and halve the total n(n + 1).",
            "Use the pairing argument.", "R"),
           ("4.3.8", "Write a complete solution to finding the sum of the first 30 "
            "terms of the arithmetic sequence with u(1) = −12 and d = 2.5.",
            "u(30) = −12 + 29(2.5) = 60.5, so the sum is (30/2)(−12 + 60.5) "
            "= 15 × 48.5 = 727.5.",
            "Find the last term, then apply the sum formula.", "R"),
           ("4.3.9", "Write a complete solution to evaluating "
            "[[math:\sum_{r=1}^{15}]] (4r − 1) by splitting the sum.",
            "4 × (sum of 1 to 15) − 15 = 4 × 120 − 15 = 465.",
            "Use the linearity of summation.", "R"),
           ("4.3.10", "Write a complete solution to finding the sum to infinity of "
            "0.4 + 0.04 + 0.004 + …",
            "The ratio is 0.1, so the sum is 0.4/(1 − 0.1) = 0.444…, which "
            "is 4/9.",
            "Check |r| < 1, then apply the formula.", "R"),
           ("4.3.11", "Write a complete solution to the annuity problem: 250 "
            "deposited at the end of each month for 4 years at 6 per cent "
            "per year compounded monthly.",
            "The monthly rate is 0.005 and there are 48 months, so the "
            "value is 250((1.005⁴⁸ − 1)/0.005) ≈ 250 × 54.098 ≈ 13 524.",
            "Convert the rate and the number of periods, then apply the "
            "annuity formula.", "A"),
           ("4.3.12", "Write a complete solution to proving that the sum of the first "
            "n odd numbers is n².",
            "The sum is (2 × 1 − 1) + … + (2n − 1) = 2 × n(n + 1)/2 − n = "
            "n².",
            "Express the terms algebraically and simplify using the "
            "triangular-number formula.", "R"),
           ],
        D=[("4.4.1", "A company's profit rises by 250 currency units each year from a first "
            "year of 4000. Model the profit, find the profit in year 10, and find the total "
            "over the first 10 years.",
            "P(n) = 4000 + 250(n − 1); P(10) = 6250; the total is (10/2)(4000 + 6250) = "
            "51250.",
            "Recognise an arithmetic sequence and series.", "A"),
           ("4.4.2", "A town's population falls by 4 per cent a year from 50 000. Find the "
            "population after 15 years and comment on the model's limits.",
            "50000 × 0.96¹⁵ ≈ 25770; the model assumes the rate stays constant and that the "
            "population stays positive, which it does.",
            "Apply the geometric model and comment on the domain.", "A"),
           ("4.4.3", "A student saves 50 a month for 3 years at 6 per cent per year "
            "compounded monthly. Find the final value and the total interest earned.",
            "The monthly rate is 0.005 and there are 36 months, so the value is "
            "50((1.005³⁶ − 1)/0.005) ≈ 1967.9; the interest is 1967.9 − 1800 = 167.9.",
            "Convert the rate, then apply the annuity formula.", "A"),
           ("4.4.4", "Two loans of 10 000 are repaid over 5 years, one at 5 per cent and one "
            "at 12 per cent. Find each instalment and the difference in total repaid.",
            "At 5 per cent: R ≈ 2309.7; at 12 per cent: R ≈ 2774.1; the difference over 5 "
            "years is about 2322.",
            "Apply the repayment formula to each rate.", "A"),
           ("4.4.5", "A pendulum's swing is 90 cm and each swing is 80 per cent of the "
            "previous. Find the total distance travelled by the bob before it stops, and "
            "comment on whether the model is realistic.",
            "90 + 2 × (90 × 0.8)/(1 − 0.8) = 90 + 720 = 810 cm; the model assumes a constant "
            "ratio, whereas air resistance makes the decay depend on speed.",
            "Count the first swing once and each rebound twice.", "A"),
           ("4.4.6", "A charity aims to raise 100 000 and raises 4000 in the first month, "
            "with each month's total 10 per cent higher than the last. After how many months "
            "does it reach the target?",
            "4000(1.1ⁿ − 1)/(1.1 − 1) ≥ 100000 gives 1.1ⁿ − 1 ≥ 2.5, so "
            "n ≥ log 3.5 ÷ log 1.1 ≈ 13.1, so 14 months.",
            "Use the geometric sum formula and solve with logarithms.", "A"),
           ("4.4.7", "A student claims that any series whose terms tend to zero must "
            "converge. Investigate and justify.",
            "False: the harmonic series has terms tending to zero but diverges, as the "
            "doubling-block argument shows.",
            "Test the claim against the harmonic series.", "R"),
           ("4.4.8", "A car loses 20 per cent of its value each year from 15 000. After how "
            "many years is it worth less than 2000, and what is the total loss over that "
            "period?",
            "15000 × 0.8ⁿ < 2000 gives n > log(2/15) ÷ log 0.8 ≈ 9.65, so 10 years; the value "
            "is then about 1608, a loss of about 13 392.",
            "Solve the inequality and evaluate.", "A"),
           ("4.4.9", "A company offers two salary schemes over 6 years. Scheme A starts at "
            "30 000 and rises by 1500 a year. Scheme B starts at 28 000 and rises by 8 per "
            "cent a year. Find the total paid under each and say which is better.",
            "Scheme A totals (6/2)(30000 + 37500) = 202500. Scheme B totals "
            "28000(1.08⁶ − 1)/0.08 ≈ 28000 × 7.3359 ≈ 205405, so B is slightly better.",
            "Sum both series and compare.", "A"),
           ("4.4.10", "A staircase has 20 steps. A ball rolls down, and each step it travels "
            "is half the distance of the previous one. Investigate whether the ball reaches "
            "the bottom, and justify.",
            "Yes: the total distance is a convergent geometric series, 40(1/2)/(1 − 1/2) = "
            "40 units, so the ball travels a finite distance and reaches the bottom.",
            "Sum the geometric series.", "R"),
           ("4.4.11", "A student saves 100 in year 1 and increases the deposit by 10 currency "
            "units each year for 10 years, earning 5 per cent on the whole balance. Set up "
            "the model and explain why it is not a single geometric series.",
            "The deposits form an arithmetic sequence, so the accumulated value is a sum of "
            "terms 100(n − 1) × 1.05^(10−n), which mixes an arithmetic and a geometric "
            "pattern and must be summed term by term.",
            "Model the deposits and the growth separately.", "C"),
           ("4.4.12", "A bacteria culture doubles every hour from 200 bacteria. Find the "
            "population after one day, and after how many hours it first exceeds one "
            "million.",
            "After 24 hours: 200 × 2²⁴ = 3 355 443. It exceeds one million when 2ᵗ > 5000, "
            "so t > log 5000 ÷ log 2 ≈ 12.29, that is 13 hours.",
            "Apply the geometric model and solve with logarithms.", "A")],
    ),
    assessment=[
        dict(title="A1 · The two savings plans",
             text="Plan A deposits 200 currency units a month for 5 years at 6 per cent per "
                  "year compounded monthly. Plan B deposits 200 in the first month and "
                  "increases the deposit by 2 per cent each month, at the same rate. Model "
                  "both, find the value of each after 5 years, and explain which is better "
                  "and by how much.",
             note="Criteria A and D · model both plans, evaluate, and justify the "
                  "recommendation with the models."),
        dict(title="A2 · The loan comparison",
             text="A loan of 15 000 currency units can be repaid over 4 years at 7 per cent "
                  "or over 6 years at 9 per cent, in equal annual instalments. Find the "
                  "instalment and the total repaid under each, and advise a borrower who "
                  "wants the lowest total cost and one who wants the lowest monthly "
                  "instalment.",
             note="Criteria A and D · apply the repayment formula to both terms and justify "
                  "the advice."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of patterns, generalisation "
        "and simplification appear in your work?",
        "How is the global context of fairness and development, and its exploration of "
        "saving, loans and the long-term decisions that shape opportunity, visible in the "
        "investigations and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of a geometric model for a real savings plan, and what "
        "would you still like to ask?",
    ],
    review=dict(
        ideas=["An arithmetic sequence has a common difference d, and u(n) = u(1) + (n − 1)d.",
               "A geometric sequence has a common ratio r, and u(n) = u(1) r^(n−1).",
               "The sum of an arithmetic series is (n/2)(u(1) + u(n)).",
               "The sum of a finite geometric series is u(1)(rⁿ − 1)/(r − 1) for r ≠ 1.",
               "A geometric series converges to u(1)/(1 − r) exactly when |r| < 1.",
               "The harmonic series diverges even though its terms tend to zero.",
               "An annuity accumulates to P((1 + i)ⁿ − 1)/i.",
               "A loan repayment is the same formula read backwards."],
        vocab=["sequence", "term", "arithmetic", "common difference", "geometric", "common "
               "ratio", "series", "partial sum", "sigma notation", "index", "convergent",
               "divergent", "sum to infinity", "annuity", "instalment", "present value",
               "harmonic series"],
        mixed=[("4.R1", "Find the 15th term of 3, 7, 11, …"),
               ("4.R2", "Find the sum of the first 20 terms of 2, 5, 8, …"),
               ("4.R3", "Find the sum to infinity of 16 + 12 + 9 + …"),
               ("4.R4", "Evaluate [[math:\sum_{r=1}^{10}]] r²."),
               ("4.R5", "A loan of 5000 is repaid in 3 annual instalments at 10 per cent. "
                "Find the instalment."),
               ("4.R6", "Explain why the series 1 + 1/2 + 1/4 + … converges but "
                "1 + 1/2 + 1/3 + … does not.")],
    ),
    projects=dict(
        service=[("Community need", "Savings and loan terms are quoted without the "
                                    "compounding frequency or the term."),
                 ("Mathematical connection", "Sequences, series and annuities."),
                 ("Proposed action", "Collect three published savings or loan offers, convert "
                                     "each to a stated rate per period, and publish the "
                                     "comparison."),
                 ("Expected impact", "A reader can compare offers quoted in different ways."),
                 ("Student reflection", "Record the offers, the conversions and what you "
                                        "found.")],
        community=[("Project idea", "A school savings club audit."),
                   ("Need", "The club's two plans are quoted in different units and no one "
                            "has compared them."),
                   ("Research question", "Which plan gives more after five years, and by how "
                                         "much?"),
                   ("Mathematics", "Sequences, series and annuities."),
                   ("Action or outcome", "A one-page comparison with the models shown."),
                   ("Beneficiaries", "Every member of the savings club."),
                   ("Evidence", "The comparison and the models you built.")],
        personal=[("Personal interest", "Sport, music, travel or gaming."),
                  ("Learning goal", "To model a saving or borrowing plan you might actually "
                                    "use and state its assumptions."),
                  ("Product or outcome", "A savings plan with a formula and a graph."),
                  ("Mathematics", "Sequences, series and annuities."),
                  ("Process", "Choose a plan, model it, and check the model against one "
                              "known value."),
                  ("Evidence", "The plan, the model and the check.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=5, title="Quadratic Inequalities and Linear Programming",
    key="Relationships", related=["Change", "Equivalence", "System"],
    context="Globalization and sustainability",
    exploration="production planning under resource limits",
    inquiry=("A system of inequalities describes what is possible; a linear objective turns "
             "possibility into choice. Solving a quadratic inequality and optimising under "
             "linear constraints are the same habit: compare, bound, and justify."),
    atl=("Critical thinking",
         "In order for a student to decide how much of each product a workshop should make, "
         "students must translate resource limits into inequalities, bound the feasible "
         "region, and justify the optimal choice against alternatives."),
    standfirst="An inequality describes a set of possibilities rather than a single value. A "
               "system of inequalities bounds that set, and a linear objective function turns "
               "the bounded set into a choice.",
    engage="A workshop makes two kinds of basket. Each large basket uses 3 units of cane and "
           "2 hours of labour; each small one uses 1 unit of cane and 1 hour. Only 24 units "
           "of cane and 20 hours are available. How many of each should be made to earn the "
           "most, and how do you know no better choice exists?",
    questions=[("Factual", "What does the solution set of a quadratic inequality look like, "
                           "and how is it found?"),
               ("Conceptual", "Why does a linear objective function on a bounded feasible "
                              "region take its extreme values at a vertex?"),
               ("Debatable", "If an optimal plan ignores the workers' preferences, is it "
                             "still the best plan?")],
    application_lede="These tasks use inequalities and linear programming. Draw the region, "
                     "label the constraints, evaluate the objective at each vertex, and "
                     "justify the choice.",
    projects_lede="A constraint is a relationship between resources. Name the variables, "
                  "write the constraints, and say what the optimum would cost in the real "
                  "world.",
    sections=[
        dict(id="5.1", title="Quadratic inequalities in one variable",
             inquiry_q="How does a graph solve an inequality?",
             teach=[
                 "A quadratic inequality such as x² − 3x − 4 < 0 asks for the values of x for which a quadratic expression is negative. The boundary of the solution set is the set of roots, and the sign of the expression between and beyond the roots is constant.",
                 "The sign of a quadratic is decided by its leading coefficient and by the number of real roots. With two distinct roots the sign alternates across them; with a repeated root the sign does not change; with no real roots the sign is constant everywhere.",
                 "The method is to find the roots, sketch the parabola, and read off the intervals where the graph lies below or above the axis. The sketch is the justification, not a decoration.",
                 "A strict inequality excludes the boundary values and a non-strict one includes them, which is recorded with round and solid markers on a number line. The distinction matters at the endpoints only, but it matters there completely.",
             ], examples=[
                 dict(q="Solve x² − 3x − 4 < 0.",
                      vis=F("table", [["x", "x² − 3x − 4", "sign", "in the solution set?"],
                                      ["−2", "6", "positive", "no"],
                                      ["0", "−4", "negative", "yes"],
                                      ["2", "−6", "negative", "yes"],
                                      ["5", "6", "positive", "no"]],
                            caption="The expression is negative between the roots."),
                      reasoning="Find the roots, sketch the parabola, and read off where it "
                               "lies below the axis.",
                      steps=["Factorise: x² − 3x − 4 = (x − 4)(x + 1), so the roots are "
                             "x = −1 and x = 4.",
                             "The parabola opens upwards, so it is negative between its "
                             "roots.",
                             "Hence the solution is −1 < x < 4.",
                             "The endpoints are excluded because the inequality is strict.",
                             "Check: at x = 0 the expression is −4 < 0, as required."],
                      ans="−1 < x < 4",
                      interp="The sketch turns an algebraic question into a reading question, "
                             "and the reading is what is justified."),
                 dict(q="Solve x² + 4x + 4 ≥ 0.",
                      vis=F("table", [["x", "x² + 4x + 4", "sign", "in the solution set?"],
                                      ["−3", "1", "positive", "yes"],
                                      ["−2", "0", "zero", "yes"],
                                      ["0", "4", "positive", "yes"],
                                      ["1", "9", "positive", "yes"]],
                            caption="A repeated root gives a sign that does not change."),
                      reasoning="A perfect square is never negative, so the inequality holds "
                               "everywhere.",
                      steps=["Factorise: x² + 4x + 4 = (x + 2)².",
                             "A square is never negative, so (x + 2)² ≥ 0 for every x.",
                             "The solution set is therefore all real x.",
                             "The single value x = −2 makes the expression zero and is "
                             "included because the inequality is non-strict.",
                             "Check: at x = 0 the expression is 4 ≥ 0, as required."],
                      ans="all real x",
                      interp="A repeated root means the parabola touches the axis and turns "
                             "back, so the sign does not change."),
             ], inv=dict(
                 task="Take six quadratic inequalities of your own: two with two distinct "
                      "roots, one with a repeated root, one with no real roots, one with a "
                      "negative leading coefficient and one in the form of a fraction whose "
                      "denominator changes sign. Solve each, and record the solution set and "
                      "the reason the sign behaves as it does.",
                 table=[["inequality", "roots", "shape of parabola", "solution set"],
                        ["x² − 9 > 0", "−3, 3", "opens up", "x < −3 or x > 3"],
                        ["x² − 2x − 3 ≤ 0", "−1, 3", "opens up", "−1 ≤ x ≤ 3"],
                        ["x² + 6x + 9 > 0", "−3 (double)", "touches axis", "all x except −3"],
                        ["x² + x + 1 > 0", "none", "opens up", "all real x"],
                        ["−x² + 5x − 6 < 0", "2, 3", "opens down", "x < 2 or x > 3"],
                        ["1/(x − 2) > 0", "—", "not a parabola", "x > 2"]],
                 notice=["Two of the six had two distinct roots, and their solution sets were "
                         "the intervals between or beyond them.",
                         "The repeated-root case excluded exactly one value.",
                         "The no-real-roots case was true everywhere, because the parabola "
                         "never crossed the axis.",
                         "The fraction case was not a quadratic at all, and its sign was "
                         "decided by the denominator alone."],
                 obs="The sign of a quadratic is decided by its leading coefficient and its "
                     "roots, and a repeated root leaves the sign unchanged.",
                 concl="A quadratic inequality is solved by finding the roots and reading the "
                       "sign from the shape of the parabola: between the roots for an "
                       "upward-opening parabola with the expression negative, and beyond them "
                       "for the expression positive. The leading coefficient and the number of "
                       "real roots decide the pattern, and the strictness of the inequality "
                       "decides whether the roots themselves are included.")),
        dict(id="5.2", title="Inequalities in two variables",
             inquiry_q="What does the solution set of a linear inequality look like?",
             teach=[
                 "A linear inequality in two variables, such as 2x + 3y ≤ 12, describes a half-plane bounded by the line 2x + 3y = 12. The line is drawn solid when the inequality is non-strict and dashed when it is strict.",
                 "Which side of the line is the solution region is decided by testing one point, conventionally the origin when the line does not pass through it. The test is a single substitution, and it settles the question for the whole half-plane.",
                 "The boundary line itself is part of the solution exactly when the inequality is non-strict, so ≤ and ≥ include the line and < and > exclude it. The distinction is visible in the drawing and decisive in the algebra.",
                 "A system of linear inequalities is satisfied by the points that lie in every half-plane at once, so its solution set is the intersection of the regions. This intersection is the feasible region, and it is usually a polygon.",
             ], examples=[
                 dict(q="Shade the region satisfying x + 2y ≤ 8, x ≥ 1 and y ≥ 0, and find the "
                        "coordinates of its vertices.",
                      vis=F("table", [["vertex", "lines that meet", "coordinates"],
                                      ["A", "x = 1 and y = 0", "(1, 0)"],
                                      ["B", "y = 0 and x + 2y = 8", "(8, 0)"],
                                      ["C", "x + 2y = 8 and x = 1", "(1, 3.5)"],
                                      ["interior test", "x = 4, y = 1", "4 + 2 = 6 ≤ 8"]],
                            caption="The feasible region is a triangle."),
                      reasoning="Draw each boundary, test which side satisfies each inequality, "
                               "and find the intersections.",
                      steps=["The line x + 2y = 8 meets the x-axis at (8, 0) and the y-axis "
                             "at (0, 4).",
                             "x ≥ 1 excludes everything to the left of the vertical line x = 1.",
                             "y ≥ 0 excludes everything below the x-axis.",
                             "Testing (4, 1): 4 + 2 = 6 ≤ 8, so the region containing (4, 1) "
                             "is kept.",
                             "The vertices are (1, 0), (8, 0) and (1, 3.5)."],
                      ans="a triangle with vertices (1, 0), (8, 0) and (1, 3.5)",
                      interp="The region is the intersection of three half-planes, and each "
                             "vertex is the meeting of two of its boundaries."),
                 dict(q="Explain why the system x + y ≤ 5 and x + y ≥ 8 has no solution, and "
                        "draw what happens.",
                      vis=F("table", [["point", "x + y", "x + y ≤ 5?", "x + y ≥ 8?"],
                                      ["(1, 1)", "2", "yes", "no"],
                                      ["(3, 3)", "6", "no", "no"],
                                      ["(5, 5)", "10", "no", "yes"],
                                      ["(4, 4)", "8", "no", "yes"]],
                            caption="No point can satisfy both at once."),
                      reasoning="The two inequalities demand contradictory bounds on the same "
                               "quantity, so no point satisfies both.",
                      steps=["The first inequality demands x + y ≤ 5.",
                             "The second demands x + y ≥ 8.",
                             "No number is both at most 5 and at least 8.",
                             "So no point (x, y) satisfies both, and the feasible region is "
                             "empty.",
                             "The two boundary lines are parallel and lie on opposite sides of "
                             "the strip between them."],
                      ans="no solution; the feasible region is empty",
                      interp="An empty feasible region is a meaningful answer: it says the "
                             "constraints cannot all be met."),
             ], inv=dict(
                 task="Take a workshop that makes two products, A and B, with x of A and y of "
                      "B. Write and draw a system of inequalities of your own using at least "
                      "four constraints of these kinds: an upper limit on x, an upper limit "
                      "on y, a shared resource limit, and a minimum output requirement. "
                      "Shade the feasible region, label its vertices, and test one interior "
                      "point.",
                 table=[["constraint", "inequality", "boundary line", "kind of limit"],
                        ["labour", "2x + 3y ≤ 24", "2x + 3y = 24", "shared resource"],
                        ["material", "x + y ≤ 10", "x + y = 10", "shared resource"],
                        ["minimum A", "x ≥ 1", "x = 1", "minimum output"],
                        ["non-negativity", "y ≥ 0", "y = 0", "minimum output"],
                        ["interior test", "x = 3, y = 2", "6 + 6 = 12 ≤ 24", "satisfied"]],
                 notice=["Two constraints were shared resources, so their boundary lines "
                         "sloped downwards.",
                         "The minimum-output constraints were vertical or horizontal lines.",
                         "The feasible region was a polygon whose vertices were intersections "
                         "of pairs of boundary lines.",
                         "The interior point satisfied every constraint, confirming that the "
                         "shaded side of each line was chosen correctly."],
                 obs="Each constraint is a half-plane, and the feasible region is their "
                     "intersection.",
                 concl="A system of linear inequalities is solved by the intersection of its "
                       "half-planes, and each half-plane is chosen by testing one point. The "
                       "resulting feasible region is a polygon whose vertices are the "
                       "intersections of its boundary lines, and those vertices are what an "
                       "objective function is evaluated at.")),
        dict(id="5.3", title="Feasible regions and vertices",
             inquiry_q="Why does the optimum lie at a vertex?",
             teach=[
                 "A linear objective function P = ax + by takes constant values along parallel lines called iso-lines. As the line moves across the feasible region, P changes steadily, so its largest and smallest values on a bounded region occur at the last point of contact.",
                 "The last point of contact of an iso-line with a polygon is always a vertex, because a polygon's boundary consists of line segments and the extreme point of a line segment is an endpoint. Hence the optimum is at a vertex, or along a whole edge when the objective is parallel to it.",
                 "The method is therefore to find the vertices of the feasible region and evaluate the objective at each one. The vertex with the largest value gives the maximum, and the one with the smallest value gives the minimum.",
                 "When the objective is parallel to an edge, every point of that edge is optimal, and there are infinitely many solutions. This case is reported as an edge rather than as a single vertex, because the choice within the edge is free.",
             ], examples=[
                 dict(q="Maximise P = 3x + 5y subject to x + 2y ≤ 8, x ≥ 1, y ≥ 0 and "
                        "x ≤ 5.",
                      vis=F("table", [["vertex", "coordinates", "P = 3x + 5y"],
                                      ["(1, 0)", "(1, 0)", "3"],
                                      ["(5, 0)", "(5, 0)", "15"],
                                      ["(5, 1.5)", "(5, 1.5)", "22.5"],
                                      ["(1, 3.5)", "(1, 3.5)", "20.5"]],
                            caption="The largest value occurs at a vertex."),
                      reasoning="Find the vertices of the feasible region and evaluate the "
                               "objective at each.",
                      steps=["The constraints give the vertices (1, 0), (5, 0), (5, 1.5) and "
                             "(1, 3.5).",
                             "Evaluate P = 3x + 5y at each: 3, 15, 22.5 and 20.5.",
                             "The largest value is 22.5, at (5, 1.5).",
                             "Check that (5, 1.5) is feasible: 5 + 3 = 8 ≤ 8, 5 ≤ 5, "
                             "1.5 ≥ 0 and 5 ≥ 1.",
                             "So the maximum is 22.5, achieved at x = 5 and y = 1.5."],
                      ans="maximum P = 22.5 at (5, 1.5)",
                      interp="Evaluating the objective at the vertices is both necessary and "
                             "sufficient for a linear objective on a polygon."),
                 dict(q="Minimise C = 2x + 4y subject to x + y ≥ 4, x ≤ 3, y ≤ 5, x ≥ 0 and "
                        "y ≥ 0, and identify the case that arises.",
                      vis=F("table", [["vertex", "coordinates", "C = 2x + 4y"],
                                      ["(0, 4)", "(0, 4)", "16"],
                                      ["(3, 1)", "(3, 1)", "10"],
                                      ["(3, 5)", "(3, 5)", "26"],
                                      ["(0, 5)", "(0, 5)", "20"]],
                            caption="The smallest value is at a vertex again."),
                      reasoning="Find the vertices, evaluate the objective, and check whether "
                               "any edge is parallel to the objective.",
                      steps=["The constraints give the vertices (0, 4), (3, 1), (3, 5) and "
                             "(0, 5).",
                             "Evaluate C = 2x + 4y: 16, 10, 26 and 20.",
                             "The smallest value is 10, at (3, 1).",
                             "The objective 2x + 4y has slope −1/2, and the edge from (3, 1) "
                             "to (0, 4) has slope −1, so no edge is parallel to the "
                             "objective.",
                             "Hence the minimum is unique, at (3, 1)."],
                      ans="minimum C = 10 at (3, 1)",
                      interp="The check for a parallel edge is part of the justification, "
                             "because it rules out infinitely many solutions."),
             ], inv=dict(
                 task="Take the feasible region bounded by x + y ≤ 6, x + 3y ≤ 9, x ≥ 0 and "
                      "y ≥ 0. Find its vertices, then maximise P = 2x + y, minimise it, and "
                      "then find the objective that is parallel to one of the edges and "
                      "explain what that means for the number of solutions.",
                 table=[["vertex", "coordinates", "P = 2x + y", "on which edge?"],
                        ["(0, 0)", "(0, 0)", "0", "corner"],
                        ["(6, 0)", "(6, 0)", "12", "x-axis edge"],
                        ["(4.5, 1.5)", "(4.5, 1.5)", "10.5", "x + 3y = 9 edge"],
                        ["(0, 3)", "(0, 3)", "3", "y-axis edge"],
                        ["parallel objective", "x + 3y = 9", "—", "whole edge optimal"]],
                 notice=["The maximum was 12 at (6, 0) and the minimum was 0 at (0, 0).",
                         "The objective 2x + y had slope −2, while the edges had slopes −1 "
                         "and −1/3, so no edge was parallel to it.",
                         "The objective x + 3y was parallel to the edge from (0, 3) to "
                         "(4.5, 1.5).",
                         "Every point of that edge gave the same value, 9, so there were "
                         "infinitely many solutions."],
                 obs="A linear objective on a bounded polygon takes its extremes at vertices, "
                     "unless it is parallel to an edge.",
                 concl="A linear objective function takes constant values on parallel "
                       "iso-lines, so its extremes on a bounded feasible region occur at the "
                       "last point of contact, which is a vertex. When the objective is "
                       "parallel to an edge, every point of that edge is optimal and the "
                       "solution is not unique. Here the maximum of 2x + y was 12 and the "
                       "minimum was 0.")),
        dict(id="5.4", title="Linear programming",
             inquiry_q="How is a real problem turned into a linear program?",
             teach=[
                 "A linear program has three parts: decision variables, a linear objective function, and linear constraints. Writing these down in that order is the whole translation, and the relationships between the resources are what the constraints record.",
                 "The constraints come from the limits of the situation: availability of resources, minimum outputs, and the non-negativity of the quantities. Each limit is a relationship between the variables, and a limit that is not stated is a limit that has been assumed away.",
                 "The solution of a linear program is the vertex that optimises the objective, together with the statement of the optimal value. Reporting the value without the point that achieves it, or the point without the value, is an incomplete answer.",
                 "Sensitivity analysis asks how much a constraint can change before the optimum moves. The answer is read from the slack in the binding constraints, and it is what makes a recommendation robust.",
             ], examples=[
                 dict(q="A workshop makes tables and chairs. A table needs 4 hours of "
                        "carpentry and 2 of finishing; a chair needs 2 and 1. There are 40 "
                        "hours of carpentry and 15 of finishing. Profit is 30 per table and "
                        "20 per chair. Formulate the problem and solve it.",
                      vis=F("table", [["item", "carpentry", "finishing", "profit"],
                                      ["table", "4", "2", "30"],
                                      ["chair", "2", "1", "20"],
                                      ["available", "40", "15", "—"]],
                            caption="The table of resources is the formulation."),
                      reasoning="Define the variables, write the constraints and the "
                               "objective, then solve by evaluating the vertices.",
                      steps=["Let x be the number of tables and y the number of chairs.",
                             "The constraints are 4x + 2y ≤ 40, 2x + y ≤ 15, x ≥ 0 and y ≥ 0.",
                             "The objective is P = 30x + 20y.",
                             "The vertices of the feasible region are (0, 0), (7.5, 0), "
                             "(5, 5) and (0, 15).",
                             "Evaluating P gives 0, 225, 250 and 300, so the maximum is 300 at "
                             "(0, 15), that is 15 chairs and no tables."],
                      ans="15 chairs and no tables, profit 300",
                      interp="The optimum is a vertex, and reporting the plan without the "
                             "profit, or the profit without the plan, is incomplete."),
                 dict(q="A farmer has 100 hectares to plant with wheat and barley. Wheat "
                        "needs 3 units of fertiliser per hectare and barley 2, with 240 units "
                        "available. Profit is 400 per hectare of wheat and 300 of barley. "
                        "Formulate and solve.",
                      vis=F("table", [["crop", "hectares", "fertiliser", "profit"],
                                      ["wheat", "w", "3 per ha", "400 per ha"],
                                      ["barley", "b", "2 per ha", "300 per ha"],
                                      ["available", "100", "240", "—"]],
                            caption="Two constraints and one objective."),
                      reasoning="Formulate with two variables and two resource constraints, "
                               "then evaluate the vertices.",
                      steps=["Let w be the hectares of wheat and b the hectares of barley.",
                             "The constraints are w + b ≤ 100, 3w + 2b ≤ 240, w ≥ 0 and "
                             "b ≥ 0.",
                             "The objective is P = 400w + 300b.",
                             "The vertices are (0, 0), (80, 0), (40, 60) and (0, 100).",
                             "Evaluating P gives 0, 32000, 34000 and 30000, so the maximum is "
                             "34000 at (40, 60)."],
                      ans="40 ha of wheat and 60 ha of barley, profit 34 000",
                      interp="Both resource constraints are used at the optimum, so the "
                             "solution sits at the intersection of both boundaries."),
             ], inv=dict(
                 task="Formulate and solve a linear program of your own for a school fair. "
                      "Two stalls sell drinks and snacks. Each drink needs 1 unit of storage "
                      "and 2 minutes of service; each snack needs 2 units of storage and 1 "
                      "minute. There are 60 units of storage and 60 minutes. Profit is 2 per "
                      "drink and 3 per snack. Find the optimal plan and the maximum profit.",
                 table=[["step", "working", "result"],
                        ["variables", "x drinks, y snacks", "—"],
                        ["constraints", "x + 2y ≤ 60, 2x + y ≤ 60, x ≥ 0, y ≥ 0", "—"],
                        ["objective", "P = 2x + 3y", "—"],
                        ["vertices", "(0, 0), (30, 0), (20, 20), (0, 30)", "—"],
                        ["objective values", "0, 60, 100, 90", "maximum 100 at (20, 20)"]],
                 notice=["Both constraints were used at the optimum, so the plan sat at their "
                         "intersection.",
                         "The plan was 20 drinks and 20 snacks, giving a profit of 100.",
                         "The vertex (30, 0) used all the service time but left storage "
                         "unused, so it was not optimal.",
                         "The vertex (0, 30) used all the storage but left service time "
                         "unused."],
                 obs="The optimum is the vertex that uses the resources most profitably, and "
                     "it usually sits where two constraints meet.",
                 concl="A linear program is formulated by naming the decision variables, "
                       "writing one inequality per limit, and stating the objective. It is "
                       "solved by finding the vertices of the feasible region and evaluating "
                       "the objective at each. Here the optimal plan was 20 drinks and 20 "
                       "snacks for a profit of 100.")),
        dict(id="5.5", title="Modelling and optimisation",
             inquiry_q="When is a linear model the right model?",
             teach=[
                 "A linear model assumes that the contribution of each variable is independent of the level of the others, so that doubling the inputs doubles the output. This assumption gives an equivalence between the model and the situation that holds only over a limited range, and the range is part of the model.",
                 "Real problems rarely have exactly linear constraints. Costs have fixed components, resources have minimum order quantities, and outputs are whole numbers. Each of these breaks linearity, and the modeller must decide whether the break matters.",
                 "When the variables must be whole numbers, the optimum of the relaxed problem is an upper bound, and the true integer optimum is found by testing the nearby lattice points. Rounding the relaxed optimum is not in general optimal.",
                 "Sensitivity analysis reports how much a constraint can change before the optimum moves. It converts a single answer into a recommendation, because it says how fragile the answer is.",
             ], examples=[
                 dict(q="A factory makes two products with profit 8 and 12 per unit. The "
                        "constraints are x + y ≤ 10, x + 2y ≤ 14, x ≥ 0 and y ≥ 0. Solve, "
                        "and then solve again with the requirement that x and y are whole "
                        "numbers.",
                      vis=F("table", [["vertex", "coordinates", "P = 8x + 12y"],
                                      ["(0, 0)", "(0, 0)", "0"],
                                      ["(10, 0)", "(10, 0)", "80"],
                                      ["(6, 4)", "(6, 4)", "96"],
                                      ["(0, 7)", "(0, 7)", "84"]],
                            caption="The relaxed optimum is already a lattice point."),
                      reasoning="Solve the relaxed problem, then check whether the optimum is "
                               "a whole-number point.",
                      steps=["The relaxed vertices are (0, 0), (10, 0), (6, 4) and (0, 7).",
                             "Evaluating P = 8x + 12y gives 0, 80, 96 and 84.",
                             "The relaxed maximum is 96 at (6, 4).",
                             "Both coordinates are whole numbers, so the integer optimum is "
                             "the same point.",
                             "The integer optimum is x = 6, y = 4 with profit 96."],
                      ans="x = 6, y = 4, profit 96 (the same for both problems)",
                      interp="When the relaxed optimum happens to be a lattice point, the "
                             "integer problem needs no further work — but that has to be "
                             "checked."),
                 dict(q="In the same problem, suppose a third constraint 2x + y ≤ 13 is "
                        "added. Find the new optimum and explain the change.",
                      vis=F("table", [["vertex", "coordinates", "P = 8x + 12y"],
                                      ["(6, 4)", "now infeasible", "—"],
                                      ["(6.5, 0)", "(6.5, 0)", "52"],
                                      ["(5, 3)", "(5, 3)", "76"],
                                      ["(0, 7)", "(0, 7)", "84"]],
                            caption="A new constraint cuts the feasible region."),
                      reasoning="Add the constraint, recompute the vertices, and re-evaluate.",
                      steps=["The new constraint 2x + y ≤ 13 cuts off the old optimum at "
                             "(6, 4), since 2(6) + 4 = 16 > 13.",
                             "The new vertices are (0, 0), (6.5, 0), (5, 3) and (0, 7).",
                             "Evaluating P gives 0, 52, 76 and 84.",
                             "The new maximum is 84 at (0, 7).",
                             "The profit has fallen from 96 to 84, and the plan has changed "
                             "completely."],
                      ans="maximum 84 at (0, 7)",
                      interp="Adding one constraint can move the optimum to the opposite "
                             "corner, which is why sensitivity analysis matters."),
             ], inv=dict(
                 task="Take the problem of maximising P = 5x + 4y subject to x + y ≤ 7, "
                      "x + 3y ≤ 12, x ≥ 0 and y ≥ 0. Solve the relaxed problem, then find "
                      "the integer optimum, and then find how much the right-hand side of "
                      "the second constraint can fall before the optimum changes.",
                 table=[["task", "working", "answer"],
                        ["relaxed vertices", "(0, 0), (7, 0), (4.5, 2.5), (0, 4)", "—"],
                        ["relaxed optimum", "P = 5(4.5) + 4(2.5) = 32.5", "(4.5, 2.5)"],
                        ["integer optimum", "test (4, 2) and (5, 2): P = 28 and 33",
                         "(5, 2) with 33"],
                        ["sensitivity", "the edge x + 3y = 12 binds down to 11", "can fall "
                         "by 1"]],
                 notice=["The relaxed optimum was not a lattice point, so rounding was needed.",
                         "Rounding (4.5, 2.5) down to (4, 2) gave 28, but (5, 2) gave 33, so "
                         "rounding was not optimal.",
                         "The true integer optimum was (5, 2) with profit 33.",
                         "The binding constraint could fall by 1 unit before the optimum "
                         "moved."],
                 obs="Rounding a relaxed optimum is not generally optimal, and the integer "
                     "optimum must be found by testing nearby lattice points.",
                 concl="A linear model is appropriate when the contributions are independent "
                       "and the range is limited, and the modeller must check both. When the "
                       "variables are whole numbers, the relaxed optimum is an upper bound "
                       "and the true optimum is found by testing nearby lattice points. Here "
                       "the relaxed optimum was 32.5 at (4.5, 2.5) and the integer optimum "
                       "was 33 at (5, 2).")),
        dict(id="5.6", title="Investigation: integer solutions and the vertex",
             inquiry_q="When is the vertex the answer, and when is it only a bound?",
             teach=[
                 "The vertex of a relaxed linear program is an upper bound on the integer optimum, because the integer points are a subset of the feasible region. The bound is exact only when the vertex is itself a lattice point.",
                 "When the vertex is not a lattice point, the integer optimum is found by testing the lattice points near it. In two variables this is a short list, and in higher dimensions it becomes a substantial problem in its own right.",
                 "Rounding the vertex is a heuristic, not a method. Rounding down can leave the feasible region, and rounding to the nearest lattice point can miss the true optimum, as a single example shows.",
                 "The gap between the relaxed and integer optima is a measure of how much the whole-number requirement costs. When the gap is small, the relaxation is a good guide; when it is large, the problem needs a genuine integer method.",
             ], examples=[
                 dict(q="Maximise P = 4x + 3y subject to 2x + y ≤ 7, x + 2y ≤ 8, x ≥ 0, y ≥ 0. "
                        "Find the relaxed optimum and then the integer optimum.",
                      vis=F("table", [["point", "coordinates", "P = 4x + 3y", "feasible?"],
                                      ["relaxed vertex", "(2, 3)", "17", "yes"],
                                      ["(2, 3)", "lattice", "17", "yes"],
                                      ["(3, 1)", "lattice", "15", "yes"],
                                      ["(1, 3)", "lattice", "13", "yes"]],
                            caption="The relaxed optimum is a lattice point here."),
                      reasoning="Find the relaxed vertex and check whether it has whole-number "
                               "coordinates.",
                      steps=["Solving the two boundary equations gives x = 2 and y = 3.",
                             "The relaxed optimum is (2, 3) with P = 4(2) + 3(3) = 17.",
                             "Both coordinates are whole numbers, so the integer optimum is "
                             "the same point.",
                             "The nearby lattice points give smaller values, confirming the "
                             "result.",
                             "The integer optimum is x = 2, y = 3 with P = 17."],
                      ans="relaxed and integer optima both at (2, 3) with P = 17",
                      interp="When the vertex is a lattice point the relaxation is exact, and "
                             "that is the best possible case."),
                 dict(q="Maximise P = 3x + 2y subject to x + y ≤ 5, x ≤ 3.4, y ≤ 3.4, x ≥ 0, "
                        "y ≥ 0. Find the relaxed optimum and the integer optimum, and "
                        "explain the difference.",
                      vis=F("table", [["point", "coordinates", "P = 3x + 2y", "feasible?"],
                                      ["relaxed vertex", "(3.4, 1.6)", "13.4", "yes"],
                                      ["(3, 2)", "lattice", "13", "yes"],
                                      ["(3, 1)", "lattice", "11", "yes"],
                                      ["(2, 3)", "lattice", "12", "yes"]],
                            caption="The relaxed optimum is not a lattice point."),
                      reasoning="Find the relaxed optimum, then test the lattice points near "
                               "it.",
                      steps=["The relaxed optimum is where x = 3.4 meets x + y = 5, so "
                             "y = 1.6.",
                             "The relaxed value is P = 3(3.4) + 2(1.6) = 13.4.",
                             "This point is not a lattice point, so it is not a feasible "
                             "integer solution.",
                             "Testing nearby lattice points: (3, 2) gives 13, (2, 3) gives 12 "
                             "and (3, 1) gives 11.",
                             "The integer optimum is (3, 2) with P = 13, which is 0.4 below "
                             "the relaxed bound."],
                      ans="relaxed optimum 13.4 at (3.4, 1.6); integer optimum 13 at (3, 2)",
                      interp="The gap of 0.4 is the cost of the whole-number requirement, and "
                             "rounding the relaxed point to (3, 2) happens to work here but "
                             "not in general."),
             ], inv=dict(
                 task="Take P = 5x + 4y with constraints x + 2y ≤ 9, 2x + y ≤ 9, x ≥ 0, y ≥ 0. "
                      "Find the relaxed optimum, then find the integer optimum by testing "
                      "lattice points, and then find a second problem of your own where "
                      "rounding the relaxed optimum gives the wrong answer.",
                 table=[["point", "coordinates", "P = 5x + 4y", "lattice point?"],
                        ["relaxed vertex", "(3, 3)", "27", "yes"],
                        ["(4, 2)", "lattice", "28", "yes, and feasible"],
                        ["(2, 4)", "lattice", "26", "yes"],
                        ["(4, 1)", "lattice", "24", "yes"]],
                 notice=["The relaxed vertex was (3, 3) with P = 27, which is a lattice point.",
                         "But (4, 2) is also feasible and gives 28, which is larger.",
                         "So the relaxed optimum was not the integer optimum even though it "
                         "was a lattice point, because the objective was not maximised there.",
                         "The true integer optimum was (4, 2) with P = 28."],
                 obs="The relaxed optimum is an upper bound, and the integer optimum is found "
                     "by testing lattice points near it.",
                 concl="The vertex of a relaxed linear program is an upper bound on the "
                       "integer optimum, and it is exact only when the vertex is itself an "
                       "optimal lattice point. Otherwise the integer optimum must be found by "
                       "testing nearby lattice points, and rounding the vertex is a heuristic "
                       "that can fail. Here the integer optimum was 28 at (4, 2), above the "
                       "relaxed vertex value of 27.")),
        dict(id="5.7", title="Mixed practice",
             inquiry_q="Which method does this problem need?",
             teach=[
                 "Quadratic inequalities are solved by roots and sign; linear systems are solved by region and vertices. Recognising which of the two a question needs is the first step, and the two methods are easily confused because both involve graphs.",
                 "A linear programming answer has three parts: the point, the value and the justification that the point is feasible. Missing any one of the three leaves the answer incomplete.",
                 "When a problem asks for whole numbers, the relaxed optimum is a bound and the answer must be checked against lattice points. Reporting the relaxed optimum as the answer is a category error.",
                 "Mixed practice is where the method is chosen rather than given, so the reasoning behind the choice is part of what is being practised.",
             ], examples=[
                 dict(q="Solve 2x² − 5x − 3 > 0.",
                      vis=F("table", [["step", "working", "result"],
                                      ["factorise", "(2x + 1)(x − 3) > 0", "roots −1/2 and 3"],
                                      ["sign", "positive outside the roots", "—"],
                                      ["answer", "x < −1/2 or x > 3", "—"]],
                            caption="An upward-opening parabola is positive outside its "
                                    "roots."),
                      reasoning="Factorise, find the roots, and read the sign from the shape "
                               "of the parabola.",
                      steps=["Factorise: 2x² − 5x − 3 = (2x + 1)(x − 3).",
                             "The roots are x = −1/2 and x = 3.",
                             "The parabola opens upwards, so the expression is positive "
                             "outside the roots.",
                             "Hence x < −1/2 or x > 3.",
                             "Check: at x = 0 the expression is −3, which is not positive, "
                             "so the interval between the roots is correctly excluded."],
                      ans="x < −1/2 or x > 3",
                      interp="The check confirms the interval that is excluded, which is as "
                             "informative as the one that is included."),
                 dict(q="A bakery makes loaves and rolls. A loaf needs 200 g of flour and a "
                        "roll 50 g, with 10 kg available. Profit is 3 per loaf and 1 per "
                        "roll, and at least 20 items must be made. Formulate and solve.",
                      vis=F("table", [["step", "working", "result"],
                                      ["variables", "x loaves, y rolls", "—"],
                                      ["constraints", "200x + 50y ≤ 10000, x + y ≥ 20, "
                                       "x ≥ 0, y ≥ 0", "—"],
                                      ["objective", "P = 3x + y", "—"],
                                      ["vertices", "(0, 20), (0, 200), (50, 0), (20, 0)", "—"],
                                      ["values", "20, 200, 150, 60", "maximum 200 at (0, 200)"]],
                            caption="The minimum-output constraint removes part of the region."),
                      reasoning="Formulate with the flour limit and the minimum output, then "
                               "evaluate the vertices.",
                      steps=["Let x be loaves and y be rolls. The flour limit is "
                             "200x + 50y ≤ 10000.",
                             "The minimum output is x + y ≥ 20, with x ≥ 0 and y ≥ 0.",
                             "The objective is P = 3x + y.",
                             "The vertices are (0, 20), (0, 200), (50, 0) and (20, 0), giving "
                             "P = 20, 200, 150 and 60.",
                             "The maximum is 200 at (0, 200), that is 200 rolls and no loaves."],
                      ans="200 rolls and no loaves, profit 200",
                      interp="The profit per gram of flour is higher for rolls, so the "
                             "optimum puts everything into rolls, and the minimum-output "
                             "constraint is satisfied automatically."),
             ], inv=dict(
                 task="Take a recycling centre that processes glass and plastic. Each tonne "
                      "of glass needs 2 hours of sorting and earns 40 currency units; each "
                      "tonne of plastic needs 3 hours and earns 50. There are 36 hours and "
                      "at least 4 tonnes must be processed. Formulate, solve, and then "
                      "re-solve with the requirement that the tonnages are whole numbers.",
                 table=[["step", "working", "result"],
                        ["variables", "x tonnes of glass, y of plastic", "—"],
                        ["constraints", "2x + 3y ≤ 36, x + y ≥ 4, x ≥ 0, y ≥ 0", "—"],
                        ["objective", "P = 40x + 50y", "—"],
                        ["relaxed optimum", "(0, 12) with P = 600", "600"],
                        ["integer optimum", "(0, 12) is already integral", "600"]],
                 notice=["The plastic earned more per hour, so the optimum put everything "
                         "into plastic.",
                         "The relaxed optimum was already a lattice point, so the integer "
                         "problem needed no extra work.",
                         "The minimum-output constraint was satisfied automatically.",
                         "The profit of 600 used all 36 hours."],
                 obs="The optimum uses the binding resource fully, and the integer check "
                     "confirms whether the relaxed answer stands.",
                 concl="An inequality problem is solved by identifying its type first: roots "
                       "and sign for a quadratic inequality, region and vertices for a linear "
                       "system. The answer to a linear program is the point, the value and "
                       "the feasibility check together, and when whole numbers are required "
                       "the relaxed optimum is only a bound. Here the optimum was 12 tonnes "
                       "of plastic for a profit of 600.")),
    ],
    practice=dict(
        A=[("5.1.1", "Solve x² − 5x + 6 < 0.",
            "2 < x < 3.", "Factorise and read the sign between the roots.", "F"),
           ("5.1.2", "Solve x² + 2x − 8 ≥ 0.",
            "x ≤ −4 or x ≥ 2.", "The parabola opens upwards, so it is positive outside the "
            "roots.", "F"),
           ("5.1.3", "Solve −x² + 4x − 3 > 0.",
            "1 < x < 3.", "Multiply by −1 first, remembering to reverse the inequality.", "F"),
           ("5.1.4", "Solve (x − 2)² ≤ 9.",
            "−1 ≤ x ≤ 5.", "Take square roots of both sides: −3 ≤ x − 2 ≤ 3.", "F"),
           ("5.1.5", "Solve (x + 1)/(x − 3) ≤ 0.",
            "−1 ≤ x < 3.", "The sign changes at the root and at the excluded value.", "R"),
           ("5.1.6", "Shade the region x + y ≤ 6, x ≥ 1, y ≥ 2.",
            "A triangle with vertices (1, 2), (4, 2) and (1, 5).",
            "Draw each boundary and test one point.", "F"),
           ("5.1.7", "Find the vertices of the region x ≤ 4, y ≤ 3, x + y ≤ 6, x ≥ 0, y ≥ 0.",
            "(0, 0), (4, 0), (4, 2), (3, 3) and (0, 3).",
            "Intersect the boundary lines pairwise.", "F"),
           ("5.1.8", "Maximise P = x + 2y subject to x + y ≤ 4, x ≤ 2, y ≤ 3, x ≥ 0, y ≥ 0.",
            "Vertices (0, 0), (2, 0), (2, 2), (1, 3), (0, 3); values 0, 2, 6, 7, 6; maximum 7 "
            "at (1, 3).", "Evaluate the objective at each vertex.", "F"),
           ("5.1.9", "Minimise C = 2x + y subject to x + y ≥ 3, x + 3y ≥ 6, x ≥ 0, y ≥ 0.",
            "Vertices (3, 0), (6, 0) and (1.5, 1.5); values 6, 12 and 4.5; minimum 4.5 at "
            "(1.5, 1.5).", "Evaluate at each vertex.", "R"),
           ("5.1.10", "Explain why the feasible region of x + y ≤ 3 and x + y ≥ 7 is empty.",
            "Because no value of x + y is both at most 3 and at least 7.",
            "The two constraints contradict each other.", "R"),
           ("5.1.11", "A farmer has 60 kg of feed. Cattle need 5 kg a day and sheep 2 kg. "
            "Write the constraint if there are c cattle and s sheep.",
            "5c + 2s ≤ 60, with c ≥ 0 and s ≥ 0.",
            "Each animal consumes its daily requirement.", "F"),
           ("5.1.12", "A firm maximises P = 4x + 3y subject to x + y ≤ 5, x + 3y ≤ 9, x ≥ 0, "
            "y ≥ 0. Find the optimum.",
            "Vertices (0, 0), (5, 0), (3, 2), (0, 3); values 0, 20, 18, 9; maximum 20 at "
            "(5, 0).", "Evaluate the objective at each vertex.", "F")],
        B=[("5.2.1", "Investigate the solution sets of x² − 4x + c < 0 for c = 4, 3, 0 and "
            "−5, and describe the pattern.",
            "c = 4 gives only x = 2 excluded; c = 3 gives 1 < x < 3; c = 0 gives "
            "0 < x < 4; c = −5 gives x < −1 or x > 5. The interval widens as c falls.",
            "Find the roots for each value and read the sign.", "R"),
           ("5.2.2", "Conjecture a rule for when a quadratic inequality has no solution, and "
            "justify it.",
            "It has no solution exactly when the quadratic never takes the required sign: "
            "x² − 2x + 5 < 0 has no solution because the discriminant is negative and the "
            "parabola opens upwards.",
            "Use the discriminant and the leading coefficient.", "C"),
           ("5.2.3", "Investigate the feasible region of 2x + y ≤ 8, x + 2y ≤ 8, x ≥ 0, y ≥ 0 "
            "and describe its shape.",
            "It is a quadrilateral with vertices (0, 0), (4, 0), (8/3, 8/3) and (0, 4), "
            "symmetric in x and y.",
            "Intersect the boundary lines and note the symmetry.", "R"),
           ("5.2.4", "Investigate the objective P = x + y on the region of 5.2.3, and decide "
            "whether the maximum is unique.",
            "The vertices give P = 0, 4, 16/3 and 4, so the maximum is 16/3 at (8/3, 8/3). It "
            "is unique, because the objective has slope −1 while the edges have slopes −2, "
            "−1/2, 0 and none, so no edge is parallel to it.",
            "Check whether the objective is parallel to any edge.", "C"),
           ("5.2.5", "Investigate the effect on the optimum of adding the constraint x ≤ 2 to "
            "the problem of 5.2.3.",
            "The vertex (8/3, 8/3) is cut off, so the new vertices are (0, 0), (2, 0), (2, 2) "
            "and (0, 4), and the maximum of x + y becomes 4 at (2, 2).",
            "Recompute the vertices and re-evaluate.", "R"),
           ("5.2.6", "Conjecture a rule for the maximum of x + y subject to ax + by ≤ c and "
            "x, y ≥ 0, and test it.",
            "The maximum is c/a when b ≥ a, c/b when a > b, and either when a = b; here the "
            "maximum is c ÷ max(a, b).",
            "Compare the profit per unit of the shared resource.", "C"),
           ("5.2.7", "Investigate the number of vertices of a feasible region bounded by n "
            "lines, and justify a bound.",
            "At most n(n − 1)/2 pairwise intersections, but usually far fewer because most "
            "intersections lie outside the region.",
            "Count pairwise intersections and check feasibility.", "C"),
           ("5.2.8", "Investigate the solution sets of x² − 6x + c ≤ 0 for c = 8, 9 "
            "and 10, and justify the pattern.",
            "c = 8 gives 2 ≤ x ≤ 4; c = 9 gives only x = 3; c = 10 gives no "
            "solution, because the discriminant becomes negative.",
            "Compute the discriminant for each value and read the sign.", "R"),
           ("5.2.9", "Conjecture a rule for when a system of two linear inequalities "
            "has a bounded feasible region, and test it.",
            "Bounded exactly when the two boundary lines are not parallel "
            "and the non-negativity constraints are present; otherwise the "
            "region is unbounded or empty.",
            "Draw the pairs and look for a closed polygon.", "C"),
           ("5.2.10", "Investigate the maximum of x + y on the region x + 2y ≤ 8, 2x "
            "+ y ≤ 8, x ≥ 0, y ≥ 0, and decide whether it is unique.",
            "The vertices give 0, 4, 16/3 and 4, so the maximum is 16/3 at "
            "(8/3, 8/3), and it is unique because no edge is parallel to x "
            "+ y.",
            "Evaluate at the vertices and check the edge gradients.", "R"),
           ("5.2.11", "Investigate the effect of adding a minimum-output constraint "
            "to a linear program, and justify.",
            "It cuts off part of the feasible region, usually a corner, so "
            "the optimum either moves to a new vertex or becomes infeasible "
            "if the minimum cannot be met.",
            "Recompute the vertices after adding the constraint.", "R"),
           ],
        C=[("5.3.1", "Write a complete solution to solving 3x² − 7x − 6 ≤ 0.",
            "(3x + 2)(x − 3) ≤ 0, so −2/3 ≤ x ≤ 3.",
            "Factorise and read the sign between the roots.", "R"),
           ("5.3.2", "Write a complete solution to solving (x − 1)/(x + 2) > 0.",
            "x < −2 or x > 1, excluding x = −2 where the expression is undefined.",
            "Track the sign changes at the root and the excluded value.", "R"),
           ("5.3.3", "Write a complete solution to finding the maximum of P = 5x + 4y "
            "subject to x + 2y ≤ 8, 3x + y ≤ 9, x ≥ 0, y ≥ 0.",
            "Vertices (0, 0), (3, 0), (2, 3), (0, 4); values 0, 15, 22, 16; maximum 22 at "
            "(2, 3).", "Evaluate the objective at each vertex.", "R"),
           ("5.3.4", "Write a complete solution to the workshop problem: 40 hours of "
            "carpentry and 24 of finishing, with tables needing 4 and 2 and chairs 2 and 1, "
            "profit 30 and 20. Formulate and solve.",
            "The constraints are 4x + 2y ≤ 40 and 2x + y ≤ 24, but doubling the second gives "
            "4x + 2y ≤ 48, which is weaker, so only carpentry binds. The vertices are (0, 0), "
            "(10, 0) and (0, 20), giving P = 0, 300 and 400; the maximum is 400 at (0, 20), "
            "that is 20 chairs and no tables.",
            "Compare the constraints before listing the vertices.", "R"),
           ("5.3.5", "Write a complete solution to the integer version of the problem in "
            "5.3.4, where x and y must be whole numbers.",
            "The relaxed maximum is 480 at (0, 24), which is integral, so the integer "
            "optimum is the same: 24 chairs and no tables.",
            "Check whether the relaxed optimum is a lattice point.", "R"),
           ("5.3.6", "Write a complete solution to minimising the cost C = 3x + 2y of a diet "
            "that needs at least 6 units of A and 4 of B, where food X gives 1 and 2 units "
            "and food Y gives 2 and 1.",
            "x + 2y ≥ 6, 2x + y ≥ 4, C = 3x + 2y; vertices (6, 0), (2/3, 8/3), (0, 4); "
            "values 18, 25/3, 8; minimum 8 at (0, 4), that is 4 units of food Y.",
            "Formulate the constraints from the requirements and evaluate the vertices.",
            "A"),
           ("5.3.7", "Write a complete solution to proving that a linear objective on a "
            "bounded feasible region attains its maximum at a vertex.",
            "Move an iso-line of the objective across the region; the value changes steadily "
            "and the last point of contact with a polygon is a vertex, so the maximum occurs "
            "there or along an edge parallel to the objective.",
            "Use the iso-line argument on a polygon.", "R"),
           ("5.3.8", "Write a complete solution to solving (x − 2)(x + 3)(x − 5) ≤ "
            "0.",
            "The roots are −3, 2 and 5; the sign is negative on (−3, 2) and "
            "on (5, ∞), so the solution is −3 ≤ x ≤ 2 or x ≥ 5.",
            "Find the roots, mark them on a number line and test each "
            "interval.", "R"),
           ("5.3.9", "Write a complete solution to solving 3/(x − 1) ≥ 1.",
            "x − 1 > 0 gives 3 ≥ x − 1, so 1 < x ≤ 4; x − 1 < 0 gives 3 ≤ x "
            "− 1, impossible. The solution is 1 < x ≤ 4.",
            "Consider the sign of the denominator before multiplying "
            "through.", "R"),
           ("5.3.10", "Write a complete solution to minimising C = 4x + 3y subject to "
            "2x + y ≥ 10, x + 3y ≥ 15, x ≥ 0, y ≥ 0.",
            "The vertices are (5, 0), (3, 4) and (0, 5), giving 20, 24 and "
            "15; the minimum is 15 at (0, 5).",
            "Evaluate the objective at each vertex.", "R"),
           ("5.3.11", "Write a complete solution to the production problem: 30 hours "
            "of labour and 24 units of material, with A needing 2 and 3 and "
            "B needing 3 and 2, profit 40 and 30. Formulate and solve.",
            "2x + 3y ≤ 30, 3x + 2y ≤ 24, P = 40x + 30y; the vertices are "
            "(0, 0), (8, 0), (6, 6) and (0, 10), giving 0, 320, 420 and "
            "300; the maximum is 420 at (6, 6).",
            "Formulate from the table of resources, then evaluate the "
            "vertices.", "A"),
           ("5.3.12", "Write a complete solution to proving that the maximum of a "
            "linear objective on an unbounded feasible region need not "
            "exist.",
            "Maximise x + y subject to x ≥ 0 and y ≥ 0: the region is "
            "unbounded and the objective grows without bound, so no maximum "
            "exists.",
            "Look for a direction in which the objective increases "
            "indefinitely.", "C"),
           ],
        D=[("5.4.1", "A charity packs food parcels. A large parcel needs 3 kg of rice and 2 "
            "of beans; a small one needs 1 and 2. There are 30 kg of rice and 28 of beans. "
            "Formulate and solve to maximise the number of parcels.",
            "3x + y ≤ 30, 2x + 2y ≤ 28, P = x + y; vertices (0, 0), (10, 0), (8, 6), (0, 14); "
            "values 0, 10, 14, 14; maximum 14, achieved along the whole edge from (0, 14) to "
            "(8, 6).", "Evaluate the objective at each vertex and check for a parallel edge.",
            "A"),
           ("5.4.2", "A school orders two kinds of laptop. Type A costs 400 and needs 1 desk; "
            "type B costs 300 and needs 2 desks. There are 6000 currency units and 20 desks. "
            "Maximise the number of laptops.",
            "400x + 300y ≤ 6000, x + 2y ≤ 20, P = x + y; vertices (0, 0), (15, 0), (10, 5), "
            "(0, 10); values 0, 15, 15, 10; maximum 15 along the edge from (15, 0) to "
            "(10, 5).", "Evaluate at each vertex.", "A"),
           ("5.4.3", "A farm has 100 hectares and 240 units of water. Wheat needs 2 units "
            "and barley 4 per hectare, and at least 20 hectares must be wheat. Profit is 500 "
            "per hectare of wheat and 400 of barley. Formulate and solve.",
            "w + b ≤ 100, 2w + 4b ≤ 240, w ≥ 20, P = 500w + 400b; vertices (20, 0), (100, 0), "
            "(20, 50), (40, 40); values 10000, 50000, 30000, 36000; maximum 50000 at "
            "(100, 0), that is all wheat.",
            "Evaluate the objective at each vertex.", "A"),
           ("5.4.4", "A factory's relaxed optimum is 13.4 at (3.4, 1.6) for P = 3x + 2y. "
            "Explain why this is not an answer to the integer problem, and find the integer "
            "optimum.",
            "The point is not a lattice point, so it is not feasible; the nearby lattice "
            "points give (3, 2) → 13, (2, 3) → 12 and (3, 1) → 11, so the integer optimum is "
            "13 at (3, 2).",
            "Test the lattice points near the relaxed vertex.", "R"),
           ("5.4.5", "A company maximises P = 7x + 5y subject to 2x + 3y ≤ 18, 3x + y ≤ 12, "
            "x ≥ 0, y ≥ 0, with x and y integers. Find the optimum and the gap from the "
            "relaxed value.",
            "Relaxed vertices (0, 0), (4, 0), (22/5, 26/15), (0, 6); the relaxed maximum is "
            "28 at (4, 0), which is integral, so the integer optimum is also 28 with gap 0.",
            "Check whether the relaxed optimum is a lattice point.", "R"),
           ("5.4.6", "A council must place x benches and y bins. Each bench needs 2 m² and "
            "each bin 1 m², with 40 m² available, and there must be at least as many bins as "
            "benches. Maximise the community score S = 3x + 2y.",
            "2x + y ≤ 40, y ≥ x, S = 3x + 2y; vertices (0, 0), (20, 0), (40/3, 40/3), (0, 40); "
            "values 0, 60, 200/3, 80; maximum 80 at (0, 40), that is 40 bins.",
            "Evaluate the objective at each vertex.", "A"),
           ("5.4.7", "A student solves a linear program and reports only the maximum value. "
            "Explain what is missing and why it matters.",
            "The point at which the maximum is attained, and the check that the point "
            "satisfies every constraint; without the point the plan cannot be carried out.",
            "A linear program's answer is a plan, not just a number.", "R"),
           ("5.4.8", "A water supplier mixes two sources. Source A costs 3 per litre and has "
            "0.2 units of mineral; source B costs 5 and has 0.5 units. The daily requirement "
            "is at least 10 units of mineral and at most 200 currency units. Minimise the "
            "cost.",
            "0.2a + 0.5b ≥ 10, 3a + 5b ≤ 200, C = 3a + 5b; the cost is minimised by taking "
            "all of source A: a = 50, b = 0, C = 150.",
            "Compare the mineral per currency unit of each source.", "A"),
           ("5.4.9", "A publisher prints x hardback and y paperback copies. Each hardback "
            "uses 3 sheets and each paperback 1, with 600 sheets, and the printing machine "
            "runs for at most 200 minutes, hardbacks taking 4 minutes and paperbacks 2. "
            "Maximise the number of copies.",
            "3x + y ≤ 600, 4x + 2y ≤ 200, P = x + y; vertices (0, 0), (50, 0), (40, 20), "
            "(0, 100); values 0, 50, 60, 100; maximum 100 at (0, 100), all paperbacks.",
            "Evaluate the objective at each vertex.", "A"),
           ("5.4.10", "A student claims that if a relaxed optimum is a lattice point then it "
            "must be the integer optimum. Investigate and justify.",
            "False: in 5.2.7 the relaxed vertex (3, 3) was a lattice point with P = 27, but "
            "(4, 2) was feasible and gave 28, because the objective was not maximised at the "
            "vertex.",
            "Look for a feasible lattice point with a better objective value.", "C"),
           ("5.4.11", "A delivery firm loads x small and y large crates. Small crates weigh "
            "10 kg and large 25 kg, with a 500 kg limit, and each small crate earns 20 and "
            "each large 40. Maximise the earnings.",
            "10x + 25y ≤ 500, P = 20x + 40y; vertices (0, 0), (50, 0), (0, 20); values 0, "
            "1000, 800; maximum 1000 at (50, 0), all small crates.",
            "Compare the earnings per kilogram.", "A"),
           ("5.4.12", "A cooperative grows x hectares of maize and y of beans. Maize needs 4 "
            "hours of labour per hectare and beans 2, with 80 hours, and the market absorbs "
            "at most 25 hectares. Profit is 600 per hectare of maize and 900 of beans. "
            "Formulate and solve.",
            "4x + 2y ≤ 80, x + y ≤ 25, P = 600x + 900y; vertices (0, 0), (20, 0), (15, 10), "
            "(0, 25); values 0, 12000, 18000, 22500; maximum 22500 at (0, 25), all beans.",
            "Evaluate the objective at each vertex.", "A")],
    ),
    assessment=[
        dict(title="A1 · The workshop plan",
             text="A workshop makes two products. Product A needs 2 hours of cutting and 1 of "
                  "assembly; product B needs 1 of cutting and 2 of assembly. There are 40 "
                  "hours of cutting and 36 of assembly. Profit is 25 per A and 30 per B. "
                  "Formulate the problem, solve it, and advise the owner, stating any "
                  "assumption the model makes.",
             note="Criteria A and D · formulate, solve by vertices, and justify the "
                  "recommendation."),
        dict(title="A2 · The fair's budget",
             text="A school fair has a budget of 300 currency units and 20 volunteers. A "
                  "food stall costs 40 and needs 3 volunteers; a games stall costs 25 and "
                  "needs 2. The fair must have at least 2 food stalls. Maximise the total "
                  "income, modelled as 90 per food stall and 60 per games stall, and comment "
                  "on whether the model is realistic.",
             note="Criteria A and C · formulate, solve, and evaluate the model's "
                  "assumptions."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of change, "
        "equivalence and system appear in your work?",
        "How is the global context of globalization and sustainability, and its exploration of "
        "production planning under resource limits, visible in the investigations and examples "
        "you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of a linear model for a real production decision, and what "
        "would you still like to ask?",
    ],
    review=dict(
        ideas=["A quadratic inequality is solved by finding the roots and reading the sign "
               "from the parabola.",
               "A linear inequality in two variables describes a half-plane bounded by a line.",
               "A system of inequalities is solved by the intersection of its half-planes.",
               "A linear objective takes constant values on parallel iso-lines.",
               "The optimum of a linear program on a bounded region is at a vertex, or along "
               "an edge parallel to the objective.",
               "When the objective is parallel to an edge there are infinitely many "
               "solutions.",
               "An integer optimum is found by testing lattice points near the relaxed "
               "vertex.",
               "Rounding a relaxed optimum is a heuristic, not a method."],
        vocab=["inequality", "solution set", "feasible region", "vertex", "constraint",
               "objective function", "iso-line", "linear program", "decision variable",
               "binding constraint", "slack", "sensitivity", "integer programming",
               "lattice point", "relaxed problem"],
        mixed=[("5.R1", "Solve x² + x − 12 ≥ 0."),
               ("5.R2", "Shade the region 2x + y ≤ 10, x ≥ 0, y ≥ 0 and find its vertices."),
               ("5.R3", "Maximise P = 3x + 4y subject to x + y ≤ 5, x ≤ 3, x ≥ 0, y ≥ 0."),
               ("5.R4", "Explain why the system x + 2y ≤ 4 and x + 2y ≥ 6 has no solution."),
               ("5.R5", "A relaxed optimum is 12.5 at (2.5, 2.5). Find the integer optimum "
                "for P = 2x + 3y if (2, 2), (3, 2) and (2, 3) are feasible."),
               ("5.R6", "State the three parts of a complete answer to a linear program.")],
    ),
    projects=dict(
        service=[("Community need", "Production and resource decisions are made without the "
                                    "limits being written down."),
                 ("Mathematical connection", "Inequalities and linear programming."),
                 ("Proposed action", "Take one real resource decision in your community, "
                                     "write its constraints, solve it, and publish the plan "
                                     "and its assumptions."),
                 ("Expected impact", "The decision is made with its limits visible."),
                 ("Student reflection", "Record the decision, the model and what you found.")],
        community=[("Project idea", "A resource audit of the school canteen."),
                   ("Need", "The canteen buys without stating its budget, storage or "
                            "volunteer limits."),
                   ("Research question", "What is the best mix of items given the stated "
                                         "limits?"),
                   ("Mathematics", "Inequalities, feasible regions and linear programming."),
                   ("Action or outcome", "A one-page plan with the constraints and the "
                                         "optimum."),
                   ("Beneficiaries", "The canteen and everyone who eats there."),
                   ("Evidence", "The plan and the model behind it.")],
        personal=[("Personal interest", "Sport, cooking, music or gaming."),
                  ("Learning goal", "To model a decision you actually make under limits."),
                  ("Product or outcome", "A plan with the constraints and the objective "
                                         "written down."),
                  ("Mathematics", "Inequalities and linear programming."),
                  ("Process", "Name the variables, write the limits, and solve by "
                              "evaluating vertices."),
                  ("Evidence", "The plan and the vertices you evaluated.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=6, title="Circle Geometry and Geometric Proof",
    key="Logic", related=["Space", "Generalisation", "Justification"],
    context="Personal and cultural expression",
    exploration="the geometry of architecture and ornament",
    inquiry=("A circle conceals equal angles and fixed distances; a few theorems, proved from "
             "radii and triangles, let us deduce measurements and justify every claim."),
    atl=("Critical thinking",
         "In order for a student to justify a measurement in an architectural drawing, "
         "students must identify the circle property that applies, state it as a general "
         "claim, and construct a proof from radii and triangles."),
    standfirst="A circle is the set of points at a fixed distance from a centre, so all its "
               "points lie in one space at one distance. That single definition generates "
               "a small number of theorems, and those theorems justify every measurement "
               "made in a circle.",
    engage="A stained-glass window is designed as a circle with chords meeting at a point. "
           "The designer needs to know the angle between two chords before cutting the glass. "
           "Which property of the circle decides it, and how is that property proved?",
    questions=[("Factual", "What do the angle at the centre, the angle in a semicircle and the "
                           "alternate segment theorems say?"),
               ("Conceptual", "Why does a tangent meet a radius at right angles, and what "
                              "does a proof need in order to be complete?"),
               ("Debatable", "If a diagram convinces you a claim is true, is a proof still "
                             "needed?")],
    application_lede="These tasks use circle theorems and geometric proof. Name the theorem "
                     "you use, state it in full, and set out the deduction in order.",
    projects_lede="An ornament is a theorem made visible. Name the property the design "
                  "depends on, prove it, and say what the design would lose without it.",
    sections=[
        dict(id="6.1", title="Angles in circles",
             inquiry_q="What relationships between angles does a circle force?",
             teach=[
                 "The angle at the centre is twice the angle at the circumference standing on the same arc. This is the fundamental circle theorem, and the others are consequences of it, so one generalisation covers many cases.",
                 "The proof splits into cases according to whether the centre lies on a side of the inscribed angle. Each case reduces to an isosceles triangle and the exterior angle theorem, and together the cases cover every configuration.",
                 "Angles in the same segment are equal, because each is half the same angle at the centre. The angle in a semicircle is a right angle, because the angle at the centre is 180 degrees.",
                 "A cyclic quadrilateral has opposite angles summing to 180 degrees, because the two opposite angles stand on arcs that together make the whole circumference. This is the theorem that makes cyclic quadrilaterals recognisable.",
             ], examples=[
                 dict(q="An angle at the centre of a circle is 118 degrees and stands on the "
                        "same arc as an angle at the circumference. Find the angle at the "
                        "circumference.",
                      vis=F("table", [["angle", "position", "measure"],
                                      ["at the centre", "standing on arc AB", "118°"],
                                      ["at the circumference", "same arc AB", "59°"],
                                      ["check", "twice 59°", "118°"],
                                      ["other segment", "major arc AB", "121°"]],
                            caption="The centre angle is twice the circumference angle."),
                      reasoning="Apply the angle at the centre theorem directly.",
                      steps=["The angle at the centre is 118 degrees and the angle at the "
                             "circumference stands on the same arc.",
                             "By the theorem, the centre angle is twice the circumference "
                             "angle.",
                             "So the circumference angle is 118 ÷ 2 = 59 degrees.",
                             "Check: 2 × 59 = 118, as required.",
                             "A point on the other arc would give 180 − 59 = 121 degrees, "
                             "because opposite angles of a cyclic quadrilateral sum to 180."],
                      ans="59 degrees",
                      interp="The theorem relates two angles through the arc they share, which "
                             "is why naming the arc is part of the justification."),
                 dict(q="Prove that the angle in a semicircle is a right angle.",
                      vis=F("table", [["step", "claim", "reason"],
                                      ["1", "AB is a diameter, so the arc AB is 180°",
                                       "definition of a diameter"],
                                      ["2", "the angle at the centre on arc AB is 180°",
                                       "straight line"],
                                      ["3", "the angle at C is half of 180°",
                                       "angle at the centre theorem"],
                                      ["4", "the angle at C is 90°", "arithmetic"]],
                            caption="The proof is one application of the main theorem."),
                      reasoning="Treat the diameter as an arc of 180 degrees and apply the "
                               "angle at the centre theorem.",
                      steps=["Let AB be a diameter and C a point on the circle distinct from "
                             "A and B.",
                             "The arc AB is a semicircle, so the angle AOB at the centre is "
                             "180 degrees.",
                             "The angle ACB stands on the same arc AB.",
                             "By the angle at the centre theorem, angle ACB is half of 180 "
                             "degrees.",
                             "Hence angle ACB is 90 degrees, as required."],
                      ans="the angle in a semicircle is 90 degrees",
                      interp="The proof names the theorem it uses and the arc it applies to, "
                             "which is what makes it a proof rather than a description."),
             ], inv=dict(
                 task="Draw a circle with centre O and three points A, B and C on it, with C "
                      "on the major arc AB. Measure the angle AOB, the angle ACB and the "
                      "angle in the alternate segment. Repeat for three different positions "
                      "of C and for two different arcs, and record the relationships you "
                      "find.",
                 table=[["configuration", "angle at centre", "angle at C", "angle in the "
                                "alternate segment"],
                        ["C on the major arc, arc AB = 100°", "100°", "50°", "130°"],
                        ["C moved on the major arc", "100°", "50°", "130°"],
                        ["C on the minor arc", "100°", "50°", "130°"],
                        ["arc AB = 160°", "160°", "80°", "100°"],
                        ["arc AB = 40°", "40°", "20°", "160°"]],
                 notice=["The angle at C did not change when C moved along the same arc.",
                         "The angle at C was always half the angle at the centre.",
                         "The two angles at C, one on each arc, always summed to 180 degrees.",
                         "Changing the arc changed every angle, but not the relationship "
                         "between them."],
                 obs="The angle at the centre is twice the angle at the circumference, and "
                     "the two angles in the two segments are supplementary.",
                 concl="The angle at the centre is twice the angle at the circumference on "
                       "the same arc, and this one theorem explains angles in the same "
                       "segment, the right angle in a semicircle, and the supplementary "
                       "opposite angles of a cyclic quadrilateral. The measurements "
                       "confirmed it in every configuration, with the angle at C always half "
                       "the centre angle.")),
        dict(id="6.2", title="Cyclic quadrilaterals",
             inquiry_q="What does a quadrilateral being cyclic tell you?",
             teach=[
                 "A cyclic quadrilateral is one whose four vertices lie on a circle, so its four points share one space of fixed radius. Its defining property is that opposite angles sum to 180 degrees, and the converse is also true: a quadrilateral with supplementary opposite angles is cyclic.",
                 "The proof of the defining property uses the angle at the centre theorem twice. Each opposite pair of angles stands on arcs that together form the whole circumference, so their halves sum to 180 degrees.",
                 "The converse gives a test for cyclicity that is used constantly: if one pair of opposite angles is supplementary, the fourth vertex lies on the circle through the other three. This is how a circle is constructed to pass through given points.",
                 "An exterior angle of a cyclic quadrilateral equals the interior opposite angle, because the interior angle is supplementary to its opposite and the exterior angle is supplementary to the interior. This is the property used to find an unknown angle quickly.",
             ], examples=[
                 dict(q="A cyclic quadrilateral has angles 3x, 5x, 2x and 4x in order. Find "
                        "each angle.",
                      vis=F("table", [["angle", "expression", "value"],
                                      ["first", "3x", "54°"],
                                      ["second", "5x", "90°"],
                                      ["third", "2x", "36°"],
                                      ["fourth", "4x", "72°"]],
                            caption="Opposite pairs sum to 180 degrees."),
                      reasoning="Use the supplementary property on both pairs of opposite "
                               "angles.",
                      steps=["Opposite angles sum to 180, so 3x + 2x = 180, giving x = 36.",
                             "Check the other pair: 5x + 4x = 9x = 9 × 36 = 324, which is not "
                             "180, so the ordering must be reconsidered.",
                             "The angles are in order around the quadrilateral, so opposite "
                             "pairs are (3x, 2x) and (5x, 4x).",
                             "Both pairs must sum to 180, which requires 5x = 180, so x = 36, "
                             "and then 5x = 180 is impossible for a genuine quadrilateral "
                             "angle.",
                             "The only consistent reading is 3x + 5x = 180 and 2x + 4x = 180, "
                             "both giving x = 22.5, so the angles are 67.5, 112.5, 45 and 90 "
                             "degrees."],
                      ans="67.5°, 112.5°, 45° and 90°",
                      interp="Naming which pairs are opposite is part of the justification, "
                             "and the two conditions must be checked together."),
                 dict(q="Prove that an exterior angle of a cyclic quadrilateral equals the "
                        "interior opposite angle.",
                      vis=F("table", [["step", "claim", "reason"],
                                      ["1", "angle DAB + angle BCD = 180°",
                                       "cyclic quadrilateral"],
                                      ["2", "angle DAE + angle DAB = 180°",
                                       "angles on a straight line"],
                                      ["3", "angle DAE = angle BCD",
                                       "both are 180° − angle DAB"]],
                            caption="Two supplementary claims give the result."),
                      reasoning="Use the cyclic property and the straight-line property "
                               "together.",
                      steps=["Let ABCD be cyclic and let AE extend the side DA beyond A.",
                             "Then angle DAB + angle BCD = 180 degrees, because ABCD is "
                             "cyclic.",
                             "Also angle DAE + angle DAB = 180 degrees, because they lie on a "
                             "straight line.",
                             "Both angle DAE and angle BCD equal 180 degrees minus angle DAB.",
                             "Hence angle DAE = angle BCD, as required."],
                      ans="the exterior angle equals the interior opposite angle",
                      interp="The proof chains two known facts, and each step cites the fact "
                             "it uses."),
             ], inv=dict(
                 task="Draw four cyclic quadrilaterals of your own, each with a different "
                      "shape, and measure all four interior angles of each. Check that "
                      "opposite angles are supplementary in every case. Then draw one "
                      "quadrilateral that is not cyclic and show that the property fails.",
                 table=[["quadrilateral", "angles", "opposite pair 1", "opposite pair 2",
                                "cyclic?"],
                        ["square in a circle", "90, 90, 90, 90", "180", "180", "yes"],
                        ["rectangle in a circle", "70, 110, 70, 110", "180", "180", "yes"],
                        ["kite in a circle", "60, 120, 60, 120", "180", "180", "yes"],
                        ["irregular cyclic", "100, 80, 75, 105", "180", "180", "yes"],
                        ["non-cyclic", "90, 90, 80, 100", "180", "170", "no"]],
                 notice=["Every cyclic quadrilateral had opposite angles summing to 180 "
                         "degrees.",
                         "The non-cyclic quadrilateral failed one of the two pairs, which was "
                         "enough to rule it out.",
                         "The test is an if and only if, so failing it proves non-cyclicity.",
                         "The irregular case confirmed the property is not restricted to "
                         "symmetric shapes."],
                 obs="Cyclicity is decided by one pair of supplementary opposite angles.",
                 concl="A quadrilateral is cyclic exactly when a pair of opposite angles is "
                       "supplementary, and then both pairs are. The exterior angle equals the "
                       "interior opposite angle, which is the quickest way to find an unknown "
                       "angle. The measurements confirmed the property in every cyclic case "
                       "and its failure in the non-cyclic one.")),
        dict(id="6.3", title="Tangents and radii",
             inquiry_q="Why is a tangent perpendicular to the radius at the point of contact?",
             teach=[
                 "A tangent to a circle is a line that meets the circle at exactly one point, called the point of contact. The tangent is perpendicular to the radius drawn to that point, and this is a theorem rather than a definition.",
                 "The proof is by contradiction. If the tangent were not perpendicular to the radius, a foot of the perpendicular from the centre to the line would give a second point of the circle on the line, contradicting the definition of a tangent.",
                 "Two tangents drawn from an external point to a circle are equal in length, and the line from the centre to that point bisects the angle between them. Both facts follow from congruent right-angled triangles.",
                 "The angle between a tangent and a chord equals the angle in the alternate segment, which is the alternate segment theorem. It is the theorem that makes tangents useful for computing angles, and it is proved from the tangent-radius property.",
             ], examples=[
                 dict(q="A point P is 13 cm from the centre O of a circle of radius 5 cm. A "
                        "tangent from P touches the circle at T. Find the length PT.",
                      vis=F("table", [["quantity", "value", "reason"],
                                      ["OP", "13 cm", "given"],
                                      ["OT", "5 cm", "radius"],
                                      ["angle OTP", "90°", "tangent perpendicular to radius"],
                                      ["PT", "12 cm", "Pythagoras: 13² − 5² = 144"]],
                            caption="The tangent forms a right-angled triangle with the "
                                    "radius."),
                      reasoning="Use the tangent-radius property to get a right angle, then "
                               "apply Pythagoras.",
                      steps=["The tangent PT is perpendicular to the radius OT, so triangle "
                             "OTP is right-angled at T.",
                             "By Pythagoras, OP² = OT² + PT².",
                             "So 13² = 5² + PT², giving 169 = 25 + PT².",
                             "Hence PT² = 144 and PT = 12 cm.",
                             "The two tangents from P are both 12 cm, by the equal-tangents "
                             "theorem."],
                      ans="PT = 12 cm",
                      interp="The tangent-radius property converts a tangent problem into a "
                             "Pythagoras problem, which is why it is used so often."),
                 dict(q="Prove that the two tangents drawn to a circle from an external point "
                        "are equal in length.",
                      vis=F("table", [["step", "claim", "reason"],
                                      ["1", "OA = OB", "radii of the same circle"],
                                      ["2", "OP is common", "shared side"],
                                      ["3", "angle OAP = angle OBP = 90°",
                                       "tangent perpendicular to radius"],
                                      ["4", "triangles OAP and OBP are congruent", "RHS"],
                                      ["5", "PA = PB", "corresponding parts"]],
                            caption="Two right-angled triangles share the hypotenuse."),
                      reasoning="Show the two right-angled triangles are congruent and read "
                               "off the equal hypotenuses.",
                      steps=["Let the tangents from P touch the circle at A and B, and let O "
                             "be the centre.",
                             "The radii OA and OB are equal, and OP is common to both "
                             "triangles.",
                             "Both triangles are right-angled, because a tangent is "
                             "perpendicular to the radius at the point of contact.",
                             "So triangles OAP and OBP are congruent by the right angle, "
                             "hypotenuse, side criterion.",
                             "Hence PA = PB, as required."],
                      ans="the two tangents are equal in length",
                      interp="The proof uses the tangent-radius property as one of its "
                             "congruency conditions, which is why that property is proved "
                             "first."),
             ], inv=dict(
                 task="Draw a circle and an external point P. Draw the two tangents from P, "
                      "touching at A and B. Measure PA, PB, the angles at P and the angles at "
                      "A and B. Repeat for three different positions of P and record what "
                      "stays the same and what changes.",
                 table=[["position of P", "PA", "PB", "angle APB", "angle OAP"],
                        ["P close to the circle", "4.1", "4.1", "112°", "90°"],
                        ["P further away", "8.7", "8.7", "64°", "90°"],
                        ["P far away", "19.4", "19.4", "30°", "90°"],
                        ["P on the other side", "8.7", "8.7", "64°", "90°"]],
                 notice=["The two tangent lengths were equal in every case.",
                         "The angles at the points of contact were always 90 degrees.",
                         "The angle at P shrank as P moved away from the circle.",
                         "Moving P to the other side changed nothing except the orientation."],
                 obs="The tangent lengths from a point are equal, and the tangent is always "
                     "perpendicular to the radius.",
                 concl="A tangent is perpendicular to the radius at the point of contact, "
                       "which is proved by contradiction from the definition of a tangent. "
                       "Two consequences follow immediately: the two tangents from an "
                       "external point are equal, and the line from the centre to that point "
                       "bisects the angle between them. The measurements confirmed both, "
                       "with PA = PB in every case.")),
        dict(id="6.4", title="Chords, secants and the alternate segment",
             inquiry_q="How do the lengths of intersecting chords relate?",
             teach=[
                 "When two chords AB and CD intersect inside a circle at X, the products AX × XB and CX × XD are equal. This is the intersecting chords theorem, and it follows from the similarity of the triangles formed.",
                 "The similarity comes from the equal angles: the angles at X are vertically opposite, and the angles subtended by the same arc are equal. Equal angles give similar triangles, and similar triangles give the equal ratios.",
                 "When two secants meet outside the circle, the product of the whole secant and its external part is the same for both. The tangent case is the limit of this, giving the tangent-secant theorem.",
                 "The alternate segment theorem states that the angle between a tangent and a chord equals the angle in the alternate segment. It is proved by drawing the radius to the point of contact and using the tangent-radius property together with the angle at the centre theorem.",
             ], examples=[
                 dict(q="Two chords AB and CD intersect at X inside a circle, with AX = 3, "
                        "XB = 4, CX = 2. Find XD.",
                      vis=F("table", [["segment", "length", "product"],
                                      ["AX", "3", "—"],
                                      ["XB", "4", "—"],
                                      ["AX × XB", "12", "—"],
                                      ["CX × XD", "2 × XD", "= 12"]],
                            caption="The two products are equal."),
                      reasoning="Apply the intersecting chords theorem and solve for the "
                               "unknown length.",
                      steps=["By the intersecting chords theorem, AX × XB = CX × XD.",
                             "So 3 × 4 = 2 × XD, giving 12 = 2 × XD.",
                             "Hence XD = 6.",
                             "Check: 2 × 6 = 12, which equals 3 × 4.",
                             "The result is independent of where X lies along CD, so long as "
                             "the products are formed correctly."],
                      ans="XD = 6",
                      interp="The theorem converts a length problem into a product equation, "
                             "and the check is the equality of the two products."),
                 dict(q="Prove the alternate segment theorem: the angle between a tangent at "
                        "A and a chord AB equals the angle in the alternate segment.",
                      vis=F("table", [["step", "claim", "reason"],
                                      ["1", "OA is perpendicular to the tangent",
                                       "tangent-radius property"],
                                      ["2", "angle OAB = angle OBA",
                                       "isosceles triangle OAB"],
                                      ["3", "angle between tangent and AB = 90° − angle OAB",
                                       "straight angle"],
                                      ["4", "angle at the centre = 2 × angle ACB",
                                       "angle at the centre theorem"],
                                      ["5", "angle at the centre = 180° − 2 angle OAB",
                                       "angle sum of triangle OAB"],
                                      ["6", "angle ACB = 90° − angle OAB",
                                       "combining steps 4 and 5"]],
                            caption="The proof chains three circle theorems."),
                      reasoning="Express both angles in terms of the base angle of the "
                               "isosceles triangle and compare.",
                      steps=["Let the tangent at A meet the chord AB, and let C be a point on "
                             "the circle in the alternate segment.",
                             "The radius OA is perpendicular to the tangent, so the angle "
                             "between the tangent and AB is 90 degrees minus angle OAB.",
                             "Triangle OAB is isosceles, so angle OAB = angle OBA.",
                             "The angle at the centre AOB is 180 degrees minus twice angle "
                             "OAB, and it is twice angle ACB.",
                             "So angle ACB is 90 degrees minus angle OAB, which equals the "
                             "angle between the tangent and the chord."],
                      ans="the angle between the tangent and the chord equals the angle in "
                          "the alternate segment",
                      interp="The proof is a chain of three theorems, and each link is "
                             "named."),
             ], inv=dict(
                 task="Draw a circle and two chords intersecting inside it. Measure the four "
                      "segments and check the intersecting chords theorem. Then draw a "
                      "tangent and a chord from the point of contact, and check the alternate "
                      "segment theorem against an angle in the alternate segment. Repeat for "
                      "a second circle.",
                 table=[["measurement", "circle 1", "circle 2", "relationship"],
                        ["AX × XB", "2 × 6 = 12", "3 × 4 = 12", "—"],
                        ["CX × XD", "4 × 3 = 12", "6 × 2 = 12", "equal to AX × XB"],
                        ["tangent-chord angle", "38°", "52°", "—"],
                        ["angle in alternate segment", "38°", "52°", "equal to the "
                         "tangent-chord angle"]],
                 notice=["The two products were equal in both circles.",
                         "The tangent-chord angle equalled the angle in the alternate segment "
                         "in both cases.",
                         "The second circle had the angle pairs swapped, which showed the "
                         "relationship is not a coincidence of one diagram.",
                         "Both theorems held regardless of where the chords crossed."],
                 obs="Intersecting chords give equal products, and a tangent-chord angle "
                     "equals the alternate segment angle.",
                 concl="The intersecting chords theorem follows from the similarity of the "
                       "triangles formed by the chords, which in turn follows from equal "
                       "angles. The alternate segment theorem follows from the "
                       "tangent-radius property and the angle at the centre theorem. The "
                       "measurements confirmed both, with the products equal and the angle "
                       "pairs equal in each circle.")),
        dict(id="6.5", title="Constructing and writing proofs",
             inquiry_q="What makes a geometric argument a proof?",
             teach=[
                 "A proof is a sequence of statements, each justified by a definition, a previously proved result, or a given fact. The logic of the chain is the proof: a list of true statements without reasons is a description.",
                 "Proofs in circle geometry are usually written in two columns, or as a numbered chain with the reason beside each step. Either form is acceptable provided every step is justified and the conclusion follows by logic alone.",
                 "A proof by contradiction assumes the opposite of what is to be proved and derives a statement that contradicts a known fact. It is the natural form for the tangent-radius property, because the definition of a tangent is a statement about the number of intersection points.",
                 "The converse of a proved result is a separate claim that needs its own proof. The angle-in-a-semicircle theorem and its converse are both true, but neither follows from the other.",
             ], examples=[
                 dict(q="Prove that if a pair of opposite angles of a quadrilateral is "
                        "supplementary then the quadrilateral is cyclic.",
                      vis=F("table", [["step", "claim", "reason"],
                                      ["1", "suppose D is not on the circle through A, B, C",
                                       "assumption for contradiction"],
                                      ["2", "let the circle meet BD again at E",
                                       "construction"],
                                      ["3", "angle AEB = 180° − angle BCD",
                                       "cyclic quadrilateral ABCE"],
                                      ["4", "angle AEB = angle ADB", "E lies on BD"],
                                      ["5", "angle ADB = 180° − angle BCD",
                                       "combining steps 3 and 4"],
                                      ["6", "D and E coincide", "both satisfy the same "
                                       "condition on the line BD"]],
                            caption="A contradiction proof constructs a second point."),
                      reasoning="Assume the fourth vertex is off the circle, construct the "
                               "point on the circle, and show the two must coincide.",
                      steps=["Let ABCD have angle DAB + angle BCD = 180 degrees.",
                             "Suppose D is not on the circle through A, B and C.",
                             "Let that circle meet the line BD again at E, so ABCE is cyclic.",
                             "Then angle AEB = 180 degrees minus angle BCD, which equals "
                             "angle ADB.",
                             "So D and E make the same angle with AB while lying on the same "
                             "line, and hence coincide.",
                             "This contradicts the assumption, so D lies on the circle and "
                             "ABCD is cyclic."],
                      ans="the quadrilateral is cyclic",
                      interp="The proof is by contradiction, and the contradiction is that "
                             "two points with the same position must be distinct."),
                 dict(q="Write a proof that the perpendicular from the centre of a circle to "
                        "a chord bisects the chord.",
                      vis=F("table", [["step", "claim", "reason"],
                                      ["1", "OM is perpendicular to chord AB",
                                       "construction"],
                                      ["2", "OA = OB", "radii"],
                                      ["3", "OM is common", "shared side"],
                                      ["4", "triangles OMA and OMB are congruent", "RHS"],
                                      ["5", "AM = MB", "corresponding parts"]],
                            caption="Two right-angled triangles with a shared hypotenuse."),
                      reasoning="Form two congruent right-angled triangles and read off the "
                               "equal segments.",
                      steps=["Let M be the foot of the perpendicular from the centre O to the "
                             "chord AB.",
                             "The radii OA and OB are equal, and OM is common.",
                             "Both triangles OMA and OMB are right-angled at M.",
                             "So they are congruent by the right angle, hypotenuse, side "
                             "criterion.",
                             "Hence AM = MB, so M bisects the chord."],
                      ans="the perpendicular from the centre bisects the chord",
                      interp="The proof is short because the congruency is immediate, and "
                             "every step cites its reason."),
             ], inv=dict(
                 task="Take four circle theorems from this chapter: the angle at the centre "
                      "theorem, the angle in a semicircle, the tangent-radius property and "
                      "the perpendicular from the centre to a chord. For each, write out a "
                      "complete proof with a reason beside every step, and then state the "
                      "converse and decide whether it is true.",
                 table=[["theorem", "proof method", "converse", "converse true?"],
                        ["angle at the centre", "isosceles triangle plus exterior angle",
                         "if a centre angle is twice a circumference angle on the same arc "
                         "then the four points are concyclic", "yes"],
                        ["angle in a semicircle", "special case of the above",
                         "if a right angle is subtended by a segment then the segment is a "
                         "diameter", "yes"],
                        ["tangent-radius", "contradiction from the definition of a tangent",
                         "if a line through a point of a circle is perpendicular to the "
                         "radius then it is a tangent", "yes"],
                        ["perpendicular bisects chord", "congruent triangles",
                         "the line from the centre to the midpoint of a chord is "
                         "perpendicular to it", "yes"]],
                 notice=["Two proofs used congruent triangles and two used a contradiction or "
                         "a reduction to an earlier result.",
                         "Every converse turned out to be true, but each needed its own "
                         "proof.",
                         "The angle in a semicircle was the quickest, because it was a "
                         "special case.",
                         "Writing the reasons beside the steps exposed the assumptions "
                         "immediately."],
                 obs="A proof is a chain of justified statements, and the converse of a true "
                     "statement is a separate claim.",
                 concl="A geometric proof is a sequence of statements each justified by a "
                       "definition, a given, or a previously proved result, and the "
                       "justification is what distinguishes it from a description. The "
                       "converse of a proved result is a separate claim requiring its own "
                       "proof, and all four converses here were true.")),
        dict(id="6.6", title="Investigation: circle theorems under transformation",
             inquiry_q="Which circle properties survive a transformation?",
             teach=[
                 "A circle is defined by a centre and a radius, so any transformation that preserves distances preserves circles. Translations, rotations and reflections all send circles to circles, and enlargements send circles to circles with a scaled radius.",
                 "An enlargement with centre on the circle sends the circle to a line, which is the tangent at that centre in the limit. This is the transformation view of a tangent: it is the image of a circle under an enlargement about a point of the circle.",
                 "Angles are preserved by all of these transformations, so every circle theorem is invariant under them. A theorem proved for one configuration is therefore proved for every configuration obtained by a transformation, which is why one diagram is enough.",
                 "Inversion in a circle is a transformation that sends circles to circles and lines to circles, and it is the transformation in which the intersecting chords theorem becomes most transparent. It is the tool behind many advanced results in circle geometry.",
             ], examples=[
                 dict(q="A circle of radius 3 with centre (2, 5) is translated by the vector "
                        "(−4, 1) and then enlarged by factor 2 about the origin. Find the "
                        "final centre and radius.",
                      vis=F("table", [["stage", "centre", "radius"],
                                      ["original", "(2, 5)", "3"],
                                      ["after translation", "(−2, 6)", "3"],
                                      ["after enlargement", "(−4, 12)", "6"]],
                            caption="Distances are scaled, so the radius scales too."),
                      reasoning="Apply each transformation to the centre and scale the radius "
                               "by the enlargement factor.",
                      steps=["The original centre is (2, 5) and the radius is 3.",
                             "Translation by (−4, 1) moves the centre to (−2, 6).",
                             "An enlargement of factor 2 about the origin multiplies every "
                             "distance from the origin by 2.",
                             "So the centre moves to (−4, 12) and the radius becomes 6.",
                             "The image is a circle, because translations and enlargements "
                             "preserve circles."],
                      ans="centre (−4, 12), radius 6",
                      interp="Tracking the centre and the radius is enough, because the shape "
                             "of a circle is determined by those two quantities."),
                 dict(q="Explain why a tangent can be regarded as the limit of circles under "
                        "an enlargement about a point of the circle.",
                      vis=F("table", [["factor", "image of the circle about a point on it",
                                       "behaviour"],
                                      ["1", "the circle itself", "unchanged"],
                                      ["2", "a larger circle through the centre",
                                       "curvature halves"],
                                      ["10", "a much larger circle", "locally nearly "
                                       "straight"],
                                      ["limit", "a straight line", "the tangent"]],
                            caption="Larger circles look straighter near the point."),
                      reasoning="An enlargement about a point of the circle increases the "
                               "radius without bound, and a circle of infinite radius is a "
                               "line.",
                      steps=["An enlargement of factor k about a point P on the circle keeps "
                             "P fixed and multiplies the radius by k.",
                             "The curvature of a circle is the reciprocal of its radius, so "
                             "the curvature is divided by k.",
                             "As k grows, the curvature tends to zero and the circle becomes "
                             "locally straight.",
                             "The limiting line passes through P and is perpendicular to the "
                             "radius OP.",
                             "That line is the tangent, which is why the tangent is "
                             "perpendicular to the radius."],
                      ans="the tangent is the limit of the images, and it is perpendicular to "
                          "the radius",
                      interp="The transformation view explains the tangent-radius property "
                             "rather than merely restating it."),
             ], inv=dict(
                 task="Draw a circle with a chord and an inscribed angle. Apply a "
                      "translation, a rotation, a reflection and an enlargement to the whole "
                      "figure, and measure the inscribed angle in each image. Then repeat "
                      "with the alternate segment theorem, and record which quantities change "
                      "and which stay the same.",
                 table=[["transformation", "inscribed angle", "arc length", "radius",
                                "chord length"],
                        ["none", "42°", "84°", "5", "7.2"],
                        ["translation", "42°", "84°", "5", "7.2"],
                        ["rotation", "42°", "84°", "5", "7.2"],
                        ["reflection", "42°", "84°", "5", "7.2"],
                        ["enlargement, factor 3", "42°", "252°", "15", "21.6"]],
                 notice=["The inscribed angle survived every transformation.",
                         "The isometries left every measurement unchanged.",
                         "The enlargement multiplied the lengths by 3 but left the angles "
                         "alone.",
                         "The alternate segment angle was likewise unchanged in every case."],
                 obs="Angles are preserved by all four transformations, and lengths only by "
                     "the isometries.",
                 concl="Translations, rotations and reflections preserve both angles and "
                       "lengths, and enlargements preserve angles while scaling lengths. "
                       "Every circle theorem is therefore invariant under all of them, which "
                       "is why a single diagram is enough to establish a circle theorem: any "
                       "other configuration is obtained by a transformation, and the "
                       "transformation preserves the quantities the theorem relates.")),
        dict(id="6.7", title="Mixed practice",
             inquiry_q="Which theorem does this figure need?",
             teach=[
                 "Every circle question begins by naming the theorem that applies. Naming it forces the relevant arc, chord or tangent to be identified, and the identification is most of the work.",
                 "A complete answer states the theorem in full, applies it to the named parts, and derives the required quantity. Omitting the statement of the theorem leaves the answer a calculation without a justification.",
                 "Proofs in this chapter are chains of at most five steps, each citing a definition, a given, or an earlier theorem. Writing the reason beside each step is the discipline that makes the chain checkable.",
                 "Mixed practice is where the theorem is chosen rather than given, so the reasoning behind the choice is part of what is being practised.",
             ], examples=[
                 dict(q="A chord of length 8 cm is 3 cm from the centre of a circle. Find the "
                        "radius.",
                      vis=F("table", [["step", "working", "result"],
                                      ["half-chord", "8 ÷ 2 = 4", "—"],
                                      ["right triangle", "r² = 4² + 3²", "—"],
                                      ["radius", "r² = 25", "r = 5"]],
                            caption="The perpendicular from the centre bisects the chord."),
                      reasoning="Use the perpendicular-bisector property to form a "
                               "right-angled triangle, then apply Pythagoras.",
                      steps=["The perpendicular from the centre to the chord bisects it, so "
                             "half the chord is 4 cm.",
                             "The distance from the centre to the chord is 3 cm.",
                             "The radius, the half-chord and the distance form a right-angled "
                             "triangle.",
                             "So r² = 4² + 3² = 16 + 9 = 25.",
                             "Hence r = 5 cm."],
                      ans="radius 5 cm",
                      interp="The perpendicular-bisector property is what makes the "
                             "right-angled triangle available, and it must be named."),
                 dict(q="Two tangents from P touch a circle of radius 6 at A and B, and the "
                        "angle APB is 70 degrees. Find the angle AOB and the length PA.",
                      vis=F("table", [["step", "working", "result"],
                                      ["right angles", "angle OAP = 90°", "—"],
                                      ["quadrilateral", "angle AOB = 180° − 70°", "110°"],
                                      ["Pythagoras", "PA² = OP² − 36", "—"],
                                      ["half-angle", "angle APO = 35°", "bisected"]],
                            caption="The two tangents and the two radii form a "
                                    "quadrilateral."),
                      reasoning="Use the tangent-radius property and the angle sum of the "
                               "quadrilateral, then Pythagoras.",
                      steps=["The radii OA and OB are perpendicular to the tangents at A and "
                             "B.",
                             "So the quadrilateral OAPB has angles 90, 70, 90 and angle AOB.",
                             "The angle sum is 360, so angle AOB = 360 − 250 = 110 degrees.",
                             "The line OP bisects the angle APB, so angle APO is 35 degrees.",
                             "In the right-angled triangle OAP, tan 35° = 6/PA, so "
                             "PA = 6 ÷ tan 35° ≈ 8.56 cm."],
                      ans="angle AOB = 110 degrees; PA ≈ 8.56 cm",
                      interp="The two properties used are the tangent-radius property and the "
                             "equal-tangents theorem, and both must be named."),
             ], inv=dict(
                 task="Take a circle of radius 5 with a point P at distance 13 from the "
                      "centre. Draw the two tangents from P and the chord of contact AB. "
                      "Find the angle APB, the length of AB, the angle AOB and the area of "
                      "the quadrilateral OAPB, and name the theorem used at each step.",
                 table=[["quantity", "method", "answer"],
                        ["length of a tangent", "Pythagoras: √(13² − 5²)", "12"],
                        ["angle APB", "2 arctan(5/12)", "45.2°"],
                        ["angle AOB", "180° − angle APB", "134.8°"],
                        ["chord AB", "2 × 5 × sin(angle AOB ÷ 2)", "9.23"],
                        ["area of OAPB", "2 × (1/2 × 5 × 12)", "60"]],
                 notice=["Every quantity came from the tangent-radius property plus one "
                         "further theorem.",
                         "The area of the quadrilateral was twice the area of one "
                         "right-angled triangle.",
                         "The chord of contact was found from the isosceles triangle OAB.",
                         "Naming the theorem at each step made the whole solution checkable."],
                 obs="The tangent-radius property converts every tangent question into a "
                     "right-angled triangle question.",
                 concl="A circle question is solved by naming the theorem that applies, "
                       "stating it in full, and applying it to the named parts. The "
                       "tangent-radius property, the equal-tangents theorem and the "
                       "perpendicular-bisector property between them handle most tangent and "
                       "chord questions, and each answer cites the property it uses. Here "
                       "the tangent was 12, the angle APB was about 45.2 degrees and the "
                       "chord of contact was about 9.23.")),
    ],
    practice=dict(
        A=[("6.1.1", "An angle at the centre is 96 degrees and stands on the same arc as an "
            "angle at the circumference. Find the angle at the circumference.",
            "48 degrees.", "The centre angle is twice the circumference angle.", "F"),
           ("6.1.2", "An angle in a semicircle is a right angle. Explain why.",
            "Because the diameter subtends 180 degrees at the centre, and the angle at the "
            "circumference is half of that.", "Apply the angle at the centre theorem.", "R"),
           ("6.1.3", "A cyclic quadrilateral has angles 70, 110 and 85 degrees. Find the "
            "fourth.",
            "95 degrees.", "Opposite angles of a cyclic quadrilateral sum to 180.", "F"),
           ("6.1.4", "A chord is 6 cm from the centre of a circle of radius 10 cm. Find the "
            "chord length.",
            "2√(100 − 36) = 2 × 8 = 16 cm.", "The perpendicular from the centre bisects the "
            "chord.", "F"),
           ("6.1.5", "A tangent from P touches a circle of radius 5 at T, and OP = 13. Find "
            "PT.",
            "12 cm.", "Pythagoras in the right-angled triangle OTP.", "F"),
           ("6.1.6", "Two chords intersect with segments 3 and 4 on one chord and 2 and x on "
            "the other. Find x.",
            "x = 6.", "Intersecting chords: 3 × 4 = 2 × x.", "F"),
           ("6.1.7", "The angle between a tangent and a chord is 35 degrees. Find the angle "
            "in the alternate segment.",
            "35 degrees.", "Alternate segment theorem.", "F"),
           ("6.1.8", "A cyclic quadrilateral has an exterior angle of 62 degrees at one "
            "vertex. Find the interior opposite angle.",
            "62 degrees.", "An exterior angle equals the interior opposite angle.", "F"),
           ("6.1.9", "Two tangents from P touch a circle at A and B, and PA = 9. Find PB.",
            "9.", "Tangents from an external point are equal.", "F"),
           ("6.1.10", "An angle at the circumference standing on a major arc is 40 degrees. "
            "Find the angle at the centre on the same arc.",
            "80 degrees.", "The centre angle is twice the circumference angle.", "F"),
           ("6.1.11", "A circle has radius 7 and a chord of length 10. Find the distance from "
            "the centre to the chord.",
            "√(49 − 25) = √24 ≈ 4.90.", "Half the chord is 5, then use Pythagoras.", "R"),
           ("6.1.12", "Prove that the perpendicular from the centre of a circle to a chord "
            "bisects the chord.",
            "The two right-angled triangles formed have equal hypotenuses (radii) and a "
            "shared side, so they are congruent and the two segments are equal.",
            "Congruent triangles.", "R")],
        B=[("6.2.1", "Investigate the angle at the centre theorem by drawing three circles "
            "with different arcs and measuring the pairs of angles, and justify the "
            "relationship.",
            "In every case the angle at the centre was twice the angle at the circumference "
            "on the same arc.",
            "Measure and compare, then prove with an isosceles triangle.", "R"),
           ("6.2.2", "Conjecture a rule for the angle between two tangents from an external "
            "point and the angle at the centre between the radii, and test it.",
            "They are supplementary: the quadrilateral formed has two right angles, so the "
            "two remaining angles sum to 180 degrees.",
            "Use the angle sum of the quadrilateral.", "R"),
           ("6.2.3", "Investigate the locus of points from which the two tangents to a circle "
            "are perpendicular, and justify.",
            "The locus is the circle concentric with the original and of radius r√2, because "
            "a right angle at P forces OP = r√2.",
            "Use the right-angled triangle OPT.", "C"),
           ("6.2.4", "Investigate whether a rectangle is always cyclic, and justify.",
            "Yes, because opposite angles are both 90 degrees and so sum to 180, which is "
            "the condition for a cyclic quadrilateral.",
            "Apply the cyclic quadrilateral test.", "R"),
           ("6.2.5", "Investigate the length of the chord of contact AB in terms of the "
            "radius r and the distance d from the centre to the external point.",
            "AB = 2r√(1 − r²/d²), because half the chord is r√(1 − r²/d²) in the isosceles "
            "triangle OAB.",
            "Split the isosceles triangle OAB and use Pythagoras.", "C"),
           ("6.2.6", "Conjecture a rule for when two circles have exactly two common "
            "tangents, and test it on three pairs.",
            "Exactly two common tangents when the circles intersect in two points; four when "
            "they are separate; none when one lies inside the other.",
            "Draw the pairs and count the tangents.", "R"),
           ("6.2.7", "Investigate the angle in the alternate segment for a tangent and a "
            "diameter, and justify the result.",
            "The angle is 90 degrees, because the chord is a diameter and the angle in a "
            "semicircle is a right angle; this also confirms the tangent is perpendicular to "
            "the radius.",
            "Combine the alternate segment and semicircle theorems.", "R"),
           ("6.2.8", "Investigate the locus of the centre of a circle tangent to two "
            "intersecting lines, and justify.",
            "The locus is the pair of angle bisectors, because the centre "
            "must be equidistant from both lines.",
            "Use the fact that the centre lies on the bisector of the angle "
            "between the tangents.", "R"),
           ("6.2.9", "Conjecture a rule for the angle between two tangents from a "
            "point at distance d from the centre of a circle of radius r, "
            "and test it.",
            "The angle is 2 arccos(r/d), because the line from the centre "
            "to the point bisects the angle and forms a right triangle.",
            "Bisect the angle and use the right-angled triangle.", "C"),
           ("6.2.10", "Investigate whether every rhombus is cyclic, and justify.",
            "No: a cyclic quadrilateral needs supplementary opposite "
            "angles, and a rhombus has them supplementary only when it is a "
            "square.",
            "Apply the cyclic quadrilateral test.", "R"),
           ("6.2.11", "Investigate the common chord of two intersecting circles and "
            "justify that it is perpendicular to the line of centres.",
            "The common chord is perpendicular to the line of centres and "
            "is bisected by it, because both centres are equidistant from "
            "the chord's endpoints.",
            "Use congruent triangles with the two radii.", "C"),
           ],
        C=[("6.3.1", "Write a complete solution to finding the radius of a circle in which a "
            "chord of length 24 is 5 cm from the centre.",
            "r² = 12² + 5² = 169, so r = 13 cm.",
            "Halve the chord and use Pythagoras.", "R"),
           ("6.3.2", "Write a complete solution to proving that the angle in a semicircle is "
            "a right angle.",
            "The diameter subtends 180 degrees at the centre, and the angle at the "
            "circumference is half the angle at the centre on the same arc, so it is 90 "
            "degrees.",
            "Apply the angle at the centre theorem.", "R"),
           ("6.3.3", "Write a complete solution to finding the angle between two tangents "
            "from P to a circle of radius 6 when OP = 10.",
            "In the right triangle OAP, sin(half the angle) = 6/10, so the half-angle is "
            "36.87 degrees and the angle is 73.74 degrees.",
            "Bisect the angle and use the right-angled triangle.", "R"),
           ("6.3.4", "Write a complete solution to proving that the two tangents from an "
            "external point are equal.",
            "The two right-angled triangles have equal radii, a shared hypotenuse and a "
            "right angle, so they are congruent and the tangents are equal.",
            "Congruent triangles.", "R"),
           ("6.3.5", "Write a complete solution to finding the length of the chord of "
            "contact when the tangents from P meet at 60 degrees and the radius is 8.",
            "Half the angle is 30 degrees, so in the right triangle OAP, tan 30° = 8/PA "
            "gives PA = 8√3 ≈ 13.86; the chord AB = 2 × 8 × sin(angle AOB/2) with "
            "angle AOB = 120 degrees, so AB = 16 × sin 60° = 8√3 ≈ 13.86.",
            "Bisect, use the tangent-radius property, then the isosceles triangle OAB.", "C"),
           ("6.3.6", "Write a complete solution to proving the intersecting chords theorem "
            "for chords meeting inside a circle.",
            "The triangles formed have equal angles — vertically opposite at the "
            "intersection and equal from the same arc — so they are similar, and the "
            "corresponding sides give AX × XB = CX × XD.",
            "Similar triangles from equal angles.", "C"),
           ("6.3.7", "Write a complete solution to finding the angle between a tangent and a "
            "chord that subtends an angle of 44 degrees in the alternate segment.",
            "44 degrees, by the alternate segment theorem.",
            "State the theorem and apply it.", "F"),
           ("6.3.8", "Write a complete solution to finding the radius of a circle in "
            "which a chord of length 30 is 8 cm from the centre.",
            "r² = 15² + 8² = 289, so r = 17 cm.",
            "Halve the chord and use Pythagoras.", "R"),
           ("6.3.9", "Write a complete solution to proving that an exterior angle of "
            "a cyclic quadrilateral equals the interior opposite angle.",
            "The exterior angle and the interior opposite are both "
            "supplementary to the same interior angle, so they are equal.",
            "Use the cyclic property and the straight-line property.", "R"),
           ("6.3.10", "Write a complete solution to finding the angle at the centre "
            "subtended by a chord of length 9 in a circle of radius 7.5.",
            "Half the chord is 4.5, so sin of half the angle is 4.5/7.5 = "
            "0.6, giving a half-angle of 36.87° and a full angle of 73.74°.",
            "Halve the chord and use a sine ratio in the isosceles "
            "triangle.", "R"),
           ("6.3.11", "Write a complete solution to finding the area of the region "
            "between a tangent from P and a circle of radius 6 when OP = "
            "10.",
            "The tangent is 8 and the angle at the centre is 2 arccos(6/10) "
            "≈ 106.26°, so the quadrilateral has area ½ × 6 × 8 × 2 = 48 "
            "and the sector has area ½ × 36 × 1.8545 ≈ 33.4, giving a "
            "difference of about 14.6.",
            "Subtract the sector from the kite formed by the two radii and "
            "two tangents.", "C"),
           ("6.3.12", "Write a complete solution to proving the converse of the angle "
            "in a semicircle.",
            "If angle ACB = 90° then the midpoint O of AB is equidistant "
            "from A, B and C, so C lies on the circle with AB as diameter.",
            "Show the midpoint of AB is equidistant from all three "
            "vertices.", "C"),
           ],
        D=[("6.4.1", "A surveyor stands 40 m from the foot of a tower and measures the angle "
            "of elevation to the top as 28 degrees. Find the height of the tower.",
            "40 tan 28° ≈ 21.3 m.", "Right-angled trigonometry with the tangent-radius "
            "property supplying the right angle.", "A"),
           ("6.4.2", "A circular garden of radius 12 m is enclosed by a fence tangent to it "
            "at three points, each pair of fence sections meeting at 90 degrees. Find the "
            "length of each fence section.",
            "Each section is a tangent of length 12√2 ≈ 17.0 m, because the angle at the "
            "corner is 90 degrees and so is supplementary to a 90 degree angle at the centre, "
            "giving OP = 12√2.",
            "Use the tangent-radius property and Pythagoras.", "A"),
           ("6.4.3", "A wheel of radius 30 cm rolls along a straight track. Describe the path "
            "of a point on the rim and explain why the track is tangent to the wheel at every "
            "instant.",
            "The path is a cycloid; the track is tangent to the wheel because the point of "
            "contact has zero velocity, so the wheel touches without slipping.",
            "The tangent-radius property describes the contact at each instant.", "A"),
           ("6.4.4", "An architect designs a window as a semicircle on top of a rectangle. "
            "The rectangle is 1.6 m wide and the semicircle has radius 0.8 m. Find the total "
            "height of the window if the rectangle is 1.2 m tall.",
            "1.2 + 0.8 = 2.0 m.", "The semicircle adds its radius to the height.", "A"),
           ("6.4.5", "A roundabout of radius 8 m is surrounded by a path 2 m wide. Find the "
            "length of the outer edge of the path.",
            "2π × 10 = 20π ≈ 62.8 m.", "The outer edge is a circle of radius 10.", "A"),
           ("6.4.6", "A lighthouse beam sweeps a circle of radius 20 km. A ship is 15 km "
            "from the lighthouse. Find the angle through which the beam must turn for the "
            "ship to pass from the edge of the beam to the closest point.",
            "arccos(15/20) ≈ 41.4 degrees.",
            "The beam is tangent to the circle of visibility at the edge.", "A"),
           ("6.4.7", "A student claims that any quadrilateral with one pair of opposite "
            "angles supplementary is cyclic. Investigate and justify.",
            "True: if one pair sums to 180 degrees then the fourth vertex lies on the circle "
            "through the other three, so the quadrilateral is cyclic, and the other pair then "
            "sums to 180 as well.",
            "Use the converse of the cyclic quadrilateral theorem.", "R"),
           ("6.4.8", "A circular medallion of radius 4 cm is to be framed by a square frame "
            "touching it on all four sides. Find the side of the square and the area of "
            "frame not covered by the medallion.",
            "The side is 8 cm; the uncovered area is 64 − 16π ≈ 13.7 cm².",
            "The square's side is the diameter; subtract the circle's area.", "A"),
           ("6.4.9", "A pulley of radius 10 cm drives a belt that also passes round a pulley "
            "of radius 4 cm with centres 30 cm apart. Find the length of the belt.",
            "The straight sections are each √(30² − 6²) ≈ 29.4 cm; the arc angles are "
            "π − 2 arcsin(0.2) on the large pulley and π + 2 arcsin(0.2) on the small, giving "
            "a total of about 70.4 cm.",
            "The belt is tangent to both pulleys, so each straight section is a common "
            "tangent.", "A"),
           ("6.4.10", "A student draws a circle, marks a point outside it and draws two "
            "lines through the point that each cut the circle twice, claiming they are "
            "secants. Investigate the products of the segments and justify.",
            "For two secants from the same external point, the product of the whole secant "
            "and its external part is the same for both, by similarity of the triangles "
            "formed.",
            "Use the secant theorem, a generalisation of the intersecting chords theorem.",
            "C"),
           ("6.4.11", "An ornamental pattern is built from a circle with four equal chords "
            "meeting at a point inside. Investigate the products of the segments and relate "
            "them to the intersecting chords theorem.",
            "The products are equal for any two chords through the point, so with four equal "
            "chords the segments pair up so that each product is the same.",
            "Apply the intersecting chords theorem.", "R"),
           ("6.4.12", "A student proves the tangent-radius property by contradiction. Write "
            "out the proof and explain each step.",
            "Suppose the tangent is not perpendicular to the radius; then the foot of the "
            "perpendicular from the centre to the line is a different point of the circle on "
            "the line, giving two intersection points and contradicting the definition of a "
            "tangent.",
            "Contradiction from the definition of a tangent.", "R")],
    ),
    assessment=[
        dict(title="A1 · The window design",
             text="A stained-glass window is a circle of radius 60 cm with three chords "
                  "meeting at a point 25 cm from the centre. One chord is divided into "
                  "segments of 15 cm and 35 cm. Find the segments of a second chord passing "
                  "through the same point, and the angle at the centre subtended by the "
                  "shorter segment of the first chord.",
             note="Criteria C and D · apply the intersecting chords theorem and the angle at "
                  "the centre theorem, justifying each step."),
        dict(title="A2 · The circular garden",
             text="A circular garden of radius 10 m has a straight path tangent to it at one "
                  "point and a second path meeting the first at 50 degrees, both tangent to "
                  "the garden. Find the length of each path from the corner to its point of "
                  "contact, the angle at the centre between the two radii to the points of "
                  "contact, and the area of the region enclosed by the two paths and the "
                  "minor arc between the contact points.",
             note="Criteria C and D · use the tangent-radius property and the "
                  "equal-tangents theorem, then compute the area."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of logic and the related concepts of space, generalisation "
        "and justification appear in your work?",
        "How is the global context of personal and cultural expression, and its exploration "
        "of the geometry of architecture and ornament, visible in the investigations and "
        "examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of a diagram as a justification, and what would you still "
        "like to ask?",
    ],
    review=dict(
        ideas=["The angle at the centre is twice the angle at the circumference on the same "
               "arc.",
               "Angles in the same segment are equal.",
               "The angle in a semicircle is a right angle.",
               "Opposite angles of a cyclic quadrilateral are supplementary.",
               "An exterior angle of a cyclic quadrilateral equals the interior opposite "
               "angle.",
               "A tangent is perpendicular to the radius at the point of contact.",
               "The two tangents from an external point are equal in length.",
               "The angle between a tangent and a chord equals the angle in the alternate "
               "segment.",
               "For intersecting chords, AX × XB = CX × XD.",
               "The perpendicular from the centre to a chord bisects the chord."],
        vocab=["circle", "centre", "radius", "diameter", "chord", "arc", "tangent", "secant",
               "point of contact", "cyclic quadrilateral", "alternate segment",
               "angle at the centre", "angle at the circumference", "concyclic", "proof by "
               "contradiction", "congruent", "similar"],
        mixed=[("6.R1", "An angle at the circumference is 33 degrees. Find the angle at the "
                "centre on the same arc."),
               ("6.R2", "A chord is 9 cm from the centre of a circle of radius 15 cm. Find "
                "the chord length."),
               ("6.R3", "A cyclic quadrilateral has angles 3x, 4x, 2x and 5x in order. Find "
                "each angle."),
               ("6.R4", "A tangent from P touches a circle of radius 7, with OP = 25. Find "
                "the tangent length."),
               ("6.R5", "Two chords meet with segments 5 and 6 on one and 4 and x on the "
                "other. Find x."),
               ("6.R6", "Prove that the angle between a tangent and a diameter is 90 "
                "degrees.")],
    ),
    projects=dict(
        service=[("Community need", "Architectural and ornamental designs are drawn without "
                                    "the geometry that makes them accurate."),
                 ("Mathematical connection", "Circle geometry and geometric proof."),
                 ("Proposed action", "Take one ornamental design in your community, identify "
                                     "the circle theorems it depends on, and publish a "
                                     "worked proof of one of them."),
                 ("Expected impact", "The design can be reproduced accurately by anyone."),
                 ("Student reflection", "Record the design, the theorem and the proof.")],
        community=[("Project idea", "A geometry audit of a local building or monument."),
                   ("Need", "The proportions are admired but not explained."),
                   ("Research question", "Which circle theorems does the design use, and can "
                                         "each be proved from radii and triangles?"),
                   ("Mathematics", "Circle geometry and geometric proof."),
                   ("Action or outcome", "A one-page explanation with a proof."),
                   ("Beneficiaries", "Anyone who visits or studies the building."),
                   ("Evidence", "The explanation and the proofs you wrote.")],
        personal=[("Personal interest", "Art, design, architecture or craft."),
                  ("Learning goal", "To prove a circle theorem and use it to make something "
                                    "accurate."),
                  ("Product or outcome", "A drawing or model that depends on one circle "
                                         "theorem."),
                  ("Mathematics", "Circle geometry and geometric proof."),
                  ("Process", "Choose a theorem, prove it, and apply it to a design."),
                  ("Evidence", "The design and the proof behind it.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=7, title="Sine and Cosine Rules; Trigonometry in Three Dimensions",
    key="Relationships", related=["Space", "Change", "Measurement"],
    context="Orientation in space and time",
    exploration="navigation, surveying and the geometry of place",
    inquiry=("Triangles that are not right-angled can still be solved: the sine and cosine "
             "rules turn measurements of angle and distance into positions, areas and "
             "three-dimensional structure."),
    atl=("Critical thinking",
         "In order for a student to decide how many triangles a set of measurements "
         "determines, students must compare the given side with the perpendicular height, "
         "identify the zero, one or two-triangle cases, and justify the conclusion."),
    standfirst="A triangle is determined by three independent measurements. The sine rule and "
               "the cosine rule are the two relationships that connect them, and together "
               "they solve every triangle and extend trigonometry into three dimensions.",
    engage="A surveyor measures two angles and one side of a triangular plot. A colleague "
           "measures two sides and a non-included angle of a different plot and finds two "
           "possible positions for the third corner. Why does one set of measurements give "
           "one triangle and the other give two?",
    questions=[("Factual", "What do the sine rule and the cosine rule state, and when is each "
                           "used?"),
               ("Conceptual", "Why can two sides and a non-included angle determine two "
                              "triangles, and when does it determine none?"),
               ("Debatable", "If a navigation calculation gives two possible positions, which "
                             "one should be acted on, and on what grounds?")],
    application_lede="These tasks use the sine and cosine rules. State which rule you use and "
                     "why, check the ambiguous case explicitly, and give every answer to "
                     "three significant figures.",
    projects_lede="A position is a relationship between measurements. Name the rule, check "
                  "the ambiguity, and say what would resolve it.",
    sections=[
        dict(id="7.1", title="The sine rule",
             inquiry_q="How do the sine rule and the ambiguous case fit together?",
             teach=[
                 "The sine rule states that a/sin A = b/sin B = c/sin C, where a is the side opposite the angle A. It is proved by dropping a perpendicular from one vertex and expressing its length in two ways.",
                 "The rule is used when a triangle has a side and its opposite angle, together with one further angle or side. It converts a known pair into an unknown one through a single ratio, which is why it is the rule for angle-side problems.",
                 "The ambiguous case arises when two sides and a non-included angle are given, written SSA. The given side opposite the given angle may be shorter than, equal to, or longer than the perpendicular height, and the three cases give two, one or no triangle.",
                 "The condition is exact: with A given and sides a and b given, the perpendicular height is b sin A. Two triangles exist when b sin A < a < b; exactly one right triangle exists when b sin A = a; no triangle exists when a < b sin A; and exactly one triangle exists when a ≥ b.",
             ], examples=[
                 dict(q="In triangle ABC, A = 38°, B = 64° and a = 9.4. Find b and c.",
                      vis=F("table", [["quantity", "working", "value"],
                                      ["C", "180° − 38° − 64°", "78°"],
                                      ["b", "9.4 sin 64° ÷ sin 38°", "13.72"],
                                      ["c", "9.4 sin 78° ÷ sin 38°", "14.93"],
                                      ["check", "largest side opposite largest angle",
                                       "c > b > a"]],
                            caption="Each side follows from one ratio."),
                      reasoning="Find the third angle, then apply the sine rule twice.",
                      steps=["The third angle is C = 180° − 38° − 64° = 78°.",
                             "By the sine rule, b = a sin B ÷ sin A.",
                             "So b = 9.4 × sin 64° ÷ sin 38° = 9.4 × 0.8988 ÷ 0.6157 ≈ 13.72.",
                             "Similarly c = 9.4 × sin 78° ÷ sin 38° = 9.4 × 0.9781 ÷ 0.6157 ≈ "
                             "14.93.",
                             "Check: C is the largest angle, so c is the largest side, as "
                             "found."],
                      ans="b ≈ 13.72 and c ≈ 14.93",
                      interp="Two angles and one side determine exactly one triangle, so "
                             "there is no ambiguity here."),
                 dict(q="In triangle ABC, A = 30°, a = 5 and b = 10. Determine how many "
                        "triangles exist and find the remaining measurements.",
                      vis=F("table", [["case", "condition", "holds?"],
                                      ["no triangle", "a < b sin A", "5 < 5, no"],
                                      ["one right triangle", "b sin A = a", "10 × 0.5 = 5, "
                                       "yes"],
                                      ["two triangles", "b sin A < a < b", "5 < 5, no"],
                                      ["one triangle", "a ≥ b", "5 ≥ 10, no"]],
                            caption="The height b sin A equals the given side."),
                      reasoning="Compute the perpendicular height b sin A and compare it with "
                               "the given side a to decide the number of triangles.",
                      steps=["The perpendicular height from C to the side AB extended is "
                             "b sin A = 10 × sin 30° = 10 × 0.5 = 5.",
                             "This equals the given side a = 5, so the height condition "
                             "b sin A = a holds.",
                             "Hence there is exactly one triangle, and it is right-angled at "
                             "C.",
                             "The remaining angles are B = 90° and C = 60°.",
                             "Check: a/sin A = 5/0.5 = 10 and b/sin B = 10/1 = 10, so the "
                             "sine rule is satisfied."],
                      ans="exactly one triangle, right-angled at C, with B = 90° and C = 60°",
                      interp="The ambiguous case is decided before any angle is computed, and "
                             "the check confirms the single solution."),
             ], inv=dict(
                 task="Take a fixed angle A = 40° and a fixed side b = 12. Vary a over the "
                      "values 6, 8, 7.7, 7.71, 12 and 14. For each, compute b sin A, decide "
                      "how many triangles exist, and where two exist, find both values of B. "
                      "Record the case boundaries.",
                 table=[["a", "b sin A", "comparison", "number of triangles", "value(s) of B"],
                        ["6", "7.713", "a < b sin A", "0", "none"],
                        ["7.7", "7.713", "a < b sin A", "0", "none"],
                        ["7.71", "7.713", "a < b sin A", "0", "none"],
                        ["7.713", "7.713", "b sin A = a", "1 (right-angled)", "90°"],
                        ["8", "7.713", "b sin A < a < b", "2", "73.9° and 106.1°"],
                        ["12", "7.713", "a = b", "1", "40°"],
                        ["14", "7.713", "a > b", "1", "33.7°"]],
                 notice=["Below the height there were no triangles at all, however close the "
                         "values were.",
                         "At the height there was exactly one triangle, and it was "
                         "right-angled.",
                         "Between the height and b there were exactly two triangles, with "
                         "supplementary values of B.",
                         "At and above b there was exactly one triangle again."],
                 obs="The number of triangles is decided by comparing a with b sin A and b, "
                     "and the two-triangle case gives supplementary values of B.",
                 concl="Two sides and a non-included angle determine a triangle only when the "
                       "given side is at least the perpendicular height b sin A. When "
                       "b sin A = a there is exactly one triangle and it is right-angled; "
                       "when b sin A < a < b there are two, with the two values of B "
                       "supplementary; when a < b sin A there is none. Here the height was "
                       "7.713, and the cases were 0, 1 and 2 triangles around it.")),
        dict(id="7.2", title="The cosine rule",
             inquiry_q="When is the cosine rule the right rule, and what does it generalise?",
             teach=[
                 "The cosine rule states that a² = b² + c² − 2bc cos A, and rearranged gives cos A = (b² + c² − a²)/(2bc). It is proved by placing the triangle in a coordinate system and applying Pythagoras to two right-angled triangles.",
                 "The rule is used when three sides are given, or two sides and the included angle. It is the only rule that handles the included angle directly, and it reduces to Pythagoras when the included angle is 90 degrees.",
                 "The cosine rule is a generalisation of Pythagoras: the term 2bc cos A vanishes when A is a right angle, and the formula becomes a² = b² + c². Every right-angled calculation is a special case of it.",
                 "When the cosine rule gives a quadratic in an unknown side, both roots must be considered and rejected if they are not positive. This happens when two sides and a non-included angle are given, and it is the algebraic form of the ambiguous case.",
             ], examples=[
                 dict(q="In triangle ABC, b = 7, c = 10 and A = 47°. Find a and then find B.",
                      vis=F("table", [["quantity", "working", "value"],
                                      ["a²", "7² + 10² − 2(7)(10) cos 47°", "95.59"],
                                      ["a", "√95.59", "9.78"],
                                      ["cos B", "(49 + 95.59 − 100) ÷ (2 × 7 × 9.78)", "0.3253"],
                                      ["B", "arccos 0.3253", "71.0°"]],
                            caption="The included angle fixes the third side."),
                      reasoning="Apply the cosine rule for the side, then again for the angle.",
                      steps=["The cosine rule gives a² = b² + c² − 2bc cos A.",
                             "So a² = 49 + 100 − 140 cos 47° = 149 − 140(0.6820) ≈ 95.59.",
                             "Hence a ≈ 9.78.",
                             "For the angle, cos B = (a² + c² − b²)/(2ac) = (95.59 + 100 − "
                             "49)/(2 × 9.78 × 10) ≈ 0.7493.",
                             "So B ≈ 41.5°, and C ≈ 180 − 47 − 41.5 = 91.5°."],
                      ans="a ≈ 9.78 and B ≈ 41.5°",
                      interp="Two sides and the included angle determine exactly one triangle, "
                             "so there is no ambiguity."),
                 dict(q="Find the angles of the triangle with sides 5, 7 and 9.",
                      vis=F("table", [["angle", "cosine", "value"],
                                      ["A (opposite 9)", "(25 + 49 − 81)/70 = −0.1", "95.7°"],
                                      ["B (opposite 7)", "(25 + 81 − 49)/90 = 0.6333", "50.7°"],
                                      ["C (opposite 5)", "(49 + 81 − 25)/126 = 0.8333", "33.6°"],
                                      ["check", "95.7 + 50.7 + 33.6", "180.0°"]],
                            caption="Three sides determine the angles uniquely."),
                      reasoning="Apply the cosine rule three times, or twice and use the angle "
                               "sum.",
                      steps=["For the angle opposite the side 9, cos A = (5² + 7² − 9²)/(2 × "
                             "5 × 7) = (25 + 49 − 81)/70 = −7/70 = −0.1.",
                             "So A ≈ 95.7°, which is obtuse as the negative cosine indicates.",
                             "For the angle opposite 7, cos B = (25 + 81 − 49)/(2 × 5 × 9) = "
                             "57/90 ≈ 0.6333, so B ≈ 50.7°.",
                             "For the angle opposite 5, cos C = (49 + 81 − 25)/(2 × 7 × 9) = "
                             "105/126 ≈ 0.8333, so C ≈ 33.6°.",
                             "The three angles sum to 180°, as required."],
                      ans="approximately 95.7°, 50.7° and 33.6°",
                      interp="Three sides determine exactly one triangle, so the answer is "
                             "unique and the angle sum is the check."),
             ], inv=dict(
                 task="Take a triangle with sides 8 and 11 and included angle 55°. Compute "
                      "the third side by the cosine rule, then all three angles, and check "
                      "the angle sum. Then repeat with the included angle 125° and compare "
                      "the two results.",
                 table=[["included angle", "third side", "largest angle", "smallest angle",
                                "angle sum"],
                        ["55°", "9.22", "62.4°", "42.6°", "180.0°"],
                        ["90°", "13.60", "90.0°", "35.8°", "180.0°"],
                        ["125°", "16.87", "125.0°", "19.9°", "180.0°"],
                        ["155°", "18.19", "155.0°", "9.7°", "180.0°"]],
                 notice=["A larger included angle gave a much larger third side, from 9.22 to "
                         "16.87.",
                         "In both cases the largest angle was the given one, because it was "
                         "opposite the largest side.",
                         "The angle sum was 180 degrees in both cases, confirming the "
                         "calculations.",
                         "The change in the third side was far from proportional to the change "
                         "in the angle, because the cosine is not linear."],
                 obs="The third side grows with the included angle, and fastest when the "
                     "cosine is changing fastest.",
                 concl="The cosine rule a² = b² + c² − 2bc cos A determines the third side "
                       "from two sides and the included angle, and rearranged determines an "
                       "angle from three sides. It is a generalisation of Pythagoras, to "
                       "which it reduces when the included angle is a right angle. Here the "
                       "third side was 9.22 for an included angle of 55 degrees and 16.87 "
                       "for 125 degrees.")),
        dict(id="7.3", title="Area and the included angle",
             inquiry_q="How is the area of a triangle found without a height?",
             teach=[
                 "The area of a triangle is half the base times the perpendicular height. When the height is not given but two sides and the included angle are, the height is one side times the sine of the included angle, giving area = ½bc sin A.",
                 "The formula is symmetric: area = ½ab sin C = ½bc sin A = ½ca sin B. Any pair of sides with the angle between them gives the same area, which is a check on the calculation.",
                 "The formula is derived by dropping the perpendicular and using the definition of sine in the resulting right-angled triangle. The derivation is short, and it explains why the included angle is the one that appears.",
                 "The same formula applied to a sector or a segment gives the area of a circular sector as ½r²θ in radians, and the segment as the sector minus the triangle. The radian measure is what makes the sector formula simple.",
             ], examples=[
                 dict(q="Find the area of a triangle with sides 9 and 13 and included angle "
                        "52°.",
                      vis=F("table", [["step", "working", "value"],
                                      ["height", "9 sin 52°", "7.09"],
                                      ["area", "½ × 13 × 7.09", "46.1"],
                                      ["check", "½ × 9 × 13 × sin 52°", "46.1"],
                                      ["units", "square units", "—"]],
                            caption="The height is one side times the sine of the included "
                                    "angle."),
                      reasoning="Drop the perpendicular and express the height with the sine "
                               "of the included angle.",
                      steps=["Take the sides 9 and 13 with the included angle 52°.",
                             "The height on the base 13 is 9 sin 52° ≈ 9 × 0.7880 ≈ 7.09.",
                             "The area is ½ × 13 × 7.09 ≈ 46.1 square units.",
                             "Check with the formula: ½ × 9 × 13 × sin 52° ≈ 46.1.",
                             "The two calculations agree, as they must."],
                      ans="about 46.1 square units",
                      interp="The direct formula is faster, and the height calculation "
                             "explains where it comes from."),
                 dict(q="A sector of a circle of radius 8 has angle 0.7 radians. Find its "
                        "area and the area of the segment cut off by the chord.",
                      vis=F("table", [["region", "working", "area"],
                                      ["sector", "½ × 8² × 0.7", "22.4"],
                                      ["triangle", "½ × 8 × 8 × sin 0.7", "20.5"],
                                      ["segment", "22.4 − 20.5", "1.9"]],
                            caption="The segment is the sector minus the triangle."),
                      reasoning="Use the sector formula with radians and subtract the "
                               "triangle.",
                      steps=["The sector area is ½r²θ = ½ × 64 × 0.7 = 22.4.",
                             "The triangle formed by the two radii and the chord has area "
                             "½r² sin θ = ½ × 64 × sin 0.7.",
                             "sin 0.7 ≈ 0.6442, so the triangle area is 32 × 0.6442 ≈ 20.5.",
                             "The segment is the sector minus the triangle: 22.4 − 20.5 ≈ 1.9.",
                             "The segment is much smaller than the sector because the angle "
                             "is small."],
                      ans="sector 22.4, segment about 1.9",
                      interp="The radian measure makes the sector formula ½r²θ, and the same "
                             "triangle formula gives the correction."),
             ], inv=dict(
                 task="Take a triangle with sides 6, 8 and 11. Compute its area using each of "
                      "the three forms of the area formula, and check that all three agree. "
                      "Then find the radius of its circumcircle using a = 2R sin A.",
                 table=[["form", "angle needed", "working", "area"],
                        ["½ab sin C", "C opposite 11", "½ × 6 × 8 × sin C", "22.4"],
                        ["½bc sin A", "A opposite 6", "½ × 8 × 11 × sin A", "22.4"],
                        ["½ca sin B", "B opposite 8", "½ × 11 × 6 × sin B", "22.4"],
                        ["circumradius", "A opposite 6", "6 ÷ (2 sin A)", "5.49"]],
                 notice=["All three forms gave the same area, as they had to.",
                         "The angles were found first by the cosine rule, since only the "
                         "sides were given.",
                         "The circumradius came from a = 2R sin A, which is the sine rule "
                         "rearranged.",
                         "The area was about 22.4 square units, and the circumradius about "
                         "5.49."],
                 obs="The area formula is symmetric in the three pairs of sides, and the sine "
                     "rule extends to the circumradius.",
                 concl="The area of a triangle is ½bc sin A, where A is the angle included "
                       "between the sides b and c, and the formula is symmetric in the three "
                       "pairs. The same relationship rearranged gives a = 2R sin A, where R "
                       "is the circumradius. Here every form gave an area of about 22.4 "
                       "square units and a circumradius of about 5.49.")),
        dict(id="7.4", title="Bearings and navigation",
             inquiry_q="How do bearings turn a triangle into a position?",
             teach=[
                 "A bearing is a direction measured clockwise from north, written as a three-figure angle. Bearings are the language in which positions are described, and they convert a diagram into a set of numbers that can be transmitted.",
                 "A navigation problem is a triangle in which the sides are distances and the angles are bearings. The sine and cosine rules solve it exactly as they solve any triangle, once the interior angles have been extracted from the bearings.",
                 "The interior angle between two bearings is the difference of the bearings, or 360 degrees minus that difference, depending on which way round the triangle goes. Getting this wrong is the commonest navigation error, and drawing the diagram prevents it.",
                 "Speed, distance and time enter as a scale on the sides: a ship travelling at 12 knots for 3 hours covers 36 nautical miles. The bearing gives the direction and the distance the magnitude, and together they give a position vector.",
             ], examples=[
                 dict(q="A ship sails 40 km on a bearing of 060° and then 30 km on a bearing "
                        "of 150°. Find its distance and bearing from the start.",
                      vis=F("table", [["leg", "distance", "bearing", "interior angle at the "
                                      "turn"],
                                      ["first", "40", "060°", "—"],
                                      ["second", "30", "150°", "90°"],
                                      ["resultant", "—", "—", "—"]],
                            caption="The turn is a right angle."),
                      reasoning="Extract the interior angle from the bearings, then apply "
                               "Pythagoras and trigonometry.",
                      steps=["The bearings differ by 150 − 60 = 90 degrees, so the turn is a "
                             "right angle.",
                             "The two legs are perpendicular, so the distance is "
                             "√(40² + 30²) = √2500 = 50 km.",
                             "The bearing of the resultant is 060° + arctan(30/40) = 060° + "
                             "36.87° = 096.87°.",
                             "So the ship is 50 km away on a bearing of approximately 097°.",
                             "Check: the eastward distance is 40 sin 60° + 30 sin 150° = "
                             "34.64 + 15 = 49.64, and the northward is 40 cos 60° + 30 cos "
                             "150° = 20 − 25.98 = −5.98, which gives the same distance."],
                      ans="50 km on a bearing of about 097°",
                      interp="The bearing difference is the interior angle, and the "
                             "components check is a different route to the same position."),
                 dict(q="Two ports A and B are 80 km apart, with B on a bearing of 035° from "
                        "A. A ship leaves A and a second leaves B at the same time, the "
                        "first on a bearing of 080° at 20 km/h and the second on a bearing of "
                        "200° at 15 km/h. Find the distance between them after 2 hours.",
                      vis=F("table", [["quantity", "working", "value"],
                                      ["first ship's distance", "20 × 2", "40 km"],
                                      ["second ship's distance", "15 × 2", "30 km"],
                                      ["angle at A between AB and the first leg",
                                       "080° − 035°", "45°"],
                                      ["angle between the two legs", "—", "140°"]],
                            caption="The included angle is not the difference of the "
                                    "bearings."),
                      reasoning="Extract the two distances and the included angle from the "
                               "bearings, then apply the cosine rule.",
                      steps=["After 2 hours the first ship has travelled 40 km and the "
                             "second 30 km.",
                             "The angle at A between AB and the first ship's course is "
                             "080° − 035° = 45°.",
                             "The second ship's course from B is on a bearing of 200°, so the "
                             "angle between the two courses at the triangle's vertices is "
                             "180° − 45° − (200° − 180°) = 140°.",
                             "By the cosine rule, the distance squared is 40² + 30² − 2(40)"
                             "(30) cos 140°.",
                             "That is 1600 + 900 + 1838.5 = 4338.5, so the distance is about "
                             "65.9 km."],
                      ans="about 65.9 km",
                      interp="The included angle must be extracted from the bearings "
                             "carefully, and drawing the diagram is what prevents the error."),
             ], inv=dict(
                 task="Set up a navigation problem of your own with two legs and a "
                      "turn, solve it by the cosine rule, and then solve the same problem by "
                      "resolving each leg into north and east components. Compare the two "
                      "answers and record which method you found more reliable.",
                 table=[["leg", "distance", "bearing", "north component", "east component"],
                        ["first", "25", "020°", "23.49", "8.55"],
                        ["second", "18", "130°", "−11.57", "13.79"],
                        ["total", "—", "—", "11.92", "22.34"],
                        ["resultant", "—", "—", "distance 25.31", "bearing 118.1°"]],
                 notice=["Both methods gave the same distance and the same bearing.",
                         "The component method made the sign of the northward distance "
                         "visible, which the cosine rule hid.",
                         "The cosine rule was fewer steps once the included angle was found.",
                         "The component method needed the angle of each leg measured from "
                         "north, which is what a bearing gives directly."],
                 obs="Bearings are angles from north, so they suit the component method; the "
                     "cosine rule suits a triangle with a known included angle.",
                 concl="A bearing is a direction measured clockwise from north, and a "
                       "navigation problem is a triangle whose sides are distances and whose "
                       "angles come from bearings. The interior angles must be extracted "
                       "carefully, and the two solution methods — the cosine rule and "
                       "resolving into components — must agree. Here both gave a distance "
                       "of 34.7 on a bearing of 137 degrees.")),
        dict(id="7.5", title="Trigonometry in three dimensions",
             inquiry_q="How does a three-dimensional problem become a two-dimensional one?",
             teach=[
                 "A three-dimensional problem is solved by finding a plane that contains the required lengths and angles, solving the two-dimensional triangle in that plane, and then relating it back to the solid. The choice of plane is the whole skill.",
                 "In a cuboid with edges a, b and c, the space diagonal is √(a² + b² + c²) and the angle between the diagonal and an edge is found from a right-angled triangle containing both. The face diagonal is an intermediate step.",
                 "The angle between a line and a plane is the angle between the line and its projection onto the plane, and it is found in the right-angled triangle formed by the line, its projection and the perpendicular. It is never the angle the line makes with the plane's normal.",
                 "In a pyramid or cone, the slant height, the vertical height and the radius of the base form a right-angled triangle, and every angle in the solid is found from that triangle or from a triangle in a face.",
             ], examples=[
                 dict(q="A cuboid has edges 6, 8 and 24. Find the space diagonal and the "
                        "angle it makes with the longest edge.",
                      vis=F("table", [["step", "working", "value"],
                                      ["face diagonal", "√(6² + 8²)", "10"],
                                      ["space diagonal", "√(10² + 24²)", "26"],
                                      ["cos of the angle", "24/26", "0.9231"],
                                      ["the angle", "arccos 0.9231", "22.6°"]],
                            caption="The space diagonal closes a right-angled triangle."),
                      reasoning="Find the face diagonal, then use it to find the space "
                               "diagonal and the angle.",
                      steps=["The face diagonal on the 6 by 8 face is √(36 + 64) = 10.",
                             "The space diagonal is √(10² + 24²) = √676 = 26.",
                             "The angle with the longest edge has cosine 24/26, because the "
                             "edge and the diagonal are in the same right-angled triangle.",
                             "So the angle is arccos(24/26) ≈ 22.6°.",
                             "Check: 6² + 8² + 24² = 36 + 64 + 576 = 676 = 26²."],
                      ans="space diagonal 26; angle about 22.6°",
                      interp="The two-step Pythagoras is the standard way through a cuboid, "
                             "and the angle is read from the final triangle."),
                 dict(q="A square pyramid has a base of side 10 and a vertical height of 12. "
                        "Find the slant height and the angle between a sloping face and the "
                        "base.",
                      vis=F("table", [["step", "working", "value"],
                                      ["half the base side", "10 ÷ 2", "5"],
                                      ["slant height", "√(5² + 12²)", "13"],
                                      ["tan of the angle", "12/5", "2.4"],
                                      ["the angle", "arctan 2.4", "67.4°"]],
                            caption="The vertical height, half the base and the slant height "
                                    "form a right triangle."),
                      reasoning="Find the right-angled triangle through the apex and the "
                               "midpoint of a base edge.",
                      steps=["The perpendicular from the apex to the midpoint of a base edge, "
                             "the vertical height and half the base side form a right-angled "
                             "triangle.",
                             "The legs are 12 and 5, so the slant height is √(144 + 25) = 13.",
                             "The angle between the face and the base has tangent 12/5.",
                             "So the angle is arctan(12/5) ≈ 67.4°.",
                             "This is the angle between the planes, measured in the "
                             "perpendicular cross-section."],
                      ans="slant height 13; angle about 67.4°",
                      interp="The angle between two planes is measured in the plane "
                             "perpendicular to their line of intersection, which is the "
                             "cross-section used here."),
             ], inv=dict(
                 task="Take a cone of radius 5 and vertical height 12. Find the slant "
                      "height, the angle between the slant height and the base, the angle "
                      "between the slant height and the axis, and the area of the curved "
                      "surface. Then repeat for a cone of radius 5 and height 5, and compare.",
                 table=[["quantity", "cone 1 (r = 5, h = 12)", "cone 2 (r = 5, h = 5)"],
                        ["slant height", "13", "5√2 ≈ 7.07"],
                        ["angle with the base", "67.4°", "45°"],
                        ["angle with the axis", "22.6°", "45°"],
                        ["curved surface area", "π × 5 × 13 ≈ 204.2", "π × 5 × 7.07 ≈ 111.1"]],
                 notice=["The two angles were complementary in each cone, as they had to be "
                         "in a right-angled triangle.",
                         "Halving the height halved the slant height only partly, from 13 to "
                         "7.07.",
                         "The curved surface area fell by nearly half, because it is "
                         "proportional to the slant height.",
                         "The second cone had equal base radius and height, so its angles "
                         "were both 45 degrees."],
                 obs="Every angle in a cone is read from the right-angled triangle formed by "
                     "the radius, the height and the slant height.",
                 concl="A three-dimensional problem is solved by choosing a plane that "
                       "contains the required lengths and solving the two-dimensional triangle "
                       "in it. In a cone that plane gives the radius, the vertical height and "
                       "the slant height, and from them every angle and the curved surface "
                       "area. Here the slant heights were 13 and about 7.07, with curved "
                       "surface areas of about 204.2 and 111.1.")),
        dict(id="7.6", title="Investigation: measuring the unmeasurable",
             inquiry_q="How can a distance be found without measuring it directly?",
             teach=[
                 "A distance that cannot be measured directly — across a river, to a "
                 "mountain top, to a star — is found by measuring a baseline and two "
                 "angles, and solving the resulting triangle. The method is triangulation, and "
                 "it is the basis of surveying.",
                 "The accuracy of the result depends on the accuracy of the angles and on the shape of the triangle. A long thin triangle amplifies angle errors, so surveyors choose baselines and angles that give a well-conditioned triangle.",
                 "The same method with a very long baseline and very small angles measures stellar distances in parsecs, where one parsec is the distance at which one astronomical unit subtends one second of arc. The scale changes; the method does not.",
                 "Triangulation is limited by the curvature of the Earth over long baselines and by atmospheric refraction in astronomy. Both are corrections to the ideal triangle, and both must be stated when the method is used.",
             ], examples=[
                 dict(q="A baseline AB of 200 m is measured on one bank of a river. From A a "
                        "tree T on the far bank is sighted at 35° from the baseline, and "
                        "from B at 65°. Find the distance from A to T.",
                      vis=F("table", [["quantity", "working", "value"],
                                      ["angle at A", "given", "35°"],
                                      ["angle at B", "given", "65°"],
                                      ["angle at T", "180° − 35° − 65°", "80°"],
                                      ["AT", "200 sin 65° ÷ sin 80°", "184.1 m"]],
                            caption="A baseline and two angles determine the triangle."),
                      reasoning="Find the third angle, then apply the sine rule.",
                      steps=["The angles at A and B are 35° and 65°, so the angle at T is "
                             "180 − 35 − 65 = 80°.",
                             "By the sine rule, AT ÷ sin 65° = AB ÷ sin 80°.",
                             "So AT = 200 × sin 65° ÷ sin 80° = 200 × 0.9063 ÷ 0.9848.",
                             "Hence AT ≈ 184.1 m.",
                             "Check the angle sum: 35 + 65 + 80 = 180°, so the triangle is "
                             "consistent."],
                      ans="about 184 m",
                      interp="The angle sum check confirms the readings are consistent, and "
                             "it is performed before any length is computed."),
                 dict(q="A mountain is observed from two stations 3 km apart on a level "
                        "plain. From the nearer station the angle of elevation to the summit "
                        "is 22° and from the further one 18°. Find the height of the "
                        "mountain.",
                      vis=F("table", [["step", "working", "value"],
                                      ["let h be the height", "—", "—"],
                                      ["nearer distance", "h ÷ tan 22°", "2.475h"],
                                      ["further distance", "h ÷ tan 18°", "3.078h"],
                                      ["difference", "3.078h − 2.475h = 3", "h = 4.97"]],
                            caption="Two angles of elevation give two equations."),
                      reasoning="Write the horizontal distance to the summit from each station "
                               "and equate the difference to the baseline.",
                      steps=["Let h be the height and d the distance from the nearer station "
                             "to the point below the summit.",
                             "From the nearer station, tan 22° = h/d, so d = h ÷ tan 22° ≈ "
                             "2.475h.",
                             "From the further station, tan 18° = h/(d + 3), so d + 3 = h ÷ "
                             "tan 18° ≈ 3.078h.",
                             "Subtracting gives 3 ≈ 0.603h, so h ≈ 4.97 km.",
                             "Check: the nearer distance is about 12.3 km and the further "
                             "about 15.3 km, differing by 3 km as required."],
                      ans="about 4.97 km",
                      interp="Two angles of elevation from a known baseline give the height, "
                             "and the check is the difference of the two horizontal "
                             "distances."),
             ], inv=dict(
                 task="Measure the height of an object in your school grounds without "
                      "measuring it directly. Choose a baseline, measure two angles of "
                      "elevation, compute the height, and repeat with a different baseline. "
                      "Compare the two results and comment on the accuracy of the method.",
                 table=[["baseline", "angle 1", "angle 2", "computed height", "difference"],
                        ["10 m", "31°", "25°", "8.42 m", "—"],
                        ["20 m", "31°", "25°", "8.46 m", "0.04 m"],
                        ["10 m", "31°", "25°", "8.42 m", "0.00 m"],
                        ["15 m", "45°", "33°", "8.43 m", "0.01 m"],
                        ["30 m", "45°", "33°", "8.47 m", "0.04 m"]],
                 notice=["The two baselines gave heights within 4 cm of each other.",
                         "The longer baseline gave a slightly different answer, because the "
                         "angles were measured with the same instrument but over a longer "
                         "distance.",
                         "The repeat measurement was identical, which showed the calculation "
                         "was being done consistently.",
                         "The method's accuracy was limited by the angle measurement, not by "
                         "the baseline."],
                 obs="Two angles of elevation and a baseline determine a height, and the "
                     "accuracy is limited by the angles.",
                 concl="A distance that cannot be measured directly is found by measuring a "
                       "baseline and two angles and solving the triangle, which is "
                       "triangulation. The accuracy is limited by the angle measurement and "
                       "by the conditioning of the triangle, and long baselines need "
                       "correction for the curvature of the Earth. Here the two baselines "
                       "gave heights of 8.42 m and 8.46 m.")),
        dict(id="7.7", title="Mixed practice",
             inquiry_q="Which rule, and how many triangles?",
             teach=[
                 "Every non-right-angled triangle question begins by asking what is given: three sides, two sides and the included angle, or two sides and a non-included angle. The answer decides the rule and whether the ambiguous case must be checked.",
                 "The ambiguous case is checked by comparing the given side with the perpendicular height. Skipping the check is how two-triangle problems are answered with one answer, and it is the defect this chapter repairs.",
                 "Three-dimensional problems are solved by choosing a plane. Naming the plane and the triangle in it is the first line of the solution, and it is what makes the rest of the solution checkable.",
                 "Mixed practice is where the rule is chosen rather than given, so the reasoning behind the choice is part of what is being practised.",
             ], examples=[
                 dict(q="In triangle ABC, A = 40°, a = 7 and b = 12. Determine how many "
                        "triangles exist and find all solutions.",
                      vis=F("table", [["case", "condition", "holds?"],
                                      ["no triangle", "a < b sin A", "7 < 7.713, yes"],
                                      ["one right triangle", "b sin A = a", "7.713 = 7, no"],
                                      ["two triangles", "b sin A < a < b", "7.713 < 7, no"]],
                            caption="The height exceeds the given side."),
                      reasoning="Compute b sin A and compare it with a before doing anything "
                               "else.",
                      steps=["The perpendicular height is b sin A = 12 × sin 40° ≈ 12 × "
                             "0.6428 ≈ 7.713.",
                             "The given side a = 7 is less than 7.713, so no triangle "
                             "exists.",
                             "The case b sin A = a does not hold, since 7.713 ≠ 7.",
                             "The case b sin A < a < b does not hold either, since 7.713 > 7.",
                             "Hence there is no triangle with these measurements."],
                      ans="no triangle exists",
                      interp="The comparison is the whole solution, and it takes one "
                             "multiplication."),
                 dict(q="In triangle ABC, A = 40°, a = 9 and b = 12. Find both solutions.",
                      vis=F("table", [["case", "condition", "holds?"],
                                      ["two triangles", "b sin A < a < b", "7.713 < 9 < 12, "
                                       "yes"],
                                      ["first solution", "B ≈ 58.9°", "C ≈ 81.1°"],
                                      ["second solution", "B ≈ 121.1°", "C ≈ 18.9°"]],
                            caption="Two values of B are supplementary."),
                      reasoning="Confirm the two-triangle case, then find both values of B "
                               "from the sine rule.",
                      steps=["The height is b sin A = 12 sin 40° ≈ 7.713, and 7.713 < 9 < 12, "
                             "so there are two triangles.",
                             "By the sine rule, sin B = b sin A ÷ a = 7.713 ÷ 9 ≈ 0.857.",
                             "So B ≈ 58.9° or B ≈ 180° − 58.9° = 121.1°.",
                             "For the first, C ≈ 180 − 40 − 58.9 = 81.1° and c = 9 sin 81.1° ÷ "
                             "sin 40° ≈ 13.82.",
                             "For the second, C ≈ 18.9° and c = 9 sin 18.9° ÷ sin 40° ≈ 4.07."],
                      ans="two solutions: B ≈ 58.9°, C ≈ 81.1°, c ≈ 13.82; and B ≈ 121.1°, "
                          "C ≈ 18.9°, c ≈ 4.07",
                      interp="Both solutions are reported, and the supplementary pair of "
                             "angles is the reason there are two."),
             ], inv=dict(
                 task="Take A = 35°, a = 8 and b = 11. Determine how many triangles exist, "
                      "find all solutions, and then repeat with a = 7, a = 6.30 and a = 14. "
                      "Record the case boundaries and explain how you decided each one.",
                 table=[["a", "b sin A", "comparison", "triangles", "solutions"],
                        ["8", "6.31", "b sin A < a < b", "2", "B ≈ 52.3° or 127.7°"],
                        ["7", "6.31", "b sin A < a < b", "2", "B ≈ 44.6° or 135.4°"],
                        ["6.30", "6.31", "a < b sin A", "0", "none"],
                        ["14", "6.31", "a > b", "1", "B ≈ 26.7°"]],
                 notice=["The height was about 6.31, and every case was decided by comparing "
                         "a with it.",
                         "Two values of a gave two triangles each, with supplementary values "
                         "of B.",
                         "One value of a gave no triangle, because it fell just below the "
                         "height.",
                         "One value of a gave exactly one triangle, because it exceeded b."],
                 obs="The comparison of a with b sin A and with b decides the number of "
                     "triangles before any angle is computed.",
                 concl="Two sides and a non-included angle determine a triangle only when the "
                       "given side is at least the perpendicular height b sin A. The "
                       "comparison is made first, and only then are angles computed: "
                       "b sin A = a gives one right triangle, b sin A < a < b gives two, "
                       "a < b sin A gives none, and a ≥ b gives one. Here the height was "
                       "6.31 and the cases were 2, 2, 0 and 1 triangles.")),
    ],
    practice=dict(
        A=[("7.1.1", "In triangle ABC, A = 38°, B = 64° and a = 9.4. Find b and c.",
            "b ≈ 13.72 and c ≈ 14.93.", "Use the sine rule with C = 78°.", "F"),
           ("7.1.2", "In triangle ABC, B = 47°, C = 68° and b = 12. Find a and c.",
            "A = 65°; a = 12 sin 65° ÷ sin 47° ≈ 15.13; c = 12 sin 68° ÷ sin 47° ≈ 15.09.",
            "Find the third angle, then apply the sine rule twice.", "F"),
           ("7.1.3", "In triangle ABC, b = 8, c = 11 and A = 55°. Find a.",
            "a² = 64 + 121 − 176 cos 55° ≈ 84.06, so a ≈ 9.17.",
            "Use the cosine rule for the included angle.", "F"),
           ("7.1.4", "Find the largest angle of the triangle with sides 7, 9 and 12.",
            "cos A = (49 + 81 − 144)/(2 × 7 × 9) = −14/126, so A ≈ 96.4°.",
            "The largest angle is opposite the largest side.", "F"),
           ("7.1.5", "Find the area of the triangle with sides 8 and 10 and included angle "
            "40°.",
            "½ × 8 × 10 × sin 40° ≈ 25.7.", "Area = ½ab sin C.", "F"),
           ("7.1.6", "In triangle ABC, A = 30°, a = 5 and b = 10. Determine how many "
            "triangles exist.",
            "One triangle, right-angled at C, because b sin A = 10 × 0.5 = 5 = a.",
            "Compare a with the perpendicular height b sin A.", "R"),
           ("7.1.7", "In triangle ABC, A = 30°, a = 6 and b = 10. How many triangles exist, "
            "and what are the values of B?",
            "b sin A = 5 and 5 < 6 < 10, so two triangles; sin B = 5/6 gives B ≈ 56.4° or "
            "123.6°.", "Compare with the height, then apply the sine rule.", "R"),
           ("7.1.8", "In triangle ABC, A = 45°, a = 4 and b = 6. How many triangles exist?",
            "b sin A = 6 × 0.7071 ≈ 4.243, and 4 < 4.243, so no triangle exists.",
            "Compare a with b sin A.", "R"),
           ("7.1.9", "A ship sails 30 km on a bearing of 040° and then 24 km on a bearing of "
            "130°. Find the distance from the start.",
            "The turn is 90°, so the distance is √(30² + 24²) ≈ 38.4 km.",
            "The bearing difference is the interior angle.", "F"),
           ("7.1.10", "A cuboid has edges 3, 4 and 12. Find the space diagonal.",
            "√(9 + 16 + 144) = √169 = 13.", "Two applications of Pythagoras.", "F"),
           ("7.1.11", "A cone has radius 6 and vertical height 8. Find the slant height and "
            "the angle between the slant height and the base.",
            "Slant height 10; the angle has tangent 8/6, so it is about 53.1°.",
            "The radius, height and slant height form a right triangle.", "F"),
           ("7.1.12", "Explain why the ambiguous case arises only when two sides and a "
            "non-included angle are given.",
            "Because the given side opposite the given angle may fall short of, equal or "
            "exceed the perpendicular height, and the three comparisons give zero, one or "
            "two triangles; with the included angle or with three sides the triangle is "
            "unique.",
            "Compare the given side with the perpendicular height.", "R")],
        B=[("7.2.1", "Investigate the number of triangles determined by A = 50°, b = 10 and "
            "a = 6, 7.66, 9, 10 and 13, and justify each case.",
            "b sin A ≈ 7.66; a = 6 gives 0, a = 7.66 gives 1 right triangle, a = 9 and a = "
            "10 give 2, and a = 13 gives 1.",
            "Compare a with b sin A and with b.", "C"),
           ("7.2.2", "Conjecture a rule for when the sine rule gives a unique answer, and "
            "test it on three examples.",
            "It is unique exactly when the given angle is opposite the longer of the two "
            "given sides, or when the side opposite the given angle is at least the "
            "perpendicular height; otherwise there are two answers or none.",
            "Compare the side opposite the given angle with the height and with the other "
            "side.", "C"),
           ("7.2.3", "Investigate the relationship between the two solutions of the ambiguous "
            "case, and justify it.",
            "The two values of B are supplementary, because sin B = sin(180° − B), and the "
            "two triangles share the given sides and angle.",
            "Use the identity sin(180° − B) = sin B.", "R"),
           ("7.2.4", "Investigate the area of a triangle with two fixed sides and a varying "
            "included angle, and justify when the area is greatest.",
            "The area is ½ab sin C, which is greatest when C = 90°, because sin C ≤ 1 with "
            "equality only at 90°.",
            "Maximise the sine of the included angle.", "R"),
           ("7.2.5", "Take a triangle with sides 5 and 8. Investigate the possible values of "
            "the third side and justify the bounds.",
            "The third side c satisfies 3 < c < 13, because |8 − 5| < c < 8 + 5 by the "
            "triangle inequality.",
            "Use the triangle inequality on both sides.", "R"),
           ("7.2.6", "Investigate the circumradius of a triangle with sides 6, 8 and 10, and "
            "justify the result.",
            "R = a ÷ (2 sin A); the triangle is right-angled, so the circumradius is half the "
            "hypotenuse, 5.",
            "A right-angled triangle's circumcentre is the midpoint of the hypotenuse.", "R"),
           ("7.2.7", "Investigate the angle between the space diagonal of a cuboid and a "
            "face diagonal as the cuboid becomes a cube, and justify.",
            "As the edges become equal the angle tends to arccos(√(2/3)) ≈ 35.3°, which is "
            "the angle between a cube's space diagonal and a face diagonal.",
            "Compute the cosine as the ratio of the face diagonal to the space diagonal.",
            "C"),
           ("7.2.8", "Investigate the number of triangles determined by A = 25°, b = "
            "9 and a = 3, 3.8, 5, 9 and 11, and justify each case.",
            "b sin A ≈ 3.80; a = 3 gives 0, a = 3.8 gives 1 right triangle, "
            "a = 5 gives 2, and a = 9 and a = 11 give 1 each.",
            "Compare a with b sin A and with b.", "C"),
           ("7.2.9", "Conjecture a rule for when the cosine rule gives a quadratic "
            "with two positive roots, and test it.",
            "When two sides and a non-included angle are given, the "
            "quadratic in the third side can have two positive roots, "
            "corresponding to the two triangles of the ambiguous case.",
            "Set up the cosine rule with the unknown side and examine the "
            "roots.", "C"),
           ("7.2.10", "Investigate the area of a triangle with two fixed sides as the "
            "included angle varies, and justify the maximum.",
            "The area is ½ab sin C, which is greatest at C = 90° and zero "
            "at C = 0° and 180°, because sin C ≤ 1 with equality only at "
            "90°.",
            "Maximise the sine of the included angle.", "R"),
           ("7.2.11", "Investigate the relationship between the three formulas for "
            "the area of a triangle and justify their equivalence.",
            "The three forms ½ab sin C, ½bc sin A and ½ca sin B are equal "
            "because each is half the product of two sides and the sine of "
            "the included angle, and the sine rule makes them "
            "interchangeable.",
            "Use the sine rule to rewrite each form.", "R"),
           ],
        C=[("7.3.1", "Write a complete solution to solving the triangle with a = 9, b = 12 "
            "and A = 35°, stating the number of solutions.",
            "b sin A ≈ 6.88 and 6.88 < 9 < 12, so two solutions: B ≈ 51.3° with C ≈ 93.7° and "
            "c ≈ 15.62, or B ≈ 128.7° with C ≈ 16.3° and c ≈ 2.85.",
            "Check the ambiguous case first, then apply the sine rule to both values of B.",
            "R"),
           ("7.3.2", "Write a complete solution to finding the area of a triangle with sides "
            "13, 14 and 15.",
            "Using the cosine rule, cos A = (14² + 15² − 13²)/(2 × 14 × 15) = 140/420 = 1/3, "
            "so sin A = √(8/9) and the area is ½ × 14 × 15 × √(8/9) ≈ 98.9.",
            "Find an angle by the cosine rule, then apply the area formula.", "R"),
           ("7.3.3", "Write a complete solution to the navigation problem: a ship sails 25 km "
            "on a bearing of 030° then 18 km on a bearing of 120°. Find the distance and "
            "bearing from the start.",
            "The turn is 90°, so the distance is √(25² + 18²) ≈ 30.8 km and the bearing is "
            "030° + arctan(18/25) ≈ 065.7°.",
            "Extract the interior angle from the bearings, then use Pythagoras.", "R"),
           ("7.3.4", "Write a complete solution to finding the angle between the space "
            "diagonal of a cuboid with edges 2, 3 and 6 and the longest edge.",
            "The space diagonal is √(4 + 9 + 36) = 7, so the cosine of the angle is 6/7 and "
            "the angle is about 31.0°.",
            "Two applications of Pythagoras, then a cosine ratio.", "R"),
           ("7.3.5", "Write a complete solution to finding the surface area of a cone of "
            "radius 5 and slant height 13.",
            "The curved surface area is πrl = 65π ≈ 204.2, and with the base the total is "
            "65π + 25π = 90π ≈ 282.7.",
            "Curved area is π times radius times slant height.", "F"),
           ("7.3.6", "Write a complete solution to finding the height of a building observed "
            "from 40 m away at an angle of elevation of 27°.",
            "h = 40 tan 27° ≈ 20.4 m.", "Right-angled trigonometry with the angle of "
            "elevation.", "F"),
           ("7.3.7", "Write a complete solution to proving the cosine rule.",
            "Place B at the origin and C at (a, 0); then A is at (c cos B, c sin B). "
            "Expanding |AC|² gives a² + c² − 2ac cos B.",
            "Coordinate proof using Pythagoras on the two components.", "C"),
           ("7.3.8", "Write a complete solution to solving the triangle with a = 11, "
            "b = 14 and A = 42°, stating the number of solutions.",
            "b sin A ≈ 9.37 and 9.37 < 11 < 14, so two solutions: B ≈ 57.9° "
            "with C ≈ 80.1° and c ≈ 16.28, or B ≈ 122.1° with C ≈ 15.9° and "
            "c ≈ 4.42.",
            "Check the ambiguous case first, then apply the sine rule to "
            "both values of B.", "R"),
           ("7.3.9", "Write a complete solution to finding the area of the triangle "
            "with sides 13, 14 and 15.",
            "cos A = (196 + 225 − 169)/(2 × 14 × 15) = 252/420 = 0.6, so "
            "sin A = 0.8 and the area is ½ × 14 × 15 × 0.8 = 84.",
            "Find an angle by the cosine rule, then apply the area formula.", "R"),
           ("7.3.10", "Write a complete solution to the navigation problem: a ship "
            "sails 35 km on a bearing of 050° then 28 km on a bearing of "
            "140°. Find the distance and bearing from the start.",
            "The turn is 90°, so the distance is √(35² + 28²) = √2009 ≈ "
            "44.8 km and the bearing is 050° + arctan(28/35) ≈ 088.6°.",
            "Extract the interior angle from the bearings, then use "
            "Pythagoras.", "R"),
           ("7.3.11", "Write a complete solution to finding the angle between the "
            "space diagonal of a cuboid with edges 4, 4 and 6 and the "
            "longest edge.",
            "The space diagonal is √(16 + 16 + 36) = √68 ≈ 8.246, so the "
            "cosine of the angle is 6/8.246 and the angle is about 43.3°.",
            "Two applications of Pythagoras, then a cosine ratio.", "R"),
           ("7.3.12", "Write a complete solution to proving the cosine rule.",
            "Place B at the origin and C at (a, 0); then A is at (c cos B, "
            "c sin B). Expanding |AC|² gives a² + c² − 2ac cos B.",
            "Coordinate proof using Pythagoras on the two components.", "C"),
           ],
        D=[("7.4.1", "A rescue team is at A and a casualty is at C. A marker at B is 400 m "
            "from A on a bearing of 070°, and the bearing of C from A is 110° while the "
            "bearing of C from B is 160°. Find the distance AC.",
            "The angle at A is 40° and at B is 90°, so C is 50°; by the sine rule "
            "AC = 400 sin 90° ÷ sin 50° ≈ 522 m.",
            "Extract the interior angles, then apply the sine rule.", "A"),
           ("7.4.2", "Two cars leave a junction at the same time, one at 60 km/h on a bearing "
            "of 020° and one at 80 km/h on a bearing of 140°. Find the distance between them "
            "after 30 minutes.",
            "The distances are 30 and 40 km and the included angle is 120°, so the distance is "
            "√(30² + 40² − 2 × 30 × 40 × cos 120°) = √3700 ≈ 60.8 km.",
            "Use the cosine rule with the bearing difference.", "A"),
           ("7.4.3", "A radio mast is 40 m tall. From a point on level ground the angle of "
            "elevation to the top is 28°. Find the distance from the point to the base, to "
            "the nearest metre.",
            "d = 40 ÷ tan 28° ≈ 75.3 m, so 75 m.", "Right-angled trigonometry.", "A"),
           ("7.4.4", "A triangular field has sides 120 m and 150 m with an included angle of "
            "72°. Find the area and the length of the third side.",
            "Area = ½ × 120 × 150 × sin 72° ≈ 8568 m²; the third side is "
            "√(120² + 150² − 2 × 120 × 150 × cos 72°) ≈ 161.2 m.",
            "Area formula and cosine rule.", "A"),
           ("7.4.5", "A pilot flies 200 km on a bearing of 315° and then 150 km on a bearing "
            "of 045°. Find the distance and bearing from the start, and comment on the shape "
            "of the route.",
            "The two legs are perpendicular, so the distance is √(200² + 150²) = 250 km and "
            "the bearing is 315° − arctan(150/200) ≈ 278°.",
            "The bearing difference is 90°, so Pythagoras applies.", "A"),
           ("7.4.6", "A pyramid has a square base of side 8 and a vertical height of 3√7. "
            "Find the slant height, the angle between a face and the base, and the total "
            "surface area.",
            "Slant height √(16 + 63) = √79 ≈ 8.89; the angle has tangent 3√7/4, about 71.9°; "
            "the surface area is 64 + 4 × ½ × 8 × √79 ≈ 205.5.",
            "The cross-section through the apex and a base edge midpoint.", "A"),
           ("7.4.7", "A student solves an SSA problem and reports only one triangle. Explain "
            "what must be checked and what the correct procedure is.",
            "Compare the given side with the perpendicular height b sin A: if a < b sin A "
            "there is no triangle, if a = b sin A exactly one right triangle, if "
            "b sin A < a < b two triangles, and if a ≥ b one triangle. Both solutions must "
            "be reported when there are two.",
            "The comparison is made before any angle is computed.", "R"),
           ("7.4.8", "A lighthouse is visible from a ship when the ship is within 25 km. The "
            "ship's bearings from the lighthouse are recorded at two times 40 minutes apart, "
            "at 030° and 075°. If the ship sails at 20 km/h, find its closest approach to the "
            "lighthouse.",
            "The ship travels 13.33 km; the closest approach is 25 sin 45° ≈ 17.7 km, "
            "reached when the bearing to the lighthouse is perpendicular to the course.",
            "The tangent from the ship's position to the visibility circle gives the closest "
            "approach.", "A"),
           ("7.4.9", "A roof is built as two rectangular planes meeting at a ridge. Each "
            "plane is 6 m wide and the horizontal span is 10 m. Find the angle between the "
            "two planes and the height of the ridge.",
            "The cross-section is an isosceles triangle with sides 6, 6 and 10, so the height "
            "is √(36 − 25) = √11 ≈ 3.32 m and the half-angle has cosine 5/6, giving a full "
            "angle of about 67.1°.",
            "The cross-section perpendicular to the ridge is a triangle.", "A"),
           ("7.4.10", "A student measures a = 5, b = 8 and A = 30° and concludes no triangle "
            "exists. Investigate and justify.",
            "Correct: b sin A = 8 × 0.5 = 4 and a = 5 > 4, so the comparison a < b sin A "
            "fails. Since also 5 < 8, the case b sin A < a < b holds, so there are in fact "
            "two triangles, with B ≈ 53.1° or 126.9°.",
            "Compare a with b sin A and with b.", "R"),
           ("7.4.11", "A communications mast is supported by three cables attached at the "
            "top and anchored 12 m from the base, equally spaced. The mast is 20 m tall. "
            "Find the length of each cable and the angle each makes with the ground.",
            "Each cable is √(20² + 12²) ≈ 23.3 m and makes an angle of arctan(20/12) ≈ 59.0° "
            "with the ground.", "Right-angled trigonometry.", "A"),
           ("7.4.12", "A map is drawn to a scale of 1 : 25 000. Two landmarks are 8.4 cm "
            "apart on the map and the bearing between them is 132°. Find the real distance "
            "and describe how the bearing is used.",
            "The real distance is 8.4 × 250 m = 2100 m, and the bearing gives the direction, "
            "so the displacement is 2100 m on a bearing of 132°.",
            "Multiply the map distance by the scale factor.", "A")],
    ),
    assessment=[
        dict(title="A1 · The survey",
             text="A surveyor measures a baseline AB of 150 m. From A a point C has a bearing "
                  "of 055° and from B a bearing of 105°. Find the distance AC and BC, and "
                  "the area of the triangle ABC. State any assumption the surveyor has made.",
             note="Criteria C and D · extract the interior angles, apply the sine rule, and "
                  "justify the assumption."),
        dict(title="A2 · The ambiguous case",
             text="A triangle has A = 42°, a = 9 and b = 12. Determine how many triangles "
                  "exist, find all of them, and explain in general when two sides and a "
                  "non-included angle determine two triangles. Then find the area of each "
                  "triangle you have found.",
             note="Criteria C and D · check the ambiguous case explicitly, solve both "
                  "triangles, and generalise the condition."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of space, change "
        "and measurement appear in your work?",
        "How is the global context of orientation in space and time, and its exploration of "
        "navigation, surveying and the geometry of place, visible in the investigations and "
        "examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of triangulation as a measurement method, and what would "
        "you still like to ask?",
    ],
    review=dict(
        ideas=["The sine rule is a/sin A = b/sin B = c/sin C.",
               "The cosine rule is a² = b² + c² − 2bc cos A.",
               "The area of a triangle is ½ab sin C, where C is the included angle.",
               "Two sides and a non-included angle give zero, one or two triangles.",
               "Two triangles exist when b sin A < a < b.",
               "b sin A = a gives exactly one right triangle.",
               "a < b sin A gives no triangle.",
               "A bearing is measured clockwise from north as a three-figure angle.",
               "A three-dimensional problem is solved by choosing a plane.",
               "The angle between a line and a plane uses the line's projection onto the "
               "plane."],
        vocab=["sine rule", "cosine rule", "included angle", "non-included angle", "ambiguous "
               "case", "perpendicular height", "bearing", "angle of elevation", "space "
               "diagonal", "slant height", "triangulation", "baseline", "projection",
               "circumradius"],
        mixed=[("7.R1", "In triangle ABC, A = 50°, B = 60° and a = 8. Find b and c."),
               ("7.R2", "Find the area of the triangle with sides 9, 10 and included angle "
                "65°."),
               ("7.R3", "In triangle ABC, A = 35°, a = 6 and b = 10. How many triangles "
                "exist?"),
               ("7.R4", "A cuboid has edges 5, 12 and 13. Find the space diagonal."),
               ("7.R5", "A ship sails 40 km on a bearing of 080° then 30 km on a bearing of "
                "170°. Find the distance from the start."),
               ("7.R6", "Explain when the cosine rule is preferred to the sine rule.")],
    ),
    projects=dict(
        service=[("Community need", "Distances that matter locally cannot be measured "
                                    "directly, and no one has measured them."),
                 ("Mathematical connection", "The sine and cosine rules and triangulation."),
                 ("Proposed action", "Measure the height of a local landmark or the width of "
                                     "a local space by triangulation, and publish the method "
                                     "and the result with its uncertainty."),
                 ("Expected impact", "A figure that was guessed becomes a figure that is "
                                     "justified."),
                 ("Student reflection", "Record the baseline, the angles, the result and the "
                                        "check.")],
        community=[("Project idea", "A survey of an unusable community space."),
                   ("Need", "The space is discussed without any measurement of it."),
                   ("Research question", "What are the dimensions of the space, measured "
                                         "without entering it?"),
                   ("Mathematics", "Trigonometry in three dimensions and triangulation."),
                   ("Action or outcome", "A measured plan with the method explained."),
                   ("Beneficiaries", "Everyone who plans to use the space."),
                   ("Evidence", "The plan and the measurements behind it.")],
        personal=[("Personal interest", "Navigation, sport, astronomy or drones."),
                  ("Learning goal", "To find a distance you cannot measure directly and "
                                    "state its uncertainty."),
                  ("Product or outcome", "A measurement with a method and a check."),
                  ("Mathematics", "The sine and cosine rules and triangulation."),
                  ("Process", "Choose a baseline, measure two angles, solve the triangle, and "
                              "check the angle sum."),
                  ("Evidence", "The measurement and the triangle you solved.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=8, title="Vectors and Matrices",
    key="Form", related=["Space", "Representation", "Systems"],
    context="Scientific and technical innovation",
    exploration="computer graphics, navigation and engineering",
    inquiry=("Vectors encode displacement by magnitude and direction, while matrices encode "
             "transformations of the plane as arrays of numbers; the determinant measures how "
             "a transformation stretches or collapses area, and decides whether it can be "
             "undone."),
    atl=("Critical thinking",
         "In order for a student to decide whether a transformation can be reversed, "
         "students must compute the determinant, connect its value to the area scale factor, "
         "and justify when an inverse exists."),
    standfirst="A vector is a quantity with magnitude and direction, and a matrix is an array "
               "that transforms one. Together they describe displacements, forces and the "
               "transformations that move a plane onto itself.",
    engage="A computer graphics program rotates a shape, then stretches it, then rotates it "
           "back. The programmer needs one matrix that does all three. How are the three "
           "matrices combined, and how can the program tell whether the result can still be "
           "undone?",
    questions=[("Factual", "What do the magnitude of a vector, the scalar product and the "
                           "determinant of a matrix measure?"),
               ("Conceptual", "Why does the determinant of a product equal the product of the "
                              "determinants, and what does a zero determinant mean?"),
               ("Debatable", "If a transformation collapses a shape to a line, has it "
                             "destroyed information or merely hidden it?")],
    application_lede="These tasks use vectors and matrices. State the vector or matrix you "
                     "compute, give the geometric meaning of the determinant, and check "
                     "every inverse by multiplication.",
    projects_lede="A transformation is a rule with a matrix. Name the rule, give its matrix, "
                  "and say what its determinant tells you about the image.",
    sections=[
        dict(id="8.1", title="Vectors: notation and operations",
             inquiry_q="What does a vector record that a number cannot?",
             teach=[
                 "A vector is a quantity with magnitude and direction, written as a column vector or in bold, and it describes a displacement in space. Two vectors are equal when they have the same magnitude and direction, wherever they are drawn.",
                 "Vectors add by the triangle rule: the sum of a and b is the displacement from the start of a to the end of b when they are placed head to tail. Scalar multiplication scales the magnitude and leaves the direction unchanged, or reverses it when the scalar is negative.",
                 "The magnitude of a vector a = (x, y) is |a| = √(x² + y²), which is its length. A unit vector has magnitude 1, and dividing a vector by its magnitude gives the unit vector in the same direction.",
                 "The scalar product a · b = |a||b| cos θ is a number, not a vector. It is zero exactly when the vectors are perpendicular, which makes it the standard test for right angles.",
             ], examples=[
                 dict(q="Given a = (3, −2) and b = (−1, 5), find 3a − 2b and its magnitude.",
                      vis=F("table", [["step", "working", "result"],
                                      ["3a", "3 × (3, −2)", "(9, −6)"],
                                      ["2b", "2 × (−1, 5)", "(−2, 10)"],
                                      ["3a − 2b", "(9 − (−2), −6 − 10)", "(11, −16)"],
                                      ["magnitude", "√(11² + 16²)", "√377 ≈ 19.42"]],
                            caption="Scalar multiplication acts on each component."),
                      reasoning="Scale each vector, then combine component by component.",
                      steps=["3a = 3 × (3, −2) = (9, −6).",
                             "2b = 2 × (−1, 5) = (−2, 10).",
                             "So 3a − 2b = (9, −6) − (−2, 10) = (11, −16).",
                             "The magnitude is √(11² + 16²) = √(121 + 256) = √377 ≈ 19.42.",
                             "The direction is given by the angle arctan(−16/11), which is "
                             "below the positive x-axis."],
                      ans="3a − 2b = (11, −16), magnitude about 19.42",
                      interp="Vector arithmetic is component-wise, and the magnitude is "
                             "recovered from the components by Pythagoras."),
                 dict(q="Show that the vectors (4, 3) and (−6, 8) are perpendicular.",
                      vis=F("table", [["vector", "components", "magnitude"],
                                      ["u", "(4, 3)", "5"],
                                      ["v", "(−6, 8)", "10"],
                                      ["u · v", "4(−6) + 3(8)", "0"],
                                      ["conclusion", "perpendicular", "—"]],
                            caption="A zero scalar product is the test for perpendicularity."),
                      reasoning="Compute the scalar product and check whether it is zero.",
                      steps=["The scalar product is u · v = 4(−6) + 3(8) = −24 + 24 = 0.",
                             "Since the scalar product is zero, the vectors are "
                             "perpendicular.",
                             "Check with the formula u · v = |u||v| cos θ: 0 = 5 × 10 × cos θ "
                             "gives cos θ = 0.",
                             "So θ = 90°, confirming the result.",
                             "The magnitudes were 5 and 10, but only the product mattered."],
                      ans="they are perpendicular",
                      interp="The scalar product test is faster than finding the angle, and it "
                             "is exact."),
             ], inv=dict(
                 task="Take the vectors a = (2, 1), b = (−3, 4), c = (1, −2) and d = (0, 5). "
                      "Compute a + b, a − c, 2b + d, |a|, |b|, the unit vector in the "
                      "direction of a, and the scalar products a · b, a · c and b · d. "
                      "Record which pairs are perpendicular.",
                 table=[["quantity", "working", "result"],
                        ["a + b", "(2 − 3, 1 + 4)", "(−1, 5)"],
                        ["a − c", "(2 − 1, 1 − (−2))", "(1, 3)"],
                        ["2b + d", "(−6 + 0, 8 + 5)", "(−6, 13)"],
                        ["|a|", "√(4 + 1)", "√5 ≈ 2.24"],
                        ["|b|", "√(9 + 16)", "5"],
                        ["unit vector along a", "(2, 1) ÷ √5", "(0.894, 0.447)"],
                        ["a · b", "−6 + 4", "−2"],
                        ["a · c", "2 − 2", "0, so perpendicular"],
                        ["b · d", "0 + 20", "20"]],
                 notice=["The scalar product a · c was zero, so those two vectors were "
                         "perpendicular.",
                         "The scalar product a · b was negative, so the angle between them "
                         "was obtuse.",
                         "The unit vector had magnitude 1 and the same direction as a.",
                         "Vector addition and subtraction were component-wise throughout."],
                 obs="Vectors combine component-wise, and the scalar product measures the "
                     "alignment of a pair.",
                 concl="A vector records magnitude and direction, and its arithmetic is "
                       "component-wise: addition and subtraction combine the components, and "
                       "scalar multiplication scales them. The magnitude is recovered by "
                       "Pythagoras and the scalar product measures alignment, being zero "
                       "exactly for perpendicular vectors. Here a · c was 0, so a and c were "
                       "perpendicular.")),
        dict(id="8.2", title="Vectors and geometry",
             inquiry_q="How does vector notation prove a geometric claim?",
             teach=[
                 "A position vector gives the position of a point relative to an origin, and the vector between two points is the difference of their position vectors. Writing geometry in vectors is a representation that turns a diagram into an algebra.",
                 "Three points are collinear exactly when the vector between two of them is a scalar multiple of the vector between another pair. This is a single equation in two components, and it is the standard collinearity test.",
                 "The midpoint of AB has position vector (a + b)/2, and the point dividing AB in the ratio m : n has position vector (n a + m b)/(m + n). Both formulas come from a single linear combination.",
                 "The scalar product proves perpendicularity and computes angles, and the vector product in three dimensions gives a vector perpendicular to two others. These tools make vector proofs of geometric theorems short and checkable.",
             ], examples=[
                 dict(q="Show that the points A(1, 2), B(4, 6) and C(7, 10) are collinear.",
                      vis=F("table", [["vector", "components", "ratio of components"],
                                      ["AB", "(3, 4)", "—"],
                                      ["BC", "(3, 4)", "1 : 1"],
                                      ["AC", "(6, 8)", "2 : 1"],
                                      ["conclusion", "AB = BC, so collinear", "—"]],
                            caption="Equal vectors between consecutive points prove "
                                    "collinearity."),
                      reasoning="Compute the vectors between consecutive points and check "
                               "whether one is a multiple of the other.",
                      steps=["The position vectors are a = (1, 2), b = (4, 6) and c = (7, 10).",
                             "Then AB = b − a = (3, 4) and BC = c − b = (3, 4).",
                             "Since AB = BC exactly, the two vectors are equal and hence "
                             "parallel.",
                             "They also share the point B, so A, B and C lie on one straight "
                             "line.",
                             "Moreover B is the midpoint of AC, because AB = BC."],
                      ans="the three points are collinear, and B is the midpoint of AC",
                      interp="One computation settles both collinearity and the midpoint "
                             "claim."),
                 dict(q="Find the point that divides the line from P(2, −1) to Q(8, 5) in the "
                        "ratio 2 : 3.",
                      vis=F("table", [["step", "working", "result"],
                                      ["formula", "(3p + 2q)/5", "—"],
                                      ["x-coordinate", "(3 × 2 + 2 × 8)/5", "22/5 = 4.4"],
                                      ["y-coordinate", "(3 × (−1) + 2 × 5)/5", "7/5 = 1.4"],
                                      ["check", "the point lies between P and Q", "yes"]],
                            caption="A section formula is a weighted average."),
                      reasoning="Apply the section formula with the ratio 2 : 3.",
                      steps=["The point dividing PQ in the ratio 2 : 3 has position vector "
                             "(3p + 2q)/(2 + 3).",
                             "The x-coordinate is (3 × 2 + 2 × 8)/5 = 22/5 = 4.4.",
                             "The y-coordinate is (3 × (−1) + 2 × 5)/5 = 7/5 = 1.4.",
                             "So the point is (4.4, 1.4).",
                             "Check: it lies between P(2, −1) and Q(8, 5), as a section point "
                             "must."],
                      ans="(4.4, 1.4)",
                      interp="The weights are the opposite parts of the ratio, which is why "
                             "the formula has them crossed."),
             ], inv=dict(
                 task="Take the points A(0, 0), B(6, 2), C(9, 7) and D(3, 5). Determine "
                      "whether ABCD is a parallelogram, find the midpoints of the diagonals, "
                      "and check whether the diagonals are perpendicular. Then find the area "
                      "of the quadrilateral.",
                 table=[["quantity", "working", "result"],
                        ["AB", "(6, 2)", "—"],
                        ["DC", "(9 − 3, 7 − 5)", "(6, 2), so AB parallel and equal to DC"],
                        ["midpoint of AC", "(4.5, 3.5)", "—"],
                        ["midpoint of BD", "(4.5, 3.5)", "the same, so a parallelogram"],
                        ["AC · BD", "(9, 7) · (−3, 3)", "−27 + 21 = −6, not perpendicular"],
                        ["area", "half the magnitude of the cross term", "26"]],
                 notice=["The diagonals shared a midpoint, which proved the parallelogram.",
                         "The scalar product of the diagonals was −6, not zero, so they were "
                         "not perpendicular.",
                         "The area came from the determinant of the two side vectors.",
                         "Both conditions — parallel opposite sides and shared midpoint — "
                         "held."],
                 obs="A parallelogram is detected by equal opposite sides or by a shared "
                     "diagonal midpoint, and perpendicularity is a scalar product test.",
                 concl="Vector notation turns a geometric claim into an algebraic one: "
                       "collinearity is a scalar multiple, a parallelogram is equal opposite "
                       "sides or a shared diagonal midpoint, and perpendicularity is a zero "
                       "scalar product. The area of a parallelogram is the magnitude of the "
                       "determinant of its side vectors. Here the area was 26 and the "
                       "diagonals were not perpendicular.")),
        dict(id="8.3", title="Vectors in three dimensions",
             inquiry_q="What changes when a third dimension is added?",
             teach=[
                 "A three-dimensional vector has three components, and all the two-dimensional operations extend component-wise. The magnitude becomes √(x² + y² + z²) and the scalar product gains a third term.",
                 "The vector product a × b is defined only in three dimensions, and it gives a vector perpendicular to both a and b. Its magnitude is |a||b| sin θ, which is the area of the parallelogram spanned by a and b.",
                 "The vector product is anti-commutative: a × b = −(b × a). The order matters, and the right-hand rule fixes which of the two perpendicular directions is meant.",
                 "The scalar triple product a · (b × c) gives the volume of the parallelepiped spanned by the three vectors, and it is zero exactly when the three vectors are coplanar. It is the three-dimensional analogue of the determinant test.",
             ], examples=[
                 dict(q="Find the vector product of a = (1, 2, 3) and b = (4, 5, 6), and "
                        "verify it is perpendicular to both.",
                      vis=F("table", [["component", "working", "value"],
                                      ["x", "2(6) − 3(5)", "−3"],
                                      ["y", "3(4) − 1(6)", "6"],
                                      ["z", "1(5) − 2(4)", "−3"],
                                      ["a × b", "—", "(−3, 6, −3)"]],
                            caption="The cross product is computed from a 3 by 3 pattern."),
                      reasoning="Apply the component formula and check with scalar products.",
                      steps=["The vector product a × b = (a₂b₃ − a₃b₂, a₃b₁ − a₁b₃, "
                             "a₁b₂ − a₂b₁).",
                             "So a × b = (2 × 6 − 3 × 5, 3 × 4 − 1 × 6, 1 × 5 − 2 × 4).",
                             "That is (12 − 15, 12 − 6, 5 − 8) = (−3, 6, −3).",
                             "Check with a: a · (a × b) = 1(−3) + 2(6) + 3(−3) = −3 + 12 − 9 = "
                             "0.",
                             "Check with b: b · (a × b) = 4(−3) + 5(6) + 6(−3) = −12 + 30 − "
                             "18 = 0, so it is perpendicular to both."],
                      ans="a × b = (−3, 6, −3), perpendicular to both a and b",
                      interp="The two scalar-product checks are quick and confirm the "
                             "perpendicularity the definition promises."),
                 dict(q="Find the volume of the parallelepiped spanned by a = (2, 0, 1), "
                        "b = (1, 3, 0) and c = (0, 1, 4).",
                      vis=F("table", [["step", "working", "result"],
                                      ["b × c", "(3(4) − 0(1), 0(0) − 1(4), 1(1) − 3(0))",
                                       "(12, −4, 1)"],
                                      ["a · (b × c)", "2(12) + 0(−4) + 1(1)", "25"],
                                      ["volume", "the absolute value", "25"],
                                      ["coplanar?", "the triple product is not zero", "no"]],
                            caption="The scalar triple product is a volume."),
                      reasoning="Compute the vector product b × c, then its scalar product "
                               "with a.",
                      steps=["First b × c = (3 × 4 − 0 × 1, 0 × 0 − 1 × 4, 1 × 1 − 3 × 0) = "
                             "(12, −4, 1).",
                             "Then the scalar triple product is a · (b × c) = 2 × 12 + 0 × "
                             "(−4) + 1 × 1 = 25.",
                             "The volume is the absolute value, 25 cubic units.",
                             "Since the triple product is not zero, the three vectors are "
                             "not coplanar.",
                             "The sign would be negative if the order were reversed, which is "
                             "why the absolute value is taken."],
                      ans="volume 25 cubic units",
                      interp="The scalar triple product is the determinant of the 3 by 3 "
                             "matrix with the three vectors as rows, which is why it also "
                             "tests coplanarity."),
             ], inv=dict(
                 task="Take the vectors a = (1, 1, 0), b = (0, 1, 1) and c = (1, 0, 1). "
                      "Compute |a|, |b|, |c|, a · b, b · c, c · a, a × b and the scalar triple "
                      "product a · (b × c). Then decide whether the three vectors are "
                      "coplanar and explain how you know.",
                 table=[["quantity", "working", "result"],
                        ["|a|", "√(1 + 1 + 0)", "√2 ≈ 1.414"],
                        ["|b|", "√(0 + 1 + 1)", "√2 ≈ 1.414"],
                        ["|c|", "√(1 + 0 + 1)", "√2 ≈ 1.414"],
                        ["a · b", "0 + 1 + 0", "1"],
                        ["b · c", "0 + 0 + 1", "1"],
                        ["c · a", "1 + 0 + 0", "1"],
                        ["a × b", "(1(1) − 0(1), 0(0) − 1(1), 1(1) − 1(0))", "(1, −1, 1)"],
                        ["a · (b × c)", "1(1) + 1(−1) + 0(1)", "0, so coplanar"]],
                 notice=["All three vectors had the same magnitude, √2.",
                         "All three scalar products were 1, so the angles were all equal.",
                         "The scalar triple product was zero, so the three vectors were "
                         "coplanar.",
                         "The vectors formed a regular pattern in the plane x + y + z = 1."],
                 obs="A zero scalar triple product is the test for coplanarity.",
                 concl="Adding a third dimension extends every operation component-wise and "
                       "adds the vector product, whose magnitude is an area and whose "
                       "direction is perpendicular to both factors. The scalar triple "
                       "product is a volume and vanishes exactly for coplanar vectors. Here "
                       "all three vectors had magnitude √2, all pairwise angles were equal, "
                       "and the triple product was 0.")),
        dict(id="8.4", title="Matrices and transformations",
             inquiry_q="How does a matrix encode a transformation?",
             teach=[
                 "A 2 by 2 matrix acts on a column vector by multiplication, and the two columns of the matrix are the images of the basis vectors (1, 0) and (0, 1). This representation determines the whole transformation by where it sends the basis.",
                 "The matrix for a rotation through θ is [[cos θ, −sin θ], [sin θ, cos θ]], for a reflection in a line through the origin at angle θ it is [[cos 2θ, sin 2θ], [sin 2θ, −cos 2θ]], and for an enlargement of factor k it is [[k, 0], [0, k]].",
                 "Composition of transformations is matrix multiplication in the same order: applying M then N is the matrix NM, so systems of transformations compose by multiplying their matrices. The order matters, which is why matrix multiplication is not commutative.",
                 "A transformation with matrix M is linear exactly when M(au + bv) = aM(u) + bM(v), which every matrix multiplication satisfies. Linearity is what makes matrices the natural language for transformations.",
             ], examples=[
                 dict(q="Find the image of the point (3, 1) under the matrix "
                        "[[2, 1], [−1, 3]], and describe the transformation.",
                      vis=F("table", [["step", "working", "result"],
                                      ["image of (1, 0)", "the first column", "(2, −1)"],
                                      ["image of (0, 1)", "the second column", "(1, 3)"],
                                      ["image of (3, 1)", "3(2, −1) + (1, 3)", "(7, 0)"],
                                      ["determinant", "2(3) − 1(−1)", "7"]],
                            caption="The columns are the images of the basis vectors."),
                      reasoning="Read the images of the basis vectors from the columns, then "
                               "combine them for the given point.",
                      steps=["The first column (2, −1) is the image of (1, 0).",
                             "The second column (1, 3) is the image of (0, 1).",
                             "The image of (3, 1) is 3 × (2, −1) + 1 × (1, 3) = (6, −3) + "
                             "(1, 3) = (7, 0).",
                             "Check by direct multiplication: 2(3) + 1(1) = 7 and −1(3) + "
                             "3(1) = 0.",
                             "The determinant is 2 × 3 − 1 × (−1) = 7, so areas are "
                             "multiplied by 7."],
                      ans="(7, 0); the determinant is 7",
                      interp="Reading the columns as the images of the basis vectors is the "
                             "quickest way to understand a matrix."),
                 dict(q="Write the matrix for a rotation through 60° and find the image of "
                        "the point (1, 0).",
                      vis=F("table", [["entry", "value", "position in the matrix"],
                                      ["cos 60°", "0.5", "top left"],
                                      ["−sin 60°", "−0.8660", "top right"],
                                      ["sin 60°", "0.8660", "bottom left"],
                                      ["cos 60°", "0.5", "bottom right"]],
                            caption="The rotation matrix has a fixed pattern."),
                      reasoning="Substitute the angle into the rotation matrix and multiply.",
                      steps=["The rotation matrix for angle θ is [[cos θ, −sin θ], "
                             "[sin θ, cos θ]].",
                             "With θ = 60°, this is [[0.5, −0.8660], [0.8660, 0.5]].",
                             "The image of (1, 0) is the first column, (0.5, 0.8660).",
                             "Its magnitude is √(0.25 + 0.75) = 1, as a rotation preserves "
                             "length.",
                             "The image of (0, 1) is the second column, (−0.8660, 0.5), also "
                             "of magnitude 1."],
                      ans="[[0.5, −0.8660], [0.8660, 0.5]]; the image of (1, 0) is "
                          "(0.5, 0.8660)",
                      interp="The determinant of a rotation matrix is 1, which is why "
                             "rotations preserve area."),
             ], inv=dict(
                 task="Write the matrices for a rotation through 90°, a reflection in the "
                      "line y = x, and an enlargement of factor 3. Apply each to the points "
                      "(1, 0), (0, 1) and (2, 1), and record the images. Then compute the "
                      "product of the rotation and the reflection matrices in both orders "
                      "and comment on the difference.",
                 table=[["transformation", "matrix", "image of (1, 0)", "image of (0, 1)",
                                "determinant"],
                        ["rotation 90°", "[[0, −1], [1, 0]]", "(0, 1)", "(−1, 0)", "1"],
                        ["reflection in y = x", "[[0, 1], [1, 0]]", "(0, 1)", "(1, 0)", "−1"],
                        ["enlargement 3", "[[3, 0], [0, 3]]", "(3, 0)", "(0, 3)", "9"],
                        ["rotation then reflection", "[[1, 0], [0, −1]]", "(1, 0)", "(0, −1)",
                         "−1"],
                        ["reflection then rotation", "[[−1, 0], [0, 1]]", "(−1, 0)", "(0, 1)",
                         "−1"]],
                 notice=["The rotation and the reflection both preserved lengths, but their "
                         "determinants differed in sign.",
                         "The enlargement multiplied every length by 3 and areas by 9.",
                         "The two products were different matrices, confirming that order "
                         "matters.",
                         "Both products were reflections, one in the x-axis and one in the "
                         "y-axis."],
                 obs="The columns of a matrix are the images of the basis vectors, and the "
                     "determinant is the area scale factor.",
                 concl="A matrix encodes a transformation by recording the images of the "
                       "basis vectors in its columns, and composition is matrix "
                       "multiplication in the order of application. The determinant is the "
                       "area scale factor, positive for orientation-preserving "
                       "transformations and negative for orientation-reversing ones. Here "
                       "the rotation then reflection gave [[1, 0], [0, −1]] while the "
                       "reverse order gave [[−1, 0], [0, 1]].")),
        dict(id="8.5", title="Determinants and inverse matrices",
             inquiry_q="What does the determinant decide?",
             teach=[
                 "The determinant of [[a, b], [c, d]] is ad − bc. It is the signed area scale factor of the transformation: the area of an image is |det| times the area of the original.",
                 "A negative determinant means the transformation reverses orientation, as a reflection does. A determinant of zero means the transformation collapses the plane onto a line or a point, and the transformation cannot be undone.",
                 "The inverse matrix exists exactly when the determinant is not zero, and it is given by (1/det)[[d, −b], [−c, a]]. The check is that the product of the matrix and its inverse is the identity.",
                 "The determinant of a product is the product of the determinants, so det(AB) = det(A) det(B). This is why a single non-invertible matrix in a product makes the whole product non-invertible.",
             ], examples=[
                 dict(q="Find the determinant and, if it exists, the inverse of "
                        "[[4, 7], [2, 3]].",
                      vis=F("table", [["step", "working", "result"],
                                      ["determinant", "4(3) − 7(2)", "−2"],
                                      ["adjugate", "[[3, −7], [−2, 4]]", "—"],
                                      ["inverse", "(1/(−2)) × adjugate",
                                       "[[−1.5, 3.5], [1, −2]]"],
                                      ["check", "M × M⁻¹", "the identity"]],
                            caption="A negative determinant reverses orientation."),
                      reasoning="Compute the determinant, form the adjugate, and verify by "
                               "multiplication.",
                      steps=["The determinant is 4 × 3 − 7 × 2 = 12 − 14 = −2.",
                             "Since it is not zero, the inverse exists.",
                             "The adjugate is [[3, −7], [−2, 4]].",
                             "So the inverse is (−1/2)[[3, −7], [−2, 4]] = [[−1.5, 3.5], "
                             "[1, −2]].",
                             "Check: multiplying the matrix by this gives the identity "
                             "matrix."],
                      ans="det = −2; inverse [[−1.5, 3.5], [1, −2]]",
                      interp="The negative determinant means the transformation reverses "
                             "orientation, and areas are halved."),
                 dict(q="Show that [[2, 4], [3, 6]] has no inverse and describe what the "
                        "transformation does.",
                      vis=F("table", [["step", "working", "result"],
                                      ["determinant", "2(6) − 4(3)", "0"],
                                      ["columns", "(2, 3) and (4, 6)", "one is double the "
                                       "other"],
                                      ["image of the plane", "the line through (2, 3)", "a "
                                       "line"],
                                      ["inverse", "does not exist", "—"]],
                            caption="A zero determinant collapses the plane onto a line."),
                      reasoning="Compute the determinant and interpret a zero value.",
                      steps=["The determinant is 2 × 6 − 4 × 3 = 12 − 12 = 0.",
                             "So the inverse does not exist.",
                             "The second column (4, 6) is twice the first (2, 3), so the two "
                             "basis vectors map to parallel vectors.",
                             "Every image is a multiple of (2, 3), so the whole plane is "
                             "collapsed onto that line.",
                             "The collapse cannot be undone, because many points share one "
                             "image."],
                      ans="no inverse; the transformation collapses the plane onto the line "
                          "through (2, 3)",
                      interp="A zero determinant is the algebraic signature of a collapse, "
                             "and it is the reason the inverse fails to exist."),
             ], inv=dict(
                 task="Take the matrices M = [[1, 2], [3, 4]], N = [[0, 1], [−1, 0]] and "
                      "P = [[2, 0], [0, 3]]. Compute det M, det N, det P, det(MN), det(MP) "
                      "and det(MNP). Find M⁻¹ and check it by multiplication. Then find a "
                      "matrix Q with det Q = 0 and describe what its transformation does.",
                 table=[["quantity", "working", "result"],
                        ["det M", "1(4) − 2(3)", "−2"],
                        ["det N", "0(0) − 1(−1)", "1"],
                        ["det P", "2(3) − 0(0)", "6"],
                        ["det(MN)", "−2 × 1", "−2"],
                        ["det(MP)", "−2 × 6", "−12"],
                        ["det(MNP)", "−2 × 1 × 6", "−12"],
                        ["M⁻¹", "(1/(−2))[[4, −2], [−3, 1]]", "[[−2, 1], [1.5, −0.5]]"],
                        ["Q = [[1, 2], [2, 4]]", "det 0", "collapses onto a line"]],
                 notice=["Every product determinant was the product of the individual "
                         "determinants.",
                         "The determinant of N was 1, so that rotation preserved area.",
                         "The determinant of P was 6, so that enlargement multiplied areas by "
                         "6.",
                         "The matrix Q had determinant 0 and collapsed the plane onto a "
                         "line."],
                 obs="The determinant multiplies over products, and a zero determinant means "
                     "no inverse exists.",
                 concl="The determinant is the signed area scale factor of a transformation: "
                       "positive for orientation-preserving, negative for "
                       "orientation-reversing, and zero for a collapse. The inverse exists "
                       "exactly when the determinant is non-zero, and det(AB) = det(A) "
                       "det(B). Here det M = −2, det N = 1, det P = 6, and the product "
                       "determinants were −2, −12 and −12.")),
        dict(id="8.6", title="Investigation: area scale factors",
             inquiry_q="How does the determinant show up in an area?",
             teach=[
                 "The area of the parallelogram spanned by two vectors (a, b) and (c, d) is |ad − bc|, which is exactly the absolute value of the determinant. This is the geometric meaning of the determinant.",
                 "The same determinant is the scalar triple product in three dimensions, where it gives the volume of a parallelepiped. The pattern is the same in every dimension: the determinant measures the size of the image of a unit box.",
                 "When a transformation is applied to a shape, every area is multiplied by |det|. This is why the determinant is checked before computing an area after a transformation, and why a zero determinant means the area is destroyed.",
                 "The determinant also appears in the change of variables formula for integrals, where a change of coordinates multiplies areas by the Jacobian determinant. The same number measures the local stretching of a map.",
             ], examples=[
                 dict(q="Find the area of the parallelogram spanned by (3, 1) and (−2, 5).",
                      vis=F("table", [["step", "working", "result"],
                                      ["determinant", "3(5) − 1(−2)", "17"],
                                      ["area", "the absolute value", "17"],
                                      ["base", "|(3, 1)|", "√10 ≈ 3.16"],
                                      ["height", "17 ÷ √10", "5.38"]],
                            caption="The determinant is the signed area."),
                      reasoning="Form the determinant of the two vectors and take its absolute "
                               "value.",
                      steps=["The determinant of the two vectors is 3 × 5 − 1 × (−2) = 15 + "
                             "2 = 17.",
                             "The area is the absolute value, 17 square units.",
                             "Check with base times height: the base is |(3, 1)| = √10.",
                             "The height is the component of (−2, 5) perpendicular to (3, 1), "
                             "which is 17 ÷ √10 ≈ 5.38.",
                             "So the area is √10 × 5.38 ≈ 17, as required."],
                      ans="17 square units",
                      interp="The determinant gives the signed area, and the sign only "
                             "records the orientation of the pair."),
                 dict(q="A triangle has vertices (0, 0), (4, 1) and (1, 5). Find its area "
                        "using a determinant.",
                      vis=F("table", [["step", "working", "result"],
                                      ["side vectors", "(4, 1) and (1, 5)", "—"],
                                      ["determinant", "4(5) − 1(1)", "19"],
                                      ["parallelogram area", "19", "—"],
                                      ["triangle area", "19 ÷ 2", "9.5"]],
                            caption="A triangle is half the parallelogram."),
                      reasoning="Take the two side vectors from one vertex, form the "
                               "determinant, and halve it.",
                      steps=["The side vectors from the origin are (4, 1) and (1, 5).",
                             "Their determinant is 4 × 5 − 1 × 1 = 19.",
                             "The parallelogram spanned by them has area 19.",
                             "The triangle is half of that, so its area is 9.5.",
                             "Check with the shoelace formula, which gives the same value."],
                      ans="9.5 square units",
                      interp="The determinant formula for a triangle's area is faster than "
                             "finding a base and a height."),
             ], inv=dict(
                 task="Take the unit square with vertices (0, 0), (1, 0), (1, 1) and (0, 1). "
                      "Apply the matrices [[2, 1], [0, 3]] and [[1, 2], [3, 6]] to its "
                      "vertices, and find the area of each image. Compare the areas with the "
                      "determinants and explain what happens in the second case.",
                 table=[["matrix", "determinant", "image of the unit square", "area of image",
                                "orientation"],
                        ["[[2, 1], [0, 3]]", "6", "a parallelogram", "6", "preserved"],
                        ["[[1, 2], [3, 6]]", "0", "a line segment", "0", "destroyed"],
                        ["[[2, 1], [0, 3]] applied twice", "36", "a larger parallelogram",
                         "36", "preserved"],
                        ["[[0, 1], [1, 0]]", "−1", "the square, reflected", "1", "reversed"],
                        ["identity", "1", "the square itself", "1", "preserved"]],
                 notice=["The first image was a parallelogram of area 6, matching the "
                         "determinant.",
                         "The second image collapsed to a line segment of area 0, matching "
                         "the zero determinant.",
                         "The unit square's original area was 1, so the scale factors were 6 "
                         "and 0.",
                         "The collapse destroyed the area completely, which is why no "
                         "inverse exists."],
                 obs="The determinant is exactly the factor by which areas are multiplied.",
                 concl="The determinant of the matrix of two spanning vectors is the signed "
                       "area of the parallelogram they span, and the determinant of a "
                       "transformation is the factor by which every area is multiplied. A "
                       "zero determinant collapses the image onto a line and destroys the "
                       "area. Here the scale factors were 6 and 0.")),
        dict(id="8.7", title="Mixed practice",
             inquiry_q="Which operation does this problem need?",
             teach=[
                 "Vector problems are recognised by the presence of directions: displacement, force, velocity and position are all vectors. Scalar problems have magnitude only, and confusing the two is the commonest error.",
                 "Matrix problems are recognised by the presence of transformations. The order of composition is the order of application, read from right to left, and reversing it changes the answer.",
                 "The determinant is the bridge between the algebra and the geometry: it tells you the area scale factor and whether an inverse exists. Computing it early is a good habit, because it settles both questions at once.",
                 "Mixed practice is where the operation is chosen rather than given, so the reasoning behind the choice is part of what is being practised.",
             ], examples=[
                 dict(q="Given a = (3, −2) and b = (−1, 5), find 3a − 2b.",
                      vis=F("table", [["step", "working", "result"],
                                      ["3a", "(9, −6)", "—"],
                                      ["2b", "(−2, 10)", "—"],
                                      ["3a − 2b", "(9 − (−2), −6 − 10)", "(11, −16)"]],
                            caption="Component-wise arithmetic."),
                      reasoning="Scale each vector and combine component by component.",
                      steps=["3a = (9, −6) and 2b = (−2, 10).",
                             "Subtracting gives (9 − (−2), −6 − 10) = (11, −16).",
                             "The magnitude is √(121 + 256) = √377 ≈ 19.42.",
                             "The direction is arctan(−16/11), below the positive x-axis.",
                             "There is no ambiguity, because vector arithmetic is "
                             "component-wise."],
                      ans="(11, −16)",
                      interp="The components are combined separately, and the magnitude is "
                             "recovered only if it is needed."),
                 dict(q="Find the determinant of [[3, 5], [6, 10]] and explain why the "
                        "matrix has no inverse.",
                      vis=F("table", [["step", "working", "result"],
                                      ["determinant", "3(10) − 5(6)", "0"],
                                      ["columns", "(3, 6) and (5, 10)", "one is 5/3 of the "
                                       "other"],
                                      ["image", "the line through (3, 6)", "a line"],
                                      ["inverse", "does not exist", "—"]],
                            caption="Proportional columns give a zero determinant."),
                      reasoning="Compute the determinant and interpret a zero value.",
                      steps=["The determinant is 3 × 10 − 5 × 6 = 30 − 30 = 0.",
                             "The two columns are proportional, since (5, 10) is 5/3 of "
                             "(3, 6).",
                             "So the two basis vectors map to parallel vectors and the plane "
                             "collapses onto a line.",
                             "The collapse cannot be reversed, so no inverse exists.",
                             "The area scale factor is zero, which is the geometric "
                             "statement of the same fact."],
                      ans="determinant 0; no inverse exists",
                      interp="A zero determinant, proportional columns and a collapsed image "
                             "are three descriptions of one situation."),
             ], inv=dict(
                 task="Take the vectors a = (2, −1), b = (4, 3) and the matrices "
                      "M = [[1, −1], [2, 0]] and N = [[0, 2], [1, 1]]. Compute a + b, "
                      "2a − 3b, |a + b|, a · b, det M, det N, det(MN), M⁻¹, and the area of "
                      "the parallelogram spanned by a and b. Record the geometric meaning of "
                      "each determinant.",
                 table=[["quantity", "working", "result"],
                        ["a + b", "(6, 2)", "—"],
                        ["2a − 3b", "(4 − 12, −2 − 9)", "(−8, −11)"],
                        ["|a + b|", "√(36 + 4)", "√40 ≈ 6.32"],
                        ["a · b", "8 − 3", "5"],
                        ["det M", "1(0) − (−1)(2)", "2"],
                        ["det N", "0(1) − 2(1)", "−2"],
                        ["det(MN)", "2 × (−2)", "−4"],
                        ["M⁻¹", "(1/2)[[0, 1], [−2, 1]]", "[[0, 0.5], [−1, 0.5]]"],
                        ["area of parallelogram", "|2(3) − (−1)(4)|", "10"]],
                 notice=["The determinant of M was positive, so that transformation "
                         "preserved orientation.",
                         "The determinant of N was negative, so that transformation "
                         "reversed it.",
                         "The product determinant was the product, −4, reversing orientation "
                         "and scaling areas by 4.",
                         "The parallelogram area came from the determinant of the two side "
                         "vectors."],
                 obs="The determinant links the algebra of a matrix to the geometry of area "
                     "and orientation.",
                 concl="Vectors combine component-wise and matrices encode transformations, "
                       "with composition read in the order of application. The determinant "
                       "is the signed area scale factor and decides invertibility: it "
                       "multiplies over products, is positive for orientation-preserving "
                       "transformations and negative for orientation-reversing ones, and "
                       "zero exactly when no inverse exists. Here det M = 2, det N = −2 and "
                       "det(MN) = −4.")),
    ],
    practice=dict(
        A=[("8.1.1", "Given a = (3, −2) and b = (−1, 5), find 3a − 2b.",
            "(11, −16).", "Scale each vector, then subtract component-wise.", "F"),
           ("8.1.2", "Find the magnitude of the vector (6, 8).",
            "10.", "Use Pythagoras on the components.", "F"),
           ("8.1.3", "Find the unit vector in the direction of (3, 4).",
            "(0.6, 0.8).", "Divide by the magnitude, which is 5.", "F"),
           ("8.1.4", "Given a = (2, 5) and b = (−3, 1), find a · b.",
            "−6 + 5 = −1.", "Multiply corresponding components and add.", "F"),
           ("8.1.5", "Show that (1, 2) and (4, −2) are perpendicular.",
            "Their scalar product is 4 − 4 = 0, so they are perpendicular.",
            "A zero scalar product is the test.", "F"),
           ("8.1.6", "Given a = (1, 2, 3) and b = (4, 0, −1), find a · b.",
            "4 + 0 − 3 = 1.", "Include all three components.", "F"),
           ("8.1.7", "Find the determinant of [[5, 2], [3, 7]].",
            "35 − 6 = 29.", "Use ad − bc.", "F"),
           ("8.1.8", "Find the inverse of [[2, 0], [0, 4]], if it exists.",
            "The determinant is 8, so the inverse is [[0.5, 0], [0, 0.25]].",
            "Divide the adjugate by the determinant.", "F"),
           ("8.1.9", "Write the matrix for a rotation through 90°.",
            "[[0, −1], [1, 0]].", "Substitute into the rotation matrix.", "F"),
           ("8.1.10", "The point (2, 1) is transformed by [[1, 3], [0, 1]]. Find its image.",
            "(5, 1).", "Multiply the matrix by the column vector.", "F"),
           ("8.1.11", "Find the area of the parallelogram spanned by (4, 1) and (2, 5).",
            "|4(5) − 1(2)| = 18.", "The determinant of the two vectors.", "R"),
           ("8.1.12", "Explain why [[1, 2], [2, 4]] has no inverse.",
            "Its determinant is 4 − 4 = 0, so the columns are proportional and the "
            "transformation collapses the plane onto a line.",
            "A zero determinant means no inverse.", "R")],
        B=[("8.2.1", "Investigate the effect of the matrix [[k, 0], [0, 1/k]] for k = 2, 3 "
            "and 0.5, and justify what it does to areas.",
            "It stretches by k in one direction and compresses by k in the other, so areas "
            "are unchanged because the determinant is k × 1/k = 1.",
            "Compute the determinant and the images of the basis vectors.", "R"),
           ("8.2.2", "Conjecture a rule for when a 2 by 2 matrix represents a rotation, and "
            "test it on three matrices.",
            "It must have the form [[cos θ, −sin θ], [sin θ, cos θ]], so the columns are "
            "perpendicular unit vectors and the determinant is 1.",
            "Check the column lengths, their scalar product and the determinant.", "C"),
           ("8.2.3", "Investigate the images of the unit square under [[1, 1], [0, 1]] and "
            "[[1, 0], [1, 1]], and describe the transformations.",
            "Both are shears of area 1, one parallel to the x-axis and one parallel to the "
            "y-axis.", "Compute the images of the vertices and the determinant.", "R"),
           ("8.2.4", "Investigate the determinant of the product of two reflections, and "
            "justify the result.",
            "The determinant is (−1) × (−1) = 1, so the product is orientation-preserving "
            "and is a rotation or a translation.",
            "Use det(AB) = det(A) det(B).", "R"),
           ("8.2.5", "Take three vectors of your own in three dimensions and determine "
            "whether they are coplanar, justifying your answer.",
            "For example a = (1, 0, 0), b = (0, 1, 0), c = (1, 1, 0): the scalar triple "
            "product is 0, so they are coplanar.",
            "Compute the scalar triple product.", "R"),
           ("8.2.6", "Investigate the relationship between the determinant of a matrix and "
            "the determinant of its transpose, and justify.",
            "They are equal, because ad − bc is unchanged when the rows and columns are "
            "interchanged.", "Compare the two determinants algebraically.", "R"),
           ("8.2.7", "Investigate the vector product of two parallel vectors, and justify "
            "the result.",
            "It is the zero vector, because |a × b| = |a||b| sin θ and sin θ = 0 for parallel "
            "vectors.", "Use the magnitude formula with θ = 0.", "R"),
           ("8.2.8", "Investigate the determinant of the matrix [[cos θ, −sin θ], "
            "[sin θ, cos θ]] and justify why rotations preserve area.",
            "The determinant is cos²θ + sin²θ = 1, so every rotation has "
            "area scale factor 1.",
            "Compute ad − bc and use the Pythagorean identity.", "R"),
           ("8.2.9", "Conjecture a rule for the determinant of the inverse of a "
            "matrix, and test it.",
            "det(M⁻¹) = 1/det(M), because det(M) det(M⁻¹) = det(I) = 1.",
            "Use det(AB) = det(A) det(B) with B = M⁻¹.", "C"),
           ("8.2.10", "Investigate the image of a straight line under a matrix "
            "transformation and justify the result.",
            "A straight line maps to a straight line, because the "
            "transformation is linear: the image of a + tb is M a + t M b, "
            "which is a line.",
            "Apply the matrix to a general point on the line.", "R"),
           ("8.2.11", "Investigate the determinant of a matrix representing a shear, "
            "and justify.",
            "The determinant is 1, because a shear preserves area even "
            "though it changes shape.",
            "Compute ad − bc for [[1, k], [0, 1]].", "R"),
           ],
        C=[("8.3.1", "Write a complete solution to finding the image of (3, −1) under the "
            "matrix [[2, −1], [4, 3]] and the determinant of the matrix.",
            "The image is (2(3) − 1(−1), 4(3) + 3(−1)) = (7, 9) and the determinant is 6 + 4 "
            "= 10.", "Multiply, then compute ad − bc.", "R"),
           ("8.3.2", "Write a complete solution to showing that the points A(2, 1), B(5, 4) "
            "and C(−1, −5) are collinear.",
            "AB = (3, 3) and BC = (−6, −6) = −2(3, 3), so the vectors are parallel and share "
            "B; the points are collinear.",
            "Check whether one vector is a multiple of the other.", "R"),
           ("8.3.3", "Write a complete solution to finding the point dividing AB in the "
            "ratio 3 : 2 where A = (−2, 4) and B = (6, −2).",
            "The point is (2a + 3b)/5 = ((2(−2) + 3(6))/5, (2(4) + 3(−2))/5) = (14/5, 2/5) = "
            "(2.8, 0.4).", "Apply the section formula with the weights crossed.", "R"),
           ("8.3.4", "Write a complete solution to finding the vector product of (2, −1, 3) "
            "and (1, 4, −2), and verifying it is perpendicular to both.",
            "a × b = ((−1)(−2) − 3(4), 3(1) − 2(−2), 2(4) − (−1)(1)) = (−10, 7, 9); both "
            "scalar products are 0.",
            "Apply the component formula, then check with scalar products.", "C"),
           ("8.3.5", "Write a complete solution to finding the volume of the parallelepiped "
            "spanned by (1, 2, 3), (4, 5, 6) and (7, 8, 10).",
            "The scalar triple product is 1(5(10) − 6(8)) − 2(4(10) − 6(7)) + 3(4(8) − 5(7)) "
            "= 1(2) − 2(−2) + 3(−3) = −3, so the volume is 3.",
            "Compute the determinant of the 3 by 3 matrix of the vectors.", "C"),
           ("8.3.6", "Write a complete solution to proving that the determinant of a product "
            "equals the product of the determinants, for 2 by 2 matrices.",
            "Expanding (ae + bg)(cf + dh) − (af + bh)(ce + dg) and simplifying gives "
            "(ad − bc)(eh − fg).",
            "Expand both sides and compare.", "C"),
           ("8.3.7", "Write a complete solution to finding the area of the triangle with "
            "vertices (1, 1), (6, 2) and (3, 7).",
            "The side vectors are (5, 1) and (2, 6), with determinant 5(6) − 1(2) = 28, so "
            "the area is 14.", "Halve the determinant of the two side vectors.", "R"),
           ("8.3.8", "Write a complete solution to finding the image of (5, −2) "
            "under [[1, 2], [-1, 3]] and the determinant of the matrix.",
            "The image is (5 − 4, −5 − 6) = (1, −11) and the determinant is "
            "3 + 2 = 5.",
            "Multiply, then compute ad − bc.", "R"),
           ("8.3.9", "Write a complete solution to showing that A(−1, 2), B(3, 5) "
            "and C(9, 11) are collinear.",
            "AB = (4, 3) and BC = (6, 6), which are not multiples, so the "
            "points are not collinear; the test is whether one vector is a "
            "multiple of the other.",
            "Compare the two vectors component by component.", "R"),
           ("8.3.10", "Write a complete solution to finding the point dividing AB in "
            "the ratio 1 : 4 where A = (2, 7) and B = (18, −3).",
            "The point is (4a + b)/5 = ((8 + 18)/5, (28 − 3)/5) = (5.2, 5).",
            "Apply the section formula with the weights crossed.", "R"),
           ("8.3.11", "Write a complete solution to finding the vector product of (3, "
            "−2, 1) and (1, 4, −2), and verifying it is perpendicular to "
            "both.",
            "a × b = ((−2)(−2) − 1(4), 1(1) − 3(−2), 3(4) − (−2)(1)) = (0, "
            "7, 14); both scalar products are 0.",
            "Apply the component formula, then check with scalar products.", "C"),
           ("8.3.12", "Write a complete solution to finding the area of the triangle "
            "with vertices (1, 2), (5, 3) and (2, 7).",
            "The side vectors are (4, 1) and (1, 5), with determinant 4(5) "
            "− 1(1) = 19, so the area is 9.5.",
            "Halve the determinant of the two side vectors.", "R"),
           ],
        D=[("8.4.1", "A drone's displacement is modelled by the vector 3a + 2b where a = "
            "(40, 30) metres and b = (−20, 50). Find the displacement and its distance from "
            "the start.",
            "3a + 2b = (120 − 40, 90 + 100) = (80, 190), a distance of √(6400 + 36100) ≈ "
            "206.2 m.", "Scale and add component-wise, then use Pythagoras.", "A"),
           ("8.4.2", "A force of (3, 4) newtons acts on a body that moves through the "
            "displacement (5, 0) metres. Find the work done.",
            "The work is the scalar product 3(5) + 4(0) = 15 joules.",
            "Work is the scalar product of force and displacement.", "A"),
           ("8.4.3", "A graphics program applies the matrix [[0, −1], [1, 0]] to a shape. "
            "Describe the transformation and find the image of the point (2, 5).",
            "It is a rotation through 90°, and the image is (−5, 2).",
            "Recognise the rotation matrix and multiply.", "A"),
           ("8.4.4", "A bridge support is modelled by two vectors (4, 0, 3) and (0, 5, 12). "
            "Find the angle between them and the area of the parallelogram they span.",
            "The scalar product is 36, the magnitudes are 5 and 13, so the cosine is 36/65 "
            "and the angle is about 56.4°; the area is |a × b| = √((5(12) − 3(0))² + "
            "(3(0) − 4(12))² + (4(5) − 0(0))²) = √(60² + 48² + 20²) ≈ 78.1.",
            "Use the scalar product for the angle and the vector product for the area.", "A"),
           ("8.4.5", "A machine part is transformed by [[1, 0], [0, −1]] and then by "
            "[[−1, 0], [0, 1]]. Find the combined matrix and describe the single "
            "transformation.",
            "The product is [[−1, 0], [0, −1]], a rotation through 180°.",
            "Multiply in the order of application and interpret the result.", "A"),
           ("8.4.6", "A student applies the matrix [[2, 0], [0, 2]] to a triangle of area 7. "
            "Find the area of the image and explain the calculation.",
            "The determinant is 4, so the area is 28.",
            "Areas are multiplied by the absolute value of the determinant.", "A"),
           ("8.4.7", "A navigation system stores positions as vectors and applies a "
            "correction matrix. Explain how a zero determinant would affect the system.",
            "It would collapse positions onto a line, so different positions would share one "
            "corrected position and the correction could not be undone.",
            "A zero determinant means no inverse and a collapsed image.", "R"),
           ("8.4.8", "A parallelogram has diagonals with vectors (6, 2) and (2, 6). Find its "
            "area.",
            "The area is half the magnitude of the determinant of the diagonals: "
            "|6(6) − 2(2)| ÷ 2 = 16.",
            "The area of a parallelogram is half the determinant of its diagonals.", "A"),
           ("8.4.9", "A transformation has matrix [[3, 1], [5, 2]]. A student claims it "
            "cannot be a rotation. Investigate and justify.",
            "Correct: the determinant is 6 − 5 = 1, but the columns (3, 5) and (1, 2) have "
            "magnitudes √34 and √5, not 1, so the columns are not unit vectors and the "
            "transformation is not a rotation.",
            "A rotation has perpendicular unit columns.", "R"),
           ("8.4.10", "A crane's arm is modelled by the vector 8(cos 35°, sin 35°) and its "
            "counterweight by −5(cos 35°, sin 35°). Find the resultant and its magnitude.",
            "The resultant is 3(cos 35°, sin 35°) ≈ (2.46, 1.72), of magnitude 3.",
            "The vectors are parallel, so they combine by subtraction of magnitudes.", "A"),
           ("8.4.11", "A school's coordinate grid is transformed by [[1, 2], [3, 4]]. Find "
            "the image of the unit square, its area, and whether the transformation can be "
            "undone.",
            "The images of the vertices are (0, 0), (1, 3), (5, 7) and (4, 4); the area is "
            "|1(4) − 2(3)| = 2, and since the determinant is −2 the transformation can be "
            "undone.",
            "Map the vertices and compute the determinant.", "A"),
           ("8.4.12", "A student computes the vector product of two vectors in two "
            "dimensions and gets a number. Investigate and justify.",
            "In two dimensions the analogue is the determinant, which is a number giving the "
            "signed area; the vector product as a vector exists only in three dimensions.",
            "Distinguish the two-dimensional determinant from the three-dimensional vector "
            "product.", "R")],
    ),
    assessment=[
        dict(title="A1 · The graphic transformation",
             text="A graphics program applies the matrix [[1, 1], [−1, 1]] to a shape and "
                  "then the matrix [[2, 0], [0, 0.5]]. Describe each transformation, find "
                  "the combined matrix, find its determinant, and say whether the combined "
                  "transformation can be undone. If it can, find the inverse matrix.",
             note="Criteria C and D · describe each transformation, combine the matrices in "
                  "order, and justify the existence of the inverse."),
        dict(title="A2 · The survey vectors",
             text="A surveyor records two displacements a = (120, −50) metres and "
                  "b = (−80, 140) metres. Find the resultant, its magnitude and bearing, the "
                  "angle between the two displacements, and the area of the parallelogram "
                  "they span. Then find a unit vector in the direction of the resultant.",
             note="Criteria C and D · combine the vectors, use the scalar product for the "
                  "angle and the determinant for the area."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of form and the related concepts of space, representation "
        "and systems appear in your work?",
        "How is the global context of scientific and technical innovation, and its "
        "exploration of computer graphics, navigation and engineering, visible in the "
        "investigations and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of a matrix as a description of a transformation, and what "
        "would you still like to ask?",
    ],
    review=dict(
        ideas=["A vector has magnitude and direction and combines component-wise.",
               "The magnitude of (x, y) is √(x² + y²).",
               "The scalar product a · b = |a||b| cos θ is zero exactly for perpendicular "
               "vectors.",
               "The columns of a matrix are the images of the basis vectors.",
               "Composition of transformations is matrix multiplication in the order of "
               "application.",
               "The determinant ad − bc is the signed area scale factor.",
               "A negative determinant reverses orientation; a zero determinant collapses "
               "the plane.",
               "The inverse exists exactly when the determinant is non-zero.",
               "det(AB) = det(A) det(B).",
               "The vector product gives a vector perpendicular to both factors, with "
               "magnitude equal to the area they span."],
        vocab=["vector", "magnitude", "direction", "position vector", "scalar product",
               "unit vector", "column vector", "matrix", "transformation", "determinant",
               "inverse matrix", "identity matrix", "adj ugate", "vector product", "scalar "
               "triple product", "coplanar", "shear", "orientation"],
        mixed=[("8.R1", "Given a = (5, −2) and b = (1, 4), find 2a + b and |a + b|."),
               ("8.R2", "Find the determinant of [[3, −1], [7, 2]] and its inverse."),
               ("8.R3", "Write the matrix for a reflection in the y-axis."),
               ("8.R4", "Find the area of the triangle with vertices (0, 0), (3, 1) and "
                "(1, 4)."),
               ("8.R5", "Given a = (1, 2, 3) and b = (4, 5, 6), find a × b."),
               ("8.R6", "Explain what a determinant of zero means geometrically.")],
    ),
    projects=dict(
        service=[("Community need", "Local mapping and measurement is done without any "
                                    "record of the transformations used."),
                 ("Mathematical connection", "Vectors and matrices."),
                 ("Proposed action", "Take one local map or plan, express two displacements "
                                     "as vectors, and publish the method with the "
                                     "determinant of the transformation used."),
                 ("Expected impact", "The plan can be checked and reproduced by anyone."),
                 ("Student reflection", "Record the vectors, the matrices and the "
                                        "determinants you computed.")],
        community=[("Project idea", "A vector audit of the school's site plan."),
                   ("Need", "The plan is used for events without any record of its scale or "
                            "orientation."),
                   ("Research question", "What transformation converts the plan's "
                                         "coordinates into metres on the ground?"),
                   ("Mathematics", "Vectors, matrices and determinants."),
                   ("Action or outcome", "A one-page conversion with the matrix shown."),
                   ("Beneficiaries", "Everyone who uses the school site plan."),
                   ("Evidence", "The conversion and the matrix behind it.")],
        personal=[("Personal interest", "Computer graphics, gaming, robotics or sport."),
                  ("Learning goal", "To describe a transformation you use as a matrix and "
                                    "state what its determinant means."),
                  ("Product or outcome", "A transformation card with a matrix and a "
                                         "determinant."),
                  ("Mathematics", "Vectors, matrices and determinants."),
                  ("Process", "Choose a transformation, write its matrix, and compute its "
                              "determinant."),
                  ("Evidence", "The card and the determinant you computed.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=9, title="Statistics: Dispersion, Correlation and Regression",
    key="Relationships", related=["Patterns", "Representation", "Measurement"],
    context="Identities and relationships",
    exploration="how groups differ, and how claims about them are made",
    inquiry=("Two groups can share a centre and differ in every other respect; measuring "
             "dispersion and association describes those differences precisely, while the "
             "origin of the data limits what the description can prove."),
    atl=("Critical thinking",
         "In order for a student to judge a claim made about two groups, students must "
         "compare a measure of centre with a measure of dispersion, consider the origin of "
         "the data, and justify what the comparison can and cannot show."),
    standfirst="A single average describes a group's centre and nothing else. Dispersion "
               "describes how the group is spread, and association describes how two "
               "variables move together, and neither can say more than the data allows.",
    engage="Two classes have the same mean test score. One class has every student within "
           "two marks of the mean; the other has scores from the lowest to the highest "
           "possible. Are the two classes equally well taught, and what would you need to "
           "know to decide?",
    questions=[("Factual", "What do the range, the interquartile range, the variance and the "
                           "standard deviation measure?"),
               ("Conceptual", "Why can two data sets share a mean and differ completely, and "
                              "what does a correlation coefficient measure?"),
               ("Debatable", "If a correlation is strong, is a causal claim justified?")],
    application_lede="These tasks use measures of dispersion, correlation and regression. "
                     "State which measure you use and why, give the formula you apply, and "
                     "comment on what the data can support.",
    projects_lede="A statistic describes a sample, not the world. Name the sample, the "
                  "measure and the claim, and say what the claim cannot reach.",
    sections=[
        dict(id="9.1", title="Measuring spread",
             inquiry_q="Why is a single average not enough to describe a group?",
             teach=[
                 "The range is the difference between the largest and smallest values, and it is sensitive to every extreme value. It is quick to compute and quick to mislead, because one unusual observation can change it completely.",
                 "The interquartile range is the difference between the upper and lower quartiles, and it describes the middle half of the data. It is resistant to outliers, which is why it is preferred when the data contain extreme values.",
                 "The variance is the mean of the squared deviations from the mean, and the standard deviation is its square root. The standard deviation is in the same units as the data, which is what makes it interpretable.",
                 "There are two conventions for variance: the population variance divides by n and the sample variance divides by n − 1. The sample version is unbiased for estimating the population variance, and the convention in use must always be stated.",
             ], examples=[
                 dict(q="Find the range, the interquartile range and the standard deviation "
                        "of the data 4, 7, 8, 9, 11, 13, 16.",
                      vis=F("table", [["step", "working", "result"],
                                      ["mean", "(4 + 7 + 8 + 9 + 11 + 13 + 16)/7", "9.714"],
                                      ["range", "16 − 4", "12"],
                                      ["quartiles", "Q1 = 7.5, Q3 = 12.5", "—"],
                                      ["interquartile range", "12.5 − 7.5", "5"]],
                            caption="The interquartile range is half the range here."),
                      reasoning="Compute the mean, then the range, the quartiles and the "
                               "deviations.",
                      steps=["The mean is (4 + 7 + 8 + 9 + 11 + 13 + 16)/7 = 68/7 ≈ 9.714.",
                             "The range is 16 − 4 = 12.",
                             "The lower quartile is 7.5 and the upper quartile is 12.5, so "
                             "the interquartile range is 5.",
                             "The squared deviations sum to 82.857, so the population "
                             "variance is 82.857/7 ≈ 11.837.",
                             "The population standard deviation is √11.837 ≈ 3.44, and the "
                             "sample standard deviation is √(82.857/6) ≈ 3.72."],
                      ans="range 12, interquartile range 5, population standard deviation "
                          "about 3.44",
                      interp="The interquartile range is much smaller than the range because "
                             "the extremes are excluded, which is exactly its purpose."),
                 dict(q="Two data sets both have mean 50. Set A has standard deviation 2 "
                        "and set B has standard deviation 12. Explain what this means for "
                        "the two groups.",
                      vis=F("table", [["set", "mean", "standard deviation", "typical "
                                      "distance from the mean"],
                                      ["A", "50", "2", "about 2 units"],
                                      ["B", "50", "12", "about 12 units"],
                                      ["difference", "0", "10", "—"]],
                            caption="The centres agree and the spreads differ."),
                      reasoning="Compare the standard deviations while noting the equal means.",
                      steps=["Both sets have the same mean of 50, so their centres agree.",
                             "Set A has a standard deviation of 2, so most of its values lie "
                             "close to 50.",
                             "Set B has a standard deviation of 12, so its values are "
                             "typically 12 units from the mean.",
                             "The two groups therefore differ completely even though their "
                             "means are identical.",
                             "A report giving only the means would hide the difference "
                             "entirely."],
                      ans="the means agree but the spreads differ by a factor of 6",
                      interp="This is the case the inquiry statement describes: a shared "
                             "centre with a complete difference in every other respect."),
             ], inv=dict(
                 task="Take six data sets of your own, each with the same mean of 10: one "
                      "with no spread at all, one with a small spread, one with a large "
                      "spread, one with one extreme outlier, one with two clusters, and one "
                      "symmetric. Compute the range, the interquartile range and the "
                      "standard deviation of each, and record which measure best captures "
                      "the difference.",
                 table=[["data set", "range", "interquartile range", "standard deviation",
                                "best description"],
                        ["all 10s", "0", "0", "0", "no spread"],
                        ["9, 10, 11", "2", "1", "0.82", "small spread"],
                        ["1, 5, 10, 15, 19", "18", "10", "6.85", "large spread"],
                        ["10, 10, 10, 10, 40", "30", "0", "13.42", "one outlier"],
                        ["1, 2, 9, 18, 19", "18", "16", "8.20", "two clusters"],
                        ["6, 8, 10, 12, 14", "8", "6", "2.83", "symmetric"]],
                 notice=["The data set with an outlier had a huge range but a zero "
                         "interquartile range.",
                         "The two-cluster set had a large interquartile range but a "
                         "standard deviation similar to the wide set.",
                         "The set with no spread had every measure equal to zero.",
                         "No single measure described all six sets adequately, which is why "
                         "more than one is reported."],
                 obs="Different measures of spread respond to different features of a data "
                     "set, and an outlier distorts the range and the standard deviation but "
                     "not the interquartile range.",
                 concl="A single average describes a centre and nothing else, so a measure of "
                       "dispersion is needed alongside it. The range is sensitive to "
                       "extremes, the interquartile range is resistant to them, and the "
                       "standard deviation uses every value in the same units as the data. "
                       "Here the outlier set had range 30 with interquartile range 0.")),
        dict(id="9.2", title="Standard deviation and grouped data",
             inquiry_q="How is dispersion computed when the data are grouped?",
             teach=[
                 "For grouped data with frequencies, the mean is the sum of each value times its frequency divided by the total frequency. The standard deviation is computed from the same table, using the squared deviations.",
                 "The coding shortcut replaces each value x by (x − a)/h for a convenient a and class width h, computes the standard deviation of the coded values, and multiplies by h. The shift does not affect the spread, and the scale multiplies it.",
                 "For a frequency table, the variance is (sum of f x²)/(sum of f) − mean². This form is faster than summing squared deviations and is the one used in practice.",
                 "When data are grouped into classes, the mid-point of each class represents every value in it. This introduces a within-class error that the standard deviation cannot detect, and it is stated as a limitation of the calculation.",
             ], examples=[
                 dict(q="Find the mean and standard deviation of the data summarised by "
                        "x = 2, 4, 6, 8 with frequencies 3, 5, 2, 1.",
                      vis=F("table", [["x", "f", "fx", "fx²"],
                                      ["2", "3", "6", "12"],
                                      ["4", "5", "20", "80"],
                                      ["6", "2", "12", "72"],
                                      ["8", "1", "8", "64"]],
                            caption="The frequency table carries all the information."),
                      reasoning="Use the frequency-table formula for the mean and the "
                               "variance.",
                      steps=["The total frequency is 3 + 5 + 2 + 1 = 11.",
                             "The sum of f x is 6 + 20 + 12 + 8 = 46, so the mean is 46/11 "
                             "≈ 4.18.",
                             "The sum of f x² is 12 + 80 + 72 + 64 = 228.",
                             "The variance is 228/11 − (46/11)² ≈ 20.73 − 17.50 ≈ 3.23.",
                             "The standard deviation is √3.23 ≈ 1.80."],
                      ans="mean about 4.18, standard deviation about 1.80",
                      interp="The frequency table formula is the same calculation written in "
                             "a form that avoids listing every observation."),
                 dict(q="The heights of 40 plants are grouped into classes 10–14, 15–19, "
                        "20–24, 25–29 with frequencies 4, 12, 16, 8. Estimate the mean and "
                        "standard deviation.",
                      vis=F("table", [["class", "mid-point", "f", "f × mid-point"],
                                      ["10–14", "12", "4", "48"],
                                      ["15–19", "17", "12", "204"],
                                      ["20–24", "22", "16", "352"],
                                      ["25–29", "27", "8", "216"]],
                            caption="Class mid-points stand in for the individual values."),
                      reasoning="Use the mid-points as representative values and apply the "
                               "frequency formula.",
                      steps=["The mid-points are 12, 17, 22 and 27.",
                             "The total frequency is 40 and the sum of f times mid-point is "
                             "48 + 204 + 352 + 216 = 820.",
                             "So the estimated mean is 820/40 = 20.5.",
                             "The sum of f times mid-point squared is 4(144) + 12(289) + "
                             "16(484) + 8(729) = 576 + 3468 + 7744 + 5832 = 17 620.",
                             "The variance is 17 620/40 − 20.5² = 440.5 − 420.25 = 20.25, so "
                             "the standard deviation is 4.5."],
                      ans="estimated mean 20.5, estimated standard deviation 4.5",
                      interp="The mid-point assumption is an estimate, and the true standard "
                             "deviation within each class is hidden by it."),
             ], inv=dict(
                 task="Take a data set of your own with at least 20 values, group it into "
                      "classes of equal width, and compute the mean and standard deviation "
                      "from the grouped table. Then compute them from the raw values and "
                      "compare, explaining any difference.",
                 table=[["method", "mean", "standard deviation", "difference in the mean"],
                        ["raw values", "31.4", "5.62", "—"],
                        ["grouped, width 10", "31.0", "5.48", "0.4"],
                        ["grouped, width 5", "31.3", "5.58", "0.1"],
                        ["grouped, width 20", "30.0", "5.90", "1.4"]],
                 notice=["The narrower the classes, the closer the grouped answers were to "
                         "the raw answers.",
                         "The widest classes gave the largest errors in both measures.",
                         "The mean was always slightly affected by the mid-point assumption.",
                         "The standard deviation was affected less, because within-class "
                         "variation partly cancels."],
                 obs="Grouping replaces each value by its class mid-point, and the error "
                     "shrinks as the classes narrow.",
                 concl="For grouped data the mid-point of each class stands in for every "
                       "value in it, and the mean and standard deviation are computed from "
                       "the frequency table with the formula variance = (sum of f x²)/(sum "
                       "of f) − mean². The mid-point assumption introduces an error that "
                       "narrows the classes reduce. Here the raw mean was 31.4 and the "
                       "grouped estimates were 31.0, 31.3 and 30.0.")),
        dict(id="9.3", title="Comparing distributions",
             inquiry_q="How are two distributions compared fairly?",
             teach=[
                 "Two distributions are compared by a measure of centre, a measure of dispersion, and a statement of the shape. Reporting only the means is the commonest statistical error, and it hides exactly the difference the inquiry statement describes.",
                 "A box plot displays the minimum, the lower quartile, the median, the upper quartile and the maximum, so it shows centre, spread and shape at once, and it is a representation of a whole distribution in five numbers. Comparing two box plots side by side is the standard visual comparison.",
                 "The shape of a distribution is described as symmetric, skewed to the left or skewed to the right. When a distribution is skewed, the median is a better measure of centre than the mean, because the mean is pulled towards the tail.",
                 "A comparison must state the sample sizes and the origin of the data, because a difference between two small samples may not be a difference between the populations they came from.",
             ], examples=[
                 dict(q="Two groups of seven values each are recorded. Group A has mean 50 "
                        "and standard deviation 2; group B has mean 50 and standard "
                        "deviation 12. Write a comparison of the two groups.",
                      vis=F("table", [["measure", "group A", "group B", "comparison"],
                                      ["mean", "50", "50", "the same"],
                                      ["standard deviation", "2", "12", "B is 6 times as "
                                       "spread"],
                                      ["interquartile range", "3", "18", "B is 6 times as "
                                       "wide"],
                                      ["shape", "tight cluster", "wide spread", "very "
                                       "different"]],
                            caption="The centres agree and every other measure differs."),
                      reasoning="Compare centre, dispersion and shape in turn.",
                      steps=["Both groups have the same mean of 50, so their centres agree.",
                             "Group A has a standard deviation of 2 and group B of 12, so "
                             "group B is six times as spread.",
                             "The interquartile ranges tell the same story: 3 against 18.",
                             "The shapes differ too, with group A tightly clustered and group "
                             "B widely spread.",
                             "So the two groups are completely different despite an identical "
                             "mean, and any report giving only the mean would be "
                             "misleading."],
                      ans="the means agree; group B is six times as dispersed as group A",
                      interp="The comparison names all three aspects, and it states what the "
                             "shared mean hides."),
                 dict(q="A distribution has mean 40, median 34 and mode 28. Describe its "
                        "shape and say which measure of centre to report.",
                      vis=F("table", [["measure", "value", "position"],
                                      ["mode", "28", "lowest"],
                                      ["median", "34", "middle"],
                                      ["mean", "40", "highest"],
                                      ["conclusion", "mean > median > mode", "skewed "
                                       "right"]],
                            caption="A long right tail pulls the mean up."),
                      reasoning="Compare the three measures and use their order to identify "
                               "the skew.",
                      steps=["The three measures are 28, 34 and 40.",
                             "The mean is the largest, so the distribution is skewed to the "
                             "right.",
                             "A right skew means a long tail of large values pulling the "
                             "mean upwards.",
                             "The median is the better measure of centre here, because it is "
                             "not affected by the tail.",
                             "So the report should give the median, 34, with a note that the "
                             "distribution is skewed."],
                      ans="skewed to the right; report the median, 34",
                      interp="The order of the three measures diagnoses the skew, and the "
                             "skew decides which measure to report."),
             ], inv=dict(
                 task="Collect two data sets of your own from different sources — for "
                      "example reaction times and test scores. Compute the mean, median, "
                      "standard deviation and interquartile range of each, draw box plots of "
                      "both, and write a comparison that states what the comparison can and "
                      "cannot show.",
                 table=[["measure", "data set 1", "data set 2", "comparison"],
                        ["mean", "0.42 s", "62.4 marks", "different units"],
                        ["median", "0.40 s", "58 marks", "different units"],
                        ["standard deviation", "0.09 s", "14.2 marks", "data set 2 is more "
                         "spread relative to its mean"],
                        ["interquartile range", "0.12 s", "21 marks", "same conclusion"],
                        ["shape", "roughly symmetric", "skewed right", "median better for "
                         "set 2"]],
                 notice=["The two sets had different units, so their standard deviations "
                         "could not be compared directly.",
                         "Comparing each standard deviation with its own mean showed that "
                         "the second set was more spread relative to its centre.",
                         "The first set was roughly symmetric, so the mean and median were "
                         "close.",
                         "The second set was skewed right, so its mean exceeded its median."],
                 obs="A fair comparison uses centre, dispersion and shape together, and "
                     "notes the units.",
                 concl="Two distributions are compared by a measure of centre, a measure of "
                       "dispersion and a statement of shape, and the sample sizes and the "
                       "origin of the data limit what the comparison can show. Where the "
                       "distributions are skewed, the median is the better centre. Here the "
                       "second set was more spread relative to its mean and skewed to the "
                       "right.")),
        dict(id="9.4", title="Scatter graphs and correlation",
             inquiry_q="What does a correlation coefficient measure, and what does it not?",
             teach=[
                 "A scatter graph plots one variable against another, and its overall patterns are described by direction, strength and shape. A straight-line pattern suggests linear correlation; a curved pattern suggests a non-linear relationship, and the eye reads the patterns before any number is computed.",
                 "The product-moment correlation coefficient r lies between −1 and 1. Values near 1 indicate strong positive linear correlation, values near −1 strong negative linear correlation, and values near 0 little or no linear correlation, so the number summarises the pattern of the scatter.",
                 "The coefficient is computed from the covariance of the two variables divided by the product of their standard deviations, which is why it is unaffected by the units of measurement, and it is a representation of the pattern in a single number. Changing metres to centimetres does not change r.",
                 "Correlation is not causation. Two variables may be correlated because one causes the other, because both are caused by a third, or by coincidence, and the data alone cannot distinguish these cases.",
             ], examples=[
                 dict(q="Compute the correlation coefficient for the paired data "
                        "(1, 2), (2, 4), (3, 5), (4, 4), (5, 6).",
                      vis=F("table", [["x", "y", "xy", "x²", "y²"],
                                      ["1", "2", "2", "1", "4"],
                                      ["2", "4", "8", "4", "16"],
                                      ["3", "5", "15", "9", "25"],
                                      ["4", "4", "16", "16", "16"],
                                      ["5", "6", "30", "25", "36"]],
                            caption="The sums feed the correlation formula."),
                      reasoning="Compute the summary sums and substitute into the formula.",
                      steps=["The means are x̄ = 3 and ȳ = 4.2.",
                             "The sum of x y is 2 + 8 + 15 + 16 + 30 = 71.",
                             "The sum of x² is 55 and the sum of y² is 97.",
                             "The correlation is (5 × 71 − 15 × 21) ÷ √((5 × 55 − 225)(5 × "
                             "97 − 441)) = 80 ÷ √(50 × 44) ≈ 0.855.",
                             "So r ≈ 0.855, indicating strong positive linear correlation."],
                      ans="r ≈ 0.855",
                      interp="The coefficient is dimensionless, so it is unaffected by a "
                             "change of units in either variable."),
                 dict(q="Explain why a correlation of 0.93 between ice-cream sales and "
                        "drowning deaths does not show that ice cream causes drowning.",
                      vis=F("table", [["explanation", "status"],
                                      ["ice cream causes drowning", "not supported"],
                                      ["a third variable, temperature, causes both",
                                       "plausible"],
                                      ["coincidence", "possible but unlikely at r = 0.93"],
                                      ["conclusion", "correlation is not causation", "—"]],
                            caption="A hidden common cause explains the correlation."),
                      reasoning="Consider the possible explanations for a correlation and "
                               "identify the plausible one.",
                      steps=["A correlation of 0.93 is strong, so the two variables really "
                             "do move together.",
                             "But correlation measures association, not causation.",
                             "Both ice-cream sales and drowning deaths rise in hot weather, "
                             "so temperature is a common cause.",
                             "Once temperature is accounted for, the association between "
                             "the other two largely disappears.",
                             "So the data support a claim of association only, and any "
                             "causal claim needs further evidence."],
                      ans="temperature is a common cause; correlation is not causation",
                      interp="The origin of the data limits what the correlation can show, "
                             "which is the second half of the inquiry statement."),
             ], inv=dict(
                 task="Collect ten paired observations of your own on two variables you "
                      "suspect are related. Draw a scatter graph, compute the correlation "
                      "coefficient, and then write a paragraph on whether the correlation "
                      "supports a causal claim, giving at least one alternative "
                      "explanation.",
                 table=[["step", "working", "result"],
                        ["scatter graph", "plotted", "roughly linear, positive"],
                        ["means", "x̄ = 12.4, ȳ = 5.6", "—"],
                        ["sums", "sum xy = 742, sum x² = 1660, sum y² = 356", "—"],
                        ["r", "(10 × 742 − 124 × 56) ÷ √((10 × 1660 − 15 376)(10 × 356 − "
                         "3136))", "0.78"],
                        ["causal claim", "not supported without more evidence", "—"]],
                 notice=["The scatter graph was roughly linear and sloped upwards.",
                         "The correlation coefficient was 0.78, indicating a strong positive "
                         "linear association.",
                         "A third variable, time of day, could plausibly explain both.",
                         "The data supported a claim of association only."],
                 obs="A strong correlation establishes association, not causation, and an "
                     "alternative explanation is always available.",
                 concl="The correlation coefficient r measures the strength of a linear "
                       "association and lies between −1 and 1, and it is unchanged by a "
                       "change of units. It says nothing about causation: a common cause, a "
                       "reverse cause or coincidence can all produce a strong r. Here r was "
                       "0.78 and the causal claim was not supported.")),
        dict(id="9.5", title="Regression and prediction",
             inquiry_q="How is a line of best fit used, and what are its limits?",
             teach=[
                 "The regression line of y on x is the line that minimises the sum of the squared vertical distances from the points to the line. It is written y = a + bx, and it is the line used to predict y from x.",
                 "The gradient is b = covariance ÷ variance of x, and the intercept is a = ȳ − b x̄. Both are computed from the same summary sums as the correlation coefficient, and r is the normalised version of b.",
                 "Interpolation is prediction within the range of the data, and it is usually reliable. Extrapolation is prediction beyond that range, and it assumes the relationship continues, which is an assumption and not a fact.",
                 "The regression line of x on y is a different line from the regression line of y on x, unless the correlation is exactly ±1. The two lines answer different questions, and using the wrong one gives a wrong prediction.",
             ], examples=[
                 dict(q="Find the regression line of y on x for the data (1, 2), (2, 4), "
                        "(3, 5), (4, 4), (5, 6), and predict y when x = 6.",
                      vis=F("table", [["step", "working", "result"],
                                      ["means", "x̄ = 3, ȳ = 4.2", "—"],
                                      ["gradient", "(5 × 71 − 15 × 21) ÷ (5 × 55 − 225)",
                                       "80/50 = 1.6"],
                                      ["intercept", "4.2 − 1.6 × 3", "−0.6"],
                                      ["line", "y = 1.6x − 0.6", "—"],
                                      ["prediction", "y at x = 6", "9.0"]],
                            caption="The gradient and intercept come from the same sums as "
                                    "r."),
                      reasoning="Compute the summary sums, then the gradient and intercept.",
                      steps=["The means are x̄ = 3 and ȳ = 4.2.",
                             "The gradient is (5 × 71 − 15 × 21)/(5 × 55 − 225) = 80/50 = "
                             "1.6.",
                             "The intercept is ȳ − b x̄ = 4.2 − 1.6(3) = −0.6.",
                             "So the line is y = 1.6x − 0.6.",
                             "At x = 6 the prediction is y = 9.0, which is an extrapolation "
                             "beyond the data and so less reliable."],
                      ans="y = 1.6x − 0.6; prediction 9.0 at x = 6",
                      interp="The prediction is labelled as extrapolation, and the "
                             "assumption it makes is stated."),
                 dict(q="A student uses the regression line of x on y to predict y from x. "
                        "Explain the error.",
                      vis=F("table", [["line", "minimises", "used to predict"],
                                      ["y on x", "vertical distances", "y from x"],
                                      ["x on y", "horizontal distances", "x from y"],
                                      ["when they differ", "whenever |r| < 1", "—"]],
                            caption="The two regression lines are different."),
                      reasoning="Identify which distances each line minimises and which "
                               "prediction it supports.",
                      steps=["The line of y on x minimises the vertical distances, so it is "
                             "the line for predicting y from x.",
                             "The line of x on y minimises the horizontal distances, so it "
                             "is the line for predicting x from y.",
                             "The two lines coincide only when |r| = 1, that is when the "
                             "points lie exactly on a line.",
                             "In general they are different, and using the wrong one gives a "
                             "biased prediction.",
                             "So the student must use the line of y on x."],
                      ans="the wrong line was used; the line of y on x is required",
                      interp="Naming which variable is being predicted is the first step in "
                             "any regression question."),
             ], inv=dict(
                 task="Take ten paired observations of your own, compute the regression "
                      "line of y on x, and use it to predict y at a value of x inside the "
                      "data range and one outside. Then compute the line of x on y and "
                      "compare the two lines, and comment on the reliability of each "
                      "prediction.",
                 table=[["task", "working", "result"],
                        ["regression of y on x", "y = 0.78x + 1.4", "—"],
                        ["interpolation at x = 10", "y = 9.2", "within the range"],
                        ["extrapolation at x = 25", "y = 20.9", "outside the range"],
                        ["regression of x on y", "x = 0.61y + 3.2", "a different line"],
                        ["comparison", "the two gradients differ", "0.78 against 1/0.61"]],
                 notice=["The two regression lines were different, as expected with "
                         "|r| < 1.",
                         "The interpolation gave a value inside the observed range.",
                         "The extrapolation gave a value far outside it, and assumed the "
                         "relationship continued.",
                         "The two gradients were not reciprocals, because the lines "
                         "minimise different distances."],
                 obs="The regression line of y on x predicts y from x, and extrapolation "
                     "assumes the relationship continues beyond the data.",
                 concl="The regression line of y on x minimises the vertical distances and "
                       "predicts y from x, and it is computed from the same summary sums as "
                       "the correlation coefficient. Interpolation within the range of the "
                       "data is reliable; extrapolation beyond it assumes the relationship "
                       "continues. The line of x on y is different whenever |r| < 1. Here "
                       "the two gradients were 0.78 and about 1.64.")),
        dict(id="9.6", title="Investigation: correlation, causation and reliability",
             inquiry_q="What limits a statistical description?",
             teach=[
                 "A statistical description describes the relationships within the sample that was measured, and it extends to a wider population only if the sample was representative. The origin of the data is therefore part of the result, not a footnote.",
                 "A correlation may arise from a common cause, from a reverse cause, or from coincidence. Distinguishing these requires an experiment or a controlled study, not a larger sample of the same kind.",
                 "The reliability of an estimate is described by a confidence interval, which is a range of values consistent with the data. A narrow interval means the estimate is precise; it says nothing about whether the estimate is unbiased.",
                 "An outlier can change a correlation coefficient substantially, because the coefficient is computed from sums of products. Reporting the coefficient with and without the outlier is a standard robustness check.",
             ], examples=[
                 dict(q="A data set of nine points gives r = 0.32, but adding a tenth point "
                        "changes r to 0.91. Investigate what has happened.",
                      vis=F("table", [["point", "x", "y", "effect on r"],
                                      ["original nine", "—", "—", "r = 0.32"],
                                      ["added point", "(30, 30)", "far from the cluster",
                                       "r = 0.91"],
                                      ["without it", "—", "—", "r = 0.32"],
                                      ["conclusion", "the tenth point is an influential "
                                       "outlier", "—"]],
                            caption="One point can dominate a correlation."),
                      reasoning="Compare the coefficient with and without the added point and "
                               "identify its role.",
                      steps=["With nine points the correlation is 0.32, indicating weak "
                             "linear association.",
                             "Adding the point (30, 30) raises the correlation to 0.91.",
                             "The added point is far from the cluster of the other nine, so "
                             "it pulls the line towards itself.",
                             "Such a point is called an influential outlier, and it changes "
                             "the coefficient without changing the other data.",
                             "The honest report gives both values and identifies the "
                             "outlier."],
                      ans="the tenth point is an influential outlier; report both values",
                      interp="The robustness check is reporting the coefficient with and "
                             "without the influential point."),
                 dict(q="A study of 1000 people finds a correlation of 0.6 between hours "
                        "of television watched and reading score. State what the study "
                        "shows and what it does not.",
                      vis=F("table", [["claim", "supported?", "reason"],
                                      ["television watching is associated with reading "
                                       "score", "yes", "r = 0.6 over 1000 people"],
                                      ["television causes lower reading scores", "no",
                                       "correlation is not causation"],
                                      ["the association holds for all age groups", "no",
                                       "the sample may not represent them"],
                                      ["a third variable explains both", "plausible",
                                       "for example socioeconomic status"]],
                            caption="Each claim needs its own justification."),
                      reasoning="Separate the claim the data support from the claims they do "
                               "not.",
                      steps=["The study shows an association, with r = 0.6 over 1000 "
                             "people.",
                             "The large sample makes the estimate of the association "
                             "reasonably precise.",
                             "It does not show causation, because correlation measures "
                             "association only.",
                             "It does not show the association holds for groups outside the "
                             "sample, unless the sample was representative of them.",
                             "A third variable, such as socioeconomic status, could explain "
                             "both."],
                      ans="an association is shown; causation and generalisation are not",
                      interp="The origin of the data limits the description, which is the "
                             "second half of the inquiry statement."),
             ], inv=dict(
                 task="Take a published correlation claim from a newspaper or a website. "
                      "Identify the variables, the sample, the correlation coefficient and "
                      "the causal claim, if any. Then write an evaluation stating what the "
                      "data support, what they do not, and at least one alternative "
                      "explanation.",
                 table=[["element", "found", "evaluation"],
                        ["variables", "hours of exercise and self-reported happiness",
                         "both self-reported, so both subject to bias"],
                        ["sample", "1500 adults in one country", "not representative of "
                         "other countries"],
                        ["coefficient", "r = 0.4", "moderate association"],
                        ["causal claim", "exercise makes people happier", "not supported by "
                         "correlation alone"],
                        ["alternative", "good health causes both", "plausible"]],
                 notice=["Both variables were self-reported, which introduced a common "
                         "measurement bias.",
                         "The sample came from one country, so the association might not "
                         "generalise.",
                         "The coefficient of 0.4 indicated a moderate association only.",
                         "The causal claim was not supported, and a common cause was "
                         "plausible."],
                 obs="The origin of the data limits the description, and a causal claim "
                     "needs more than a correlation.",
                 concl="A statistical description describes the sample measured and extends "
                       "to a wider population only if the sample was representative. A "
                       "correlation may arise from a common cause, a reverse cause or "
                       "coincidence, and distinguishing these needs an experiment rather "
                       "than a larger sample. Reporting the coefficient with and without "
                       "influential points is the standard robustness check.")),
        dict(id="9.7", title="Mixed practice",
             inquiry_q="Which measure, and what does it support?",
             teach=[
                 "Every statistics question begins by asking what is being described: a centre, a spread, an association or a prediction. The four need different measures, and using the wrong one is the commonest error.",
                 "When data are skewed, the median and the interquartile range are the appropriate measures, because they are resistant to extreme values. When data are symmetric, the mean and the standard deviation use more of the information.",
                 "A regression prediction must state whether it is interpolation or extrapolation, and an association must be reported as an association rather than a cause. Both statements are part of the answer.",
                 "Mixed practice is where the measure is chosen rather than given, so the reasoning behind the choice is part of what is being practised.",
             ], examples=[
                 dict(q="Find the mean and standard deviation of 12, 15, 18, 20, 23.",
                      vis=F("table", [["step", "working", "result"],
                                      ["mean", "88/5", "17.6"],
                                      ["deviations", "−5.6, −2.6, 0.4, 2.4, 5.4", "—"],
                                      ["squared sum", "31.36 + 6.76 + 0.16 + 5.76 + 29.16",
                                       "73.2"],
                                      ["variance", "73.2/5", "14.64"],
                                      ["standard deviation", "√14.64", "3.83"]],
                            caption="The mean is the reference for every deviation."),
                      reasoning="Compute the mean, then the squared deviations, then the "
                               "variance.",
                      steps=["The mean is (12 + 15 + 18 + 20 + 23)/5 = 88/5 = 17.6.",
                             "The deviations are −5.6, −2.6, 0.4, 2.4 and 5.4.",
                             "Their squares sum to 31.36 + 6.76 + 0.16 + 5.76 + 29.16 = "
                             "73.2.",
                             "The population variance is 73.2/5 = 14.64.",
                             "The standard deviation is √14.64 ≈ 3.83."],
                      ans="mean 17.6, standard deviation about 3.83",
                      interp="The sample standard deviation would divide by 4 instead of 5, "
                             "and the convention must be stated."),
                 dict(q="A line of best fit is y = 2.4x + 8. Predict y when x = 15 and "
                        "comment on the prediction if the data ranged from x = 5 to x = 12.",
                      vis=F("table", [["step", "working", "result"],
                                      ["prediction", "y = 2.4(15) + 8", "44"],
                                      ["data range", "5 to 12", "—"],
                                      ["type", "x = 15 is outside the range",
                                       "extrapolation"],
                                      ["assumption", "the linear relationship continues",
                                       "stated"]],
                            caption="Extrapolation assumes the relationship continues."),
                      reasoning="Substitute, then classify the prediction by comparing x "
                               "with the data range.",
                      steps=["The prediction is y = 2.4(15) + 8 = 44.",
                             "The data ranged from x = 5 to x = 12.",
                             "Since 15 is outside that range, the prediction is an "
                             "extrapolation.",
                             "Extrapolation assumes the linear relationship continues beyond "
                             "the observed data.",
                             "The prediction should therefore be reported with that "
                             "assumption stated."],
                      ans="44, an extrapolation assuming the relationship continues",
                      interp="The classification of the prediction is part of the answer, "
                             "not an optional remark."),
             ], inv=dict(
                 task="Take a data set of at least ten paired observations from a source "
                      "you choose. Compute the mean and standard deviation of each variable, "
                      "the correlation coefficient, and the regression line of y on x. Then "
                      "write an evaluation stating what the analysis supports, what it does "
                      "not, and one limitation of the data source.",
                 table=[["step", "working", "result"],
                        ["mean of x", "18.4", "—"],
                        ["standard deviation of x", "4.7", "—"],
                        ["mean of y", "52.1", "—"],
                        ["standard deviation of y", "11.3", "—"],
                        ["correlation", "r = 0.82", "strong positive linear association"],
                        ["regression line", "y = 1.97x + 15.8", "—"],
                        ["limitation", "the sample was self-selected", "the association may "
                         "not generalise"]],
                 notice=["The correlation was strong, at 0.82.",
                         "The regression line allowed predictions within the observed "
                         "range.",
                         "The sample was self-selected, so the association might not "
                         "generalise.",
                         "The analysis supported a claim of association only."],
                 obs="A complete statistical report gives the centre, the spread, the "
                     "association and the limitation together.",
                 concl="A statistics question is answered by choosing the measure that "
                       "matches what is being described: a centre, a dispersion, an "
                       "association or a prediction. Skewed data call for the median and "
                       "the interquartile range, and every association is reported as an "
                       "association rather than a cause. Here the correlation was 0.82 and "
                       "the regression line was y = 1.97x + 15.8.")),
    ],
    practice=dict(
        A=[("9.1.1", "Find the range of the data 3, 7, 8, 12, 12, 15, 20.",
            "20 − 3 = 17.", "The range is the largest minus the smallest.", "F"),
           ("9.1.2", "Find the mean of 4, 8, 8, 10, 15.",
            "45/5 = 9.", "Sum the values and divide by the count.", "F"),
           ("9.1.3", "Find the median of 4, 8, 8, 10, 15.",
            "8.", "The middle value of the ordered list.", "F"),
           ("9.1.4", "Find the population standard deviation of 2, 4, 4, 4, 5, 5, 7, 9.",
            "The mean is 5, the squared deviations sum to 32, so the variance is 4 and the "
            "standard deviation is 2.",
            "Divide the sum of squared deviations by n.", "F"),
           ("9.1.5", "Find the sample standard deviation of 2, 4, 4, 4, 5, 5, 7, 9.",
            "The sum of squared deviations is 32, so the variance is 32/7 ≈ 4.571 and the "
            "standard deviation is about 2.14.",
            "Divide by n − 1 for the sample version.", "R"),
           ("9.1.6", "A data set has mean 20 and standard deviation 3. A second has mean 20 "
            "and standard deviation 9. Compare them.",
            "The means agree; the second is three times as dispersed.",
            "Compare the measures of dispersion.", "R"),
           ("9.1.7", "Find the interquartile range of 5, 7, 8, 9, 11, 13, 16, 18.",
            "Q1 = 7.5 and Q3 = 14.5, so the interquartile range is 7.",
            "Take the difference of the quartiles.", "F"),
           ("9.1.8", "Find the mean and standard deviation of the frequency table x = 1, 2, "
            "3 with frequencies 4, 6, 2.",
            "Mean = (4 + 12 + 6)/12 = 22/12 ≈ 1.83; variance = (4 + 24 + 18)/12 − "
            "1.83² ≈ 3.833 − 3.361 ≈ 0.472, so the standard deviation is about 0.69.",
            "Use the frequency-table formulas.", "R"),
           ("9.1.9", "Compute the correlation coefficient for (1, 1), (2, 3), (3, 2), "
            "(4, 5), (5, 4).",
            "The means are 3 and 3, and r = (sum xy − n x̄ ȳ) ÷ √((sum x² − n x̄²)(sum y² − "
            "n ȳ²)) = (55 − 45) ÷ √((55 − 45)(55 − 45)) = 1.",
            "Use the summary-sum form of the formula.", "C"),
           ("9.1.10", "Explain what a correlation coefficient of −0.95 indicates.",
            "A very strong negative linear association: as one variable rises the other "
            "falls, almost exactly along a line.",
            "The sign gives the direction and the magnitude the strength.", "R"),
           ("9.1.11", "A regression line is y = 3.2x + 5. Predict y when x = 4.",
            "y = 17.8.", "Substitute into the line.", "F"),
           ("9.1.12", "Explain why the median is preferred to the mean for skewed data.",
            "Because the mean is pulled towards the long tail, while the median depends only "
            "on the middle of the ordered data and is resistant to extreme values.",
            "Consider the effect of a tail on each measure.", "R")],
        B=[("9.2.1", "Investigate the effect of adding a single extreme value to a data set "
            "on its range, interquartile range and standard deviation, and justify.",
            "The range and the standard deviation increase sharply, while the interquartile "
            "range is barely affected.",
            "Compute all three before and after the addition.", "R"),
           ("9.2.2", "Conjecture a rule for when the sample and population standard "
            "deviations are close, and justify.",
            "They are close when n is large, because the ratio √(n/(n − 1)) tends to 1.",
            "Compare the two divisors as n grows.", "R"),
           ("9.2.3", "Investigate the correlation coefficient for data that lie exactly on a "
            "curve, and justify the result.",
            "A curved relationship can give r near 0 even though the variables are closely "
            "related, because r measures linear association only.",
            "Plot the data and compute r.", "R"),
           ("9.2.4", "Take a data set of your own and show that multiplying every value by "
            "10 multiplies the standard deviation by 10 but leaves the correlation "
            "coefficient unchanged.",
            "The standard deviation scales with the data, while r is a ratio of "
            "standardised quantities and so is unchanged.",
            "Compute both before and after the scaling.", "R"),
           ("9.2.5", "Investigate the effect of an influential outlier on a regression "
            "line, and justify.",
            "The line rotates towards the outlier, changing both the gradient and the "
            "intercept, because the line minimises squared distances.",
            "Compute the line with and without the point.", "R"),
           ("9.2.6", "Conjecture a rule for the relationship between the two regression "
            "lines, and test it.",
            "The gradient of the line of x on y is r times the ratio of the standard "
            "deviations, and the two gradients multiply to r² only when the variables are "
            "standardised; in general the product of the gradients is r².",
            "Compute both gradients and compare with r².", "C"),
           ("9.2.7", "Investigate whether a correlation coefficient can exceed 1, and "
            "justify.",
            "No: r is a ratio of a covariance to a product of standard deviations, and the "
            "covariance is bounded by that product, so −1 ≤ r ≤ 1.",
            "Use the Cauchy–Schwarz inequality on the deviations.", "C"),
           ("9.2.8", "Investigate the effect of multiplying every value in a data "
            "set by 5 on its mean, range and standard deviation, and "
            "justify.",
            "The mean and the range are multiplied by 5, and the standard "
            "deviation is multiplied by 5, because every deviation is "
            "multiplied by 5.",
            "Track one value through the definitions.", "R"),
           ("9.2.9", "Conjecture a rule for when the mean and the median of a data "
            "set are close, and justify.",
            "They are close exactly when the distribution is approximately "
            "symmetric; a long tail on one side pulls the mean away from "
            "the median.",
            "Compare the two measures for symmetric and skewed examples.", "R"),
           ("9.2.10", "Investigate the correlation coefficient for data lying exactly "
            "on a line with negative gradient, and justify.",
            "r = −1 exactly, because every point lies on a straight line "
            "and the deviations are perfectly proportional.",
            "Compute r for points on a line of negative gradient.", "R"),
           ("9.2.11", "Investigate the effect of changing the units of one variable "
            "on the regression line of y on x, and justify.",
            "The gradient is divided by the conversion factor while the "
            "correlation coefficient is unchanged, because r is a ratio of "
            "standardised quantities.",
            "Convert the units, recompute the gradient, and compare with r.", "C"),
           ],
        C=[("9.3.1", "Write a complete solution to finding the mean, median and standard "
            "deviation of 14, 16, 16, 18, 21, 24, 28.",
            "Mean 19.57, median 18, population standard deviation about 4.63.",
            "Compute each measure and note which is resistant.", "R"),
           ("9.3.2", "Write a complete solution to comparing two data sets with the same "
            "mean but different spreads, stating what the comparison shows and what it does "
            "not.",
            "The means agree, so the centres match; the standard deviations differ, so the "
            "spreads differ; the comparison says nothing about why, because it describes "
            "the samples only.",
            "Compare centre, dispersion and shape, then state the limit.", "R"),
           ("9.3.3", "Write a complete solution to computing the correlation coefficient "
            "for (2, 5), (4, 7), (6, 6), (8, 10), (10, 11).",
            "The means are x̄ = 6 and ȳ = 7.8; sum xy = 264, sum x² = 220 and sum y² = 331, "
            "so r = (264 − 234) ÷ √((220 − 180)(331 − 304.2)) = 30 ÷ √1072 ≈ 0.92, "
            "indicating strong positive correlation.",
            "Compute the summary sums carefully before substituting.", "C"),
           ("9.3.4", "Write a complete solution to finding the regression line of y on x "
            "for the data in 9.3.3.",
            "The gradient is (sum xy − n x̄ ȳ)/(sum x² − n x̄²) ≈ 0.87 and the intercept is "
            "7.8 − 0.87(6) ≈ 2.6, so y ≈ 0.87x + 2.6.",
            "Use the same summary sums as for r.", "C"),
           ("9.3.5", "Write a complete solution to the grouped-data problem: classes 0–9, "
            "10–19, 20–29 with frequencies 5, 12, 8. Estimate the mean and standard "
            "deviation.",
            "Mid-points 4.5, 14.5, 24.5; mean = (22.5 + 174 + 196)/25 ≈ 15.7; variance = "
            "(101.25 + 2523 + 4802)/25 − 15.7² ≈ 297.05 − 246.49 ≈ 50.56, so the standard "
            "deviation is about 7.11.",
            "Use mid-points and the frequency formulas.", "R"),
           ("9.3.6", "Write a complete solution to evaluating a claim that a correlation of "
            "0.8 between two variables proves that one causes the other.",
            "It does not: a correlation measures association, and a common cause, a reverse "
            "cause or coincidence can all produce it. An experiment or controlled study is "
            "needed for a causal claim.",
            "Separate association from causation and name the alternatives.", "R"),
           ("9.3.7", "Write a complete solution to finding the area of a triangle with "
            "vertices (0, 0), (3, 1) and (1, 4) using a determinant.",
            "The side vectors are (3, 1) and (1, 4), with determinant 3(4) − 1(1) = 11, so "
            "the area is 5.5.",
            "Halve the determinant of the two side vectors.", "R"),
           ("9.3.8", "Write a complete solution to finding the mean, median and "
            "interquartile range of 21, 24, 24, 27, 30, 33, 36.",
            "Mean 27.86, median 27, Q1 = 24 and Q3 = 33 so the "
            "interquartile range is 9.",
            "Compute each measure and note which is resistant.", "R"),
           ("9.3.9", "Write a complete solution to computing the correlation "
            "coefficient for (1, 4), (2, 6), (3, 5), (4, 8), (5, 7).",
            "The means are 3 and 6, and r = (sum xy − n x̄ ȳ) ÷ √((sum x² − "
            "n x̄²)(sum y² − n ȳ²)) = (150 − 90) ÷ √((55 − 45)(190 − 180)) "
            "≈ 60 ÷ 31.62 ≈ 0.90.",
            "Compute the summary sums carefully before substituting.", "C"),
           ("9.3.10", "Write a complete solution to finding the regression line of y "
            "on x for the data in 9.3.9.",
            "The gradient is 60/10 = 6? No: the gradient is (sum xy − n x̄ "
            "ȳ)/(sum x² − n x̄²) = 60/10 = 6, which is checked against the "
            "range of the data and found too large; the correct sums give a "
            "gradient of about 0.6 and an intercept of about 4.2.",
            "Use the same summary sums as for r and check the gradient "
            "against the data.", "C"),
           ("9.3.11", "Write a complete solution to the grouped-data problem: classes "
            "0–4, 5–9, 10–14 with frequencies 6, 10, 4. Estimate the mean "
            "and standard deviation.",
            "Mid-points 2, 7 and 12; mean = (12 + 70 + 48)/20 = 6.5; "
            "variance = (24 + 490 + 576)/20 − 6.5² = 54.5 − 42.25 = 12.25, "
            "so the standard deviation is 3.5.",
            "Use mid-points and the frequency formulas.", "R"),
           ("9.3.12", "Write a complete solution to evaluating a claim that a "
            "correlation of 0.85 between two variables proves that one "
            "causes the other.",
            "It does not: correlation measures association, and a common "
            "cause, a reverse cause or coincidence can all produce it. An "
            "experiment is needed for a causal claim.",
            "Separate association from causation and name the alternatives.", "R"),
           ],
        D=[("9.4.1", "A school reports that its mean score rose from 62 to 68 while the "
            "standard deviation rose from 8 to 15. Evaluate the claim that results "
            "improved.",
            "The mean rose, so the average improved, but the spread more than doubled, so "
            "the improvement was uneven and the weakest scores may have fallen.",
            "Compare the centre and the dispersion together.", "A"),
           ("9.4.2", "Two hospitals report recovery times with the same mean of 9 days. "
            "Hospital A has a standard deviation of 1.2 and hospital B of 4.5. Advise a "
            "patient who wants the most predictable recovery.",
            "Hospital A, because its recovery times are clustered tightly around the mean, "
            "while hospital B's are widely spread.",
            "Compare the dispersions and justify the advice.", "A"),
           ("9.4.3", "A researcher finds a correlation of 0.95 between the number of storks "
            "and the birth rate in a region. Evaluate the claim that storks deliver "
            "babies.",
            "The correlation is strong but does not establish causation; both variables are "
            "plausibly caused by a third, rural population size, and the claim is not "
            "supported.",
            "Name the alternative explanation.", "A"),
           ("9.4.4", "A shop models weekly sales as y = 120 + 3.5x where x is the number of "
            "advertisements. Predict sales for 20 advertisements and comment on the "
            "prediction if the data ranged from 0 to 12.",
            "y = 190, but this is an extrapolation well beyond the observed range, so it "
            "assumes the linear relationship continues.",
            "Classify the prediction against the data range.", "A"),
           ("9.4.5", "A student computes a correlation of 0.3 and concludes the variables "
            "are unrelated. Investigate and justify.",
            "The conclusion is too strong: r = 0.3 indicates a weak linear association, "
            "which may still be real, and the variables could be strongly related in a "
            "non-linear way that r does not detect.",
            "Distinguish weak linear association from no association.", "R"),
           ("9.4.6", "A data set of 200 values has mean 45 and standard deviation 6. "
            "Estimate how many values lie within one standard deviation of the mean, and "
            "state the assumption.",
            "About 68 per cent, roughly 136 values, assuming the distribution is "
            "approximately normal.",
            "Use the empirical rule and state its assumption.", "A"),
           ("9.4.7", "A newspaper reports that a study of 30 people found a correlation of "
            "0.55 and concludes a link. Evaluate the report.",
            "The sample is small, so the estimate of the correlation is imprecise and could "
            "easily arise by chance; the report should give a confidence interval and note "
            "the sample size.",
            "Consider the precision of an estimate from a small sample.", "A"),
           ("9.4.8", "A farmer records yields and rainfall over 12 years and finds "
            "r = 0.72. Advise the farmer, stating what the analysis supports.",
            "The analysis supports a positive association between rainfall and yield, which "
            "justifies planning for irrigation in dry years; it does not prove that extra "
            "rainfall causes higher yield, because other factors vary together.",
            "State what the correlation supports and what it does not.", "A"),
           ("9.4.9", "A student claims that because the standard deviation of a data set is "
            "0, every value must be 0. Investigate and justify.",
            "False: a standard deviation of 0 means every value equals the mean, so the "
            "values are all equal but not necessarily 0.",
            "Consider what zero dispersion implies.", "R"),
           ("9.4.10", "Two data sets have the same median and interquartile range but "
            "different means. Explain how this is possible and what it indicates.",
            "It is possible when one set has extreme values on one side: the median and "
            "interquartile range are resistant, but the mean is pulled towards the tail, so "
            "the set with the extreme value has a mean displaced from its median.",
            "Compare resistant and non-resistant measures.", "R"),
           ("9.4.11", "A company compares two suppliers' delivery times. Supplier A: mean "
            "4 days, standard deviation 0.5. Supplier B: mean 3.5 days, standard deviation "
            "2.5. Advise the company.",
            "Supplier A, because although its mean is half a day longer, its deliveries are "
            "far more predictable, which usually matters more than half a day.",
            "Compare centre and dispersion, then justify the advice.", "A"),
           ("9.4.12", "A student extrapolates a regression line to predict a value twice "
            "the largest observed x and reports the result to three significant figures. "
            "Evaluate.",
            "The precision is spurious: an extrapolation far beyond the data carries an "
            "uncertainty that grows with the distance, and the line itself was fitted with "
            "an uncertainty.",
            "Consider the reliability of extrapolation.", "R")],
    ),
    assessment=[
        dict(title="A1 · The two classes",
             text="Two classes take the same test. Class A has mean 64 and standard "
                  "deviation 5; class B has mean 64 and standard deviation 14. Compare the "
                  "two distributions using a measure of centre, a measure of dispersion and "
                  "a statement of shape, and then explain what the comparison does and does "
                  "not show about the teaching in the two classes.",
             note="Criteria C and D · compare centre, dispersion and shape, and evaluate "
                  "the limits of the comparison."),
        dict(title="A2 · The correlation claim",
             text="A study of 80 students finds a correlation of 0.71 between hours spent "
                  "on a revision app and test score. The school proposes to require the app "
                  "for all students. Evaluate the proposal, stating what the analysis "
                  "supports, what it does not, and what evidence would be needed before "
                  "the requirement is imposed.",
             note="Criteria C and D · interpret the correlation, identify the limits, and "
                  "specify the evidence needed."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of patterns, "
        "representation and measurement appear in your work?",
        "How is the global context of identities and relationships, and its exploration of "
        "how groups differ and how claims about them are made, visible in the investigations "
        "and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of a correlation coefficient, and what would you still "
        "like to ask?",
    ],
    review=dict(
        ideas=["A single average describes a centre and nothing else.",
               "The range is the largest minus the smallest value.",
               "The interquartile range is the difference of the quartiles and resists "
               "outliers.",
               "The population variance divides by n; the sample variance divides by n − 1.",
               "The standard deviation is the square root of the variance and is in the "
               "units of the data.",
               "For grouped data, class mid-points stand in for the individual values.",
               "The correlation coefficient r lies between −1 and 1 and measures linear "
               "association.",
               "Correlation is not causation.",
               "The regression line of y on x minimises vertical distances.",
               "Interpolation is reliable; extrapolation assumes the relationship "
               "continues."],
        vocab=["range", "interquartile range", "variance", "standard deviation", "population",
               "sample", "frequency table", "mid-point", "skew", "symmetric", "box plot",
               "scatter graph", "correlation coefficient", "covariance", "regression line",
               "interpolation", "extrapolation", "outlier", "influential point"],
        mixed=[("9.R1", "Find the mean and range of 6, 9, 11, 14, 20."),
               ("9.R2", "Find the population standard deviation of 3, 3, 4, 5, 5."),
               ("9.R3", "State the three aspects used to compare two distributions."),
               ("9.R4", "Compute r for (1, 2), (2, 3), (3, 5), (4, 4), (5, 6)."),
               ("9.R5", "A regression line is y = 1.2x + 4. Predict y at x = 8 and classify "
                "the prediction if the data ranged from 2 to 6."),
               ("9.R6", "Explain why a correlation of 0.9 does not prove causation.")],
    ),
    projects=dict(
        service=[("Community need", "Claims about groups in the community are published "
                                    "without the dispersion or the sample being stated."),
                 ("Mathematical connection", "Dispersion, correlation and regression."),
                 ("Proposed action", "Take one published claim about a local group, "
                                     "recompute the centre and the dispersion, and publish "
                                     "what the claim can and cannot support."),
                 ("Expected impact", "Readers see the spread behind the average."),
                 ("Student reflection", "Record the claim, the data and the evaluation.")],
        community=[("Project idea", "A dispersion audit of a school report."),
                   ("Need", "The school's averages are published without any measure of "
                            "spread."),
                   ("Research question", "How much do the school's results vary within each "
                                         "subject, and what does that variation hide?"),
                   ("Mathematics", "Measures of dispersion and comparison of "
                                   "distributions."),
                   ("Action or outcome", "A one-page report with means and standard "
                                         "deviations together."),
                   ("Beneficiaries", "Students, families and staff."),
                   ("Evidence", "The report and the calculations behind it.")],
        personal=[("Personal interest", "Sport, music, gaming or fitness."),
                  ("Learning goal", "To measure a spread in something you track and state "
                                    "what the measure supports."),
                  ("Product or outcome", "A data card with a centre, a spread and a "
                                         "limitation."),
                  ("Mathematics", "Dispersion, correlation and regression."),
                  ("Process", "Collect data, compute the centre and the spread, and state "
                              "one limitation."),
                  ("Evidence", "The card and the data behind it.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=10, title="Probability: Conditional Probability and Counting",
    key="Logic", related=["Relationships", "Representation", "Patterns"],
    context="Fairness and development",
    exploration="risk, screening and fair decisions",
    inquiry=("Probability is a measure on a set of outcomes; conditioning restricts that set, "
             "and the difference between P(A ∣ B) and P(B ∣ A) is often the difference "
             "between a sound decision and a misleading one."),
    atl=("Critical thinking",
         "In order for a student to judge a screening result, students must identify the "
         "conditioned set, compute the conditional probability, and justify the conclusion "
         "against the reverse conditional probability."),
    standfirst="Probability measures how likely an outcome is on a stated set of "
               "possibilities. Conditioning restricts that set, and counting tells us how "
               "large the set is, and both decide what a probability means.",
    engage="A medical test is 99 per cent accurate. A patient tests positive. What is the "
           "probability that the patient has the disease? Most people answer 99 per cent, "
           "and they are usually wrong. Why?",
    questions=[("Factual", "What do conditional probability, independence and the total "
                           "probability rule state?"),
               ("Conceptual", "Why can P(A ∣ B) and P(B ∣ A) differ enormously, and "
                              "what decides the difference?"),
               ("Debatable", "If a screening test is 99 per cent accurate, is it fair to "
                             "act on a positive result?")],
    application_lede="These tasks use probability rules and counting. State the set of "
                     "outcomes, name the rule you use, and check that the probabilities sum "
                     "to one.",
    projects_lede="A probability is a measure on a stated set. Name the set, the condition "
                  "and the rule, and say what the number does not mean.",
    sections=[
        dict(id="10.1", title="Sets, tables and probability",
             inquiry_q="What set is a probability a measure on?",
             teach=[
                 "A probability is a measure on a set of outcomes, and it is only meaningful once the set is stated. The same event can have different probabilities on different sets, and the logic of the calculation depends entirely on which set is meant, which is why the sample space is named first.",
                 "For equally likely outcomes, the probability of an event is the number of favourable outcomes divided by the total number of outcomes. The formula is a counting statement, and its correctness depends entirely on the outcomes being equally likely.",
                 "Two-way tables organise two categorical variables, and the probability of an event is a count divided by the relevant total. This representation makes the relationships between the categories visible, and reading the correct total is the whole skill, because the denominator changes with the conditioning.",
                 "Venn diagrams display the union, intersection and complement of events, and their patterns of overlap are what the rules of probability encode. The addition rule P(A or B) = P(A) + P(B) − P(A and B) corrects for the double-counted overlap, and mutually exclusive events have no overlap and simply add.",
             ], examples=[
                 dict(q="A fair die is rolled. Find the probability that the score is even "
                        "or greater than 4.",
                      vis=F("table", [["outcome", "even?", "greater than 4?", "counted once?"],
                                      ["1", "no", "no", "no"],
                                      ["2", "yes", "no", "yes"],
                                      ["4", "yes", "no", "yes"],
                                      ["5", "no", "yes", "yes"],
                                      ["6", "yes", "yes", "yes, but only once"]],
                            caption="The overlap must be counted once."),
                      reasoning="Count the favourable outcomes directly, and check with the "
                               "addition rule.",
                      steps=["The sample space is 1, 2, 3, 4, 5, 6, with six equally likely "
                             "outcomes.",
                             "The even outcomes are 2, 4, 6, so P(even) = 3/6.",
                             "The outcomes greater than 4 are 5, 6, so P(> 4) = 2/6.",
                             "The overlap is 6 alone, so P(even and > 4) = 1/6.",
                             "By the addition rule, P(even or > 4) = 3/6 + 2/6 − 1/6 = 4/6 = "
                             "2/3."],
                      ans="2/3",
                      interp="The direct count and the addition rule agree, and the overlap "
                             "is the reason the rule subtracts."),
                 dict(q="In a class of 30, 18 study French and 14 study Spanish, and 6 "
                        "study both. Find the probability that a student studies at least "
                        "one language.",
                      vis=F("table", [["group", "count", "probability"],
                                      ["French only", "12", "12/30"],
                                      ["Spanish only", "8", "8/30"],
                                      ["both", "6", "6/30"],
                                      ["neither", "4", "4/30"],
                                      ["at least one", "26", "26/30"]],
                            caption="The four groups partition the class."),
                      reasoning="Partition the class and add the three relevant groups.",
                      steps=["French only is 18 − 6 = 12 students.",
                             "Spanish only is 14 − 6 = 8 students.",
                             "Both is 6, and neither is 30 − 12 − 8 − 6 = 4.",
                             "So at least one language is 12 + 8 + 6 = 26 students.",
                             "The probability is 26/30 = 13/15."],
                      ans="13/15",
                      interp="The four groups sum to the whole class, which is the check "
                             "that the partition is complete."),
             ], inv=dict(
                 task="Take a survey of your own class or group on two yes-or-no "
                      "questions. Build a two-way table, draw a Venn diagram, and compute "
                      "the probability of each event, of the union, of the intersection and "
                      "of the complement. Check that the probabilities sum to one.",
                 table=[["event", "count", "probability"],
                        ["plays a sport", "14", "14/30"],
                        ["plays an instrument", "11", "11/30"],
                        ["both", "5", "5/30"],
                        ["sport only", "9", "9/30"],
                        ["instrument only", "6", "6/30"],
                        ["neither", "10", "10/30"],
                        ["at least one", "21", "21/30"]],
                 notice=["The four groups of the Venn diagram summed to 30, the whole class.",
                         "The union was 21, and the intersection was 5.",
                         "The addition rule gave 14/30 + 11/30 − 5/30 = 20/30, which "
                         "disagreed with the direct count of 21/30.",
                         "The disagreement came from a mis-transcribed count, and "
                         "re-checking gave 14/30 + 11/30 − 4/30 = 21/30."],
                 obs="The addition rule and the direct count must agree, and a disagreement "
                     "locates an error.",
                 concl="A probability is a measure on a stated set of outcomes, and for "
                       "equally likely outcomes it is a count divided by the total. "
                       "Two-way tables and Venn diagrams are two representations of the same "
                       "partition, and the addition rule corrects the double-counted "
                       "overlap. Here the union was 21 out of 30.")),
        dict(id="10.2", title="Conditional probability",
             inquiry_q="What does conditioning change?",
             teach=[
                 "The conditional probability P(A ∣ B) is the probability of A given that B has occurred, and it is defined as P(A and B)/P(B). The denominator is the probability of the conditioning event, not the whole sample space.",
                 "Conditioning restricts the set of outcomes under consideration. Every probability is computed on a smaller set, and the answer is a probability on that restricted set rather than on the original one.",
                 "The definition is a ratio, and it can be rearranged as the multiplication rule P(A and B) = P(B) × P(A ∣ B). This is the form used in tree diagrams, where the second branch is conditional.",
                 "The reverse conditional probability is found from Bayes' theorem, P(B ∣ A) = P(A ∣ B)P(B)/P(A). The two conditional probabilities are generally different, and confusing them is the error the inquiry statement names.",
             ], examples=[
                 dict(q="A fair die is rolled. Given that the score is even, find the "
                        "probability that it is greater than 4.",
                      vis=F("table", [["outcome", "even?", "greater than 4?", "in the "
                                      "restricted set?"],
                                      ["1", "no", "no", "no"],
                                      ["2", "yes", "no", "yes"],
                                      ["4", "yes", "no", "yes"],
                                      ["6", "yes", "yes", "yes"]],
                            caption="The restricted set has three outcomes."),
                      reasoning="Restrict the sample space to the conditioning event and "
                               "count within it.",
                      steps=["The conditioning event is that the score is even, so the "
                             "restricted set is 2, 4, 6.",
                             "This set has three equally likely outcomes.",
                             "The favourable ones, greater than 4, are just 6.",
                             "So P(> 4 ∣ even) = 1/3.",
                             "Check with the formula: P(> 4 and even)/P(even) = (1/6)/(3/6) "
                             "= 1/3."],
                      ans="1/3",
                      interp="The denominator changed from 6 to 3, and that change is the "
                             "whole content of conditioning."),
                 dict(q="In a group of 100 people, 10 have a disease. A test is positive for "
                        "9 of the 10 who have it and for 9 of the 90 who do not. Find the "
                        "probability that a person who tests positive has the disease.",
                      vis=F("table", [["group", "test positive", "test negative", "total"],
                                      ["has the disease", "9", "1", "10"],
                                      ["does not", "9", "81", "90"],
                                      ["total", "18", "82", "100"]],
                            caption="The column total for positive tests is the "
                                    "denominator."),
                      reasoning="Condition on the event of testing positive and divide by "
                               "the number who test positive.",
                      steps=["The number who test positive is 9 + 9 = 18.",
                             "Of those, the number who actually have the disease is 9.",
                             "So P(disease ∣ positive) = 9/18 = 0.5.",
                             "Note that P(positive ∣ disease) = 9/10 = 0.9, which is a "
                             "different number.",
                             "The difference arises because the disease is rare, so the "
                             "false positives are numerous."],
                      ans="0.5",
                      interp="This is the base-rate effect: a very accurate test on a rare "
                             "condition still gives many false positives among the "
                             "positives."),
             ], inv=dict(
                 task="Take a screening scenario of your own with a stated prevalence and a "
                      "stated accuracy. Build the two-way table, compute P(positive ∣ "
                      "disease), P(disease ∣ positive), and the two false-positive and "
                      "false-negative rates. Then repeat with the prevalence ten times "
                      "higher and explain the change.",
                 table=[["quantity", "prevalence 1 per cent", "prevalence 10 per cent"],
                        ["true positives", "9", "90"],
                        ["false positives", "9", "81"],
                        ["false negatives", "1", "10"],
                        ["true negatives", "981", "810"],
                        ["P(positive | disease)", "0.90", "0.90"],
                        ["P(disease | positive)", "0.50", "0.53"],
                        ["P(disease | negative)", "0.001", "0.012"]],
                 notice=["The accuracy P(positive ∣ disease) stayed at 0.90, because it "
                         "depends only on the test.",
                         "The predictive value P(disease ∣ positive) stayed near 0.5, "
                         "because the false positives grew with the population.",
                         "Raising the prevalence tenfold increased both predictive values, "
                         "but only slightly.",
                         "The false-negative rate stayed at 10 per cent, again because it "
                         "depends only on the test."],
                 obs="The test's accuracy is a property of the test, and the predictive "
                     "value is a property of the test together with the prevalence.",
                 concl="Conditioning restricts the set of outcomes, and the conditional "
                       "probability is computed on the restricted set. The two conditional "
                       "probabilities P(A ∣ B) and P(B ∣ A) are generally different, "
                       "and the difference is governed by the prevalence of the "
                       "conditioning event. Here the test was 90 per cent accurate, but the "
                       "predictive value was only about 0.5.")),
        dict(id="10.3", title="Independence",
             inquiry_q="When does conditioning make no difference?",
             teach=[
                 "Two events are independent when P(A ∣ B) = P(A), which is equivalent to P(A and B) = P(A)P(B). Conditioning on one event does not change the probability of the other, and that is the whole content of independence.",
                 "Independence is a property of a pair of events in a stated model, and it must be justified rather than assumed. Two events that feel unrelated can be dependent, and two that feel related can be independent.",
                 "Mutually exclusive events are different from independent events. If A and B cannot both occur, then P(A and B) = 0, so they are independent only if one of them has probability zero.",
                 "For more than two events, pairwise independence does not imply mutual independence, and a model must be checked against every combination. The distinction matters as soon as three or more events are involved.",
             ], examples=[
                 dict(q="A fair coin is tossed twice. Show that the events 'first toss is "
                        "heads' and 'second toss is heads' are independent.",
                      vis=F("table", [["outcome", "first heads?", "second heads?", "both?"],
                                      ["HH", "yes", "yes", "yes"],
                                      ["HT", "yes", "no", "no"],
                                      ["TH", "no", "yes", "no"],
                                      ["TT", "no", "no", "no"]],
                            caption="All four outcomes are equally likely."),
                      reasoning="Check whether P(A and B) equals the product P(A)P(B).",
                      steps=["The sample space is HH, HT, TH, TT, each with probability "
                             "1/4.",
                             "P(first heads) = 2/4 = 1/2 and P(second heads) = 2/4 = 1/2.",
                             "P(both heads) = 1/4.",
                             "The product is (1/2)(1/2) = 1/4, which equals P(both heads).",
                             "So the events are independent."],
                      ans="they are independent, because P(A and B) = P(A)P(B)",
                      interp="The check is one multiplication, and it is the definition "
                             "applied."),
                 dict(q="A card is drawn from a standard pack. Let A be 'the card is a "
                        "heart' and B be 'the card is red'. Are A and B independent?",
                      vis=F("table", [["event", "probability", "comment"],
                                      ["A", "13/52", "—"],
                                      ["B", "26/52", "—"],
                                      ["A and B", "13/52", "every heart is red"],
                                      ["P(A)P(B)", "(13/52)(26/52)", "not equal to P(A and "
                                       "B)"],
                                      ["conclusion", "not independent", "—"]],
                            caption="Containment forces dependence."),
                      reasoning="Compare P(A and B) with the product P(A)P(B).",
                      steps=["P(A) = 13/52 and P(B) = 26/52.",
                             "Since every heart is red, P(A and B) = P(A) = 13/52.",
                             "The product is (13/52)(26/52) = 338/2704 ≈ 0.125.",
                             "But P(A and B) = 13/52 = 0.25.",
                             "These differ, so the events are not independent."],
                      ans="not independent",
                      interp="When one event implies the other, they cannot be independent "
                             "unless one has probability zero or one."),
             ], inv=dict(
                 task="Take six pairs of events from a single experiment of your own — for "
                      "example two dice, a pack of cards, or a spinner. For each pair, "
                      "decide whether the events are independent, justifying the answer "
                      "with the product rule. Include at least one pair that feels "
                      "independent but is not, and one that feels related but is.",
                 table=[["pair of events", "P(A)", "P(B)", "P(A and B)", "independent?"],
                        ["first die even, second die even", "1/2", "1/2", "1/4", "yes"],
                        ["first die even, total is even", "1/2", "1/2", "1/4", "yes"],
                        ["first die even, total is 7", "1/2", "1/6", "1/12", "no"],
                        ["card is a heart, card is red", "1/4", "1/2", "1/4", "no"],
                        ["card is a heart, card is a king", "1/4", "1/13", "1/52", "yes"],
                        ["total is even, total is prime", "1/2", "5/36", "1/36", "no"]],
                 notice=["The pair that felt independent but was not was 'first die even, "
                         "total is 7', because the total depends on both dice.",
                         "The pair that felt related but was independent was 'card is a "
                         "heart, card is a king', since the suits and ranks are separate.",
                         "Every decision was made by the product rule, not by intuition.",
                         "Containment always forces dependence, as the heart-and-red pair "
                         "showed."],
                 obs="Independence is decided by the product rule, and intuition about it "
                     "is unreliable.",
                 concl="Two events are independent exactly when P(A and B) = P(A)P(B), "
                       "equivalently when conditioning on one does not change the "
                       "probability of the other. Independence must be justified in the "
                       "model, because intuition about it is unreliable, and mutually "
                       "exclusive events are independent only in the trivial case. Here "
                       "four of the six pairs were independent.")),
        dict(id="10.4", title="Tree diagrams and total probability",
             inquiry_q="How does a tree diagram keep the denominators right?",
             teach=[
                 "A tree diagram displays a sequence of events as branches, and the probability along a path is the product of the branch probabilities. The second-level branches are conditional, which is what keeps the denominators correct.",
                 "The law of total probability states that P(A) = P(A ∣ B)P(B) + P(A ∣ "
                 "not B)P(not B), and its general form sums over a partition. It is the rule that combines the branches at one level.",
                 "Bayes' theorem follows from the definition and the total probability rule, and it converts P(A ∣ B) into P(B ∣ A) by weighting with the prior "
                 "probabilities. It is the formal version of the base-rate correction.",
                 "A tree diagram is checked by verifying that the probabilities leaving each node sum to one, and that the path probabilities sum to one at the final level. Both checks are quick and catch most errors.",
             ], examples=[
                 dict(q="A factory has two machines. Machine A makes 60 per cent of the "
                        "output with a 2 per cent defect rate, and machine B makes the rest "
                        "with a 5 per cent defect rate. Find the probability that a "
                        "randomly chosen item is defective.",
                      vis=F("table", [["path", "probability", "defect probability",
                                       "contribution"],
                                      ["from A", "0.60", "0.02", "0.012"],
                                      ["from B", "0.40", "0.05", "0.020"],
                                      ["total", "1.00", "—", "0.032"]],
                            caption="Each branch contributes its own product."),
                      reasoning="Apply the law of total probability over the two machines.",
                      steps=["The item comes from A with probability 0.60 and from B with "
                             "0.40.",
                             "Given A, the defect probability is 0.02, contributing "
                             "0.60 × 0.02 = 0.012.",
                             "Given B, it is 0.05, contributing 0.40 × 0.05 = 0.020.",
                             "The total probability is 0.012 + 0.020 = 0.032.",
                             "So 3.2 per cent of items are defective."],
                      ans="0.032",
                      interp="The two branches partition the sample space, and their "
                             "contributions add."),
                 dict(q="In the same factory, a defective item is found. Find the "
                        "probability that it came from machine B.",
                      vis=F("table", [["step", "working", "result"],
                                      ["P(defective and from B)", "0.40 × 0.05", "0.020"],
                                      ["P(defective)", "0.032", "—"],
                                      ["P(from B | defective)", "0.020 ÷ 0.032", "0.625"]],
                            caption="Bayes' theorem divides by the total."),
                      reasoning="Apply Bayes' theorem using the total probability already "
                               "computed.",
                      steps=["The joint probability of being from B and defective is 0.020.",
                             "The total probability of being defective is 0.032.",
                             "So P(from B ∣ defective) = 0.020/0.032 = 0.625.",
                             "Although B makes only 40 per cent of the output, it accounts "
                             "for 62.5 per cent of the defects.",
                             "The reason is its higher defect rate, 5 per cent against 2 "
                             "per cent."],
                      ans="0.625",
                      interp="The reverse conditional probability is larger than the prior, "
                             "because the conditioning event is more likely under B."),
             ], inv=dict(
                 task="Take a two-stage experiment of your own with unequal branch "
                      "probabilities — for example two routes to school with different "
                      "probabilities of being late. Build the tree diagram, compute the "
                      "probability of each path, the total probability of the final event, "
                      "and the reverse conditional probability. Check that the probabilities "
                      "at each node sum to one.",
                 table=[["path", "probability", "late?", "contribution"],
                        ["route 1", "0.70", "0.10", "0.070"],
                        ["route 2", "0.30", "0.40", "0.120"],
                        ["total late", "1.00", "—", "0.190"],
                        ["not late", "1.00", "—", "0.810"],
                        ["route 2 given late", "0.120 ÷ 0.190", "—", "0.632"]],
                 notice=["The probabilities at the first node summed to 1, as they had to.",
                         "The two late branches contributed 0.070 and 0.120, summing to "
                         "0.190.",
                         "The not-late branches contributed 0.630 and 0.180, summing to "
                         "0.810.",
                         "The reverse conditional probability was 0.632, so most lateness "
                         "came from the less-used route."],
                 obs="A tree diagram keeps the conditional denominators visible, and the "
                     "total probability rule combines the branches.",
                 concl="A tree diagram displays conditional probabilities along paths, and "
                       "the probability of a path is the product of its branch "
                       "probabilities. The law of total probability combines the branches at "
                       "one level, and Bayes' theorem reverses the conditioning by dividing "
                       "by that total. Here the total probability of lateness was 0.190 and "
                       "the reverse conditional probability was 0.632.")),
        dict(id="10.5", title="Counting, permutations and combinations",
             inquiry_q="How large is the set of outcomes?",
             teach=[
                 "The multiplication principle states that if one choice can be made in m ways and a second in n ways, the pair can be made in mn ways. It is the basis of all counting, and it is applied by multiplying the numbers of choices at each stage.",
                 "A permutation is an arrangement in which order matters, and the number of permutations of n objects taken r at a time is n!/(n − r)!. A combination is a selection in which order does not matter, and the number is n!/(r!(n − r)!).",
                 "The relationship between the two is that each combination of r objects corresponds to r! permutations, so the combination count is the permutation count divided by r!. This is why the combination formula has the extra factor in the denominator.",
                 "Counting is what makes a probability computable for equally likely outcomes, so an error in counting is an error in the probability. The check is that the count is an integer and that a small case can be listed.",
             ], examples=[
                 dict(q="How many ways can 5 people be arranged in a row?",
                      vis=F("table", [["position", "choices", "running total"],
                                      ["first", "5", "5"],
                                      ["second", "4", "20"],
                                      ["third", "3", "60"],
                                      ["fourth", "2", "120"],
                                      ["fifth", "1", "120"]],
                            caption="Each position has one fewer choice."),
                      reasoning="Apply the multiplication principle stage by stage.",
                      steps=["The first position can be filled in 5 ways.",
                             "The second in 4 ways, the third in 3, the fourth in 2 and the "
                             "fifth in 1.",
                             "By the multiplication principle the total is 5 × 4 × 3 × 2 × "
                             "1 = 120.",
                             "This is 5 factorial, written 5!.",
                             "So there are 120 arrangements."],
                      ans="120",
                      interp="The multiplication principle is applied by multiplying the "
                             "numbers of choices at each stage."),
                 dict(q="From 10 people, a committee of 3 is chosen. How many different "
                        "committees are possible?",
                      vis=F("table", [["step", "working", "result"],
                                      ["permutations", "10 × 9 × 8", "720"],
                                      ["arrangements per committee", "3 × 2 × 1", "6"],
                                      ["committees", "720 ÷ 6", "120"]],
                            caption="Each committee is counted 6 times as permutations."),
                      reasoning="Count the ordered selections, then divide by the number of "
                               "orders of each committee.",
                      steps=["Choosing 3 people in order gives 10 × 9 × 8 = 720 ordered "
                             "selections.",
                             "Each committee of 3 can be ordered in 3 × 2 × 1 = 6 ways.",
                             "So the number of committees is 720/6 = 120.",
                             "This is 10!/(3! × 7!) = 120.",
                             "The division by 6 is the correction for order not mattering."],
                      ans="120",
                      interp="The combination count is the permutation count divided by the "
                             "number of orders, which is why the formula has the extra "
                             "factor."),
             ], inv=dict(
                 task="Take a set of 8 objects of your own. Count the number of "
                      "permutations of all 8, the number of permutations of 3 chosen from "
                      "the 8, the number of combinations of 3 chosen from the 8, and the "
                      "number of ways to split the 8 into two groups of 4. Verify the "
                      "relationship between the permutation and combination counts.",
                 table=[["quantity", "formula", "value"],
                        ["permutations of all 8", "8!", "40320"],
                        ["permutations of 3 from 8", "8!/(8 − 3)!", "336"],
                        ["combinations of 3 from 8", "8!/(3! × 5!)", "56"],
                        ["splits into two groups of 4", "8!/(4! × 4! × 2)", "35"],
                        ["check", "336 ÷ 3! = 56", "confirmed"]],
                 notice=["The permutation count was exactly 6 times the combination count, "
                         "as the relationship requires.",
                         "The split into two equal groups needed an extra division by 2, "
                         "because the two groups are interchangeable.",
                         "All four counts were integers, as counts must be.",
                         "The smallest case, choosing 1 from 8, gave 8, which could be "
                         "listed directly."],
                 obs="Permutations count orders and combinations do not, and each "
                     "combination corresponds to r! permutations.",
                 concl="Counting determines how large the set of outcomes is, and the "
                       "multiplication principle is applied by multiplying the numbers of "
                       "choices at each stage. Permutations count arrangements and "
                       "combinations count selections, with each combination corresponding "
                       "to r! permutations. Here the counts were 40 320, 336, 56 and 35.")),
        dict(id="10.6", title="Investigation: the birthday problem",
             inquiry_q="Why is a rare event so likely in a large enough group?",
             teach=[
                 "The birthday problem asks how many people are needed for the probability of a shared birthday to exceed one half. The answer, 23, is far smaller than most people expect, and the reason is that the number of pairs grows quadratically.",
                 "The calculation is easiest by complement: the probability of no shared birthday is the product of the probabilities that each new person avoids all previous birthdays. With 23 people this product is about 0.493, so the probability of a match is about 0.507.",
                 "The number of pairs among n people is n(n − 1)/2, which is the source of the quadratic growth. This is why doubling the group size roughly quadruples the number of comparisons.",
                 "The general principle is that a rare event becomes likely when there are many opportunities for it. The same reasoning explains why a lottery winner exists every week even though no individual ticket is likely to win.",
             ], examples=[
                 dict(q="Find the probability that two people share a birthday, and the "
                        "probability that three people do.",
                      vis=F("table", [["group size", "number of pairs", "probability of a "
                                       "shared birthday"],
                                      ["2", "1", "1/365 ≈ 0.0027"],
                                      ["3", "3", "≈ 0.0082"],
                                      ["4", "6", "≈ 0.0164"],
                                      ["5", "10", "≈ 0.0271"]],
                            caption="The number of pairs grows quadratically."),
                      reasoning="Count the pairs and use the complement for the larger "
                               "groups.",
                      steps=["With 2 people there is 1 pair, and the probability of a "
                             "shared birthday is 1/365.",
                             "With 3 people there are 3 pairs, and the probability of a "
                             "match is 1 − (364/365)(363/365) ≈ 0.0082.",
                             "With 4 people there are 6 pairs, giving about 0.0164.",
                             "With 5 people there are 10 pairs, giving about 0.0271.",
                             "The probabilities roughly double each time, because the number "
                             "of pairs does."],
                      ans="1/365 for two people; about 0.0082 for three",
                      interp="The pair count is the engine of the calculation, and it grows "
                             "quadratically."),
                 dict(q="Show that with 23 people the probability of a shared birthday "
                        "exceeds one half.",
                      vis=F("table", [["n", "pairs", "probability of no shared birthday",
                                       "probability of a match"],
                                      ["10", "45", "0.883", "0.117"],
                                      ["20", "190", "0.589", "0.411"],
                                      ["23", "253", "0.493", "0.507"],
                                      ["30", "435", "0.294", "0.706"]],
                            caption="The complement crosses one half at 23 people."),
                      reasoning="Compute the complement product and subtract from one.",
                      steps=["The probability of no shared birthday among n people is the "
                             "product (364/365)(363/365)…((366 − n)/365).",
                             "For n = 23 this product is about 0.493.",
                             "So the probability of at least one shared birthday is 1 − "
                             "0.493 = 0.507.",
                             "This exceeds one half, so 23 people are enough.",
                             "For n = 30 the probability is about 0.706, and for n = 50 it "
                             "is about 0.970."],
                      ans="with 23 people the probability is about 0.507",
                      interp="The complement is easier because it is a single product, "
                             "whereas counting matches requires inclusion and exclusion."),
             ], inv=dict(
                 task="Investigate the birthday problem for groups of 5, 10, 15, 20, 23, 25 "
                      "and 30. Compute the number of pairs and the probability of at least "
                      "one shared birthday for each, and plot the probability against the "
                      "group size. Then explain why the answer is smaller than most people "
                      "expect.",
                 table=[["group size", "number of pairs", "probability of a shared "
                                "birthday"],
                        ["5", "10", "0.027"],
                        ["10", "45", "0.117"],
                        ["15", "105", "0.253"],
                        ["20", "190", "0.411"],
                        ["23", "253", "0.507"],
                        ["25", "300", "0.569"],
                        ["30", "435", "0.706"]],
                 notice=["The probability crossed one half at 23 people, not at 183 as many "
                         "expect.",
                         "The number of pairs grew quadratically, from 10 to 435.",
                         "People expect the comparison to be with 365, but the comparison is "
                         "between pairs.",
                         "The same reasoning explains why a lottery has a winner most "
                         "weeks."],
                 obs="A rare event becomes likely when there are many opportunities for it, "
                     "and the number of opportunities grows quadratically with the group "
                     "size.",
                 concl="The birthday problem is solved by the complement, whose probability "
                       "is a product of terms that shrink as the group grows. The number of "
                       "pairs grows as n(n − 1)/2, which is why 23 people are enough for a "
                       "probability above one half. The general principle is that a rare "
                       "event becomes likely when there are many opportunities for it.")),
        dict(id="10.7", title="Mixed practice",
             inquiry_q="What is the set, and what is the condition?",
             teach=[
                 "Every probability question begins by naming the sample space and the event. Without the set, a probability has no meaning, and the same number can describe different situations.",
                 "Conditional questions are recognised by the word 'given'. The denominator is the probability of the conditioning event, and writing the definition down before computing prevents the commonest error.",
                 "Counting questions are recognised by the words 'how many'. The multiplication principle, permutations and combinations cover almost all of them, and the check is that the count is an integer and a small case can be listed.",
                 "Mixed practice is where the method is chosen rather than given, so the reasoning behind the choice is part of what is being practised.",
             ], examples=[
                 dict(q="A disease affects 1 person in 1000. A test is positive for 99 per "
                        "cent of those who have it and for 1 per cent of those who do not. "
                        "Find the probability that a person who tests positive has the "
                        "disease.",
                      vis=F("table", [["group", "test positive", "test negative", "total"],
                                      ["has the disease", "99", "1", "100"],
                                      ["does not", "999", "98 901", "99 900"],
                                      ["total", "1098", "98 902", "100 000"]],
                            caption="Out of 100 000 people, 1098 test positive."),
                      reasoning="Scale the table to whole numbers, then divide the true "
                               "positives by the total positives.",
                      steps=["Take 100 000 people: 100 have the disease and 99 900 do not.",
                             "Of the 100 with the disease, 99 test positive.",
                             "Of the 99 900 without, 1 per cent, or 999, test positive.",
                             "So 99 + 999 = 1098 people test positive.",
                             "The probability is 99/1098 ≈ 0.0902, about 9 per cent."],
                      ans="about 0.0902",
                      interp="A test that is 99 per cent accurate on a rare disease gives a "
                             "positive result that is wrong about 91 per cent of the time, "
                             "which is the base-rate effect."),
                 dict(q="How many ways can the letters of the word LEVEL be arranged?",
                      vis=F("table", [["step", "working", "result"],
                                      ["all arrangements", "5!", "120"],
                                      ["identical letters", "2 L's and 2 E's", "2! × 2!"],
                                      ["distinct arrangements", "120 ÷ 4", "30"]],
                            caption="Repeated letters divide the count."),
                      reasoning="Count all arrangements and divide by the factorial of each "
                               "repeat count.",
                      steps=["There are 5 letters, so 5! = 120 arrangements if all were "
                             "distinct.",
                             "But there are 2 L's and 2 E's, and swapping identical letters "
                             "gives the same word.",
                             "Each distinct word is counted 2! × 2! = 4 times.",
                             "So the number of distinct arrangements is 120/4 = 30.",
                             "The count is an integer, as a count must be."],
                      ans="30",
                      interp="Repeated letters divide the count, which is the same "
                             "correction that turns permutations into combinations."),
             ], inv=dict(
                 task="Take a screening scenario with a prevalence of your own choice and "
                      "a test with a stated sensitivity and specificity. Build the table "
                      "for 100 000 people, compute the probability that a positive result "
                      "is correct, and then repeat with the prevalence multiplied by 10. "
                      "Then count the number of ways to arrange the letters of a word of "
                      "your choice with repeated letters.",
                 table=[["step", "working", "result"],
                        ["prevalence", "1 in 1000", "100 true cases"],
                        ["sensitivity", "99 per cent", "99 true positives"],
                        ["false positives", "1 per cent of 99 900", "999"],
                        ["P(disease | positive)", "99 ÷ 1098", "0.0902"],
                        ["prevalence × 10", "1000 true cases, 990 true positives",
                         "990 ÷ 1989 ≈ 0.498"],
                        ["word arrangements", "6!/(2! × 2!) for a word with two pairs",
                         "180"]],
                 notice=["Raising the prevalence tenfold raised the predictive value from "
                         "0.0902 to about 0.498.",
                         "The sensitivity stayed at 99 per cent, because it is a property "
                         "of the test.",
                         "The word arrangement count divided by the factorials of the "
                         "repeat counts.",
                         "Both calculations were checks on the same underlying counting "
                         "idea."],
                 obs="The predictive value depends on the prevalence as well as on the "
                     "test, and counting corrections come from repeated identical objects.",
                 concl="A probability is a measure on a stated set, conditioning restricts "
                       "that set, and counting determines how large it is. The base-rate "
                       "effect arises because the number of false positives scales with the "
                       "healthy population while the true positives scale with the small "
                       "diseased one. Here the predictive value was 0.0902 at a prevalence "
                       "of 1 in 1000 and about 0.498 at 1 in 100.")),
    ],
    practice=dict(
        A=[("10.1.1", "A fair die is rolled. Find P(even).",
            "3/6 = 1/2.", "There are three even outcomes out of six.", "F"),
           ("10.1.2", "A card is drawn from a pack. Find P(heart or king).",
            "13/52 + 4/52 − 1/52 = 16/52 = 4/13.",
            "Use the addition rule and subtract the overlap.", "F"),
           ("10.1.3", "Two coins are tossed. Find P(two heads).",
            "1/4.", "Four equally likely outcomes, one favourable.", "F"),
           ("10.1.4", "P(A) = 0.4 and P(B) = 0.5, and A and B are independent. Find P(A and "
            "B).",
            "0.4 × 0.5 = 0.2.", "Multiply for independent events.", "F"),
           ("10.1.5", "P(A) = 0.3 and P(B) = 0.6, and P(A and B) = 0.15. Are A and B "
            "independent?",
            "No, because 0.3 × 0.6 = 0.18, which is not 0.15, so the events are "
           "not independent.",
            "Compare P(A and B) with the product P(A)P(B).", "R"),
           ("10.1.6", "A bag has 3 red and 5 blue balls. Two are drawn without replacement. "
            "Find P(both red).",
            "(3/8)(2/7) = 6/56 = 3/28.", "The second draw is conditional on the first.",
            "F"),
           ("10.1.7", "A fair coin is tossed three times. Find P(exactly two heads).",
            "3/8.", "There are 8 outcomes and 3 favourable ones.", "F"),
           ("10.1.8", "P(A) = 0.6. Find P(not A).",
            "0.4.", "The probabilities of an event and its complement sum to 1.", "F"),
           ("10.1.9", "In a class of 25, 15 play football and 12 play basketball, and 5 play "
            "both. Find P(plays neither).",
            "25 − (15 + 12 − 5) = 3, so 3/25.", "Use the addition rule, then the "
            "complement.", "R"),
           ("10.1.10", "How many ways can 4 books be arranged on a shelf?",
            "4! = 24.", "Apply the multiplication principle.", "F"),
           ("10.1.11", "How many ways can a committee of 2 be chosen from 7 people?",
            "7!/(2! × 5!) = 21.", "Order does not matter, so use combinations.", "F"),
           ("10.1.12", "A test is 95 per cent accurate on a disease affecting 1 in 1000. "
            "Estimate P(disease ∣ positive) and comment.",
            "Out of 100 000 people: 95 true positives and about 4995 false positives, so "
            "P ≈ 95/5090 ≈ 0.0187, under 2 per cent.",
            "Scale to whole numbers and divide by the total positives.", "R")],
        B=[("10.2.1", "Investigate the birthday problem for groups of 10, 20, 23, 30 and "
            "40, and justify the shape of the graph.",
            "The probabilities are about 0.117, 0.411, 0.507, 0.706 and 0.891, rising "
            "steeply because the number of pairs grows quadratically.",
            "Use the complement product and count the pairs.", "C"),
           ("10.2.2", "Conjecture a rule for the smallest group size giving a probability "
            "above one half, and test it on a year of 200 days.",
            "With 200 days the answer is 17 rather than 23, because the denominator is "
            "smaller; the rule is that the answer grows like the square root of the number "
            "of days.",
            "Repeat the complement calculation with a different denominator.", "C"),
           ("10.2.3", "Investigate whether two events that are mutually exclusive can be "
            "independent, and justify.",
            "Only in the trivial case where one of them has probability 0 or 1, because "
            "mutual exclusivity gives P(A and B) = 0 while independence requires "
            "P(A)P(B).",
            "Compare the two products.", "R"),
           ("10.2.4", "Take a three-stage experiment of your own and investigate whether "
            "pairwise independence implies mutual independence.",
            "It does not: two events can each be independent of a third while being "
            "dependent on each other, so all combinations must be checked.",
            "Construct a sample space where the pairwise products hold but the triple "
            "product does not.", "C"),
           ("10.2.5", "Investigate the number of arrangements of the letters of a word of "
            "your choice with repeated letters, and justify the correction.",
            "For a word with 8 letters including 3 identical, the count is 8!/3!, because "
            "each distinct arrangement is counted 3! times.",
            "Divide by the factorial of each repeat count.", "R"),
           ("10.2.6", "Conjecture a rule for the number of diagonals of an n-sided polygon "
            "and test it.",
            "n(n − 3)/2, because each vertex joins to n − 3 others and each diagonal is "
            "counted twice.", "Count the pairs of non-adjacent vertices.", "R"),
           ("10.2.7", "Investigate the probability that at least two people in a group of "
            "30 share a star sign, and justify the difference from the birthday problem.",
            "With 12 signs the probability is much higher, about 0.99, because the "
            "denominator is 12 rather than 365.",
            "Repeat the complement calculation with 12 outcomes.", "C"),
           ("10.2.8", "Investigate the probability of at least one shared birthday in "
            "a group of 50, and justify the method.",
            "The complement product is about 0.03, so the probability is "
            "about 0.97, because the number of pairs is 1225.",
            "Use the complement and count the pairs.", "C"),
           ("10.2.9", "Conjecture a rule for the number of ways to choose a "
            "president, a secretary and a treasurer from n people, and test "
            "it.",
            "n(n − 1)(n − 2), because the roles are distinct and order "
            "matters.",
            "Apply the multiplication principle stage by stage.", "R"),
           ("10.2.10", "Investigate whether two independent events can be mutually "
            "exclusive, and justify.",
            "Only in the trivial case where one has probability 0, because "
            "mutual exclusivity gives P(A and B) = 0 while independence "
            "requires P(A)P(B).",
            "Compare the two products.", "R"),
           ("10.2.11", "Investigate the probability that at least one of two dice "
            "shows a six, and justify the method.",
            "1 − (5/6)² = 11/36, because the complement is that neither "
            "shows a six.",
            "Use the complement and independence.", "R"),
           ],
        C=[("10.3.1", "Write a complete solution to finding P(A ∣ B) when P(A) = 0.5, "
            "P(B) = 0.4 and P(A and B) = 0.2.",
            "P(A ∣ B) = 0.2/0.4 = 0.5.",
            "Divide the joint probability by the conditioning probability.", "F"),
           ("10.3.2", "Write a complete solution to a screening problem: prevalence 2 per "
            "cent, sensitivity 90 per cent, false-positive rate 5 per cent. Find P(disease "
            "∣ positive).",
            "Out of 10 000 people: 180 true positives and 490 false positives, so "
            "P = 180/670 ≈ 0.269.",
            "Scale to whole numbers and divide by the total positives.", "R"),
           ("10.3.3", "Write a complete solution to applying Bayes' theorem to a factory "
            "with two machines, A making 70 per cent at a 1 per cent defect rate and B "
            "making 30 per cent at a 4 per cent defect rate.",
            "P(defective) = 0.70(0.01) + 0.30(0.04) = 0.019; P(B ∣ defective) = "
            "0.012/0.019 ≈ 0.632.",
            "Apply the total probability rule, then Bayes' theorem.", "C"),
           ("10.3.4", "Write a complete solution to counting the number of ways to choose a "
            "president, a secretary and a treasurer from 9 people.",
            "9 × 8 × 7 = 504, because the roles are distinct and order matters.",
            "Apply the multiplication principle stage by stage.", "F"),
           ("10.3.5", "Write a complete solution to counting the number of ways to choose 3 "
            "toppings from 8 available.",
            "8!/(3! × 5!) = 56.", "Order does not matter, so use combinations.", "F"),
           ("10.3.6", "Write a complete solution to proving the law of total probability "
            "for a partition of the sample space into B and not B.",
            "P(A) = P(A and B) + P(A and not B) = P(A ∣ B)P(B) + P(A ∣ not B)P(not "
            "B), because B and not B are disjoint and exhaustive.",
            "Split the event A by the partition.", "R"),
           ("10.3.7", "Write a complete solution to the birthday problem for a group of "
            "25, giving the answer to three decimal places.",
            "The complement product is about 0.4313, so the probability of a shared "
            "birthday is 1 − 0.4313 = 0.569.",
            "Compute the product of the no-match probabilities.", "C"),
           ("10.3.8", "Write a complete solution to finding P(A ∣ B) when P(B) = 0.35 "
            "and P(A and B) = 0.14.",
            "P(A ∣ B) = 0.14/0.35 = 0.4.",
            "Divide the joint probability by the conditioning probability.", "F"),
           ("10.3.9", "Write a complete solution to a screening problem: prevalence 5 "
            "per cent, sensitivity 92 per cent, false-positive rate 6 per "
            "cent. Find P(disease ∣ positive).",
            "Out of 10 000 people: 460 true positives and 570 false "
            "positives, so P = 460/1030 ≈ 0.447.",
            "Scale to whole numbers and divide by the total positives.", "R"),
           ("10.3.10", "Write a complete solution to applying Bayes' theorem to two "
            "suppliers, X supplying 75 per cent at a 2 per cent fault rate "
            "and Y the rest at 6 per cent.",
            "P(faulty) = 0.75(0.02) + 0.25(0.06) = 0.03; P(Y ∣ faulty) = "
            "0.015/0.03 = 0.5.",
            "Apply the total probability rule, then Bayes' theorem.", "C"),
           ("10.3.11", "Write a complete solution to counting the number of ways to "
            "choose 4 toppings from 11 available.",
            "11!/(4! × 7!) = 330.",
            "Order does not matter, so use combinations.", "F"),
           ("10.3.12", "Write a complete solution to the birthday problem for a group "
            "of 40, to three decimal places.",
            "The complement product is about 0.1088, so the probability of "
            "a shared birthday is 1 − 0.1088 = 0.891.",
            "Compute the product of the no-match probabilities.", "C"),
           ],
        D=[("10.4.1", "A rare disease affects 1 in 5000. A test has sensitivity 99 per cent "
            "and a false-positive rate of 1 per cent. Find P(disease ∣ positive) and "
            "comment on the result.",
            "Out of 500 000 people: 99 true positives and 4990 false positives, so "
            "P = 99/5089 ≈ 0.0195, under 2 per cent.",
            "Scale to whole numbers and divide by the total positives.", "A"),
           ("10.4.2", "A hospital screens 20 000 people for a condition affecting 4 per "
            "cent. The test catches 95 per cent of cases and falsely flags 3 per cent of "
            "the rest. How many true and false positives are there, and what fraction of "
            "positives are genuine?",
            "760 true positives and 576 false positives, so 760/1336 ≈ 0.569 are genuine.",
            "Build the two-way table and divide.", "A"),
           ("10.4.3", "Two factories supply components. Factory X supplies 55 per cent with "
            "a 3 per cent fault rate and factory Y the rest with a 7 per cent rate. A "
            "faulty component is found. Find the probability it came from Y.",
            "P(faulty) = 0.55(0.03) + 0.45(0.07) = 0.048; P(Y ∣ faulty) = "
            "0.0315/0.048 ≈ 0.656.",
            "Apply the total probability rule, then Bayes' theorem.", "A"),
           ("10.4.4", "A security system has two sensors. Sensor A fires with probability "
            "0.8 when there is an intruder and 0.1 otherwise; sensor B fires with "
            "probability 0.9 and 0.2. The system alerts only if both fire. Find the "
            "probability of an alert when there is an intruder and when there is not, "
            "assuming independence given the state.",
            "With an intruder: 0.8 × 0.9 = 0.72. Without: 0.1 × 0.2 = 0.02.",
            "Multiply the conditional probabilities along each branch.", "A"),
           ("10.4.5", "A lottery sells 1 000 000 tickets and 1000 prizes. A player buys 10 "
            "tickets. Find the probability of winning at least one prize, to three decimal "
            "places.",
            "P(no prize) = (999 000/1 000 000)^10 ≈ 0.9900, so P(at least one) ≈ 0.0100.",
            "Use the complement with the probability of losing each ticket.", "A"),
           ("10.4.6", "A student says that because a coin has landed heads five times in a "
            "row, tails is now more likely. Investigate and justify.",
            "False for a fair coin: the tosses are independent, so P(heads) remains 0.5 on "
            "every toss regardless of the past.",
            "Independence means the past does not affect the next outcome.", "R"),
           ("10.4.7", "A doctor tells a patient that a positive result means a 95 per cent "
            "chance of disease. The test has 95 per cent sensitivity and the disease "
            "prevalence is 1 in 200. Evaluate the statement.",
            "Out of 200 000 people: 950 true positives and 9950 false positives, so the "
            "actual probability is 950/10 900 ≈ 0.087, far below 95 per cent. The doctor "
            "has confused P(positive ∣ disease) with P(disease ∣ positive).",
            "Build the table and identify the two conditional probabilities.", "A"),
           ("10.4.8", "A school chooses a committee of 4 from 12 students and 8 staff. Find "
            "the number of committees with at least one student.",
            "Total committees are 20!/(4! × 16!) = 4845; all-staff committees are "
            "8!/(4! × 4!) = 70, so the answer is 4845 − 70 = 4775.",
            "Count the total and subtract the unwanted case.", "A"),
           ("10.4.9", "A password uses 3 letters followed by 2 digits, with repetition "
            "allowed. Find the number of possible passwords.",
            "26³ × 10² = 17 576 × 100 = 1 757 600.",
            "Apply the multiplication principle at each position.", "F"),
           ("10.4.10", "A bag contains 4 red, 5 blue and 6 green counters. Three are drawn "
            "without replacement. Find the probability that all three are the same colour.",
            "(4/15)(3/14)(2/13) + (5/15)(4/14)(3/13) + (6/15)(5/14)(4/13) = "
            "24/2730 + 60/2730 + 120/2730 = 204/2730 ≈ 0.0747.",
            "Sum the three colour cases, each a product of conditional probabilities.",
            "C"),
           ("10.4.11", "A student claims that if two events each have probability 0.5 and "
            "are independent, then their union has probability 1. Investigate and justify.",
            "False: P(A or B) = 0.5 + 0.5 − 0.25 = 0.75, because the overlap of 0.25 must "
            "be subtracted once.",
            "Apply the addition rule with the independence product.", "R"),
           ("10.4.12", "A fair die is rolled until a six appears. Find the probability that "
            "this takes more than 4 rolls.",
            "(5/6)⁴ ≈ 0.482, because the first four rolls must all be non-sixes.",
            "Use the complement and multiply the conditional probabilities.", "C")],
    ),
    assessment=[
        dict(title="A1 · The screening programme",
             text="A disease affects 2 people in 1000. A test has a sensitivity of 98 per "
                  "cent and a false-positive rate of 4 per cent. A screening programme "
                  "tests 50 000 people. Find the number of true positives and false "
                  "positives, the probability that a person with a positive result has the "
                  "disease, and the number of people who would be unnecessarily treated if "
                  "every positive result were treated. Advise the programme.",
             note="Criteria C and D · build the table, compute the predictive value, and "
                  "justify the advice."),
        dict(title="A2 · The two factories",
             text="Factory A supplies 60 per cent of a component with a 1 per cent defect "
                  "rate, and factory B supplies the rest with a 5 per cent rate. A "
                  "defective component is found. Find the probability that it came from "
                  "factory B, and then find the probability that two components drawn at "
                  "random are both defective and from the same factory. Explain each step "
                  "of your reasoning.",
             note="Criteria C and D · apply the total probability rule and Bayes' theorem, "
                  "then combine with independence."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of logic and the related concepts of relationships, "
        "representation and patterns appear in your work?",
        "How is the global context of fairness and development, and its exploration of "
        "risk, screening and fair decisions, visible in the investigations and examples you "
        "completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of a probability as a guide to a decision, and what would "
        "you still like to ask?",
    ],
    review=dict(
        ideas=["A probability is a measure on a stated set of outcomes.",
               "For equally likely outcomes, probability is a count divided by the total.",
               "The addition rule is P(A or B) = P(A) + P(B) − P(A and B).",
               "Conditional probability is P(A ∣ B) = P(A and B)/P(B).",
               "Independence means P(A and B) = P(A)P(B).",
               "Mutually exclusive events are independent only in the trivial case.",
               "The law of total probability sums the contributions over a partition.",
               "Bayes' theorem reverses the conditioning.",
               "The multiplication principle multiplies the numbers of choices at each "
               "stage.",
               "Permutations count order; combinations do not."],
        vocab=["sample space", "event", "outcome", "equally likely", "union", "intersection",
               "complement", "mutually exclusive", "conditional probability", "independent",
               "tree diagram", "law of total probability", "Bayes' theorem", "sensitivity",
               "specificity", "prevalence", "permutation", "combination", "factorial"],
        mixed=[("10.R1", "P(A) = 0.3, P(B) = 0.5 and P(A and B) = 0.1. Find P(A ∣ B)."),
               ("10.R2", "Two dice are rolled. Find P(total is 7)."),
               ("10.R3", "How many ways can 5 people be seated in a row of 5 chairs?"),
               ("10.R4", "How many ways can 3 cards be chosen from 10?"),
               ("10.R5", "A disease affects 1 in 100. A test is 90 per cent sensitive with "
                "a 10 per cent false-positive rate. Find P(disease ∣ positive)."),
               ("10.R6", "Explain the difference between P(A ∣ B) and P(B ∣ A) in "
                "the context of a screening test.")],
    ),
    projects=dict(
        service=[("Community need", "Screening and risk claims in the community are "
                                    "published without the prevalence or the false-positive "
                                    "rate."),
                 ("Mathematical connection", "Conditional probability and counting."),
                 ("Proposed action", "Take one published screening claim, rebuild the "
                                     "two-way table, and publish what a positive result "
                                     "actually means."),
                 ("Expected impact", "Readers can judge a positive result for themselves."),
                 ("Student reflection", "Record the claim, the table and the predictive "
                                        "value.")],
        community=[("Project idea", "A probability audit of a school or club lottery."),
                   ("Need", "Participants believe their chance of winning is far higher "
                            "than it is."),
                   ("Research question", "What is the actual probability of each prize, and "
                                         "how does it change with the number of tickets "
                                         "bought?"),
                   ("Mathematics", "Counting, permutations and combinations."),
                   ("Action or outcome", "A one-page probability table with the counting "
                                         "shown."),
                   ("Beneficiaries", "Everyone who enters the lottery."),
                   ("Evidence", "The table and the counts behind it.")],
        personal=[("Personal interest", "Games, sport, weather or health."),
                  ("Learning goal", "To compute a probability you rely on and state the set "
                                    "it is measured on."),
                  ("Product or outcome", "A probability card with the set and the rule "
                                         "named."),
                  ("Mathematics", "Conditional probability and counting."),
                  ("Process", "Name the set, count the outcomes, and state the rule."),
                  ("Evidence", "The card and the counting behind it.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=11, title="Capstone: A Mathematical Modelling Project",
    key="Relationships", related=["Change", "Representation", "System"],
    context="Globalization and sustainability",
    exploration="decisions about shared resources, access and long-term cost",
    inquiry=("A mathematical model is an argument about the world: its value depends as much "
             "on the assumptions it makes and the evidence it ignores as on the accuracy of "
             "its arithmetic."),
    atl=("Critical thinking",
         "In order for a student to defend a model of a shared resource, students must state "
         "its assumptions, test it against data, and justify which evidence it leaves out and "
         "why."),
    standfirst="A capstone project applies the whole of the course to a real decision. The "
               "mathematics is only part of the work: naming the problem, stating the "
               "assumptions and defending the model are the rest.",
    engage="A school is deciding whether to install a water tank. The tank costs money, saves "
           "money, and takes up space. Three students build three models and reach three "
           "different conclusions from the same arithmetic. What went wrong?",
    questions=[("Factual", "What are the stages of the modelling cycle, and what is produced "
                           "at each?"),
               ("Conceptual", "Why can two correct models of the same situation give "
                              "different recommendations?"),
               ("Debatable", "Is a model that ignores an important factor more or less "
                             "honest than one that includes it approximately?")],
    application_lede="These tasks build and evaluate models. State the assumptions, test the "
                     "model against data, and report the sensitivity of the conclusion to "
                     "each assumption.",
    projects_lede="A model is an argument. Name the assumptions, the evidence and the "
                  "limits, and defend the conclusion against the strongest objection.",
    sections=[
        dict(id="11.1", title="The modelling cycle",
             inquiry_q="What are the stages of a modelling project, and what does each "
                       "produce?",
             teach=[
                 "The modelling cycle has five stages: define the problem, make assumptions, build the model, test and evaluate it, and report the result. Each stage produces something specific, and skipping one leaves a gap that shows up later.",
                 "The first stage defines the variables, the units, the quantity to be optimised or predicted, and the audience for the answer. A problem that has not been defined cannot be solved, however good the mathematics.",
                 "Assumptions are the bridge between the situation and the mathematics, and every one of them is a choice that can be challenged. Listing them explicitly is what allows a reader to disagree with a specific claim rather than with the whole model.",
                 "Testing compares the model's predictions with data, and evaluation reports where the model fails. A model that has never failed a test has not been tested, and a model that has not been evaluated has not been finished.",
             ], examples=[
                 dict(q="A school models the cost of running a bus service. List the "
                        "variables, the units and the assumptions a first model would need.",
                      vis=F("table", [["stage", "what is produced", "example for the bus"],
                                      ["define", "variables and units", "cost per week in "
                                       "currency units, distance in km"],
                                      ["assume", "a list of simplifications", "constant fuel "
                                       "price, no maintenance, fixed route"],
                                      ["build", "a formula", "C = 50 + 1.2d"],
                                      ["test", "a comparison with data", "compare with three "
                                       "past invoices"],
                                      ["report", "a recommendation with limits", "the model "
                                       "ignores driver overtime"]],
                            caption="Each stage produces a specific artefact."),
                      reasoning="Work through the stages in order and name the output of "
                               "each.",
                      steps=["Define: the quantity is the weekly cost, the variables are the "
                             "distance and the number of services, and the units are currency "
                             "units and kilometres.",
                             "Assume: the fuel price is constant, the route is fixed, and "
                             "maintenance is ignored in a first model.",
                             "Build: the cost is a fixed part plus a part proportional to "
                             "distance, so C = 50 + 1.2d.",
                             "Test: compare the model's predictions with three past "
                             "invoices.",
                             "Report: give the recommendation and state that the model "
                             "ignores driver overtime and maintenance."],
                      ans="variables, units, assumptions, formula, test and report, each "
                          "named",
                      interp="The list of assumptions is the part that lets a reader "
                             "challenge a specific claim rather than the whole model."),
                 dict(q="Two students model the same bus service and reach different "
                        "conclusions. One included a term for maintenance and one did not. "
                        "Explain how both can be correct.",
                      vis=F("table", [["model", "formula", "assumption", "conclusion"],
                                      ["student 1", "C = 50 + 1.2d", "no maintenance",
                                       "cheaper"],
                                      ["student 2", "C = 50 + 1.2d + 0.3d", "maintenance "
                                       "proportional to distance", "dearer"],
                                      ["difference", "the maintenance term", "—", "—"]],
                            caption="The difference is an assumption, not an error."),
                      reasoning="Identify the assumption that differs and trace its effect "
                               "on the conclusion.",
                      steps=["Both students used correct arithmetic on the same data.",
                             "Student 1 assumed no maintenance cost; student 2 assumed "
                             "maintenance proportional to distance.",
                             "The second model has an extra term, 0.3d, which student 1 "
                             "omitted.",
                             "So the two models make different predictions, and both are "
                             "internally correct.",
                             "The disagreement is about an assumption, and it is settled by "
                             "evidence about maintenance, not by arithmetic."],
                      ans="the two models differ in an assumption, so both can be correct",
                      interp="This is the inquiry statement in action: the value of a model "
                             "depends on its assumptions, not only on its arithmetic."),
             ], inv=dict(
                 task="Choose a decision in your school or community that involves a cost "
                      "over time. Work through the five stages of the modelling cycle, "
                      "producing an artefact at each stage. Then find a second model of the "
                      "same decision that differs from yours in exactly one assumption, and "
                      "explain how the conclusion changes.",
                 table=[["stage", "artefact produced", "what it commits you to"],
                        ["define", "variables, units, audience", "what is being optimised"],
                        ["assume", "a list of five simplifications", "each is challengeable"],
                        ["build", "a formula with named parameters", "the parameters are "
                         "estimates"],
                        ["test", "a comparison with three data points", "the size of the "
                         "error"],
                        ["report", "a recommendation with limits", "what the model ignores"]],
                 notice=["Defining the problem first made the rest of the work easier, "
                         "because the variables were fixed.",
                         "Listing five assumptions exposed two that were doing most of the "
                         "work.",
                         "Testing against three data points showed an error of about 8 per "
                         "cent, which set the confidence in the recommendation.",
                         "Changing one assumption moved the conclusion, which showed how "
                         "sensitive the answer was."],
                 obs="Each stage of the cycle produces an artefact, and the artefacts are "
                     "what a reader examines.",
                 concl="The modelling cycle runs from defining the problem, through "
                       "assumptions and building, to testing and reporting, and each stage "
                       "produces a specific artefact. Two models of the same situation can "
                       "both be correct and reach different conclusions when they differ in "
                       "an assumption, and the disagreement is settled by evidence about "
                       "that assumption.")),
        dict(id="11.2", title="Defining the problem",
             inquiry_q="What has to be settled before any mathematics is done?",
             teach=[
                 "A problem definition names the decision to be made, the quantity to be optimised or predicted, the variables with their units, and the constraints. Anything not named is assumed, and an unstated assumption is an undefended one.",
                 "The quantity to be optimised is a choice, and different choices lead to different models. Minimising cost and maximising access describe different relationships between the resources, and a model built for one does not answer the other.",
                 "Constraints come from the limits of the situation, and each becomes an inequality in the model. A constraint that is not stated is a constraint that has been assumed away, which is the commonest reason a model fails in practice.",
                 "The audience for the answer decides the form of the report. A recommendation to a school council is stated in the council's terms, with the limits named, and not in the terms of the calculation that produced it.",
             ], examples=[
                 dict(q="Define the problem of deciding whether a school should install a "
                        "water tank, naming the decision, the objective, the variables and "
                        "the constraints.",
                      vis=F("table", [["element", "statement", "why it matters"],
                                      ["decision", "install or not", "defines the "
                                       "recommendation"],
                                      ["objective", "minimise the total cost over 10 "
                                       "years", "fixes what is optimised"],
                                      ["variables", "tank volume in litres, cost in "
                                       "currency units", "fixes the units"],
                                      ["constraints", "roof area, budget, space", "each is a "
                                       "limit"],
                                      ["audience", "the school council", "sets the form of "
                                       "the report"]],
                            caption="A definition has five named parts."),
                      reasoning="Name each part of the definition and state why it matters.",
                      steps=["The decision is whether to install a tank of a given size.",
                             "The objective is to minimise the total cost over ten years, "
                             "counting the purchase, the installation and the water saved.",
                             "The variables are the tank volume in litres and every cost in "
                             "currency units per year.",
                             "The constraints are the available roof area, the budget and "
                             "the space on the site.",
                             "The audience is the school council, so the report is in "
                             "currency units and years, with the limits named."],
                      ans="decision, objective, variables, constraints and audience all "
                          "named",
                      interp="The definition is a contract: it fixes what the model will "
                             "and will not answer."),
                 dict(q="A student's model of the tank ignores the rainfall pattern because "
                        "no local data were available. Evaluate the model.",
                      vis=F("table", [["aspect", "assessment"],
                                      ["what the model does", "computes cost from tank "
                                       "volume"],
                                      ["what it omits", "the rainfall pattern, which "
                                       "determines the saving"],
                                      ["effect on the conclusion", "the saving is "
                                       "unreliable, so the recommendation is unsafe"],
                                      ["what would fix it", "local rainfall data, or a "
                                       "stated range"],
                                      ["honest report", "gives the recommendation with the "
                                       "omission named"]],
                            caption="An omission is part of the model's value."),
                      reasoning="Identify the omission, trace its effect, and state what "
                               "would repair it.",
                      steps=["The model computes cost from tank volume but omits rainfall.",
                             "Rainfall determines how much water the tank actually collects, "
                             "so it determines the saving.",
                             "Without it, the saving is an estimate with an unknown error, "
                             "and the recommendation is unsafe.",
                             "The repair is local rainfall data, or a stated range of "
                             "rainfall with the recommendation for each.",
                             "The honest report names the omission and gives the "
                             "recommendation as conditional on it."],
                      ans="the omission makes the recommendation unsafe, and it must be "
                          "named",
                      interp="An ignored factor is part of the model's value, which is the "
                             "second half of the inquiry statement."),
             ], inv=dict(
                 task="Take a real decision in your community that involves a cost over "
                      "time. Write a full problem definition with the five named parts. Then "
                      "list three factors the situation involves that your definition "
                      "excludes, and for each state the effect on the conclusion and what "
                      "data would repair it.",
                 table=[["part of the definition", "statement"],
                        ["decision", "whether to install solar panels on the school roof"],
                        ["objective", "minimise the total cost over 15 years"],
                        ["variables", "installed capacity in kW, costs in currency units per "
                         "year"],
                        ["constraints", "roof area, budget, structural limits"],
                        ["audience", "the school council"],
                        ["excluded factor 1", "the future price of electricity, which "
                         "changes the saving"],
                        ["excluded factor 2", "panel degradation, which lowers output over "
                         "time"],
                        ["excluded factor 3", "the resale value at the end of the term"]],
                 notice=["Naming the objective first showed that a different objective, "
                         "such as maximising carbon saving, would give a different answer.",
                         "Each excluded factor changed the saving, not the cost, so the "
                         "conclusion was sensitive to all three.",
                         "Two of the three could be repaired with published data.",
                         "The third, the resale value, had no reliable data and had to be "
                         "left as a stated range."],
                 obs="A definition fixes what the model will answer, and the excluded "
                     "factors set the limits of the answer.",
                 concl="A problem definition names the decision, the objective, the "
                       "variables with units, the constraints and the audience, and anything "
                       "not named is an unstated assumption. Excluded factors are part of "
                       "the model's value: each one limits the conclusion, and the honest "
                       "report names them and says what data would repair them.")),
        dict(id="11.3", title="Building and testing a model",
             inquiry_q="How is a model built, and how is it shown to work?",
             teach=[
                 "A model is built by choosing a mathematical form for each relationship, fitting its parameters to data, and combining the parts into a system. The form is chosen for simplicity first, and complexity is added only when the data demand it.",
                 "Testing compares the model's predictions with data that were not used to fit it. A model that predicts new data well is useful; one that only reproduces the data it was fitted to has learned nothing.",
                 "A sensitivity analysis varies each parameter and reports the effect on the conclusion. The parameters with the largest effect are the ones that most need better data, and the sensitivity report says where the effort should go.",
                 "A model is tested by attempting to break it: with extreme values, with values outside the fitted range, and against known special cases. A model that survives these is ready to report; one that does not needs repair.",
             ], examples=[
                 dict(q="A model for the tank's saving is S = 0.002rV, where r is the annual "
                        "rainfall in millimetres and V the tank volume in litres. Test it "
                        "against r = 800, V = 5000 and a measured saving of 7800 currency "
                        "units.",
                      vis=F("table", [["step", "working", "result"],
                                      ["model prediction", "0.002 × 800 × 5000", "8000"],
                                      ["measured", "—", "7800"],
                                      ["error", "8000 − 7800", "200"],
                                      ["relative error", "200 ÷ 7800", "0.0256"],
                                      ["verdict", "within 3 per cent", "acceptable"]],
                            caption="The error is expressed relative to the measurement."),
                      reasoning="Compute the prediction, the error and the relative error.",
                      steps=["The model predicts S = 0.002 × 800 × 5000 = 8000.",
                             "The measured saving is 7800.",
                             "The absolute error is 8000 − 7800 = 200.",
                             "The relative error is 200/7800 ≈ 0.0256, about 2.6 per cent.",
                             "An error under 3 per cent is acceptable for a planning model, "
                             "so the model passes this test."],
                      ans="the model predicts 8000 against a measured 7800, an error of about "
                          "2.6 per cent",
                      interp="The relative error is the useful measure, because it says "
                             "whether the error matters for the decision."),
                 dict(q="In the same model, find the sensitivity of the saving to the "
                        "rainfall when r changes from 800 to 900.",
                      vis=F("table", [["rainfall", "saving", "change"],
                                      ["800", "8000", "—"],
                                      ["900", "9000", "+1000"],
                                      ["relative change", "1000 ÷ 8000", "0.125"],
                                      ["verdict", "a 12.5 per cent rise in the saving", "high "
                                       "sensitivity"]],
                            caption="The saving is proportional to the rainfall."),
                      reasoning="Compute the change in the saving and express it relatively.",
                      steps=["At r = 800 the saving is 8000, and at r = 900 it is 9000.",
                             "The change is 1000, which is 12.5 per cent of 8000.",
                             "Since the model is linear in r, the relative change in the "
                             "saving equals the relative change in the rainfall.",
                             "A 12.5 per cent rise in rainfall gives a 12.5 per cent rise in "
                             "the saving, so the model is highly sensitive to rainfall.",
                             "This means the rainfall data matter more than any other "
                             "input."],
                      ans="a 12.5 per cent change in the saving for a 12.5 per cent change "
                          "in rainfall",
                      interp="The sensitivity analysis says where to spend effort on better "
                             "data, and here it is unambiguously the rainfall."),
             ], inv=dict(
                 task="Build a model for a decision of your own with at least three "
                      "parameters. Fit it to three data points, test it against a fourth, "
                      "and then carry out a sensitivity analysis on each parameter, "
                      "reporting the percentage change in the conclusion for a 10 per cent "
                      "change in each.",
                 table=[["parameter", "10 per cent change", "change in the conclusion",
                                "rank"],
                        ["unit price", "+10 per cent", "+10 per cent", "1"],
                        ["usage", "+10 per cent", "+8 per cent", "2"],
                        ["discount rate", "+10 per cent", "+2 per cent", "3"],
                        ["lifetime", "+10 per cent", "−6 per cent", "2"]],
                 notice=["The unit price was the most sensitive parameter, so its data "
                         "mattered most.",
                         "The usage and the lifetime had comparable effects, in opposite "
                         "directions.",
                         "The discount rate had the smallest effect, so its estimate could "
                         "be crude.",
                         "Testing against the fourth data point gave an error of 6 per cent, "
                         "consistent with the sensitivity ranking."],
                 obs="A sensitivity analysis ranks the parameters by their effect on the "
                     "conclusion, and the ranking says where better data are needed.",
                 concl="A model is built by choosing a form for each relationship and "
                       "fitting its parameters, and it is tested against data not used in "
                       "the fit. The relative error says whether the model is good enough, "
                       "and a sensitivity analysis ranks the parameters by their effect on "
                       "the conclusion. Here the unit price was the most sensitive "
                       "parameter.")),
        dict(id="11.4", title="Optimising and evaluating",
             inquiry_q="How is a model's recommendation chosen and defended?",
             teach=[
                 "When a model has a linear objective and linear constraints, the optimum is found at a vertex of the feasible region. When the objective is non-linear, the optimum is found numerically and reported with the interval that contains it.",
                 "An optimal recommendation is a point, a value and a justification that the point is feasible. The value alone is not a recommendation, because it does not say what to do.",
                 "Evaluation compares the model's recommendation with what a decision-maker would do without it. If the model adds nothing, it has failed, and the reason should be reported.",
                 "Robustness asks whether the recommendation survives reasonable changes in the parameters. A recommendation that reverses under a 10 per cent change in one input is not a recommendation but a coin toss, and it must be reported as such.",
             ], examples=[
                 dict(q="A model of a community garden gives a profit of P = 40x + 30y "
                        "subject to x + 2y ≤ 12, 2x + y ≤ 12, x ≥ 0 and y ≥ 0. Find the "
                        "optimal plan and test its robustness to a 10 per cent fall in the "
                        "profit from x.",
                      vis=F("table", [["vertex", "coordinates", "P = 40x + 30y"],
                                      ["(0, 0)", "(0, 0)", "0"],
                                      ["6, 0)", "(6, 0)", "240"],
                                      ["(4, 4)", "(4, 4)", "280"],
                                      ["(0, 6)", "(0, 6)", "180"]],
                            caption="The optimum is at the intersection of both "
                                    "constraints."),
                      reasoning="Evaluate the objective at the vertices, then perturb the "
                               "profit from x.",
                      steps=["The vertices are (0, 0), (6, 0), (4, 4) and (0, 6).",
                             "Evaluating P gives 0, 240, 280 and 180, so the optimum is "
                             "(4, 4) with P = 280.",
                             "If the profit from x falls by 10 per cent to 36, then "
                             "P(4, 4) = 36(4) + 30(4) = 264.",
                             "The other vertices give 216 and 180, so (4, 4) is still "
                             "optimal.",
                             "The recommendation is therefore robust to a 10 per cent fall "
                             "in the profit from x."],
                      ans="optimal plan (4, 4) with profit 280, robust to a 10 per cent "
                          "fall in the profit from x",
                      interp="The robustness test is part of the recommendation, because it "
                             "says how much the conclusion can be trusted."),
                 dict(q="A model recommends a plan that a gardener rejects because it "
                        "ignores the volunteers' availability. Evaluate the model.",
                      vis=F("table", [["aspect", "assessment"],
                                      ["what the model does", "optimises profit subject to "
                                       "land and money"],
                                      ["what it omits", "volunteer availability, which "
                                       "caps the labour"],
                                      ["effect", "the recommended plan needs more labour "
                                       "than exists"],
                                      ["verdict", "the model is not wrong but is "
                                       "incomplete"],
                                      ["repair", "add the labour constraint and re-solve"]],
                            caption="An omitted constraint can invalidate a plan."),
                      reasoning="Identify the omission, trace its effect, and state the "
                               "repair.",
                      steps=["The model optimises profit subject to land and money only.",
                             "It omits volunteer availability, which caps the labour "
                             "available.",
                             "The recommended plan needs more labour than the volunteers "
                             "can supply, so it cannot be carried out.",
                             "The model is not wrong in its arithmetic, but it is "
                             "incomplete, and an incomplete model can recommend an "
                             "impossible plan.",
                             "The repair is to add the labour constraint and solve again."],
                      ans="the model is incomplete; adding the labour constraint repairs it",
                      interp="An omitted constraint is more dangerous than an omitted cost, "
                             "because it can make the recommendation impossible rather than "
                             "merely inaccurate."),
             ], inv=dict(
                 task="Take a model you have built and optimise it. Report the optimal "
                      "point, the optimal value and the feasibility check. Then test the "
                      "robustness of the recommendation to a 10 per cent change in each "
                      "parameter, and state whether the recommendation survives.",
                 table=[["parameter", "10 per cent change", "recommendation survives?",
                                "new optimal value"],
                        ["profit from x", "+10 per cent", "yes", "300"],
                        ["profit from y", "+10 per cent", "yes", "280"],
                        ["resource 1", "+10 per cent", "yes", "300"],
                        ["resource 2", "−10 per cent", "yes", "260"],
                        ["all together", "as above", "yes", "the plan is unchanged"]],
                 notice=["The optimal plan did not change under any single 10 per cent "
                         "perturbation.",
                         "The optimal value changed by up to about 7 per cent.",
                         "The most sensitive parameter was the profit from x, as the "
                         "earlier sensitivity analysis had predicted.",
                         "The recommendation was therefore robust, and this was reported "
                         "with the value range."],
                 obs="A recommendation is a point, a value and a robustness statement, and "
                     "all three are needed.",
                 concl="A recommendation from a model is the optimal point, the optimal "
                       "value and the justification that the point is feasible, together "
                       "with a robustness statement. A recommendation that reverses under a "
                       "reasonable change in a parameter is not a recommendation. Here the "
                       "plan survived every single perturbation, with the value ranging "
                       "from 260 to 300.")),
        dict(id="11.5", title="Presenting and defending",
             inquiry_q="What does a defensible report contain?",
             teach=[
                 "A modelling report states the problem, the assumptions, the model, the test results, the recommendation and the limits, in that order. This representation of the work is the argument, and each section answers the question the previous one raises.",
                 "A defence is a response to the strongest objection, not a summary of the work. Anticipating the objection and answering it is what makes a report defensible, and the objection is usually about an assumption.",
                 "Every claim in a report is traceable either to a calculation or to a stated assumption. A claim that is neither is removed, because it cannot be defended.",
                 "The audience decides the level of detail. A council needs the recommendation, the limits and one number each for the cost and the benefit; a mathematics audience needs the model and its test.",
             ], examples=[
                 dict(q="Write the structure of a report on the water-tank decision, naming "
                        "what each section contains.",
                      vis=F("table", [["section", "contents", "answers"],
                                      ["problem", "the decision and the objective", "what is "
                                       "being decided"],
                                      ["assumptions", "the five simplifications", "what the "
                                       "model takes for granted"],
                                      ["model", "the formula and its parameters", "how the "
                                       "conclusion is computed"],
                                      ["test", "the error against four data points", "how "
                                       "well it works"],
                                      ["recommendation", "the plan and the value", "what to "
                                       "do"],
                                      ["limits", "what the model omits", "what could go "
                                       "wrong"]],
                            caption="The order is the argument."),
                      reasoning="Name the sections in order and state what each answers.",
                      steps=["The problem section states the decision and the objective.",
                             "The assumptions section lists the five simplifications, so a "
                             "reader can challenge one specifically.",
                             "The model section gives the formula and its parameters, with "
                             "the source of each.",
                             "The test section gives the error against four data points.",
                             "The recommendation gives the plan and the value, and the "
                             "limits section names what the model omits."],
                      ans="problem, assumptions, model, test, recommendation and limits, in "
                          "that order",
                      interp="Each section answers the question the previous one raises, "
                             "which is why the order matters."),
                 dict(q="A reviewer objects that the tank model assumes a constant water "
                        "price, which has risen 8 per cent a year for a decade. Write the "
                        "defence.",
                      vis=F("table", [["step", "content"],
                                      ["restate the objection", "the water price is assumed "
                                       "constant"],
                                      ["concede", "the assumption is optimistic"],
                                      ["quantify", "at 8 per cent a year the saving is "
                                       "understated by about 40 per cent over ten years"],
                                      ["consequence", "the recommendation is unchanged, and "
                                       "the saving is larger than reported"],
                                      ["repair", "model the price rise and report both"]],
                            caption="A defence concedes, quantifies and repairs."),
                      reasoning="Restate the objection, concede what is true, quantify the "
                               "effect, and state the repair.",
                      steps=["The objection is that the model assumes a constant water "
                             "price.",
                             "This is conceded: the price has in fact risen about 8 per cent "
                             "a year.",
                             "The effect is quantified: over ten years the saving is "
                             "understated by about 40 per cent.",
                             "The consequence is that the recommendation is unchanged, and "
                             "the reported saving is too small.",
                             "The repair is to model the price rise explicitly and report "
                             "both figures."],
                      ans="the objection is conceded, quantified and repaired, and the "
                          "recommendation survives",
                      interp="A defence that concedes and quantifies is stronger than one "
                             "that denies, because it shows the objection was understood."),
             ], inv=dict(
                 task="Write a full report on a model you have built, with the six sections "
                      "in order. Then find the strongest objection a reader could make and "
                      "write a defence of it in five steps: restate, concede, quantify, "
                      "state the consequence, and repair.",
                 table=[["section", "length", "what it contains"],
                        ["problem", "half a page", "the decision and the objective"],
                        ["assumptions", "half a page", "five numbered simplifications"],
                        ["model", "one page", "the formula, the parameters and their "
                         "sources"],
                        ["test", "half a page", "the error against four data points"],
                        ["recommendation", "half a page", "the plan, the value and the "
                         "robustness"],
                        ["limits", "half a page", "what the model omits and the effect of "
                         "each"],
                        ["defence", "half a page", "restate, concede, quantify, consequence, "
                         "repair"]],
                 notice=["Writing the assumptions section first made the rest easier, "
                         "because the challenges were already visible.",
                         "The strongest objection was about the assumption with the largest "
                         "sensitivity, which the earlier analysis had identified.",
                         "Quantifying the objection showed it did not change the "
                         "recommendation, only the size of the benefit.",
                         "The report was about four pages, which was the right length for "
                         "the audience."],
                 obs="A report is an argument with a fixed order, and a defence answers the "
                     "strongest objection in five steps.",
                 concl="A modelling report states the problem, the assumptions, the model, "
                       "the test results, the recommendation and the limits, in that order, "
                       "and each section answers the question the previous one raises. A "
                       "defence restates the strongest objection, concedes what is true, "
                       "quantifies the effect, states the consequence and gives the "
                       "repair.")),
        dict(id="11.6", title="The capstone project brief",
             inquiry_q="What must a capstone project contain?",
             teach=[
                 "The capstone project is an extended piece of work on a real decision, and it must contain all six elements of a modelling report together with the evidence behind them. The evidence is what distinguishes a project from an essay.",
                 "The project is assessed on the mathematics, on the quality of the assumptions, on the testing, and on the communication. A project with excellent arithmetic and unstated assumptions scores badly, because the assumptions are the model.",
                 "Every number in a project is either computed, measured or estimated, and its status is stated. An estimate with no stated basis is a guess, and a guess cannot be defended.",
                 "The project ends with a reflection on what the model could not answer. That reflection is the most valuable part of the work, because it is what transfers to the next problem.",
             ], examples=[
                 dict(q="List the required elements of a capstone project and the evidence "
                        "each needs.",
                      vis=F("table", [["element", "required evidence"],
                                      ["problem definition", "the decision, the objective, "
                                       "the variables and the constraints"],
                                      ["assumptions", "a numbered list with the reason for "
                                       "each"],
                                      ["model", "the formula, the parameters and the source "
                                       "of each"],
                                      ["test", "the comparison with data and the error"],
                                      ["recommendation", "the plan, the value and the "
                                       "robustness"],
                                      ["limits and reflection", "what the model omits and "
                                       "what could not be answered"]],
                            caption="Each element has its own evidence."),
                      reasoning="List the elements and state the evidence each requires.",
                      steps=["The problem definition needs the decision, the objective, the "
                             "variables and the constraints, all named.",
                             "The assumptions need to be a numbered list with a reason for "
                             "each, so a reader can challenge one specifically.",
                             "The model needs the formula, the parameters and the source of "
                             "each parameter.",
                             "The test needs the comparison with data and the resulting "
                             "error.",
                             "The recommendation needs the plan, the value and the "
                             "robustness, and the limits and reflection need what the model "
                             "omits."],
                      ans="six elements, each with its required evidence",
                      interp="The evidence is what distinguishes a project from an essay, "
                             "and it is what is assessed."),
                 dict(q="A student's project has excellent arithmetic but no stated "
                        "assumptions. Evaluate it against the capstone requirements.",
                      vis=F("table", [["criterion", "assessment", "consequence"],
                                      ["mathematics", "excellent", "full credit"],
                                      ["assumptions", "absent", "major loss of credit"],
                                      ["testing", "absent", "major loss of credit"],
                                      ["communication", "clear but undefended", "partial "
                                       "credit"],
                                      ["overall", "fails the capstone requirements", "—"]],
                            caption="Missing assumptions cost more than weak arithmetic."),
                      reasoning="Assess each criterion and state the consequence of the "
                               "omissions.",
                      steps=["The mathematics is excellent, so that criterion earns full "
                             "credit.",
                             "But the assumptions are absent, so the reader cannot "
                             "challenge any specific claim.",
                             "The testing is absent too, so there is no evidence the model "
                             "works.",
                             "The communication is clear but undefended, which earns only "
                             "partial credit.",
                             "The project fails the capstone requirements, because the "
                             "assumptions are the model."],
                      ans="the project fails the requirements despite excellent arithmetic",
                      interp="This is the inquiry statement applied to assessment: the value "
                             "of a model depends on its assumptions, not only on its "
                             "arithmetic."),
             ], inv=dict(
                 task="Plan your capstone project. Choose a real decision, write the "
                      "problem definition, list the assumptions you expect to make, name "
                      "the data you will need and where you will get it, and write the "
                      "reflection you expect to end with. Present the plan to a peer and "
                      "record the strongest objection they raise.",
                 table=[["element", "planned content", "evidence needed"],
                        ["decision", "whether to install a water tank", "the school's water "
                         "bills"],
                        ["objective", "minimise the ten-year total cost", "the tank and "
                         "installation prices"],
                        ["assumptions", "constant water price, constant rainfall, no "
                         "maintenance", "local rainfall and price data"],
                        ["data needed", "rainfall, water price, roof area, tank prices",
                         "the school and the national weather service"],
                        ["peer objection", "the model ignores the maintenance cost", "a "
                         "maintenance estimate"],
                        ["expected reflection", "the model cannot answer whether the tank "
                         "is the best use of the money", "—"]],
                 notice=["Choosing the decision first made the data needs obvious.",
                         "Listing the assumptions before collecting data showed which data "
                         "actually mattered.",
                         "The peer objection matched the most sensitive parameter, which "
                         "the plan had already identified.",
                         "The expected reflection named something the model could not "
                         "answer, which is the most transferable part of the work."],
                 obs="A capstone plan is a problem definition, an assumption list, a data "
                     "list and an expected reflection, tested against a peer's objection.",
                 concl="A capstone project contains a problem definition, a numbered list "
                       "of assumptions, a model with sourced parameters, a test against "
                       "data, a recommendation with a robustness statement, and a "
                       "reflection on what the model could not answer. The evidence behind "
                       "each element is what distinguishes a project from an essay, and the "
                       "assumptions are assessed as heavily as the arithmetic.")),
    ],
    practice=dict(
        A=[("11.1.1", "Name the five stages of the modelling cycle.",
            "Define the problem, make assumptions, build the model, test and evaluate, "
            "report the result.", "The cycle runs from definition to report.", "F"),
           ("11.1.2", "State what a problem definition must name.",
            "The decision, the objective, the variables with units, the constraints and the "
            "audience.", "Anything not named is an unstated assumption.", "F"),
           ("11.1.3", "Explain why a model's assumptions are listed explicitly.",
            "So that a reader can challenge a specific claim rather than the whole model, "
            "and so the model's limits are visible.", "An unstated assumption is an "
            "undefended one.", "R"),
           ("11.1.4", "A model is tested against data. State the two kinds of data and why "
            "they differ.",
            "Fitting data, used to choose the parameters, and test data, not used in the "
            "fit, which show whether the model predicts.", "A model that only reproduces "
            "its fitting data has learned nothing.", "R"),
           ("11.1.5", "State what a sensitivity analysis reports.",
            "The percentage change in the conclusion for a stated percentage change in each "
            "parameter, ranked by size.", "The ranking says where better data are needed.",
            "R"),
           ("11.1.6", "A model omits a constraint rather than a cost. Explain why this is "
            "more serious.",
            "Because an omitted cost makes the recommendation inaccurate, while an omitted "
            "constraint can make it impossible to carry out.",
            "A constraint is a limit on what is feasible.", "R"),
           ("11.1.7", "State the three parts of a recommendation from a linear program.",
            "The optimal point, the optimal value, and the justification that the point is "
            "feasible.", "The value alone is not a recommendation.", "F"),
           ("11.1.8", "Explain what a robustness test adds to a recommendation.",
            "It says whether the recommendation survives reasonable changes in the "
            "parameters, which is how much the conclusion can be trusted.",
            "A recommendation that reverses under a small change is a coin toss.", "R"),
           ("11.1.9", "State the order of the six sections of a modelling report.",
            "Problem, assumptions, model, test, recommendation, limits.",
            "The order is the argument.", "F"),
           ("11.1.10", "Name the five steps of a defence of a model.",
            "Restate the objection, concede what is true, quantify the effect, state the "
            "consequence, give the repair.", "A defence that concedes is stronger than one "
            "that denies.", "F"),
           ("11.1.11", "Explain why an estimate in a report must state its basis.",
            "Because an estimate with no stated basis is a guess, and a guess cannot be "
            "defended or challenged.", "Every number is computed, measured or estimated.",
            "R"),
           ("11.1.12", "State what the final reflection of a capstone project should "
            "address.",
            "What the model could not answer, and what would be needed to answer it.",
            "The reflection is the most transferable part of the work.", "R")],
        B=[("11.2.1", "Investigate the effect of changing the objective in a model of your "
            "own, and justify the change in the recommendation.",
            "Changing from minimising cost to maximising access moved the recommendation "
            "from a small, cheap plan to a larger, dearer one, because the objective "
            "function changed.",
            "Re-solve with the new objective and compare.", "C"),
           ("11.2.2", "Conjecture a rule for which assumptions most affect a model's "
            "conclusion, and test it on two models.",
            "The assumptions attached to the most sensitive parameters, which the "
            "sensitivity analysis identifies; in both test models the assumption about the "
            "most sensitive parameter dominated.",
            "Rank the assumptions by the sensitivity of their parameters.", "C"),
           ("11.2.3", "Investigate whether a model with more assumptions is always better "
            "than one with fewer, and justify.",
            "No: a model with more assumptions is more detailed but also more fragile, "
            "because each assumption can be challenged and each adds an error.",
            "Compare the predictions of a simple and a detailed model against the same "
            "data.", "R"),
           ("11.2.4", "Take a published model of a real decision and identify three "
            "assumptions it makes, justifying each.",
            "For a published transport model: constant travel demand, no new "
            "infrastructure, and unchanged fuel prices, each visible in the report's "
            "stated inputs.",
            "Look for the inputs the model holds fixed.", "R"),
           ("11.2.5", "Investigate the effect of the choice of time horizon on a model's "
            "recommendation, and justify.",
            "A longer horizon favours plans with higher initial cost and lower running "
            "cost, because the running cost is saved for longer; a shorter horizon reverses "
            "the ranking.",
            "Re-solve with two horizons and compare.", "R"),
           ("11.2.6", "Conjecture a rule for when a linear model is adequate for a "
            "modelling project, and test it.",
            "When the relationships are approximately proportional over the range of "
            "interest and the errors are small compared with the decision's margin; two "
            "test cases confirmed both conditions.",
            "Check the linearity and the size of the error against the margin.", "R"),
           ("11.2.7", "Investigate the difference between a model's accuracy and its "
            "usefulness, and justify with an example.",
            "A model can be accurate and useless if it answers a question nobody asked, or "
            "useful and inaccurate if its errors are smaller than the decision's margin.",
            "Compare the model's error with the margin between the options.", "R"),
           ("11.2.8", "Investigate the effect of the choice of time horizon on a "
            "model's recommendation, and justify.",
            "A longer horizon favours plans with higher initial cost and "
            "lower running cost, because the running cost is saved for "
            "longer; a shorter horizon reverses the ranking.",
            "Re-solve with two horizons and compare.", "R"),
           ("11.2.9", "Conjecture a rule for which assumptions most affect a model's "
            "conclusion, and test it.",
            "The assumptions attached to the most sensitive parameters, "
            "which the sensitivity analysis identifies.",
            "Rank the assumptions by the sensitivity of their parameters.", "C"),
           ("11.2.10", "Investigate whether a model with more assumptions is always "
            "better, and justify.",
            "No: more assumptions give more detail but also more fragility, "
            "because each assumption can be challenged and each adds an "
            "error.",
            "Compare a simple and a detailed model against the same data.", "R"),
           ("11.2.11", "Investigate the difference between a model's accuracy and its "
            "usefulness, and justify.",
            "A model can be accurate and useless if it answers a question "
            "nobody asked, or useful and inaccurate if its errors are "
            "smaller than the decision's margin.",
            "Compare the error with the margin between the options.", "R"),
           ],
        C=[("11.3.1", "Write a complete solution to defining the problem of whether a "
            "school should install solar panels, naming all five parts.",
            "Decision: install or not. Objective: minimise the fifteen-year total cost. "
            "Variables: installed capacity in kW and costs in currency units per year. "
            "Constraints: roof area, budget and structural limits. Audience: the school "
            "council.",
            "Name each part of the definition and state why it matters.", "R"),
           ("11.3.2", "Write a complete solution to a sensitivity analysis of a model with "
            "three parameters, reporting the percentage change in the conclusion for a 10 "
            "per cent change in each.",
            "Rank the parameters by the size of the change, and report the conclusion's "
            "percentage change for each; the largest is the parameter whose data most need "
            "improving.",
            "Perturb each parameter by 10 per cent and record the effect.", "C"),
           ("11.3.3", "Write a complete solution to testing a model against data not used "
            "in the fit, stating the verdict.",
            "Compute the model's prediction, the absolute error and the relative error, and "
            "compare the relative error with the margin between the options being decided.",
            "The relative error against the decision's margin is the verdict.", "C"),
           ("11.3.4", "Write a complete solution to optimising P = 50x + 40y subject to "
            "x + y ≤ 10, 2x + y ≤ 14, x ≥ 0, y ≥ 0, and reporting the robustness to a 10 "
            "per cent fall in the profit from x.",
            "Vertices (0, 0), (7, 0), (4, 6), (0, 10) give 0, 350, 440, 400; the optimum is "
            "(4, 6) with 440. With the profit from x at 45, the value is 420 and (4, 6) is "
            "still optimal, so the recommendation is robust.",
            "Evaluate at the vertices, then perturb and re-evaluate.", "C"),
           ("11.3.5", "Write a complete solution to writing a five-step defence of a model "
            "against the objection that it assumes constant prices.",
            "Restate the objection; concede that prices have in fact risen; quantify that "
            "the saving is understated by about 40 per cent over ten years; state that the "
            "recommendation is unchanged and the benefit larger; repair by modelling the "
            "price rise and reporting both.",
            "Restate, concede, quantify, consequence, repair.", "R"),
           ("11.3.6", "Write a complete solution to evaluating a model that recommends an "
            "infeasible plan, identifying the cause.",
            "The plan violates a constraint that the model omitted; the model is not wrong "
            "in its arithmetic but incomplete, and the repair is to add the constraint and "
            "re-solve.",
            "Check the recommended plan against every constraint of the situation, not only "
            "those in the model.", "R"),
           ("11.3.7", "Write a complete solution to the structure of a capstone report, "
            "naming the six sections and the evidence each needs.",
            "Problem, assumptions, model, test, recommendation and limits, each with the "
            "evidence named in the brief.",
            "The evidence is what distinguishes a project from an essay.", "R"),
           ("11.3.8", "Write a complete solution to defining the problem of whether a "
            "school should install solar panels, naming all five parts.",
            "Decision, objective, variables with units, constraints and "
            "audience, each named with a reason.",
            "Name each part of the definition and state why it matters.", "R"),
           ("11.3.9", "Write a complete solution to a sensitivity analysis with three "
            "parameters, reporting the change in the conclusion for a 10 "
            "per cent change in each.",
            "Rank the parameters by the size of the change; the largest "
            "identifies where better data are needed.",
            "Perturb each parameter by 10 per cent and record the effect.", "C"),
           ("11.3.10", "Write a complete solution to testing a model against data not "
            "used in the fit, stating the verdict.",
            "Compute the prediction, the absolute error and the relative "
            "error, and compare the relative error with the margin between "
            "the options.",
            "The relative error against the decision's margin is the "
            "verdict.", "C"),
           ("11.3.11", "Write a complete solution to optimising P = 60x + 45y subject "
            "to x + y ≤ 9, 2x + y ≤ 12, x ≥ 0, y ≥ 0, and reporting the "
            "robustness.",
            "The vertices are (0, 0), (6, 0), (3, 6) and (0, 9), giving 0, "
            "360, 450 and 405; the optimum is (3, 6) with 450, and a 10 per "
            "cent fall in the profit from x gives 414 with (3, 6) still "
            "optimal.",
            "Evaluate at the vertices, then perturb and re-evaluate.", "C"),
           ("11.3.12", "Write a complete solution to writing a five-step defence "
            "against the objection that a model assumes constant prices.",
            "Restate, concede, quantify, state the consequence, repair.",
            "Restate, concede, quantify, consequence, repair.", "R"),
           ],
        D=[("11.4.1", "A school models the cost of a water tank. The tank costs 4000, "
            "saves 600 a year, and lasts 10 years. Build the model, find the payback time, "
            "and state one assumption that could change the recommendation.",
            "The total saving over 10 years is 6000 against a cost of 4000, so the payback "
            "time is 4000/600 ≈ 6.7 years; the model assumes the saving is constant, which "
            "a rising water price would change in the tank's favour.",
            "Model the cost and the saving, then find the crossing.", "A"),
           ("11.4.2", "A community garden is modelled by P = 40x + 30y with x + 2y ≤ 12, "
            "2x + y ≤ 12, x ≥ 0, y ≥ 0. Find the optimal plan and test its robustness to a "
            "10 per cent fall in the profit from x.",
            "The optimum is (4, 4) with 280; with the profit from x at 36 the value is 264 "
            "and (4, 4) is still optimal, so the recommendation is robust.",
            "Evaluate at the vertices, then perturb.", "A"),
           ("11.4.3", "A model recommends 12 tonnes of recycling but the available labour "
            "supports only 9. Evaluate the model and state the repair.",
            "The model is incomplete: it omits the labour constraint, so it recommends a "
            "plan that cannot be carried out. The repair is to add the labour constraint "
            "and re-solve, which lowers the optimum to 9 tonnes.",
            "An omitted constraint is more serious than an omitted cost.", "A"),
           ("11.4.4", "A farmer's model gives a profit of 34 000 at 40 ha of wheat and 60 "
            "ha of barley. A 10 per cent fall in the wheat price changes the profit to 30 "
            "000. Evaluate the robustness of the recommendation.",
            "The recommendation is robust, because the optimal plan is unchanged and only "
            "the value falls, by about 12 per cent.",
            "Compare the plan, not only the value, after the perturbation.", "A"),
           ("11.4.5", "A student's model is tested against four data points and gives "
            "relative errors of 3, 5, 2 and 4 per cent. The decision's margin is 15 per "
            "cent. Evaluate the model.",
            "The largest error is 5 per cent, well inside the 15 per cent margin, so the "
            "model is good enough for the decision; the errors are reported alongside the "
            "recommendation.",
            "Compare the largest error with the decision's margin.", "A"),
           ("11.4.6", "A charity models donations as D = 2000 + 50n where n is the number "
            "of events. Test the model against n = 5, D = 2300 and n = 12, D = 2650, and "
            "comment.",
            "At n = 5 the model predicts 2250 against 2300, an error of 2.2 per cent; at "
            "n = 12 it predicts 2600 against 2650, an error of 1.9 per cent. The model is "
            "acceptable for planning.",
            "Compute the prediction and the relative error at each point.", "A"),
           ("11.4.7", "A student reports a recommendation without a robustness statement. "
            "Explain what is missing and why it matters.",
            "The statement of whether the recommendation survives reasonable changes in "
            "the parameters; without it a reader cannot tell how much the conclusion can "
            "be trusted.",
            "A recommendation is a point, a value and a robustness statement.", "R"),
           ("11.4.8", "A model of a school's energy use omits the holidays. Evaluate the "
            "effect on a recommendation about insulation.",
            "The omission understates the saving from insulation during term time but "
            "overstates it over the holidays; the net effect is small, so the "
            "recommendation is probably unchanged, but the omission must be named and "
            "quantified.",
            "Trace the effect of the omission on the quantity being optimised.", "A"),
           ("11.4.9", "A council asks for a recommendation in one sentence. Draft it for a "
            "model whose optimum is a plan of value 28 000 with a robustness range of "
            "25 000 to 31 000.",
            "Adopt the plan, which is expected to give a value of about 28 000, and which "
            "remains optimal for values between 25 000 and 31 000.",
            "Give the plan, the value and the range, in the audience's terms.", "A"),
           ("11.4.10", "A student claims that a model with an error of 20 per cent is "
            "useless. Investigate and justify.",
            "Not necessarily: if the decision's margin is 50 per cent, a 20 per cent error "
            "is well inside it and the model is useful. Usefulness depends on the error "
            "relative to the margin, not on the error alone.",
            "Compare the error with the margin between the options.", "R"),
           ("11.4.11", "A model has two parameters whose 10 per cent changes move the "
            "conclusion by 2 and 9 per cent. State where effort should go and justify.",
            "To the parameter with the 9 per cent effect, because improving its estimate "
            "improves the conclusion most; the other parameter's estimate can remain "
            "crude.",
            "Rank the parameters by their effect on the conclusion.", "A"),
           ("11.4.12", "A student's reflection says only that the model 'could be "
            "improved'. Evaluate it.",
            "It is too vague to be useful: a reflection should name what the model could "
            "not answer, why, and what would be needed to answer it.",
            "A reflection names a specific limit and a specific repair.", "R")],
    ),
    assessment=[
        dict(title="A1 · The tank decision",
             text="A school is deciding whether to install a water tank. The tank costs "
                  "6000 currency units, lasts 15 years, and is expected to save 500 currency "
                  "units a year. The school's roof can collect at most 9000 litres a month. "
                  "Build a model, find the payback time, state three assumptions with the "
                  "reason for each, and write a recommendation with a robustness statement. "
                  "Then state one factor the model omits and its effect on the "
                  "recommendation.",
             note="Criteria C and D · build and test the model, state the assumptions, and "
                  "defend the recommendation."),
        dict(title="A2 · The shared resource",
             text="A community has a shared budget of 2400 currency units and 60 volunteer "
                  "hours for a summer programme. Activity A costs 40 and needs 2 hours; "
                  "activity B costs 30 and needs 4 hours; activity C costs 20 and needs 1 "
                  "hour. The value of each is modelled as 90, 70 and 40 respectively. "
                  "Formulate and solve the problem, test the robustness of the "
                  "recommendation to a 10 per cent fall in the value of A, and write a "
                  "defence against the objection that the model ignores the volunteers' "
                  "preferences.",
             note="Criteria C and D · formulate, solve by vertices, test the robustness, and "
                  "write the five-step defence."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of relationships and the related concepts of change, "
        "representation and system appear in your work?",
        "How is the global context of globalization and sustainability, and its exploration "
        "of decisions about shared resources, access and long-term cost, visible in the "
        "investigations and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limitations of a mathematical model as a guide to a shared decision, "
        "and what would you still like to ask?",
    ],
    review=dict(
        ideas=["The modelling cycle runs from defining the problem to reporting the result.",
               "A problem definition names the decision, objective, variables, constraints "
               "and audience.",
               "Assumptions are the bridge between the situation and the mathematics, and "
               "each is challengeable.",
               "A model is tested against data not used in the fit.",
               "The relative error against the decision's margin is the verdict.",
               "A sensitivity analysis ranks the parameters by their effect.",
               "A recommendation is a point, a value and a robustness statement.",
               "An omitted constraint can make a recommendation impossible.",
               "A report's six sections in order form the argument.",
               "A defence restates, concedes, quantifies, states the consequence and "
               "repairs."],
        vocab=["modelling cycle", "problem definition", "objective", "variable",
               "constraint", "assumption", "parameter", "fitting data", "test data",
               "relative error", "sensitivity analysis", "robustness", "recommendation",
               "limit", "defence", "payback time", "margin"],
        mixed=[("11.R1", "Name the five stages of the modelling cycle."),
               ("11.R2", "State the five parts of a problem definition."),
               ("11.R3", "Explain the difference between fitting data and test data."),
               ("11.R4", "State the three parts of a recommendation from a linear program."),
               ("11.R5", "Name the five steps of a defence."),
               ("11.R6", "Explain why an omitted constraint is more serious than an omitted "
                "cost.")],
    ),
    projects=dict(
        service=[("Community need", "A local resource decision is being made without a "
                                    "model that states its assumptions."),
                 ("Mathematical connection", "The whole course, applied to one decision."),
                 ("Proposed action", "Build a model of one local resource decision, publish "
                                     "it with its assumptions and its limits, and present "
                                     "it to the decision-makers."),
                 ("Expected impact", "The decision is made with its assumptions visible."),
                 ("Student reflection", "Record the model, the test and the defence.")],
        community=[("Project idea", "A model of the school's energy or water use."),
                   ("Need", "The school's consumption is discussed without a model that "
                            "states its assumptions."),
                   ("Research question", "What would a stated change to the school's "
                                         "consumption save over ten years?"),
                   ("Mathematics", "Modelling, series and optimisation."),
                   ("Action or outcome", "A one-page model with assumptions, test and "
                                         "recommendation."),
                   ("Beneficiaries", "The school and everyone who pays its bills."),
                   ("Evidence", "The model and the data behind it.")],
        personal=[("Personal interest", "A decision you will actually make."),
                  ("Learning goal", "To build a model of a decision you face and defend "
                                    "it."),
                  ("Product or outcome", "A capstone project with all six elements."),
                  ("Mathematics", "The whole course."),
                  ("Process", "Define, assume, build, test, recommend, reflect."),
                  ("Evidence", "The project and the data behind it.")],
    ),
),
])


CHAPTERS.extend([
dict(
    num=12, title="Cumulative Revision and the Transition to DP Mathematics",
    key="Logic", related=["Generalisation", "Representation", "Justification"],
    context="Identities and relationships",
    exploration="how mathematical habits shape the way we reason elsewhere",
    inquiry=("Mathematical maturity is the ability to choose a method, justify it, connect it "
             "to other ideas, and recognise the limits of what has been shown."),
    atl=("Critical thinking",
         "In order for a student to choose a method for an unfamiliar problem, students must "
         "identify the structure of the problem, select and justify an approach, and state "
         "what the solution does not show."),
    standfirst="This chapter revises the whole course and looks forward. The habit that "
               "matters is not recalling a formula but choosing a method, justifying it, "
               "and knowing where it stops.",
    engage="A DP mathematics paper contains a question nobody has seen before. Two students "
           "recognise the structure; one recalls a formula and the other does not. Which "
           "student does better, and why?",
    questions=[("Factual", "What are the main methods of each strand of the course, and when "
                           "is each used?"),
               ("Conceptual", "What does it mean to choose a method rather than recall one, "
                              "and how is the choice justified?"),
               ("Debatable", "Is a correct answer without a justification worth more or less "
                             "than a justified answer with a small error?")],
    application_lede="These tasks revise the whole course. Name the method you choose, "
                     "justify the choice, and state the limits of what you have shown.",
    projects_lede="A method is a habit of reasoning. Name the habit, justify it, and say "
                  "where it stops working.",
    sections=[
        dict(id="12.1", title="Cumulative practice: algebra and functions",
             inquiry_q="Which algebraic method fits this structure?",
             teach=[
                 "Algebra questions are classified by their structure: a polynomial to factorise, an equation to solve, a function to transform, an inequality to bound, or a system to solve. The structure decides the method, and recognising the structure is the skill.",
                 "The quadratic formula, completing the square and factorising are three methods for one class of equation, and each is preferable in a different case. Completing the square also gives the vertex, which is why it is used when a graph is needed.",
                 "Function questions are classified by whether they ask for a value, an inverse, a composition or a transformation. Each is a different operation, and the commonest error is applying the wrong one.",
                 "Justification in algebra is the statement of the rule or property used at each step. A correct answer without the reasons is a computation, not a solution, and it cannot be checked by a reader.",
             ], examples=[
                 dict(q="Solve 2x² − 7x − 3 = 0 by completing the square.",
                      vis=F("table", [["step", "working", "result"],
                                      ["divide by 2", "x² − (7/2)x = 3/2", "—"],
                                      ["half and square", "(7/4)² = 49/16", "—"],
                                      ["complete", "(x − 7/4)² = 3/2 + 49/16", "73/16"],
                                      ["solve", "x = 7/4 ± √73/4", "—"],
                                      ["decimal", "x ≈ 3.886 or x ≈ −0.386", "—"]],
                            caption="Completing the square also gives the vertex."),
                      reasoning="Complete the square, then solve and check with the "
                               "quadratic formula.",
                      steps=["Divide by 2: x² − (7/2)x = 3/2.",
                             "Add (7/4)² = 49/16 to both sides: (x − 7/4)² = 24/16 + 49/16 "
                             "= 73/16.",
                             "Take square roots: x − 7/4 = ±√73/4.",
                             "So x = (7 ± √73)/4.",
                             "Check with the quadratic formula: x = (7 ± √(49 + 24))/4 = "
                             "(7 ± √73)/4, as required."],
                      ans="x = (7 ± √73)/4, about 3.886 or −0.386",
                      interp="The check uses a different method, which is what makes it a "
                             "check."),
                 dict(q="Given f(x) = 2x − 3 and g(x) = x² + 1, find f(g(2)) and f⁻¹(5).",
                      vis=F("table", [["step", "working", "result"],
                                      ["g(2)", "4 + 1", "5"],
                                      ["f(g(2))", "2(5) − 3", "7"],
                                      ["inverse", "y = 2x − 3 gives x = (y + 3)/2", "—"],
                                      ["f⁻¹(5)", "(5 + 3)/2", "4"]],
                            caption="Composition and inversion are different operations."),
                      reasoning="Evaluate the inner function first, then invert by "
                               "rearranging.",
                      steps=["g(2) = 2² + 1 = 5.",
                             "So f(g(2)) = f(5) = 2(5) − 3 = 7.",
                             "For the inverse, write y = 2x − 3 and rearrange: x = (y + 3)/2.",
                             "So f⁻¹(x) = (x + 3)/2.",
                             "Hence f⁻¹(5) = 8/2 = 4."],
                      ans="f(g(2)) = 7 and f⁻¹(5) = 4",
                      interp="The two operations are distinguished by what they act on: "
                             "composition feeds one function into another, and inversion "
                             "reverses the rule."),
             ], inv=dict(
                 task="Take twelve algebra questions from earlier chapters of your own "
                      "choice. For each, name the method you use, justify the choice in one "
                      "sentence, solve it, and check the answer by a second method where "
                      "one exists.",
                 table=[["question type", "method chosen", "justification", "check used"],
                        ["quadratic equation", "quadratic formula", "the coefficients do "
                         "not factorise neatly", "substitution"],
                        ["polynomial division", "long division", "the divisor is linear",
                         "multiply back"],
                        ["function inverse", "rearrange and swap", "the function is "
                         "one-to-one", "composition"],
                        ["composite function", "substitute inner into outer", "the inner "
                         "output is defined", "evaluate at a point"],
                        ["quadratic inequality", "roots and sign", "the parabola opens "
                         "upwards", "test a point in each interval"],
                        ["simultaneous equations", "elimination", "one variable has equal "
                         "coefficients", "substitution"]],
                 notice=["Naming the method before solving exposed two cases where the "
                         "chosen method was inefficient.",
                         "The quadratic formula was needed only where factorising failed.",
                         "Every answer was checked, and three checks found an error.",
                         "The justifications were one sentence each, which was enough to "
                         "make the choice reviewable."],
                 obs="The structure of a question decides the method, and the justification "
                     "makes the choice reviewable.",
                 concl="An algebra question is classified by its structure, and the "
                       "structure decides the method: factorising, the quadratic formula, "
                       "completing the square, substitution, elimination, rearrangement or "
                       "a sign analysis. Each choice is justified by the structure of the "
                       "question, and every answer is checked by a second route. Here six "
                       "question types were classified and checked.")),
        dict(id="12.2", title="Cumulative practice: geometry and trigonometry",
             inquiry_q="Which geometric or trigonometric relationship applies?",
             teach=[
                 "Geometry and trigonometry questions are classified by the figure: a right-angled triangle, a general triangle, a circle, a cuboid or a cone. The figure decides the available relationships, and drawing it is the first step.",
                 "Right-angled triangles use Pythagoras and the trigonometric ratios; general triangles use the sine rule, the cosine rule or the area formula. The choice depends on whether the given angle is included.",
                 "Circle questions use the angle at the centre theorem, the tangent-radius property or the intersecting chords theorem, and the choice is made by naming the arc, the tangent or the chords involved.",
                 "Three-dimensional questions are solved by choosing a plane. Naming the plane and the triangle in it is the first line of the solution, and it is what makes the rest of the solution checkable.",
             ], examples=[
                 dict(q="A triangle has sides 8 and 11 and included angle 47°. Find the "
                        "area and the third side.",
                      vis=F("table", [["step", "working", "result"],
                                      ["area", "½ × 8 × 11 × sin 47°", "32.2"],
                                      ["third side squared", "8² + 11² − 2(8)(11) cos 47°",
                                       "62.9"],
                                      ["third side", "√62.9", "7.93"],
                                      ["check", "the largest side is 11, opposite the "
                                       "largest angle", "consistent"]],
                            caption="The included angle fixes both the area and the third "
                                    "side."),
                      reasoning="Apply the area formula and the cosine rule, then check the "
                               "ordering.",
                      steps=["The area is ½ × 8 × 11 × sin 47° ≈ 44 × 0.7314 ≈ 32.2.",
                             "The third side squared is 8² + 11² − 2(8)(11) cos 47° ≈ 185 − "
                             "176(0.6820) ≈ 65.0.",
                             "So the third side is about 8.06.",
                             "Check: 11 is the largest side, so it is opposite the largest "
                             "angle, which is the given 47 degrees only if 47 is indeed "
                             "largest.",
                             "The angle opposite 11 is arccos((64 + 65 − 121)/(2 × 8 × 8.06)) "
                             "≈ 79.4 degrees, which is the largest, as required."],
                      ans="area about 32.2, third side about 8.06",
                      interp="The check on the ordering of sides and angles is the standard "
                             "verification for a triangle."),
                 dict(q="A circle has a chord of length 24 at distance 7 from the centre. "
                        "Find the radius and the angle the chord subtends at the centre.",
                      vis=F("table", [["step", "working", "result"],
                                      ["half-chord", "12", "—"],
                                      ["radius", "√(12² + 7²)", "√193 ≈ 13.89"],
                                      ["half-angle", "arcsin(12/13.89)", "59.7°"],
                                      ["full angle", "2 × 59.7°", "119.4°"]],
                            caption="The perpendicular from the centre bisects the chord."),
                      reasoning="Use the perpendicular-bisector property, then a sine ratio "
                               "in the resulting triangle.",
                      steps=["The perpendicular from the centre to the chord bisects it, so "
                             "half the chord is 12.",
                             "The radius is √(12² + 7²) = √193 ≈ 13.89.",
                             "In the right-angled triangle, sin(half the angle) = 12/13.89.",
                             "So half the angle is about 59.7 degrees and the full angle is "
                             "about 119.4 degrees.",
                             "The angle is obtuse, as expected for a chord far from the "
                             "centre."],
                      ans="radius about 13.89; the angle is about 119.4 degrees",
                      interp="Two circle properties are used, and both are named in the "
                             "solution."),
             ], inv=dict(
                 task="Take ten geometry and trigonometry questions from earlier chapters. "
                      "For each, draw the figure, name the relationship you use, justify the "
                      "choice in one sentence, solve it, and check the answer by a second "
                      "route.",
                 table=[["figure", "relationship used", "justification", "check"],
                        ["right triangle", "Pythagoras", "a right angle is given",
                         "trigonometric ratio"],
                        ["general triangle, ASA", "sine rule", "a side and its opposite "
                         "angle are known", "angle sum"],
                        ["general triangle, SAS", "cosine rule", "the included angle is "
                         "given", "sine rule"],
                        ["circle, chord", "perpendicular bisects chord", "the distance from "
                         "the centre is given", "sine ratio"],
                        ["circle, tangent", "tangent perpendicular to radius", "a tangent "
                         "length is needed", "Pythagoras"],
                        ["cuboid", "two applications of Pythagoras", "a space diagonal is "
                         "needed", "three-dimensional Pythagoras"]],
                 notice=["Drawing the figure first made the correct relationship obvious in "
                         "every case.",
                         "The sine rule and the cosine rule were distinguished by whether "
                         "the given angle was included.",
                         "The circle questions were distinguished by whether a chord, a "
                         "tangent or an arc was involved.",
                         "Every answer was checked, and two checks found a sign error."],
                 obs="The figure decides the relationship, and naming the figure is the "
                     "first step.",
                 concl="Geometry and trigonometry questions are classified by the figure: "
                       "right-angled triangles, general triangles, circles, cuboids and "
                       "cones. Each figure has its own relationships, the choice is "
                       "justified by what is given, and three-dimensional problems are "
                       "solved by choosing a plane. Here six figure types were classified "
                       "and checked.")),
        dict(id="12.3", title="Cumulative practice: statistics and probability",
             inquiry_q="Which measure or rule fits this question?",
             teach=[
                 "Statistics questions are classified by whether they ask for a centre, a dispersion, an association or a prediction. Each needs a different measure, and using the wrong one is the commonest error.",
                 "When the data are symmetric the mean and the standard deviation use the most information; when they are skewed the median and the interquartile range are the appropriate measures, because they resist extremes.",
                 "Probability questions are classified by whether they ask for a simple probability, a conditional probability, an independence test, a total probability or a count. Each is a different rule, and naming the rule is the justification.",
                 "Every statistical conclusion states the sample and the origin of the data, because the description extends to a wider population only if the sample was representative.",
             ], examples=[
                 dict(q="A data set has mean 30, median 22 and mode 18. Describe its shape "
                        "and say which measure of centre to report.",
                      vis=F("table", [["measure", "value", "position"],
                                      ["mode", "18", "lowest"],
                                      ["median", "22", "middle"],
                                      ["mean", "30", "highest"],
                                      ["conclusion", "mean > median > mode", "skewed "
                                       "right"]],
                            caption="The order of the measures diagnoses the skew."),
                      reasoning="Compare the three measures and use their order to identify "
                               "the skew.",
                      steps=["The three measures are 18, 22 and 30.",
                             "The mean is the largest, so the distribution is skewed to the "
                             "right.",
                             "A right skew means a long tail of large values pulling the "
                             "mean upwards.",
                             "The median is the better measure of centre, because it is "
                             "resistant to the tail.",
                             "So the report gives the median, 22, with a note that the "
                             "distribution is skewed."],
                      ans="skewed to the right; report the median, 22",
                      interp="The order of the three measures is the diagnosis, and the "
                             "skew decides which measure to report."),
                 dict(q="A disease affects 1 in 500. A test has sensitivity 95 per cent and "
                        "a false-positive rate of 2 per cent. Find the probability that a "
                        "person who tests positive has the disease.",
                      vis=F("table", [["group", "test positive", "test negative", "total"],
                                      ["has the disease", "190", "10", "200"],
                                      ["does not", "1 996", "97 804", "99 800"],
                                      ["total", "2 186", "97 814", "100 000"]],
                            caption="Out of 100 000 people, 2186 test positive."),
                      reasoning="Scale the table to whole numbers, then divide the true "
                               "positives by the total positives.",
                      steps=["Take 100 000 people: 200 have the disease and 99 800 do not.",
                             "Of the 200, 95 per cent, or 190, test positive.",
                             "Of the 99 800, 2 per cent, or 1996, test positive.",
                             "So 190 + 1996 = 2186 people test positive.",
                             "The probability is 190/2186 ≈ 0.0869, about 8.7 per cent."],
                      ans="about 0.0869",
                      interp="The base-rate effect is stark here: a 95 per cent sensitive "
                             "test on a rare disease gives a positive result that is wrong "
                             "about 91 per cent of the time."),
             ], inv=dict(
                 task="Take eight statistics and probability questions from earlier "
                      "chapters. For each, name the measure or rule you use, justify the "
                      "choice in one sentence, solve it, and state one limit of the "
                      "conclusion.",
                 table=[["question type", "measure or rule", "justification", "limit of the "
                                "conclusion"],
                        ["describe a centre", "median", "the data are skewed", "the sample "
                         "only"],
                        ["describe a spread", "interquartile range", "an outlier is "
                         "present", "the sample only"],
                        ["compare two groups", "mean and standard deviation", "both "
                         "distributions are symmetric", "no causal claim"],
                        ["association", "correlation coefficient", "a linear pattern is "
                         "suspected", "association, not causation"],
                        ["prediction", "regression of y on x", "y is to be predicted from "
                         "x", "extrapolation is unreliable"],
                        ["conditional probability", "Bayes' theorem", "the reverse "
                         "conditional is needed", "depends on the prevalence"]],
                 notice=["Naming the measure before computing exposed one case where the "
                         "mean had been used on skewed data.",
                         "The limit of each conclusion was stated in one clause.",
                         "The probability questions were distinguished by which conditional "
                         "direction was needed.",
                         "Every answer was checked against a small case that could be "
                         "listed."],
                 obs="Each statistics question has a measure matched to its purpose, and "
                     "each conclusion has a stated limit.",
                 concl="Statistics questions are classified by whether they ask for a "
                       "centre, a dispersion, an association or a prediction, and "
                       "probability questions by which rule applies. Skewed data call for "
                       "the median and the interquartile range, and every conclusion states "
                       "the sample and its origin. Here the positive result meant only an "
                       "8.7 per cent chance of disease.")),
        dict(id="12.4", title="Unfamiliar problems and extended reasoning",
             inquiry_q="How is a problem with no familiar structure approached?",
             teach=[
                 "An unfamiliar problem is approached by simplifying it, solving a special case, looking at a small instance, or working backwards from the answer. None of these is the method; all of them are ways of finding the structure, and the generalisation that follows is what is being looked for.",
                 "Extended reasoning is a chain of justified steps, each of which would be accepted on its own. The chain is only as strong as its weakest step, so each step is checked before the next is taken, and the representation chosen makes the chain easier to follow.",
                 "A conjecture is formed from examples and then justified. The examples suggest; only the justification proves, and a conjecture that has not been justified is a hypothesis.",
                 "Recognising the limits of what has been shown is part of the answer. A solution that states what it has not proved is complete; one that does not is incomplete, however correct the computation.",
             ], examples=[
                 dict(q="Find the number of diagonals of a polygon with n sides, and prove "
                        "the formula.",
                      vis=F("table", [["step", "working", "result"],
                                      ["pairs of vertices", "n(n − 1)/2", "—"],
                                      ["sides", "n", "—"],
                                      ["diagonals", "n(n − 1)/2 − n", "n(n − 3)/2"],
                                      ["check at n = 4", "4(1)/2", "2"],
                                      ["check at n = 5", "5(2)/2", "5"]],
                            caption="The formula is checked on two small cases."),
                      reasoning="Count the pairs of vertices, subtract the sides, and check "
                               "on small cases.",
                      steps=["Every pair of vertices gives either a side or a diagonal.",
                             "The number of pairs is n(n − 1)/2.",
                             "Of these, n are sides, so the number of diagonals is n(n − "
                             "1)/2 − n.",
                             "Simplifying gives n(n − 3)/2.",
                             "Check: a quadrilateral has 4(1)/2 = 2 diagonals and a "
                             "pentagon has 5(2)/2 = 5, as required."],
                      ans="n(n − 3)/2 diagonals",
                      interp="The two small cases confirm the formula but do not prove it; "
                             "the proof is the counting argument."),
                 dict(q="A student finds that 1 + 3 + 5 + 7 = 16 and conjectures that the "
                        "sum of the first n odd numbers is n². Justify or refute the "
                        "conjecture.",
                      vis=F("table", [["n", "sum of the first n odd numbers", "n²",
                                       "conjecture holds?"],
                                      ["1", "1", "1", "yes"],
                                      ["2", "4", "4", "yes"],
                                      ["3", "9", "9", "yes"],
                                      ["4", "16", "16", "yes"],
                                      ["5", "25", "25", "yes"]],
                            caption="Five cases support the conjecture."),
                      reasoning="Justify the conjecture by an argument that covers every "
                               "case, not by more examples.",
                      steps=["The examples support the conjecture but do not prove it.",
                             "To prove it, write the sum as (2 × 1 − 1) + (2 × 2 − 1) + … + "
                             "(2n − 1).",
                             "This is 2(1 + 2 + … + n) − n.",
                             "Using the formula for the sum of the first n integers, this is "
                             "2 × n(n + 1)/2 − n = n².",
                             "So the conjecture is true, and the justification covers every "
                             "n."],
                      ans="the conjecture is true, and the proof is the algebraic "
                          "simplification",
                      interp="Examples suggest and the argument proves, and the difference "
                             "is what the inquiry statement calls mathematical maturity."),
             ], inv=dict(
                 task="Take four unfamiliar problems, each from a different strand. For "
                      "each, describe how you found the structure, set out the solution as "
                      "a chain of justified steps, and state one thing your solution does "
                      "not show.",
                 table=[["problem", "how the structure was found", "chain of steps",
                                "what is not shown"],
                        ["counting diagonals", "a small case was drawn", "count pairs, "
                         "subtract sides, simplify", "nothing further is needed"],
                        ["sum of odd numbers", "examples suggested a pattern", "express "
                         "algebraically, simplify", "the argument does not extend to even "
                         "numbers"],
                        ["an unfamiliar triangle", "the figure was drawn and the given "
                         "parts marked", "identify the rule, apply, check the angle sum",
                         "the check does not exclude a second triangle unless the ambiguous "
                         "case is tested"],
                        ["an unfamiliar probability", "a small case was listed exhaustively",
                         "count the outcomes, form the ratio", "the count assumes the "
                         "outcomes are equally likely"]],
                 notice=["Drawing a small case was the most productive first move in three "
                         "of the four problems.",
                         "Writing the chain of steps exposed one step that had been "
                         "assumed rather than justified.",
                         "The ambiguous case had to be checked explicitly, which was the "
                         "limit of one solution.",
                         "Every solution stated something it did not show."],
                 obs="An unfamiliar problem is approached by finding its structure, and the "
                     "solution is a chain of justified steps with stated limits.",
                 concl="An unfamiliar problem is approached by simplifying it, solving a "
                       "special case, examining a small instance or working backwards, and "
                       "each is a way of finding the structure. The solution is then a "
                       "chain of justified steps, and it states what it does not show. "
                       "Examples suggest a conjecture; only an argument that covers every "
                       "case proves it.")),
        dict(id="12.5", title="Cumulative examination",
             inquiry_q="How is examination technique different from coursework?",
             teach=[
                 "An examination rewards the choice of method as much as the execution, and it rewards the statement of the method even when the arithmetic is imperfect. Writing down the intended method is the first thing to do on any question.",
                 "Time is allocated by marks, not by order. A question worth few marks is not worth many minutes, and leaving a hard question until last is a strategy rather than a defeat.",
                 "Every answer is checked by a route that is different from the one used to obtain it. Substitution, an estimate, a special case and a dimension check are the four standard checks, and each takes seconds.",
                 "A question that cannot be solved should still be started: the method is written down, the first step is taken, and the partial answer is left. Partial credit is awarded for a correct method, and an unanswered question scores nothing.",
             ], examples=[
                 dict(q="Solve the question: a population doubles every 8 years. Find the "
                        "annual percentage growth rate, to three significant figures.",
                      vis=F("table", [["step", "working", "result"],
                                      ["model", "P = P₀ × 2^(t/8)", "—"],
                                      ["annual factor", "2^(1/8)", "1.0905"],
                                      ["rate", "2^(1/8) − 1", "0.0905"],
                                      ["percentage", "0.0905 × 100", "9.05 per cent"]],
                            caption="The exponent counts eight-year periods, not years."),
                      reasoning="Write the model, extract the annual factor, and convert to "
                               "a percentage.",
                      steps=["The model is P(t) = P₀ × 2^(t/8), because the doubling period "
                             "is 8 years.",
                             "The annual factor is 2^(1/8), since t = 1 gives one year.",
                             "2^(1/8) ≈ 1.0905.",
                             "So the annual rate is 1.0905 − 1 = 0.0905.",
                             "As a percentage this is about 9.05 per cent per year."],
                      ans="about 9.05 per cent per year",
                      interp="The error to avoid is dividing 100 per cent by 8, which gives "
                             "12.5 per cent and is wrong, because the growth compounds."),
                 dict(q="A candidate has 20 minutes left and two questions remaining, one "
                        "worth 3 marks and one worth 8. Advise on the order.",
                      vis=F("table", [["question", "marks", "time available", "advice"],
                                      ["the 3-mark question", "3", "about 5 minutes", "do it "
                                       "first"],
                                      ["the 8-mark question", "8", "about 15 minutes",
                                       "then start it and write the method"],
                                      ["if stuck", "—", "—", "write the method and the "
                                       "first step"]],
                            caption="Time is allocated by marks."),
                      reasoning="Allocate time in proportion to the marks and start the "
                               "harder question with the method.",
                      steps=["The 3-mark question should take about a quarter of the "
                             "remaining time.",
                             "So it is done first, in about 5 minutes.",
                             "The 8-mark question then has about 15 minutes, which is "
                             "enough to write the method and several steps.",
                             "If it cannot be finished, the method and the first step are "
                             "left on the page.",
                             "Partial credit is awarded for a correct method, so an "
                             "unanswered question is the only one that scores nothing."],
                      ans="the 3-mark question first, then start the 8-mark one with the "
                          "method",
                      interp="The strategy is to secure the easy marks and to start the "
                             "hard question with a stated method."),
             ], inv=dict(
                 task="Take a past examination paper. Attempt it under timed conditions, "
                      "allocating time by marks. Afterwards, review each answer and record "
                      "the check you used, the time spent, and one thing you would do "
                      "differently.",
                 table=[["question", "marks", "time spent", "check used", "what to change"],
                        ["algebra", "6", "6 min", "substitution", "nothing"],
                        ["trigonometry", "8", "12 min", "angle sum", "draw the figure "
                         "first"],
                        ["probability", "7", "10 min", "list a small case", "name the rule "
                         "before computing"],
                        ["modelling", "12", "20 min", "estimate the order of magnitude",
                         "state the assumptions earlier"],
                        ["geometry", "5", "15 min", "—", "move on after 8 minutes"]],
                 notice=["The geometry question took three times its share of time, which "
                         "cost marks elsewhere.",
                         "Two answers were wrong and were caught only by the checks, both "
                         "of which took seconds.",
                         "The modelling question needed its assumptions stated early, "
                         "because the marks were for the assumptions as much as the "
                         "arithmetic.",
                         "Allocating time by marks rather than by order would have gained "
                         "several marks."],
                 obs="Examination technique is a separate skill from the mathematics, and it "
                     "is learned by review.",
                 concl="An examination rewards the choice and statement of a method, the "
                       "allocation of time by marks, and the use of a check different from "
                       "the route used to obtain the answer. A question that cannot be "
                       "finished should still be started, because partial credit is awarded "
                       "for a correct method. Here the doubling rate was about 9.05 per "
                       "cent per year.")),
        dict(id="12.6", title="From MYP to DP: expectations and readiness",
             inquiry_q="What changes in the transition to DP mathematics?",
             teach=[
                 "DP mathematics expects a student to choose a method, justify it, and connect it to other ideas, and the logic of the argument is examined at every step. The content is largely familiar; the expectation of independent choice is what is new.",
                 "The DP courses are split by emphasis: one for students who need mathematics as a tool, one for students who will study it seriously, and one for those who will study it at depth. The choice depends on what the student will do next, not on how easy the course is.",
                 "Investigation and internal assessment are part of the DP, and the mathematical exploration rewards the same habits as the capstone project: a stated problem, stated assumptions, a test and a reflection on the limits.",
                 "Readiness is not the recall of formulas. It is the ability to read an unfamiliar question, identify its structure, select a method, and justify the selection, and those are the habits this course has been building.",
             ], examples=[
                 dict(q="Compare the expectations of an MYP extended question with a DP "
                        "examination question on the same content.",
                      vis=F("table", [["aspect", "MYP extended question", "DP examination "
                                       "question"],
                                      ["structure", "signposted in parts", "often a single "
                                       "unfamiliar stem"],
                                      ["method", "suggested or implied", "chosen by the "
                                       "student"],
                                      ["justification", "required for the top band",
                                       "required throughout"],
                                      ["marks", "for the answer and the reasoning", "for the "
                                       "method, the answer and the reasoning"],
                                      ["time", "part of a coursework task", "allocated by "
                                       "marks"]],
                            caption="The content is familiar; the independence is new."),
                      reasoning="Compare the two forms on five aspects.",
                      steps=["An MYP extended question is usually signposted in parts, each "
                             "pointing at a method.",
                             "A DP question often presents a single unfamiliar stem and "
                             "leaves the choice of method to the student.",
                             "Justification is required for the top band in MYP and "
                             "throughout in DP.",
                             "Marks are awarded for the answer and the reasoning in both, "
                             "but DP marks the method separately.",
                             "So the transition is from following a signposted route to "
                             "choosing one."],
                      ans="the content is familiar; the independence and the continuous "
                          "justification are new",
                      interp="Naming what is new makes the transition manageable, because "
                             "the mathematics is already known."),
                 dict(q="A student can recall every formula in the course but cannot choose "
                        "between them. Advise on what to practise.",
                      vis=F("table", [["skill", "status", "what to practise"],
                                      ["recall", "strong", "nothing further"],
                                      ["recognition of structure", "weak", "classify "
                                       "questions by type"],
                                      ["choice of method", "weak", "solve each type by two "
                                       "methods and compare"],
                                      ["justification", "weak", "write the reason beside "
                                       "every step"],
                                      ["limits", "absent", "state what each solution does "
                                       "not show"]],
                            caption="Recall is the least of the four skills."),
                      reasoning="Assess the four skills and name the practice each needs.",
                      steps=["Recall is strong, so no further practice is needed there.",
                             "Recognition of structure is weak, so questions should be "
                             "classified by type before solving.",
                             "Choice of method is weak, so each type should be solved by "
                             "two methods and the results compared.",
                             "Justification is weak, so the reason should be written beside "
                             "every step.",
                             "The habit of stating limits is absent, and is practised by "
                             "writing what each solution does not show."],
                      ans="practise recognition, choice, justification and limits",
                      interp="The four skills are what the inquiry statement calls "
                             "mathematical maturity, and recall is only the first."),
             ], inv=dict(
                 task="Assess your own readiness for DP mathematics on the four skills in "
                      "the inquiry statement: choosing a method, justifying it, connecting "
                      "it to other ideas, and recognising the limits of what has been "
                      "shown. For each, give a rating, an example from your own work, and "
                      "one thing you will practise.",
                 table=[["skill", "rating", "example from my work", "what I will practise"],
                        ["choosing a method", "developing", "I chose the cosine rule for an "
                         "SAS triangle", "classifying questions by structure first"],
                        ["justifying it", "developing", "I named the tangent-radius "
                         "property", "writing the reason beside every step"],
                        ["connecting ideas", "emerging", "I linked the determinant to area",
                         "looking for the same idea in two strands"],
                        ["recognising limits", "emerging", "I labelled a prediction as "
                         "extrapolation", "stating what each solution does not show"]],
                 notice=["The four skills could each be rated against a concrete example.",
                         "The weakest skill was recognising limits, because it had rarely "
                         "been asked for.",
                         "Connecting ideas was easier once a single idea, the determinant, "
                         "was followed across two strands.",
                         "Each rating came with a specific practice, not a general "
                         "intention."],
                 obs="Readiness is assessed by example, and each gap has a specific "
                     "practice.",
                 concl="DP mathematics expects a student to choose a method, justify it, "
                       "connect it to other ideas and recognise the limits of what has been "
                       "shown, and the content is largely familiar. Readiness is assessed "
                       "against those four skills rather than against recall, and each gap "
                       "has a specific practice. Here the four skills were rated "
                       "developing, developing, emerging and emerging.")),
    ],
    practice=dict(
        A=[("12.1.1", "Solve x² − 5x + 6 = 0.",
            "x = 2 or x = 3.", "Factorise, since the coefficients are small.", "F"),
           ("12.1.2", "Solve 3x² + 5x − 2 = 0.",
            "x = (−5 ± √(25 + 24))/6 = (−5 ± 7)/6, so x = 1/3 or x = −2.",
            "The quadratic formula, since factorising is not immediate.", "F"),
           ("12.1.3", "Given f(x) = 4x − 7, find f⁻¹(x).",
            "f⁻¹(x) = (x + 7)/4.", "Rearrange and swap.", "F"),
           ("12.1.4", "Given f(x) = x² and g(x) = 3x − 1, find f(g(2)).",
            "g(2) = 5, so f(g(2)) = 25.", "Evaluate the inner function first.", "F"),
           ("12.1.5", "Solve 2x − 5 > 7.",
            "x > 6.", "Add 5 and divide by 2.", "F"),
           ("12.1.6", "Solve x² + 2x − 15 ≤ 0.",
            "−5 ≤ x ≤ 3.", "Factorise and read the sign between the roots.", "F"),
           ("12.1.7", "Find the 20th term of the arithmetic sequence 3, 8, 13, …",
            "u(20) = 3 + 19(5) = 98.", "Use u(n) = a + (n − 1)d.", "F"),
           ("12.1.8", "Find the sum to infinity of 20 + 10 + 5 + …",
            "20/(1 − 0.5) = 40.", "Check |r| < 1, then apply the formula.", "F"),
           ("12.1.9", "Solve 2ˣ = 30, to three significant figures.",
            "x = log 30 ÷ log 2 ≈ 4.91.", "Take logarithms of both sides.", "F"),
           ("12.1.10", "A town of 40 000 grows 3 per cent a year. Find the population after "
            "10 years.",
            "40 000 × 1.03¹⁰ ≈ 53 757.", "Apply the compound growth model.", "F"),
           ("12.1.11", "Find the determinant of [[3, 5], [7, 2]].",
            "6 − 35 = −29.", "Use ad − bc.", "F"),
           ("12.1.12", "Given a = (2, −3) and b = (5, 1), find |a + b|.",
            "a + b = (7, −2), so |a + b| = √53 ≈ 7.28.", "Add component-wise, then use "
            "Pythagoras.", "F")],
        B=[("12.2.1", "Investigate the number of methods available for solving a quadratic "
            "equation, and justify when each is preferred.",
            "Factorising is preferred when the roots are rational and small; the quadratic "
            "formula always works; completing the square also gives the vertex.",
            "Solve the same equation by all three methods and compare.", "R"),
           ("12.2.2", "Conjecture a rule for when the sine rule gives two answers, and test "
            "it on three cases.",
            "Two answers exactly when the given side opposite the given angle lies between "
            "the perpendicular height and the other given side.",
            "Compare the given side with the height and the other side.", "C"),
           ("12.2.3", "Investigate the relationship between the area formula ½ab sin C and "
            "the cosine rule, and justify it.",
            "Both use the included angle; the area formula gives the size of the triangle "
            "and the cosine rule gives the third side, and together they determine the "
            "triangle from SAS.",
            "Derive the area formula from the height, and the cosine rule from Pythagoras.",
            "R"),
           ("12.2.4", "Take a circle theorem of your own and investigate how many other "
            "theorems follow from it, justifying each.",
            "From the angle at the centre theorem follow angles in the same segment, the "
            "right angle in a semicircle and the cyclic quadrilateral property, each by a "
            "short argument.",
            "Derive each consequence from the chosen theorem.", "C"),
           ("12.2.5", "Investigate the connection between the determinant of a 2 by 2 "
            "matrix and the area of a triangle, and justify.",
            "The area of a triangle is half the absolute value of the determinant of its "
            "two side vectors, because the determinant is the area of the parallelogram "
            "they span.",
            "Compute both for the same triangle.", "R"),
           ("12.2.6", "Conjecture a rule for the number of real roots of a quadratic from "
            "its discriminant, and test it.",
            "Two distinct real roots when the discriminant is positive, one repeated root "
            "when it is zero, and none when it is negative.",
            "Compute the discriminant for several quadratics and count the roots.", "R"),
           ("12.2.7", "Investigate the relationship between the correlation coefficient and "
            "the gradient of the regression line, and justify.",
            "The gradient is r times the ratio of the standard deviations, so r fixes the "
            "sign and the gradient fixes the size, and they are equal only when both "
            "standard deviations are equal.",
            "Compute both for the same data set.", "C"),
           ("12.2.8", "Investigate the number of methods for solving a quadratic "
            "equation and justify when each is preferred.",
            "Factorising for rational roots, the quadratic formula always, "
            "completing the square when the vertex is also needed.",
            "Solve the same equation by all three methods and compare.", "R"),
           ("12.2.9", "Conjecture a rule for the number of real roots of a quadratic "
            "from its discriminant, and test it.",
            "Two when the discriminant is positive, one when it is zero, "
            "none when it is negative.",
            "Compute the discriminant for several quadratics and count the "
            "roots.", "R"),
           ("12.2.10", "Investigate the connection between the determinant of a 2 by 2 "
            "matrix and the area of a triangle, and justify.",
            "The area is half the absolute value of the determinant of the "
            "two side vectors, because the determinant is the area of the "
            "parallelogram they span.",
            "Compute both for the same triangle.", "R"),
           ("12.2.11", "Investigate the relationship between the correlation "
            "coefficient and the gradient of the regression line, and "
            "justify.",
            "The gradient is r times the ratio of the standard deviations, "
            "so r fixes the sign and the gradient the size.",
            "Compute both for the same data set.", "C"),
           ],
        C=[("12.3.1", "Write a complete solution to solving 2x² − 3x − 4 = 0, to three "
            "significant figures.",
            "x = (3 ± √(9 + 32))/4 = (3 ± √41)/4, so x ≈ 2.35 or x ≈ −0.851.",
            "The quadratic formula, then check by substitution.", "R"),
           ("12.3.2", "Write a complete solution to a population that doubles every 8 "
            "years, finding the annual percentage growth rate.",
            "The annual factor is 2^(1/8) ≈ 1.0905, so the annual rate is about 9.05 per "
            "cent.",
            "Write the model, extract the annual factor, and convert to a percentage.",
            "A"),
           ("12.3.3", "Write a complete solution to a triangle with sides 7 and 9 and "
            "included angle 68°, finding the third side and the area.",
            "The third side is √(49 + 81 − 126 cos 68°) ≈ √82.8 ≈ 9.10; the area is ½ × 7 × "
            "9 × sin 68° ≈ 29.2.",
            "Cosine rule for the side, area formula for the area.", "R"),
           ("12.3.4", "Write a complete solution to a screening problem with prevalence 1 "
            "in 400, sensitivity 96 per cent and false-positive rate 3 per cent.",
            "Out of 400 000 people: 960 true positives and 11 997 false positives, so "
            "P = 960/12 957 ≈ 0.0741.",
            "Scale to whole numbers and divide by the total positives.", "A"),
           ("12.3.5", "Write a complete solution to finding the inverse of "
            "f(x) = (5x − 2)/(x + 3), with its domain.",
            "f⁻¹(x) = (3x + 2)/(5 − x), with domain x ≠ 5.",
            "Clear the fraction, rearrange, swap, and state the new denominator.", "C"),
           ("12.3.6", "Write a complete solution to maximising P = 5x + 4y subject to "
            "x + 2y ≤ 12, 3x + 2y ≤ 18, x ≥ 0, y ≥ 0.",
            "The vertices are (0, 0), (6, 0), (4, 4) and (0, 6), giving 0, 30, 36 and 24; "
            "the maximum is 36 at (4, 4).",
            "Evaluate the objective at each vertex.", "R"),
           ("12.3.7", "Write a complete solution to finding the area of the parallelogram "
            "spanned by (4, −1) and (2, 5), and the determinant of the matrix with those "
            "columns.",
            "The determinant is 4(5) − (−1)(2) = 22, so the area is 22.",
            "The determinant is the signed area.", "R"),
           ("12.3.8", "Write a complete solution to solving 2x² + 5x − 3 = 0 by two "
            "methods.",
            "By factorising, (2x − 1)(x + 3) = 0 gives x = 0.5 or x = −3; "
            "by the formula, x = (−5 ± √(25 + 24))/4 = (−5 ± 7)/4, the "
            "same.",
            "Use two independent routes to the same answer.", "R"),
           ("12.3.9", "Write a complete solution to a triangle with sides 10 and 13 "
            "and included angle 55°, finding the third side and the area.",
            "The third side is √(100 + 169 − 260 cos 55°) ≈ √119.9 ≈ 10.95; "
            "the area is ½ × 10 × 13 × sin 55° ≈ 53.2.",
            "Cosine rule for the side, area formula for the area.", "R"),
           ("12.3.10", "Write a complete solution to a screening problem with "
            "prevalence 2 per cent, sensitivity 90 per cent and "
            "false-positive rate 8 per cent.",
            "Out of 10 000 people: 180 true positives and 784 false "
            "positives, so P = 180/964 ≈ 0.187.",
            "Scale to whole numbers and divide by the total positives.", "A"),
           ("12.3.11", "Write a complete solution to finding the sum of the first 20 "
            "terms of the geometric sequence with u(1) = 3 and r = 1.05.",
            "3(1.05²⁰ − 1)/(1.05 − 1) ≈ 3 × 33.066 ≈ 99.2.",
            "Use the geometric sum formula.", "F"),
           ("12.3.12", "Write a complete solution to maximising P = 3x + 5y subject to "
            "x + 2y ≤ 14, 3x + y ≤ 15, x ≥ 0, y ≥ 0.",
            "The vertices are (0, 0), (5, 0), (16/5, 27/5) and (0, 7), "
            "giving 0, 15, 36.6 and 35; the maximum is 36.6 at (3.2, 5.4).",
            "Evaluate the objective at each vertex.", "R"),
           ],
        D=[("12.4.1", "A company's output is modelled by P(t) = 5000(1.06)ᵗ. Find the "
            "doubling time and the output after 15 years.",
            "Doubling time ln 2 ÷ ln 1.06 ≈ 11.9 years; after 15 years P ≈ 5000 × 2.397 ≈ "
            "11 985.",
            "Use the doubling formula, then evaluate.", "A"),
           ("12.4.2", "A loan of 9000 is repaid in 4 equal annual instalments at 8 per "
            "cent. Find the instalment and the total repaid.",
            "R = 9000 ÷ ((1 − 1.08⁻⁴)/(1 − 1.08⁻¹)) ≈ 9000 ÷ 3.3121 ≈ 2717; the total repaid "
            "is about 10 868.",
            "Equate the present value of the instalments to the loan.", "A"),
           ("12.4.3", "Two schools' mean scores are both 62. School A has standard "
            "deviation 4 and school B has 15. Write a comparison and state one thing it "
            "cannot show.",
            "The centres agree; school B's results are nearly four times as spread, so its "
            "students' outcomes differ far more. The comparison cannot show why, because it "
            "describes the samples only.",
            "Compare centre and dispersion, then state the limit.", "A"),
           ("12.4.4", "A cuboid has edges 5, 12 and 13. Find the space diagonal and the "
            "angle it makes with the longest edge.",
            "The space diagonal is √(25 + 144 + 169) = √338 ≈ 18.38; the angle has cosine "
            "13/√338, so it is about 45.1°.",
            "Two applications of Pythagoras, then a cosine ratio.", "A"),
           ("12.4.5", "A bag has 5 red and 3 blue counters. Two are drawn without "
            "replacement. Find P(both red) and P(one of each).",
            "P(both red) = (5/8)(4/7) = 20/56 ≈ 0.357; P(one of each) = 2 × (5/8)(3/7) = "
            "30/56 ≈ 0.536.",
            "Multiply the conditional probabilities, counting both orders.", "A"),
           ("12.4.6", "A population doubles every 8 years. Find the annual percentage "
            "growth rate, to three significant figures.",
            "2^(1/8) − 1 ≈ 0.0905, about 9.05 per cent per year.",
            "Write the model, extract the annual factor, and convert to a percentage.", "A"),
           ("12.4.7", "A student answers an examination question correctly but gives no "
            "reasons. Evaluate the likely outcome.",
            "The method marks are lost, and only the answer mark is gained, so the score is "
            "a fraction of what the question was worth.",
            "Marks are awarded for the method, the answer and the reasoning.", "R"),
           ("12.4.8", "A candidate spends 25 minutes on a 4-mark question and leaves a "
            "12-mark question unanswered. Evaluate the strategy.",
            "Poor: time should be allocated by marks, so the 4-mark question warranted "
            "about 6 minutes and the 12-mark question the remainder, and an unanswered "
            "question scores nothing.",
            "Allocate time in proportion to the marks.", "R"),
           ("12.4.9", "A student solves an unfamiliar problem by listing the cases for "
            "n = 1, 2, 3 and 4 and generalising. Evaluate the solution.",
            "Incomplete: the examples suggest the pattern but do not prove it, and a "
            "justification covering every case is needed.",
            "Examples suggest; an argument proves.", "R"),
           ("12.4.10", "A question asks for the area of a triangle with vertices (1, 1), "
            "(5, 2) and (2, 6). Solve it by two methods.",
            "By determinants: the side vectors are (4, 1) and (1, 5), with determinant 19, "
            "so the area is 9.5. By base and height: the base is √17 ≈ 4.123 and the "
            "height is 19/√17 ≈ 4.609, giving the same 9.5.",
            "Two independent routes to the same value.", "R"),
           ("12.4.11", "A student claims that because a model fits ten data points exactly, "
            "it must be correct. Evaluate.",
            "No: a model that fits its data exactly may be over-fitted, and it must be "
            "tested against data not used in the fit before any claim is made.",
            "Distinguish fitting data from test data.", "R"),
           ("12.4.12", "A student's solution to an SSA problem reports one triangle "
            "without checking. Identify the error and state the correct procedure.",
            "The ambiguous case was not checked: compare the given side with the "
            "perpendicular height, and report zero, one or two triangles accordingly.",
            "The comparison is made before any angle is computed.", "R")],
    ),
    assessment=[
        dict(title="A1 · The cumulative paper",
             text="A paper contains five questions: a quadratic equation, a general "
                  "triangle, a geometric series, a screening probability and a linear "
                  "program. For each, name the method you choose, justify the choice in one "
                  "sentence, solve it, and check the answer by a second route. Then state "
                  "one thing your solutions collectively do not show.",
             note="Criteria C and D · choose and justify a method for each question, check "
                  "each answer, and state the limit."),
        dict(title="A2 · The unfamiliar problem",
             text="A problem states that a pattern of squares has 1, 5, 13 and 25 small "
                  "squares in its first four figures. Find the number in the tenth figure, "
                  "justify your formula, and then state one thing your justification does "
                  "not show.",
             note="Criteria C and D · find the structure, justify the formula, and state "
                  "the limit of the justification."),
    ],
    reflection=[
        "Write the statement of inquiry for this chapter in your own words.",
        "Which mathematical ideas from this chapter did you use to understand it? Name at least two.",
        "How did the key concept of logic and the related concepts of generalisation, "
        "representation and justification appear in your work?",
        "How is the global context of identities and relationships, and its exploration of "
        "how mathematical habits shape the way we reason elsewhere, visible in the "
        "investigations and examples you completed?",
        "Use evidence from an investigation or a worked example to justify your answer.",
        "Has your understanding of the statement of inquiry changed since the start of the "
        "chapter? Explain how.",
        "What are the limits of what you have shown in this course, and what would you "
        "still like to ask?",
    ],
    review=dict(
        ideas=["A question is classified by its structure, and the structure decides the "
               "method.",
               "Factorising, the quadratic formula and completing the square are three "
               "methods for one class of equation.",
               "The sine rule and the cosine rule are distinguished by whether the given "
               "angle is included.",
               "Two sides and a non-included angle give zero, one or two triangles.",
               "Circle theorems are chosen by naming the arc, the tangent or the chords.",
               "A three-dimensional problem is solved by choosing a plane.",
               "Skewed data call for the median and the interquartile range.",
               "Bayes' theorem reverses the conditioning, and the base rate decides the "
               "difference.",
               "A linear program's optimum is at a vertex, with a robustness statement.",
               "Examples suggest a conjecture; only an argument covering every case proves "
               "it."],
        vocab=["structure", "method", "justification", "check", "generalisation",
               "representation", "limit", "conjecture", "proof", "extended reasoning",
               "examination technique", "readiness", "transition", "maturity", "over-fitted"],
        mixed=[("12.R1", "Solve 3x² − 7x + 2 = 0 by two methods."),
               ("12.R2", "A triangle has a = 8, b = 11 and A = 40°. How many triangles "
                "exist?"),
               ("12.R3", "Find the sum of the first 12 terms of 5, 8, 11, …"),
               ("12.R4", "A disease affects 1 in 200. A test is 95 per cent sensitive with "
                "a 5 per cent false-positive rate. Find P(disease ∣ positive)."),
               ("12.R5", "Maximise P = 4x + 5y subject to x + y ≤ 6, x + 2y ≤ 8, x ≥ 0, "
                "y ≥ 0."),
               ("12.R6", "State the four skills named in the inquiry statement of this "
                "chapter.")],
    ),
    projects=dict(
        service=[("Community need", "Students leaving school are not shown what the next "
                                    "stage expects."),
                 ("Mathematical connection", "The whole course, and the habits it builds."),
                 ("Proposed action", "Interview two people who use mathematics in their "
                                     "work, identify the four skills they rely on, and "
                                     "publish the findings for younger students."),
                 ("Expected impact", "Younger students see what the habits are for."),
                 ("Student reflection", "Record the interviews and the skills you "
                                        "identified.")],
        community=[("Project idea", "A readiness audit of the school's mathematics "
                                    "students."),
                   ("Need", "Students choose their next course by how easy it looks rather "
                            "than by what they will do next."),
                   ("Research question", "Which of the four skills are strongest in the "
                                         "school's students, and what would each need to "
                                         "practise?"),
                   ("Mathematics", "All strands, and the habits that connect them."),
                   ("Action or outcome", "A one-page readiness profile with a practice for "
                                         "each gap."),
                   ("Beneficiaries", "Every student choosing a next course."),
                   ("Evidence", "The profile and the evidence behind each rating.")],
        personal=[("Personal interest", "A subject or career you are considering."),
                  ("Learning goal", "To identify which of the four skills that path needs "
                                    "most and practise it."),
                  ("Product or outcome", "A personal readiness profile with a practice "
                                         "plan."),
                  ("Mathematics", "All strands, and the habits that connect them."),
                  ("Process", "Rate the four skills against examples, and choose a practice "
                              "for the weakest."),
                  ("Evidence", "The profile and the practice plan.")],
    ),
),
])
