import heapq
n, m = map(int, input().split())
a = list( map(int, input().split())) 
ans = sum(a)
a = [(-x, x) for x in a]
heapq.heapify(a)


for i in range(m):
    minusaa, aa  = heapq.heappop(a)
    ans -= aa
    heapq.heappush(a, (-(aa//2), aa//2))
    ans += aa//2

print(ans)