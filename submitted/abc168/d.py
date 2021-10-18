import heapq
n,m = map(int,input().split())
src = [tuple(map(int,input().split())) for i in range(m)]

es = [[] for i in range(n)]
for x,y in src:
    x,y = x-1,y-1
    es[x].append(y)
    es[y].append(x)

INF = float('inf')
ds = [INF] * n
ans = [-1]*(n)

def dijkstra(start, dists):
    dists[start] = 0
    hq = [(0,start)]
    heapq.heapify(hq)
    while hq:
        dist,v = heapq.heappop(hq)
        for to in es[v]:
            if dist+1 >= dists[to]: continue
            dists[to] = dist+1
            ans[to]=v+1
            heapq.heappush(hq, (dist+1,to))

dijkstra(0,ds)

print('Yes')
print(*ans[1:],sep='\n')