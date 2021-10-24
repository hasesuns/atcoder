from bisect import bisect_left
from typing import List, Tuple


def make_compressed_list(val_list: List[float]):
    """座標圧縮したリストを返す。"""
    unique_val_list = list(set(val_list))
    unique_val_list.sort()

    compressed_val_list = [bisect_left(unique_val_list, val) for val in val_list]
    return compressed_val_list


class LIS:
    """LIS（最長増加部分列）をDPと二分探索を用いて求める"""

    def __init__(self, num_list, compress: bool = True):
        if compress:
            self.num_list = make_compressed_list(num_list)
        else:
            self.num_list = num_list

    def exec(self) -> Tuple[int, List[int], List[int]]:
        """[summary]

        Returns:
            max_len (int): self.nun_listの最長増加部分列の長さ
            length_list (List[int]):self.nun_listの先頭から各要素までにおける最長増加部分列の長さのリスト
            dp (List[int]): 各長さの増加部分列の最終要素の最小値のリスト
        """
        dp = [float("inf")] * (len(self.num_list) + 1)
        dp[0] = -1
        length_list = [-1] * len(self.num_list)
        for i, val in enumerate(self.num_list):
            length = bisect_left(dp, val)
            dp[length] = min(val, dp[length])
            length_list[i] = length
        max_len = max(length_list)
        return max_len, length_list, dp


import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

lis = LIS(a)
_, length_list, _ = lis.exec()

lis = LIS(a[::-1])
_, reverse_lis_list, _ = lis.exec()
reverse_lis_list = reverse_lis_list[::-1]

ans = 0
for i in range(n):
    ans = max(ans, length_list[i] + reverse_lis_list[i] - 1)

print(ans)