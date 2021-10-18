import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

from collections import defaultdict

n = int(input())
d = defaultdict(list)
xy = [tuple(map(int,input().split())) for i in range(n-1)]

p = 10**9 +7

for x,y in xy:
    x,y = x-1, y-1
    d[x].append(y)
    d[y].append(x)

dp = [[1]*2 for _ in range(n+1)]

def dfs(now, prev):
    for next_ in d[now]:
        if next_ == prev:
            continue
        dfs(next_, now) #  子の方を先に埋めとく

        # 現在地を白で塗る
        dp[now][0] *= (dp[next_][0] + dp[next_][1])%p
        dp[now][0] %= p

        # 現在地を黒で塗る
        dp[now][1] *= dp[next_][0]%p
        dp[now][1] %= p

dfs(0, -1)

ans = (dp[0][0] + dp[0][1])%p
print(ans)