import numpy as np
n = int(input())
a = list( map(int, input().split()))

p = np.mean(a)

p1 = int(p)
p2 = p1 + 1

ans1 = 0
ans2 = 0
for i in range(n):
    ans1 += (a[i] - p1)**2
    ans2 += (a[i] - p2)**2



print(min(ans1, ans2))