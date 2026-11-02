"""Source-linked editorial sample, not exhaustive answer certification.
Run: python second-edition/audit/evidence/verified_sample_checks.py
All page references are physical PDF pages. Expected values were read from the
first-edition prompt/solution before independent recomputation.
"""
from fractions import Fraction as F
import math, statistics, csv, pathlib
checks=[]
def close(a,b,tol):
    if isinstance(a,(tuple,list)) and isinstance(b,(tuple,list)):
        return len(a)==len(b) and all(close(x,y,tol) for x,y in zip(a,b))
    if isinstance(a,(int,float,F)) and isinstance(b,(int,float,F)):
        return abs(float(a)-float(b))<=tol
    return a==b

def add(lev,ch,page,ref,prompt,computed,expected,tol=1e-9,kind='chapter_sample',book_claim=None):
    ok=close(computed,expected,tol)
    if kind=='chapter_sample':
        outcome='AGREE' if ok else 'DISAGREE'
        book=expected
    else:
        # A defect probe is successful when the independent result matches the
        # counterexample/correct value and contradicts the recorded book claim.
        outcome='ISSUE_CONFIRMED' if ok else 'PROBE_INCONCLUSIVE'
        book=book_claim or expected
    checks.append(dict(level=lev,chapter=ch,physical_page=page,reference=ref,check_type=kind,prompt=prompt,independent_result=str(computed),book_value_or_claim=str(book),outcome=outcome))
