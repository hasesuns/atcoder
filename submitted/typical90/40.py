from collections import deque


class Dinic:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = [[] for i in range(num_nodes)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.graph[v1].append(edge1)
        self.graph[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.num_nodes
        deq = deque([s])
        level[s] = 0
        graph = self.graph
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in graph[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        while self.bfs(s, t):
            *self.it, = map(iter, self.graph)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, w = map(int, input().split())
a = list(map(int, input().split()))

INF = float('inf')
graph = Dinic(n+2)
s, t = 0, n+1
offset_sum = 0

for i in range(n):
    graph.add_edge(s, i+1, w)  # w - a[i] + offset 
    graph.add_edge(i+1, t, a[i])  # offset
    offset_sum += a[i]

    kc = list(map(int, input().split()))
    for c in kc[1:]:
        graph.add_edge(i+1, c, float("inf"))  # 向きはグラフを書くと確認できる

min_cost = graph.max_flow(s,t)
ans = offset_sum - min_cost
print(ans)