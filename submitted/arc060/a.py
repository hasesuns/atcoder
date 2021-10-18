import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, a = map(int, input().split())
x = list( map(int, input().split()))


# i番目までで総和がjで使った枚数がkになる組み合わせの総数
dp = [[[0]*(n+1) for _ in range(a*n+1)] for _ in range(n+1)]

for i in range(0, n+1):
    dp[i][0][0] = 1

for i in range(1, n+1):
    for j in range(1, a*n+1):
        for k in range(1, n+1):
            if j - x[i-1] >= 0:
                dp[i][j][k] = dp[i-1][j-x[i-1]][k-1] +  dp[i-1][j][k]
            else:
                dp[i][j][k] = dp[i-1][j][k]

ans = 0

for i in range(1, n+1):
    sum_ = i * a
    ans += dp[n][sum_][i]

print(ans)