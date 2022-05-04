import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
l = [0] * n
r = [0] * n
for i in range(n):
    l[i], r[i] = map(int, input().split())

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ri_ = r[i] + 1
        rj_ = r[j] + 1
        num_patterns = (ri_ - l[i]) * (rj_ - l[j])
        for k in range(l[i], ri_):
            ans += max(max(k - l[j], 0) - max(k - rj_, 0), 0) / num_patterns

print(ans)