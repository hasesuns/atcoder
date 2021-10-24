import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, l = map(int, input().split())

MOD = 10**9 + 7
# dp[i]:i番目にたどり着く移動方法の通り数
dp = [0 for _ in range(n+1)]
dp[0] = 1

for i in range(1,n+1):
    for j in [1, l]:
        if i-j>=0:
            dp[i] +=dp[i-j]
            dp[i] %= MOD
    
ans = dp[n]
print(ans)