import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = [0]* n
b = [0]* n
c= [(0,0)]*n
for i in range(n):
    a[i], b[i] = map(int, input().split())
    c[i] = (i, a[i]+b[i] )

c.sort(key=lambda x:x[1],reverse=True)

ans = 0
for i in range(n):
    if i%2==0:
        ans+=a[c[i][0]]
    else:
        ans-=b[c[i][0]]

print(ans)