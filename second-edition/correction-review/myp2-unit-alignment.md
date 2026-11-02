# MYP 2 — unit alignment for the whole coursebook

Prepared for review. The approved MYP 1 prototype, the MYP 2 architecture and
the approved interior are unchanged: the alignment framework was applied
*inside* the existing page model, as additions in space that was previously
empty.

## 1. Status of the work

* Everything is on branch `arena/c767ce09-myp-texbook`. The pre-alignment MYP 2
  build was preserved first (commit `6adf119`), then the Chapter 1 pilot was
  committed (`84c54dc`), and this full-book pass is the working state.
* Exported book: **422 pages, 3 309 224 bytes**, A4, fonts embedded,
  **0 overflow, 0 placeholders, 0 raw maths, 0 KaTeX errors, 0 console
  errors**, 517 practice items / 517 answers, 44 answer pages, 14 KaTeX
  expressions; mechanical QA `book-qa.json` → **STATUS: PASS**.
* Alignment audit: **165 / 165 points** across the eleven chapters
  (`python3 unit_alignment_audit.py`), against a baseline of **93 / 165**.
* Chapter start pages: 11, 45, 79, 108, 142, 176, 205, 239, 273, 302, 336;
  answers 370, formula bank 414, glossary 418, references 421, back cover 422.

## 2. What was added, and where

Four additions, all rendered by existing page types and existing CSS classes:

| Addition | Where it appears | Rendered by |
| --- | --- | --- |
| **Global context exploration** | chapter opener, under the global context in the *Framing the inquiry* card | a new row in the existing opener card |
| **Inquiry question** | investigation page, above *Your task* | `.callout` with the existing `.label` |
| **Statement of inquiry as a statement** | chapter opener, in the *Framing the inquiry* card | the existing opener card |
| **Returning to the statement of inquiry** | a third review page, after the mixed practice | `.callout` (the statement itself) + `.assessment-task` + `.construction-space` |

No new page structure, no new palette, no new typography, no change to the
running heads, no change to the chapter or section sequence. The renderer is
conditional: a chapter without an exploration, an inquiry question or a
reflection renders exactly as it did before.

### Pagination

The closing reflection is a **third review page** rather than a block squeezed
under the key ideas and vocabulary, because the seven prompts plus a writing
space do not fit beside the review summary. This follows the standing rule to
add pages rather than overcrowd them: the book grew from 411 to **422 pages**
(eleven new review pages). Every chapter is otherwise the same length it was.

## 3. Diagnosis that motivated the change

The audit of the eleven chapters as they stood found four uniform gaps:

1. no global context **exploration** was named (0 / 11);
2. no investigation opened with a formulated **inquiry question** (0 / 41);
3. no chapter closed with a **reflection returning to the statement of
   inquiry** (0 / 11);
4. the statements of inquiry were **phrased as questions** and named neither
   the key concept nor the related concepts nor the exploration, so the
   central thread of the unit could not be traced from the opening inquiry to
   the closing reflection.

A further defect was found while applying the framework: **only Chapter 1 used
an official IB global context** ("Fairness and development"). Chapters 2–11
carried invented contexts — "Cooking and construction", "Transport and trade",
"Weather and finance", "Design and budgeting", "Design and nature", "Design and
construction", "Packaging and construction", "Art, design and architecture",
"Games and risk", "Surveys and reports" — which are not IB global contexts.
Each has been remapped to an official global context with an official
exploration, chosen so that the mathematics of the chapter genuinely carries it:

| Chapter | Invented context (removed) | Official global context | Official exploration |
| --- | --- | --- | --- |
| 1 Ratios and equivalent ratios | *(already official)* | Fairness and development | Inequality, difference and inclusion |
| 2 Proportional reasoning | *(none)* | Globalisation and sustainability | Markets, commodities and commercialisation |
| 3 Rates and conversions | *(none)* | Scientific and technical innovation | Precision, accuracy and measurement |
| 4 Integers and their operations | *(none)* | Orientation in space and time | Natural and human landscapes and resources |
| 5 Algebraic expressions and equations | *(none)* | Scientific and technical innovation | Products, processes and solutions |
| 6 Numerical patterns and generalisation | *(none)* | Personal and cultural expression | Artistry, craft, creation and beauty |
| 7 2D geometry | Design and construction | Globalisation and sustainability | Urban and rural planning |
| 8 3D geometry | Packaging and construction | Globalisation and sustainability | Human impact on the environment |
| 9 Transformations and symmetry | Art, design and architecture | Personal and cultural expression | Artistry, craft, creation and beauty |
| 10 Probability and simulation | Games and risk | Scientific and technical innovation | Randomness, chance, risk and uncertainty |
| 11 Univariate data | Surveys and reports | Globalisation and sustainability | Population and demography |

