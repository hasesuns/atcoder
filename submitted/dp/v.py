import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

xy = [tuple(map(int,input().split())) for i in range(n-1)]
es = [[] for i in range(n)]
for i, (x,y) in enumerate(xy):
    x,y = x-1,y-1
    es[x].append(y)
    es[y].append(x)

parent_list = [-1] * n

dp_down = [1] * (n+1)
def dfs1(now, prev):
    prod = 1
    for next_ in es[now]:
        if next_ == prev:
            continue
        dfs1(next_, now)  # 帰りがけ順にしたいので子の方を先に埋めとく
        prod *= dp_down[next_] % m

        parent_list[next_] = now  # 後処理をやりやすくするために記録しておく
    dp_down[now] = prod + 1

dfs1(0, -1)  # 0を根とした木構造を考える


# 予め累積和（積）を計算
cumL = {}
cumR = {}
for v, v_next_list in enumerate(es):
    cumL[v] = [0, 1]
    for v_next in v_next_list:
        if parent_list[v] == v_next:
            cumL[v].append(cumL[v][-1])  # up側なので1つ飛ばす意味で直前の値を繰り返す
        else:
            cumL[v].append(cumL[v][-1] * dp_down[v_next] % m)

    cumR[v] = [0, 1]
    for v_next in reversed(v_next_list):
        if parent_list[v] == v_next:
            cumR[v].append(cumR[v][-1])  # up側なので1つ飛ばす意味で直前の値を繰り返す
        else:
            cumR[v].append(cumR[v][-1] * dp_down[v_next] % m)
    cumR[v] = cumR[v][::-1]


dp_up = [1] * (n+1)
def dfs2(now, prev):
    for i, next_ in enumerate(es[now]):
        if next_ == prev:
            continue
        prod = cumL[now][i+1] * cumR[now][i+1]
        dp_up[next_] = (prod * dp_up[now] + 1) % m
        dfs2(next_, now)

dfs2(0, -1)

for v in range(n):
    ans = 1
    for v_next in es[v]:
        if v_next == parent_list[v]:
            ans *= dp_up[v]
        else:
            ans *= dp_down[v_next]
        ans %= m
    print(ans)