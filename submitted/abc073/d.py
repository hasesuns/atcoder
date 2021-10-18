# --- ワーシャルフロイド 任意のペアに対して最短距離を求める（非負）
def warshall_floyd(dp):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j] , dp[i][k] + dp[k][j])
    return dp

n, m,R = map(int, input().split())
r = list( map(int, input().split()))

d = [[float("inf")]*n for i in range(n)]

abc = [tuple(map(int,input().split())) for i in range(m)]
for a,b,c in abc:
    a,b = a-1,b-1
    d[a][b] = c
    d[b][a] = c

for i in range(n):
    d[i][i] = 0

warshall_floyd(d)

import itertools

p = itertools.permutations(r, R)

INF = float('inf')
ans = INF
for path in p:
    tmp = 0
    for i in range(R-1):
        tmp += d[path[i]-1][path[i+1]-1]
    ans = min(ans,tmp)

print(ans)