import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = [[0] * (n + 1) for _ in range(n + 1)]
p = 10**9 + 7

bitcnt = [0] * 2**n

ans = 0
for i in range(n):
    a[i] = list(map(int, input().split()))

dp = [0] * (2**n + 1)
dp[0] = 1
for s in range(1, 2**n):
    bitcnt[s] = bitcnt[s//2] + s % 2
    i_male = bitcnt[s] - 1
    for j_female in range(n):
        if (s >> j_female) & 1 == 0:
            continue
        else:
            # 部分集合sからj_femaleを除いた部分集合を考える
            dp[s] += dp[s - (1 << j_female)] * a[i_male][j_female]%p
            dp[s] %= p

print(dp[2**n - 1]%p) #  11111...11