import heapq

q = int(input())

offset = 0

a = []
heapq.heapify(a)

ans = []

for i in range(q):
    s = input()
    if s[0] == "1":
        _, x = map(int, s.split())
        heapq.heappush(a, x-offset)
    elif s[0] == "2":
        _, x = map(int, s.split())
        offset += x
    else:
        ans.append(heapq.heappop(a) + offset)

print(*ans, sep="\n")