import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list( map(int, input().split()))

dp = [False]*(k+1)  # FalseならばSecondが勝ち，TrueならばFirstの勝ち
dp[0] = False

for i in range(k+1):
    for j in range(n):
        if i - a[j] >= 0:
            dp[i] |= not dp[i-a[j]]  # 負けを相手に渡したいのでnot。1つでも勝利ルートがあればいいのでorを取る。


if dp[k]:
    print('First')
else:
    print('Second')