#!/usr/bin/env python3
"""Build the targeted Chapter 7 revision. Preserves the approved design system; expands mathematics."""
import json
from pathlib import Path
from collections import Counter, defaultdict
import diagrams as d
from exercises_data import ITEMS, table
from worked_examples import EXAMPLES

OUT=Path(__file__).resolve().parent
G=d.G; GOLD=d.GOLD; RUST=d.RUST; INK=d.INK; MUT=d.MUT
COVER=d.svg(500,260,
    d.polygon([(60,220),(440,220),(250,40)],GOLD,'none',2.5)+
    d.line((145,140),(355,140),GOLD,2)+d.line((250,40),(250,220),GOLD,1.5,'5 5')+
    d.arc((60,220),34,-63,0,GOLD,1.5)+d.arc((440,220),34,180,243,GOLD,1.5)+
    d.dot((60,220),4,RUST)+d.dot((440,220),4,RUST)+d.dot((250,40),4,RUST)+
    d.label(250,248,'equal slopes · horizontal collar · exact template',GOLD,12),
    'Chapter 7 truss illustration')

PAGES=[]; PAGE_META=[]
def page(body,cls='',head=True,pid='',title='',kind='student',items=(),examples=()):
    h='<div class="running-head"><span>Part IV · Shape, structure and measure</span><span>Chapter 7 · Lines, angles, triangles and constructions</span></div>' if head else ''
    PAGES.append(f'<section class="page {cls}" data-page-id="{pid}">{h}{body}</section>')
    PAGE_META.append(dict(page=len(PAGES),id=pid,title=title,kind=kind,items=list(items),examples=list(examples)))

def kicker(k,h,lede=''):
    return f'<div class="kicker">{k}</div><h2>{h}</h2>'+ (f'<p class="lede">{lede}</p>' if lede else '')

def figure(vis,cap=''):
    return f'<div class="figure">{vis}'+(f'<div class="caption">{cap}</div>' if cap else '')+'</div>'

def callout(label,text,cls=''):
    return f'<div class="callout {cls}"><div class="label">{label}</div><p>{text}</p></div>'

def card(title,body,cls=''):
    return f'<div class="card {cls}"><h3>{title}</h3>{body}</div>'

def example_page(e):
    steps=''.join(f'<li>{s}</li>' for s in e['steps'])
    body=kicker(f'Chapter {e["concept"]} · Worked example {e["id"]}',e['title'])
    body+=f'<div class="example visual-example"><div class="example-title">Problem</div><p>{e["problem"]}</p>'
    body+=f'<div class="example-title">Visual representation</div>{figure(e["visual"],e["caption"])}'
    body+=f'<div class="example-title">Mathematical reasoning</div><p>{e["reasoning"]}</p>'
    body+=f'<div class="example-title">Step-by-step solution</div><ol class="steps">{steps}</ol>'
    body+=f'<div class="answer"><strong>Final answer.</strong> {e["answer"]}</div>'
    body+=f'<p class="interpretation"><strong>Interpretation.</strong> {e["interpretation"]}</p></div>'
    page(body,pid=f'example-{e["id"]}',title=f'Worked example {e["id"]}',kind='worked-example',examples=[e['id']])

def item_html(it):
    vis=f'<div class="visual">{it["visual"]}</div>' if it['visual'] else ''
    if it['space']=='large': work='<div class="construction-space"></div>'
    elif it['space']=='box': work='<div class="workspace medium"></div>'
    else: work='<div class="workline"></div><div class="workline"></div>'
    return f'<div class="item practice-item" data-item-id="{it["id"]}"><div class="id">{it["id"]}<span class="tier">{it["thinking"]}</span></div><div><p class="prompt">{it["prompt"]}</p>{vis}{work}</div></div>'

def practice_pages():
    groups=defaultdict(list)
    for it in ITEMS: groups[(it['concept'],it['subtopic'])].append(it)
    for (concept,subtopic),items in groups.items():
        chunk=[]; weight=0
        def flush():
            nonlocal chunk,weight
            if not chunk: return
            ids=[i['id'] for i in chunk]
            head=f'<div class="exercise-head"><h3>Practice {concept} · {subtopic}</h3><span class="range">{ids[0]}–{ids[-1]}</span></div>'
            note='<p class="small muted">Show a method, a representation and a check. Where a question asks for a reason, the reason is part of the answer.</p>'
            body=kicker(f'Chapter {concept} · Practice',subtopic)+head+note+''.join(item_html(i) for i in chunk)
            page(body,pid=f'practice-{concept}-{ids[0]}',title=f'Practice {subtopic}',kind='practice',items=ids)
            chunk=[]; weight=0
        for it in items:
            w=2 if it['space']=='large' else (1.35 if it['visual'] else 1)
            limit=2 if any(i['space']=='large' for i in chunk) or it['space']=='large' else 3
            if chunk and (len(chunk)>=limit or weight+w>3.6): flush()
            chunk.append(it); weight+=w
        flush()

