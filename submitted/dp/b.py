import sys
input = sys.stdin.readline

import numpy as np

n, k = map(int, input().split())
h = np.array([int(i) for i in input().split()])

dp = np.array([0]*n)
dp[0] = 0

for i in range(1,n):
    j = max(0,i-k)
    dp[i] = np.min(np.abs(h[i] - h[j:i]) + dp[j:i] )

print(dp[-1])