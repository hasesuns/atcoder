import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m, k = map(int, input().split())

ab = [tuple(map(int,input().split())) for _ in range(m)]
adj_list = [[] for _ in range(n)]
indegree_list = [0] * n
for i, (a,b) in enumerate(ab):
    a, b = a - 1, b - 1
    adj_list[a].append(b)
    indegree_list[b] += 1

class TopologicalSortDFS:
    def __init__(self, n, adj_list, indegree_list, max_num_ans=1):
        self.n = n
        self.adj_list = adj_list
        self.max_num_ans = max_num_ans
        self.indegree_list = indegree_list
        self.zero_indegree_list = []
        for i in range(n):
            if self.indegree_list[i] == 0:
                self.zero_indegree_list.append(i)

        self.ans_order_list = []
        self.tmp_order = []

    def _try_exit(self):
        if len(self.ans_order_list) >= self.max_num_ans:
            for i in range(self.max_num_ans):
                print(*self.ans_order_list[i], sep=" ")
            exit()

    def _forward(self, target, target_idx):
        del self.zero_indegree_list[target_idx]
        self.tmp_order.append(target+1)
        for to in self.adj_list[target]:
            self.indegree_list[to] -= 1
            if indegree_list[to] == 0:
                self.zero_indegree_list.append(to)

    def _back(self, target, target_idx):
        for to in self.adj_list[target]:
            if indegree_list[to] == 0:
                self.zero_indegree_list.pop()
            self.indegree_list[to] += 1
        self.tmp_order.pop()
        self.zero_indegree_list.insert(target_idx, target)

    def dfs(self, depth):
        if depth == self.n:
            self.ans_order_list.append(self.tmp_order[:])
            self._try_exit()
            return

        if len(self.zero_indegree_list) == 0:
            print(-1)
            exit()

        for target_idx in range(len(self.zero_indegree_list)):
            target = self.zero_indegree_list[target_idx]

            self._forward(target, target_idx)
            self.dfs(depth + 1)
            self._back(target, target_idx)

topological_sort_dfs = TopologicalSortDFS(n, adj_list, indegree_list, k)
topological_sort_dfs.dfs(0)

print(-1)