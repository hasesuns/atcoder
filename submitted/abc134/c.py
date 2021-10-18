import numpy as np

n = int(input())
a = [int(input()) for _ in range(n)]
na = np.array(a)
maxI = np.argmax(na)
maxA = na[maxI]
nb = np.copy(na)
nb[maxI] = 0
maxA2 = np.max(nb)
for i in range(n):
    if i != maxI:
        print(na[maxI])
    else:
       print(maxA2)