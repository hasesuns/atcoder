import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

from itertools import accumulate
acc = [0] + a
acc = list(accumulate(acc))

suma = sum(a)

ans = float('inf')

for i in range(n):
    ans = min(abs( 2*acc[i]-suma  ),ans  )

print(ans)