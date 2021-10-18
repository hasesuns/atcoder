import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
x = [0]* n
y = [0]* n
for i in range(n):
    x[i],y[i] = map(int, input().split())

import itertools
ans=0
for v in itertools.combinations(range(n),3):
    a,b,c = v
    xb = x[b]-x[a]
    yb = y[b]-y[a]
    xc = x[c]-x[a]
    yc = y[c]-y[a]

    s2 = abs(xb*yc-xc*yb)

    if s2%2==0 and s2>0:
        ans+=1

print(ans)
 