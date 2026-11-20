#import "../shared/personal-pages.typ": author
#set document(title: "Mathematics · MYP1 · Factors, multiples and primes", author: author)
#let ink = rgb("102b40")
#let teal = rgb("006e67")
#let mist = rgb("e9f5f2")
#set page(paper: "a4", margin: (x: 23mm, y: 21mm), header: align(right, text(size: 8pt, fill: teal)[MATHEMATICS / MYP1 / FACTORS]), numbering: "1")
#set text(size: 11pt, fill: ink)
#set par(leading: .72em)
#show heading: set text(fill: teal)
#let example(title, body) = block(width: 100%, fill: mist, inset: 10pt, radius: 4pt, [#strong(title) #parbreak() #body])
= 03 / Factors, multiples and primes
#text(fill: teal, weight: "bold")[MYP1 STUDENT COURSEBOOK · CHAPTER PROOF]

At a community sports day, volunteers have 84 blue bibs and 60 orange bibs. They want identical station kits with both colours in every kit and no leftovers. Later, two rotating activities will need to finish together. What makes these two problems different?

#example([Inquiry lens], [*Key concept:* logic. *Related concepts:* patterns and equivalence. *Global context:* fairness and development.

*Statement of inquiry:* Recognising the multiplicative structure of quantities helps us justify fair allocations and coordinate recurring events.])

- *Factual:* How do we recognise a factor?
- *Conceptual:* Why does one problem ask for a common factor and the other for a common multiple?
- *Debatable:* Is giving each group identical resources always the fairest choice?

== Learning route
List factors systematically; explain and apply divisibility tests; distinguish primes from composites; use prime factorisation to find the highest common factor and lowest common multiple.

== First look / Rectangles without leftovers
Draw the different rectangles that can be made with exactly 24 unit tiles. Treat a turned rectangle as the same design. Compare your list with a partner’s: instead of saying “we found the same shapes,” agree on an argument that guarantees the list is complete.
#v(10mm)
#text(weight: "bold", author)
#pagebreak()
= 3.1 / Factors, multiples and factor pairs
For positive whole numbers, $a$ is a *factor* of $b$ if $b = a times k$ for some positive whole number $k$. Then $b$ is a *multiple* of $a$. The two statements describe the same relationship from opposite directions. Factors of a positive whole number form a finite list; its positive multiples go on indefinitely.

#example([Worked example / Know when to stop], [For 36, test 1, 2, 3, 4, 5 and 6. This gives $(1,36)$, $(2,18)$, $(3,12)$, $(4,9)$ and $(6,6)$; 5 leaves a remainder. A pair cannot have both factors greater than 6: its product would exceed 36. Count 6 only once when listing individual factors.])

#table(columns: 4, align: center, fill: (x,y) => if y == 0 { mist }, [Smaller factor], [1], [3], [5], [Paired factor of 45], [45], [15], [9])
The table pairs the width and length of each rectangular arrangement of 45 unit tiles. The next possible smaller factor, 7, is already too large: $7 times 7 > 45$.

== Practice 3.1
+ List the factor pairs of 24 and 48. Identify factors of 48 that are not factors of 24.
+ List the positive multiples of 7 from 30 to 65 inclusive. How can you start without listing those below 30?
+ Describe the relationship between 9 and 63 in two sentences, one using *factor* and one using *multiple*.
+ A class has 54 chairs. It needs at least three rows and at least six chairs in each row, with equal row lengths. Give every layout, specifying rows and chairs per row.
+ Find all positive whole numbers below 40 whose factor pairs include $(n,n)$ for some whole number $n$. Explain what their tile rectangles have in common.
+ A student checked possible smaller factors through 8 for a number and said no further testing was necessary because $9 times 9$ was too large. Would this stopping argument work for 80? For 81? Explain the boundary case.
#pagebreak()
= 3.2 / Divisibility tests
A number is *divisible* by a positive whole number if division leaves no remainder. A divisibility test can establish this without finding the quotient.

#table(columns: (1fr, 3fr), fill: (x,y) => if y == 0 { mist }, [Divisor], [Test for a positive whole number], [2], [The last digit is even.], [3 or 9], [The sum of the digits is divisible by 3 or 9, respectively.], [4], [The number formed by the last two digits is divisible by 4.], [8], [The number formed by the last three digits is divisible by 8.], [5 or 10], [The last digit is 0 or 5 for 5; it must be 0 for 10.], [6], [The number is divisible by both 2 and 3.])

