import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

s = int(input())

def nCr_mod_p(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p), 0! = 1! = 1
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p), 0! = 1! = 1
inv = [0, 1]  # inv[n] = n^(-1) mod p, 0! = 1　だけど便宜上inv[0]=0にしてる

for i in range(2, N + 2):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

p = 10**9+7
ans =0

maxnum = -(-s//3)

for shikiri in range(maxnum):

    maru = s-(shikiri+1)*3
    if maru < 0: continue
    ans += nCr_mod_p(maru+shikiri,shikiri,p)
    ans %= p

print(ans%p)
 