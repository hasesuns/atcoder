import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
wsv = [tuple(map(int,input().split())) for i in range(n)]
wsv = sorted(wsv, key=lambda x: x[0]+x[1])  # s+wの値でソート
S = 10**4  # sの最大値
dp = [[0] * (2*S+1) for _ in range(n+1)]  # dp[i][j]:i番目以前の商品を見たときに重さの和をjとしたときの価値の最大値

for i in range(1, n+1):
    w, s, v = wsv[i-1]
    for j in range(2*S+1):
        if 0 <= j - w <= s:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]

ans = max(dp[n])
print(ans)