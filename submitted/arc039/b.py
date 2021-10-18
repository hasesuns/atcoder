import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
p=10**9+7

if k>=n:
    cand = k%n

    # --- nCr mod p を求めるときに使う2（pは素数）（nが大きくてrがそんなに大きくないとき）
    def make_mod_inv(l,p): # lまでの逆元を作る
        mod_inv = [0, 1] + [0] * (l+3) # inv[n] = n^(-1) mod p, 0! = 1　だけど便宜上inv[0]=0にしてる
        for i in range(2, l+5):
            mod_inv[i] = -mod_inv[p % i] * (p // i) % p
        return mod_inv

    max_r = n-1
    mod_inv = make_mod_inv(max_r,p)

    def NCr_mod_p(N, r, p):
        ret = 1
        for i in range(r):
            ret *= (N-i)%p
            ret *= mod_inv[i+1]
            ret %= p
        return ret

    print(NCr_mod_p(n,cand,p))
else:
    nn = n-1+k
    def fur(n,r,mod):
        p,q = 1,1
        for i in range(r):
            p = p*(n-i)%mod
            q = q*(i+1)%mod
        return p * pow(q,mod-2,mod) % mod
    print(fur(nn,k,p))