N, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]
w = [0]*(N+1) # 商品番号とのズレが嫌だったのでこっちも1足しといた
v = [0]*(N+1)
for i in range(N):
    w[i+1], v[i+1] = wv[i]

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(W+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

print(dp[N][W])