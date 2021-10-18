import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

import numpy as np
oa, ab,bc = map(int, input().split())
r1 = oa+ab+bc
s1=r1*r1*np.pi

if bc>=oa+ab:
    r2=bc-oa-ab
elif oa>=ab+bc:
    r2=oa-ab-bc
elif ab>=oa+bc:
    r2=ab-oa-bc
else:
    r2=0
s2=r2*r2*np.pi
print(s1-s2)