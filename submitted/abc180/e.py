import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
xyz = [tuple(map(int, input().split())) for _ in range(n)]

# dp[s][i]:部分集合sを周りかつiに到達しているときの最小コスト
dp = [[10 ** 12] * (n) for _ in range(2**n)]
dp[0][0] = 0

for i in range(1 << n):
    for j in range(n):
        for k in range(n):
            if i != 0 and not (i >> k) & 1: continue
            if (i >> j) & 1 == 0:
                k2j = abs(xyz[j][0] - xyz[k][0]) + abs(xyz[j][1] - xyz[k][1]) + max(0, xyz[j][2] - xyz[k][2])
                dp[i | (1 << j)][j] = min(dp[i | (1 << j)][j], dp[i][k] + k2j)

ans = dp[2 ** n - 1][0]
print(ans)
 