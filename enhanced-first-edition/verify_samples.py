#!/usr/bin/env python3
"""Independent numerical and figure spot checks against the authored answer source."""
from fractions import Fraction as F
from itertools import product
import math
import re

from build import read_practice

books = {i: read_practice(i) for i in range(1, 6)}
checked = 0


def expect(y, section, task, part, *values):
    global checked
    text = books[y][section]['tasks'][task-1]['answers'][part-1]
    normal = re.sub(r'\s+', '', text).replace('−','-')
    for value in values:
        target = re.sub(r'\s+', '', str(value)).replace('−','-')
        if target not in normal:
            raise AssertionError(f'MYP{y}/{section}/{task}/{part}: {value!r} missing from {text!r}')
    checked += 1


# Year 1: fraction arithmetic, limit decisions, shape and plotted sample.
expect(1,'1.5',1,2,197*3+42)
expect(1,'3.5',1,2,math.lcm(42,56))
expect(1,'4.3',1,1,F(3,10)+F(1,4))
expect(1,'4.4',1,3, int((F(15,4)-5*F(3,16))/F(3,8)), (F(15,4)-5*F(3,16))%F(3,8))
expect(1,'5.3',1,3,float(((320*F(5,4)*F(9,10))/320-1)*100))
expect(1,'5.4',1,2,int(8000*F(85,100)*F(105,100)))
expect(1,'9.1',1,1,6*5-3*3)
expect(1,'9.1',1,2,sum([6,2,3,3,3,5]))
dot_payload=books[1]['10.3']['tasks'][0]['visuals'][0][1].split('|')[-1]
obs=[int(v) for v,n in (term.split(':') for term in dot_payload.split(',')) for _ in range(int(n))]
expect(1,'10.3',1,2,F(sum(obs),len(obs)))

# Year 2: compare rates with proper denominators, signed thresholds and grouped readings.
expect(2,'1.4',1,1,*(132*i//12 for i in (3,4,5)))
expect(2,'3.3',1,2,int(F(15)/F(45,60)))
expect(2,'4.4',1,2,*[f'{h%24:02}:00' for h,t in zip(range(18,26),[-3,-5,-7,-9,-8,-7,-6,-5]) if t<=-7])
expect(2,'5.4',1,2,2400//(900-600))
expect(2,'6.4',1,2,(52-3)//4,(52-3)%4)
expect(2,'7.4',1,3,2*(9+6)+2*2)
expect(2,'7.5',1,3,math.ceil(12*1.1)*2400+math.ceil(45*1.1)*1800)
expect(2,'8.4',1,3,math.ceil(1000*10/(12*10))/10)
expect(2,'10.3',1,1,float(F(12+27,40+120)))

# Year 3: exact calculation and consistency with generated comparison data.
expect(3,'1.1',1,3,F(27,99)-F(135,1000))
expect(3,'2.3',1,1,240_000 * 800 / 10**8, 240_000 * 800 * 30 / 10**9)
expect(3,'2.3',1,3,6_000_000_000//(240_000*800))
expect(3,'4.3',1,1,F(-2-7,4+2))
expect(3,'5.1',1,1,F(8+F(2,3)-F(1,2),F(1,3)+F(1,2)))
expect(3,'7.3',1,2,round(math.hypot(1.2,1.65),2))
expect(3,'7.4',2,3, math.ceil((.55/math.sin(math.radians(8)))*100)/100)
expect(3,'10.2',1,2,30)
expect(3,'10.5',1,2,F(18,18+90))
expect(3,'E.1',1,2,round(math.pi*.5**2*.8*1000))

# Year 4: solve model equations and check plotted/ungrouped statistic examples.
expect(4,'1.3',1,4,16_000_000_000//(38_000*2_600))
expect(4,'3.5',1,2,(8400*2-9600)//4,(9600-3600)//4)
expect(4,'6.4',1,3,6*(14-6))
expect(4,'7.3',1,3,*(2*n*n-n+3 for n in (6,10)))
expect(4,'8.2',1,1,round(80_000*(1.04)**3))
expect(4,'10.4',1,2,round(9/math.cos(math.radians(38))+.6,2))
classes=books[4]['12.2']['tasks'][1]['visuals'][0][1].split('|')[-1]
expect(4,'12.2',2,1,*[int((b-a)*height) for a,b,height in (map(float,s.split(',')) for s in classes.split(';'))])
expect(4,'12.5',2,1,(19+23)//2,(20+21)/2)
expect(4,'13.1',1,1,sum(a+b==5 for a,b in product(range(1,5),repeat=2)),sum(a+b>=6 for a,b in product(range(1,5),repeat=2)))
expect(4,'13.5',1,3,(500+2*200)/8)
expect(4,'C.2',1,2,int(200+40*17.5*.75),int(200+40*18.5*.75))

# Year 5: independently enumerate and evaluate numerical and graphical examples.
coef=list(map(int,books[5]['1.1']['tasks'][0]['visuals'][0][1].split('|')[-1].split(',')))
for x in range(-3,5):
    y=sum(n*x**i for i,n in enumerate(reversed(coef)))
    if y != -2*(x+1)**2*(x-3):
        raise AssertionError('MYP5/1.1 plot does not match factored cubic')
expect(5,'3.5',1,2,math.ceil(math.log(.15)/math.log(.72)))
expect(5,'4.2',1,1,sum(4*k+3 for k in range(4,16)))
expect(5,'4.4',1,2,sum(12*F(-1,3)**n for n in range(4)))
end=sum(20_000*F(105,100)**n for n in range(4))
expect(5,'4.5',1,2,round(float(end)),round(float(end*F(105,100))))
profit,x,y=max((500*x+400*y,x,y) for x,y in product(range(9),repeat=2) if 2*x+y<=9 and x+2*y<=8)
expect(5,'5.5',1,2,profit,f'({x},{y})')
angle=math.degrees(math.asin(10*math.sin(math.radians(35))/7))
expect(5,'7.1',1,2,round(angle,1),round(180-angle,1))
expect(5,'7.5',1,1,math.isqrt(9**2+12**2),math.isqrt(9**2+12**2+8**2))
expect(5,'9.2',1,2,round(math.sqrt(40),2))
flaw_posterior=F(2,5)*F(5,100)/(F(3,5)*F(2,100)+F(2,5)*F(5,100))
expect(5,'10.4',1,3,float(flaw_posterior))
expect(5,'10.5',1,3,9*8*math.comb(7,2))
expect(5,'12.2',1,2,math.isqrt(30**2+40**2-30*40+12**2))
print(f'PASS: {checked} numerical answer samples across all five volumes and plotted cubic coefficients.')
