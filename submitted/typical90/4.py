import sys

sys.setrecursionlimit(10 ** 9)

h, w = map(int, input().split())
maze = [[-1 for _ in range(w)] for _ in range(h)]

sum_h_list = [0] * h
sum_w_list = [0] * w

for i in range(h):
    maze[i] = list(map(int, input().split()))
    for j, a_ij in enumerate(maze[i]):
        sum_h_list[i] += a_ij
        sum_w_list[j] += a_ij

ans = [[-1 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] = sum_h_list[i] + sum_w_list[j] - maze[i][j]

for ans_ in ans:
    print(*ans_)
    