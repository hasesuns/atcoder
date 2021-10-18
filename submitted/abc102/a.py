import numpy as np

n = int(input())

a = list(map(int, input().split()))
a = np.array(a)
a -= np.array(range(1,n+1))

b = np.median(a)

ans = int(np.sum(abs(a-b)))

print(ans)