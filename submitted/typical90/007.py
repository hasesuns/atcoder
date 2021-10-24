import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = list(int(input()) for _ in range(q))
a.sort()

for bb in b:
    ans = 0
    idx = bisect_left(a, bb)
    if idx == 0:
        ans = abs(a[idx] - bb)
    elif idx == n:
        ans = abs(a[idx - 1] - bb)
    else:
        ans = min(abs(a[idx - 1] - bb), abs(a[idx] - bb))

    print(ans)