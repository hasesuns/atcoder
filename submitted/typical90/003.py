import sys
from typing import List

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n - 1)]
adj_list = [[] for i in range(n)]
for a, b in ab:
    a, b = a - 1, b - 1
    adj_list[a].append(b)
    adj_list[b].append(a)


class TreeDiameterSolver:
    def __init__(self):
        self.max_dist = -1
        self.most_far_pos = -1

    def dfs(self, now_pos: int, is_visited: List[bool], dist: int):
        is_visited[now_pos] = True
        if self.max_dist < dist:
            self.max_dist = dist
            self.most_far_pos = now_pos

        for next in self.adj_list[now_pos]:
            if is_visited[next]:
                continue
            self.dfs(next, is_visited, dist + 1)

    def solve(self, num_node: int, adj_list: List[List[int]]):
        self.adj_list = adj_list
        self.dfs(0, [False] * num_node, 0)
        pos_u = self.most_far_pos  # most far from 0

        self.max_dist = -1
        self.most_far_pos = -1
        self.dfs(pos_u, [False] * num_node, 0)
        pos_v = self.most_far_pos  # most far from u
        diameter = self.max_dist
        return diameter, pos_u, pos_v


tds = TreeDiameterSolver()
diameter, _, _ = tds.solve(num_node=n, adj_list=adj_list)

ans = diameter + 1
print(ans)