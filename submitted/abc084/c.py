import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
c = [0]*(n-1)
s = [0]*(n-1)
f = [0]*(n-1)

for i in range(n-1):
    c[i], s[i], f[i] = map(int, input().split())

from functools import lru_cache
@lru_cache(None)
def dfs(eki,t):
    if eki == n-1:
        return t

    cc = c[eki]
    ss = s[eki]
    ff = f[eki]

    if t <= ss:
        return dfs(eki+1, ss+cc)
    else:
        m = -(-t//ff)
        return dfs(eki+1, ff*m+cc)

for i in range(n):
    print(dfs(i,0))