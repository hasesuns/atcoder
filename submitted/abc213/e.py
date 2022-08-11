import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)

h, w = map(int, input().split())
maze = [[-1 for _ in range(w)] for _ in range(h)]

ans = 0
for i in range(h):
    maze[i] = input()

INF = h * w
distance = [[INF for _ in range(w)] for _ in range(h)]

queue0 = deque()
queue1 = deque()

sx, sy = 0, 0
queue0.append((sx, sy))
distance[sy][sx] = 0

while queue0 or queue1:

    if queue0:
        y, x = queue0.popleft()
    elif queue1:
        y, x = queue1.popleft()

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            ny, nx = y + dy, x + dx
            if abs(dy) + abs(dx) == 1 and 0 <= nx < w and 0 <= ny < h:
                if maze[ny][nx] != "#" and distance[ny][nx] > distance[y][x]:
                    queue0.append((ny, nx))
                    distance[ny][nx] = distance[y][x]


    for dy in range(-2, 3):
        for dx in range(-2, 3):
            ny, nx = y + dy, x + dx
            if abs(dy) + abs(dx) != 4 and 0 <= nx < w and 0 <= ny < h:
                if distance[ny][nx] > distance[y][x] + 1:
                    queue1.append((ny, nx))
                    distance[ny][nx] = distance[y][x] + 1

ans = distance[h - 1][w - 1]
print(ans)