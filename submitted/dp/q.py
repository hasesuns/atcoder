class SegTree:
    def __init__(self, seq, segfunc=max, id_elmnt=-float('inf')):
        self.N = len(seq)
        self.id_elmnt = id_elmnt
        self.X = [self.id_elmnt] * (self.N + self.N)
        self.segfunc = segfunc

        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.segfunc(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.segfunc(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.id_elmnt
        vR = self.id_elmnt
        while L < R:
            if L & 1:
                vL = self.segfunc(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.segfunc(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.segfunc(vL, vR)

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
h = list( map(int, input().split()))
a = list( map(int, input().split()))

dp = [0]*(n)
seg = SegTree(dp, segfunc=max, id_elmnt=-float('inf'))
h_order = list(sorted(range(len(h)), key=h.__getitem__))
for i in h_order:
    if h_order[i] == 0:
        dp[i] = a[i]
    else:
        dp[i] = seg.fold(0, i) + a[i]

    seg.set_val(i, dp[i])

ans = seg.fold(0, n)
print(ans)