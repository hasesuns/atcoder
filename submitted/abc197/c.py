import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
a = list( map(int, input().split()))
or_chunck_dict = defaultdict(lambda: None)
ans = float("inf")

def dfs(now, xor_tmp):
    global ans
    if now == n:
        ans = min(ans, xor_tmp)
        return

    for i in range(now, n):
        if or_chunck_dict[(now, i)]:
            or_chunck = or_chunck_dict[(now, i)]
        else:
            or_chunck = 0
            for j in range(now, i+1):
                or_chunck |= a[j]
            or_chunck_dict[(now, i)] = or_chunck

        dfs(i+1, xor_tmp ^ or_chunck)

dfs(0, 0)

print(ans)