import sys

sys.setrecursionlimit(10 ** 7)
from fractions import Fraction

input = sys.stdin.readline

n = int(input())
x = [0] * n
y = [0] * n
p = [0] * n
for i in range(n):
    x[i], y[i], p[i] = map(int, input().split())

adj_matrix = [[Fraction(0, 1)] * n for _ in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        adj_matrix[i][j] = Fraction(abs(x[j] - x[i]) + abs(y[j] - y[i]), p[i])
        adj_matrix[j][i] = Fraction(abs(x[j] - x[i]) + abs(y[j] - y[i]), p[j])

# 任意のペアに対して最短距離を求める（非負）
def warshall_floyd():
    global dp
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] < dp[k][j]:
                    bigger_cost = dp[k][j]
                else:
                    bigger_cost = dp[i][k]

                if dp[i][j] > bigger_cost:
                    dp[i][j] = bigger_cost


dp = adj_matrix
warshall_floyd()

INF = 10 ** 10
min_frac = Fraction(INF, 1)
for start in range(n):
    tmp_max_frac = Fraction(0, 1)
    for cost in dp[start]:
        if tmp_max_frac < cost:
            tmp_max_frac = cost
    if min_frac > tmp_max_frac:
        min_frac = tmp_max_frac

ans = -(-min_frac.numerator // min_frac.denominator)
print(ans)