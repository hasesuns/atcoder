import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, p = map(int, input().split())
a = list( map(int, input().split()))

for i in range(n):
    a[i] %=2

one = a.count(1)
zero = a.count(0)

ans=0

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

if p==0:
    for i in range(0,one+1,2):
        ans += cmb(one,i)*2**zero

else:
    for i in range(1,one+1,2):
        ans += cmb(one,i)*2**zero

print(ans)