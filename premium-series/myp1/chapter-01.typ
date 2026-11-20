#set document(title: "Mathematics · MYP1 · Number and accuracy", author: "SADIKOU MOUKODDIM")
#let ink = rgb("102b40")
#let accent = rgb("006e67")
#let mist = rgb("e9f5f2")
#set page(paper: "a4", margin: (x: 23mm, y: 22mm), header: align(right, text(size: 8pt, fill: accent)[MATHEMATICS / MYP1 / NUMBER]), numbering: "1")
#set text(size: 11pt, fill: ink)
#set par(leading: .72em)
#show heading: set text(fill: accent)
#let panel(label, body) = block(width: 100%, inset: 12pt, fill: mist, radius: 4pt, [#text(fill: accent, weight: "bold", label) #parbreak() #body])
#let rule = line(length: 100%, stroke: 1pt + accent)
#text(fill: accent, size: 12pt, weight: "bold")[MYP1 / STUDENT COURSEBOOK / CHAPTER PROOF]
#v(18mm)
#text(size: 42pt, weight: "bold")[Mathematics]
#v(3mm)
#rule
#v(8mm)
#text(size: 26pt)[01 / Number and accuracy]
#v(5mm)
The same count can be a precise inventory, a rounded headline or the basis for a decision. How can we tell which representation to use?
#v(12mm)
#image("assets/number-line.svg", width: 100%, alt: "Number line from −4 to 4 with A at −3 and B at 2")
#v(12mm)
#text(size: 14pt, weight: "bold")[SADIKOU MOUKODDIM]
#pagebreak()
= 01 / How precise should a number be?
#panel([Inquiry lens], [*Key concept:* relationships. *Related concepts:* representation and quantity. *Global context:* scientific and technical innovation.

*Statement of inquiry:* The way we represent quantities affects how we judge and communicate the accuracy of a decision.])

A repair workshop has *1,247 washers*. The storekeeper writes 1,247 in the inventory and tells a visitor there are “about 1,200”. A kit requires exactly 12 washers. Is either statement enough to tell whether the shop can fill 103 kits?

- *Factual:* What does each digit in 1,247 represent?
- *Conceptual:* How can different numbers produce the same rounded value?
- *Debatable:* When should a decision-maker insist on exact figures?

== Your route through the chapter
+ Classify and locate numbers.
+ Explain why zero matters in place-value notation.
+ Translate between standard, expanded and regrouped forms.
+ Compare and round numbers; recover a range from a rounded report.
+ Decide whether an estimate is precise enough to support a claim.

#panel([ATL / Communication], [Write a recommendation about the 103 kits before calculating. Exchange it with a partner. Mark the exact quantities, the approximations and the assumptions in each recommendation. Revisit both recommendations after section 1.5.])

== Before you start
List as many numbers as you can between 0 and 3. Compare lists. If one person chose only whole numbers and another chose fractions, which list answers the question as written? How could you change the wording to ask for just two answers?
#pagebreak()
= 1.1 / Number systems and the number line
A *whole number* belongs to the list $0, 1, 2, 3, dots$. The *integers* include the whole numbers and their negative counterparts. The word *natural* is used in two ways: some authors start at 0 and some at 1. Here we start at 1. A *rational number* can be written as a fraction of two integers with a non-zero denominator. Thus $-3$ is rational because it equals $-3/1$.

A number line has equally spaced marks for equal steps. A number farther right is greater. Negative numbers lie to the left of zero. Terminating decimals fit on the same line: $0.25 = 25/100$, one quarter of the distance from 0 to 1.

#image("assets/number-line.svg", width: 100%, alt: "A is three units left of zero; B is two units right of zero")

#panel([Worked example / Order or distance?], [Point A represents $-3$ and point B represents $2$. Since A is left of B, $-3 < 2$. But A is three units from zero while B is only two units from zero. To find the distance between A and B, go three units to zero and then two more: $3 + 2 = 5$ units.])