def answer_pages():
    chunk=[]
    def flush():
        nonlocal chunk
        if not chunk: return
        ids=[i['id'] for i in chunk]
        body=kicker('Chapter 7 · Answers and reasoning',f'Answers {ids[0]}–{ids[-1]}')
        for it in chunk:
            body+=f'<div class="answer-block" data-answer-id="{it["id"]}"><span class="id">{it["id"]}</span> <span class="sol">{it["answer"]}</span><div class="why">{it["reasoning"]}</div></div>'
        page(body,pid=f'answers-{ids[0]}',title=f'Answers {ids[0]}–{ids[-1]}',kind='answers',items=ids)
        chunk=[]
    for it in ITEMS:
        if chunk and len(chunk)>=5: flush()
        chunk.append(it)
    flush()

# ---------------- front matter ----------------
page(f'''
<div class="part">Part IV · Shape, structure and measure · MYP Year 1 · Chapter 07</div>
<div><h1>Lines, angles, triangles and constructions</h1>
<p class="standfirst">A single straight line contains 180°, and a full turn contains 360°. From those two facts, and one statement about parallel lines, an entire system of shape reasoning follows. Constructions turn that reasoning into a repeatable physical procedure.</p>
{figure(COVER)}
<div class="chips"><span class="chip">Key concept · Relationships</span><span class="chip">Related · Space</span><span class="chip">Related · Representation</span><span class="chip">Context · Orientation in space and time</span></div>
<div class="inquiry"><div class="label">Inquiry</div><p>A workshop needs a triangular roof truss with equal slopes and a horizontal collar beam. Which angles must the carpenter set, how can the shape be checked without measuring every angle, and how can a full-size template be reproduced exactly?</p></div></div>
<div class="foot"><span>MYP Mathematics 1</span><span>Student coursebook · Prototype</span></div>
''','cover',head=False,pid='cover',title='Chapter cover',kind='cover')

page(kicker('Chapter 7 · Opener','Reasoning with straight lines','Geometry begins with a few reliable facts and becomes powerful when those facts are connected. In this chapter you will name angle relationships, explain triangle and polygon sums, and use equal-radius constructions to force a property rather than guess it.')+
callout('Engagement','Before cutting timber, a carpenter can test a design with a scale drawing. Which measurements are enough to guarantee the shape? Which checks protect against a drawing that only looks correct?')+
'<h3>Inquiry questions</h3><ul><li><strong>Factual:</strong> What do angles on a straight line and around a point add to?</li><li><strong>Conceptual:</strong> Why must the two shorter sides of a triangle together exceed the longest side?</li><li><strong>Debatable:</strong> When is a construction reliable enough to build from?</li></ul>'+
'<div class="grid-2">'+card('Learning goals','<ul><li>Use angle facts on lines, at points and with parallel lines.</li><li>Reason with triangle and polygon angle sums.</li><li>Apply the triangle inequality and regular-polygon facts.</li><li>Construct perpendicular bisectors, angle bisectors and SSS triangles.</li></ul>')+
card('MYP lens','<p><strong>Key concept:</strong> Relationships</p><p><strong>Related concepts:</strong> Space, Representation</p><p><strong>Global context:</strong> Orientation in space and time</p><p><strong>Criteria:</strong> A, B, C and D in separate tasks</p>','pale')+'</div>'+
'<div class="atl"><strong>ATL focus.</strong> In order for a student to think creatively and critically, students must choose an appropriate geometric fact or construction, test a design and explain why the method is reliable.</div>'+
'<p class="small"><strong>Language bank:</strong> acute · right · obtuse · reflex · vertically opposite · corresponding · alternate · co-interior · isosceles · exterior angle · polygon · perpendicular bisector · angle bisector · construction</p>',pid='opener',title='Opener')

page(kicker('Chapter 7 · Start here','Ready check and chapter map','Use the ready check to find the ideas you already control. Then follow the map from concrete angle facts to constructions and design decisions.')+
card('Ready check','<p>Before starting, check that you can: name acute, right and obtuse angles; draw and label an angle ABC; use a ruler to draw a 6 cm segment; open compasses to a given radius. If any skill is uncertain, ask for a quick demonstration before beginning 7.1.</p>','sand')+
card('Chapter map','<ol><li><strong>7.1 Lines, angles and angle facts</strong> — name the relationship first: straight line, full turn, vertically opposite or right angle.</li><li><strong>7.2 Parallel lines and triangles</strong> — use corresponding, alternate and co-interior angles only when the lines are parallel.</li><li><strong>7.3 Polygons and the triangle inequality</strong> — split polygons into triangles; test whether three lengths can close a triangle.</li><li><strong>7.4 Ruler-and-compass constructions</strong> — use equal radii to force a property, keep arcs visible and check the defining relationship.</li></ol>')+
callout('Explain how you know','For every answer, be ready to give a method, a diagram or a reason. A correct result without a check is only half an explanation.'),pid='ready-map',title='Ready check and map')

