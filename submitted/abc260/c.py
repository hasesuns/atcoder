import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, x, y = map(int, input().split())


def dfs(r_lev, r_num, b_lev, b_num):
    if r_lev <= 1 and b_lev <= 1:
        return b_num

    tmp = 0
    if r_lev > 1:
        tmp += dfs(r_lev-1, r_num, r_lev, r_num * x)
    if b_lev > 1:
        tmp += dfs(b_lev-1, b_num, b_lev - 1, b_num * y)
    return tmp

ans = dfs(n, 1, n, 0)
print(ans)