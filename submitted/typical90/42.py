import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

k = int(input())
MOD = 10**9 + 7

if k % 9 != 0:
    print(0)
    exit()

# dp[i] 各桁の数字の和がiの時の通り数
dp = [0] * (k+1)
dp[0] = 1
for i in range(1, k+1):
    for j in range(1, 10):
        if i - j >= 0:
            dp[i] += dp[i-j] % MOD

ans = dp[k] % MOD
print(ans)