#import "../shared/personal-pages.typ": author
#set document(title: "Mathematics · MYP5 · Polynomials and algebraic fractions", author: author)
#let ink = rgb("102b40")
#let teal = rgb("375b36")
#let mist = rgb("e9f5f2")
#set page(paper: "a4", margin: (x: 23mm, y: 21mm), header: align(right, text(size: 8pt, fill: teal)[MATHEMATICS / MYP5 / POLYNOMIALS]), numbering: "1")
#set text(size: 11pt, fill: ink)
#set par(leading: .72em)
#show heading: set text(fill: teal)
#let example(title, body) = block(width: 100%, fill: mist, inset: 10pt, radius: 4pt, [#strong(title) #parbreak() #body])
= 03 / Polynomials and algebraic fractions
= 01 / Polynomials, factor theorem and algebraic fractions
A model of a machine may have a formula that looks simple after cancellation. Yet the cancelled expression might mark a configuration in which the model was never defined. How can algebra simplify the calculation without changing the conditions under which it is valid?

#example([Inquiry lens], [*Key concept:* form. *Related concepts:* equivalence, representation and validity. *Global context:* scientific and technical innovation. Algebraic representations expose useful structure, but each transformation must preserve the conditions of the original model.])

- What does the remainder of division by $x-c$ tell us?
- Which features of a model become easier to see in factored form?
- When should a simple formula be rejected as a model, even if its algebra is correct?

*ATL:* Exchange two model solutions. Ask your partner to separate assumptions about physical quantities from exclusions imposed by the algebra.
#pagebreak()
= 1.1 / Polynomials and their behaviour
A polynomial in $x$ is a finite sum of terms $a x^n$, with non-negative integer exponents $n$. For a non-zero polynomial, the degree is the largest exponent whose coefficient is non-zero. The leading term determines long-run behaviour: dividing each lower-degree term by it gives a ratio that approaches zero as the magnitude of $x$ grows.

#example([Worked example / Different forms reveal different features], [$P(x)=-2x(x-3)(x+1)$ has leading term $-2x^3$, so far to the right its values are negative and far to the left positive. The factors immediately give roots $-1,0,3$. Expanding gives $-2x^3+4x^2+6x$, which makes the coefficient of $x^2$ visible.])

+ Identify the degree and leading coefficient of $7-3x^4+x^2$ and $(x+2)^3-x^3$. Explain why expansion can matter for the latter.
+ Which of $x^(-1)+4$, $sqrt(x)+1$, and $3/4 x^2-2$ is a polynomial? Justify each choice.
+ Find the roots and leading term of $3(x-2)^2(x+1)$. Predict the sign for very large positive and negative $x$.
+ Construct two different cubics with the same three specified roots $-2,1,4$. What property can distinguish them?
+ Find a quadratic with roots 1 and 5 and value $-8$ at $x=3$. Is it unique among quadratics? Justify.
#pagebreak()
= 1.2 / Dividing polynomials
To divide $P$ by a non-zero polynomial $D$, repeatedly cancel the leading term using a multiple of $D$. Stop when the remainder has lower degree than $D$ (or is zero). The check is $P=D Q+R$. Keep zero coefficients in their places so that no term is accidentally shifted.

#example([Worked example / Carry the remainder], [Divide $x^3+0x^2-4x+7$ by $x-2$. Subtract $x^2(x-2)$, leaving $2x^2-4x+7$. Subtract $2x(x-2)$, leaving 7. So $Q=x^2+2x$, $R=7$. Multiplying back gives $(x-2)(x^2+2x)+7=x^3-4x+7$.])

+ Divide $x^2+5x+7$ by $x+2$. Check by reconstructing the dividend.
+ Divide $2x^3+3x-5$ by $x-1$. Show where you used a zero coefficient.
+ Divide $x^4+1$ by $x^2+1$. Explain why the final remainder need not have degree exactly one.
+ Construct a dividend with divisor $2x-1$, quotient $x^2+x$ and remainder 6. What changes if the remainder is replaced by $6x$? Explain why the latter is not a final remainder.
+ A student claims $x^3=(x-1)(x^2+x)+1$. Find the error and repair the identity without restarting the division.
#pagebreak()
= 1.3 / Remainder and factor theorems
If $P(x)=(x-c)Q(x)+r$, then substitution gives $P(c)=r$. Thus $x-c$ divides $P$ exactly when $P(c)=0$. A candidate root is not a factor until this test is passed.

#example([Worked example / Work backwards from a factor], [If $x+2$ is a factor of $x^3+k x+6$, substituting $-2$ gives $-8-2k+6=0$. Hence $k=-1$. Multiplying $(x+2)(x^2-2x+3)$ gives $x^3-x+6$, verifying the result.])

