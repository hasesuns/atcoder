import numpy as np

n = int(input())
p = np.array(list( map(int, input().split())) )
pp = np.arange(n) + 1 

if sum(p == pp) >= n-2:
    print('YES')
else:
    print('NO')