(The contexts recorded for chapters 2–6 in the source file at the time of the
diagnosis were working labels; the table records the official ones now in the
book.)

## 4. The chapter-by-chapter alignment

Each statement of inquiry is a claim that the chapter investigates: it names the
key concept, the related concepts and the global context with its exploration,
and it is written for Year 2 students rather than copied from another chapter.
The three question categories are derived from the same elements, and each
investigation opens with a question that its own mathematical conclusion then
answers.

#### Chapter 1 · Ratios and equivalent ratios

| Element | Content |
| --- | --- |
| Key concept | Form |
| Related concepts | Equivalence · Representation |
| Global context | Fairness and development |
| Global context exploration | Inequality, difference and inclusion |
| Statement of inquiry | *The form of a ratio, and the equivalence of its different representations, allow a limited resource to be shared fairly and allow that fairness to be justified and checked.* |
| Factual question | What does the ratio 3:5 compare, what is its simplest form, and how do you generate ratios equivalent to it? |
| Conceptual question | Why can one ratio describe many different-sized situations, and how does representing it as a unit rate or a ratio table change what you are able to compare? |
| Debatable question | Is a ratio always the fairest way to share a limited resource, and how could you use mathematical evidence to defend your position? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 1.1 Understanding ratio language | How can one ratio describe a comparison between two quantities, and what does its simplest form tell us about that comparison? | a : b = (ak) : (bk) for any non-zero number k, so one ratio can describe the comparison in any size, and its simplest form is the shortest honest description of that comparison. |
| 1.2 Equivalent ratios and simplest form | What stays the same when both parts of a ratio change, and how can you tell whether two ratios describe the same comparison? | What stays the same is the comparison: equivalent ratios are exactly the ratios that reduce to the same simplest form, whatever the size of the numbers. |
| 1.3 Ratio tables and double number lines | How can a ratio table or a double number line find a missing value in a comparison without guessing? | A missing value is found by locating the multiplier in one row and applying it to the other, which is why the table and the number line never need trial and error. |
| 1.4 Sharing and comparing with ratios | When is a sharing rule fair, and how can you check that a sharing really matches the rule that was agreed? | A sharing is fair when the rule is stated first and the result is checked: find the value of one part, then verify both the total and the simplest form. |


#### Chapter 2 · Proportional reasoning

| Element | Content |
| --- | --- |
| Key concept | Relationships |
| Related concepts | Equivalence · Representation · Logic |
| Global context | Globalisation and sustainability |
| Global context exploration | Markets, commodities and commercialisation |
| Statement of inquiry | *A proportional relationship models two quantities that change together; the equivalence of its representations as a table, a unit rate and a straight line through the origin rests on the logic of one constant multiplier, and allows costs and scales to be compared, justified and predicted.* |
| Factual question | What is a proportional relationship, what is its constant of proportionality, and how do you recognise one in a table, an equation and a graph? |
| Conceptual question | Why does every proportional relationship graph as a straight line through the origin, and what does the slope tell you that a table alone does not? |
| Debatable question | When two offers are compared per unit, is the cheaper unit price always the fairer choice for a buyer with very little money? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 2.1 Recognising proportional relationships | How can you tell whether two quantities really change together in a proportional relationship, and what single number describes it? | A relationship is proportional exactly when every quotient is the same, and that one quotient is the constant of proportionality k in y = kx. |
| 2.2 Unit rates and comparison | How does converting two different offers to the same unit rate turn an unfair comparison into a fair one? | Converting to a common unit rate puts both offers on the same basis, and that unit rate is the constant of proportionality, so it is unique to the situation. |
| 2.3 Graphs of proportional relationships | What does the graph of a proportional relationship show that a table of values cannot show? | The graph shows the rate of growth as steepness: proportional relationships graph as straight lines through the origin whose slope is the constant k. |
| 2.4 Scaling and real-world models | When a shape or a quantity is scaled, what changes and what must stay the same for the model to remain faithful? | Under a scale factor k, lengths scale by k, areas by k² and volumes by k³, so the shape stays the same while each measure changes by its own power of k. |


#### Chapter 3 · Rates and conversions

