p = 10**9+7
h, w = map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]

ans = 0
for i in range(h):
    maze[i] = input()

dp = [[0]*(w+1) for _ in range(h+1)]
dp[1][1] = 1

for i in range(1,h+1):
    for j in range(1,w+1):
        if maze[i-1][j-1] == '.':
            dp[i][j] += dp[i-1][j]%p + dp[i][j-1]%p


ans = dp[h][w]%p

print(ans)