import math
MOD = 10**9 + 7 #　素数
x, y = map(int, input().split())

if (x+y)%3 != 0:
    print(0)
    exit()

if x == 0 or y == 0:
    print(0)
    exit()

X = max(x,y)
Y = min(x,y)

all_move = (X+Y)//3
diff = (X-Y)
Y_move = (all_move - diff)//2


def mod_cmb(n, r, mod): # nCr mod p
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]

    for i in range( 2, n + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )

    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

print(mod_cmb(all_move, Y_move,MOD))