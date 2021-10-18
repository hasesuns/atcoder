import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int,input().split())) for _ in range(n-1)]
adj_list = [[] for _ in range(n)]
for i, (a,b) in enumerate(ab):
    a, b = a - 1, b - 1
    adj_list[a].append(b)
    adj_list[b].append(a)

num_way = [-1] * n 

def dfs(now=0, prev=-1):
    num_way[now] = 1
    for next_v in adj_list[now]:
        if next_v == prev:
            continue
        if num_way[next_v] == -1:
            dfs(next_v, now)
        num_way[now] += num_way[next_v]

dfs(0)
ans = 0
for i in range(n):
    ans += num_way[i] * (n - num_way[i])
print(ans)