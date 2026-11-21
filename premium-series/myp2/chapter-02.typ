#import "../shared/personal-pages.typ": author
#set document(title: "Mathematics · MYP2 · Proportional reasoning", author: author)
#let ink = rgb("102b40")
#let teal = rgb("245785")
#let mist = rgb("eaf2fb")
#set page(paper: "a4", margin: (x: 23mm, y: 21mm), header: align(right, text(size: 8pt, fill: teal)[MATHEMATICS / MYP2 / PROPORTION]), numbering: "1")
#set text(size: 11pt, fill: ink)
#set par(leading: .72em)
#show heading: set text(fill: teal)
#let example(title, body) = block(width: 100%, fill: mist, inset: 10pt, radius: 4pt, [#strong(title) #parbreak() #body])
= 03 / Proportional reasoning
= 02 / Proportional reasoning

A map that doubles every length preserves shapes. A print setting that adds two centimetres to each dimension does not. How can you recognise the difference from measurements alone?

#example([Inquiry lens], [*Key concept:* relationships. *Related concepts:* scale and representation. *Global context:* orientation in space and time. A constant scale links numerical representations to distances we cannot conveniently measure on paper.])

*Entry task:* Compare enlarging a 3 cm by 5 cm sketch by a factor of two with increasing both dimensions by 2 cm. Measure the long-to-short ratio before and after each change. Which change preserves the shape?
#pagebreak()
= 2.1 / Recognising proportional relationships
Two quantities are directly proportional if $y=k x$ for a fixed constant $k$. The ratio $y/x$ must stay constant for all non-zero inputs. A graph of a direct proportion lies on a straight line through the origin; a straight line alone is not enough.

#table(columns: 5, fill: (x,y)=>if y==0 {mist}, [Input], [0], [2], [4], [6], [Plan A], [0], [6], [12], [18], [Plan B], [2], [8], [14], [20])
#example([Worked example / Compare ratios, not differences], [For Plan A, $6/2=12/4=18/6=3$. For B, $8/2=4$ but $14/4=3.5$. B increases steadily, but the non-zero start prevents a constant ratio. The table is consistent with $y=3x$ for A and $y=3x+2$ for B.])

+ For each plan, predict an output at $x=8$ if its stated rule continues. Give the units of $k$ if output is litres and input is minutes.
+ Plot both plans on one grid using inputs from 0 to 8 and outputs from 0 to 26. Label the intercepts and explain what the intercept for B means.
+ Decide whether the pairs $(3,8)$, $(6,16)$ and $(9,25)$ could all follow one exact proportional rule. Name the pair you would remeasure if you suspected a recording error in one output.
+ Give a rule whose graph passes through the origin but is not proportional. Test it at two positive inputs.
+ A water meter initially reads 250 L. A tap adds 3 L per minute. Which quantity is proportional to time: the meter reading or water added? Explain why this distinction matters.
#pagebreak()
= 2.2 / Solving proportional problems
The unit-rate method finds the output per one unit of input and then scales to the required input. A scale-factor method multiplies both values by the same factor. The two give the same result if the model is proportional.

#example([Worked example / Two routes], [If 7 panels require 4.2 L, one requires 0.6 L, and 12 require 7.2 L. Alternatively multiply both entries by $12/7$. The second route keeps the original pair together, while the first makes the meaning of the constant explicit.])

+ At a fixed rate, 3.5 kg of grain cost 1,750 FCFA. Find the price of 6.2 kg.
+ A pump transfers 18 L in 45 s. Find how long 50 L would take if the rate is constant. Give the answer in seconds and in minutes and seconds.
+ An 8-portion recipe requires 300 g flour. A cook has 870 g. Find the largest number of whole portions possible and the flour left over.
+ A printer produces 24 finished cards in 6 minutes, including a 2-minute warm-up at the start. With no further pauses and a steady printing rate after warm-up, find the total time for 60 cards. Explain why simply scaling 6 minutes gives a wrong time.
+ Three reports claim that 12 items cost 2,700 FCFA, 20 items cost 4,500 FCFA and 24 items cost 5,500 FCFA. Assume exactly one reported cost is wrong and the true pricing is proportional. Identify and correct it.
#pagebreak()
= 2.3 / Scale drawings and similar figures
A scale of $1:200$ means one unit on the drawing represents 200 of the *same unit* in reality. Similar figures use one common scale factor for corresponding sides and preserve corresponding angles. If lengths scale by $k$, area scales by $k^2$, because both perpendicular dimensions scale by $k$.

#example([Worked example / Convert after scaling], [On a $1:250$ plan, a path measures 6.4 cm. Its real length is $6.4 times 250=1,600$ cm, or 16 m. A 1 cm by 1 cm square on this plan corresponds to 2.5 m by 2.5 m, not 2.5 square metres.])

+ At $1:400$, convert 3.6 cm to metres and convert 30 m to drawing centimetres.
+ A map bar shows 12 m by a printed length of 4 cm. Write the scale in simplest $1:n$ form.
+ A drawing of a 4 m by 6 m rectangle is enlarged from scale $1:100$ to $1:50$. Calculate the old and new drawing areas and explain their ratio.
+ Two rectangular plans measure 5 cm by 8 cm and 8 cm by 12 cm. Could one be an exact enlargement of the other? Explain why comparing only perimeters cannot establish similarity.
+ A map at $1:2,000$ is photocopied so that its printed lengths become 75% of their original size. Find the new scale and explain why multiplying the denominator by 0.75 is not correct.
#pagebreak()
= 2.4 / Investigate and model
== Investigation / Which drawings fit?
A rectangular venue is 24 m by 15 m. The drawing space is 18 cm by 12 cm. Keep the longer sides aligned. Make a table of drawing lengths and areas for scales $1:100$, $1:125$, $1:150$ and $1:200$. Predict all integer scale denominators that fit. Justify the threshold for each dimension, then explain which dimension controls the final choice. Test how the result changes if a 1 cm margin is required on every edge.

== Model / Make an accessible route plan
A school wants to display the diagram of a 30 m by 18 m courtyard. A route from the gate to the hall has two perpendicular segments of 12 m and 9 m. The available area for the diagram is 19 cm by 13 cm. Staff want a printed route width of at least 0.5 cm to remain legible; the actual route width is 1.2 m.

+ Find all scale denominators that can both fit the rectangular courtyard and show the width legibly. Keep longer sides aligned and use consistent units.
+ Select a scale from $1:150$, $1:175$, $1:200$ and $1:250$. If several work, choose the one that makes the diagram largest. Draw the boundary and a scale bar; show both route segments and label their lengths on the drawing.
+ A student uses the straight-line distance from gate to hall as the length travelled. State both distances and explain why the shorter distance cannot replace the route length.
+ The display is reduced to 80% of the chosen size. Recheck legibility, and explain why a scale bar copied with the image is safer than leaving a numerical scale unchanged.

== 2.5 / Review and reflection
+ Find $k$ from $y=18$ at $x=7.5$. Find $x$ at $y=30$ using the same model.
+ A straight line passes through $(2,5)$ and $(4,9)$. Explain why it is not a direct proportion.
+ A drawing of a square has side 7 cm at $1:80$. Calculate its actual area in square metres.
+ *Challenge:* Map A is $1:600$ and map B is $1:750$. What percentage enlargement of B makes a distance on B exactly match its length on A? Show why the same percentage cannot be used for area.

*Reflect:* Identify one assumption that could break a proportional model even when two measurements agree with it.
