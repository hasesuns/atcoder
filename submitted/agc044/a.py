import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

t = int(input())

nabcd = [tuple(map(int,input().split())) for i in range(t)]

INF = float('inf')
from functools import lru_cache

for n,a,b,c,d in nabcd:

    @lru_cache(None)
    def dfs(now):
        if now == 0:
            return 0
        elif now == 1:
            return d
        elif now == 2:
            return min(d+a, d*2)
        elif now <0:
            return INF

        tmp = now*d

        # over 2
        sho = now//2+1
        fusoku = sho*2 - now
        over2 = dfs(sho)+d*fusoku+a

        # not over 2
        sho = now//2
        amari = now-sho*2
        nver2 = dfs(sho)+d*amari+a

        # over 3
        sho = now//3+1
        fusoku = sho*3 - now
        over3 = dfs(sho)+d*fusoku+b

        # not over 3
        sho = now//3
        amari = now-sho*3
        nver3 = dfs(sho)+d*amari+b

        # over 5
        sho = now//5+1
        fusoku = sho*5 - now
        over5 = dfs(sho)+d*fusoku+c

        # not over 5
        sho = now//5
        amari = now-sho*5
        nver5 = dfs(sho)+d*amari+c

        return min(tmp,over2,nver2,over3,nver3,over5,nver5)

    ans = dfs(n)
    print(ans)