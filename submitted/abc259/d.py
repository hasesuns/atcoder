import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
sx, sy, tx, ty = map(int, input().split())
xyr = [tuple(map(int,input().split())) for _ in range(n)]

class UnionFind():
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
        return ''.join('{}: {}'.format(r, self.members(r)) for r in self.all_roots())

uf = UnionFind(n+2)

def dist2(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

for i in range(n):
    x, y, r = xyr[i]
    if dist2(x, y, sx, sy) == r**2:
        uf.union(i, n)
    if dist2(x, y, tx, ty) == r**2:
        uf.union(i, n+1)
    for j in range(i, n):
        xx, yy, rr = xyr[j]

        minr = min(r, rr)
        maxr = max(r, rr)
        if (maxr-minr)**2 <= dist2(x, y, xx, yy) <= (r + rr)**2:
            uf.union(i, j)

if uf.is_same(n, n+1):
    print('Yes')
else:
    print('No')
    