== Practice 1.1
+ Sketch a line from $-5$ to $5$. Locate $-4$, $0$, $2$ and $-1/2$.
+ From your four points, identify the integers, whole numbers and rational numbers. A point can belong to more than one group.
+ Write the integers between $-3$ and $3$, excluding the endpoints. Which is farthest from zero? Explain any tie.
+ A probe moves from 2 m above a reference level to 3 m below it. Draw and label both positions. How far down does it travel?
+ “Every rational number is an integer.” Give two counterexamples, one positive and one negative. Explain why 4 is not a counterexample.
+ Two integer points are seven units apart. One lies at $-2$. Find every possible location of the other point, and explain why there are no more.
#pagebreak()
= 1.2 / Place value and the role of zero
Our base-ten system uses ten digits. Each place is worth ten times the place to its right. To the right of the decimal point, the columns count tenths, hundredths and thousandths. In 4.06, the 6 counts six hundredths; in 4.6 it counts six tenths. A zero in a tens column means no tens are counted there; removing that zero can move other digits to new places.

#table(columns: 5, align: center, fill: (x,y) => if y == 0 { mist }, [Ten-thousands], [Thousands], [Hundreds], [Tens], [Ones], [4], [0], [6], [0], [8])

#panel([Worked example / Same digit, different value], [In 40,608 the 6 contributes 600. In 46,008 the same digit contributes 6,000 because it moved one place left. In 40,608, the two zeros show that neither thousands nor tens are counted. The numbers are not equal even though their digits are the same.])

== Practice 1.2
+ Write the value of each 7 in 70,707. What is the ratio of the largest value to the smallest?
+ Write a number with five thousands, two tens and six ones. Explain why 526 does not work.
+ Use 3, 0, 4, 0 and 9 once each to form the smallest five-digit number. Explain how you chose its first two digits.
+ Compare 4.06 and 4.6 using place values. Then, in 18,381, swap the two digits whose values are 8,000 and 80. Does the number change? Now swap the thousands and hundreds digits. Find the change.
+ A display shows 30,005 but its thousands light stops working, leaving a blank in that column. Why is interpreting the remaining symbols as 3,005 unsafe?
+ Find all four-digit numbers whose thousands digit is 6, whose tens digit is 0 and whose hundreds digit is twice their ones digit.

== 1.3 / Expanded and regrouped forms
Expanded form shows the contribution of each digit: $40,608 = 40,000 + 600 + 8$. A regrouped form may be more useful for a particular operation: $40,608$ is also 406 hundreds and 8 ones. Regrouping changes the units used to count, not the quantity. For a decimal, $3.407 = 3 + 4/10 + 7/1000$.

#panel([Worked example / Pack by hundreds], [To pack 3,742 washers in sleeves of 100, split the count into $3,700 + 42$. Since $3,700 = 37 times 100$, there are 37 full sleeves and 42 loose washers. Writing “37 hundreds” is more useful here than using separate thousands and hundreds.])
#pagebreak()
== Practice 1.3
+ Write 608,014 in expanded form. Then express it using only thousands and ones.
+ Write 5,040 as hundreds and a remainder, then as tens. Which expression gives the number of full cartons if each carton holds exactly 100 items?
+ A student writes $3 times 1,000 + 11 times 100 + 2 = 3,112$. Identify the regrouping error and correct the total.
+ A stockroom has 17 sealed boxes of 100 items, 23 packets of 10 and 14 loose items. How many items are there? If you repack them, what is the greatest possible number of sealed boxes?
+ Find two different ways to express 2,307 as a sum of whole thousands, hundreds and ones, using at least one hundred in each expression. Explain why neither expression needs any tens.

= 1.4 / Comparing and rounding
For whole numbers with the same number of digits, find the first place from the left where the digits differ. That place decides the comparison. A larger digit farther to the right cannot make up for the difference. For rounding, find the two adjacent multiples of the chosen unit and compare distances. In this chapter, exact halfway cases for non-negative numbers round to the larger multiple.

#panel([Worked example / The boundary matters], [To round 6,752 to the nearest hundred, compare 6,700 and 6,800. The halfway point is 6,750. The same method works for decimals: 3.746 is below 3.75, so it rounds to 3.7 to the nearest tenth. The number is above halfway, so the result is 6,800. For a whole number to round to 6,800, it must be at least 6,750 but less than 6,850. Why is 6,850 excluded?])