page(kicker('Chapter 7 · How to use the practice','Six kinds of mathematical thinking','The practice is organised by concept, then by the kind of thinking it develops. The labels describe the task, not a separate mark scheme.')+
'<div class="grid-2">'+card('Understand','Identify, classify, state, complete and interpret definitions, notation and properties.')+card('Fluency','Calculate, solve, complete diagrams and use procedures accurately.')+card('Reasoning','Justify, compare methods, find errors and explain why a statement is true or false.')+card('Investigation','Observe, organise evidence, make conjectures, test them and draw conclusions.')+card('Application','Use mathematics in design, measurement and everyday contexts, then interpret the result.')+card('Challenge','Combine ideas, consider alternatives and explain deeper relationships.')+'</div>'+
callout('Working space','Use the space provided for diagrams, equations and checks. Construction tasks ask you to draw in your notebook at the stated size; printed figures are models, not always full-size templates.')+
'<div class="atl"><strong>ATL evidence.</strong> As you work, record one place where you chose a method, one place where you tested a result, and one place where you explained why the method is reliable.</div>',pid='practice-guide',title='Practice guide')

# ---------------- 7.1 ----------------
page(kicker('Chapter 7 · Mathematical development','7.1 Lines, angles and angle facts','Name the relationship first: straight line, full turn, vertically opposite or right angle.')+
'<p>An angle measures a turn. A half-turn along a straight line is 180°, so adjacent angles on a straight line are supplementary. A full turn about a point is 360°. When two straight lines cross, vertically opposite angles are equal.</p>'+
'<div class="grid-2">'+figure(d.straight_pair(65,'65°'),'Straight line: the two angles complete 180°.')+figure(d.around([90,110,75,85],['90°','110°','75°','85°']),'Full turn: the four angles complete 360°.')+'</div>'+
card('Key idea','<p>Straight line: 180°. Full turn: 360°. Vertically opposite: equal. Right angle: 90°. Complementary angles sum to 90°; supplementary angles sum to 180°. The middle letter of angle ABC names the vertex B.</p>','pale')+
callout('Common error','Do not swap the totals: a straight line is 180°, a full turn is 360°. Do not treat vertically opposite angles as supplementary; they are equal. The adjacent pair is supplementary.','rust'),pid='theory-7-1',title='7.1 explanation')
for e in EXAMPLES:
    if e['concept']=='7.1': example_page(e)
practice_pages_71=[i for i in ITEMS if i['concept']=='7.1']
# practice_pages() emits all concepts in order; call once after all theory? We need interleaving. Instead custom emit by concept.

def emit_practice(concept):
    groups=defaultdict(list)
    for it in ITEMS:
        if it['concept']==concept: groups[it['subtopic']].append(it)
    for subtopic,items in groups.items():
        chunk=[]; weight=0
        def flush():
            nonlocal chunk,weight
            if not chunk: return
            ids=[i['id'] for i in chunk]
            head=f'<div class="exercise-head"><h3>Practice {concept} · {subtopic}</h3><span class="range">{ids[0]}–{ids[-1]}</span></div>'
            note='<p class="small muted">Show a method, a representation and a check. Where a question asks for a reason, the reason is part of the answer.</p>'
            body=kicker(f'Chapter {concept} · Practice',subtopic)+head+note+''.join(item_html(i) for i in chunk)
            page(body,pid=f'practice-{concept}-{ids[0]}',title=f'Practice {subtopic}',kind='practice',items=ids)
            chunk=[]; weight=0
        for it in items:
            w=2 if it['space']=='large' else (1.35 if it['visual'] else 1)
            large=any(i['space']=='large' for i in chunk) or it['space']=='large'
            visual=any(i['visual'] for i in chunk) or it['visual']
            limit=2 if large else (3 if visual else 4)
            if chunk and (len(chunk)>=limit or weight+w>4.0): flush()
            chunk.append(it); weight+=w
        flush()
emit_practice('7.1')

