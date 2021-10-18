import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

p = 10**9+7
h, w, k = map(int, input().split())

if w == 1:
    print(1)
    exit()

d = [[0]*(w+1) for _ in range(h+1)]

d[0][0] = 1
# [i,j]を(i*0.5)行 (j+1)列 の地点とする
# dp[i][j]: [0][0]をスタートとした時の[i][j]に到達しうるあみだくじの総数

case = [1, 2, 3, 5, 8, 13, 21]

ans = 0
for i in range(1,h+1):
    for j in range(w):
        if i+1 <= j: continue
        # center to center
        d[i][j] += d[i-1][j]*case[max(0,w-j-2)] * case[max(0,j-1)]%p
        # left to right
        if j-1>=0:
            d[i][j] += d[i-1][j-1]* case[max(0,w-j-2)] * case[max(0,j-2)]%p
        # right to left
        if j+1<=w:
            d[i][j] += d[i-1][j+1]* case[max(0,w-j-3)] * case[max(0,j-1)]%p

print(d[h][k-1]%p)