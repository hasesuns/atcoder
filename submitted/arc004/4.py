import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
p = 10**9+7

if m==1:
    print(1)
    exit()

nabs = abs(n)

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

import collections

c = collections.Counter(prime_factorize(nabs))

def nCr_mod_p(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 5+100  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p), 0! = 1! = 1
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p), 0! = 1! = 1
inv = [0, 1]  # inv[n] = n^(-1) mod p, 0! = 1　だけど便宜上inv[0]=0にしてる

for i in range(2, N + 2):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans=1
for val in c.values():
    nn = val + (m-1)
    ans *= nCr_mod_p(nn,m-1,p)
pn = (2**m)//2
ans*= pn%p
print(ans%p)
 