# ---------------- 7.2 ----------------
page(kicker('Chapter 7 · Mathematical development','7.2 Parallel lines and transversals','A transversal crosses two or more lines. When the crossed lines are parallel, the angles fall into equal or supplementary families.')+
figure(d.numbered_parallel(),'Figure 7.4 · With l parallel to m: corresponding and alternate angles are equal; co-interior angles are supplementary.')+
card('Key idea','<p>Corresponding angles sit in the same position at each intersection. Alternate angles lie on opposite sides of the transversal between the parallel lines. Co-interior angles lie on the same side between the parallel lines.</p>','pale')+
callout('Watch for this misconception','Do not assume lines are parallel or angles equal unless marked or stated. Conversely, equal alternate angles or supplementary co-interior angles can show that two lines are parallel.','rust'),pid='theory-7-2-parallel',title='7.2 parallel explanation')
page(kicker('Chapter 7 · Mathematical development','Triangle and exterior-angle facts','Every triangle has angle sum 180°. An exterior angle equals the sum of the two opposite interior angles.')+
'<div class="grid-2">'+figure(d.triangle(70,70,40,Alab='x',Blab='x',Clab='40°',ticks={1:1,2:1}),'Equal sides give equal base angles.')+figure(d.triangle(60,70,50,Alab='60°',Clab='50°',exterior=('110°',75)),'Exterior angle = sum of opposite interior angles.')+'</div>'+
card('Key idea','<p>Triangles may be classified by sides (equilateral, isosceles, scalene) and by angles (acute, right, obtuse). In an isosceles triangle the angles opposite the equal sides are equal; conversely, equal angles face equal sides. In a right triangle the two acute angles are complementary.</p>','pale')+
callout('Common error','The exterior angle is equal to the sum of the two opposite interior angles. It is not added to them to make 180°. The adjacent interior angle is the one supplementary to the exterior angle.','rust'),pid='theory-7-2-triangles',title='7.2 triangle explanation')
for e in EXAMPLES:
    if e['concept']=='7.2': example_page(e)
emit_practice('7.2')

# ---------------- 7.3 polygons ----------------
page(kicker('Chapter 7 · Mathematical development','7.3 Polygons and their angles','A polygon is a closed plane shape made from straight sides. Its interior angle sum depends on the number of sides.')+
figure(d.regular_polygon(6,triangulate=True),'Figure 7.9 · A hexagon splits into four triangles from one vertex.')+
'<p>Choose one vertex and draw diagonals to every non-adjacent vertex. An n-sided polygon divides into n−2 triangles, so its interior angle sum is (n−2)×180°. The exterior angles of any convex polygon sum to 360°.</p>'+
card('Key idea','<p>Interior sum: (n−2)×180°. Exterior sum: 360°. Regular polygon: each exterior = 360°÷n; each interior = 180°−360°÷n.</p>','pale'),pid='theory-7-3-polygons',title='7.3 polygon explanation')
for e in EXAMPLES:
    if e['concept']=='7.3' and e['id'] in ('7.3.1','7.3.2'): example_page(e)
# polygon practice only
poly_items=[i for i in ITEMS if i['concept']=='7.3' and i['subtopic']=='Polygon angle sums']
for start in range(0,len(poly_items),2):
    chunk=poly_items[start:start+2]; ids=[i['id'] for i in chunk]
    body=kicker('Chapter 7.3 · Practice','Polygon angle sums')+f'<div class="exercise-head"><h3>Practice 7.3 · Polygons</h3><span class="range">{ids[0]}–{ids[-1]}</span></div>'+''.join(item_html(i) for i in chunk)
    page(body,pid=f'practice-7-3-poly-{ids[0]}',title='Practice polygon angle sums',kind='practice',items=ids)

