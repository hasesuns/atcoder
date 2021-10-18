from bisect import bisect_left

n = int(input())
a = list( map(int, input().split()))

a.sort()
half = a[-1]/2

index = bisect_left(a,half)
candi1 = a[index]
if index > 0: candi0 = a[index-1]
else: candi0 = -1

if abs(half-candi0) > abs(half-candi1): ans = candi1
else: ans = candi0

print(a[-1], ans, sep=' ')