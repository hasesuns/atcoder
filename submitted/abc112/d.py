import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

max_cand = m//n

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


divs = make_divisors(m)
divs.sort()

from bisect import bisect_right

index = bisect_right(divs, max_cand)

print(divs[index-1])