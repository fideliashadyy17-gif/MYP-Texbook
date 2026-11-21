#import "personal-pages.typ": author
#let accents = (rgb("006e67"), rgb("245785"), rgb("6c4383"), rgb("963e2e"), rgb("375b36"))
#let subtitles = (
  "Number, pattern and measurement", "Proportion, space and chance",
  "Structure, relationships and evidence", "Functions, precision and variation",
  "Models, transformations and proof",
)
#let cover(level, back: false) = {
  let accent = accents.at(level - 1)
  set page(paper: "a4", margin: 25mm)
  set text(fill: rgb("102b40"), size: 12pt)
  set par(leading: .8em)
  text(size: 12pt, tracking: 1pt, fill: accent, weight: "bold")[MYP #level / STUDENT COURSEBOOK]
  v(20mm)
  text(size: 40pt, weight: "bold")[Mathematics]
  v(4mm)
  text(size: 17pt, fill: accent, subtitles.at(level - 1))
  v(10mm)
  line(length: 100%, stroke: 1pt + accent)
  v(10mm)
  if back {
    [This coursebook develops mathematical fluency through examples and practice, and asks students to explain why their methods work. Investigations move from particular cases to general rules. Modelling tasks ask students to make assumptions explicit, test decisions against constraints, and communicate the limits of a result.]
  } else {
    // For any n, the array contains n² cells. The darker border has 2n−1 cells.
    let n = level + 4
    grid(columns: n, gutter: 1pt, ..range(n*n).map(i => rect(
      width: 11pt, height: 11pt, stroke: none,
      fill: if i < n or calc.rem(i,n) == n - 1 { accent } else { accent.lighten(76%) },
    )))
    v(3mm)
    text(size: 9pt)[From $#(n - 1)^2$ to $#n^2$: a border of $#(2*n - 1)$ cells.]
  }
  v(1fr)
  text(size: 14pt, weight: "bold", author)
}
