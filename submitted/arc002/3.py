n = int(input())
s = input() #sys.stdin.readlineは最後が改行

if n==1:
    print(1)
    exit()

import itertools
abxy = ['A','B','X','Y']
lr = list(itertools.product(abxy,repeat=2))
INF = float('inf')
ans = n

for l,r in itertools.combinations(lr,2):
    dp = [INF]*(n+1)
    dp[0]=0
    dp[1]=1

    for i in range(1,n):
        if s[i-1]==l[0] and s[i]==l[1]:
            dp[i+1] = min(dp[i+1], dp[i-1]+1)
        elif s[i-1]==r[0] and s[i]==r[1]:
            dp[i+1] = min(dp[i+1], dp[i-1]+1)
        else:
            dp[i+1] = min(dp[i+1], dp[i]+1)

    ans = min(ans, dp[-1])

print(ans)