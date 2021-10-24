import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, q = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]

sqrt2_acwrot45_xy = []
x_min, x_max, y_min, y_max = float("inf"), -float("inf"), float("inf"), -float("inf")
for x, y in xy:
    sqrt2_acwrot45_x = x + y
    sqrt2_acwrot45_y = x - y
    sqrt2_acwrot45_xy.append((sqrt2_acwrot45_x, sqrt2_acwrot45_y))
    x_min = min(x_min, sqrt2_acwrot45_x)
    x_max = max(x_max, sqrt2_acwrot45_x)
    y_min = min(y_min, sqrt2_acwrot45_y)
    y_max = max(y_max, sqrt2_acwrot45_y)

for _ in range(q):
    i = int(input()) - 1
    x_, y_ = sqrt2_acwrot45_xy[i]
    ans = max(abs(x_min - x_), abs(x_max - x_), abs(y_min - y_), abs(y_max - y_))
    print(ans)