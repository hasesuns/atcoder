import heapq

n,m = map(int,input().split())
src = [tuple(map(int,input().split())) for i in range(m)]

es = [[] for i in range(n)]
for x,y,d in src:
    x,y = x-1,y-1
    es[x].append((y,d))
    es[y].append((x,d))

INF = float('inf')

def dijkstra(start, dist_list):
    dist_list[start] = 0
    hq = [(0,start)]
    heapq.heapify(hq)
    while hq:
        dist,v = heapq.heappop(hq)
        for to,d in es[v]:
            if dist+d >= dist_list[to]: continue
            dist_list[to] = dist+d
            heapq.heappush(hq, (dist+d,to))
    return dist_list

dist_list_from_s = [INF] * n
dist_list_from_s = dijkstra(0, dist_list_from_s)

dist_list_from_g = [INF] * n
dist_list_from_g = dijkstra(n-1, dist_list_from_g)

for i in range(n):
    print(dist_list_from_s[i]+dist_list_from_g[i])

    