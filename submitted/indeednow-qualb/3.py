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

from collections import defaultdict
d = defaultdict(list)

n = int(input())

ab = [tuple(map(int,input().split())) for i in range(n-1)]
for a,b in ab:
    d[a].append(b)
    d[b].append(a)

q = Heapq([], False) # 最小値順にする

ans = [1]

for b in d[1]:
    q.push(b)


visit = [-1]*n
visit[0]=1

for i in range(1,n):
    if q.size():
        nex = q.pop()
        if visit[nex-1] == -1:
            ans.append(nex)
            visit[nex-1] = 1

        for b in d[nex]:
            if visit[b-1] == -1:
                q.push(b)

print(*ans,sep=' ')
 