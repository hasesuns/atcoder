import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
ab = [tuple(map(int,input().split())) for _ in range(m)]
adj_list = [[] for _ in range(n)]
for i, (a,b) in enumerate(ab):
    a, b = a - 1, b - 1
    adj_list[a].append(b)
    adj_list[b].append(a)

color_list = [1] * n

b = int((2*m)**0.5)
is_big_list = [len(adj_list[i])> b for i in range(n)]
adj_list_big = [[] for _ in range(n)]
for i, next_list in enumerate(adj_list):
    for next in next_list:
        if is_big_list[next]:
            adj_list_big[i].append(next)
last_update_query_list = [-1] * n

q = int(input())
xy = [tuple(map(int,input().split())) for _ in range(q)]

ans = [0] * q
for i, (x,y) in enumerate(xy):
    x -= 1
    if is_big_list[x]:
        ans[i] = color_list[x]
        color_list[x] = y
    else:
        last_update = last_update_query_list[x]
        for next in adj_list[x]:
            last_update = max(last_update, last_update_query_list[next])
        if last_update == -1:
            ans[i] = 1
        else:
            ans[i] = xy[last_update][1]
    last_update_query_list[x] = i

    for next in adj_list_big[x]:
        color_list[next] = y

print(*ans, sep="\n")