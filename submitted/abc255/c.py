import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x, a, d, n = map(int, input().split())

if d >= 0:
    start = a
    end = a + d * (n-1)
else:
    end = a
    start = a + d * (n-1)


if x <= start:
    print(start-x)
    exit()
elif x >= end:
    print(x-end)
    exit()

tmp = x - a
d = abs(d)
ans1 = tmp % d
ans2 = d - ans1
ans = min(ans1, ans2)
print(ans)