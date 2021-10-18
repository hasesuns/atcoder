import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
INF = float('inf')

n = int(input())
a = list( map(int, input().split()))

dp = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n):
    dp[i][i+1] = 0

from itertools import accumulate
accA = [0] + a
accA = list(accumulate(accA))

for length in range(n+1):
    for left in range(n - length + 1):
        right = left + length
        for i in range(1,length):
            dp[left][right] = min(dp[left][right], dp[left][left+i] + dp[left+i][right] + accA[right] - accA[left] )

print(dp[0][n])