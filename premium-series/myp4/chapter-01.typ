#import "../shared/personal-pages.typ": author
#set document(title: "Mathematics · MYP4 · Number foundations", author: author)
#let ink = rgb("102b40")
#let teal = rgb("963e2e")
#let mist = rgb("e9f5f2")
#set page(paper: "a4", margin: (x: 23mm, y: 21mm), header: align(right, text(size: 8pt, fill: teal)[MATHEMATICS / MYP4 / NUMBER FOUNDATIONS]), numbering: "1")
#set text(size: 11pt, fill: ink)
#set par(leading: .72em)
#show heading: set text(fill: teal)
#let example(title, body) = block(width: 100%, fill: mist, inset: 10pt, radius: 4pt, [#strong(title) #parbreak() #body])
= 03 / Number foundations
= 01 / Number foundations: exponents, surds and accuracy

Two workshops report that a spacer is 3.0 cm thick. One measured to the nearest millimetre; the other copied a nominal drawing dimension. A batch of 40 must fit into a cabinet. Can the two reports justify the same decision?

#example([Inquiry lens], [*Key concept:* logic. *Related concepts:* quantity and justification. *Global context:* scientific and technical innovation. Exact expressions support proof, while bounded approximations support decisions under uncertainty.])

- What distinguishes an exact value from a bound?
- Why can rounding early change the decision even when a reported answer looks precise?
- Who should decide what accuracy is acceptable in a design?

*ATL:* Compare two written solutions and underline every quantity assumed exact. Ask whether those assumptions came from the problem or the solver.
#pagebreak()
= 1.1 / Number systems and proof
Integers and fractions of integers are rational. Irrational numbers are real but not rational. To prove that some operation preserves rationality, express arbitrary inputs as fractions and check that the result is again a ratio of integers. To refute a universal statement, a single counterexample suffices.

#example([Worked example / Generalise a difference], [Let $r=a/b$ and $s=c/d$ with non-zero integer denominators. Then $r-s=(a d-b c)/(b d)$. The numerator is an integer and the denominator is a non-zero integer. Thus the difference of any two rational numbers is rational, not only for a sample of fractions.])

+ Classify $-7/9$, $sqrt(49)$, $pi$, $0.overline(12)$ and $sqrt(10)$ into rational or irrational.
+ Prove that the product of two rational numbers is rational. Explain why division needs another condition.
+ Find two irrational numbers with rational sum and two with irrational sum. Justify both outcomes.
+ Prove that adding a rational number to an irrational number gives an irrational result. Start by assuming the result is rational.
+ Disprove “if $a/b$ is rational, then both $a$ and $b$ are rational”. What does the *definition* guarantee, and what does it not say about a particular representation?
#pagebreak()
= 1.2 / Integer and rational exponents
For $a>0$, $a^0=1$, $a^(-n)=1/a^n$ and $a^(m/n)=(root(n,a))^m$ for integers $m$ and positive $n$. A negative exponent means a reciprocal, not a negative value. A fractional exponent specifies a root. Use $a^p a^q=a^(p+q)$ only when the bases match.

#example([Worked example / Read the operations in order], [$81^(-3/4)=1/(root(4,81))^3=1/3^3=1/27$. Check that the positive fourth root really is 3 before cubing.])

+ Simplify $3^4 times 3^(-6)$, $4^0$ and $(5^(-2))^3$.
+ Evaluate $64^(2/3)$, $16^(-3/4)$ and $125^(1/3)$ exactly.
+ Rewrite $1/(x sqrt(x))$ as one power of $x$ for $x>0$.
+ Find $k$ if $8^k=2^(-6)$. Explain why a negative answer is plausible.
+ Decide whether $9^(1/2)+16^(1/2)=25^(1/2)$. Explain why a rule for multiplying powers cannot be transferred here.
+ Give an example showing why the chapter states $a>0$ for these real-number exponent rules. Compare an odd root and an even root of a negative input.
#pagebreak()
= 1.3 / Standard form and estimation
Standard form writes a non-zero number as $a times 10^n$ with $1<=abs(a)<10$ and integer $n$. Multiplication and division combine powers of ten. To add or subtract, rewrite into a common power first. Estimate before calculating to test the likely scale.

#example([Worked example / Align scales before subtracting], [$4.2 times 10^5-7.6 times 10^4=(4.2-0.76)times 10^5=3.44 times 10^5$. A result around 340,000 is reasonable because the subtraction removes less than one fifth of 420,000.])

