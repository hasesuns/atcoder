import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

from bisect import bisect_left
from typing import List


def make_compressed_list(val_list: List[float]):
    """座標圧縮したリストを返す。"""
    unique_val_list = list(set(val_list))
    unique_val_list.sort()

    compressed_val_list = [bisect_left(unique_val_list, val) for val in val_list]
    return compressed_val_list


n, k = map(int, input().split())
a = list(map(int, input().split()))
a = make_compressed_list(a)
ans = 0
count_list = [0] * len(a)
right = 0
num_type = 0
for left in range(n):
    while right < n and ((num_type <= k and count_list[a[right]] != 0) or (num_type < k and count_list[a[right]] == 0)):
        if count_list[a[right]] == 0:
            num_type += 1
        count_list[a[right]] += 1
        ans = max(ans, right - left + 1)
        right += 1
    if count_list[a[left]] == 1:
        num_type -= 1
    count_list[a[left]] -= 1

print(ans)