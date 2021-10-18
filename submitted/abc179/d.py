import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())

lr = [tuple(map(int,input().split())) for i in range(k)]
lr = sorted(lr, key=lambda x: x[0])

MOD = 998244353

dp = [0] * (n + 1) # マスiに行く方法の通り数
dp[0] = 1

dp_sparse = [0] * (2 * n + 1)
acc = 0
for i in range(n):
    for l, r in lr:
        dp_sparse[i + l] += dp[i] % MOD
        dp_sparse[i + l] %= MOD
        dp_sparse[i + r + 1] -= dp[i] % MOD
        dp_sparse[i + r + 1] %= MOD

    acc = (acc + dp_sparse[i + 1]) % MOD
    dp[i + 1] = acc % MOD

ans = dp[n-1]
print(ans)