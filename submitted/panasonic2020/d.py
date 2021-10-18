import sys
sys.setrecursionlimit(10 ** 7)
from functools import lru_cache

n = int(input())
ans = []

if n == 1:
    print('a')
    exit()

@lru_cache(None)
def rec(before, depth, MAX):
    for i in range(MAX-ord('a') +2):
        tmp = before + chr(ord('a') + i)
        if len(tmp) >= n:
            ans.append(tmp)
        else:
            MAX = max(MAX, ord(tmp[-1]) )
            rec(tmp, depth+1, MAX)


rec('a',1, ord('a'))

ans.sort()

print(*ans, sep ='\n')