MOD = 10**9+7
import fractions

def extgcd(a,b): #互いに素なa,bについて、a*x+b*y=1の一つの解
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

def mod_inv(a,mod): # (x/a)%MODをしたい時は x%MOD * mod_inv(a,MOD)%MOD
    x = extgcd(a,mod)[0]
    return (mod+x%mod)%mod


# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a%b)

# def lcm(a, b):
#     return a*b//gcd(a,b)

n = int(input())
a = list(map(int, input().split()))

lcm_ = a[0]
for i in range(1, n):
    lcm_ = lcm_ * a[i] // fractions.gcd(lcm_, a[i])

# lcm_ = a[0]
ans = 0
for i in range(0,n):
    # if lcm_ % a[i] != 0:
    #     lcm_new = lcm(lcm_, a[i])
    #     ans = ans*(lcm_new%MOD *mod_inv(lcm_,MOD)%MOD)
    #     lcm_ = lcm_new

    ans += lcm_%MOD * mod_inv(a[i], MOD)%MOD

print(ans%MOD)



 