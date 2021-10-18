import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

for length in range(1, n+1):
    for left in range(n - length + 1):
        right = left + length
        if n % 2 == length % 2:  # Tarou
            dp[left][right] = max(dp[left+1][right]+a[left], dp[left][right-1]+a[right-1])
        else:                    # Jirou
            dp[left][right] = min(dp[left+1][right]-a[left], dp[left][right-1]-a[right-1])

print(dp[0][n])