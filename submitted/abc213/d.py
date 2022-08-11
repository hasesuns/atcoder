from collections import deque
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n - 1)]
adj_list = [[] for _ in range(n)]
for i, (a, b) in enumerate(ab):
    a, b = a - 1, b - 1
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(n):
    adj_list[i].sort()

ans = []

def dfs(now, prev=-1):
    ans.append(now + 1)
    for next in adj_list[now]:
        if next == prev:
            continue
        dfs(next, now)
        ans.append(now + 1)


dfs(0)
print(*ans)