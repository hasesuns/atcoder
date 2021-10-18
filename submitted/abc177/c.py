import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
p = 10**9+7
ans = 0

suma = sum(a)
sumaa1 = (suma**2//2)%p

sumaa2 = 0
for i in range(n):
    sumaa2 += (a[i]**2)
sumaa2 = sumaa2//2

ans = (sumaa1-sumaa2)%p

print(ans)