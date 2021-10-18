import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, q = map(int, input().split())
ab = [tuple(map(int,input().split())) for i in range(n-1)]
px = [tuple(map(int,input().split())) for i in range(q)]

es = [[] for i in range(n)]
for a,b in ab:
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a)

ans = [0]*n

# DFS for tree (再帰はpypyの方が遅かったりするので注意)
def dfs(v=0, parent=-1):# どこからきたかの情報を入れとく
    for to in es[v]:
        if to == parent: continue # 今回はcontinue

        ans[to] += ans[v]
        dfs(to, v)


for p, x in px:
    ans[p-1] += x

dfs(0)

print(*ans, sep=' ')