import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

from itertools import accumulate

n = int(input())
s = input() #sys.stdin.readlineは最後が改行

p = 10 ** 9 + 7

dp = [[0] * n for _ in range(n)]  # i文字目までで条件を満たす通り数。ただしjはi番目の文字より小さいものが残りの数にいくつあるかを示す
for i in range(n):
    dp[0][i] = 1

# 累積和を使わない場合
# for i in range(n):
#     cum = [0] * n
#     for j in range(n-i-1):
#         if s[i] == '<':
#             for k in range(j+1):
#                 dp[i+1][j] += dp[i][k]
#         elif s[i] == '>':
#             for k in range(j+1, n):
#                 dp[i+1][j] += dp[i][k]


for i in range(n):
    cum = [0] + dp[i][:]
    cum = list(accumulate(cum))
    for j in range(n-i-1):
        if s[i] == '<':
            dp[i+1][j] = cum[j+1] % p 
        elif s[i] == '>':
            dp[i+1][j] = (cum[n] - cum[j+1]) % p

ans = dp[n-1][0] % p
print(ans)