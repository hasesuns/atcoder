import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
p = 10007

a=[0]*max(n,3)
a[0]=0
a[1]=0
a[2]=1
for i in range(3,n):
    a[i] = a[i-1]%p+a[i-2]%p+a[i-3]%p

print(a[n-1]%p)