N, K = [int(_) for _ in input().split()]
import math
MOD = 10**9+7

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for i in range(1,K+1):
    try:
        print( (combinations_count(K-1,i-1)*combinations_count(N-K+1,i))%MOD )
    except:
        print(0)
        