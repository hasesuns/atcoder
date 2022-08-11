import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

def calc_dist(x, y, xx, yy):
    return ((xx - x)**2 + (yy-y)**2)**0.5

ans = 0

for i in range(n):
    tmp_min = 10 ** 9
    for aa in a:
        tmp_min = min(tmp_min, calc_dist(x[i], y[i], x[aa - 1], y[aa - 1]))
    ans = max(ans, tmp_min)

print(ans)