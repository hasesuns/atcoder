import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.loop = [0] * n

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
        return ''.join('{}: {}'.format(r, self.members(r)) for r in self.all_roots())

n, h, w = map(int, input().split())

rca = [tuple(map(int,input().split())) for i in range(n)]
rca = sorted(rca, key=lambda x: x[2], reverse=True)

uf = UnionFind(h+w)

ans = 0
for r, c, a in rca:
    r, c = r - 1, c - 1 + h
    if uf.is_same(r, c):
        root = uf.root(r)
        if uf.loop[root] == 0:
            ans += a
            uf.loop[root] = uf.loop[r] = uf.loop[c] = 1
    else:
        root_r = uf.root(r)
        root_c = uf.root(c)
        if uf.loop[root_r] == 0 or uf.loop[root_c] == 0:

            # どちらがrootとして更新されてもloopが正しく反映されるように注意
            if uf.loop[root_r] == 1:
                uf.loop[root_c] = 1
            elif uf.loop[root_c] == 1:
                uf.loop[root_r] = 1

            ans += a
            uf.union(r, c)

print(ans)