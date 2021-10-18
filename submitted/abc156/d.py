n, a, b = map(int, input().split())
p = 10**9+7

max_r = b

# nCrでnがでかすぎる時は直接O(r)で計算した方がいい
# 1<=n<=10**9, 1<=k<=10**7くらいのとき

def make_mod_inv(l,p): # lまでの逆元を作る
    mod_inv = [0, 1] + [0] * (l+3) # inv[n] = n^(-1) mod p, 0! = 1　だけど便宜上inv[0]=0にしてる
    for i in range(2, l+5):
        mod_inv[i] = -mod_inv[p % i] * (p // i) % p
    return mod_inv

mod_inv = make_mod_inv(max_r,p)

def NCr_mod_p(N, r, p):
    ret = 1
    for i in range(r):
        ret *= (N-i)%p
        ret *= mod_inv[i+1]
        ret %= p
    return ret

ans = pow(2,n,p) - 1 - NCr_mod_p(n,a,p) - NCr_mod_p(n,b,p)
print(ans%p)