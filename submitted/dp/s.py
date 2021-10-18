K = input()
D = int(input())
p = 10 ** 9 + 7

# dp[桁][Dで割った余り][is_smaller]
dp = [[[0]*2 for _ in range(D)] for _ in range(len(K)+1)]
dp[0][0][0] = 1  # Kの最高位のさらに1桁多い位が0のケース

for i in range(len(K)):
    for j in range(D):

        # smaller = 1 の時
        for k in range(10):
            # i+1桁目がk
            dp[i+1][(j+k)%D][1] += dp[i][j][1]%p
            dp[i+1][(j+k)%D][1] %= p

        # smaller = 0 から smaller = 0
        dp[i+1][(j+int(K[i]))%D][0] += dp[i][j][0]%p
        dp[i+1][(j+int(K[i]))%D][0] %= p

        # smaller = 0 から smaller = 1
        for k in range(int(K[i])):
            dp[i+1][(j+k)%D][1] += dp[i][j][0]%p
            dp[i+1][(j+k)%D][1] %= p

ans = dp[len(K)][0][0] + dp[len(K)][0][1] - 1  # 初期化で与えたKの最高位よりもさらに1桁多い位が0のケースの1通りを除く
ans %= p

print(ans)