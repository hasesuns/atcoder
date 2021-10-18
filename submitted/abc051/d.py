import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

# --- ワーシャルフロイド
def warshall_floyd(dp):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j] , dp[i][k] + dp[k][j])
    return dp

n, m = map(int, input().split())
d = [[float("inf")]*n for i in range(n)]

abc = [tuple(map(int,input().split())) for i in range(m)]
for a,b,c in abc:
    a,b = a-1,b-1
    d[a][b] = c
    d[b][a] = c

for i in range(n):
    d[i][i] = 0

warshall_floyd(d)

ans = m

for i, (a,b,c) in enumerate(abc):
    a,b = a-1,b-1
    for j in range(n):
        if  d[j][a] + c == d[j][b]:
            ans-=1
            break

print(ans)

 