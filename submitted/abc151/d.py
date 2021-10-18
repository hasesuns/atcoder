h, w = map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]


ans = 0
for i in range(h):
    maze[i] = input()

INF = 1000
ans = 0


for sy in range(h):
    for sx in range(w):
        if maze[sy][sx] == '#':
            continue
        else:
            distance = [[-1 for i in range(w)] for j in range(h)]


        queue = []

        queue.insert(0, (sy, sx))

        distance[sy][sx] = 0

        while len(queue):
            y, x = queue.pop()

            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

                if 0 <= nx < w and 0 <= ny < h:
                    if maze[ny][nx] != '#' and distance[ny][nx] == -1:
                        queue.insert(0, (ny, nx))
                        distance[ny][nx] = distance[y][x] + 1

                        ans = max(ans, distance[ny][nx])

print(ans)