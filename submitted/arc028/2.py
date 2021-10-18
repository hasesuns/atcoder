import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


# --- 優先度付きキュー
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

n, k = map(int, input().split())
x = list( map(int, input().split()))

x2i = [0]*(n+1)

for i in range(n):
    x2i[x[i]] = i+1


q = Heapq([], True)

for i in range(k):
    q.push(x[i])

ans = q.pop()
print(x2i[ans])
q.push(ans)


for i in range(k,n):
    q.push(x[i])
    q.pop()
    ans = q.pop()
    print(x2i[ans])
    q.push(ans)

 