import collections

n = int(input())
a = list( map(int, input().split()))
c = collections.Counter(a)

ans = len(c)
count_even = 0

for num in c.keys():
    if c[num] %2 ==0: count_even += 1

if count_even%2 == 1:ans-=1

print(ans)