import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = [0] * n
b = [0] * n

queue = []
ab = [tuple(map(int,input().split())) for _ in range(n)]
adj_list = [[] for _ in range(n)]
for i, (a,b) in enumerate(ab):
    a, b = a - 1, b - 1
    adj_list[a].append(i)
    adj_list[b].append(i)
    if a == i or b == i:
        queue.append(i)
        
ans = []
visited = [False] * n
while queue:
    v = queue.pop()
    if visited[v] == True:
        continue  
    visited[v] = True
    ans.append(v+1)
    
    for to in adj_list[v]:
        if visited[to] == False:
            queue.append(to)
        
if len(ans) != n:
    print(-1)
else:
    print(*ans[::-1], sep="\n")