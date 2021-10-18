import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, p, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    amari0 = a[i]
    for j in range(i+1, n):
        amari1 = amari0 * a[j] % p
        for k in range(j+1, n):
            amari2 = amari1 * a[k] % p
            for l in range(k+1, n):
                amari3 = amari2 * a[l] % p
                for m in range(l+1, n):
                    amari4 = amari3 * a[m] % p
                    if amari4 == q:
                        ans += 1

print(ans) 