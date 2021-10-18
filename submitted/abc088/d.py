from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)
# import numpy as np
# 答えの提出の時にi+1とj+1は忘れないように
h, w = map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]

ans = 0
count_wall = 0
for i in range(h):
    maze[i] = input()
    count_wall += maze[i].count('#')

INF = h*w
visited = [[0 for i in range(w)] for j in range(h)]
distance = [[INF for i in range(w)] for j in range(h)]

if maze[0][0]=='#':
    print(-1)
    exit()

sx=0
sy=0
queue = deque()
queue.append((sy,sx))
distance[sy][sx] = 0

while queue:
    y, x = queue.popleft()
    for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
        ny, nx = y+i, x+j
        if 0 <= nx < w and 0 <= ny < h:
            if maze[ny][nx] != '#' and distance[ny][nx] > distance[y][x]+1:
                    queue.append((ny, nx))
                    distance[ny][nx] = distance[y][x]+1

if distance[h-1][w-1] <INF:
    ans = h*w-count_wall- (distance[h-1][w-1]+1)
else:
    ans = -1
print(ans)