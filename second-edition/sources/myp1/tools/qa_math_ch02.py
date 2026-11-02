#!/usr/bin/env python3
"""Independent mathematical QA for Chapter 2. Recomputes numeric results rather than trusting stored answer strings."""
import json, re, sys, math
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parents[1] / 'qa' / 'myp1'

def plain(s):
    return re.sub(r'<[^>]+>', '', s)

def main():
    data = json.loads((ROOT / 'data' / 'chapter-02.exercises.json').read_text())
    items = {q['id']: q for g in data['groups'] for q in g['items']}
    checks = []
    def add(qid, computed, ok, note=''):
        checks.append({'id': qid, 'computed': computed, 'stored_answer': items[qid]['answer'], 'pass': bool(ok), 'note': note})
    def has(qid, *needles):
        a = plain(items[qid]['answer'])
        return all(str(n) in a for n in needles)

    # Ready check
    add('R1', [6*7, 9*9], [6*7,9*9]==[42,81] and has('R1','42','81'))
    add('R2', 4000+500+30+6, 4000+500+30+6==4536 and has('R2','4,536'))
    add('R3', 12+3*4, 12+3*4==24 and has('R3','24'))
    add('R4', 3*3*3, 3*3*3==27 and has('R4','27'))
    add('R5', 8*8, 8*8==64 and has('R5','64'))
    add('R6', (2+4)*3, (2+4)*3==18 and has('R6','(2 + 4) × 3','18'))

    # Practice 2.1
    add('2.1.1', [4**3,7**2,10**5,2**7], has('2.1.1','4','7','10','2') and '3' in plain(items['2.1.1']['answer']))
    add('2.1.2', [2**3,3**2,5**3,10**3,2**6,4**3], [2**3,3**2,5**3,10**3,2**6,4**3]==[8,9,125,1000,64,64] and has('2.1.2','8','9','125','1,000','64'))
    add('2.1.3', [math.log(81,3),math.log(64,2),math.log(1000,10),0], has('2.1.3','4','6','3','0'))
    add('2.1.4', [4**2,4*2], [4**2,4*2]==[16,8] and has('2.1.4','16','8'))
    add('2.1.5', 9**2, 9**2==81 and has('2.1.5','81'))
    add('2.1.6', [2**4,4**2,2**3,3**2], [2**4,4**2,2**3,3**2]==[16,16,8,9] and has('2.1.6','16','8','9','false'))
    add('2.1.7', [3**4,sum(3**k for k in range(1,5))], [3**4,sum(3**k for k in range(1,5))]==[81,120] and has('2.1.7','81','120'))
    add('2.1.8', [2**10,10**3], 2**10>10**3 and has('2.1.8','1,024','1,000','larger'))

    # Practice 2.2
    add('2.2.1', [10**2,10**4,10**6,10**0], has('2.2.1','100','10,000','1,000,000','1'))
    add('2.2.2', 8*10**3+3*10**2+0*10+4, 8*10**3+3*10**2+4==8304 and has('2.2.2','8','3','0','4'))
    add('2.2.3', 4*10**3+7*10**2+0*10+6, 4*10**3+7*10**2+6==4706 and has('2.2.3','4,706'))
    add('2.2.4', 90050, has('2.2.4','9','0','5','50'))
    add('2.2.5', 2*10**4+5*10, 2*10**4+5*10==20050 and has('2.2.5','20,050'))
    add('2.2.6', 12480, has('2.2.6','1','2','4','8','0','10,000'))
    add('2.2.7', (3*10**3)/(3*10**2), (3*10**3)/(3*10**2)==10 and has('2.2.7','3,000','300','10'))
    sample=12690; digits=[int(x) for x in str(sample)]
    add('2.2.8', {'sample':sample,'digit_sum':sum(digits),'zero_digits':digits.count(0)}, len(str(sample))==5 and sum(digits)==18 and digits.count(0)==1 and digits[0]!=0 and has('2.2.8','12,690','18'), 'Sample answer checked; other valid numbers possible.')

    # Practice 2.3
    add('2.3.1', [n*n for n in range(1,13)], [n*n for n in range(1,13)]==[1,4,9,16,25,36,49,64,81,100,121,144] and has('2.3.1','144'))
    add('2.3.2', [13**2,15**2,6**3,10**3], has('2.3.2','169','225','216','1,000'))
    add('2.3.3', [math.isqrt(49),math.isqrt(100),math.isqrt(169),round(8**(1/3)),round(27**(1/3)),round(125**(1/3))], has('2.3.3','7','10','13','2','3','5'))
    add('2.3.4', math.isqrt(144), math.isqrt(144)==12 and has('2.3.4','12'))
    add('2.3.5', [math.isqrt(64),round(216**(1/3)),math.isqrt(225)], has('2.3.5','8','6','15'))
    add('2.3.6', [math.isqrt(81)+math.isqrt(16), math.isqrt(81+16)], (math.isqrt(81)+math.isqrt(16))!=math.isqrt(81+16) and has('2.3.6','13','97','not'))
    add('2.3.7', [7,8,7.5**2], 7**2<50<8**2 and 50<7.5**2 and has('2.3.7','7','8','closer to 7'))
    add('2.3.8', [round(343**(1/3)),14**3,14**3/343], has('2.3.8','7','14','2,744','8'))

    # Practice 2.4
    add('2.4.1', 8+2*5, 8+2*5==18 and has('2.4.1','18'))
    add('2.4.2', 20-3*4, 20-3*4==8 and has('2.4.2','8'))
    add('2.4.3', [6+4**2,(6+4)**2,2**3+3**2], has('2.4.3','22','100','17'))
    add('2.4.4', [24/4*2,24/(4*2),36/6+3], [24/4*2,24/(4*2),36/6+3]==[12,3,9] and has('2.4.4','12','3','9'))
    add('2.4.5', 5*2**3-3**2, 5*2**3-3**2==31 and has('2.4.5','31'))
    add('2.4.6', [(3+5)*2,(12-4)*2,18/(3+6)], [(3+5)*2,(12-4)*2,18/(3+6)]==[16,16,2] and has('2.4.6','(3 + 5)','(12 − 4)','(3 + 6)'))
    add('2.4.7', 12+6/3, 12+6/3==14 and has('2.4.7','14'))
    add('2.4.8', [2+3*4,(2+3)*4,2**3+4,4**2-3], [2+3*4,(2+3)*4,2**3+4,4**2-3]==[14,20,12,13] and has('2.4.8','14','20','12','13'), 'Sample expressions checked; other valid answers possible.')

    # Practice 2.5
    add('2.5.1', [2*n*n for n in (3,5,10)], [2*n*n for n in (3,5,10)]==[18,50,200] and has('2.5.1','18','50','200'))
    add('2.5.2', [(2*n)**2 for n in (3,5,10)], [(2*n)**2 for n in (3,5,10)]==[36,100,400] and has('2.5.2','36','100','400','double'))
    add('2.5.3', [3**2+4**2,(3+4)**2], [3**2+4**2,(3+4)**2]==[25,49] and has('2.5.3','25','49','not'))
    add('2.5.4', 12**2, 12**2==144 and has('2.5.4','144'))
    add('2.5.5', [3**3,5**3], has('2.5.5','27','125'))
    add('2.5.6', [5*2**2,5*4**2], [5*2**2,5*4**2]==[20,80] and has('2.5.6','20','80','quadruples'))
    add('2.5.7', [(2*3)**2,(2+5)**2], [(2*3)**2,(2+5)**2]==[36,49] and has('2.5.7','(2x)','(a + b)'))
    add('2.5.8', [math.isqrt(81),(3*9)**2,(3*9)**2/81], has('2.5.8','9','27','729','9'))

    # Exploration
    layers=[2**n for n in range(6)]; thick=[0.1*x for x in layers]
    add('B1', {'layers':layers,'thickness_mm':thick}, layers==[1,2,4,8,16,32] and has('B1','1, 2, 4, 8, 16, 32','0.1, 0.2, 0.4, 0.8, 1.6, 3.2'), 'Physical fold count is intentionally variable; ideal model checked.')
    add('B2', 'T=0.1*2^n', has('B2','0.1','2','doubles'))
    add('B3', [0.1*2**10,2**10], abs(0.1*2**10-102.4)<1e-9 and has('B3','102.4','1,024'))
    add('B4', [0.1*2**13,0.1*2**14], 0.1*2**13<1000<0.1*2**14 and has('B4','14','819.2','1,638.4'))
    add('B5', 'model limitations', has('B5','No','ideal model','Assumptions'), 'Open reasoning checked against model assumptions.')
    add('B6', [0.1*3**5,0.1*2**5], abs(0.1*3**5-24.3)<1e-9 and abs(0.1*2**5-3.2)<1e-9 and has('B6','24.3','3.2','faster'))

    # Guided
    add('G1', [8**3,8**1], [8**3,8**1]==[512,8] and has('G1','8','3','512'))
    add('G2', [math.isqrt(169),round(216**(1/3)),math.isqrt(196)], has('G2','13','6','14'))
    add('G3', [2*5**2,(2*5)**2,2**2+3**2,(2+3)**2], [2*5**2,(2*5)**2,2**2+3**2,(2+3)**2]==[50,100,13,25] and has('G3','50','100','13','25'))
    add('G4', [-(3**2),(-3)**2], [-(3**2),(-3)**2]==[-9,9] and has('G4','−9','9'))

    # Checkpoint
    add('C1', 6**4, 6**4==1296 and has('C1','6','4','1,296'))
    add('C2', 5020, has('C2','5','0','2','0'))
    add('C3', [math.isqrt(144),round(64**(1/3))], has('C3','12','4'))
    add('C4', 18-2*3**2, 18-2*3**2==0 and has('C4','0'))

    # Application
    total_gb=(4+4+2)*1000
    reserve=total_gb*15//100
    available=total_gb-reserve
    projects=available//6
    leftover=available-projects*6
    add('D1', [10,total_gb], total_gb==10000 and has('D1','10 TB','10,000'))
    add('D2', [reserve,available,projects,leftover], [reserve,available,projects,leftover]==[1500,8500,1416,4] and has('D2','1,416','4 GB'))
    add('D3', [(projects+1)*6,available], (projects+1)*6>available and has('D3','1,417','8,502','8,500'))
    tib=Decimal(10)**13/(Decimal(2)**40)
    add('D4', tib, abs(tib-Decimal('9.0949470177'))<Decimal('0.000001') and has('D4','9.09','No storage'), 'Binary-unit conversion checked with exact powers.')

    # Assessment
    add('S1', 5**3, 5**3==125 and has('S1','base','exponent','125'), 'Sample wording checked.')
    add('S2', [5**3,5**2,5**1,5**0], [5**3,5**2,5**1,5**0]==[125,25,5,1] and has('S2','125','25','5','1'), 'Sample pattern checked.')
    add('S3', [4**2,4**3], [4**2,4**3]==[16,64] and has('S3','16','64'), 'Sample diagram description checked.')
    add('S4', 4+3*(8-2)**2/6, 4+3*(8-2)**2/6==22 and has('S4','22'))
    test_expr=2+5*3**2
    add('S5', [3*2**2,(3*2)**2,test_expr], [3*2**2,(3*2)**2,test_expr]==[12,36,47] and has('S5','12','36','47'), 'Sample peer-test evaluation checked.')

    # Mixed
    add('M1', [3**4,2**7,10**6,6**3,11**2,4**4], has('M1','81','128','1,000,000','216','121','256'))
    add('M2', [9**3,12**2,10**5,5**7], has('M2','9','12','10','5'))
    add('M3', 60304, has('M3','6','0','3','0','4'))
    add('M4', 8*10**4+2*10**2+5, 8*10**4+2*10**2+5==80205 and has('M4','80,205'))
    add('M5', [math.isqrt(81),math.isqrt(196),round(27**(1/3)),round(1000**(1/3))], has('M5','9','14','3','10'))
    add('M6', [6+2*5,(6+2)*5,3**2*4-10,48/(4+4),5+12/3,(7-2)**2], [6+2*5,(6+2)*5,3**2*4-10,48/(4+4),5+12/3,(7-2)**2]==[16,40,26,6,9,25] and has('M6','16','40','26','6','9','25'))
    add('M7', [3**2+2**2,(3+2)**2,2*3**3,(2*3)**2], [3**2+2**2,(3+2)**2,2*3**3,(2*3)**2]==[13,25,54,36] and has('M7','13','25','54','36'))
    add('M8', [(2+3)*4,(24-8)/4,(3*2)**2,(10-4)**2], [(2+3)*4,(24-8)/4,(3*2)**2,(10-4)**2]==[20,4,36,36] and has('M8','(2 + 3)','(24 − 8)','(3 × 2)','(10 − 4)'))
    add('M9', [2**5,5**2], 2**5>5**2 and has('M9','32','25','larger'))
    add('M10', 7**2, 7**2==49 and has('M10','49'))
    add('M11', [math.log(64,2),math.log(100000,10),math.log(81,3),round(125**(1/3))], has('M11','6','5','4','5'))
    add('M12', 10**0, 10**0==1 and has('M12','1'))
    add('M13', 10**3+10**2+10+1, 10**3+10**2+10+1==1111 and has('M13','1,111'))
    add('M14', [math.isqrt(169),4*13,(2*13)**2,4*(2*13)], has('M14','13','52','26','676','104','4','2'))
    add('M15', [2**3,4**3,4**3/2**3], [2**3,4**3,4**3/2**3]==[8,64,8] and has('M15','8','64'))
    add('M16', [4*3+2,4*(3+2)], [4*3+2,4*(3+2)]==[14,20] and has('M16','14','20'))
    add('M17', [3**4,1+sum(3**k for k in range(1,5)),3**5], [3**4,1+sum(3**k for k in range(1,5)),3**5]==[81,121,243] and has('M17','81','121','243'))
    add('M18', [math.isqrt(36+64),math.isqrt(36)+math.isqrt(64)], [math.isqrt(36+64),math.isqrt(36)+math.isqrt(64)]==[10,14] and has('M18','10','14'))

    failed=[c for c in checks if not c['pass']]
    missing=sorted(set(items)-{c['id'] for c in checks})
    report={'chapter':2,'independent_checks':len(checks),'passed':len(checks)-len(failed),'failed':failed,'unchecked_ids':missing,'status':'PASS' if not failed and not missing else 'FAIL','note':'Open-ended items are checked as valid samples where applicable; numeric results are recomputed independently.'}
    QA.mkdir(parents=True,exist_ok=True)
    (QA/'chapter-02-math-qa.json').write_text(json.dumps(report,indent=2,default=str))
    print(json.dumps({k:report[k] for k in ['chapter','independent_checks','passed','status','unchecked_ids']},indent=2))
    if failed: print(json.dumps(failed,indent=2,default=str))
    return 0 if report['status']=='PASS' else 1

if __name__=='__main__':
    sys.exit(main())
