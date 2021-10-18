import numpy as np


n = int(input())
st = [tuple(input().split()) for i in range(n)]
x = input()
T = []

for i, (s, t) in enumerate(st):
    T.append(int(t))

    if s == x:
        fin = i

T = np.array(T)

ans = np.sum(T[fin+1:])

print(ans)