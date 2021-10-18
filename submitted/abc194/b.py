import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int,input().split())) for i in range(n)]
ab = sorted(ab, key=lambda x: x[0])

a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = ab[i]

ans = a[0] + b[0]
ans = min(ans, max(a[0], min(b[1:])))

ab = sorted(ab, key=lambda x: x[1])
for i in range(n):
    a[i], b[i] = ab[i]

ans = min(ans, max(min(a[1:]), b[0]))

print(ans)