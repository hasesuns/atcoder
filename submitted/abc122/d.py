import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
p = 10**9+7

n = int(input())

from functools import lru_cache
@lru_cache(None)
def dfs(v=0, parent=-1):# どこからきたかの情報を入れとく

    if v == n:
        return 1

    if parent[-3] == 'A' and parent[-1] == 'G':
        return sum([dfs(v+1, parent[-2:]+'A'), dfs(v+1, parent[-2:]+'G'), dfs(v+1,parent[-2:]+'T')])%p
    elif parent[-3:-1] == 'AG':
        return sum([dfs(v+1,parent[-2:]+'A'), dfs(v+1,parent[-2:]+'G'), dfs(v+1,parent[-2:]+'T')])%p
    elif parent[-2:] == 'AC':
        return sum([dfs(v+1,'ACA'), dfs(v+1,'ACC'), dfs(v+1,'ACT')])%p
    elif parent[-2:] == 'GA':
        return sum([dfs(v+1,'GAG'), dfs(v+1,'GAA'), dfs(v+1,'GAT')])%p
    elif parent[-2:] == 'AG':
        return sum([dfs(v+1,'AGA'), dfs(v+1,'AGG'), dfs(v+1,'AGT')])%p
    else:
        return sum([dfs(v+1, parent[-2:]+'A')%p, dfs(v+1,parent[-2:]+'G')%p, dfs(v+1,parent[-2:]+'C')%p, dfs(v+1,parent[-2:]+'T')%p])%p


ans = 0

agc = 'AGCT'

for i in range(4):
    for j in range(4):
        word = 'T' +agc[i] + agc[j]
        ans += dfs(2,word)%p

print(ans%p)