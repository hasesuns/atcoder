import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


n, m,c = map(int, input().split())
b = list( map(int, input().split()))
ans = 0
for i in range(n):
    a = list( map(int, input().split()))
    tmp = 0
    for j in range(m):
        tmp += b[j]*a[j]
    if tmp + c > 0:
        ans+=1

print(ans)