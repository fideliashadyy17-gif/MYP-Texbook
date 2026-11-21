#import "../shared/personal-pages.typ": author
#set document(title: "Mathematics · MYP1 · Percentages and budgets", author: author)
#let ink = rgb("102b40")
#let teal = rgb("006e67")
#let mist = rgb("e9f5f2")
#set page(paper: "a4", margin: (x: 23mm, y: 21mm), header: align(right, text(size: 8pt, fill: teal)[MATHEMATICS / MYP1 / PERCENTAGES]), numbering: "1")
#set text(size: 11pt, fill: ink)
#set par(leading: .72em)
#show heading: set text(fill: teal)
#let example(title, body) = block(width: 100%, fill: mist, inset: 10pt, radius: 4pt, [#strong(title) #parbreak() #body])
= 03 / Percentages and budgets
= 05 / Percentages and budgets
A market stall advertises “20% off”. Another offers “2,000 FCFA off”. Neither sign tells you which purchase costs less. What information would turn each announcement into a decision?

#example([Inquiry lens], [*Key concept:* relationships. *Related concepts:* quantity and equivalence. *Global context:* fairness and development.

*Statement of inquiry:* Choices about the comparison base change what a percentage tells us and whether comparisons are fair.])

- *Factual:* What does per cent mean?
- *Conceptual:* Why does a discount followed by the same percentage increase not restore a price?
- *Debatable:* Which information should every discount sign disclose?

*Learning route:* translate benchmark percentages; find a proportion of a quantity; apply percentage multipliers; build a budget that includes fixed and proportional charges.

*ATL / communication:* In pairs, design two accurate but potentially misleading offer signs for the same product. Swap them with another pair and propose wording that makes each **starting amount** explicit.
#pagebreak()
= 5.1 / A proportion of 100
The symbol % means “per hundred”. The percentage $p$% expresses the ratio $p/100$ relative to a chosen whole. Percentages can be smaller than 1% or greater than 100%; for example, 150% of the original amount means one and a half times the original.

#let n = 100
#figure(grid(columns: 10, gutter: 1pt, ..range(n).map(i => rect(width: 10pt, height: 10pt, stroke: none, fill: if i < 35 { teal } else { mist }))), caption: [Thirty-five of 100 cells represent 35%, or $7/20$ of the grid.])

#example([Worked example / Move between representations], [$3/8 = 0.375$. To find an equivalent quantity per hundred, $0.375 times 100 = 37.5$. Thus $3/8 = 37.5$%. The decimal point in the percentage does not make it approximate.])

== Practice 5.1
+ Write 6%, 62%, and 125% as decimals and simplified fractions.
+ Express $9/20$, $7/8$, and 0.004 as percentages.
+ Order $3/5$, 0.61 and 59.5%. Compare them using the same unit.
+ Two runners completed 80% and 75% of their routes. Can the second runner have run farther? Give actual route lengths that make this possible.
+ Mark 2.5% on a hundred-grid using whole and partial cells. Explain why filling 25 cells cannot represent 2.5%.
+ Give all whole-number percentages strictly between $1/8$ and $1/6$ of the same whole. Justify why no endpoint can enter the list.
#pagebreak()
= 5.2 / Finding a percentage of a quantity
To find $p$% of $Q$, compute $(p/100)Q$. A useful mental method decomposes a percentage into manageable parts. For 15%, use 10% plus half of that amount. Both parts must refer to the same original quantity.

#example([Worked example / Find the base], [Of 240 messages, 18 were flagged. The fraction is $18/240 = 3/40 = 0.075$, so 7.5% were flagged. If 18 is 7.5% of an unknown total, divide 18 by 0.075 to recover 240. Dividing by 7.5 would use the wrong unit.])

== Practice 5.2
+ Calculate 5%, 15% and 35% of 360 without a calculator. Show a common starting calculation.
+ A library has 640 books; 72 are in a display. Find the percentage on display.
+ A tile pattern is 12.5% blue. Exactly 42 tiles are blue. Find the total and explain your method.
+ Find 0.8% of 2,500. Explain why the answer is smaller than 1% of 2,500.
+ A class of 24 students records that 35% have a subscription. Show why 35% cannot be exact. If reported to the nearest 5 percentage points with ties rounding up, find the compatible student count or counts.
+ Two equal-sized classes combine data: one is 25% left-handed, the other 15%. Find the combined percentage. Construct a counterexample showing why your method might fail for unequal classes.
#pagebreak()
= 5.3 / Increasing and decreasing by a percentage
A 12% increase means keeping 100% and adding another 12%, so multiply by 1.12. A 12% decrease retains 88%, so multiply by 0.88. To reverse a change, divide by its multiplier; changing the sign of the original percentage does not usually reverse it.

