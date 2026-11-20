#import "../shared/personal-pages.typ": author
#set document(title: "Mathematics · MYP1 · Powers and expressions", author: author)
#let ink = rgb("102b40")
#let teal = rgb("006e67")
#let mist = rgb("e9f5f2")
#set page(paper: "a4", margin: (x: 23mm, y: 21mm), header: align(right, text(size: 8pt, fill: teal)[MATHEMATICS / MYP1 / POWERS]), numbering: "1")
#set text(size: 11pt, fill: ink)
#set par(leading: .72em)
#show heading: set text(fill: teal)
#let example(title, body) = block(width: 100%, fill: mist, inset: 10pt, radius: 4pt, [#strong(title) #parbreak() #body])
= 02 / Powers and expressions
#text(fill: teal, weight: "bold")[MYP1 STUDENT COURSEBOOK · CHAPTER PROOF]

Imagine a photograph of 100 people arranged as a square. Now imagine the same 100 people arranged as a single row. The count is unchanged, but the square has a structure the row does not. How can a single expression tell a reader about both the count and the arrangement?

#example([Inquiry lens], [*Key concept:* form. *Related concepts:* representation and simplification. *Global context:* scientific and technical innovation.

*Statement of inquiry:* The structure of a mathematical expression makes repeated actions easier to describe, check and communicate.])

- *Factual:* What does the exponent in $3^4$ count?
- *Conceptual:* When does changing a bracket change the model?
- *Debatable:* When is a compact formula less useful than a diagram or a sentence?

== Learning route
Read and evaluate powers; write whole numbers with powers of ten; connect squares and cubes to equal dimensions; use precedence to interpret expressions; substitute values to test a rule.

== First look / Build a code
A maker starts with one tile. At each step, they make three copies of the entire previous arrangement. Sketch steps 0, 1, 2 and 3 and record the tile counts. What does the step number count? What does the number 3 count? Compare your notation with a partner’s and agree on a way to tell those two roles apart. Revisit your notation at the end of section 2.1.

#v(12mm)
#text(weight: "bold", author)
#pagebreak()
= 2.1 / From repeated multiplication to powers
A *power* such as $4^3$ describes repeated multiplication. The *base* (4) is the factor being repeated. The *exponent* or *index* (3) counts the factors. When the exponent is a positive whole number, the value is the product of that many copies of the base.

#example([Worked example / Count factors, not signs], [$4^3 = 4 times 4 times 4 = 64$. There are three factors but only two multiplication signs. Compare $4^3$ with $3^4 = 3 times 3 times 3 times 3 = 81$. Switching base and exponent changes both the factor and the number of copies, so there is no general reason for the values to match.])

In the tile activity, the number of copies made at each step gives the base. The step number tells us how many times the count has been multiplied by 3. Starting from a single tile, the count after four steps is $3^4$. At step zero, the count is still 1.

== Practice 2.1
+ For $2^6$, name the base, name the exponent and write the product. How many multiplication signs do you need?
+ Write each as a power and evaluate: six factors of 2; three factors of 6; four factors of 5.
+ Fill each gap with a positive whole number: $square^3 = 125$; $2^square = 128$; $square^4 = 81$.
+ A student replaces $7^3$ by $7 times 3$. Draw or write two models that make the difference visible. What would have to be counted in groups of seven to give the student's result?
+ Compare $2^8$ and $4^4$ without multiplying either out. Explain by grouping the factors in one expression.
+ Write 64 as a power in all possible ways if the base and exponent are whole numbers greater than 1. Explain how you know that no larger exponent is possible.
+ Two machines each start with one counter. One triples its entire collection at each step; the other doubles it. Find the least number of doubling steps needed to exceed the tripler’s count after four steps. Use two neighbouring powers to justify your answer.
#pagebreak()
= 2.2 / Powers of ten and expanded form
Powers of ten name the units of the place-value system. Moving a digit left one place multiplies its contribution by ten. For example, $10^3$ means $10 times 10 times 10 = 1,000$. In this system $10^0 = 1$, the ones unit: step backwards from 10 by dividing by 10.

#table(columns: 5, align: center, fill: (x,y) => if y == 0 { mist }, [Ten-thousands], [Thousands], [Hundreds], [Tens], [Ones], [$10^4$], [$10^3$], [$10^2$], [$10^1$], [$10^0$], [3], [0], [4], [0], [6])

