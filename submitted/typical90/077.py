import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, t = map(int, input().split())
a = [tuple(map(int, input().split() + [i])) for i in range(n)]
b = [tuple(map(int, input().split())) for _ in range(n)]
a.sort() # HACK
b.sort() # HACK

b_map = {b_: i for i, b_ in enumerate(b)}
dist_to_d = {
    # HACK
    (-t, -t): 6,
    (-t, t): 4,
    (-t, 0): 5,
    (0, -t): 7,
    (0, t): 3,
    (t, -t): 8,
    (t, t): 2,
    (t, 0): 1,
}

from collections import deque


class Dinic:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = [[] for _ in range(num_nodes)]

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

    def _bfs(self, s, t):
        self.level = level = [None] * self.num_nodes
        deq = deque([s])
        level[s] = 0
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in self.graph[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def _dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self._dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10 ** 9 + 7
        while self._bfs(s, t):
            (*self.it,) = map(iter, self.graph)
            f = INF
            while f:
                f = self._dfs(s, t, INF)
                flow += f
        return flow


dinic = Dinic(2 * n + 2)
# sourceとtankのindexは最後に持ってきた方が実装時の添字のバグは起きにくそう
source = 2 * n
tank = 2 * n + 1

for ax, ay, i in a:
    dinic.add_edge(source, i, 1)
    for (dx, dy) in dist_to_d.keys():
        b_ = b_map.get((ax + dx, ay + dy))
        if b_ is not None:
            dinic.add_edge(i, b_ + n, 1)
    dinic.add_edge(i + n, tank, 1)

flow = dinic.flow(source, tank)
if flow != n:
    print("No")
    exit()

# 復元
ans = [0] * n
for ax, ay, idx in a:
    for (to, cap, _) in dinic.graph[idx]:
        to -= n
        if cap == 0 and 0 <= to < n:
            dx = b[to][0] - ax
            dy = b[to][1] - ay
            ans[idx] = dist_to_d[(dx, dy)]
            break

print("Yes")
print(*ans)