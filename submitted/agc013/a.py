import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

ans=0
up = 0

for i in range(n-1):
    if a[i] < a[i+1]:
        if up == -1:
            ans+=1
            up=0
        elif up==0:
            up=1
    elif a[i] > a[i+1]:
        if up == 1:
            ans+=1
            up=0
        elif up==0:
            up=-1

ans+=1
print(ans)