#example([Worked example / Explain the digit sum], [In 4,572, every place-value unit is one more than a multiple of 9: $1,000 = 999 + 1$, $100 = 99 + 1$, $10 = 9 + 1$. So subtracting $4 + 5 + 7 + 2 = 18$ leaves a multiple of 9. Since 18 is divisible by 9, so is 4,572. The same reasoning works for 3 because every multiple of 9 is also a multiple of 3.])

For 8, any thousands contribute multiples of $1,000 = 8 times 125$. For 4, any hundreds contribute multiples of 100, and $100 = 4 times 25$. When dividing by 4, only the final two digits can affect the remainder. The test for 6 works because a multiple of 3 has the form $3k$; if it is also even, then $k$ must be even, so $3k$ is a multiple of 6.

== Practice 3.2
+ Which of 2, 3, 4, 5, 6, 8, 9 and 10 divide 540? For each, show the relevant part of the test.
+ Test 1,234 and 1,432 for divisibility by 4. Explain why rearranging digits may change this result, but cannot change divisibility by 9. Find the remainder of each number when divided by 8 using only the last three digits.
+ Find every digit that completes 47□ so that the result is divisible by 6.
+ Use the digits 1, 2, 3 and 6 once each to make the smallest four-digit multiple of 4. Explain how you ruled out smaller starts.
+ A student claims that a multiple of both 4 and 6 is always a multiple of 24. Give a counterexample and explain why passing both tests does not prove the claim.
+ A four-digit code begins with 35 and ends in two digits you choose. Find the least and greatest codes divisible by both 5 and 9. Justify that your search was complete.
#pagebreak()
= 3.3 / Prime and composite numbers
A *prime* is a whole number greater than 1 with exactly two positive factors: 1 and itself. A *composite* number has more than two positive factors. The number 1 is neither: it has just one positive factor. The number 2 is prime; all other positive even numbers greater than 2 are composite.

#example([Worked example / How much trial division is enough?], [To test 97, any non-trivial factor pair would have a smaller factor at most 9, since $10^2 > 97$. It is enough to test primes 2, 3, 5 and 7: if a composite number divided 97, its prime factors would divide 97 as well. The number is odd, its digit sum is 16, it does not end in 0 or 5, and $97 = 7 times 13 + 6$. Therefore 97 is prime.])

== Practice 3.3
+ Classify 1, 2, 27, 31 and 49. For a composite number, exhibit a non-trivial factor pair.
+ Copy a table of the numbers 2–50. Circle 2, cross out its other multiples, then repeat with the smallest surviving uncircled number. Explain why after crossing out multiples of 7 you need not cross out any more. List the primes.
+ A student argues that 91 is prime because it is odd and not divisible by 3 or 5. Find the missing check and explain why the conclusion failed.
+ Find all primes between 70 and 90. Use the same stopping argument as in the worked example.
+ Prove that no even number greater than 4 can be the sum of 2 and another prime.
+ Three consecutive whole numbers are all greater than 1. Show that at least one is composite, even if you are not told the numbers.
#pagebreak()
= 3.4 / Prime factorisation
*Prime factorisation* writes a whole number greater than 1 as a product of primes. Split any composite factor until all remaining factors are prime. A different starting split may produce a different tree, but every whole number greater than 1 has the same prime factorisation up to the order of the factors.

