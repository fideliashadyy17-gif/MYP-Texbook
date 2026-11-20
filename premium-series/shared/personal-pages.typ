// Only author-approved text should replace these explicit proof placeholders.
#let author = "SADIKOU MOUKODDIM"
#let personal-pages(level, dedication: none, acknowledgements: none, biography: none) = {
  set page(paper: "a4", margin: (x: 30mm, y: 25mm))
  set text(size: 12pt, fill: rgb("102b40"))
  set par(leading: .8em)
  let entries = (
    ("Dedication", dedication, "Author-approved dedication to come."),
    ("Acknowledgements", acknowledgements, "Author-approved names and acknowledgements to come."),
    ("About the Author", biography, "Author-approved biography to come."),
  )
  for (index, (title, body, placeholder)) in entries.enumerate() {
    if index > 0 { pagebreak() }
    text(size: 9pt, tracking: 1.3pt, fill: rgb("006e67"))[MATHEMATICS / MYP#level / STUDENT COURSEBOOK]
    v(if index == 0 { 57mm } else { 30mm })
    text(size: 32pt, weight: "bold", title)
    v(7mm)
    line(length: 28mm, stroke: 1pt + rgb("006e67"))
    v(6mm)
    if index == 2 { strong(author); parbreak() }
    if body == none { text(fill: rgb("506777"), style: "italic", placeholder) } else { body }
  }
}