# ---------------- inquiry before inequality rule ----------------
page(kicker('Chapter 7 · Inquiry launch','Which lengths close a triangle?','Three strips joined end to end may or may not close a triangle. Predict first, then test. Do not state a rule until the evidence forces it.')+
table(['Side lengths (cm)','Prediction','Arcs meet above the base?','Triangle?'],['3, 4, 5','','',''],['3, 4, 8','','',''],['4, 5, 9','','',''],['6, 7, 10','','',''],['2, 2, 3','','',''])+
callout('Observe','When the arcs meet on the base, the “triangle” has zero area. When they do not meet, there is a gap. What must be true about the two shorter lengths for a real apex to exist?','blue')+
'<div class="workspace medium"></div><p class="small muted">Keep this prediction. You will return to it after testing more cases.</p>',pid='inquiry-launch',title='Inquiry launch')
page(kicker('Chapter 7 · Investigation · Criterion B practice','Test lengths with compass arcs','Choose a longest side c and two shorter sides a and b. Set the base to c, then draw an arc of radius a from one endpoint and an arc of radius b from the other. Record what happens.')+
table(['a, b, c (cm)','a+b','Compare a+b with c','Arcs meet above base?','Triangle?'],['4, 5, 6','','','',''],['2, 3, 6','','','',''],['5, 8, 13','','','',''],['6, 8, 9','','','',''],['your own case','','','',''])+
'<ol><li>Complete the table. Include at least one borderline case of your own.</li><li>Compare a+b with c for each row. Write a conjecture that predicts whether a triangle can be made.</li><li>Test your conjecture on 5, 8, 12 and 7, 7, 14. Does it still work?</li><li>Explain why the arcs behave as they do. Use a labelled sketch.</li></ol>'+
'<div class="atl"><strong>ATL evidence.</strong> Choose your own extra case, organise the evidence, test the conjecture and explain the result.</div>',pid='inquiry-test',title='Investigation testing')
page(kicker('Chapter 7 · Investigation · Discovery','From evidence to a rule','Write your conjecture before comparing it with the formal statement below.')+
'<div class="workspace medium"></div>'+
callout('Discovery','The two shorter sides must together be <strong>strictly greater</strong> than the longest side. If a+b=c, the arcs meet on the base and the triangle has zero area. If a+b&lt;c, the arcs do not meet.')+
card('Conclusion','<p>For sides a, b, c with c longest, a triangle exists if and only if a+b&gt;c. The other two inequalities then hold automatically. This is the triangle inequality.</p>','pale')+
figure(d.sss(5,8,13,complete=True),'Figure 7.12 · Equality gives a degenerate straight line.'),pid='inquiry-discovery',title='Inquiry discovery')
example_page(next(e for e in EXAMPLES if e['id']=='7.3.3'))
ineq_items=[i for i in ITEMS if i['concept']=='7.3' and i['subtopic']=='Triangle inequality']
for start in range(0,len(ineq_items),3):
    chunk=ineq_items[start:start+3]; ids=[i['id'] for i in chunk]
    body=kicker('Chapter 7.3 · Practice','Triangle inequality')+f'<div class="exercise-head"><h3>Practice 7.3 · Possible triangles</h3><span class="range">{ids[0]}–{ids[-1]}</span></div>'+''.join(item_html(i) for i in chunk)
    page(body,pid=f'practice-7-3-ineq-{ids[0]}',title='Practice triangle inequality',kind='practice',items=ids)

# ---------------- 7.4 ----------------
page(kicker('Chapter 7 · Mathematical development','7.4 Constructions with ruler and compass','A construction is an argument made with instruments. Each arc records a fixed distance from a named point.')+
'<div class="grid-2">'+figure(d.perp_bisector(8,5),'Perpendicular bisector: equidistant from two endpoints.')+figure(d.angle_bisector(64),'Angle bisector: equidistant from the two arms.')+'</div>'+
table(['Construction','Compass setting','How to test'],['Perpendicular bisector of AB','One radius greater than half AB, unchanged from A and B','Crosses AB at its midpoint and makes 90°'],['Angle bisector','Arc from vertex cuts both arms; same radius from those points','Two half-angles are equal'],['Triangle from three sides','Base equal to one side; radii equal to the other two sides','Arcs meet; two shorter sides exceed the longest'])+
callout('Common error','Never change the compass between a pair of arcs. Check the defining property, not the appearance of the drawing.','rust'),pid='theory-7-4-bisectors',title='7.4 bisectors explanation')
page(kicker('Chapter 7 · Mathematical development','Constructing triangles from sides','To construct a triangle from three sides, fix the base and locate the apex with two arcs.')+
figure(d.sss(6,5,7,complete=True),'Figure 7.14 · The arc intersection fixes the third vertex.')+
'<p>The triangle inequality predicts whether the arcs meet above the base. If the two shorter sides together equal the longest side, the apex lies on the base; if they are shorter, the arcs do not meet.</p>'+
card('Key idea','<p>SSS construction: base AB, arc from A with radius AC, arc from B with radius BC. The intersection is C. Keep the arcs visible as evidence.</p>','pale'),pid='theory-7-4-sss',title='7.4 SSS explanation')
for e in EXAMPLES:
    if e['concept']=='7.4': example_page(e)
emit_practice('7.4')

# ---------------- mixed retrieval ----------------
page(kicker('Chapter 7 · Mixed practice','Connect ideas across the chapter','This route revisits items from the bank in a mixed order. Do not use a calculator. Draw a sketch, mark known facts and give a reason for each step.')+
table(['Route','Items','Focus'],['Fluency','7.1.04, 7.1.05, 7.2.08, 7.3.06','Angle facts and regular polygons'],['Visual reasoning','7.2.03, 7.2.15, 7.3.05, 7.2.10','Diagrams, triangles and trusses'],['Construction','7.4.03, 7.4.06, 7.4.07, 7.4.08','Equal radii and evidence'],['Inquiry and challenge','7.3.13, 7.3.14, 7.3.15, 7.3.16','Triangle inequality and design'])+
callout('Check your progress','Match the fact to the position: a line gives 180°, a point gives 360°, and co-interior angles are supplementary, not equal. Use the correct pair: alternate and corresponding angles are equal only when the crossed lines are parallel.','blue')+
'<div class="workspace medium"></div>',pid='mixed-practice',title='Mixed practice route')

