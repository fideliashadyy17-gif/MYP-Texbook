#import "../shared/personal-pages.typ": author
#set document(title: "Mathematics · MYP3 · The real number system", author: author)
#let ink = rgb("102b40")
#let teal = rgb("6c4383")
#let mist = rgb("e9f5f2")
#set page(paper: "a4", margin: (x: 23mm, y: 21mm), header: align(right, text(size: 8pt, fill: teal)[MATHEMATICS / MYP3 / REAL NUMBERS]), numbering: "1")
#set text(size: 11pt, fill: ink)
#set par(leading: .72em)
#show heading: set text(fill: teal)
#let example(title, body) = block(width: 100%, fill: mist, inset: 10pt, radius: 4pt, [#strong(title) #parbreak() #body])
= 03 / The real number system
= 01 / The real number system

A square cutting guide has a side of exactly one metre. Its diagonal is longer than 1.4 m but shorter than 1.5 m. A workshop can mark a decimal length, yet its drawing needs the exact diagonal. How can both descriptions be useful?

#example([Inquiry lens], [*Key concept:* logic. *Related concepts:* representation and justification. *Global context:* scientific and technical innovation. An exact representation and an approximation answer different questions; a proof establishes which conclusions survive a change of representation.])

- What makes a number rational?
- Why can a decimal approximation be useful without being exact?
- When should a workshop reject a mathematically accurate approximation?

*ATL:* Ask a partner to classify each of 0.101, $sqrt(2)$ and $sqrt(9)$, then compare the evidence rather than only the classifications.
#pagebreak()
= 1.1 / Rational numbers and decimal form
A rational number is a quotient $a/b$ of integers with $b != 0$. In long division there are only $b$ possible non-negative remainders for a positive divisor $b$. Once a remainder repeats, all subsequent digits repeat; a zero remainder gives a terminating expansion. Conversely a purely repeating block of $k$ digits can be converted by multiplying by $10^k$ and subtracting the original, making the repeating tails cancel.

#example([Worked example / A non-repeating start], [For $x=0.1 overline(6)$, set $10x=1.overline(6)$ and $100x=16.overline(6)$. Subtraction gives $90x=15$, hence $x=1/6$. The initial shift puts both repeating tails in the same position.])

+ Express 0.0325, $0.overline(27)$ and $0.2 overline(7)$ as reduced fractions.
+ Divide 5 by 12. Record the remainders and identify exactly which digits repeat.
+ A calculator shows $2/7$ as 0.28571429. Explain why this display is not the number’s exact decimal expansion.
+ Predict which of $7/24$, $9/24$, $13/40$ and $15/42$ terminate. Justify by reducing first, then considering factors of 10.
+ Explain why $0.overline(9)=1$ using the subtraction argument. What does this equality show about the uniqueness of decimal representations?
+ An unknown number has decimal form $0.overline(a b)$ with two distinct digits and lies strictly between $1/3$ and $2/5$. Find all possibilities if its numerator is even when written with denominator 99.
#pagebreak()
= 1.2 / Irrational numbers and surds
An irrational number cannot be written as a ratio of integers. Together the rational and irrational numbers make up the real numbers. A *surd* here is an irrational root kept in exact radical form. A radical is not automatically irrational: $sqrt(81)=9$. The diagonal of a unit square is $sqrt(2)$ by Pythagoras.

#figure(grid(columns: (auto,auto), gutter: 14pt, block(width: 54pt, height: 54pt, stroke: teal)[#place(top + left, line(end: (54pt,54pt), stroke: 1.2pt + teal))], [side lengths: 1 m #linebreak() diagonal: $sqrt(2)$ m]), caption: [Unit square; the diagonal joins opposite vertices.])

#example([Worked example / Bound without a calculator], [Since $1.41^2=1.9881$ and $1.42^2=2.0164$, we have $1.41<sqrt(2)<1.42$. Squaring preserves order for non-negative inputs. Keep $sqrt(2)$ when exact equality matters.])

+ Classify $sqrt(64)$, $-sqrt(11)$, $0.overline(31)$ and $pi$ as rational or irrational.
+ Find consecutive tenths bounding $sqrt(7)$ by squaring.
+ A square has area 30 square metres. Give an exact side and show it lies between 5.4 m and 5.5 m.
+ Find all positive integers below 35 whose square roots are rational, using that a rational square root of an integer must be an integer. Explain why the list ends where it does.
+ Give a non-terminating decimal that is rational. Explain what extra property a non-terminating decimal must have to be irrational.
#pagebreak()
= 1.3 / Order, absolute value and intervals
The absolute value $abs(x)$ is the distance from zero. The distance from $x$ to $c$ is $abs(x-c)$. An interval records every number between endpoints. Square brackets include an endpoint; round brackets exclude it. So $[2,5)$ means $2 <= x < 5$.