| Element | Content |
| --- | --- |
| Key concept | Logic |
| Related concepts | Representation · Equivalence |
| Global context | Scientific and technical innovation |
| Global context exploration | Precision, accuracy and measurement |
| Statement of inquiry | *A rate compares quantities of different kinds, and the logic of converting units precisely relies on the equivalence of different representations of the same quantity, which allows speeds, densities and pressures to be measured, compared and trusted.* |
| Factual question | What two units does a rate compare, and how do you convert between compound units such as km/h and m/s? |
| Conceptual question | Why does converting to the smaller unit before dividing protect the accuracy of a rate, and how does a unit rate make unlike quantities comparable? |
| Debatable question | Is an average speed ever an honest description of a journey, and what evidence would you need to defend your answer? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 3.1 Understanding rates | How can one number compare two journeys of different lengths and durations? | One number — total distance ÷ total time — compares journeys of any length and duration, which is why average speed is defined from totals. |
| 3.2 Converting units | How can the same rate be written in different units without changing its value? | Converting units is proportional reasoning with a fixed constant, so the same rate can be written in different units without changing its value. |
| 3.3 Density and pressure | How can a rate compare objects of different sizes and shapes fairly? | Density and pressure are rates, so dividing by the size — volume or area — compares objects of different sizes fairly: density = mass ÷ volume and pressure = force ÷ area. |


#### Chapter 4 · Integers and their operations

| Element | Content |
| --- | --- |
| Key concept | Logic |
| Related concepts | Representation · Patterns |
| Global context | Orientation in space and time |
| Global context exploration | Natural and human landscapes and resources |
| Statement of inquiry | *Signed numbers are a representation of position relative to a chosen reference point, and the logic of direction on the number line, together with the patterns in the sign rules, allows changes in temperature, depth and balance to be described, ordered and predicted.* |
| Factual question | What is an integer, how are integers ordered on the number line, and what does the sign of a number tell you? |
| Conceptual question | Why does subtracting a negative number increase the value, and how does the number line explain each of the sign rules? |
| Debatable question | Is a negative balance or a negative temperature a real quantity, or only a convention about where we place zero? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 4.1 The integer number line | How can a single line represent numbers both above and below a reference point, and how does it decide which of two integers is greater? | One line with a chosen reference point represents numbers in both directions: opposites are symmetric about zero and sum to zero (a + (−a) = 0), and the further right a number lies the greater it is. |
| 4.2 Adding and subtracting integers | How can the number line explain what happens when a negative number is added or subtracted? | Addition is a move along the line, so subtracting a negative moves right, and the total of a set of moves does not depend on the order in which they are made. |
| 4.3 Multiplying and dividing integers | Where do the sign rules for multiplication and division come from, and why is a negative times a negative positive? | The sign rules come from continuing a pattern rather than from a separate law: same signs give a positive product or quotient, different signs give a negative one. |
| 4.4 Integers in context | How can signed numbers describe a change in a real quantity such as temperature, depth or balance? | A change is the difference of two signed values measured from the same reference point, so its sign shows the direction of the change. |


#### Chapter 5 · Algebraic expressions and equations

| Element | Content |
| --- | --- |
| Key concept | Logic |
| Related concepts | Patterns · Representation |
| Global context | Scientific and technical innovation |
| Global context exploration | Products, processes and solutions |
| Statement of inquiry | *A variable represents an unknown or changing quantity, and the logic of equivalence between different representations of the same relationship, together with the patterns in its structure, allows one expression or equation to model many situations, so that processes can be designed, solved and checked.* |
| Factual question | What does a variable represent, what are like terms, and how do you build an expression from a written description? |
| Conceptual question | Why can 3x and 5x be collected but 3x and 5 cannot, and how does expanding show that two expressions are equivalent? |
| Debatable question | Is algebra a new kind of mathematics or a shorthand for arithmetic, and what would count as evidence for your view? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 5.1 Building expressions | How can a letter stand for a number so that one expression describes every possible case? | A variable lets one expression act as a rule for every case: substituting a value applies the rule. |
| 5.2 Simplifying and expanding | What makes two expressions the same, and how can you show it without testing every number? | Two expressions are equivalent when they agree for every value of the variable, which is why expanding and collecting change the form but never the value. |
| 5.3 Solving equations | How can an equation be solved by keeping it true at every step? | An equation is solved by keeping it true at every step: applying the same operation to both sides preserves the solution. |
| 5.4 Equations in context | How can an equation model a real situation, and how do you decide whether its solution is meaningful? | Solve, then check that the answer makes sense in the original situation, because the context decides which solutions are acceptable. |


