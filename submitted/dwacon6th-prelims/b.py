n = int(input())
x = list( map(int, input().split()))
MOD = 10**9 + 7

def make_mod_inv(l,p): # lまでの逆元を作る
    mod_inv = [0, 1] + [0] * (l+3) # inv[n] = n^(-1) mod p, 0! = 1　だけど便宜上inv[0]=0にしてる
    for i in range(2, l+5):
        mod_inv[i] = -mod_inv[p % i] * (p // i) % p
    return mod_inv

mod_inv = make_mod_inv(n-1,MOD)

ans = 0

factorial = 1
for i in range(2,n):
    factorial = (factorial * i%MOD) %MOD

p = [0]*(n-1)
p[0] = 1 * factorial%MOD

for i in range(1,n-1):
    p[i] = p[i-1] + factorial*mod_inv[i+1]
    p[i] %= MOD

for i in range(n-1):
    ans += (x[i+1]-x[i])%MOD*p[i]
    ans %= MOD

print(int(ans))