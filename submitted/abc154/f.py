r1,c1,r2,c2 = map(int, input().split())

def nCr_mod_p(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 2*10 ** 6 + 10  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p), 0! = 1! = 1
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p), 0! = 1! = 1
inv = [0, 1]  # inv[n] = n^(-1) mod p, 0! = 1　だけど便宜上inv[0]=0にしてる

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

sum22 = nCr_mod_p(r2+1+c2+1,r2+1,p) - 1
sum21 = nCr_mod_p(r2+1+c1,r2+1,p) - 1
sum12 = nCr_mod_p(r1+c2+1,c2+1,p) - 1
sum11 = nCr_mod_p(r1+c1,c1,p) - 1

ans = sum22 - sum21 - sum12 + sum11
ans %= p

print(ans)