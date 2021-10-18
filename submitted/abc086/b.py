import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())

white_table = [[0] * k for _ in range(k)]
black_table = [[0] * k for _ in range(k)]

for i in range(n):
    x, y, c = input().split()
    xx = int(x) % (2*k)
    yy = int(y) % (2*k)

    if (xx >= k and yy < k) or (xx < k and yy >= k):
        if c == 'W':
            black_table[xx%k][yy%k] += 1
        else:
            white_table[xx%k][yy%k] += 1
    else:
        if c == 'W':
            white_table[xx%k][yy%k] += 1
        else:
            black_table[xx%k][yy%k] += 1

cs_w = [[0 for i in range(k+1)] for j in range(k+1)]
for i in range(k):
    for j in range(k):
        cs_w[i+1][j+1] = cs_w[i][j+1] + cs_w[i+1][j] - cs_w[i][j] + white_table[i][j]

cs_b = [[0 for i in range(k+1)] for j in range(k+1)]
for i in range(k):
    for j in range(k):
        cs_b[i+1][j+1] = cs_b[i][j+1] + cs_b[i+1][j] - cs_b[i][j] + black_table[i][j]

ans = 0
for i in range(1, k+1):
    for j in range(1, k+1):

        # 交点に対して左上と右下が黒ブロックで右上と左下が白ブロックとする。(i, j)は右上の白ブロックのスタートの座標。
        tmp = 0
        tmp += cs_w[k][k] - cs_w[i-1][k] - cs_w[k][j-1] + cs_w[i-1][j-1]  # 右上の白ブロック
        tmp += cs_w[i-1][j-1] - cs_w[i-1][0] - cs_w[0][j-1] + cs_w[0][0]  # 左下の白ブロック
        tmp += cs_b[i-1][k] - cs_b[0][k] - cs_b[i-1][j-1] + cs_b[0][j-1]  # 左上の黒ブロック
        tmp += cs_b[k][j-1] - cs_b[i-1][j-1] - cs_b[k][0] + cs_b[i-1][0]  # 右下の黒ブロック
        ans = max(ans, tmp)

        # 上の逆パターン
        tmp = 0
        tmp += cs_b[k][k] - cs_b[i-1][k] - cs_b[k][j-1] + cs_b[i-1][j-1]  # 右上の黒ブロック
        tmp += cs_b[i-1][j-1] - cs_b[i-1][0] - cs_b[0][j-1] + cs_b[0][0]  # 左下の黒ブロック
        tmp += cs_w[i-1][k] - cs_w[0][k] - cs_w[i-1][j-1] + cs_w[0][j-1]  # 左上の白ブロック
        tmp += cs_w[k][j-1] - cs_w[i-1][j-1] - cs_w[k][0] + cs_w[i-1][0]  # 右下の白ブロック
        ans = max(ans, tmp)

print(ans)