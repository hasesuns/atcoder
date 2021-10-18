from bisect import bisect_left

n = int(input())
l = list( map(int, input().split())) 
ans = 0
l.sort()

for i in range(n-2):
    shortest = l[i]
    for j in range(i+1, n-1):
        second = l[j]
        # このスライスしたやつと地味にTLEになる...
        # k = bisect_left(l[j], shortest + second)
        # ans += k

        k = bisect_left(l, shortest + second)
        ans += k - j - 1

print(ans)