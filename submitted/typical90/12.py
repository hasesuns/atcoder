import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


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


h, w = map(int, input().split())
table = [[0 for _ in range(w)] for _ in range(h)]
uf = UnionFind(h*w)

ans = []
q = int(input())
for i in range(q):
    trc = list(map(int, input().split()))
    if trc[0] == 1:
        r, c = trc[1] - 1, trc[2] - 1
        table[r][c] = 1
        if 0 <= r-1: 
            if table[r-1][c] == 1:
                uf.union(r*w+c, (r-1)*w+c)
        if r+1 < h:
            if table[r+1][c] == 1:
                uf.union(r*w+c, (r+1)*w+c)
        if 0 <= c-1: 
            if table[r][c-1] == 1:
                uf.union(r*w+c, r*w+(c-1))
        if c+1 < w:
            if table[r][c+1] == 1:
                uf.union(r*w+c, r*w+(c+1))
    else:
        ra, ca, rb, cb = trc[1] - 1, trc[2] - 1, trc[3] - 1, trc[4] - 1

        if uf.is_same(ra*w+ca, rb*w+cb) and table[ra][ca] == 1 and table[rb][cb] == 1:
            ans.append("Yes")
        else:
            ans.append("No")

print(*ans, sep="\n")            
        