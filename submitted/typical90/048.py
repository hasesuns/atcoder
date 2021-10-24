import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())

points = []
for i in range(n):
    a, b = map(int, input().split())
    points.append(b)
    points.append(a-b)

points.sort(reverse=True)
ans = sum(points[:k])

print(ans)