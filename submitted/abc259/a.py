import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m, x, t, d = map(int, input().split())

if m > x:
    ans = t
else:
    ans = t - (x-m) * d

print(ans)