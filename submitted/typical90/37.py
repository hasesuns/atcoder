class SegTree:
    def __init__(self, seq, segfunc=max, id_elem=-float("inf")):
        self.num_elem = len(seq)
        self.id_elem = id_elem
        self.vals = [self.id_elem] * self.num_elem + seq
        self.segfunc = segfunc
        for i in range(self.num_elem - 1, 0, -1):
            self.vals[i] = self.segfunc(self.vals[i << 1], self.vals[i << 1 | 1])

    def set(self, idx, val):
        idx += self.num_elem
        self.vals[idx] = val
        while idx > 1:
            idx >>= 1
            self.vals[idx] = self.segfunc(self.vals[idx << 1], self.vals[idx << 1 | 1])

    def get(self, left, right):  # 左閉右開区間
        left += self.num_elem
        right += self.num_elem
        v_left = self.id_elem
        v_right = self.id_elem
        while left < right:
            if left & 1:
                v_left = self.segfunc(v_left, self.vals[left])
                left += 1
            if right & 1:
                right -= 1
                v_right = self.segfunc(self.vals[right], v_right)
            left >>= 1
            right >>= 1
        return self.segfunc(v_left, v_right)

    def get_one(self, idx):
        """1つだけgetしたいときに定数倍高速化のために使う関数"""
        return self.vals[self.num_elem+idx]

import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

w, n = map(int, input().split())
lrv = [tuple(map(int,input().split())) for _ in range(n)]

dp = [-1] * (w+1)
dp[0] = 0
seg = SegTree(dp, segfunc=max, id_elem=-1)  # 定数倍高速化のためにflort("inf")を使わない

for w_min, w_max, v in lrv:
    for ww in range(w, -1, -1):
        ll = max(0, ww - w_max)
        rr = ww - w_min + 1
        if rr <= 0:
            break
        incoming = seg.get(left=ll, right=rr)
        if incoming == -1:
            continue
        current = seg.get_one(idx=ww)
        if current < incoming + v:
            seg.set(idx=ww, val=incoming + v)

ans = seg.get_one(w)
print(ans)