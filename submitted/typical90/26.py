import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int,input().split())) for _ in range(n-1)]
adj_list = [[] for _ in range(n)]
for i, (a,b) in enumerate(ab):
    a, b = a - 1, b - 1
    adj_list[a].append(b)
    adj_list[b].append(a)

def sssp_bfs(start, n):
    dist = [-1] * n
    prev = [-1] * n  # パス復元用
    que = deque([start])
    dist[start] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in adj_list[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            que.append(w)
            prev[w] = v
    return dist, prev

dist, prev = sssp_bfs(start=0, n=n)

ans = []
for i, d in enumerate(dist):
    if d % 2 ==0:
        ans.append(i+1)
    if len(ans) == n // 2:
        print(*ans, sep=" ")
        exit()

ans = []
for i, d in enumerate(dist):
    if d % 2 ==1:
        ans.append(i+1)
    if len(ans) == n // 2:
        print(*ans, sep=" ")
        exit()
 