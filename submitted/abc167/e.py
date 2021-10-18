import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m,k = map(int, input().split())


def nCr_mod_p(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 998244353
N = 2*10 ** 5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p), 0! = 1! = 1
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p), 0! = 1! = 1
inv = [0, 1]  # inv[n] = n^(-1) mod p, 0! = 1　だけど便宜上inv[0]=0にしてる

for i in range(2, N + 2):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans =0

for i in range(k+1):
    ans += m*pow(m-1,n-i-1,p)%p * nCr_mod_p(n-1,i,p)%p
print(ans%p)