#example([Worked example / Change the reference amount], [An 8,000 FCFA item falls by 25% to 6,000 FCFA. A 25% increase now adds 1,500 FCFA, giving 7,500 FCFA. To regain 8,000 FCFA you need an increase of 2,000 relative to 6,000, or $1/3$ of the reduced price.])

== Practice 5.3
+ Increase 480 by 15%; decrease 480 by 15%. Explain why the differences from 480 are equal.
+ A plant grows from 24 cm to 30 cm. Find the percentage increase. If it shrinks back to 24 cm, find the percentage decrease. Explain the difference.
+ An item costs 13,500 FCFA after a 10% discount. Find the original price and check by applying the discount.
+ Replace an increase of 10% followed by another increase of 20% with a single equivalent percentage increase.
+ Without assuming a specific initial amount, explain why decreasing by 10% then increasing by 10% gives a 1% loss.
+ A price falls by 40%. Is an increase of 60% enough to recover the original price? Give the exact recovery percentage.
#pagebreak()
= 5.4 / Discounts, taxes and budgets
Write a budget as a list of amounts with units and identify the base of each percentage. A fixed fee is added once; a proportional charge depends on a specified subtotal. If a rule is uncertain, calculate both interpretations and identify what you need to confirm.

#example([Worked example / Put the charges in order], [A workshop buys supplies priced at 12,000 FCFA before a 10% discount. In this example a 5% tax applies to the discounted supplies only; delivery is 800 FCFA. The discounted subtotal is 10,800 and the tax is 540, giving $10,800 + 540 + 800 = 12,140$ FCFA. Applying 5% to the original price would use the wrong base.])

== Practice 5.4
+ A 9,000 FCFA order receives 15% off, then adds a delivery fee of 600 FCFA. Find the total.
+ An advertised price of 11,000 FCFA already includes a 10% tax. Find the pre-tax price and the tax.
+ For a 12,000 FCFA bike repair, compare 15% off with a 1,700 FCFA fixed discount. What original price would make the two discounts equal? Give an exact fraction of FCFA if needed.
+ A shop offers 20% off clothing only. An order has 8,000 FCFA clothing and 4,000 FCFA food. Find the order discount as a percentage of the entire original bill.
+ A fundraiser budgets 8% of its money for supplies; after paying exactly that amount it has 23,000 FCFA left. Find the total budget and supplies amount.
+ Compare giving 10% off then adding 500 FCFA with adding 500 FCFA then giving 10% off. Decide whether the original price matters to the difference.
#pagebreak()
= Consolidate / Compare offers
== Investigate / When does a percentage offer win? (Criterion B practice)
Compare a fixed 1,200 FCFA discount with 15% off at original prices of 4,000, 8,000 and 12,000 FCFA. Tabulate the discount and final price. Find the break-even point and predict which offer wins on each side. Explain why the percentage option becomes relatively more attractive as the price rises. Generalise to a positive fixed discount $D$ and a percentage $p$ greater than zero. Which low prices would make an uncapped fixed-discount model unrealistic?

== Model / Supplies for a school repair day (Criterion D practice)
The organising team needs at least five boxes of materials. It can spend at most 34,000 FCFA and is comparing two shops. Shop A sells boxes at 6,500 FCFA with 12% off the merchandise subtotal and a fixed delivery charge of 2,000 FCFA. Shop B sells boxes at 6,200 FCFA and charges a fixed 800 FCFA delivery fee, which is waived if the merchandise subtotal reaches 35,000 FCFA. Orders must be placed entirely with one shop and only whole boxes can be bought.

+ Compare the total cost of five boxes at the two shops. Explain which costs are fixed and where each discount applies.
+ Find the largest affordable order at each shop. Show that all larger orders are unaffordable, taking Shop B's waiver threshold into account.
+ The team could obtain another 2,500 FCFA. Recheck order size and cost for both shops. Recommend a shop, stating whether your priority is lower cost or a larger order. Identify one assumption to confirm before buying.

== Mixed review
+ There are 18 unripe pieces in a crate of 120. Find the percentage that are ripe, assuming each piece is either ripe or unripe.
+ Find the percentage increase from 40 to 50 and the percentage decrease from 50 to 40.
+ *Challenge:* Two successive positive whole-number discounts each less than 20% reduce a price by exactly 23.5%. Find all possible unordered pairs. Hint: express the retained percentages as whole numbers and use factor pairs.

#example([Reflect], [Underline the reference amount used in each percentage calculation in your model. Where would switching the base lead to the most misleading conclusion?])
