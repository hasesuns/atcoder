import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

MOD = 10 ** 9 + 7
n = int(input())

ans = 1
for i in range(n):
    a = map(int, input().split())
    ans *= sum(a) % MOD
print(ans % MOD)