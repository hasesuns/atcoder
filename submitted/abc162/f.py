import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

INF = float('inf')

skip = 1 + n % 2

dp = [[-INF]*(skip+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(skip+1):
        if j < skip:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
        tmp = dp[i][j]
        if (i+j)%2 == 0: tmp += a[i]
        dp[i+1][j] = max(dp[i+1][j], tmp)

ans = dp[n][skip]

print(ans)