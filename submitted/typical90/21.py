import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from typing import List


class SCC():
    """Strongly Connected Components
    """
    def __init__(self, num_node: int, adj_list: List[List[int]], rev_adj_list: List[List[int]]):
        self.num_node = num_node
        self.adj_list = adj_list
        self.rev_adj_list = rev_adj_list
        self.postorder = []  # 帰りがけ順（postoder）のindex list
        self.visited = [False] * self.num_node
        self.node2comp_list = [None] * self.num_node 

    def _dfs(self, node_now: int):
        self.visited[node_now] = True
        for node_next in self.adj_list[node_now]:
            if not self.visited[node_next]:
                self._dfs(node_next)
        self.postorder.append(node_now)

    def _rdfs(self, node_now: int, comp_idx):
        self.node2comp_list[node_now] = comp_idx
        self.visited[node_now] = True
        for node_next in self.rev_adj_list[node_now]:
            if not self.visited[node_next]:
                self._rdfs(node_next, comp_idx)

    def exec(self):
        for i in range(self.num_node):
            if not self.visited[i]:
                self._dfs(i)
        self.visited = [False]*self.num_node
        comp_idx = 0
        for node_now in reversed(self.postorder):
            if not self.visited[node_now]:
                self._rdfs(node_now, comp_idx)
                comp_idx += 1
        num_comp = comp_idx
        return num_comp, self.node2comp_list

n, m = map(int, input().split())
ab = [tuple(map(int,input().split())) for _ in range(m)]
adj_list = [[] for _ in range(n)]
rev_adj_list =  [[] for _ in range(n)]
for i, (a,b) in enumerate(ab):
    a, b = a - 1, b - 1
    adj_list[a].append(b)
    rev_adj_list[b].append(a)

scc = SCC(num_node=n, adj_list=adj_list, rev_adj_list=rev_adj_list)
num_comp, node2comp_list = scc.exec()

num_nodes_in_comps = [0] * num_comp
for comp_idx in node2comp_list:
    num_nodes_in_comps[comp_idx] += 1
    
ans = 0
for num_nodes_in_comp in num_nodes_in_comps:
    ans += num_nodes_in_comp * (num_nodes_in_comp - 1) // 2

print(ans)