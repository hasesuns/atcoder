import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
h = list(int(input()) for i in range(n))

if n<3:
    print(n)
    exit()

nishi = False
s = 0
t = 0
u = 0
ans = 0

if h[0]<h[1]:
    nishi=True
    t=1
else:
    t=0
    u=1

for i in range(1,n-1):

    if nishi:
        if h[i] < h[i+1]:
            t=i+1
        else:
            nishi=False
            u = i+1

    else:
        if h[i] > h[i+1]:
                u=i+1
        else:
            nishi=True
            ans = max(ans, u-s+1)
            s = i
            t = i+1



u = n-1
ans = max(ans, u-s+1)

print(ans)