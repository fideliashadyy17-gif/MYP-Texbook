#import "../shared/personal-pages.typ": author
#set document(title: "Mathematics · MYP1 · Fractions and decimals", author: author)
#let ink = rgb("102b40")
#let teal = rgb("006e67")
#let mist = rgb("e9f5f2")
#set page(paper: "a4", margin: (x: 23mm, y: 21mm), header: align(right, text(size: 8pt, fill: teal)[MATHEMATICS / MYP1 / FRACTIONS]), numbering: "1")
#set text(size: 11pt, fill: ink)
#set par(leading: .72em)
#show heading: set text(fill: teal)
#let example(title, body) = block(width: 100%, fill: mist, inset: 10pt, radius: 4pt, [#strong(title) #parbreak() #body])
= 03 / Fractions and decimals
= 04 / Fractions and decimals
#text(fill: teal, weight: "bold")[MYP1 STUDENT COURSEBOOK · CHAPTER PROOF]

A kitchen makes eight portions from one batch of batter. A cook needs twelve portions, but the measuring jug and the recipe use different markings. What must remain unchanged when the amount of batter changes? How can the cook tell whether a convenient decimal measurement is close enough?

#example([Inquiry lens], [*Key concept:* relationships. *Related concepts:* equivalence and representation. *Global context:* scientific and technical innovation.

*Statement of inquiry:* Equivalent representations can make the same quantity easier to compare, calculate or measure, but the choice of representation matters when accuracy is limited.])

- *Factual:* What makes two fractions equivalent?
- *Conceptual:* Why does a common denominator help addition but not need to appear in multiplication?
- *Debatable:* When is a rounded measurement better than an exact but impractical instruction?

== Learning route
Represent and simplify fractions; compare quantities by benchmarks and common units; use the four operations; connect decimal place value to fractions and explain when a decimal expansion stops.

== First look / Which share is bigger?
One group gets three slices from a six-slice tray. Another gets four slices from an eight-slice tray. Predict which gets more, draw the trays as two equal-length bars, and then ask what changes if the trays are not the same size. Compare explanations with a partner and underline where each explanation names the whole.
#pagebreak()
= 4.1 / Equivalent fractions and simplest form
The denominator counts how many equal parts make one whole. The numerator counts how many of those parts the fraction names. Each third below is split into two sixths. The shaded amount stays fixed, but the number and size of the units change.

#let strip(parts, shaded) = grid(columns: parts, gutter: 0pt, ..range(parts).map(i => rect(width: 100%, height: 15pt, stroke: .6pt + ink, fill: if i < shaded { teal } else { mist })))
#figure(block(width: 75%)[#strip(3,2) #v(3pt) #strip(6,4)], caption: [The equal-length strips show two thirds and four sixths of the same whole.])

Multiplying or dividing both parts of a fraction by the same non-zero number preserves its value. For positive integer fractions, *simplest form* means the numerator and denominator share no factor greater than 1.

#example([Worked example / Choose a common factor], [The HCF of 18 and 24 is 6. Divide both by 6: $18/24 = 3/4$. Alternatively divide both by 2, then by 3. Either route gives the same simplest form, because both routes remove the same common factors.])

== Practice 4.1
+ Draw equal-length strips to show $3/5$ and $9/15$. Explain what changed and what stayed fixed.
+ Complete $4/7 = square/35 = 24/square$. Then write two more equivalents.
+ Reduce $21/49$, $48/60$ and $45/36$ to simplest form. Which result is greater than one?
+ A student claims $6/11=7/12$ because both numbers increased by one. Test this with a common denominator.
+ There are 28 red and 35 blue counters. Write the fraction of all counters that is red. Explain why $28/35$ answers a different question.
+ Find all fractions equivalent to $3/4$ whose positive whole-number numerator plus denominator is less than 25. Explain how you ruled out another pair.
#pagebreak()
= 4.2 / Comparing and ordering fractions
When wholes are equal, more parts of the same size mean a greater amount. A common denominator expresses fractions in the same-sized unit. Sometimes a benchmark such as one half is quicker: if one fraction is below a half and the other above it, you can order them without converting.

#example([Worked example / Compare close to one], [Compare $7/8$ and $9/10$. Their gaps from 1 are $1/8$ and $1/10$. A tenth is smaller than an eighth, so $9/10$ has the smaller gap and is larger. As a check, the common denominator 40 gives $35/40 < 36/40$.])

#table(columns: 4, align: center, fill: (x,y) => if y == 0 { mist }, [Fraction], [$3/8$], [$1/2$], [$5/8$], [Eighths], [3], [4], [5])