#example([Worked example / Read the exponents as positions], [The table shows 30,406. Its non-zero contributions are $3 times 10^4 + 4 times 10^2 + 6 times 10^0$. The missing exponents indicate zero digits; they do not make the other digits move. If you write 346 instead, the 3 would represent hundreds rather than ten-thousands.])

== Practice 2.2
+ Write $10^1$, $10^3$ and $10^6$ in standard form. Describe the relationship between the exponent and the number of zeros.
+ Expand 706,028 using powers of ten. Circle the term containing $10^0$.
+ Evaluate $8 times 10^4 + 3 times 10^2 + 9 times 10^0$. Explain where the zero digits belong.
+ A student writes $14 times 10^2 + 3 times 10^1 + 5 times 10^0$. Regroup the hundreds to write this using only single-digit coefficients.
+ Find a single digit and a power of ten that have product 90,000. Then multiply that product by 100 and give the result in the same form.
+ Use each of the digits 0, 2, 4 and 6 exactly once in each number. Make two four-digit numbers whose difference is the greatest possible. Explain how each place contributes to that difference.
+ A counter jumps from 99,999 to 100,000. Express both readings using powers of ten. Explain the carry that turns five non-zero digits into one.
#pagebreak()
= 2.3 / Squares, cubes and roots
A *square number* is the result of multiplying a whole number by itself. The area of a square with side 5 units is $5^2 = 25$ square units. A *cube number* is the product of three equal whole-number factors. A cube with edge 5 units has volume $5^3 = 125$ cubic units, because each layer has 25 unit cubes and there are five layers.

#grid(columns: (1fr, 1fr), gutter: 12pt,
  figure(grid(columns: 4, gutter: 1pt, ..range(16).map(_ => rect(width: 9pt, height: 9pt, fill: teal, stroke: none))), caption: [Four rows of four squares.]),
  figure(grid(columns: 4, gutter: 2pt, ..range(4).map(_ => grid(columns: 4, gutter: .4pt, ..range(16).map(_ => rect(width: 4pt, height: 4pt, fill: teal, stroke: none))))), caption: [Four equal layers of sixteen cubes.]))

#example([Worked example / Reverse the calculation], [A square floor contains 81 unit tiles. The side length is $sqrt(81) = 9$ units because $9^2 = 81$. A solid cube made with 216 unit cubes has edge $root(3,216) = 6$ units because $6^3 = 216$. The square-root symbol gives the non-negative root; it does not ask for all possible numbers with that square.])

== Practice 2.3
+ List the squares of 8, 9, 10 and 11; then list the cubes of 2, 3, 4 and 5. Compare how the gaps change in each list.
+ Evaluate $sqrt(144)$, $root(3,64)$ and $sqrt(1)$. Check each with a power.
+ Between which two consecutive whole numbers is $sqrt(78)$? Defend your answer without finding a decimal approximation.
+ A solid cube has 125 unit cubes. How many cubes are in the bottom layer? How many cubes are left if the top two layers are removed?
+ One student says $sqrt(36+64)=6+8$. Check both sides and explain why adding side lengths does not add square areas.
+ Find the smallest whole number greater than 1 that is both a square and a cube. Use a list of cubes and rule out the smaller ones.
+ A square and a cube both have whole-number edge lengths. The numerical value of the square’s area equals the numerical value of the cube’s volume, and both edges exceed 1 unit. Find a possible pair of edge lengths. Explain why the actual units of the measurements are not interchangeable.
#pagebreak()
= 2.4 / Order of operations
An expression is a set of instructions with a structure. Evaluate groups inside brackets first, then powers, then multiplication and division from left to right, then addition and subtraction from left to right. Multiplication does not take precedence over division just because it is named first; those operations share a priority.

#example([Worked example / Same symbols, different group], [In $36 div 6 times 2 + 3^2$, evaluate the power to get 9. From left to right in the multiplication/division group, $36 div 6 = 6$ and $6 times 2 = 12$. Add 9 to get 21. But in $36 div (6 times 2) + 3^2$, the bracket makes 12 the divisor, so the result is $3 + 9 = 12$.])

