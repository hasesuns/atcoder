import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


class Combination:

    def __init__(self, n=10**5, mod=10**9+7):

        self.n = 2 * 10 ** 5  # n は必要分だけ用意する
        self.mod = mod
        self.fact = [1, 1]  # fact[n] = (n! mod p), 0! = 1! = 1
        self.factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p), 0! = 1! = 1
        self.inv = [0, 1]  # inv[n] = n^(-1) mod p, 0! = 1　だけど便宜上inv[0]=0にしてる

        for i in range(2, self.n + 2):
            self.fact.append(self.fact[-1] * i % self.mod)
            self.inv.append((-self.inv[self.mod % i] * (self.mod // i)) % self.mod)
            self.factinv.append((self.factinv[-1] * self.inv[-1]) % self.mod)

    def nCr_mod_p(self, n, r):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] % self.mod * self.factinv[n-r] % self.mod


n = int(input())
MOD = 10 **9 + 7
comb = Combination(n=10**5, mod=MOD)
for k in range(1, n+1):
    ans = 0
    max_num_pick = - (-n // k)
    for num_pick in range(1, max_num_pick+1):
        ans += comb.nCr_mod_p(n-(k-1)*(num_pick-1), num_pick)
        ans %= MOD
    print(ans)