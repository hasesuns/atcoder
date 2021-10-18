import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

def divisors(n):
    ret = set()
    m = 1
    while m*m <= n:
        if n%m==0:
            # ret.add(m)
            if n//m > m+1:
                ret.add(n//m)
        m += 1
    return ret
ndivs = list(divisors(n))

ans = sum(ndivs) - len(ndivs)*1

print(ans)