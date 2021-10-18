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


n, m = map(int, input().split())
a = list( map(int, input().split()))

uf = UnionFind(n)

xy = [tuple(map(int,input().split())) for i in range(m)]
for i, (x,y) in enumerate(xy):
    uf.union(x,y)

ans = 0
arr_a = []

cnt_group = n - m

from collections import defaultdict
root2a_dict = defaultdict(lambda: [])

for i in range(n):
    root = uf.root(i)
    root2a_dict[root].append(a[i])

for k, v in root2a_dict.items():
    v.sort()
    ans += v[0]
    arr_a += v[1:]

arr_a.sort()

if cnt_group == 1:
    print(0)
    exit()
elif len(arr_a) < 2*(cnt_group-1)-cnt_group:
    print('Impossible')
    exit()

ans += sum(arr_a[:2*(cnt_group-1)-cnt_group])

print(ans)
 