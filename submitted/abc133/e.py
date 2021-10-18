import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())

if n==1:
    print(k)
    exit()

ab = [tuple(map(int,input().split())) for i in range(n-1)]
p=10**9+7
es = [[] for i in range(n)]
for i, (a,b) in enumerate(ab):
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a)

d = [1]*n
for i in range(1,n):
    d[i] *= d[i-1]*max(0,(k-1-i))%p
    d[i] %=p

root=0
ans = k
for i in range(n):
    if i == root:
        ans *= (k-1)*d[len(es[i])-1]%p
    else:
        ans *= d[len(es[i])-1]%p

print(ans%p)

 