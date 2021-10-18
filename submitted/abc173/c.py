h, w, k = map(int, input().split())
maze = [[-1 for i in range(w)] for j in range(h)]

ans = 0
for i in range(h):
    maze[i] = input()

import itertools
ans=0
count=0
for casei in itertools.product([0,1], repeat=h):
    for casej in itertools.product([0,1], repeat=w):
        for i in range(h):
            for j in range(w):
                if maze[i][j]=='#' and casei[i]==0 and casej[j]==0:
                    count+=1
        if count == k:
            ans+=1
        count=0

print(ans)
 