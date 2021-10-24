import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

TABLE_HEIGHT = 1001
TABLE_WIDTH = 1001
imos_table = [[0 for _ in range(TABLE_WIDTH)] for _ in range(TABLE_HEIGHT)]

n = int(input())

# 重みの加算
for i in range(n):
    x_lu, y_lu, x_rd, y_rd = map(int, input().split())
    imos_table[y_lu][x_lu] += 1
    imos_table[y_lu][x_rd] -= 1
    imos_table[y_rd][x_lu] -= 1
    imos_table[y_rd][x_rd] += 1

# 横方向の累積和
for y in range(TABLE_HEIGHT):
    for x in range(1, TABLE_WIDTH):
        imos_table[y][x] += imos_table[y][x-1]

# 縦方向の累積和
for y in range(1, TABLE_HEIGHT):
    for x in range(TABLE_WIDTH):
        imos_table[y][x] += imos_table[y-1][x]

    
ans = [0] * (n+1)
for y in range(TABLE_HEIGHT):
    for x in range(TABLE_WIDTH):
        score = imos_table[y][x]
        ans[score] += 1

print(*ans[1:], sep="\n")