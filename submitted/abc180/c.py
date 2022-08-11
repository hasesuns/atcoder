import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

def divisors(n): #ソートはしてない
    ret = set()
    m = 1
    while m*m <= n:
        if n%m==0:
            ret.add(m)
            ret.add(n//m)
        m += 1
    return ret
ans = sorted(list(divisors(n)))

print(*ans, sep="\n")