== Practice 4.2
+ Use one-half as a benchmark to compare $4/9$ and $6/11$. Explain without using decimals.
+ Order $7/12$, $3/4$, $5/6$ and $2/3$ in increasing order. Show how the common unit helps.
+ Set A has completed 23 of 25 tasks; set B has completed 17 of 18. Compare the fractions *unfinished* first, then decide which fraction completed is greater.
+ Find two different fractions with denominator 24 strictly between $1/3$ and $1/2$. Show there is at least one more.
+ A student says any fraction with a larger denominator must be smaller. Give a counterexample and a condition under which the rule would work.
+ Find the smallest positive whole denominator $d$ such that $1/2 < 3/d < 3/4$. Give all possible denominators, explaining why neither boundary works.
#pagebreak()
= 4.3 / Adding and subtracting fractions
Fractions can be added or subtracted once they count equal-sized pieces of the same whole. Use a common denominator to make those pieces match, then add or subtract the number of pieces. Do not add denominators: the pieces do not change size after the conversion.

#example([Worked example / Use twelfths], [From a full roll, cut $1/3$ of the original length in the morning and $1/4$ of the original length later. Both amounts refer to the same roll. The total is $4/12 + 3/12 = 7/12$, leaving $5/12$. Had the second amount meant one quarter of what remained, its denominator would describe parts of a different whole.])

== Practice 4.3
+ Calculate $2/9+4/9$, $2/3+1/8$ and $5/6-3/10$. Simplify each result.
+ Add the mixed numbers $1 + 3/4$ and $2 + 5/6$. Explain how you regroup a whole from the fractional sum.
+ A student writes $3/5-1/2=2/3$. Predict whether the result should be greater or less than $3/5$, then repair the calculation.
+ Find the missing fraction in $square+5/12=7/8$. Verify by addition after subtracting.
+ A tank loses $1/6$ of its full capacity in the morning and $1/4$ of its full capacity later. It started with $5/6$ of capacity. What fraction remains? Draw one bar representing full capacity.
+ Find two distinct unit fractions (fractions with numerator 1) that sum to $5/6$. Prove that the larger fraction must be at least $5/12$, then use that bound to justify your choice.
#pagebreak()
= 4.4 / Multiplying and dividing fractions
Multiplying by a fraction means taking that fraction of a quantity. For $2/3$ of $3/5$, shade three columns of a five-column grid, then select two of its three rows. The overlap covers six of fifteen equal cells.

#figure(grid(columns: 5, gutter: 1pt, ..range(15).map(i => rect(width: 19pt, height: 12pt, fill: if calc.rem(i, 5) < 3 and i < 10 { teal } else if calc.rem(i, 5) < 3 { rgb("addbd3") } else { mist }, stroke: .4pt + ink))), caption: [Six dark cells make $6/15 = 2/5$ of the whole grid.])

Dividing asks how many groups of the divisor fit, including parts of a group. Converting both quantities to the same unit makes the question a comparison of counts. This gives the same result as multiplying by the *reciprocal*, which swaps the numerator and denominator of the non-zero divisor.

#example([Worked example / Count groups], [How many $3/8$-litre portions are in $3/4$ litre? In eighths, there are six units to divide into groups of three, so there are two portions. Using the reciprocal gives $3/4 times 8/3 = 2$.])

== Practice 4.4
+ Find $2/3$ of 45 and $5/8$ of $4/5$. Use cancellation and describe what it does.
+ Evaluate $7/10 div 1/5$ using a common unit, then check using reciprocals.
+ Find $3/4 div 5/6$. Before calculating, explain why the result is less than one but greater than $3/4$.
+ A jug is $3/5$ full. A cook uses $1/3$ of what is in it. What fraction of its full capacity is left? Explain why subtracting $1/3$ directly gives the wrong answer.
+ A ribbon of length $5/2$ m is cut into pieces of length $3/8$ m. Find the number of full pieces and the leftover length. Explain why the quotient is not the leftover length.
+ Find a positive fraction less than one for which multiplying $3/4$ by it gives exactly half the result of dividing $3/4$ by it, or prove no rational fraction can do this. Hint: think about the exponents of 2 in the resulting squared numerator and denominator.
#pagebreak()
= 4.5 / Decimal place value and calculation
In 4.305 the 3 counts tenths, the 0 shows there are no hundredths and the 5 counts thousandths. The number is $4 + 3/10 + 5/1000$. Trailing zeros do not add quantity, so 4.3 and 4.300 are equal. When adding or subtracting, align the decimal points so that like units match.

