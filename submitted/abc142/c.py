n = int(input())
a = list( map(int, input().split())) 

from collections import defaultdict
d = defaultdict(list)

for i in range(n):
    d[a[i]] = i 

for i in range(1, n+1):
    print(d[i]+1, end=' ')