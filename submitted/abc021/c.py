def dijkstra(s,e,n,w,cost):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    num = [0]*n
    num[s] = 1

    while True:
        v = -1
        #まだ使われてない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True

        for j in range(n):
            if d[j] > d[v]+cost[v][j]:
                d[j] = d[v]+cost[v][j]
                num[j] = num[v]
            elif d[j] == d[v]+cost[v][j]:
                num[j] += num[v]
                num[j] %= MOD
    return d, num

################################
MOD = 10**9+7
n = int(input())
a, b = map(int, input().split())
m = int(input())
cost = [[float('inf') for i in range(n)] for j in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    cost[x-1][y-1] = 1
    cost[y-1][x-1] = 1

d, num  = dijkstra(a-1, b-1,n,m,cost)

print(num[b-1])
 