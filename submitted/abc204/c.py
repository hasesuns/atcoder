import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
adjacency_list = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    adjacency_list[a-1].append(b-1)

def dfs(now, visited):
    visited[now] = True
    for next in adjacency_list[now]:
        if visited[next]:
            continue
        dfs(next, visited)

ans = 0
for i in range(n):
    visited = [False] * n
    dfs(i, visited)
    ans += sum(visited)

print(ans)