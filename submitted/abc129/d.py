from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)

h, w = map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]

ans = 0
for i in range(h):
    maze[i] = input()

queue = deque()

left = [[0 for j in range(w)] for i in range(h)]
right = [[0 for j in range(w)] for i in range(h)]
up = [[0 for j in range(w)] for i in range(h)]
down = [[0 for j in range(w)] for i in range(h)]

cnt = 0

for i in range(h):
    cnt = 0
    for j in range(w):
        if maze[i][j] == '#': cnt = 0
        else:
            cnt += 1
            left[i][j] = cnt

    cnt = 0
    for j in reversed(range(w)):
        if maze[i][j] == '#': cnt = 0
        else:
            cnt += 1
            right[i][j] = cnt


for j in range(w):
    cnt = 0
    for i in range(h):
        if maze[i][j] == '#': cnt = 0
        else:
            cnt += 1
            up[i][j] = cnt

    cnt = 0
    for i in reversed(range(h)):
        if maze[i][j] == '#': cnt = 0
        else:
            cnt += 1
            down[i][j] = cnt

ans = 0
for i in range(h):
    for j in range(w):
        tmp = left[i][j] + right[i][j] + up[i][j] + down[i][j] - 3
        ans = max(tmp, ans)

print(ans)