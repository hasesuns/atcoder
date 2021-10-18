import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = list( map(int, input().split()))
b = list( map(int, input().split()))

from itertools import accumulate
aacc = [0] + a
aacc = list(accumulate(aacc))
bacc = [0] + b
bacc = list(accumulate(bacc))

from bisect import bisect_right
ans = 0
for cnta, ac in enumerate(aacc):
    if k-ac>=0:
        cntb = bisect_right(bacc, k-ac) - 1
        ans = max(ans, cnta+cntb)

print(ans)