import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

from collections import defaultdict

n, m = map(int, input().split())
dg = defaultdict(list)
dg_reverse = defaultdict(list)
ab = [tuple(map(int,input().split())) for i in range(m)]
for a,b in ab:
    a,b = a-1,b-1
    dg[a].append(b)
    dg_reverse[b].append(a)

from collections import deque
# 辺の重みが全て1なので普通のbfsで解ける
def sssp_bfs(start, N):
    dist = [-1] * N
    prev = [-1] * N  # パス復元用
    que = deque([start])
    dist[start] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in dg[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            que.append(w)
            prev[w] = v

    return dist, prev

shortest_dist = float('inf')
shortest_path = []

for s in range(n):
    dist, prev = sssp_bfs(s, n)
    for g in dg_reverse[s]:
        tmp = dist[g]
        if tmp != -1 and tmp < shortest_dist:
            shortest_dist = tmp + 1
            shortest_path = []
            cur = g
            while cur != s:
                shortest_path.append(cur + 1)
                cur = prev[cur]
            shortest_path.append(s + 1)

shortest_path = shortest_path[::-1]
if shortest_path != []:
    print(shortest_dist)
    print(*shortest_path, sep='\n')
else:
    print(-1)