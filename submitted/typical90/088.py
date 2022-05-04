import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

from collections import defaultdict

n, q = map(int, input().split())
a = list(map(int, input().split()))
xy = [tuple(map(int,input().split())) for _ in range(q)]

adj_list = [[] for _ in range(n)]
for i, (x,y) in enumerate(xy):
    x, y = x - 1, y - 1
    if x > y:
        adj_list[x].append(y)
    else:
        adj_list[y].append(x)

sum_dict = defaultdict(list)

def dfs(i, sum, selected_cards):
    if i == n: return
    global sum_dict, adj_list
    if len(set(adj_list[i]).intersection(selected_cards)) == 0:
        tmp_selected_cards = selected_cards + [i]
        tmp_sum = sum + a[i]
        if len(sum_dict[tmp_sum]) > 0:
            print(len(sum_dict[tmp_sum]))
            print(*[i+1 for i in sum_dict[tmp_sum]])
            print(len(selected_cards) + 1)
            print(*[i+1 for i in tmp_selected_cards])
            exit()
        sum_dict[tmp_sum] = tmp_selected_cards
        dfs(i+1, tmp_sum, tmp_selected_cards)
    dfs(i+1, sum, selected_cards)

dfs(0, 0, [])