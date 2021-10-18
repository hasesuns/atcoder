import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
ab = [tuple(map(int,input().split())) for i in range(n-1)]

es = [[] for i in range(n)]
for i, (a,b) in enumerate(ab):
    a,b = a-1,b-1
    es[a].append((b, i))
    es[b].append((a, i))

visited = [0]*n
ans_color = [0]*(n-1)

# DFS
def dfs(v, fromColor):
    color = 1
    visited[v] = 1
    for to, i in es[v]:
        if visited[to]: continue

        if color == fromColor:
            color += 1
        ans_color[i] = color
        dfs(to, color)
        color += 1

root = 0 # 頂点1が存在することが問題文中で保証されてるからここを根ノードとしよう
dfs(root, 0)

print(max(ans_color))
print(*ans_color, sep='\n')