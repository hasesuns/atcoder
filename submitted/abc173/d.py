import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

a.sort(reverse=True)

from collections import deque
deq = deque([a[1], a[1]])

ans = a[0]

for i in range(2,n):
    ans += deq.popleft()
    deq.append(a[i])
    deq.append(a[i])

print(ans)