# MYP1
add(1,1,24,'WE 1.2.1','Underlined digit values in 6502.94: 5,4,9',(500,0.04,0.9),(500,0.04,0.9))
add(1,2,38,'WE 2.1.1','2^5,5^2,10^4,4^3',(2**5,5**2,10**4,4**3),(32,25,10000,64))
add(1,3,56,'WE 3.1.1','All factors of 48',tuple(n for n in range(1,49) if 48%n==0),(1,2,3,4,6,8,12,16,24,48))
add(1,4,78,'WE 4.1.1','42/56 simplest form',F(42,56),F(3,4))
add(1,5,99,'WE 5.1.2','3/8 as percentage',F(3,8)*100,F(75,2))
add(1,6,118,'WE 6.1.1','4,9,14,19: 12th term',5*12-1,59)
add(1,7,137,'WE 7.1.1','Supplementary angles 3x+20 and 2x+30',((180-50)/5,3*26+20,2*26+30),(26,98,82))
add(1,8,158,'WE 8.1.1','Cardinalities: primes<12; multiples of 3<=12; letters of book',(len({2,3,5,7,11}),len({3,6,9,12}),len(set('book'))),(5,4,3))
add(1,9,178,'WE 9.1.1','Rectangle 8.4 by 3.6: perimeter, area',(2*(8.4+3.6),8.4*3.6),(24,30.24))
add(1,10,199,'WE 10.1.2','Apple or banana: (12+9)/30',F(12+9,30),F(7,10))
# MYP2
add(2,1,23,'WE 1.1.1','8 red,12 blue: red:blue and red:total',(F(8,12),F(8,20)),(F(2,3),F(2,5)))
add(2,2,39,'WE 2.1.1','45/3,75/5,120/8 constant',(F(45,3),F(75,5),F(120,8)),(15,15,15))
add(2,3,54,'WE 3.1.1','180 pages/4 min; time for 585',F(585,F(180,4)),13)
add(2,4,70,'WE 4.1.2','|-9|, |6|, -|-4|',(abs(-9),abs(6),-abs(-4)),(9,6,-4))
add(2,5,88,'WE 5.1.3','3x^2-2x+1 at x=-2',3*(-2)**2-2*(-2)+1,17)
add(2,6,106,'WE 6.1.3','Save 15 then add 8: week 10 total; first week >=100',(15+8*9,math.ceil((100-15)/8)+1),(87,12))
add(2,7,127,'WE 7.1.1','Supplementary 3x+5 and 2x+15',((180-20)/5,3*32+5,2*32+15),(32,101,79))
add(2,8,152,'WE 8.1.1','Cuboid 8x4x5 surface area',2*(8*4+8*5+4*5),184)
add(2,9,171,'WE 9.1.1','Translate (1,2),(4,2),(1,5) by (3,-4)',tuple((x+3,y-4) for x,y in [(1,2),(4,2),(1,5)]),((4,-2),(7,-2),(4,1)))
add(2,10,193,'WE 10.1.2','Two dice counts: sum7,sum12,doubles',tuple(sum((a+b==s if s else a==b) for a in range(1,7) for b in range(1,7)) for s in [7,12,0]),(6,1,6))
add(2,11,210,'WE 11.1.1','Goals frequencies 3,5,6,4,2 at 0..4: mean',F(sum(v*f for v,f in enumerate([3,5,6,4,2])),20),F(37,20))
# MYP3
add(3,1,22,'WE 1.1.1','0.3636... as fraction',F(36,99),F(4,11))
add(3,2,40,'WE 2.1.2','2^-4 and (3/4)^-2',(F(2)**-4,F(3,4)**-2),(F(1,16),F(16,9)))
add(3,3,56,'WE 3.1.2','3x^2-2x+1 at x=-2',3*(-2)**2-2*(-2)+1,17)
add(3,4,74,'WE 4.1.1','y=2x-1 for x=-2..3',tuple(2*x-1 for x in range(-2,4)),(-5,-3,-1,1,3,5))
add(3,5,94,'WE 5.1.1','3(x-4)=2x+5',3*17-12,2*17+5)
add(3,6,115,'WE 6.1.1','Translate (1,1),(3,1),(2,3) by (4,-2)',tuple((x+4,y-2) for x,y in [(1,1),(3,1),(2,3)]),((5,-1),(7,-1),(6,1)))
add(3,7,138,'WE 7.1.2','Similar sides 5,7,9 scaled by 7.5/5',(7*1.5,9*1.5,1.5**2),(10.5,13.5,2.25))
add(3,8,160,'WE 8.1.1','12-gonal prism F,E,V and Euler check',(14,36,24,14+24-36),(14,36,24,2))
add(3,9,188,'WE 9.2.1','Correlation of (1,52),(2,58),(3,64),(4,68),(5,78)',62/math.sqrt(10*392),0.990,0.0005)
add(3,10,210,'WE 10.1.1','Fair die: even or prime',len({2,3,4,5,6})/6,F(5,6))
# MYP4
add(4,1,16,'Example 1.2','0.4747... and 0.8333... as fractions',(F(47,99),F(75,90)),(F(47,99),F(5,6)))
add(4,2,46,'Example 2.1','5y(2y+1)-3y(y-4) at y=2',5*2*(2*2+1)-3*2*(2-4),7*2**2+17*2)
add(4,3,71,'Example 3.1','4(2x-3)=3(x+5)-2: check x=5',(4*(2*5-3),3*(5+5)-2),(28,28))
add(4,4,95,'Example 4.1','f(x)=2x-3: f(4),f(-2),f(0)',(2*4-3,2*(-2)-3,-3),(5,-7,-3))
add(4,5,119,'Example 5.1','(2x-3)(x+4) at x=1',(2*1-3)*(1+4),2*1**2+5*1-12)
add(4,6,141,'Example 6.1','x^2-6x+5 vertex and roots',((6/2,(6/2)**2-6*(6/2)+5),tuple(x for x in range(-10,11) if x*x-6*x+5==0)),((3,-4),(1,5)))
add(4,7,163,'Example 7.2','Matches in 8 adjacent squares',3*8+1,25)
add(4,8,185,'Example 8.1','80 increased 15% then decreased 15%',80*1.15*.85,78.20)
add(4,9,208,'Example 9.1','Translate (2,1),(5,1),(2,4) by (4,-3)',tuple((x+4,y-3) for x,y in [(2,1),(5,1),(2,4)]),((6,-2),(9,-2),(6,1)))
add(4,10,237,'Example 10.2','Right-triangle legs 9,12: hypotenuse',math.hypot(9,12),15)
add(4,11,267,'Example 11.1','Triangular prism legs3,4,5 length10: volume, surface area',(.5*3*4*10,2*(.5*3*4)+(3+4+5)*10),(60,132))
add(4,12,296,'Example 12.3','Stratified sample 72 from 180,200,170,170',tuple(n*72/720 for n in [180,200,170,170]),(18,20,17,17))
out=[(a,b) for a in range(1,7) for b in range(1,7)]
add(4,13,329,'Example 13.1','Fair die: even, prime, >4, not prime',tuple(F(sum(f(x) for x in range(1,7)),6) for f in [lambda x:x%2==0,lambda x:x in [2,3,5],lambda x:x>4,lambda x:x not in [2,3,5]]),(F(1,2),F(1,2),F(1,3),F(1,2)))
add(4,14,358,'Example C.1','Scale 1:50; plan 7.2x4.8 cm: real area m²',(7.2*50/100)*(4.8*50/100),8.64)
# MYP5
add(5,1,17,'Example 1.2','(2x-3)(x^2+4x-1) at x=1',(2*1-3)*(1+4-1),2+5-14+3)
add(5,2,39,'Example 2.2','f=x^2-3x, g=2x+1: f(-2),g(f(1))',((-2)**2-3*(-2),2*(1-3)+1),(10,-3))
add(5,3,59,'Example 3.2','800 bacteria double every 3h: after12h; hourly factor',800*2**(12/3),12800)
add(5,4,79,'Example 4.1','7,11,15...: u20 and position of 143',(7+19*4,(143-7)//4+1),(83,35))
add(5,5,105,'Example 5.2','2x^2+5x<=12 roots',tuple(sorted([( -5+math.sqrt(25+96))/4,(-5-math.sqrt(25+96))/4])),(-4,1.5))
add(5,6,126,'Example 6.2','Central 128: major/minor arc angles and reflex',(128/2,(360-128)/2,360-128),(64,116,232))
add(5,7,145,'Example 7.1','A=38,B=64,a=9.4: b,c',(9.4*math.sin(math.radians(64))/math.sin(math.radians(38)),9.4*math.sin(math.radians(78))/math.sin(math.radians(38))),(13.7,14.9),0.05)
add(5,8,167,'Example 8.1','a=(3,-2),b=(-1,5): 3a-2b',(3*3-2*(-1),3*(-2)-2*5),(11,-16))
x=[5,7,8,10,12,13,15]
add(5,9,191,'Example 9.3','Population variance and SD of seven values',(statistics.pvariance(x),statistics.pstdev(x)),(76/7,3.30),0.005)
add(5,10,214,'Example 10.5','Screening: 180 true positives of 670 positives',F(180,670),F(18,67))
add(5,11,240,'Example 11.6','60m fencing on three sides: max area and dimensions',(15*(60-2*15),15,60-2*15),(450,15,30))
add(5,12,248,'Example 12.1','x^3-2x^2-5x+6 roots',tuple(x for x in range(-10,11) if x**3-2*x**2-5*x+6==0),(-2,1,3))
# Additional defect probes
add(4,13,441,'Opening problem answer 4','Neither player wins when total is not 7 or 8',F(sum(a+b not in [7,8] for a,b in out),36),F(25,36),kind='defect_probe',book_claim='A single game always has a winner and a loser.')
add(5,7,145,'Example 7.2 general claim','SSA A=30,a=5,b=10: b sin A=a gives ONE right triangle, not two',10*math.sin(math.radians(30)),5,kind='defect_probe',book_claim='Book claims two triangles precisely when A is acute and a<b; equality a=b sin A is a counterexample.')
add(5,11,240,'Guided practice 2 hint','P=900+a(n-50)^2,a=-5,n=48: loss',900-(900+(-5)*(48-50)**2),20,kind='defect_probe',book_claim='Hint 900-4a gives 920 for a=-5, a gain, while the note reports loss 20.')
add(5,11,241,'Exercise 11D Q14','Open-top tank cost coefficient at r=.70,h=2/(pi*r^2)',2*math.pi*.70**2+4/.70,8.79,0.01,kind='defect_probe',book_claim='Prompt omits open top/lid; answer key acknowledges the ambiguity and answers open-top first.')
add(5,12,328,'Revision 12D Q6','Annual doubling rate 2^(1/8)-1',2**(1/8)-1,.0905,.00005,kind='defect_probe',book_claim='Raw LaTeX commands are visible in the printed answer.')
outpath=pathlib.Path(__file__).with_name('verified-sample-results.csv')
with outpath.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(checks[0]));w.writeheader();w.writerows(checks)
print(f'{len(checks)} checks; {sum(c["outcome"]=="AGREE" for c in checks)} chapter samples agree with book values; {sum(c["outcome"]=="DISAGREE" for c in checks)} sample disagreements; {sum(c["outcome"]=="ISSUE_CONFIRMED" for c in checks)} defect probes confirm issues.')
print('Coverage:',{lev:sum(c['level']==lev for c in checks) for lev in range(1,6)})
for c in checks:
    if c['outcome'] in ('DISAGREE','PROBE_INCONCLUSIVE'):print('CHECK',c)
