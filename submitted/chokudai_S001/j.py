import sys
from typing import List

class BinaryIndexedTree:
    """BinaryIndexedTree
    予め1-indexedにしたデータが入力されることを想定している。
    """
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, i: int, x):
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
    """座標圧縮したリストを返す。
    BITの前処理で使用することを想定している。
    """
    val2cval_dict = {val: i+1 for i, val in enumerate(sorted(val_list))}
    compressed_val_list = [val2cval_dict[val]  for val in val_list]
    return compressed_val_list


sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

a = make_compressed_list(a)  # 必要があれば座標圧縮しておく

bit = BinaryIndexedTree(size=n)
ans = 0
for i, a_i in enumerate(a):
    ans += i - bit.get_sum(a_i)  # 順序が転倒している要素の個数を加える
    bit.add(a_i, 1)

print(ans)