#### Chapter 6 · Numerical patterns and generalisation

| Element | Content |
| --- | --- |
| Key concept | Patterns |
| Related concepts | Relationships · Logic |
| Global context | Personal and cultural expression |
| Global context exploration | Artistry, craft, creation and beauty |
| Statement of inquiry | *A numerical pattern describes relationships between position and value, and the logic of generalisation allows one rule to describe and predict every term, which is how patterns in design and nature are created, extended and reproduced.* |
| Factual question | What is a numerical sequence, what is the nth term, and how do you describe a pattern in words and in symbols? |
| Conceptual question | How do you know a rule is correct for every term and not only for the terms you checked, and what do the differences tell you about the rule? |
| Debatable question | Is finding a pattern the same as proving it, and what would you accept as proof? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 6.1 Describing sequences | How can a list of numbers be described so that any term can be found without listing them all? | A list can be described by its differences: constant differences give a linear rule and constant second differences a quadratic one, so the nth triangular number is n(n + 1)/2. |
| 6.2 From pattern to formula | How can a pattern be turned into a formula that works for every position? | A formula replaces listing: it is a generalisation that holds for every position and can be tested on a term that has not yet been counted. |
| 6.3 Graphs of sequences | What can a graph of a sequence show that the list of terms cannot show? | Steepness and curvature compare growth rates that a list of numbers hides, so a graph shows which rule grows faster and where the order changes. |


#### Chapter 7 · 2D geometry: angles, perimeter and area

| Element | Content |
| --- | --- |
| Key concept | Form |
| Related concepts | Logic · Representation |
| Global context | Globalisation and sustainability |
| Global context exploration | Urban and rural planning |
| Statement of inquiry | *The form of a two-dimensional shape, and the logic of how its parts relate, are represented by formulas for perimeter and area, and that representation allows spaces to be measured, planned and costed when land, flooring and materials are limited.* |
| Factual question | What is the difference between perimeter and area, and which formula gives each for a rectangle, a triangle and a circle? |
| Conceptual question | Why does the angle sum of a triangle always equal 180°, and how do the properties of a shape produce its perimeter and area formulas? |
| Debatable question | When a community space is planned with a limited budget, is the cheapest shape per square metre always the best choice? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 7.1 Angles and their relationships | What relationships exist between angles formed by lines, and why do they always hold? | Angle relationships come from straight lines, full turns and parallel lines, and they combine to give the angle sum of a polygon with n sides as (n − 2) × 180°. |
| 7.2 Perimeter of 2D shapes | How is the boundary of a shape measured, and how does the perimeter formula follow from the shape's properties? | Perimeter is the total boundary length, and each formula is a shortcut that follows from the properties of that shape. |
| 7.3 Area of 2D shapes | How is the surface covered by a shape measured, and where does each area formula come from? | Every area formula can be derived by cutting and rearranging into a rectangle, so area of a parallelogram = base × height. |
| 7.4 Using properties to solve problems | How can the properties of a shape be used to find a missing measurement? | Quadrilaterals form a hierarchy in which the more specialised shape has more properties, and those properties supply the equations that find a missing measurement. |


#### Chapter 8 · 3D geometry: volume and surface area

| Element | Content |
| --- | --- |
| Key concept | Form |
| Related concepts | Logic · Representation |
| Global context | Globalisation and sustainability |
| Global context exploration | Human impact on the environment |
| Statement of inquiry | *The form of a solid, and the logic of how its faces and cross-sections relate, are represented by formulas for volume and surface area, and that representation allows the material used for containers to be measured and reduced.* |
| Factual question | What is the difference between volume and surface area, and which formula gives each for a cuboid, a cylinder and a prism? |
| Conceptual question | Why do two solids with the same volume have different surface areas, and how does a net reveal the surface area of a solid? |
| Debatable question | Is the most efficient shape for packaging always the best choice for the environment, and how would you use mathematics to argue your case? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 8.1 Naming and drawing solids | How can a solid be described so that its faces, edges and vertices can be counted without seeing all of them? | A solid is described by its faces, edges and vertices, and a net lays every face out flat, so a cuboid always has 6 faces, 12 edges and 8 vertices. |
| 8.2 Volume of prisms and cylinders | How can the space inside very different solids be measured with one rule? | One rule covers every prism — volume = area of cross-section × length — of which volume of a cuboid = length × width × height is the special case. |
| 8.3 Surface area of solids | How can the material needed to cover a solid be measured, and why does the same volume need different amounts of material? | Surface area is the sum of the face areas, so it depends on shape and not only on volume: for a fixed volume the shape closest to a cube uses the least material. |
| 8.4 Solving 3D problems | How can volume, surface area and edge length be used together to solve a real problem about a container? | Volume, surface area and edge length are three distinct measures of one solid, and a real problem usually needs more than one of them. |


