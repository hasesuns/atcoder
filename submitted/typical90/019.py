import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# dp[l][r]:lからr番目全ての数字が除去される時のコストの最小値
dp = [[float("inf")]*2*n for _ in range(2*n)]

for i in range(2*n - 1):
    dp[i][i+1] = abs(a[i+1] - a[i])   

for length in range(1, 2*n, 2):
    for l in range(2*n-length):
        dp[l][l+length] = min(dp[l][l+length], dp[l+1][l+length-1] + abs(a[l+length] - a[l]))
        for k in range(length):
            dp[l][l+length] = min(dp[l][l+length], dp[l][l+k]+dp[l+k+1][l+length])

ans = dp[0][2*n-1]
print(ans)
 