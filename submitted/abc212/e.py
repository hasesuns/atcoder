import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m, k = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]
non_adj_list = [[i] for i in range(n)]
for _, (a, b) in enumerate(ab):
    a, b = a - 1, b - 1
    non_adj_list[a].append(b)
    non_adj_list[b].append(a)

p = 998244353

# dp[day][j]:都市1をスタートしてday日目にj番目の都市に到達する通り数
dp = [[0] * n for _ in range(k + 1)]
dp[0][0] = 1

for day in range(1, k + 1):
    total = sum(dp[day-1]) % p
    for i in range(n):
        dp[day][i] = total
        for j in non_adj_list[i]:
            dp[day][i] -= dp[day - 1][j]
            dp[day][i] %= p

ans = dp[k][0]
print(ans)