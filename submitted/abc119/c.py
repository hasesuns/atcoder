import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, a, b, c = map(int, input().split())
l = list(int(input()) for i in range(n))

ans = 0
mpa = mpb = mpc = 0
mp = [0,0,0]
INF = 10**4

groups = [[]*n for _ in range(3)]

def dfs(groups, parent=-1):
    groupa = groups[0]
    groupb = groups[1]
    groupc = groups[2]

    if parent == n-1:
        if len(groupa) > 0:mpa = 10 * (len(groupa)-1) + abs(sum(groupa)-a)
        else: mpa = INF

        if len(groupb) > 0:mpb = 10 * (len(groupb)-1) + abs(sum(groupb)-b)
        else: mpb = INF

        if len(groupc) > 0:mpc = 10 * (len(groupc)-1) + abs(sum(groupc)-c)
        else: mpc = INF

        return mpa+mpb+mpc

    else:
        parent+=1

        addl = [l[parent]]

        adda = dfs([groupa+addl ,groupb, groupc], parent)
        addb = dfs([groupa, groupb+addl, groupc], parent)
        addc = dfs([groupa, groupb, groupc+addl], parent)
        noadd = dfs([groupa,groupb,groupc],parent)

        return min(adda, addb, addc, noadd)

print(dfs(groups))