s = input()

INF = float('inf')
dp = [[INF,INF] for _ in range(len(s)+1)]
dp[0][0]=0
dp[0][1]=1
for i in range(len(s)):
    dp[i+1][0] = min(dp[i][0]+int(s[i]), dp[i][1]+10-int(s[i]), dp[i][1]+int(s[i])+1)
    dp[i+1][1] = min(dp[i][0]+int(s[i])+1,dp[i][1]+10-int(s[i])-1)

print(dp[-1][0])