import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
MOD = 10 ** 9 + 7

if n == 1:
    ans = k % MOD
else:
    ans = (k % MOD) * ((k - 1) % MOD)
    ans *= pow(k - 2, n - 2, MOD)

ans %= MOD
print(ans)