== Practice 1.4
+ Order 70,041; 70,104; 70,014; and 71,004. Underline the first digit that decides each adjacent comparison.
+ Order 0.7, 0.07 and 0.707; then round each to the nearest tenth.
+ Round 48,496 to the nearest ten, hundred and thousand. Round directly from the original each time.
+ Find all possible tens digits in 3,4□7 if the number rounds to 3,500 to the nearest hundred.
+ Round 1,449 first to the nearest hundred and then to the nearest thousand. Compare with rounding directly to the nearest thousand. Explain why the two results differ.
+ Two different whole numbers each round to 9,000 to the nearest thousand. How far apart can they be at most? Justify your endpoints.
#pagebreak()
= 1.5 / Estimation and sensible accuracy
An *estimate* is a value close enough for a stated purpose. To estimate quickly, replace numbers with nearby values that are easier to use. To guarantee a decision, use bounds or exact values. A convenient estimate alone does not tell you the direction or size of its error.

#panel([Worked example / A quick check and an exact decision], [Using 1,200 washers and 100 kits gives a rough sense of scale: about 12 per kit. But 103 kits actually need $103 times 12 = 1,236$ washers. The exact count of 1,247 leaves 11 spare. If we only knew there were “1,200 to the nearest hundred”, the count might be 1,150, which is not enough.])

== Practice 1.5
+ Estimate $398 + 607 + 194$ using nearby hundreds. Calculate exactly, then state how much your estimate overstates or understates the sum.
+ Without calculating exactly, explain why $29 times 41$ is greater than $29 times 40$ but less than $30 times 41$. Which bound helps you show that the product exceeds 1,100?
+ Four tickets cost 498 FCFA each. Give a quick estimate, then show without multiplying 498 by 4 directly whether 2,000 FCFA is enough. Find the change.
+ A newsletter reports 2,300 visitors, rounded to the nearest hundred. Could 2,340 visitors have attended? Could 2,350? Give the smallest possible attendance.
+ Two shops report sales of 1,500 items each, rounded to the nearest hundred. Find the least and greatest combined sales compatible with those reports. Is the rounded combined sale necessarily 3,000 to the nearest hundred?

== Investigation / The invisible intervals (Criterion B practice)
For each reported whole number 200, 300 and 400, determine all possible original whole numbers if the report used rounding to the nearest hundred. Draw each set on a number line and count the values. Predict and check the endpoints and counts for a report of 2,000 rounded to the nearest thousand. State a rule for positive reports that are multiples of a rounding unit of 10, 100 or 1,000. Justify why adjacent sets have no overlaps and no missing integers. At zero, how would the rule change if counts cannot be negative?
#pagebreak()
= Consolidate / Report a decision
#panel([Remember], [Order is about position; distance is about separation. A digit’s place determines its value. Expanded form records the place values; regrouping chooses units that suit the problem. Rounding gives a replacement value. A bound says how small or large the original could be.])

== Criterion D with communication practice / Reuse depot
A community reuse depot recorded washers in two bins. Its public board lists *850* and *650*, each rounded to the nearest ten. Volunteers must make 100 activity kits using 15 washers per kit. Unused washers go back into storage. The bins can be combined, and every washer counted in the stock has been inspected and can be used.

+ Identify which values are exact and which are not. Explain why adding the reported values alone cannot guarantee enough kits.
+ Build a two-row table showing the smallest and largest possible stock for each bin. Use it to decide how many complete kits the depot can guarantee. Show how the kit capacity is affected across the possible stock totals.
+ Loose washers can be ordered only in packs of 12. Recommend the minimum number of packs that guarantees 100 complete kits. State what you assumed about the counts and the order, and explain how to check your recommendation before spending money.
+ Write a three-sentence note for the volunteers. A reader should be able to tell what is known, what is guaranteed, and what remains uncertain.

*Evidence to aim for:* relevant quantities with units, justified rounding bounds, a whole-number kit count, and a recommendation tested against the least favourable stock.

== Mixed review / Knowing and understanding
+ Write $-4$, $2$, $-1/2$ and $0$ in increasing order. Identify the two most distant points and give their separation.
+ A counter shows 95,062. Find the difference after swapping the hundreds and tens digits. Explain using place values rather than only subtracting the two totals.
+ A number divided into hundreds leaves 43 hundreds and 89 ones. Write it in standard form, then round it to the nearest ten and nearest hundred.
+ *Challenge:* Find all whole numbers that round to 2,500 to the nearest hundred and 2,000 to the nearest thousand. Explain why your range cannot be extended at either end.

#panel([Reflect], [Return to the workshop recommendation. Mark one place where an exact count is essential and one place where a rounded count is adequate. Explain why the audience or purpose changes your choice.])
