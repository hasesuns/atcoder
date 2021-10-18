import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from bisect import bisect_left


n, m = map(int, input().split())
a = list( map(int, input().split()))
a.sort()

bc = [tuple(map(int,input().split())) for i in range(m)]
bc = sorted(bc, reverse=True, key=lambda x: x[1])

i = 0
d = []
for b, c in bc:
    d.extend([c]*b)
    if len(d) >= n:
        break

ans = 0
for i in range(n):
    if i < len(d):
        ans += max(a[i], d[i])
    else: ans += a[i]

print(ans)