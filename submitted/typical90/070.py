import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
x.sort()
y.sort()

x_median = x[n//2]
y_median = y[n//2]

ans = 0

for i in range(n):
    ans += abs(x_median - x[i])
    ans += abs(y_median - y[i])

print(ans)