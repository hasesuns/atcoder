import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
c = list( map(int, input().split()))
m = n - 1
adjacency = [[] for _ in range(n)]
ab = [tuple(map(int,input().split())) for _ in range(m)]
for a,b in ab:
    a,b = a-1,b-1
    adjacency[a].append(b)
    adjacency[b].append(a)

visited = [False] * n

def dfs(now):
    global ans
    global used_colors_cnt
    global visited

    if used_colors_cnt[c[now]] == 0:
        ans.append(now+1)
    visited[now] = True
    
    for next in adjacency[now]:
        if visited[next]: continue
        used_colors_cnt[c[now]] += 1
        dfs(now=next)
        used_colors_cnt[c[now]] -= 1

ans = []
used_colors_cnt = defaultdict(lambda: 0)
dfs(0)

print(*sorted(ans), sep="\n")