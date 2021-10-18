import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from bisect import bisect_left

n, k = map(int, input().split())
v = list( map(int, input().split()))

amax = min(n,k)
ans = 0
for a in range(amax+1):
    bmax = amax - a
    for b in range(bmax+1):

        getlist = v[:a] + v[n-b:]
        getlist.sort()
        cdmax = k - a - b
        zero_index = bisect_left(getlist, 0)
        start = min(zero_index, cdmax)
        tmp = sum(getlist[start:])
        ans = max(ans, tmp)

print(ans)