+ Write 0.000037, 64,100,000 and $-0.009$ in standard form.
+ Evaluate $(4 times 10^6)(8 times 10^(-9))$ and normalise your answer.
+ Estimate $(6.2 times 10^8)/(2.9 times 10^(-4))$, then calculate to three significant figures and compare.
+ Two sensors measure $3.08 times 10^(-3)$ and $7.8 times 10^(-4)$ seconds. Find the difference and give it in milliseconds.
+ A student adds $2.3 times 10^5$ and $1.8 times 10^4$ to get $4.1 times 10^9$. Identify both errors, then construct a magnitude check.
#pagebreak()
= 1.4 / Surds and exact values
A simplified square-root surd has no square factor greater than 1 under the root. Unlike surds cannot be combined as like terms. The identity $(u+v)(u-v)=u^2-v^2$ explains why a conjugate can rationalise a binomial denominator.

#example([Worked example / Multiply by one in a useful form], [$2/(sqrt(5)-1) = (2(sqrt(5)+1))/(5-1) = (sqrt(5)+1)/2$. The denominator is non-zero, and multiplying by the conjugate over itself preserves the original value.])

+ Simplify $sqrt(108)$ and $3sqrt(12)-sqrt(75)$.
+ Expand $(2+sqrt(3))^2$ and multiply $(2+sqrt(3))(2-sqrt(3))$. Compare the results.
+ Rationalise $7/sqrt(14)$ and $3/(sqrt(7)+2)$.
+ Find the exact diagonal of a rectangle with sides $2sqrt(3)$ cm and $3sqrt(2)$ cm. Explain why adding the two surds is not the correct operation.
+ Decide whether $sqrt(7)$ is larger than $2+sqrt(2)$. Use exact inequalities and justify squaring.
#pagebreak()
= 1.5 / Accuracy, bounds and error
If a positive reading $r$ is rounded to the nearest step $h$, with ties rounded up, the true value is in $[r-h/2, r+h/2)$. For positive dimensions, a product is smallest at the lower endpoints and has its supremum at the upper endpoints. Subtraction is different: the smallest possible difference pairs the smallest minuend with the largest subtrahend, with endpoint inclusion checked separately.

#example([Worked example / The interval matters], [A rectangle recorded as 8.0 cm by 5.0 cm to the nearest tenth has area in $[7.95 times 4.95,8.05 times 5.05) = [39.3525,40.6525)$ square cm. Reporting 40 square cm is a point estimate, not a guarantee of maximum error 0.5 square cm.])

#table(columns: 3, fill: (x,y) => if y==0 { mist }, [Measurement], [Lower endpoint included], [Upper endpoint excluded], [Width, 8.0 cm], [7.95 cm], [8.05 cm], [Height, 5.0 cm], [4.95 cm], [5.05 cm])

+ Give the interval for 2.36 kg rounded to the nearest 0.01 kg and for 560 g rounded to the nearest 10 g.
+ Both legs of a bracket are measured as 12 cm and 9 cm to the nearest centimetre. Find the interval for their sum, then their difference. Label open endpoints.
+ A reading of 80 mm has maximum absolute error 0.5 mm. Find the maximum error as a percentage of the reading. Explain the reference quantity you used.
+ Two values round to 5.0 and 3.0 to one decimal place. Can their ratio exceed 1.70? Demonstrate with actual allowed inputs or a bound.
+ Explain why rounding an upper bound down can turn a correct safety check into a false guarantee. Give an example from the area above.
#pagebreak()
= 1.6 / Investigation and modelling
== Investigate / When does the error grow?
A square recorded as 10 cm on each side has side error at most 0.5 cm. Compare the changes in area at the two extremes. Repeat for nominal sides 20 and 30 cm. If the side is $s$ and the possible error is $e$ with $0<e<s$, expand $(s+e)^2$ and $(s-e)^2$. Explain why the increase and decrease are not equal, and predict which quantity controls their difference. Test your rule on a fourth size. Distinguish absolute and percentage area error as the side length increases.

== Model / Will the rack fit?
A cabinet opening is measured as 121.0 cm to the nearest millimetre. A single production batch contains 40 spacers, each individually measured as 3.0 cm to the nearest millimetre. The designer needs at least 0.4 cm free clearance after installing them side by side. No compression is assumed.

+ Find the bounds on opening and total spacer length. Decide whether fit is guaranteed. Produce a feasible example in which the clearance fails if one exists.
+ A supplier offers another batch certified to lie between 2.98 and 3.01 cm inclusive per spacer. Test the guarantee. What assumptions do the bounds make about the way tolerances accumulate?
+ Recommend what to measure before installation if the original batch is used. Distinguish a decision about this specific batch from a claim about all batches.

*Challenge:* The opening is still measured as 121.0 cm to the nearest millimetre. Find the largest allowed upper bound per spacer that guarantees clearance for 40. If the quoted bound must be expressed to the nearest hundredth of a centimetre, choose a conservative value and justify its direction.
