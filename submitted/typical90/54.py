import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
adjacency = [[] for _ in range(n+m)]
for paper_idx in range(m):
    k = int(input())
    r = list(map(int, input().split()))
    for j in range(k):
        researcher_idx = r[j] - 1 + m
        adjacency[paper_idx].append(researcher_idx)
        adjacency[researcher_idx].append(paper_idx)

def sssp_bfs(start, n):
    dist = [-1] * n
    prev = [-1] * n  # パス復元用
    que = deque([start])
    dist[start] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in adjacency[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            que.append(w)
            prev[w] = v
    return dist, prev

takahashi_index = 1 - 1 + m
dist, prev = sssp_bfs(takahashi_index, n+m)

for i in range(n):
    print(dist[i + m] // 2)