#### Chapter 9 · Transformations and symmetry

| Element | Content |
| --- | --- |
| Key concept | Form |
| Related concepts | Logic · Relationships |
| Global context | Personal and cultural expression |
| Global context exploration | Artistry, craft, creation and beauty |
| Statement of inquiry | *The form of a shape is preserved by transformations, and the logic of describing each movement precisely — and the relationships between them — allows patterns to be created, extended and recognised in art, craft and design.* |
| Factual question | What are the four basic transformations, and what information is needed to describe each one completely? |
| Conceptual question | Which properties of a shape are preserved under each transformation, and how are translations, reflections and rotations related to one another? |
| Debatable question | Is a reflected or enlarged shape still the same shape, and how would you defend your answer to a designer? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 9.1 Translations and reflections | How can a movement of a shape be described so that someone else can reproduce it exactly? | A movement is fully described by a vector or a mirror line, and combining them shows that reflections in perpendicular mirror lines are equivalent to a rotation of 180°. |
| 9.2 Rotations and enlargements | What changes and what stays the same when a shape is rotated or enlarged? | Rotation preserves length and angle, while an enlargement preserves angle only: under an enlargement of scale factor k, lengths scale by k and areas by k². |
| 9.3 Symmetry | How can symmetry be described and counted, and what does it tell you about a shape? | A shape's symmetry is fully described by its lines of symmetry and its rotational order, and counting them also checks a transformation. |


#### Chapter 10 · Probability and simulation

| Element | Content |
| --- | --- |
| Key concept | Relationships |
| Related concepts | Logic · Representation |
| Global context | Scientific and technical innovation |
| Global context exploration | Randomness, chance, risk and uncertainty |
| Statement of inquiry | *The relationship between an experiment and the outcomes it can produce is described by probability, and the logic of counting those outcomes — with representation as a sample space or a simulation — allows randomness to be quantified and risk to be assessed rather than guessed.* |
| Factual question | What does a probability of 0.5 mean, and how are experimental and theoretical probabilities calculated? |
| Conceptual question | Why can experimental results differ from theoretical probabilities, and how does the sample space connect the outcomes to the probabilities? |
| Debatable question | Is a simulation ever better than a real experiment, and what would you need to know about the risk before relying on it? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 10.1 Describing probability | How can chance be described as a number, and what does that number mean? | Probability is a number from 0 to 1 on a scale from impossible to certain, and experimental probability approaches theoretical probability as the number of trials grows. |
| 10.2 Sample spaces and listing outcomes | How can every possible outcome be counted so that none is missed? | Listing the full sample space prevents missing favourable outcomes, and its size gives the denominator of every theoretical probability. |
| 10.3 Probability rules | How do the probabilities of events combine, and what rules govern them? | The addition rule covers mutually exclusive outcomes, the multiplication rule covers independent stages, and more trials reduce the gap between experimental and theoretical probability. |
| 10.4 Simulation and fair games | How can a real experiment be replaced by a model, and when is a game fair? | A simulation is a model of a real experiment, and its rule must reproduce the probabilities; a game is fair when every player has the same chance of winning. |


#### Chapter 11 · Univariate data

| Element | Content |
| --- | --- |
| Key concept | Logic |
| Related concepts | Representation · Relationships |
| Global context | Globalisation and sustainability |
| Global context exploration | Population and demography |
| Statement of inquiry | *The logic of organising a data set, and the relationships between its values, are represented by displays, measures of centre and measures of spread, and that representation allows a sample to be reported honestly and used to describe a larger population.* |
| Factual question | What do the mean, median and mode measure, and what does each of the range and the IQR measure? |
| Conceptual question | Why can two data sets with the same mean look very different, and how does the choice of display change what the data appear to say? |
| Debatable question | Can an average ever be misleading when it is used to describe a whole population, and how would you argue for a fairer report? |
| Reflection prompts | 7, opening with the statement of inquiry itself |

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 11.1 Collecting and displaying data | How can a collection of data be organised and displayed so that its story is visible? | Data are organised in a table and displayed in a chart, and the display must match the data type and the question being asked. |
| 11.2 Measures of centre | How can the middle of a data set be summarised by a single number, and which single number is the fairest? | Each average summarises a different aspect of the data, so the mean uses every value, the median resists extremes and the mode suits categories. |
| 11.3 Measures of spread | How can the spread of a data set be summarised, and why does spread matter as much as centre? | Spread is measured by the range and the IQR, and a box plot shows centre, spread and extremes together. |
| 11.4 Interpreting and reporting data | How can a report about data be made honest, and what must it state before it draws a conclusion? | Report the centre, the spread and the sample before drawing a conclusion, because a conclusion about a population rests on the logic of how the sample was chosen. |



