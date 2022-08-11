import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
s = input()[:-1]
w = list(map(int, input().split()))

from bisect import bisect_left
from typing import List
def compressed_val_list(val_list: List[float]):
    """座標圧縮したリストを返す。"""
    unique_val_list = list(set(val_list))
    unique_val_list.sort()

    compressed_val_list = [bisect_left(unique_val_list, val) for val in val_list]
    return compressed_val_list

w = compressed_val_list(w)
import collections
c = collections.Counter(w)

human = []
for i in range(n):
    if s[i] == "0":
        human.append((w[i], 0))
    else:
        human.append((w[i], 1))

human.sort(key=lambda x:x[0])

num_child = s.count("0")
ans = n - num_child
tmp = ans

cnt_ad = 0
cnt_ch = 0
for index, (ww, is_adult) in enumerate(human):

    if index + 1 < n:
        if ww == human[index+1][0]:
            if is_adult:
                cnt_ad += 1
            else:
                cnt_ch += 1
            continue
        elif cnt_ad > 0 or cnt_ch > 0:
            if is_adult:
                cnt_ad += 1
            else:
                cnt_ch += 1
            tmp -= cnt_ad
            tmp += cnt_ch
            ans = max(ans, tmp)

            cnt_ad = 0
            cnt_ch = 0
            continue

    if is_adult:
        tmp -= 1
    else:
        tmp += 1
    ans = max(ans, tmp)

ans = max(ans, num_child)

print(ans)