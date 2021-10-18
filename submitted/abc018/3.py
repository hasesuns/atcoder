from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)
import numpy as np

r, c, k = map(int, input().split())
maze = [[-1 for i in range(c)] for j in range(r)]

ans = 0
for i in range(r):
    maze[i] = input()

INF = 10000
ans = 0

queue = deque()
distance = [[INF for i in range(c)] for j in range(r)]
visited = [[0 for i in range(c)] for j in range(r)]

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'x':
            queue.append((i, j))
            distance[i][j] = 0
            visited[i][j] = 1
        elif i==0 or i == r-1 or j ==0 or j==c-1:
            queue.appendleft((i, j))
            distance[i][j] = 1
            visited[i][j] = 1

move = [[1,0],[-1,0], [0,1], [0,-1]]

while len(queue):
    y, x = queue.pop()
    for x_, y_ in move:
        nx, ny = x + x_, y + y_
        if 0 <= nx < c and 0 <= ny < r and visited[ny][nx]==0:
            distance[ny][nx] = distance[y][x]+1
            queue.appendleft((ny, nx))
            visited[ny][nx] = 1

distance = np.array(distance)
ans = np.sum(distance >= k)

print(ans)
 