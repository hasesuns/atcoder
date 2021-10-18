import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int,input().split())) for i in range(n)]
es = [[] for i in range(n)]
for a,b in ab:
    a,b = a-1,b
    es[a].append(b)

import heapq
# max heap
class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        return heapq.heappop(self.hq) * self.sign

    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)

    def top(self):
        return self.hq[0] * self.sign

    def size(self):
        return len(self.hq)


q = Heapq([], True)

ans = [0]*n

for i in range(n):
    for b in es[i]:
        q.push(b)
    if q.size():
        if i==0:
             ans[i] = q.pop()
        else:
            ans[i] = ans[i-1] + q.pop()

print(*ans,sep='\n')