import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n,m,x = map(int, input().split())
cas = [tuple(map(int,input().split())) for i in range(n)]

ans = float('inf')


for i in range(2 ** n):
    d = [0]*m
    tmp = 0
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            ca = cas[j]
            c= ca[0]
            for k,a in enumerate(ca[1:]):
                d[k]+=a
            tmp+=c

    if min(d)>=x:
        ans = min(ans,tmp)

if ans == float('inf'):
    print(-1)
else:
    print(ans)