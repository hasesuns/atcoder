import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
table = [[-1 for _ in range(n)] for _ in range(n)]
counter = [[] for _ in range(10)]

for y in range(n):
    s = input()[:-1]
    for x in range(n):
        counter[int(s[x])].append([y, x])
        table[y][x] = int(s[x])

starts = []

for count in reversed(counter):
    if len(count) != 0:
        starts = count
        break

def dfs(y, x, dy, dx, cnt, val):
    val += table[y][x] * (10 ** (n-cnt-1))
    if cnt == n-1:
        return val
    return dfs((y+dy)%n,(x+dx)%n, dy, dx ,cnt+1, val)

ans = 0

for sy,sx in starts:
    for dy,dx in [(-1,-1),(-1,0), (-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)]:
        ans = max(ans, dfs(sy,sx, dy, dx, 0, 0))

print(ans)