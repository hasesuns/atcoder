import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

from collections import deque

d = deque(a)
ans=0
while len(d)>2:
    head = 1+2*d[0]+d[1]
    tail = 1+2*d[-1]+d[-2]
    if head <= tail:
        ans+=head
        d1=d.popleft()
        d2=d.popleft()
        d3=d.popleft()
        d.appendleft(d1+d2+d3+2)
    else:
        ans+=tail
        d1=d.pop()
        d2=d.pop()
        d3= d.pop()
        d.append(d1+d2+d3+2)

print(ans)