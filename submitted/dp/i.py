n = int(input())
p = list(map(float, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1
# dp[i][j]:i番目以前の商品を見たときに表の枚数がj枚となる確率の和

for i in range(1,n+1):
    for j in range(i+1):
            dp[i][j] = dp[i-1][j]*(1-p[i-1])
            if j>0:
                dp[i][j] += dp[i-1][j-1]*p[i-1]

ans = sum(dp[n][(n+1)//2:])

print(ans)