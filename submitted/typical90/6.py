import sys
from typing import List

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
s = input()[:-1]


def get_next_c_lists(s: str) -> List[List[int]]:
    """Sのi文字目以降で最初に文字cが登場するindexのリストnext_c_lists[i][c]を返す

    Args:
        s (str): [description]

    Returns:
        List[List[int]]: [description]
    """
    len_s = len(s)
    next_c_lists = [[len_s+1]*26 for _ in range(len_s+1)] 
    for i in reversed(range(len_s)):
        for j in range(26):
            if ord(s[i]) - ord("a") == j:
                next_c_lists[i][j] = i 
            else:
                next_c_lists[i][j] = next_c_lists[i+1][j]
         
    return next_c_lists

next_c_lists = get_next_c_lists(s)

ans = ""
now_idx = 0
for _ in range(k):
    for j in range(26):
        target_idx = next_c_lists[now_idx][j]
        num_can_use = len(s) - target_idx - 1  # target_idxを使った場合に残る文字
        num_must_use = k - len(ans) - 1  # target_idxを使った場合にさらに追加するべき文字
        if num_must_use <= num_can_use:
            # s[target_idx]の文字を使う
            ans += chr(j + ord("a"))
            now_idx = target_idx + 1
            break

print(ans)