# ---------------- assessment ----------------
page(kicker('Chapter 7 · Assessment · Criterion A','Knowing and understanding','Select appropriate mathematics, apply it successfully and solve problems in familiar and unfamiliar situations. Show your method and a check.')+
'<div class="assessment-task"><h3>A1 · The badge design</h3><p>A badge is made from a triangle with one side extended. The exterior angle is 3x + 18°, and the two opposite interior angles are 2x + 8° and 52°. Find x, all three interior angles, and classify the triangle.</p>'+figure(d.triangle(92,36,52,Alab='2x+8°',Clab='52°',exterior=('3x+18°',75)),'Assessment figure A1')+'</div>'+
'<div class="assessment-task"><h3>A2 · Parallel supports</h3><p>Two parallel supports are crossed by a brace. Alternate angles are labelled 4x − 10° and 2x + 30°. Find x and the co-interior partner of one marked angle.</p>'+figure(d.parallel_map([None,None,None,'4x−10°'],['2x+30°',None,None,None],acute=70),'Assessment figure A2')+'</div>',pid='assessment-a-1',title='Criterion A task 1',kind='assessment')
page(kicker('Chapter 7 · Assessment · Criterion A','Knowing and understanding · continued')+
'<div class="assessment-task"><h3>A3 · A tile and a frame</h3><p>A regular tile has interior angle 150°. Identify the polygon. A triangular frame has two sides 5 cm and 9 cm. Find all whole-centimetre lengths for the third side. Explain why the endpoints are excluded.</p>'+figure(d.regular_polygon(12),'Assessment figure A3')+'</div>'+
'<div class="workspace large"></div>'+
'<p class="small muted">Criterion A evidence: your choice of method, successful application and correct solutions. Do not just state answers; show the mathematics that supports them.</p>',pid='assessment-a-2',title='Criterion A task 2',kind='assessment')

page(kicker('Chapter 7 · Assessment · Criterion B','Investigating patterns','Work independently. Choose your own method and representation. Your task is to discover a relationship, describe it as a general rule, and verify it on new examples.')+
'<div class="assessment-task"><h3>B1 · Triangles from an interior point</h3><p>Choose a convex polygon. Mark a point O inside it and join O to every vertex. Investigate how the number of sides affects the interior angle sum.</p>'+figure(d.regular_polygon(5,interior_point=True),'One possible starting diagram')+'</div>'+
'<ol><li>Investigate at least a triangle, quadrilateral, pentagon and hexagon. Organise your findings in a way of your choice.</li><li>Describe a general rule for an n-sided polygon using this interior-point method.</li><li>Verify your rule for an octagon using a different method.</li><li>Explain why the angles around O must be subtracted. What changes if O lies on a side instead of inside?</li></ol>'+
'<div class="atl"><strong>ATL evidence.</strong> Choose a technique, look for a pattern, generalise, verify and explain.</div>',pid='assessment-b-1',title='Criterion B task',kind='assessment')
page(kicker('Chapter 7 · Assessment · Criterion B','Workspace for investigation')+
'<div class="workspace large"></div><div class="workspace large"></div>'+
'<p class="small muted">Criterion B evidence: organised cases, a rule consistent with your findings, verification on a new example, and an explanation. A table is optional; choose a representation that makes the pattern visible.</p>',pid='assessment-b-2',title='Criterion B workspace',kind='assessment')

page(kicker('Chapter 7 · Assessment · Criterion C','Communicating','Write for a partner who knows angle facts but has not seen this argument. Use mathematical language, a labelled diagram and a logical sequence.')+
'<div class="assessment-task"><h3>C1 · Explain the triangle angle sum</h3><p>Use the diagram to explain why the angles of any triangle sum to 180°. Your explanation must include the parallel line, alternate angles and the straight line through the apex.</p>'+figure(d.triangle_sum_model(55,65),'Assessment figure C1')+'</div>'+
'<div class="assessment-task"><h3>C2 · Improve a flawed explanation</h3><p>A student writes: “The angles are 55°, 65° and 60°, so they add to 180°. Therefore every triangle adds to 180°.” Explain why this is not a general argument, then rewrite it using the parallel-line model.</p></div>'+
'<p class="small muted">A strong response uses correct notation, names the relationships, and moves logically from the diagram to the conclusion.</p>',pid='assessment-c-1',title='Criterion C task',kind='assessment')
page(kicker('Chapter 7 · Assessment · Criterion C','Workspace for communication')+
'<div class="workspace large"></div><div class="workspace medium"></div>'+
'<div class="card"><h3>Self-check before submitting</h3><ul><li>Have I used terms such as alternate, parallel and supplementary correctly?</li><li>Does my diagram support each step?</li><li>Could a partner follow the reasoning without seeing my working?</li></ul></div>',pid='assessment-c-2',title='Criterion C workspace',kind='assessment')