== Practice 2.4
+ Evaluate $12+2^5$, $(12+2)^2$ and $12 times 2^3$. For each, underline the first operation you used.
+ Evaluate $48 div 4 times 3$ and $48 div (4 times 3)$. Write a sentence explaining the role of the brackets.
+ Evaluate $30-8+6$ and $30-(8+6)$. Explain why working from right to left is not safe for the first expression.
+ Replace the two boxes in $2^3 + 18 div square - square = 10$ with distinct whole numbers greater than 1. Find a solution in which the division is exact.
+ Insert one pair of brackets in $8 + 4 times 3^2$ so that the result is 108. Explain why $8 + (4 times 3)^2$ does not work.
+ To buy three packs at 700 FCFA each, a customer receives a single 250 FCFA discount. Write an expression for the bill. How would it change if the discount applied to every pack instead?
+ Find every value you can obtain by inserting exactly one pair of brackets into $2 + 3 times 4 - 1$. Keep the digits and operations in the same order. Include redundant brackets if you wish, but count each resulting value only once. Explain how you checked the possible groups.
#pagebreak()
= 2.5 / Substitution with powers
To *substitute*, replace a variable by its given value. Preserve the structure of the expression. In $2n^2$, only $n$ is squared. In $(2n)^2$, the whole product is squared. When substituting a negative value, brackets keep its sign attached to the number: the square of negative 3 is $(-3)^2=9$.

#example([Worked example / Read the model before calculating], [Two square panels of side $n$ centimetres cover a total of $2n^2$ square centimetres. One panel with side $2n$ centimetres covers $(2n)^2$ square centimetres. When $n=7$, these are $2 times 49 = 98$ and $14^2 = 196$. Doubling both dimensions multiplies the area by four, not two.])

== Practice 2.5
+ Calculate $5n^2$ and $(5n)^2$ when $n=2$. Name the base in each expression before substituting.
+ Use $n=-4$ to evaluate $n^2 + 2$ and $2n^2$. Explain the brackets in your working.
+ Evaluate $a^2+b^2$ and $(a+b)^2$ for $a=3$ and $b=5$. Draw two smaller squares inside a larger one and account for the difference using the uncovered rectangles.
+ A garden of side $s$ metres has a second square garden of side $s+2$. Write an expression for the extra area. Evaluate it for $s=4$ and check it by drawing the added strips.
+ A function machine outputs $3n^2-2$ for an input $n$. Work out the output for $n=4$. Find two different integer inputs that give that output, and explain why.
+ Which positive whole numbers $n$ make $n^2 < 6n$? Find all of them. Explain why checking $n=1,2,3$ alone cannot establish the complete answer.

== Investigate / Build a border (Criterion B practice)
A square has $n$ tiles along each side. Build the next square by adding a strip at the top and a strip at the right, including the new corner. Draw the change for $n=2,3,4$ and record the number added. Predict the number of tiles added for $n=20$, check it by finding both square counts, then give a rule for any positive whole $n$. Use the corner tile in your diagram to explain why the difference is odd. What total do you get if you add the first ten positive odd numbers? Explain using your diagrams rather than only adding.
#pagebreak()
= Consolidate / Store, predict, decide
#example([Remember], [A power records repeated multiplication. A root reverses a power in a specified domain. Powers of ten name place-value units. Brackets define groups. Substitution changes values, not the structure of an expression.])

== Model / A school image archive (Criterion D practice)
For a photography exhibition, a school is choosing between square greyscale images of side 400 pixels and side 600 pixels. For its trial, assume every pixel uses one byte, every image has an additional 200 bytes of metadata, and compression is off. The school sets aside $2 times 10^7$ bytes to store 60 images.

+ Explain why the number of pixels is a square. Write a rule for the bytes needed for $m$ images of side $s$ pixels under the trial assumptions.
+ Calculate the space used if all 60 images use the smaller setting, then if all use the larger setting. Explain which plan fits.
+ The photography group wants the greatest possible number of large images, with the remaining images small. Find that number. Present a table with the totals for your proposal and for one more large image. Explain why checking the latter is sufficient.
+ Choose a practical reason the model might differ from the real file sizes. Explain what you would measure before using the model to decide storage for the actual exhibition.

== Mixed review
+ Without expanding every product, determine whether $8^2$, $4^3$ and $2^6$ are equal. Show the factor regrouping.
+ Write $2 times 10^5 + 5 times 10^2 + 3$ in standard form. Explain the role of each zero.
+ Which whole numbers can be the square root of a square number strictly between 70 and 160? Give the complete list.
+ Evaluate $2(n+3)^2$ and $(2n+3)^2$ when $n=2$. Explain which operations the expressions share and where the instructions differ.
+ *Challenge:* Starting with a $1$-by-$1$ square, add borders until you have a $12$-by-$12$ square. How many tiles are added on every other step, beginning with the first addition? Show a way to count without drawing the entire square.

#example([Reflect], [Return to the tile-copy explanation. Rewrite one sentence so that a reader cannot confuse the base, the exponent and the final tile count.])
