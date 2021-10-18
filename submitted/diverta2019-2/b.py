import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

x = [0]*n
y = [0]*n
for i in range(n):
    xx,yy= map(int, input().split())
    x[i] = xx-1
    y[i] = yy-1

if n==1:
    print(1)
    exit()

from collections import defaultdict
d = defaultdict(lambda:0)

for i in range(n):
    for j in range(n):
        if i==j:continue

        p = x[j]-x[i]
        q = y[j]-y[i]

        d[p*10**9+q] +=1

dv = d.values()
mad =max(dv)

print(n-mad)