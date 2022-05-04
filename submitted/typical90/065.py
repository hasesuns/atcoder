import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

r, g, b, k = map(int, input().split())
x, y, z = map(int, input().split())
MOD = 998244353


class Combination:
    def __init__(self, n=10 ** 5, mod=10 ** 9 + 7):
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
        return self.fact[n] * self.factinv[r] % self.mod * self.factinv[n - r] % self.mod


class Convolution:
    def __init__(self, mod):
        self._primitive_root = self._calc_primitive_root(mod)

    def _calc_primitive_root(self, mod):
        typical_value_dict = {2: 1, 167772161: 3, 469762049: 3, 754974721: 11, 998244353: 3}
        if mod in typical_value_dict.keys():
            return typical_value_dict[mod]
        divs = [0] * 20
        divs[0] = 2
        cnt = 1
        x = (mod - 1) // 2
        while x % 2 == 0:
            x //= 2
        i = 3
        while i * i <= x:
            if x % i == 0:
                divs[cnt] = i
                cnt += 1
                while x % i == 0:
                    x //= i
            i += 2
        if x > 1:
            divs[cnt] = x
            cnt += 1
        g = 2
        while 1:
            ok = True
            for i in range(cnt):
                if pow(g, (mod - 1) // divs[i], mod) == 1:
                    ok = False
                    break
            if ok:
                return g
            g += 1

    def _ceil_pow2(self, n):
        assert n >= 0
        x = 0
        while (1 << x) < n:
            x += 1
        return x

    def _bsf(self, n):
        assert n >= 1
        return len(bin(n & -n)) - 3

    def _butterfly(self, a, mod):
        n = len(a)
        h = self._ceil_pow2(n)
        self.sum_e = [0] * 30
        es = [0] * 30
        ies = [0] * 30
        cnt2 = self._bsf(mod - 1)
        g = self._primitive_root
        e = pow(g, (mod - 1) >> cnt2, mod)
        ie = pow(e, mod - 2, mod)
        for i in range(cnt2, 1, -1):
            es[i - 2] = e
            ies[i - 2] = ie
            e *= e
            e %= mod
            ie *= ie
            ie %= mod
        now = 1
        for i in range(cnt2 - 2):
            self.sum_e[i] = (es[i] * now) % mod
            now *= ies[i]
            now %= mod
        for ph in range(1, h + 1):
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            now = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p] * now
                    a[i + offset] = (l + r) % mod
                    a[i + offset + p] = (l - r) % mod
                now *= self.sum_e[self._bsf(((1 << 32) - 1) ^ s)]
                now %= mod

    def _butterfly_inv(self, a, mod):
        n = len(a)
        h = self._ceil_pow2(n)
        self.sum_ie = [0] * 30
        es = [0] * 30
        ies = [0] * 30
        cnt2 = self._bsf(mod - 1)
        g = 3  # primitive_root ??
        e = pow(g, (mod - 1) >> cnt2, mod)
        ie = pow(e, mod - 2, mod)
        for i in range(cnt2, 1, -1):
            es[i - 2] = e
            ies[i - 2] = ie
            e *= e
            e %= mod
            ie *= ie
            ie %= mod
        now = 1
        for i in range(cnt2 - 2):
            self.sum_ie[i] = (ies[i] * now) % mod
            now *= es[i]
            now %= mod
        for ph in range(h, 0, -1):
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            inow = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p]
                    a[i + offset] = (l + r) % mod
                    a[i + offset + p] = ((l - r) * inow) % mod
                inow *= self.sum_ie[self._bsf(((1 << 32) - 1) ^ s)]
                inow %= mod

    def convolution_mod(self, a, b, mod):
        n, m = len(a), len(b)
        if n == 0 or m == 0:
            return []
        if min(n, m) <= 60:
            if n < m:
                a, b, n, m = b, a, m, n
            ans = [0] * (n + m - 1)
            for i in range(n):
                for j in range(m):
                    ans[i + j] += a[i] * b[j]
                    ans[i + j] %= mod
            return ans
        z = 1 << self._ceil_pow2(n + m - 1)
        a += [0] * (z - n)
        self._butterfly(a, mod)
        b += [0] * (z - m)
        self._butterfly(b, mod)
        for i in range(z):
            a[i] *= b[i]
            a[i] %= mod
        self._butterfly_inv(a, mod)
        a = a[: n + m - 1]
        iz = pow(z, mod - 2, mod)
        for i in range(n + m - 1):
            a[i] *= iz
            a[i] %= mod
        return a


comb = Combination(max([r, g, b]), MOD)
r_patterns = [comb.nCr_mod_p(r, i) if k - y <= i <= r else 0 for i in range(x + 1)]
g_patterns = [comb.nCr_mod_p(g, i) if k - z <= i <= g else 0 for i in range(x + 1)]
conv = Convolution(MOD)
rg_patterns = conv.convolution_mod(r_patterns, g_patterns, MOD)

ans = 0
for rg in reversed(range(x + 1)):
    b_ = k - rg
    if b_ > b:
        break
    ans += rg_patterns[rg] * comb.nCr_mod_p(b, b_)
    ans %= MOD

print(ans % MOD)