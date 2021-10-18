import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

from math import gcd
n = int(input())
a = list( map(int, input().split()))


g = 0
for aa in a:
    g = gcd(g,aa)
if g > 1:
    print('not coprime')
    exit()

MAXN = 10**6+10

def eratosthenes3(limit):
    sieve = [i for i in range(limit+1)]
    p = 2
    while p*p <= limit:
        if sieve[p] == p:
            for q in range(2*p,limit+1,p):
                if sieve[q] == q:
                    sieve[q] = p
        p += 1

    return sieve

sieve = eratosthenes3(MAXN)

st = set()
for aa in a:
    tmp = set()
    while aa > 1:
        tmp.add(sieve[aa])
        aa //= sieve[aa]
    for p in tmp:
        if p in st:
            print('setwise coprime')
            exit()
        st.add(p)
print('pairwise coprime')

 