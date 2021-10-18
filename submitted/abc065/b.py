import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
x = [0]* n
y = [0]* n
for i in range(n):
    x[i], y[i] = map(int, input().split())

xi = [(i,x[i]) for i in range(n)]
yi = [(i,y[i]) for i in range(n)]

xi.sort(key=lambda x:x[1])
yi.sort(key=lambda x:x[1])

INF = float('inf')

# xycost = [[INF]*n for i in range(n)]
# for i in range(n-1):
#     xycost[xi[i][0]][xi[i+1][0]] = min(xycost[xi[i][0]][xi[i+1][0]], xi[i+1][1] -xi[i][1])
#     xycost[xi[i+1][0]][xi[i][0]] = min(xycost[xi[i+1][0]][xi[i][0]], xi[i+1][1] -xi[i][1])
#     xycost[yi[i][0]][yi[i+1][0]] = min(xycost[yi[i][0]][yi[i+1][0]], yi[i+1][1] -yi[i][1])
#     xycost[yi[i+1][0]][yi[i][0]] = min(xycost[yi[i+1][0]][yi[i][0]], yi[i+1][1] -yi[i][1])

xycost = []

for i in range(n-1):
    tmp = (xi[i][0], xi[i+1][0], xi[i+1][1] -xi[i][1])
    xycost.append(tmp)
    tmp = (yi[i][0], yi[i+1][0], yi[i+1][1] -yi[i][1])
    xycost.append(tmp)

xycost.sort(key=lambda x:x[2])

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

uf = UnionFind(n)
ans = 0
for i,j, cost in xycost:
    if not uf.is_same(i,j):
        uf.union(i,j)
        ans += cost
    if uf.size == n: break

print(ans)