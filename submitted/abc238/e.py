import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, q = map(int, input().split())
lr = [tuple(map(int, input().split())) for _ in range(q)]

adj_list = [[] for _ in range(n + 1)]
for l, r in lr:
    l -= 1
    adj_list[l].append(r)
    adj_list[r].append(l)

visited_list = [False] * (n + 1)


def dfs(now):
    if now == n:
        print("Yes")
        exit()
    visited_list[now] = True
    for next in adj_list[now]:
        if visited_list[next]:
            continue
        dfs(next)


dfs(0)

print("No")