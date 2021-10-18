import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, p = map(int, input().split())

from collections import Counter;
def prime_factorize(n):
    d = Counter()
    m = 2
    while m*m <= n:
        while n%m == 0:
            n //= m
            d[m] += 1
        m += 1
    if n > 1:
        d[n] += 1
    return d

soinsu = prime_factorize(p)

ans =1
for k,v in soinsu.items():
    if v>=n:
        ans *= k**(v//n)

print(ans)