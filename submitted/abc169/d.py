import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())


from collections import Counter
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

soinsu = prime_factorize(n)

sankaku = [1]*20

from bisect import bisect_right

for i in range(1,20):
    sankaku[i] = sankaku[i-1]+(i+1)

ans=0
for k,v in soinsu.items():
    index = bisect_right(sankaku,v)
    ans += index

print(ans)
 