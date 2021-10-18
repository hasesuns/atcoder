n = int(input())

def warshall_floyd(dp):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp

d = [[float("inf")]*n for i in range(n)]

for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == '1':
            d[i][j] = 1
        if i == j:
            d[i][j] = 0

warshall_floyd(d)

ans = 0

for j in range(n):
    num_risk = 0
    for i in range(n):
        if d[i][j] != float("inf") and d[i][j] != 0:
            num_risk += 1
    ans += 1 / (1 + num_risk)

print(ans)