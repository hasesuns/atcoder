# import sys
# input = sys.stdin.readline

n, m, l = map(int, input().split())

def warshall_floyd(dp):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j] , dp[i][k] + dp[k][j])
    return dp

dp = [[float('inf')]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int,input().split())
    dp[a-1][b-1] = dp[b-1][a-1] = c

for i in range(n):
    dp[i][i] = 0

dp = warshall_floyd(dp)

dp2 = [[float('inf')]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dp[i][j] <= l:
            dp2[i][j] = 1
    dp2[i][i] = 0
dp2 = warshall_floyd(dp2)

q = int(input())

ans = [0]*q
for i in range(q):
    s, t = map(int,input().split())
    tmp = dp2[s-1][t-1]
    ans[i] = -1 if tmp == float('inf') else tmp - 1

print(*ans, sep='\n')