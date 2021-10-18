import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

k = int(input())
a = list( map(int, input().split()))

if a[-1]!=2:
    print(-1)
    exit()

ma = 2

for i in reversed(range(k)):
    ma = ma//a[i]*a[i] + (a[i]-1)

    if a[i] > ma:
        print(-1)
        exit()

mi = 2

for i in reversed(range(k)):

    mi = -(-mi//a[i])*a[i]

if mi > ma:
    print(-1)
    exit()

print(mi,ma)
 