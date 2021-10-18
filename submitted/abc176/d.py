from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)
# import numpy as np
# 答えの提出の時にi+1とj+1は忘れないように
h, w = map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]
ch, cw = map(int, input().split())
ch, cw = ch-1, cw-1
dh, dw = map(int, input().split())
dh, dw = dh-1, dw-1


ans = 0
for i in range(h):
    maze[i] = input()

INF = h*w
distance = [[INF for i in range(w)] for j in range(h)]

queue0 = deque()
queue0.append((ch,cw))
distance[ch][cw] = 0

queue1 = deque()

while queue0 or queue1:

    if queue0:
        y, x = queue0.popleft()
    elif queue1:
        y, x = queue1.popleft()

    for dy in range(-2, 3):
        for dx in range(-2, 3):
            ny, nx = y+dy, x+dx
            if dy == dx == 0: continue
            elif abs(dy) + abs(dx) == 1:
                if 0 <= nx < w and 0 <= ny < h:
                    if maze[ny][nx] != '#' and distance[ny][nx] > distance[y][x]:
                            queue0.append((ny, nx))
                            distance[ny][nx] = distance[y][x]
            else:
                if 0 <= nx < w and 0 <= ny < h:
                    if maze[ny][nx] != '#' and distance[ny][nx] > distance[y][x]+1:
                            queue1.append((ny, nx))
                            distance[ny][nx] = distance[y][x]+1


ans = distance[dh][dw]
if ans == INF:
    print(-1)
else:
    print(ans)

 