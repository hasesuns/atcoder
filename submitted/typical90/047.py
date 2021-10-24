from math import gcd
from random import randint
from typing import List


class RollingHash:
    """ローリングハッシュ
    """
    def __init__(self, s: List[str], base: int = -1, min_base: int = ord("Z") + 1, use_primitive_base: bool = True):
        """ローリングハッシュの初期化

        Args:
            s (str): [description]
            base (int, optional): [description]. Defaults to -1.
            min_base (int, optional): [description]. Defaults to ord("Z")+1.
            use_primitive_base (bool, optional): [description]. Defaults to False.
        """
        MOD = 10 ** 9 + 7
        self.mod = MOD
        self.min_base = min_base

        if base != -1:
            self.base = base
        elif use_primitive_base:
            self._set_primitive_base_number()
        else:
            self.base = randint(min_base, MOD-1)
        
        l = len(s)
        self.pw = pw = [1] * (l + 1)
        self.h = h = [0] * (l + 1)
        v = 0
        for i in range(l):
            h[i + 1] = v = (v * self.base + ord(s[i])) % self.mod
        v = 1
        for i in range(l):
            pw[i + 1] = v = v * self.base % self.mod

    def _set_primitive_base_number(self) -> int:
        """原始根を利用した利用した基数をsetする

        Returns:
            int: [description]
        """
        root_0 = 3  # 3は2^61-1の原始根になることが知られている
        k = randint(1, 38)  # 38は3^k < 2^61 - 1 を満たす最大の整数
        while True:
            if k == 39:
                k = 1
                continue

            if gcd(k, self.mod) != 1:
                k += 1
                continue
            base = root_0 ** k % self.mod

            if base < self.min_base:
                k += 1
                continue
            
            self.base = base
            return self.base

    def get(self, l: int, r: int) -> int:
        """self.sの部分文字列のハッシュ値を計算して返す
        lとrは左閉右開区間を想定している。

        Args:
            l (int): [description]
            r (int): [description]

        Returns:
            int: [description]
        """
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod

import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
s = input()[:-1]
t = input()[:-1]

t_gb = []
t_br = []
t_rg = []

for tt in list(t):
    if tt == "R":
        t_gb.append("R")
        t_br.append("B")
        t_rg.append("G")

    elif tt == "G":
        t_gb.append("B")
        t_br.append("G")
        t_rg.append("R")

    elif tt == "B":
        t_gb.append("G")
        t_br.append("R")
        t_rg.append("B")

s_rh = RollingHash(s, base=1007)
t_rh_gb = RollingHash(t_gb, base=s_rh.base)
t_rh_br = RollingHash(t_br, base=s_rh.base)
t_rh_rg = RollingHash(t_rg, base=s_rh.base)

ans = 0
for k in range(-n + 1, n):
    if k <= 0:
        sk_hash = s_rh.get(l=-k, r=n)
        tk_hash_gb = t_rh_gb.get(l=0, r=n + k)
        tk_hash_br = t_rh_br.get(l=0, r=n + k)
        tk_hash_rg = t_rh_rg.get(l=0, r=n + k)

    else:
        sk_hash = s_rh.get(l=0, r=n - k)
        tk_hash_gb = t_rh_gb.get(l=k, r=n)
        tk_hash_br = t_rh_br.get(l=k, r=n)
        tk_hash_rg = t_rh_rg.get(l=k, r=n)

    if sk_hash in [tk_hash_gb, tk_hash_br, tk_hash_rg]:
        ans += 1

print(ans)