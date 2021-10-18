import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

ans = 0

suma = sum(a)

for i in range(n):
    a_ = a[i]
    ans += n * a_**2

ans -= suma**2

print(ans)