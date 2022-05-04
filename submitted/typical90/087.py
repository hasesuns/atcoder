import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, p, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def get_substituted_array(a, x):
    aa = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][j] == -1:
                aa[i][j] = aa[j][i] = x
            else:
                aa[i][j] = aa[j][i] = a[i][j]
    return aa


# 任意のペアに対して最短距離を求める（非負）
def warshall_floyd(dp):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp


def count_leq_p(cost, p):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if cost[i][j] <= p:
                cnt += 1
    return cnt


def isok_leq_k(ans):
    cost = warshall_floyd(get_substituted_array(a, ans))
    return count_leq_p(cost, p) <= k


INF = 10 ** 9
ok = INF
ng = 0
while ok - ng > 1:
    m = (ok + ng) // 2
    if isok_leq_k(m):
        ok = m
    else:
        ng = m
x_leq_k = ok


def isok_less_k(ans):
    cost = warshall_floyd(get_substituted_array(a, ans))
    return count_leq_p(cost, p) < k


ok = INF
ng = 0
while ok - ng > 1:
    m = (ok + ng) // 2
    if isok_less_k(m):
        ok = m
    else:
        ng = m
x_less_k = ok


if x_leq_k == INF:
    print(0)
elif x_less_k == INF:
    print("Infinity")
else:
    ans = x_less_k - x_leq_k  # xに対して経路は単調減少
    print(ans)