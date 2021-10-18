import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
t = list( map(int, input().split()))

# dp[i][j]:i番目以前の商品を見たときに合計をjにできるか否か
dp = [[False] * (sum(t)+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = True

for i in range(n):
    for j in range(sum(t)):
        dp[i+1][j] |= dp[i][j]
        if j >= t[i]:
            dp[i+1][j] |= dp[i][j-t[i]]

ans = sum(t)
for i in range(-(-sum(t)//2), sum(t)+1):
    if dp[n][i]:
        ans = min(ans, i)

print(ans)