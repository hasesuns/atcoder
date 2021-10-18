n, t = [int(i) for i in input().split()]
dishes = []
for _ in range(n):
    a, b = map(int, input().split())
    dishes.append((a, b))

dishes = sorted(dishes, key=lambda x: x[0])

dp = [[0] * t for _ in range(n+1)]

ans = 0

for i in range(n):
    for j in range(t):
        if j < dishes[i][0] :
            dp[i+1][j] = dp[i][j]
        else:
            if dp[i][j] > dp[i][j-dishes[i][0]]+dishes[i][1]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = dp[i][j-dishes[i][0]]+dishes[i][1]
    ans_i = dp[i][t-1] + max( dishes[i:], key=lambda x: x[1])[1]
    ans = max(ans, ans_i)

print(ans)