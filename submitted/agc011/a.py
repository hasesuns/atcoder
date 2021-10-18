import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n,c,k = map(int, input().split())
t = list(int(input()) for i in range(n))
t.sort()
ans =0

from collections import deque
queue = deque()

INF = float('inf')
t.append(INF)

for i in range(n):

    queue.append(t[i])
    limit = queue[0]+k

    if limit < t[i+1] or len(queue)>=c:
        for i in range(min(len(queue), c)):
            queue.popleft()
        ans += 1

while queue:
    for i in range(min(len(queue), c)):
        queue.popleft()
    ans += 1

print(ans)
 