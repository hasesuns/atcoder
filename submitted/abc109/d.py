import sys
sys.setrecursionlimit(10 ** 7)

h, w = map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]
used = [[-1 for i in range(w)] for j in range(h)]


ans = 0
for i in range(h):
    maze[i] = list(map(int, input().split()))

ans = []

for y in range(h):
    if y%2==0:
        for x in range(w):
            if maze[y][x]%2==0:
                continue
            else:
                if x<w-1:
                    ans.append([y+1,x+1,y+1,x+1+1])
                    maze[y][x+1]+=1
                elif y<h-1:
                    ans.append([y+1,x+1,y+1+1,x+1])
                    maze[y+1][x]+=1

    else:
        for x in reversed(range(w)):
            if maze[y][x]%2==0:
                continue
            else:
                if x>0:
                    ans.append([y+1,x+1,y+1,x+1-1])
                    maze[y][x-1]+=1
                elif y<h-1:
                    ans.append([y+1,x+1,y+1+1,x+1])
                    maze[y+1][x]+=1

print(len(ans))

for i in range(len(ans)):
    print(*ans[i], sep=' ')