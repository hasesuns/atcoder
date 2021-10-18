import sys
sys.setrecursionlimit(10 ** 7)


h, w = map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]

ans = 0
for i in range(h):
    maze[i] = input()

INF = 1000
ans = 0

for sy in range(h):
    for sx in range(w):
        if maze[sy][sx] == '.':
            continue

        flg = 0
        for i in range(0, 4):
            nx, ny = sx + [1, 0, -1, 0][i], sy + [0, 1, 0, -1][i]
            if 0 <= nx < w and 0 <= ny < h:
                if maze[ny][nx] == '#':
                    flg = 1
        if flg == 0:
            print('No')
            exit()

print('Yes')