n = int(input())
uvw = [tuple(map(int,input().split())) for i in range(n-1)]
to_dist = [[] for i in range(n)]
for u,v,w in uvw:
    u,v = u-1,v-1
    to_dist[u].append((v,w))
    to_dist[v].append((u,w))

visited = [0]* n
visited[0] = 1
ans = [0]*n
start_vertexes = [0]
 
while start_vertexes:
    start_vertex = start_vertexes.pop()
    for to, dist in to_dist[start_vertex]:
        if visited[to]: continue
        ans[to] = (ans[start_vertex]+dist)%2
        visited[to] = 1
        start_vertexes.append(to)
print(*ans, sep='\n')