+ Find the remainder when $2x^3-x+5$ is divided by $x+1$ without division.
+ Test whether $x-3$ and $x+3$ divide $x^3-9x$. Use the results to factor fully.
+ Find $k$ so that $x-2$ is a factor of $x^3+k x^2-7x+2$. Verify by substitution.
+ Find the monic quadratic that has remainder 0 on division by $x-1$ and remainder 6 on division by $x-3$.
+ Show why a non-zero cubic cannot have four distinct roots. Use the factor theorem repeatedly and explain why a factor for one root does not remove another distinct root.
#pagebreak()
= 1.4 / Algebraic fractions
First list the real inputs making any original denominator zero. Then factor and cancel common non-zero factors. Cancellation changes a formula, not its original domain. To add fractions, use a common denominator and combine numerators, not denominators.

#example([Worked example / Keep the excluded input], [For $x!=2$, $(x^2-4)/(x-2)=x+2$. The simplified formula has value 4 at $x=2$, but the original has no value there. A graph of the original therefore agrees with the line everywhere except for a missing point at $(2,4)$.])

+ Simplify $(x^2-9)/(x^2+x-12)$ and state every original exclusion.
+ Add $2/(x-1)+1/(x+1)$, state restrictions, and check at $x=2$.
+ Simplify $(x^2-1)/(2x) times 4/(x+1)$ with restrictions.
+ Find all $x$ for which $(x^2-4)/(x-2)$ equals 4. Explain why a solution of the simplified equation need not solve the original one.
+ Give two different algebraic fractions that agree with $x-3$ wherever defined but have different domains. Specify those domains.
#pagebreak()
= 1.5 / Rational equations and applications
A rational equation contains a variable in a denominator. State exclusions before multiplying by a common denominator; on the allowed domain that multiplier is non-zero. Solve the resulting equation, then check each candidate in the original expression and against any contextual constraints.

#example([Worked example / Distinguish a root from a solution], [$1/x+1/(x+2)=1/2$ excludes 0 and $-2$. Multiplying by $2x(x+2)$ gives $2(x+2)+2x=x(x+2)$, so $x^2-2x-4=0$. The roots $1+sqrt(5)$ and $1-sqrt(5)$ are both allowed by the algebra. If $x$ represents a positive rate, only the first fits that context.])

+ Solve $3/(x-1)=2/(x+1)$ and check in both fractions.
+ Solve $x/(x-3)=3/(x-3)$. Explain why the cleared equation gives no valid solution.
+ Solve $1/x+1/(x+3)=1/2$ exactly, stating exclusions.
+ Two pumps can fill the same tank independently in $t$ and $t+3$ hours. Together they take two hours. Write an equation, solve it, and explain the domain restriction.
+ A cyclist travels 18 km out at $v$ km/h and returns at $v+3$ km/h. Explain why average speed is not usually $v+1.5$. Write the total-time equation for a three-hour trip and find the positive speed.
#pagebreak()
= 1.6 / Investigation and modelling
== Investigate / Factors, roots and sign
Fill a sign table for $(x+2)(x-1)(x-4)$, using the open intervals cut out by the roots and a separate column for each root. Repeat when the middle factor is squared, then cubed. Explain why an even power does not change sign across its root and an odd power does. Predict the sign of $-(x+3)^2(x-2)^3$ on each interval without expanding. Check with representative inputs, then justify why test points alone would not prove the general rule.

#table(columns: 5, fill: (x,y) => if y == 0 { mist }, [Interval], [$x<-2$], [$-2<x<1$], [$1<x<4$], [$x>4$], [One test input], [$-3$], [$0$], [$2$], [$5$])

== Model / A tile frame
A workshop cuts a rectangular panel from a blank of width $x+4$ cm and length $x+6$ cm. A border of width 2 cm is removed on all four sides. The workshop wants the ratio of blank area to finished area to be no more than 2, and can choose positive whole-number $x$ only.

+ Draw the two rectangles and label their dimensions. Explain why $x>0$ is essential.
+ Write the ratio as an algebraic fraction, cancel where appropriate and record the domain. Solve the boundary equation where the ratio equals 2. Find the smallest allowed blank that meets the target; justify the decision on both sides of the boundary.
+ The tool requires an additional half-centimetre trim on every edge of the finished piece. Revise the ratio and find the smallest qualifying blank. Discuss what happens if there is a maximum blank width of 16 cm.

*Challenge:* Construct a monic cubic with distinct integer roots such that it is positive precisely on $(-3,1)$ and $(4,infinity)$. Explain why your reconstruction is unique.
