import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
s, t = map(int, input().split())

src = [tuple(map(int,input().split())) for i in range(m)]

es = [[] for i in range(n)]
for x,y,d in src:
    x,y = x-1,y-1
    es[x].append((y,d))
    es[y].append((x,d))


import heapq

def dijkstra(start, dists):
    dists[start] = 0
    hq = [(0,start)]
    heapq.heapify(hq)
    while hq:
        dist,v = heapq.heappop(hq)
        for to,d in es[v]:
            if dist+d >= dists[to]: continue
            dists[to] = dist+d
            heapq.heappush(hq, (dist+d,to))

INF = float('inf')
sdist = [INF] * n
tdist = [INF] * n

dijkstra(s-1,sdist)
dijkstra(t-1,tdist)


for i in range(n):
    if sdist[i]==tdist[i] and tdist[i]!=INF:
        print(i+1)
        exit()

print(-1)
 