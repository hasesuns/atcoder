N, W = map(int, input().split())
w, v = [0]*(N+1),[0]*(N+1)
for i in range(N):
    w[i+1], v[i+1] = [int(_) for _ in input().split()]
V = sum(v)

dp = [[10**12]*(V+1) for _ in range(N+1)]
dp[0][0] = 0
# dp[i][j]:i番目以前の商品を見たときの価値総和jとしたときの重さの最小値

ans = 0
for i in range(1,N+1):
    for j in range(V+1): # なんか間違えて1スタートにしててハマった
        if v[i] <= j: #v[i]が入るとjになるときの計算なので，v[i]がjよりでかいのはあり得ない。j-v[i]>0だしね。
            # i-1番目までの商品で価値jの場合とi番目の商品を入れて価値jの場合の比較
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i]] + w[i])
        else:
            dp[i][j] = dp[i-1][j]


for j in range(V+1):
    if dp[N][j] <= W:
        ans = max(ans, j)

print(ans)