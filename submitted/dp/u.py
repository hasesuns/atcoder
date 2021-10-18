import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# dp[S] 集合Sをグループ分けした時の最大得点

score = [0] * (1<<n)

for T in range(1<<n):
    for i in range(n):
        for j in range(i+1, n):
            if (T >> i) & 1 == 1 and (T >> j) & 1 == 1:
                score[T] += a[i][j]

dp = [0] * (1<<n)  # 最終的な答えが少なくとも0点以上になることが確定しているので0による初期化で十分

for S in range(1<<n):
    T = S
    while T:
        dp[S] = max(dp[S], dp[S ^ T] + score[T])
        T = (T-1) & S

ans = dp[(1<<n) - 1]
print(ans)