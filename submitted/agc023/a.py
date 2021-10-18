import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))


from itertools import accumulate
acc = [0] + a
acc = list(accumulate(acc))

import collections

c = collections.Counter(acc)

ans = 0
for key,val in c.items():
    if val>1:
        ans +=val*(val-1)//2

print(ans)