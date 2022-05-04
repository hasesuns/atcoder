import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

import math
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

soinsu_dict = prime_factorize(n)

if len(soinsu_dict.keys()) == 1 and list(soinsu_dict.values())[0] == 1:
    ans = 0
else:
    sum_deg = sum(list(soinsu_dict.values()))
    ans = math.ceil(math.log2(sum_deg))

print(ans)