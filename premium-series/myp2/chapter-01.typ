#import "../shared/personal-pages.typ": author
#set document(title: "Mathematics · MYP2 · Ratios and equivalent ratios", author: author)
#let ink = rgb("102b40")
#let teal = rgb("245785")
#let mist = rgb("eaf2fb")
#set page(paper: "a4", margin: (x: 23mm, y: 21mm), header: align(right, text(size: 8pt, fill: teal)[MATHEMATICS / MYP2 / RATIOS]), numbering: "1")
#set text(size: 11pt, fill: ink)
#set par(leading: .72em)
#show heading: set text(fill: teal)
#let example(title, body) = block(width: 100%, fill: mist, inset: 10pt, radius: 4pt, [#strong(title) #parbreak() #body])
= 03 / Ratios and equivalent ratios
= 01 / Ratios and equivalent ratios
A theatre crew mixes two shades of paint. One crew uses three scoops of blue and five of white. Another adds two extra scoops of each. Will the results match? How could you prove your answer without mixing the paint?

#example([Inquiry lens], [*Key concept:* relationships. *Related concepts:* equivalence and representation. *Global context:* personal and cultural expression.

*Statement of inquiry:* Multiplicative comparison helps us reproduce designs consistently and allocate resources according to a stated rule.])

- *Factual:* What does the order of the quantities in a ratio tell us?
- *Conceptual:* Why does scaling preserve a mixture but adding equal amounts usually change it?
- *Debatable:* When is a proportional share preferable to an equal share?

*Learning route:* interpret ratio language; simplify and scale ratios; use tables and double number lines; compare mixtures and allocate a total.

*ATL / communication:* Write two instructions that could generate your paint mixture. Ask a partner to follow them on paper. Check whether they chose the same ratio and the same total; revise any wording that confuses the two.
#pagebreak()
= 1.1 / Ratio language
A ratio is an ordered multiplicative comparison. The ratio $3:5$ of blue to white describes three units of blue for every five of white. It is not a fraction of the whole: if the mixture contains only these two colours, blue makes up $3/(3+5)=3/8$ of it. Reversing the ratio reverses the roles.

#example([Worked example / Name the quantities first], [A set has 9 short strips and 15 long strips. Short to long is $9:15$, long to short is $15:9$, and short to total is $9:24$. The numerator 9 belongs in both the first and third ratios, but the second quantity represents a different group.])

== Practice 1.1
+ For 14 red and 21 gold beads, write the ratios red to gold, gold to red, and red to total. Explain the meaning of each second term.
+ Draw a strip model for $4:7$. Use it to represent each part as a fraction of the total.
+ Two ribbons measure 45 cm and 1.2 m. Express the first-to-second ratio using a common unit; explain why $45:1.2$ misrepresents the lengths.
+ A poster adds one blue shape for every two yellow shapes. Which ratio describes yellow to all shapes? Why is it not $2:1$?
+ A class has 24 students. Give two different part-to-part ratios that could describe the number travelling by bus versus everyone else. For each, say how many travel by bus.
+ A display contains only striped and plain cards. The striped-to-total ratio is $2:7$. Explain why adding seven cards *could* preserve the ratio. Describe what must be added.
#pagebreak()
= 1.2 / Equivalent ratios
Equivalent ratios compare quantities by the same multiplicative relationship. Scale every term by the same positive number. For whole-number terms, reduce to simplest form by dividing by their highest common factor. Equal differences do not establish equivalent ratios.

#example([Worked example / Test both multipliers], [For $18:30$, divide each number by 6 to obtain $3:5$. The ratio $21:35$ also reduces to $3:5$. But $21:33$ is different: the first term grew from 18 by a factor of $7/6$, which would require the second term to grow to 35, not 33.])

== Practice 1.2
+ Reduce $20:32$, $81:63$ and $36:54$ to simplest form.
+ Fill the gaps in $7:9 = 21:square = square:63$. State both scale factors.
+ Decide if $15:24$, $20:32$ and $30:45$ represent the same mixture. Explain how you know.
+ Express $1.5:2.25$ as a simplest whole-number ratio. Justify scaling up before simplifying.
+ Two whole numbers sum to 99 and are in the ratio $6:5$. Find them. Explain why the second number is not 5.
+ Show that adding the same positive number to both terms of $a:b$ cannot preserve a positive ratio unless $a=b$. Try a case first, then compare the multipliers or reason with a common denominator.
#pagebreak()
= 1.3 / Ratio tables and double number lines
A ratio table pairs corresponding quantities. In a proportional table, multiply both entries in a column by the same factor to obtain another column. Aligned positions on a double number line express the same idea continuously and make zero visible.

#table(columns: 5, align: center, fill: (x,y) => if y == 0 { mist }, [Panels], [0], [2], [4], [6], [Paint (L)], [0], [3], [6], [9])

#let number-line(label, values) = grid(columns: (70pt, 1fr), align: horizon, text(size: 9pt, label), grid(columns: 4, column-gutter: 0pt, ..values.map(n => block(width: 100%, stroke: (top: .8pt + teal), inset: (top: 0pt), [#align(center)[#line(angle: 90deg, length: 4pt, stroke: .8pt + teal) #linebreak() #n]]))))
#figure(block(width: 85%)[#number-line("Panels", (0,2,4,6)) #v(5pt) #number-line("Paint (L)", (0,3,6,9))], caption: [Aligned labels show equivalent pairs; each step adds two panels and three litres.])

