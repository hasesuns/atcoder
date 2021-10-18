import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list( map(int, input().split()))
bci = [tuple(map(int,input().split())) for i in range(m)]


import itertools
ans=0
for sisters in itertools.combinations(range(n),9):
    tmp = 0
    for i in range(9):
        tmp+=a[sisters[i]]

    ss = set(sisters)

    for i in range(m):
        ii = [j-1 for j in bci[i][2:]]
        si= set(ii)
        if len(ss&si)>=3:
            tmp+=bci[i][0]
    ans = max(ans,tmp)

print(ans)

 