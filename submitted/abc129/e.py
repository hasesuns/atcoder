s = input() #sys.stdin.readlineは最後が改行
n = len(s)
p=10**9+7

dp = [[0]*2 for _ in range(n)]

dp[0][0]=2
dp[0][1]=1


# dp[i][smaller]:i番目以前の商品を見たときの組み合わせの数。L以下が確定かどうか

for i in range(1,n):
        if s[i]=='1':
            dp[i][0] = (dp[i-1][0]*2)%p
            dp[i][1] = (dp[i-1][1]*3)%p + (dp[i-1][0])%p
        else:
            dp[i][0] = dp[i-1][0]*1
            dp[i][1] = (dp[i-1][1]*3)%p

print((dp[n-1][0]+dp[n-1][1])%p)
 