#grid(columns: (1fr, 1fr), gutter: 10pt,
  [#align(center)[$72 = 8 times 9$ #linebreak() $8 = 2 times 4, quad 9 = 3 times 3$ #linebreak() $4 = 2 times 2$]],
  [#align(center)[$72 = 6 times 12$ #linebreak() $6 = 2 times 3, quad 12 = 3 times 4$ #linebreak() $4 = 2 times 2$]])

#example([Worked example / Check the leaves], [The two splits above both end in three 2s and two 3s, so $72 = 2^3 times 3^2$. Check that the five factors multiply to 72 and that none is composite. The correct product $8 times 9$ is only a starting point, not a prime factorisation.])

== Practice 3.4
+ Factorise 42, 56 and 100 into primes. Write repeated factors with powers.
+ For 90, start one factor tree with $9 times 10$ and another with $5 times 18$. Compare the leaves.
+ Find the missing exponent in $540 = 2^2 times 3^square times 5$ and check by multiplication.
+ One student gives $2^2 times 15$ for 60; another gives $2^3 times 3 times 5$. Explain what is wrong with each and repair the factorisation.
+ Find the smallest positive whole number by which 180 can be multiplied to make a perfect square. Explain using pairs of prime factors.
+ A number has exactly two distinct prime factors: 2 and 5. It has three factors of 2 in its prime factorisation. List all such numbers less than 300 and justify your stopping point.
#pagebreak()
= 3.5 / Common factors and common multiples
The *highest common factor* (HCF) is the greatest positive number that divides each number. The *lowest common multiple* (LCM) is the smallest positive number divisible by each number. To construct an HCF, keep only the prime copies both numbers can supply. To construct an LCM, take enough copies of each prime to meet the larger requirement.

#table(columns: 5, align: center, fill: (x,y) => if y == 0 { mist }, [Prime], [84], [60], [HCF copies], [LCM copies], [2], [2], [2], [2], [2], [3], [1], [1], [1], [1], [5], [0], [1], [0], [1], [7], [1], [0], [0], [1])

#example([Worked example / Read the question before choosing], [With 84 blue and 60 orange bibs, the kit count must divide both totals. Using the shared copies gives $2^2 times 3 = 12$ kits, each with seven blue and five orange bibs. If the same numbers were cycle lengths in seconds, the first positive repeat would instead be $2^2 times 3 times 5 times 7 = 420$ seconds.])

== Practice 3.5
+ Find the HCF and LCM of 18 and 24. Check the HCF by division and the LCM by listing multiples up to the first match.
+ Repeat using 16 and 48. Explain what happens whenever one number divides the other.
+ Cut ribbons of lengths 72 cm and 108 cm into equal pieces, wasting none. Find the longest possible pieces and how many pieces each ribbon gives.
+ Two free shuttles leave together at 09:00. They repeat every 18 minutes and every 30 minutes. When do they first leave together again? If a third repeats every 20 minutes from 09:00, when do all three first leave together again?
+ The HCF of two numbers is 6 and their LCM is 72. Find all unordered pairs and explain how you know the list is complete.
#pagebreak()
= Consolidate / Fair kits and shared schedules
== Investigate / A product that stays the same (Criterion B practice)
Make a table for pairs $(8,12)$, $(9,15)$ and $(12,18)$. For each pair, compare the product of the pair with the product of its HCF and LCM. Predict and test what happens for two numbers with no shared prime factors and for two numbers where one divides the other. Give a general explanation: choose one prime and track how many copies appear on each side. Repeat with three numbers, for example 2, 4 and 8. Does the two-number rule extend unchanged?

== Model / A community equipment rota (Criterion D practice)
A sports day has 96 cones, 72 batons and 60 bibs. Organisers want the greatest possible number of identical equipment kits, without leftovers. Each station uses one kit. In a trial, the cone activity finishes every 8 minutes and the baton activity every 12 minutes. Both start at 10:00. The venue closes at 10:25 and clearing all equipment requires four uninterrupted minutes after the joint finish.

+ Decide how many stations can receive a kit and list the contents of each kit. Show why an extra identical kit is impossible under the stated rules.
+ Decide whether both activities can reach their first joint finish and clear the venue on time. Use a timeline or a table and include units.
+ The organisers can start earlier or shorten the baton cycle by changing a drill. Find the latest viable shared start if the trial times stay the same. Alternatively, find a shorter whole-minute baton cycle of at least eight minutes that allows the original start. Compare the practical trade-offs.
+ A test run shows packing up sometimes takes five minutes rather than four. Explain which assumptions your recommendation uses, and suggest one observation that would help decide whether to keep it.

== Mixed review
+ Explain the direction of both claims: “11 is a factor of 77” and “77 is a multiple of 11”.
+ Use the digit-sum test to find the smallest three-digit multiple of 9 with distinct digits.
+ Decide whether 121 is prime. Explain why testing only 2, 3, 5 and 7 is not enough.
+ Find the HCF and LCM of 45 and 75 by prime factorisation.
+ *Challenge:* A positive whole number has exactly three positive factors. Prove it must be the square of a prime. Hint: pair every factor with its partner.

#example([Reflect], [Return to the two sports-day questions at the start. For each, write one sentence that identifies what must divide what. Use this check whenever you are unsure whether a problem needs an HCF or an LCM.])
