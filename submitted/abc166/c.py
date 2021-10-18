n, m = map(int, input().split())
h = list( map(int, input().split()))

ab = [tuple(map(int,input().split())) for i in range(m)]
es = [[] for i in range(n)]
for i, (a,b) in enumerate(ab):
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a) #無向グラフ

ans = 0
for i in range(n):
    ma = h[i]
    if es[i] == []:
        ans+=1
    else:
        for aa in set(es[i]):
            if ma <= h[aa]:
                break
        else:
            ans+=1

print(ans)