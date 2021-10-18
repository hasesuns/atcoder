import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, c = map(int, input().split())
a = list( map(int, input().split()))

ans = [n*(n+1)//2]*(c+1)

es = [[0] for i in range(c+1)]
for i in range(1,n+1):
    aa = a[i-1]
    tmp = i - es[aa][-1]
    ans[aa] -= tmp*(tmp-1)//2
    es[aa].append(i)

for i in range(1,c+1):
    tmp = (n+1) - es[i][-1]
    ans[i] -= tmp*(tmp-1)//2


print(*ans[1:],sep='\n')

 