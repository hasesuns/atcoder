from collections import deque
from typing import NamedTuple


class LinearFunction(NamedTuple):
    """1次関数 ax+bを表す。"""
    a: float
    b: float

    def val_at(self, x: float) -> float:
        return self.a * x + self.b


class ConvexHullTrick:
    """傾きが単調現象 and xの値が単調増加を仮定したCHT"""

    def __init__(self):
        self.deq = deque()

    def check(self, f1: LinearFunction, f2: LinearFunction, f3: LinearFunction):
        """f1, f2, f3のうちf2が不要かどうかを返す。傾きaは単調減少を仮定。"""
        return (f2.a - f1.a) * (f3.b - f2.b) >= (f2.b - f1.b) * (f3.a - f2.a)

    def insert(self, lf: LinearFunction):
        """f(x)=ax+bを集合の一番最後に追加する。傾きaは単調減少を仮定。"""
        while len(self.deq) >= 2 and self.check(self.deq[-2], self.deq[-1], lf):
            self.deq.pop()
        self.deq.append(lf)

    def query(self, x: float) -> float:
        """直線群のxにおける最小値を返す。"""
        while len(self.deq) >= 2 and self.deq[0].val_at(x) >= self.deq[1].val_at(x):
            self.deq.popleft()
        return self.deq[0].val_at(x)


import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, c = map(int, input().split())
h = list( map(int, input().split()))

dp = [float("inf")] * n
dp[0] = 0

cht = ConvexHullTrick()

for i in range(1,n):
    a = - 2 * h[i-1]
    b = dp[i-1] + h[i-1]**2
    lf = LinearFunction(a, b)
    cht.insert(lf)

    min_lfpart = cht.query(h[i])  # 1次式の直線群の最小値で表現できる部分
    dp[i] = min_lfpart + h[i]**2 + c

ans = dp[n-1]

print(ans)