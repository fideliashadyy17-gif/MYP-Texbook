#!/usr/bin/env python3
"""Build the MYP1 Chapter 7 correction prototype. Editable source; outputs index.html and exercises.json."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
G = '#0d2a28'; GOLD = '#d7a55d'; RUST = '#b24f32'; INK = '#1d2523'; MUT = '#5c6663'

def svg(w, h, body):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img">{body}</svg>'

def line(x1,y1,x2,y2,stroke=G,sw=2,dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def text(x,y,s,fill=INK,size=13,anchor='middle',cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" text-anchor="{anchor}"{c}>{s}</text>'

def poly(points, stroke=G, fill='none', sw=2):
    return f'<polygon points="{points}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def circle(cx,cy,r,stroke=G,fill='none',sw=2,dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def arc(cx,cy,r,a0,a1,stroke=RUST,sw=2):
    import math
    x0=cx+r*math.cos(math.radians(a0)); y0=cy+r*math.sin(math.radians(a0))
    x1=cx+r*math.cos(math.radians(a1)); y1=cy+r*math.sin(math.radians(a1))
    large = 1 if abs(a1-a0)>180 else 0
    return f'<path d="M {x0:.1f} {y0:.1f} A {r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{stroke}" stroke-width="{sw}"/>'

# ---- diagrams -------------------------------------------------------------
COVER = svg(500,260,
    poly('60,220 440,220 250,40', GOLD, 'none', 2.5) +
    line(145,140,355,140,GOLD,2) + line(250,40,250,220,GOLD,1.5,'5 5') +
    arc(60,220,34,-63,0,GOLD,1.5) + arc(440,220,34,180,243,GOLD,1.5) +
    circle(60,220,4,RUST,RUST) + circle(440,220,4,RUST,RUST) + circle(250,40,4,RUST,RUST) +
    text(250,248,'equal slopes · horizontal collar · exact template',GOLD,12))

ANGLE_LINE = svg(500,170,
    line(40,120,460,120) + line(250,120,340,38) +
    arc(250,120,34,-43,0,RUST) + arc(250,120,44,180,317,GOLD) +
    text(315,105,'65°',RUST) + text(185,105,'x',G,15,'middle','math') +
    text(40,145,'A',INK,12,'start') + text(460,145,'B',INK,12,'end'))

CROSSING = svg(500,190,
    line(60,160,440,40) + line(60,40,440,160) +
    text(250,55,'115°',RUST) + text(330,105,'x',G,15,'middle','math') +
    text(250,165,'y',G,15,'middle','math') + text(170,105,'z',G,15,'middle','math'))

PARALLEL = svg(500,210,
    line(40,60,460,60) + line(40,160,460,160) + line(160,20,340,200) +
    text(470,64,'l',INK,13,'start','math') + text(470,164,'m',INK,13,'start','math') +
    text(245,82,'65°',RUST) + text(330,185,'a',G,15,'middle','math') +
    text(185,150,'b',G,15,'middle','math') + text(315,150,'c',G,15,'middle','math') +
    text(60,40,'parallel lines',MUT,11,'start'))

ISOSCELES = svg(500,200,
    poly('250,30 120,180 380,180') +
    line(180,100,190,110,RUST,2) + line(310,110,320,100,RUST,2) +
    arc(250,30,30,60,120,RUST) + text(250,80,'40°',RUST) +
    text(150,170,'x',G,15,'middle','math') + text(350,170,'x',G,15,'middle','math') +
    text(250,195,'equal sides marked',MUT,11))

HEXAGON = svg(500,210,
    poly('250,20 410,70 410,150 250,200 90,150 90,70') +
    line(250,20,410,150,GOLD,1.5) + line(250,20,250,200,GOLD,1.5) + line(250,20,90,150,GOLD,1.5) +
    text(330,90,'1',G) + text(330,150,'2',G) + text(170,150,'3',G) + text(170,90,'4',G) +
    text(250,208,'one vertex → four triangles',MUT,11))

BISECTOR = svg(500,220,
    line(100,120,400,120) + circle(100,120,170,GOLD, 'none',1.5,'5 4') + circle(400,120,170,GOLD,'none',1.5,'5 4') +
    line(250,25,250,210,RUST,2) + circle(100,120,3,G,G) + circle(400,120,3,G,G) +
    circle(250,40,3,RUST,RUST) + circle(250,200,3,RUST,RUST) +
    text(95,145,'A',INK,13,'end') + text(405,145,'B',INK,13,'start') +
    text(262,38,'P',RUST,13,'start') + text(262,205,'Q',RUST,13,'start') +
    text(250,216,'same radius greater than half AB',MUT,11))

TRUSS = svg(500,210,
    poly('60,180 440,180 250,40') + line(145,117,355,117,GOLD,2) +
    arc(60,180,34,-36,0,RUST) + arc(440,180,34,180,216,RUST) +
    text(105,170,'65°',RUST) + text(395,170,'65°',RUST) + text(250,75,'?',G,16) +
    text(250,200,'base',MUT,11) + text(250,110,'collar parallel to base',MUT,10))

GATES = svg(500,190,
    line(80,140,420,140,GOLD,1.5,'5 4') + line(250,30,250,175,RUST,2) +
    circle(100,140,5,G,G) + circle(400,140,5,G,G) +
    text(100,165,'A',INK,13) + text(400,165,'B',INK,13) +
    text(262,45,'path',RUST,12,'start') + text(250,185,'every point on the path is equally distant from A and B',MUT,10))

KITE = svg(500,210,
    poly('250,20 380,105 250,190 120,105') + line(120,105,380,105,GOLD,1.5) +
    text(250,55,'40°',RUST) + text(160,100,'70°',G) + text(340,100,'?',G,15) +
    text(250,205,'two congruent triangles',MUT,11))

EXTERIOR = svg(500,190,
    poly('100,150 330,150 220,50') + line(330,150,450,150) +
    arc(330,150,34,180,230,RUST) + text(390,135,'110°',RUST) +
    text(140,140,'60°',G) + text(235,80,'50°',G) +
    text(250,180,'exterior angle = sum of the two opposite interior angles',MUT,10))

BORDERLINE = svg(500,190,
    line(60,140,450,140) + circle(60,140,150,GOLD,'none',1.5,'5 4') + circle(450,140,240,GOLD,'none',1.5,'5 4') +
    circle(210,140,4,RUST,RUST) + text(135,125,'5 cm',G) + text(330,125,'8 cm',G) +
    text(250,170,'13 cm base · arcs meet on the line',MUT,11))

DESIGN = svg(500,200,
    poly('80,170 420,170 250,40') + line(250,40,250,170,GOLD,1.5,'5 4') +
    text(160,100,'x',G,15,'middle','math') + text(340,100,'x',G,15,'middle','math') +
    text(250,190,'8 m base',MUT,11))

# ---- exercise data --------------------------------------------------------
ITEMS = [
 ('F1','Foundation','Classify each angle: 35°, 90°, 125°, 210°.',None,'Acute, right, obtuse, reflex.','Compare with 90°, 180° and 360°.'),
 ('F2','Foundation','Find x on the straight line.',ANGLE_LINE,'115°.','Angles on a straight line sum to 180°: 180−65.'),
 ('F3','Foundation','Three angles around a point are 90°, 110° and 75°. Find the fourth.',None,'85°.','360−(90+110+75).'),
 ('F4','Foundation','Two lines cross. One angle is 115°. Find x, y and z.',CROSSING,'x=65°, y=115°, z=65°.','Vertically opposite angles are equal; adjacent angles sum to 180°.'),
 ('F5','Foundation','In a parallel-line diagram, angle 3 and angle 6 are alternate. If angle 3=68°, find angle 6 and the co-interior angle 5.',None,'Angle 6=68°; angle 5=112°.','Alternate angles are equal; co-interior angles sum to 180°.'),
 ('F6','Foundation','A triangle has angles 35° and 85°. Find the third angle and classify the triangle.',None,'60°; acute scalene.','180−35−85; all angles are acute and different.'),
 ('F7','Foundation','Name the polygons with 5, 6 and 8 sides.',None,'Pentagon, hexagon, octagon.','Polygon names count sides.'),
 ('F8','Foundation','Which construction locates all points equally distant from A and B? A) angle bisector B) perpendicular bisector C) parallel line D) circle centre A.',None,'B.','The perpendicular bisector is the locus of points equidistant from A and B.'),
 ('D1','Developing','Use the parallel-line diagram. Find a, b and c.',PARALLEL,'a=65°, b=65°, c=115°.','Corresponding and alternate angles are equal; co-interior angles sum to 180°.'),
 ('D2','Developing','The angles of a triangle are x, 2x and 3x. Find x and classify the triangle.',None,'x=30°; angles 30°, 60°, 90°; right triangle.','x+2x+3x=180.'),
 ('D3','Developing','Find each base angle x.',ISOSCELES,'70° each.','(180−40)÷2; base angles of an isosceles triangle are equal.'),
 ('D4','Developing','An exterior angle of a triangle is 115°. One opposite interior angle is 48°. Find the other opposite interior angle and the adjacent interior angle.',None,'67° and 65°.','115−48; 180−115.'),
 ('D5','Developing','Complete the table: quadrilateral → __ triangles, __°; pentagon → __ triangles, __°; hexagon → __ triangles, __°.',HEXAGON,'Quadrilateral: 2 triangles, 360°. Pentagon: 3, 540°. Hexagon: 4, 720°.','An n-gon splits into n−2 triangles; multiply by 180°.'),
 ('D6','Developing','A regular polygon has exterior angle 45°. Find the number of sides and each interior angle.',None,'8 sides; interior 135°.','360÷45; 180−45.'),
 ('D7','Developing','Order the steps for a perpendicular bisector of AB=8 cm: (i) draw arcs from A and B with the same radius; (ii) draw AB; (iii) join the arc intersections; (iv) open the compass to more than half of AB. State the radius condition.',BISECTOR,'ii, iv, i, iii; radius >4 cm.','The arcs must meet; the line through the intersections is perpendicular and bisects AB.'),
 ('D8','Developing','Test whether these triples can form a triangle: 3,4,8; 5,5,9; 6,7,10.',None,'No; yes; yes.','Compare the sum of the two shorter sides with the longest.'),
 ('A1','Application','A ramp makes 12° with the ground. What angle does it make with a vertical post?',None,'78°.','Ground and vertical are perpendicular: 90−12.'),
 ('A2','Application','The truss has equal base angles of 65°. Find the apex angle, the exterior angle at a base, and classify the triangle.',TRUSS,'Apex 50°; exterior 115°; isosceles.','180−65−65; 180−65; equal base angles imply equal rafters.'),
 ('A3','Application','A scale drawing uses 1:20. The model base is 30 cm. Find the real base in metres.',None,'6 m.','30×20=600 cm=6 m.'),
 ('A4','Application','A path must pass through points equally distant from gates A and B. Which construction locates the path? Explain.',GATES,'Perpendicular bisector of AB.','Every point on the perpendicular bisector is equidistant from A and B.'),
 ('A5','Application','A collar is parallel to the base. At a rafter joint it makes a 66° co-interior angle. Find the angle on the other side of the collar at that joint.',None,'114°.','Co-interior angles sum to 180°.'),
 ('A6','Application','The kite is made from two congruent triangles. One triangle has angles 40° and 70°. Find the missing angle and explain why the matching angle in the other triangle is equal.',KITE,'70°; corresponding angles of congruent triangles are equal.','180−40−70; congruence preserves angles.'),
 ('A7','Application','A student says a triangle with sides 4 cm, 4 cm and 9 cm is possible because 4+9>4. Correct the reasoning.',None,'Impossible: the two shorter sides give 4+4<9.','The triangle inequality must be checked using the two shorter sides against the longest.'),
 ('R1','Reasoning','Can a triangle have two obtuse angles? Explain.',None,'No.','Two obtuse angles already sum to more than 180°.'),
 ('R2','Reasoning','True or false: any two angles between parallel lines are equal. Justify.',None,'False.','Corresponding and alternate angles are equal; co-interior angles are supplementary.'),
 ('R3','Reasoning','A student says the exterior angle 110° should be added to the opposite interior angles 60° and 50° to make 180°. Identify the error and correct it.',EXTERIOR,'The exterior angle equals the sum of the two opposite interior angles: 110°=60°+50°. It is not added to them to make 180°.','The adjacent interior angle is 70°; 110° and 70° are supplementary.'),
 ('R4','Reasoning','Complete the missing steps: a heptagon has __ sides, splits into __ triangles, so its interior angle sum is __.',None,'7 sides; 5 triangles; 900°.','(7−2)×180.'),
 ('R5','Reasoning','A student uses a compass radius of 2 cm to bisect a 6 cm segment. The arcs do not meet. Explain why and state a suitable radius.',None,'The radius must be greater than half of 6 cm, so greater than 3 cm; 2 cm is too small.','Equal-radius arcs meet only when the radius exceeds half the segment.'),
 ('R6','Reasoning','Use the arcs to explain why sides 5 cm, 8 cm and 13 cm do not form a triangle.',BORDERLINE,'They form a degenerate straight line because 5+8=13.','Equality gives zero area; the two shorter sides must exceed the longest.'),
 ('R7','Reasoning','Why should construction arcs be kept visible?',None,'They record the equal radii and the defining property, so the construction can be checked.','A construction is an argument made with instruments.'),
 ('C1','Challenge','Two sides of a triangle are 7 cm and 11 cm. The third side is a whole number of centimetres. Find all possible values.',None,'5 through 17 cm.','11−7 < x < 11+7, so 4 < x < 18.'),
 ('C2','Challenge','Construct an isosceles triangle with equal sides 6 cm and base 8 cm. Explain why the perpendicular bisector of the base passes through the apex.',None,'The apex is equidistant from the base endpoints, so it lies on the perpendicular bisector.','Equal sides place the apex on the locus of points equidistant from the endpoints.'),
 ('C3','Challenge','A regular polygon has each interior angle five times its exterior angle. Find the number of sides.',None,'12 sides.','Interior + exterior =180°; 6e=180°, e=30°, n=360÷30.'),
 ('C4','Challenge','A truss has an 8 m base and equal rafters of length x m. Find the smallest whole-number value of x that makes a triangle.',DESIGN,'5 m.','2x>8, so x>4; x=4 gives a degenerate straight line.'),
 ('C5','Challenge','Use compass arcs to explain why the two shorter sides of a triangle must together exceed the longest side.',None,'If the base is the longest side c, arcs of radius a and b from the endpoints meet above the base only when a+b>c. If a+b=c they meet on the base; if a+b<c they do not meet.','The arc intersection is the possible apex; no intersection means no triangle.'),
]

VISUAL_IDS = [i[0] for i in ITEMS if i[3]]
assert len(ITEMS)==35, len(ITEMS)
assert len(VISUAL_IDS)==12, VISUAL_IDS

def item_html(it):
    id,tier,prompt,vis,ans,why = it
    v = f'<div class="visual">{vis}</div>' if vis else ''
    return f'<div class="item"><div class="id">{id}<span class="tier">{tier}</span></div><div><p class="prompt">{prompt}</p>{v}<div class="workline"></div></div></div>'

def ex_head(title, rng):
    return f'<div class="exercise-head"><h3>{title}</h3><span class="range">{rng}</span></div>'

def page(body, cls='', head=True):
    h = '<div class="running-head"><span>Part IV · Shape, structure and measure</span><span>Chapter 7 · Lines, angles, triangles and constructions</span></div>' if head else ''
    return f'<section class="page {cls}">{h}{body}</section>'

def ans_block(it):
    id,tier,prompt,vis,ans,why = it
    return f'<div class="answer-block"><span class="id">{id}</span> <span class="sol">{ans}</span><div class="why">{why}</div></div>'

P = []
# 1 cover
P.append(page(f'''
<div class="part">Part IV · Shape, structure and measure · MYP Year 1 · Chapter 07</div>
<div>
<h1>Lines, angles, triangles and constructions</h1>
<p class="standfirst">A single straight line contains 180°, and a full turn contains 360°. From those two facts, and one statement about parallel lines, an entire system of shape reasoning follows. Constructions turn that reasoning into a repeatable physical procedure.</p>
<div class="figure">{COVER}</div>
<div class="chips"><span class="chip">Key concept · Relationships</span><span class="chip">Related · Space</span><span class="chip">Related · Representation</span><span class="chip">Context · Orientation in space and time</span></div>
<div class="inquiry"><div class="label">Inquiry</div><p>A workshop needs a triangular roof truss with equal slopes and a horizontal collar beam. Which angles must the carpenter set, how can the shape be checked without measuring every angle, and how can a full-size template be reproduced exactly?</p></div>
</div>
<div class="foot"><span>MYP Mathematics 1</span><span>Student coursebook · Prototype</span></div>
''', 'cover', head=False))
# 2 opener
P.append(page(f'''
<div class="kicker">Chapter 7 · Opener</div><h2>Reasoning with straight lines</h2>
<p class="lede">Geometry begins with a few reliable facts and becomes powerful when those facts are connected. In this chapter you will name angle relationships, explain triangle and polygon sums, and use equal-radius constructions to force a property rather than guess it.</p>
<div class="callout"><div class="label">Engagement</div><p>Before cutting timber, a carpenter can test a design with a scale drawing. Which measurements are enough to guarantee the shape? Which checks protect against a drawing that only looks correct?</p></div>
<h3>Inquiry questions</h3>
<ul><li><strong>Factual:</strong> What do angles on a straight line and around a point add to?</li><li><strong>Conceptual:</strong> Why must the two shorter sides of a triangle together exceed the longest side?</li><li><strong>Debatable:</strong> When is a construction reliable enough to build from?</li></ul>
<div class="grid-2"><div class="card"><h3>Learning goals</h3><ul><li>Use angle facts on lines, at points and with parallel lines.</li><li>Reason with triangle and polygon angle sums.</li><li>Apply the triangle inequality and regular-polygon facts.</li><li>Construct perpendicular bisectors, angle bisectors and SSS triangles.</li></ul></div><div class="card pale"><h3>MYP lens</h3><p><strong>Key concept:</strong> Relationships</p><p><strong>Related concepts:</strong> Space, Representation</p><p><strong>Global context:</strong> Orientation in space and time</p><p><strong>Criteria:</strong> A, B, C and D in separate tasks</p></div></div>
<div class="atl"><strong>ATL focus.</strong> In order for a student to think creatively and critically, students must choose an appropriate geometric fact or construction, test a design and explain why the method is reliable.</div>
<p class="small"><strong>Language bank:</strong> acute · right · obtuse · reflex · vertically opposite · corresponding · alternate · co-interior · isosceles · exterior angle · polygon · perpendicular bisector · angle bisector · construction</p>
'''))
# 3 inquiry launch
P.append(page(f'''
<div class="kicker">Chapter 7 · Inquiry launch</div><h2>Which lengths close a triangle?</h2>
<p class="lede">Three strips joined end to end may or may not close a triangle. Predict first, then test with compass arcs. Do not state a rule until the evidence forces it.</p>
<table><tr><th>Side lengths (cm)</th><th>Prediction</th><th>Arcs meet above the base?</th><th>Triangle?</th></tr>
<tr><td>3, 4, 5</td><td></td><td></td><td></td></tr><tr><td>3, 4, 8</td><td></td><td></td><td></td></tr><tr><td>4, 5, 9</td><td></td><td></td><td></td></tr><tr><td>6, 7, 10</td><td></td><td></td><td></td></tr><tr><td>2, 2, 3</td><td></td><td></td><td></td></tr></table>
<div class="figure">{BORDERLINE}</div>
<div class="callout blue"><div class="label">Observe</div><p>When the arcs meet on the base, the “triangle” has zero area. When they do not meet, there is a gap. What must be true about the two shorter lengths for a real apex to exist?</p></div>
<div class="workspace"></div>
<p class="small muted">Keep this prediction. You will return to it in the investigation on pages 17–18 and compare your first ideas with the evidence.</p>
'''))
# 4 ready check + map
P.append(page(f'''
<div class="kicker">Chapter 7 · Start here</div><h2>Ready check and chapter map</h2>
<p class="lede">Use the ready check to find the ideas you already control. Then follow the map from concrete angle facts to constructions and design decisions.</p>
<div class="card sand"><h3>Ready check</h3><p>Before starting, answer <strong>F1, F3, F6 and F8</strong> from the Foundation bank on page 7. If any answer is uncertain, review the turn model in 7.1 before moving on.</p></div>
<div class="card"><h3>Chapter map</h3><ol><li><strong>7.1 Lines, angles and angle facts</strong> — name the relationship first: straight line, full turn, vertically opposite or right angle.</li><li><strong>7.2 Parallel lines and triangles</strong> — use corresponding, alternate and co-interior angles only when the lines are parallel.</li><li><strong>7.3 Polygons and the triangle inequality</strong> — split polygons into triangles; test whether three lengths can close a triangle.</li><li><strong>7.4 Ruler-and-compass constructions</strong> — use equal radii to force a property, keep arcs visible and check the defining relationship.</li></ol></div>
<div class="callout"><div class="label">Explain how you know</div><p>For every answer, be ready to give a method, a diagram or a reason. A correct result without a check is only half an explanation.</p></div>
'''))
# 5 7.1 theory
P.append(page(f'''
<div class="kicker">Chapter 7 · Mathematical development</div><h2>7.1 Lines, angles and angle facts</h2>
<div class="callout"><div class="label">Big idea</div><p>Name the relationship first: straight line, full turn, vertically opposite or right angle.</p></div>
<p>An angle measures a turn. A half-turn along a straight line is 180°, so adjacent angles on a straight line are supplementary. A full turn about a point is 360°, so angles around a point sum to 360°. When two straight lines cross, the angles opposite each other are vertically opposite and equal.</p>
<div class="figure">{ANGLE_LINE}<div class="caption">Figure 7.1 · The angle x and 65° lie on a straight line, so x+65°=180°.</div></div>
<p>Classify angles as acute (&lt;90°), right (90°), obtuse (between 90° and 180°), straight (180°) or reflex (between 180° and 360°). A diagram is not always drawn to scale, so use stated facts rather than appearance.</p>
<div class="card pale"><h3>Key idea</h3><p>Straight line: 180°. Full turn: 360°. Vertically opposite: equal. Right angle: 90°. The middle letter of ∠ABC names the vertex B.</p></div>
'''))
# 6 7.1 worked + guided
P.append(page(f'''
<div class="kicker">Chapter 7 · Worked modelling</div><h2>7.1 Worked examples and guided practice</h2>
<div class="example"><div class="example-title">Worked example 7.1.1 · Missing angle on a line</div><p>Two adjacent angles on a straight line are 47° and x. Find x.</p><ol class="steps"><li>Angles on a straight line sum to 180°.</li><li>x = 180−47 = 133°.</li><li>Check: 47+133=180.</li></ol><div class="answer">x=133°.</div></div>
<div class="example"><div class="example-title">Worked example 7.1.2 · Angles around a point</div><p>Four angles meet at a point: 95°, 120°, 85° and x. Find x.</p><ol class="steps"><li>Angles around a point sum to 360°.</li><li>x = 360−(95+120+85) = 60°.</li><li>Check: 95+120+85+60=360.</li></ol><div class="answer">x=60°.</div></div>
<div class="callout rust"><div class="label">Common error</div><p>Do not swap the totals: a straight line is 180°, a full turn is 360°. Do not treat vertically opposite angles as supplementary; they are equal. The adjacent pair is supplementary.</p></div>
<div class="card"><h3>Guided practice · copy and complete</h3><p>Angles on a straight line: 118° + □ = 180°, so the missing angle is □°. Angles at a point: 95° + 120° + 85° + □ = 360°, so the missing angle is □°. Vertically opposite: if one angle is 47°, the opposite angle is □°, and each adjacent angle is 180−□ = □°.</p></div>
'''))
# 7 Foundation
P.append(page(ex_head('Practice 7.1 · Foundation','F1–F8') + ''.join(item_html(i) for i in ITEMS[:8])))
# 8 7.2 parallel
P.append(page(f'''
<div class="kicker">Chapter 7 · Mathematical development</div><h2>7.2 Parallel lines and triangles</h2>
<p>A transversal is a line that crosses two or more other lines. When the crossed lines are parallel, the eight angles formed fall into equal or supplementary families.</p>
<div class="figure">{PARALLEL}<div class="caption">Figure 7.2 · With l ∥ m: corresponding and alternate angles are equal; co-interior angles sum to 180°.</div></div>
<div class="card pale"><h3>Key idea</h3><p>Corresponding angles sit in the same position at each intersection and are equal. Alternate angles lie on opposite sides of the transversal between the parallel lines and are equal. Co-interior angles lie on the same side between the parallel lines and are supplementary.</p></div>
<div class="callout rust"><div class="label">Watch for this misconception</div><p>Do not assume lines are parallel or angles equal unless marked or stated. “Looks like 90°” is not a reason.</p></div>
'''))
# 9 triangles
P.append(page(f'''
<div class="kicker">Chapter 7 · Mathematical development</div><h2>Triangle sums and exterior angles</h2>
<p>Every triangle has an angle sum of 180°. This follows from the parallel-line facts. Triangles are classified by sides as equilateral, isosceles or scalene, and by angles as acute, right or obtuse. In an isosceles triangle the angles opposite the equal sides are equal.</p>
<div class="figure">{ISOSCELES}<div class="caption">Figure 7.3 · Equal sides force equal base angles.</div></div>
<div class="example"><div class="example-title">Worked example 7.2.1 · Isosceles base angles</div><p>An isosceles triangle has apex angle 40°. Find each base angle.</p><ol class="steps"><li>Base angles are equal; call each x.</li><li>2x+40=180, so 2x=140.</li><li>x=70°.</li></ol><div class="answer">Each base angle is 70°.</div></div>
<p>An exterior angle of a triangle equals the sum of the two opposite interior angles. It is supplementary to the interior angle at the same vertex.</p>
'''))
# 10 D1-D4
P.append(page(ex_head('Practice 7.2 · Developing','D1–D4') + ''.join(item_html(i) for i in ITEMS[8:12]) + '<div class="workspace"></div>'))
# 11 polygons
P.append(page(f'''
<div class="kicker">Chapter 7 · Mathematical development</div><h2>7.3 Polygons and their angles</h2>
<p>A polygon is a closed plane shape made from straight sides. Choose one vertex and draw diagonals to every non-adjacent vertex. The polygon is divided into triangles. An n-sided polygon divides into n−2 triangles, so its interior angle sum is (n−2)×180°.</p>
<div class="figure">{HEXAGON}<div class="caption">Figure 7.4 · A hexagon splits into four triangles; the interior angle sum is 4×180°=720°.</div></div>
<div class="example"><div class="example-title">Worked example 7.3.1 · Regular polygon</div><p>A regular polygon has exterior angle 45°. Find the number of sides and each interior angle.</p><ol class="steps"><li>Exterior angles of any convex polygon sum to 360°.</li><li>n = 360÷45 = 8.</li><li>Interior = 180−45 = 135°.</li></ol><div class="answer">8 sides; each interior angle 135°.</div></div>
<div class="card pale"><h3>Key idea</h3><p>Interior sum: (n−2)×180°. Exterior sum: 360°. Regular polygon: each exterior = 360÷n; each interior = 180−360÷n.</p></div>
'''))
# 12 D5-D8
P.append(page(ex_head('Practice 7.3 · Developing','D5–D8') + ''.join(item_html(i) for i in ITEMS[12:16]) + '<div class="card"><h3>Guided practice · copy and complete</h3><p>A pentagon has □ sides, splits into □ triangles, so its interior angle sum is □×180° = □°. A regular hexagon has each exterior angle 360÷□ = □°, so each interior angle is 180−□ = □°.</p></div>'))
# 13 constructions
P.append(page(f'''
<div class="kicker">Chapter 7 · Mathematical development</div><h2>7.4 Constructions with ruler and compass</h2>
<p>A construction is an argument made with instruments. Each arc records a fixed distance from a named point, so the finished drawing contains evidence: equal radii, equal distances, and a property that can be checked.</p>
<div class="figure">{BISECTOR}<div class="caption">Figure 7.5 · The perpendicular bisector of AB is the line through the two equal-radius arc intersections.</div></div>
<table><tr><th>Construction</th><th>Compass setting</th><th>How to test</th></tr><tr><td>Perpendicular bisector of AB</td><td>One radius greater than half AB, unchanged from A and B</td><td>Crosses AB at its midpoint and makes 90°</td></tr><tr><td>Angle bisector</td><td>Arc from vertex cuts both arms; same radius from those points</td><td>Two half-angles are equal</td></tr><tr><td>Triangle from three sides</td><td>Base equal to one side; radii equal to the other two sides</td><td>Arcs meet; two shorter sides exceed the longest</td></tr></table>
'''))
# 14 worked construction
P.append(page(f'''
<div class="kicker">Chapter 7 · Worked modelling</div><h2>7.4 Worked construction and guided steps</h2>
<div class="example"><div class="example-title">Worked example 7.4.1 · SSS triangle</div><p>Construct a triangle with sides 5 cm, 6 cm and 7 cm.</p><ol class="steps"><li>Draw base AB=7 cm.</li><li>Open the compass to 5 cm; draw an arc from A.</li><li>Open the compass to 6 cm; draw an arc from B.</li><li>Label the intersection C and join AC and BC.</li><li>Check: 5+6>7, so the arcs meet above the base.</li></ol><div class="answer">Triangle ABC has the required three sides. Keep the arcs visible.</div></div>
<div class="callout rust"><div class="label">Common error</div><p>Never change the compass between a pair of arcs. If the radius is not greater than half the segment, the arcs for a perpendicular bisector will not meet. Check the defining property, not the appearance of the drawing.</p></div>
<div class="card"><h3>Guided practice · order the steps</h3><p>Put these steps for a perpendicular bisector in order: (i) keep the same radius and draw arcs from A and B; (ii) draw segment AB; (iii) draw the line through the two intersection points; (iv) open the compasses to more than half of AB. Correct order: __, __, __, __. The line is perpendicular because both intersection points are the same distance from __ and from __.</p></div>
'''))
# 15 application A1-A4
P.append(page(ex_head('Application · The roof-truss workshop','A1–A4') + '<p class="lede">A carpenter is making a triangular roof truss for a garden shelter. Use angle facts, scale and constructions to check the design before cutting timber.</p>' + ''.join(item_html(i) for i in ITEMS[16:20])))
# 16 application A5-A7
P.append(page(ex_head('Application · Collar, kite and error check','A5–A7') + ''.join(item_html(i) for i in ITEMS[20:23]) + '<div class="callout blue"><div class="label">Evaluate</div><p>Which check protects the design most: measuring one angle, checking the triangle inequality, or keeping construction arcs visible? Explain your choice.</p></div>'))
# 17 investigation 1
P.append(page(f'''
<div class="kicker">Chapter 7 · Investigation · Criterion B</div><h2>The triangle inequality</h2>
<p class="lede">Return to the prediction on page 3. Choose a longest side c and two shorter sides a and b. Set the base to c, then draw an arc of radius a from one endpoint and an arc of radius b from the other. A triangle exists exactly when the two arcs meet above the base.</p>
<table><tr><th>Sides a, b, c (c longest)</th><th>3,4,5</th><th>3,4,8</th><th>4,5,9</th><th>6,7,10</th><th>2,2,3</th></tr><tr><td>a+b</td><td>7</td><td>7</td><td>9</td><td>13</td><td>4</td></tr><tr><td>Triangle possible?</td><td></td><td></td><td></td><td></td><td></td></tr></table>
<div class="figure">{BORDERLINE}<div class="caption">Figure 7.6 · Arcs of radius 5 cm and 8 cm from the ends of a 13 cm base meet on the base, not above it.</div></div>
<ol><li>Complete the table. Explain what happens when the strips 4, 5 and 9 are joined.</li><li>Compare a+b with c for each row. Write a rule that predicts whether a triangle can be made.</li><li>Test the rule on 5,8,13; 5,8,12; and 7,7,14. Which cases are borderline?</li></ol>
'''))
# 18 investigation 2 + R1-R3
P.append(page(f'''
<div class="kicker">Chapter 7 · Investigation · Discovery and conclusion</div><h2>From arcs to a rule</h2>
<div class="callout"><div class="label">Discovery</div><p>The two shorter sides must together be <strong>strictly greater</strong> than the longest side. If a+b=c, the arcs meet on the base and the triangle has zero area. If a+b&lt;c, the arcs do not meet.</p></div>
<div class="card pale"><h3>Conclusion</h3><p>For sides a, b, c with c longest, a triangle exists if and only if a+b&gt;c. The other two inequalities then hold automatically. This is the triangle inequality.</p></div>
''' + ''.join(item_html(i) for i in ITEMS[23:26])))
# 19 reasoning R4-R7
P.append(page(ex_head('Reasoning · Explain and justify','R4–R7') + ''.join(item_html(i) for i in ITEMS[26:30])))
# 20 challenge C1-C5
P.append(page(ex_head('Challenge · Deeper thinking','C1–C5') + ''.join(item_html(i) for i in ITEMS[30:])))
# 21 criterion mini-task
P.append(page(f'''
<div class="kicker">Chapter 7 · Assessment practice</div><h2>The truss card</h2>
<p class="lede">Write a step-by-step card for a partner who must construct an isosceles truss with an 8 m base and equal rafters. The card must be usable with a ruler and compasses, not a protractor.</p>
<div class="figure">{DESIGN}</div>
<div class="grid-2"><div class="card"><h3>Criteria A and C</h3><p>Choose a whole-number rafter length that makes a triangle. Explain why it works, give the construction steps, and state how your partner can check the result without relying on appearance.</p></div><div class="card pale"><h3>Criterion D</h3><p>Evaluate the design: what happens if the rafter length is exactly 4 m? What safety margin would you recommend, and why? Use the triangle inequality and the construction evidence in your answer.</p></div></div>
<div class="callout"><div class="label">Evidence</div><p>Your card should show: a valid length (A), a clear construction and check (C), and an evaluation of the borderline case in context (D). Do not claim Criterion B unless you include an investigation.</p></div>
'''))
# 22 mixed practice route
P.append(page(f'''
<div class="kicker">Chapter 7 · Mixed practice</div><h2>Connect ideas across the chapter</h2>
<p class="lede">Do not use a calculator. Draw a sketch, mark the known angles and give a reason for each step. This route revisits items from the bank in a mixed order.</p>
<table><tr><th>Route</th><th>Items</th><th>Focus</th></tr><tr><td>Fluency</td><td>F2, F3, F4, D6</td><td>Angle facts and regular polygons</td></tr><tr><td>Visual reasoning</td><td>D1, D3, D5, A2</td><td>Diagrams, triangles and trusses</td></tr><tr><td>Construction</td><td>D7, A4, R5, R7</td><td>Equal radii and evidence</td></tr><tr><td>Inquiry and challenge</td><td>R6, C1, C4, C5</td><td>Triangle inequality and design</td></tr></table>
<div class="callout blue"><div class="label">Check your progress</div><p>Match the fact to the position: a line gives 180°, a point gives 360°, and co-interior angles are supplementary, not equal. Use the correct pair: alternate and corresponding angles are equal only when the crossed lines are parallel.</p></div>
<div class="workspace"></div>
'''))
# 23 review
P.append(page(f'''
<div class="kicker">Chapter 7 · Review</div><h2>Summary and connections</h2>
<div class="review-grid"><div class="card"><h3>Angle facts</h3><ul><li>Straight line: 180°.</li><li>Full turn: 360°.</li><li>Vertically opposite: equal.</li><li>Parallel lines: corresponding and alternate equal; co-interior supplementary.</li></ul></div><div class="card"><h3>Triangles and polygons</h3><ul><li>Triangle sum: 180°.</li><li>Exterior angle: sum of opposite interior angles.</li><li>n-gon interior sum: (n−2)×180°.</li><li>Exterior sum: 360°.</li></ul></div><div class="card"><h3>Constructions</h3><ul><li>Perpendicular bisector: equal radii greater than half the segment.</li><li>Angle bisector: equal arcs from the arms.</li><li>SSS triangle: arcs meet when the triangle inequality holds.</li></ul></div><div class="card"><h3>Inquiry</h3><ul><li>Triangle inequality: two shorter sides &gt; longest.</li><li>Equality gives a degenerate straight line.</li><li>Keep arcs visible as evidence.</li></ul></div></div>
<div class="callout"><div class="label">Connections · Drawing is not proving</div><p>A construction is an argument made with instruments. Each arc records a fixed distance from a named point, so the finished drawing already contains evidence: equal radii, equal distances, and a property that can be checked. A picture that looks right is not enough; the defining relationship must hold.</p></div>
<p class="small muted">Where this leads: Chapter 8 turns classification into a precise language. Sets describe which objects share a property, and Venn diagrams show relationships of overlap and exclusion — the same kind of structural thinking used to sort triangles and angles here. Chapter 9 then measures the shapes whose boundaries you have learned to reason about.</p>
'''))
# 24 progress
P.append(page(f'''
<div class="kicker">Chapter 7 · Check your progress</div><h2>Reflection and next step</h2>
<table><tr><th>Success criterion</th><th>My rating (1–4)</th><th>Evidence: item or task</th><th>Next step</th></tr><tr><td>I can name and classify angles.</td><td></td><td></td><td></td></tr><tr><td>I can use angle facts with reasons.</td><td></td><td></td><td></td></tr><tr><td>I can calculate triangle and polygon angles.</td><td></td><td></td><td></td></tr><tr><td>I can carry out and explain constructions.</td><td></td><td></td><td></td></tr><tr><td>I can decide whether three lengths form a triangle.</td><td></td><td></td><td></td></tr><tr><td>I can produce and evaluate a scale drawing.</td><td></td><td></td><td></td></tr></table>
<div class="callout blue"><div class="label">Reflection</div><p>Which inquiry question changed your thinking most: the factual question about angle totals, the conceptual question about why the inequality must hold, or the debatable question about when a construction is reliable enough to build from? Use one item from the bank as evidence.</p></div>
<div class="atl"><strong>ATL evidence.</strong> In order for a student to think creatively and critically, students must choose an appropriate geometric fact or construction, test a design and explain why the method is reliable. Point to the place in your work where you did this.</div>
<p class="small muted">Review the answer key only after attempting each question. A correct answer without a reason is only half an explanation.</p>
'''))
# 25-28 answers
chunks = [ITEMS[:9], ITEMS[9:18], ITEMS[18:27], ITEMS[27:]]
titles = ['Answers · Foundation and Developing','Answers · Developing and Application','Answers · Application and Reasoning','Answers · Reasoning and Challenge']
for title, chunk in zip(titles, chunks):
    P.append(page(f'<div class="kicker">Chapter 7 · Answers and reasoning</div><h2>{title}</h2>' + ''.join(ans_block(i) for i in chunk)))

html = '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>MYP1 Chapter 7 · Correction prototype</title><link rel="stylesheet" href="styles.css"></head><body>' + ''.join(P) + '</body></html>'
(OUT/'index.html').write_text(html, encoding='utf-8')
data = {'chapter':7,'title':'Lines, angles, triangles and constructions','visual_target':0.34,'items':[{'id':i[0],'tier':i[1],'prompt':i[2],'visual':bool(i[3]),'answer':i[4],'reasoning':i[5]} for i in ITEMS]}
(OUT/'exercises.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
print(f'Wrote index.html ({len(P)} pages) and exercises.json ({len(ITEMS)} items, {len(VISUAL_IDS)} visual: {", ".join(VISUAL_IDS)})')
