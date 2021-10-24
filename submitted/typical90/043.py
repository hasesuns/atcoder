import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)

h, w = map(int, input().split())
ys, xs = map(int, input().split())
yt, xt = map(int, input().split())
ys, xs = ys-1, xs-1
yt, xt = yt-1, xt-1
maze = [[-1 for _ in range(w)] for _ in range(h)]

ans = 0
for i in range(h):
    maze[i] = input()

cost = [[[float("inf")] * 2 for _ in range(w)] for _ in range(h)]
queue0 = deque()
queue1 = deque()

for dy, dx, direction in [(-1, 0, 0), (0, 1, 1), (1, 0, 0), (0, -1, 1)]:     
    cost[ys][xs][direction] = 0
    ny, nx = ys + dy, xs + dx
    if not 0 <= nx < w: continue
    if not 0 <= ny < h: continue 
    if maze[ny][nx] != "#":
        queue0.append((ny, nx, direction))
        cost[ny][nx][direction] = 0

while queue0 or queue1:
    if queue0:
        y, x, old_direction = queue0.popleft()
    elif queue1:
        y, x, old_direction = queue1.popleft()

    for dy, dx, new_direction in [(-1, 0, 0), (0, 1, 1), (1, 0, 0), (0, -1, 1)]:     
        ny, nx = y + dy, x + dx
        if not 0 <= nx < w: continue
        if not 0 <= ny < h: continue 
        if maze[ny][nx] != '#':
            if new_direction == old_direction and cost[ny][nx][new_direction] > cost[y][x][old_direction]:
                cost[ny][nx][new_direction] = cost[y][x][old_direction]
                queue0.append((ny, nx, old_direction))
            elif new_direction != old_direction and cost[ny][nx][new_direction] > cost[y][x][old_direction] + 1:
                cost[ny][nx][new_direction] = cost[y][x][old_direction] + 1
                queue1.append((ny, nx, new_direction))

ans = min(cost[yt][xt])
print(ans)