from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)
import numpy as np
# import numpy as np
# 答えの提出の時にi+1とj+1は忘れないように
h, w = map(int, input().split())
cost = [[-1 for i in range(10)] for j in range(10)]

for i in range(10):
    cost[i] = list( map(int, input().split()))

cost = np.array(cost).T

def dijkstra(s,n,w,cost):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost[u][v] : vからuへのコスト(逆にした)
    d = [float("inf")] * (n+1)
    used = [False] * n
    d[s] = 0
    num = [0]*n # 視点sから各頂点への最短経路の経路数を保存するリスト
    num[s] = 1 # 辺の重みが0のやつがあったらここ使えないな

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
            if d[j] > d[v]+cost[v][j]: # vを使った場合と使わない場合の最短値で比較
                d[j] = d[v]+cost[v][j]

    return d

d = dijkstra(1,10,100,cost)
d[-1] = 0

ans = 0
for _ in range(h):
    for number in list( map(int, input().split())):
        ans += d[number]

print(ans)