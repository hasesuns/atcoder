import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
a.sort()

from itertools import accumulate
acc = [0]+a
acc = list(accumulate(acc))

mi = 0
for i in reversed(range(1,n)):
    if acc[i]*2 < a[i]:
        mi = i
        break

print(n-mi)