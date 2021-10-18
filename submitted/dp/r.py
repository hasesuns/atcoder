import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

import numpy as np

n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

p = 10 ** 9 + 7
A = np.array(A, dtype=object)

def mat_pow(A, k, p):
    ret = np.identity(len(A), dtype=object)
    while k > 0:
        if (k & 1):
            ret = ret @ A
            ret %= p
        A = A @ A
        A %= p
        k >>= 1

    return ret

A_k = mat_pow(A, k, p)
ans = A_k.sum() % p

print(ans)