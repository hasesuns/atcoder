import sys
from collections import defaultdict
from itertools import accumulate
from typing import List

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


class BinaryIndexedTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = defaultdict(lambda: 0)

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get_sum(self, i: int):
        sum_0toi = 0
        while i > 0:            
            sum_0toi += self.tree[i]
            i -= i & -i
        return sum_0toi


def make_compressed_list(val_list: List[float]):
    val2cval_dict = {val: i+1 for i, val in enumerate(sorted(val_list))}
    compressed_val_list = [val2cval_dict[val]  for val in val_list]
    return compressed_val_list


n, k = map(int, input().split())
a = list(int(input()) for _ in range(n))

acc_list = [0] + a
acc_list = list(accumulate(acc_list))

val_list = []
for i, acc in enumerate(acc_list):
    val_list.append(acc - k*i)

compressed_val_list = make_compressed_list(val_list)
    
bit = BinaryIndexedTree(size=n+1)
ans = 0
for i, cval in enumerate(compressed_val_list):
    ans += bit.get_sum(cval)  # 転倒していないものを数える
    bit.add(cval, 1)
print(ans)