#example([Worked example / Scale through an intermediate pair], [If 2 panels need 3 L, one panel needs 1.5 L. Five panels need $5 times 1.5 = 7.5$ L. This assumes equal paint coverage and no fixed wastage. A non-zero amount needed before any panel is painted would invalidate the proportional model.])

== Practice 1.3
+ Extend the table to 8 and 10 panels. Use it to predict paint for 9 panels.
+ Sketch a double number line for 4 notebooks costing 1,600 FCFA. Include zero and label the cost for 1, 4, and 7 notebooks.
+ A printer reports 3, 6, and 9 posters using 8, 14, and 20 mL of ink. Differences are constant. Is this proportional? Support your answer with a calculation.
+ For a craft session, 5 bags supply 12 learners. Assuming learners need equal shares, how many bags supply 30 learners? If bags cannot be opened until the session and must be ordered whole, how many must be ordered?
+ Two different interviews report 6 volunteers per 15 residents and 14 volunteers per 35 residents. Add the groups if they are disjoint. Explain why the combined data preserve the same ratio.
+ Give a proportion table with an integer value in one row and a non-integer corresponding value in the other. Explain why an integer-only table might hide a valid estimate.
#pagebreak()
= 1.4 / Sharing and comparing with ratios
To share a total in a ratio, add the ratio terms to count equal shares. Divide the total by that sum to find one share. To compare two mixtures, scale to the same amount of a named component or compare fractions of their respective totals.

#example([Worked example / Allocate, then check], [Share 126 tickets in the ratio $2:3:4$. There are nine shares and each is $126 div 9=14$ tickets. The allocations are 28, 42 and 56. Verify both the sum and the reduced ratio; a sum of 126 alone is not enough.])

== Practice 1.4
+ Share 96 counters in the ratio $5:3$. Check the result in two ways.
+ A crew spends 72,000 FCFA on materials, travel and refreshments in the ratio $5:2:1$. Find each amount.
+ Compare the blue fraction of mixtures $3:5$ and $5:8$ (blue to white). Which has the larger blue fraction? Show the comparison exactly.
+ Equal volumes of mixtures with blue fractions $1/3$ and $1/2$ are combined. Find the resulting blue fraction. Why would averaging the two *blue-to-white ratios* be inappropriate?
+ Two teams share 64 seats in a ratio of $5:2$. Show that an exact whole-seat split is impossible. Propose a split that uses all seats and minimises the difference from each team's exact share.
+ Two positive integer allocations have ratio $4:7$. If 9 units are transferred from the larger to the smaller, the two amounts are equal. Find the original total. Check by simulating the transfer.
#pagebreak()
= 1.5 / Investigate and model
== Investigate / Same change, different effect (Criterion B practice)
Three trial batches use blue and white in the ratios $1:4$, $2:5$, and $3:6$. For each, make a table showing the blue fraction after adding 0, 1, 2 and 3 equal units to each colour. Predict whether the blue fraction can reach one half by repeating this operation. Explain using the difference between the colour volumes and how the total changes. Give a rule for any starting quantities $a<b$. Test your explanation when $a=b$, then when $a>b$.

== Model / An exhibit backdrop (Criterion D practice)
A theatre group needs at least 13 L of mixed paint for two identical backdrops. Its test mixture uses blue and white in the ratio $2:5$ by volume. Blue paint comes in sealed 2 L cans at 4,500 FCFA; white paint comes in sealed 3 L cans at 3,000 FCFA. The group may measure partial cans accurately but pays for every can opened or bought. Its budget is 22,000 FCFA.

+ Find the exact volumes of each colour for 13 L. Identify which conditions require rounding and which quantities should not be rounded prematurely.
+ Choose the cheapest purchase that meets the target. Tabulate number of cans, bought volume, used volume and remainder by colour. Check the budget.
+ Rain damage raises the required mixed volume to 14.5 L. Show whether the same purchase works. If not, determine the least new cost that preserves the original paint ratio.
+ Recommend a response for the theatre group. Distinguish confirmed quantities from assumptions, and explain a simple test of whether the original coverage estimate is dependable.

== 1.6 / Summary, revision and reflection
- Label the quantities and their order before writing a ratio.
- Scale each term by the same factor. To compare mixtures, use a common component or a common total.
- A calculated share may be fractional even if the decision requires a whole number of seats or cans.

+ A blend contains 28 g of dried fruit in 80 g in total. State dried fruit to everything else in simplest form.
+ Share 180 g in a ratio $3:4:5$. Verify the ratio and the total.
+ *Challenge:* Two integer paint recipes use blue to white in a ratio $3:7$. If four units of white are removed from one recipe, it becomes $1:2$. Find that recipe's starting total; explain why the answer is unique.

#example([Reflect], [Which is most useful when explaining your decision: a ratio, a fraction of the total, or a pair of actual quantities? Justify your choice for two different questions in this chapter.])
