import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, x = map(int, input().split())
a = list( map(int, input().split()))

if x ==0:
    print(sum(a))
    exit()

ans = 0

if a[0]>x:
    ans += a[0]-x
    a[0]=x

for i in range(1,n):
    two = a[i-1]+a[i]
    if two > x:
        tmp = two-x
        ans += tmp
        if tmp > a[i]: a[i]=0
        else: a[i] = a[i]-tmp

print(ans)