page(kicker('Chapter 7 · Assessment · Criterion D','Applying mathematics in real-life contexts','Design brief: a simplified shade-canopy frame for a school courtyard. The dimensions below are illustrative, not construction specifications.')+
'<div class="assessment-task"><h3>D1 · Check and draw the canopy frame</h3><p>The frame is an isosceles triangle with base 2.4 m and equal rafters 1.5 m. A scale drawing uses 1 : 20.</p>'+figure(d.truss(base=2.4,rafter=1.5,apex_label='shade-canopy model'),'Assessment figure D1 · simplified geometry only')+'</div>'+
'<ol><li>Identify the relevant mathematical elements of the brief.</li><li>Select and apply strategies to check whether the triangle is possible and to find the scale-drawing lengths.</li><li>Construct the scale triangle with ruler and compasses. Measure the apex angle to the nearest degree and check the angle sum.</li><li>Explain the degree of accuracy of your drawing and measurements.</li><li>Describe whether the solution makes sense in context, and state one limitation of the model.</li></ol>',pid='assessment-d-1',title='Criterion D task',kind='assessment')
page(kicker('Chapter 7 · Assessment · Criterion D','Workspace for application and interpretation')+
'<div class="workspace large"></div>'+
'<div class="card"><h3>Context check</h3><p>This task assesses geometry, scale and interpretation. It does not certify a real structure. Real canopies also need material thickness, joints, loads, wind and safety checks.</p></div>'+
'<p class="small muted">Criterion D evidence: relevant elements, appropriate strategies, a successful solution, accuracy, and interpretation in context.</p>',pid='assessment-d-2',title='Criterion D workspace',kind='assessment')

# ---------------- review ----------------
page(kicker('Chapter 7 · Review','Summary and connections')+
'<div class="review-grid">'+card('Angle facts','<ul><li>Straight line: 180°.</li><li>Full turn: 360°.</li><li>Vertically opposite: equal.</li><li>Parallel lines: corresponding and alternate equal; co-interior supplementary.</li></ul>')+card('Triangles and polygons','<ul><li>Triangle sum: 180°.</li><li>Exterior angle: sum of opposite interior angles.</li><li>n-gon interior sum: (n−2)×180°.</li><li>Exterior sum: 360°.</li></ul>')+card('Constructions','<ul><li>Perpendicular bisector: equal radii greater than half the segment.</li><li>Angle bisector: equal arcs from the arms.</li><li>SSS triangle: arcs meet when the triangle inequality holds.</li></ul>')+card('Inquiry','<ul><li>Triangle inequality: two shorter sides &gt; longest.</li><li>Equality gives a degenerate straight line.</li><li>Keep arcs visible as evidence.</li></ul>')+'</div>'+
callout('Connections · Drawing is not proving','A construction is an argument made with instruments. Each arc records a fixed distance from a named point, so the finished drawing already contains evidence: equal radii, equal distances, and a property that can be checked. A picture that looks right is not enough; the defining relationship must hold.')+
'<p class="small muted">Where this leads: Chapter 8 turns classification into a precise language. Sets describe which objects share a property, and Venn diagrams show relationships of overlap and exclusion. Chapter 9 then measures the shapes whose boundaries you have learned to reason about.</p>',pid='review',title='Review')
page(kicker('Chapter 7 · Check your progress','Reflection and next step')+
table(['Success criterion','My rating (1–4)','Evidence: item or task','Next step'],['I can name and classify angles.','','',''],['I can use angle facts with reasons.','','',''],['I can calculate triangle and polygon angles.','','',''],['I can carry out and explain constructions.','','',''],['I can decide whether three lengths form a triangle.','','',''],['I can produce and evaluate a scale drawing.','','',''])+
callout('Reflection','Which inquiry question changed your thinking most: the factual question about angle totals, the conceptual question about why the inequality must hold, or the debatable question about when a construction is reliable enough to build from? Use one item from the bank as evidence.','blue')+
'<div class="atl"><strong>ATL evidence.</strong> In order for a student to think creatively and critically, students must choose an appropriate geometric fact or construction, test a design and explain why the method is reliable. Point to the place in your work where you did this.</div>'+
'<p class="small muted">Review the answer key only after attempting each question. A correct answer without a reason is only half an explanation.</p>',pid='progress',title='Progress and reflection')

