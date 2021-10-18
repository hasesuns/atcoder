import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
b = list( map(int, input().split()))
d = [0]*n

for i in range(n):
    d[i] = a[i]-b[i]

d.sort()

if sum(d)<0:
    print(-1)
    exit()

cnt_neg = 0
for i in range(n):
    if d[i]<0:cnt_neg+=1

if cnt_neg==0:
    print(0)
    exit()
else:
    ans = cnt_neg

last=n-1
for neg in range(n):
    if d[neg]>=0:break

    while d[neg]<0:
        tmp = min(-d[neg], d[last])
        d[neg] += tmp
        d[last] -= tmp
        if d[last] == 0:
            last-=1
            ans+=1

if d[last] != a[last]-b[last] and d[last]!=0 : ans+=1

print(ans)