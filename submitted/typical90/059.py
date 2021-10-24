import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m, q = map(int, input().split())
xy = [tuple(map(int,input().split())) for _ in range(m)]
adj_list = [[] for _ in range(n)]
for x,y in xy:
    x, y = x - 1, y - 1
    adj_list[x].append(y)

# dp[i]: iに行ける頂点が対応するbitが1になっている整数
dp = [1 << start for start in range(n)]

# 今回はxi<yiが確定しているのでindexが小さい順に更新すれば良い
for from_ in range(n):
    for to in adj_list[from_]:
        dp[to] |= dp[from_] 

ab = [tuple(map(int,input().split())) for _ in range(q)]
for a,b in ab:
    a, b = a - 1, b - 1
    if dp[b] & (1 << a):
        print('Yes')
    else:
        print('No')