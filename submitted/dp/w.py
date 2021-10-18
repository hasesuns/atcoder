import operator


class LazySegTree:
    """
    遅延評価セグメント木。
    Range Maximum Query and Range Add Query (RMQ and RAQ)に対応。
    https://tjkendev.github.io/procon-library/python/range_query/rmq_raq_segment_tree_lp.html をクラス化した。

    Attribute
    --------------
    INF: int
        初期化等に用いる無限大。
    LV: int
        Nを二進数表記したときの文字列の長さ。
    N0: int
        N以上で最小の2の累乗となる数。
    data: List[int]
        要素を保存するlist。
    lazy: List[int]
        作用素を保存するlist。

    """

    def __init__(self, N):
        self.INF = 2**31-1
        self.LV = (N-1).bit_length()
        self.N0 = 2**self.LV
        self.data = [0]*(2*self.N0)
        self.lazy = [0]*(2*self.N0)

    def gindex(self, l, r):
        L = (l + self.N0) >> 1; R = (r + self.N0) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range(self.LV):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1; R >>= 1

    def propagates(self, *ids):
        """遅延伝搬処理"""
        for i in reversed(ids):
            v = self.lazy[i-1]
            if not v:
                continue
            self.lazy[2*i-1] += v; self.lazy[2*i] += v
            self.data[2*i-1] += v; self.data[2*i] += v
            self.lazy[i-1] = 0

    def range(self, l, r, x, func_r=operator.add, func_q=max):
        """
        区間[l, r)にxを引数としたfuncの処理を行う。

        Parameters
        -------------
        func_r : builtin_function_or_method
            range()の中で行う処理を表す関数。
        func_q : builtin_function_or_method
            queryで指定される関数がminかmaxか指定。

        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        L = self.N0 + l; R = self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = func_r(self.lazy[R-1], x)
                self.data[R-1] = func_r(self.data[R-1], x)
            if L & 1:
                self.lazy[L-1] = func_r(self.lazy[L-1], x)
                self.data[L-1] = func_r(self.data[L-1], x)
                L += 1
            L >>= 1; R >>= 1
        for i in ids:
            self.data[i-1] = func_q(self.data[2*i-1], self.data[2*i])

    def query(self, l, r, func_q=max, ret=0):
        """
        区間[l, r)内の最大値・最小値を求める

        Parameters
        -----------
        func_q : builtin_function_or_method
            queryで行うしょりを表す関数。maxまたはmin。
        ret : int
            返り値の初期値

        """

        self.propagates(*self.gindex(l, r))
        L = self.N0 + l; R = self.N0 + r

        while L < R:
            if R & 1:
                R -= 1
                ret = func_q(ret, self.data[R-1])
            if L & 1:
                ret = func_q(ret, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return ret


import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

dp_seg = LazySegTree(n)
lra = [tuple(map(int,input().split())) for i in range(m)]

qry = [[] for i in range(n)]
for l, r, a in lra:
    l, r = l - 1, r - 1
    qry[r].append((l, a))  # 右端のインデックスごとに保存

for r in range(n):
    ma = dp_seg.query(0, r)
    dp_seg.range(r, r+1, ma)

    for l, a in qry[r]:
        dp_seg.range(l, r+1, a)


ans = dp_seg.query(0, n+1)

print(ans)