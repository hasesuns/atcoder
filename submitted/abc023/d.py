import numpy as np
n = int(input())
from collections import defaultdict
h = np.array([0]* n)
s = np.array([0]* n)
for i in range(n):
    h[i], s[i] = map(int, input().split())

height = h

ans = 0

def isok(ans):
    time_limits = (ans - h)/s
    time_limits.sort()

    for i in range(n):
        if time_limits[i] < i:
            return False
    return True


ok = np.max(h)+n*np.max(s)
ng = -1 # -1にしとけば答えが0の時も普通に扱えるな

while ok - ng > 1:
    m = (ok+ng)//2
    if isok(m):
        ok = m
    else:
        ng = m
print(ok)
 