import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
s = input()[:-1]

# dp[i][j]:i番目以前文字を見たときにatcoderのj文字目まで結合できるケースの通り数
dp = [[0]*(7+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
ATCODER = "atcoder"
MOD = 10**9 + 7

for i in range(1,n+1):
    for j in range(1,7+1):
        dp[i][j] += dp[i-1][j] % MOD
        if ATCODER[j-1] == s[i-1]:
            dp[i][j] += dp[i-1][j-1] % MOD
    
ans = dp[n][7] % MOD
print(ans)