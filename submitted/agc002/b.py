import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
x = [0]* n
y = [0]* n

box = [[1, 0] for _ in range(n)]
box[0] = [0,1]

for i in range(m):
    x, y = map(int, input().split())
    x,y= x-1,y-1

    if box[x][1]>0:
        box[x][1] = box[x][1]-1
        box[y][1] = box[y][1] + box[y][0] + 1
        box[y][0] = 0
    else:
        box[x][0] = box[x][0]-1
        if box[y][1]>0:
            box[y][1] = box[y][1]+1
        else:
            box[y][0] = box[y][0]+1

ans = 0
for i in range(n):
    if box[i][1]>0: ans+=1

print(ans)
 