# ---------------- answers ----------------
answer_pages()
page(kicker('Chapter 7 · Assessment guidance','Sample responses · Criteria A and B')+
'<div class="answer-block"><span class="id">A1</span> <span class="sol">x = 42°; interior angles 92°, 36°, 52°; obtuse scalene.</span><div class="why">3x+18 = (2x+8)+52 gives x=42. The adjacent interior angle is 180−144=36°.</div></div>'+
'<div class="answer-block"><span class="id">A2</span> <span class="sol">x = 20°; marked angles 70°; co-interior partner 110°.</span><div class="why">4x−10 = 2x+30 gives x=20.</div></div>'+
'<div class="answer-block"><span class="id">A3</span> <span class="sol">Regular dodecagon; third side 5–13 cm.</span><div class="why">Exterior angle 30°, so n=12. For sides 5 and 9, 4&lt;x&lt;14; endpoints give degenerate cases.</div></div>'+
'<div class="answer-block"><span class="id">B1</span> <span class="sol">Interior-point method: n triangles, total 180n°, subtract the 360° around O, giving 180n−360 = (n−2)180°.</span><div class="why">For an octagon this gives 1080°, matching (8−2)×180°. If O lies on a side, the angles around O on the interior side sum to 180°, and the count of triangles changes; the same interior sum must still result.</div></div>'+
'<p class="small muted">These are sample responses, not the only acceptable methods. Criterion B credit depends on the student’s own investigation, generalisation and verification.</p>',pid='assessment-answers-1',title='Assessment guidance A/B',kind='answers')
page(kicker('Chapter 7 · Assessment guidance','Sample responses · Criteria C and D')+
'<div class="answer-block"><span class="id">C1–C2</span> <span class="sol">A general argument uses the parallel line through the apex.</span><div class="why">Alternate angles transfer the two base angles to the apex. The three angles on the straight line through the apex sum to 180°, so the triangle angles sum to 180°. One numeric example alone is not a general argument.</div></div>'+
'<div class="answer-block"><span class="id">D1</span> <span class="sol">Possible: 1.5+1.5&gt;2.4. Scale lengths: base 12 cm, rafters 7.5 cm.</span><div class="why">2.4 m=240 cm; 240÷20=12 cm. 1.5 m=150 cm; 150÷20=7.5 cm. A measured apex is about 106° and base angles about 37°; accept small measurement variation. Accuracy: nearest millimetre in the model corresponds to 2 cm in reality; angles to nearest degree. Limitations include thickness, joints, loads and wind.</div></div>'+
'<p class="small muted">Criterion C values clear language, representations and logical organisation. Criterion D values context, strategy, accuracy and interpretation, not just a correct calculation.</p>',pid='assessment-answers-2',title='Assessment guidance C/D',kind='answers')

html='<!doctype html><html lang="en"><head><meta charset="utf-8"><title>MYP1 Chapter 7 · Targeted revision prototype</title><link rel="stylesheet" href="styles.css"></head><body>'+''.join(PAGES)+'</body></html>'
(OUT/'index.html').write_text(html,encoding='utf-8')
visual=[i['id'] for i in ITEMS if i['visual']]
data={'chapter':7,'title':'Lines, angles, triangles and constructions','revision':'targeted-mathematical-depth','core_items':len(ITEMS),'visual_items':visual,'visual_fraction':len(visual)/len(ITEMS),'worked_examples':len(EXAMPLES),'items':[{k:v for k,v in i.items() if k!='visual'}|{'visual':bool(i['visual'])} for i in ITEMS]}
(OUT/'exercises.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
(OUT/'worked-examples.json').write_text(json.dumps([{k:v for k,v in e.items() if k!='visual'}|{'visual':True} for e in EXAMPLES],indent=2),encoding='utf-8')
(OUT/'manifest.json').write_text(json.dumps(PAGE_META,indent=2),encoding='utf-8')
coverage=[]
for c in ['7.1','7.2','7.3','7.4']:
    its=[i for i in ITEMS if i['concept']==c]; ex=[e for e in EXAMPLES if e['concept']==c]
    coverage.append(dict(concept=c,items=len(its),visual=sum(bool(i['visual']) for i in its),examples=len(ex),thinking=dict(Counter(i['thinking'] for i in its)),subtopics=dict(Counter(i['subtopic'] for i in its)),pages=[p['page'] for p in PAGE_META if p['kind']=='practice' and any(i.startswith(c) for i in p['items'])]))
(OUT/'coverage.json').write_text(json.dumps(coverage,indent=2),encoding='utf-8')
print(f'Wrote {len(PAGES)} pages; {len(ITEMS)} core items; {len(visual)} visual ({len(visual)/len(ITEMS):.1%}); {len(EXAMPLES)} visual worked examples')
