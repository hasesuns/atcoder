import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
c = list(input().split())
ab = [tuple(map(int,input().split())) for _ in range(n-1)]
p = 10**9 +7

adj_list = defaultdict(list)

for a,b in ab:
    a, b = a - 1, b - 1
    adj_list[a].append(b)
    adj_list[b].append(a)

# dp[now][state]: 全体が条件を満たしうるようにカットしていくときのnow以下の部分木カットの通り数
# state: 0 => only "a", 1 => only "b", 2 => both
dp = [[0]*3 for _ in range(n)]


def dfs(now, prev):

    tmp_one = 1
    tmp_both = 1

    for next in adj_list[now]:
        if next == prev:
            continue
        dfs(next, now) # 子の方を先に埋めとく

        if c[now] == "a":
            tmp_one *= (dp[next][0] # 切断しない
                        + dp[next][2]) # 切断する
            tmp_one %= p
        if c[now] == "b":
            tmp_one *= (dp[next][1] # 切断しない
                        + dp[next][2]) # 切断する
            tmp_one %= p
        tmp_both *= (dp[next][0] # 切断しない
                        + dp[next][1] # 切断しない
                        + 2 * dp[next][2]) # 両方
        tmp_both %= p

    if c[now] == "a":
        dp[now][0] = tmp_one
    if c[now] == "b":
        dp[now][1] = tmp_one
    dp[now][2] = (tmp_both - tmp_one) % p

dfs(0, -1)

ans = dp[0][2]
print(ans)