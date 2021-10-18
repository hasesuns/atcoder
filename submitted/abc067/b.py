n = int(input())

ab = [tuple(map(int,input().split())) for i in range(n-1)]
es = [[] for i in range(n)]
for a,b in ab:
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a)
INF = float('inf')
dist0 = [INF] * n
dist0[0] = 0
import heapq
hq = [(0,0)]
heapq.heapify(hq)
while hq:
    c,v = heapq.heappop(hq)
    for to in es[v]:
        if c+1 >= dist0[to]: continue
        dist0[to] = c+1
        heapq.heappush(hq,(c+1,to))

distn = [INF] * n
distn[n-1] = 0
hq = [(0,n-1)]
heapq.heapify(hq)
while hq:
    c,v = heapq.heappop(hq)
    for to in es[v]:
        if c+1 >= distn[to]: continue
        distn[to] = c+1
        heapq.heappush(hq,(c+1,to))


count_f = 0
for i in range(n):
    if dist0[i] <= distn[i]:
        count_f+=1

if count_f > n-count_f: print('Fennec')
else: print('Snuke')
 