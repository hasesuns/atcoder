import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
p=10**9+7
n, m = map(int, input().split())
a = list(int(input()) for i in range(m))

safe = [1]*(n+1)
for aa in a:
    safe[aa]=0

dp = [0]*(n+1)
dp[0] = 1

if safe[1]:dp[1]=1

for i in range(2,n+1):
    if not safe[i]:
        continue

    dp[i] = dp[i-1]%p+dp[i-2]%p

print(dp[-1]%p)