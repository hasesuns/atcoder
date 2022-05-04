import sys

sys.setrecursionlimit(10 ** 9)
h, w = map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]

ans = 0
for i in range(h):
    maze[i] = input()

ans = -1

def dfs(y,x, distance, visited):
    global ans
    visited[y][x] = 1
    for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
        ny, nx = y+i, x+j
        if 0 <= nx < w and 0 <= ny < h:
            if ny == sy and nx == sx and distance >= 3:
                ans = max(ans, distance+1)

            if maze[ny][nx] != '#' and not visited[ny][nx]:
                dfs(ny, nx, distance+1, visited)

for i in range(h):
    for j in range(w):
        if maze[i][j] == ".":
            sy, sx = i, j
            visited = [[0 for _ in range(w)] for _ in range(h)]
            dfs(sy, sx, 0, visited)

print(ans)