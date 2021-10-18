import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list( map(int, input().split()))
p = 10**9 + 7

dp = [[0]*(k+1) for _ in range(n+1)]
dp_sum = [[0]*(k+1) for _ in range(n+1)]

for i in range(0, n+1):
    dp[i][0] = 1
    dp_sum[i][0] = dp[i][0]
    for j in range(1, k+1):
        dp_sum[i][j] = dp_sum[i][j-1]%p + dp[i][j]%p

for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = dp_sum[i-1][j]%p
        if j - a[i-1] - 1 >= 0:
            dp[i][j] -= dp_sum[i-1][j-a[i-1]-1]%p

        dp_sum[i][j] = dp_sum[i][j-1]%p + dp[i][j]%p

print(dp[n][k]%p)