#example([Worked example / Read a tolerance], [The condition $abs(x-8)<=0.03$ allows any value within 0.03 of 8, including both boundaries. Hence $7.97<=x<=8.03$. In interval notation the set is $[7.97,8.03]$.])

+ Place $-sqrt(5)$, $-2.24$, $-2$, and $sqrt(5)$ in increasing order. Justify the closest comparison by squaring positive magnitudes.
+ Convert $-3<x<=4$ to interval notation and sketch it on a number line.
+ Translate $abs(x+2)<0.5$ into an interval. Is $-2.5$ allowed?
+ Find the intersection of $[1.8,2.4)$ and $(2.1,2.6]$. Name which condition excludes each new endpoint.
+ Write one absolute-value inequality that describes exactly all numbers from 6.8 through 7.6, endpoints included.
+ Find an interval of length 1.2 with midpoint $-0.3$ that includes the left but not the right endpoint. Explain why ordering negative numbers matters.
#pagebreak()
= 1.4 / Working with surds
For non-negative $a,b$, $sqrt(a b)=sqrt(a)sqrt(b)$. Extract the largest square factor to simplify. Only like radical parts combine by addition. The distributive law still applies to products.

#example([Worked example / Compare exact forms], [$sqrt(72)-sqrt(8)=6sqrt(2)-2sqrt(2)=4sqrt(2)$. To rationalise $3/sqrt(2)$, multiply numerator and denominator by $sqrt(2)$ to get $3sqrt(2)/2$. This multiplies the quotient by one, so changes only its form.])

+ Simplify $sqrt(48)$, $sqrt(125)$, and $sqrt(98)$.
+ Evaluate $sqrt(27)+sqrt(75)-2sqrt(3)$ exactly.
+ Rationalise $5/sqrt(3)$ and $sqrt(6)/sqrt(2)$; simplify the final forms.
+ Expand $(sqrt(3)+2)(sqrt(3)-2)$. Show why the radical terms cancel.
+ A student writes $sqrt(4+9)=sqrt(4)+sqrt(9)$. Refute the rule without a calculator.
+ Find positive integer pairs $(m,n)$ with $m<n<100$ for which $sqrt(m)+sqrt(n)=5sqrt(3)$. Start by considering which multiples of $sqrt(3)$ are possible.
#pagebreak()
= 1.5 / Sets, logic and proof
The set of integers is contained in the rational numbers, which are contained in the real numbers. One counterexample disproves a universal statement, but several confirming examples cannot establish it. A proof by contradiction starts by supposing the opposite of the claim and derives an impossibility.

#example([Worked example / Why the diagonal is irrational], [Suppose $sqrt(2)=a/b$ with positive integers $a,b$ and no common factor. Then $a^2=2b^2$, so $a$ is even: an odd integer has an odd square. Write $a=2k$. Substitution gives $b^2=2k^2$, so $b$ is even too. They share 2, contradicting the reduced form.])

+ Give a counterexample to “the product of two irrationals is always irrational”.
+ Show that if $r$ is rational and $s$ irrational, then $s+r$ is irrational.
+ Decide whether the converse of “every integer is rational” holds. Give evidence.
+ Explain why merely showing that *one* fraction cannot equal $sqrt(2)$ would not prove irrationality.
+ Use the possible remainders 0, 1 and 2 modulo 3 to prove that a square divisible by 3 has a root divisible by 3. Use that result to adapt the diagonal proof to $sqrt(3)$.
#pagebreak()
= Apply and investigate
== Investigation / Narrowing the diagonal
Use squared comparisons to find decimal bounds for $sqrt(2)$ of widths 0.1, 0.01 and 0.001. Record the exact squared endpoints. Predict what happens when you increase precision by one place. Explain how to select ten candidate subintervals and why exactly one contains the root. Would an identical procedure always give a strict interior point for $sqrt(4)$? Discuss endpoint handling.

== Modelling / Cutting guide tolerance
A laser cutter rounds lengths to the nearest millimetre and the measured length of a test cut may differ from its instruction by up to 0.4 mm. The design calls for a unit-square diagonal, with maximum actual error 0.75 mm from the exact design. Decide whether commanding 1,414 mm guarantees acceptance. Bound the exact diagonal tightly enough to justify your decision, draw the permitted actual-length interval, and state whether the answer changes for a 0.60 mm tolerance. Explain how you would test the stated cutter error in practice.

== Mixed review
+ Order $sqrt(3)$, 1.73 and $7/4$ using exact comparisons.
+ Express $0.overline(18)$ as a fraction and simplify $sqrt(18)/sqrt(2)$.
+ Find the intersection of $abs(x-3)<=0.5$ and $x>3.2$. Express it as an interval.
+ *Challenge:* Without decimal approximations, determine whether $sqrt(3)+sqrt(5)$ is greater or less than 4. State why squaring is valid at each step.
