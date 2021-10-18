from functools import lru_cache
h,w= map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]

ans = 0
for i in range(h):
    maze[i] = input()

INF = 10000

@lru_cache(None)
def dfs(y,x,flg,cnt):
    if y == h-1 and x ==w-1:
        if flg ==1:
            cnt+=1
        return cnt
    ans = [INF]
    for (ny, nx) in [(y+1, x), (y, x+1)]:
        if 0 <= nx < w and 0 <= ny < h:
            if maze[ny][nx] != maze[y][x]:
                if flg == 0: ans.append(dfs(ny,nx,1,cnt))
                else: ans.append(dfs(ny,nx,0,cnt+1))
            else:
                ans.append(dfs(ny,nx,flg,cnt))
    return(min(ans))

print(dfs(0,0,(0 if maze[0][0]=='.' else 1),0))