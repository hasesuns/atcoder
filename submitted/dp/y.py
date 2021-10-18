import sys
from typing import NamedTuple

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

h, w, n = map(int, input().split())
rc = [tuple(map(int,input().split())) for i in range(n)]
rc = sorted(rc, key=lambda x: x[0] + x[1])  # r+cが小さい順に並び替えて逆走だけは起きないようにする。移動可能不可能はあとで判定。
MOD = 10 ** 9 + 7

class Point(NamedTuple):
    y: int
    x: int

class Combination:

    def __init__(self, N=10**5, MOD=10**9+7):

        self.N = 2 * 10 ** 5  # N は必要分だけ用意する
        self.MOD = MOD
        self.fact = [1, 1]  # fact[n] = (n! mod p), 0! = 1! = 1
        self.factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p), 0! = 1! = 1
        self.inv = [0, 1]  # inv[n] = n^(-1) mod p, 0! = 1　だけど便宜上inv[0]=0にしてる

        for i in range(2, self.N + 2):
            self.fact.append(self.fact[-1] * i % self.MOD)
            self.inv.append((-self.inv[self.MOD % i] * (self.MOD // i)) % self.MOD)
            self.factinv.append((self.factinv[-1] * self.inv[-1]) % self.MOD)

    def nCr_mod_p(self, n, r):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] % self.MOD * self.factinv[n-r] % self.MOD

    def routes(self, p: Point, q: Point):
        x1, y1 = p.x, p.y
        x2, y2 = q.x, q.y

        if x2 < x1 or y2 < y1:  # 移動不可能なものを弾く
            return 0

        return self.nCr_mod_p((y2-y1)+(x2-x1), y2-y1)

dp = [[0] * 2 for _ in range(n+1)]  # dp[i][p]:通った壁の個数の偶奇をpとしてi番目の点に到る場合の通り数
dp[0][0] = 1  # 最初のスタートは壁ではないので偶奇は0

rc = [(1, 1)] + rc  # スタートのマスを追加

cmb = Combination(2*10**5)

for i in range(1, n+1):
    wall_i = Point(rc[i][0], rc[i][1])
    for j in range(i):
        wall_j = Point(rc[j][0], rc[j][1])
        dp[i][0] += dp[j][1] * cmb.routes(wall_j, wall_i) % MOD
        dp[i][0] %= MOD
        dp[i][1] += dp[j][0] * cmb.routes(wall_j, wall_i) % MOD
        dp[i][1] %= MOD

ans_bar = 0
g = Point(h, w)  # ゴールのマス
for i in range(1, n+1):
    wall_i = Point(rc[i][0], rc[i][1])
    ans_bar -= dp[i][0] * cmb.routes(wall_i, g) % MOD
    ans_bar += dp[i][1] * cmb.routes(wall_i, g) % MOD
    ans_bar %= MOD

s = Point(rc[0][0], rc[0][1])  # スタートのマス
ans = (cmb.routes(s, g) % MOD - ans_bar) % MOD

print(ans)