## 5. What was preserved

A page-by-page comparison of the exported PDF before and after this pass
(matching pages by their page id, ignoring the page number in the footer)
gives **312 pages textually identical** and **99 pages changed**. The 99 are
exactly and only the pages the framework touches:

| Page type | Count | Change |
| --- | --- | --- |
| chapter openers | 11 | exploration row, statement-form SOI, sharpened questions |
| investigation pages | 37 | inquiry-question callout above *Your task* |
| investigation notes pages | 37 | conclusion rewritten to answer the inquiry question |
| review summary pages | 11 | reflection block moved to its own page |
| contents pages | 4 | page numbers in the contents listing |

Chapter 1's four investigations were already aligned in the pilot, which is why
37 rather than 41 investigation pages changed. Everything else — the teaching
pages, the 82 worked-example pages, the 88 criterion A–D practice pages, the
assessment pages, the mixed-practice pages, the projects pages, the 44 answer
pages, the formula bank, the glossary, the references, the covers and the back
cover — is textually identical.

Within the changed pages nothing was removed: the engagement hook, the ATL
statement, the standfirst, the section titles, the investigation tasks, tables,
diagrams, the six-part worked examples, the practice items and their answers,
the review vocabulary and the Service as Action / Community Project / Personal
Project connections are all still present in their original wording and order.

## 6. Alignment audit

```
$ python3 unit_alignment_audit.py
Chapter 1  · Ratios and equivalent ratios            ->  15/15 points
Chapter 2  · Proportional reasoning                  ->  15/15 points
Chapter 3  · Rates and conversions                   ->  15/15 points
Chapter 4  · Integers and their operations           ->  15/15 points
Chapter 5  · Algebraic expressions and equations     ->  15/15 points
Chapter 6  · Numerical patterns and generalisation   ->  15/15 points
Chapter 7  · 2D geometry: angles, perimeter and area ->  15/15 points
Chapter 8  · 3D geometry: volume and surface area    ->  15/15 points
Chapter 9  · Transformations and symmetry            ->  15/15 points
Chapter 10 · Probability and simulation              ->  15/15 points
Chapter 11 · Univariate data                         ->  15/15 points

TOTAL: 165/165 alignment points across 11 chapter(s)
```

The tool reads `framework.py` only, so it can be re-run without building the
book. It checks, per chapter: the key concept is developed in the teaching
text; the related concepts are named in the statement of inquiry or the
teaching text; the global context and its exploration are present; the
statement of inquiry is a statement that connects them; the three question
categories are present and substantial; every investigation opens with an
inquiry question; every investigation has an observation and a conclusion
before the formal development; the worked examples and criterion A–D practice
are complete; the context is visible in the learning experiences; and the
reflection returns to the statement of inquiry.

## 7. How the MYP 1 prototype is preserved

* No MYP 1 source, export, cover or QA file has been touched; the MYP 1 build
  remains at 381 pages with QA STATUS: PASS.
* The MYP 2 pipeline still copies the MYP 1 architecture: the same page model
  (`.page`, running heads, page numbering), the same CSS class vocabulary, the
  same palette and typography, the same investigation → teaching → worked
  example → criterion practice → assessment → review → projects order.
* The additions reuse existing classes (`.callout`, `.label`,
  `.assessment-task`, `.construction-space`, `.review-grid`) and existing page
  types; no new page structure and no new visual language were introduced.
* MYP 1's own `framework.py` has no exploration, inquiry-question or reflection
  fields, which is why these are genuine additions rather than imports from a
  template that already had them.

## 8. Next step

MYP 3, MYP 4 and MYP 5, using the same framework with level-appropriate
statements of inquiry, inquiry questions and reflections written for each level
rather than copied from MYP 2.