#example([Worked example / Track the decimal unit], [To multiply 0.24 by 0.3, multiply 24 hundredths by 3 tenths. A hundredth of a tenth is one thousandth, so the answer is 72 thousandths, or 0.072. To divide 1.26 by 0.3, multiply both quantities by 10: $12.6 div 3 = 4.2$. Scaling both quantities preserves how many times one fits into the other.])

== Practice 4.5
+ Write 6.032 and 0.406 as sums of place-value contributions. State the value of the digit 6 in each number.
+ Order 0.404, 0.44, 0.4 and 0.044. Explain where 0.400 belongs.
+ Calculate $3.08+0.742$ and $5.2-3.867$. Explain the alignment used.
+ Evaluate $0.06 times 1.4$ and $2.52 div 0.6$. Use estimation to check your decimal placement.
+ Two sticks measure 2.495 m and 2.486 m. Round each to the nearest hundredth; find the exact difference and compare with the difference of the rounded readings.
+ A student says $0.3 times 0.7 = 0.21$ must be wrong because multiplication makes numbers larger. Explain the mistake with a diagram or a measurement context.
#pagebreak()
= 4.6 / Fractions and decimals name the same numbers
Dividing a fraction’s numerator by its denominator gives its decimal expansion. Every terminating decimal is a fraction with denominator a power of ten: for example, $0.036 = 36/1000 = 9/250$. Some fractions need infinitely many digits instead. For example, division for $1/3$ repeats the same remainder, so the digit 3 repeats forever. The rounded value 0.33 is not exactly one third.

#example([Worked example / Check for termination], [$7/20 = 35/100 = 0.35$. The denominator 20 divides 100. In simplest form, a fraction terminates exactly when its denominator divides some power of ten. Since powers of ten contain only 2s and 5s as prime factors, a simplified denominator containing another prime cannot terminate. Conversely, any product of 2s and 5s divides a sufficiently large power of ten.])

== Practice 4.6
+ Convert $3/8$, $7/25$ and $11/40$ to terminating decimals using equivalent fractions.
+ Convert 0.45, 0.125 and 2.04 to fractions in simplest form.
+ Predict whether $3/12$, $5/12$, $9/30$ and $7/30$ terminate. Simplify before deciding.
+ In the division for $2/3$, record the first three steps and explain why the same remainder keeps returning. Round to two decimal places and say which number is larger, the fraction or the rounded result.
+ Place $0.58$, $7/12$ and $3/5$ in order. Show at least one exact comparison rather than rounding all three first.
+ Two terminating decimals differ by 0.01. Find a pair such that $1/3$ lies strictly between them. Verify using fractions.
#pagebreak()
= Consolidate / Scale a recipe and test the result
== Investigate / How long does a terminating decimal need?
Find the minimum number of digits after the point for $1/2$, $1/4$, $1/8$, $1/5$, $1/25$, $1/20$ and $1/40$. Write the denominator as a product of 2s and 5s before each conversion. Predict the minimum number for $1/200$ without dividing. Justify a rule by asking how many of each factor appear in $10^k$. Test whether your rule needs a “simplest form” condition, using $5/40$.

== Model / A kitchen trial
An eight-portion recipe uses $3/4$ L milk and $2/5$ L water. A cook prepares twelve portions using the same recipe ratios. The jug is marked every 0.05 L and holds at most one litre. The cook can make repeated pours and wants each ingredient within 0.02 L of the target.

+ Find the scale factor and both exact target volumes. Explain which can be measured exactly using the markings.
+ Find the two adjacent measurable totals around any target that is not exactly measurable. Can the cook meet the tolerance by using only the jug marks? Explain why repeated pours do not remove that limitation.
+ A second cup has a 0.025 L mark. Give a practical sequence of pours and check both totals. Explain one source of error the idealised markings do not cover.
+ The cook accidentally adds 1.15 L of milk before the water. If no milk can be removed, find the water volume that would preserve the original milk-to-water ratio. Explain whether matching that ratio alone guarantees twelve original-size portions.

== Mixed review
+ Give a fraction with denominator 36 equivalent to $5/9$; order it with $2/3$ and 0.54.
+ Evaluate $3/4-1/6$ and $3/4 div 1/6$. Explain why the results describe different actions.
+ Decide whether $0.7 div 0.04$ is closer to 2, 20 or 200, then calculate it.
+ *Challenge:* Find all positive integers $n$ for which $1/n$ lies strictly between 0.1 and 0.2. Which give a terminating decimal? Give a reason why no other value of $n$ works.

#example([Reflect], [For each kitchen calculation, decide whether to keep a fraction or switch to a decimal. Explain one place where switching too early could change a decision.])
