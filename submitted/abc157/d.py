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

    def members(self, x):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    def all_roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, m, k = map(int, input().split())
uf = UnionFind(n)
ab = [tuple(map(int,input().split())) for i in range(m)]
cd = [tuple(map(int,input().split())) for i in range(k)]
es1 = [[] for i in range(n)]
for i, (a,b) in enumerate(ab):
    a,b = a-1,b-1
    es1[a].append(b)
    es1[b].append(a)
    uf.union(a,b)

es_block_in_union = [[] for i in range(n)]
for i, (c,d) in enumerate(cd):
    c,d = c-1,d-1
    if uf.is_same(c,d):
        es_block_in_union[c].append(d)
        es_block_in_union[d].append(c)


ans = [0]*n
for i in range(n):
    ans[i] =  uf.size(i) - len(es_block_in_union[i])  - len(es1[i]) -1

print(*ans, sep=' ')