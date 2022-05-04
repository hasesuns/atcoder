class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.root(x)]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def members(self, x):  # 計算量n
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    def all_roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.all_roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.all_roots()}

    def __str__(self):
        return "".join("{}: {}".format(r, self.members(r)) for r in self.all_roots())


import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


n = int(input())
uf = UnionFind(n)
q = int(input())
txyv = [tuple(map(int, input().split())) for i in range(q)]

sum_list = [0] * n
for i, (t, x, y, v) in enumerate(txyv):
    x, y = x - 1, y - 1
    if t == 0:
        sum_list[x] = v
diff_list = [0] * n
diff_list[1] = -0 + sum_list[0]
for i in range(n - 2):
    diff_list[i + 2] = diff_list[i] + (sum_list[i + 1] - sum_list[i])
sum_list[-1] = diff_list[-1]

for i, (t, x, y, v) in enumerate(txyv):
    x, y = x - 1, y - 1
    if t == 0:
        sum_list[x] = v
        uf.union(x, y)
    else:
        if not uf.is_same(x, y):
            print("Ambiguous")
        else:
            offset = v - diff_list[x]
            if x % 2 == y % 2:
                ans = offset + diff_list[y]
            else:
                ans = -offset + diff_list[y]
            print(ans)