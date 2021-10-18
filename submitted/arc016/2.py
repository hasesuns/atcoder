import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline

n = int(input())

ans = 0

x = [[] for _ in range(n)]
ans = 0
for i in range(n):
    x[i] = list(input())
    ans += x[i].count('x')

x=np.array(x)
x=x.T

for i in range(9):
    flg = 0
    for ss in x[i]:
        if ss == 'o':
            flg=1
        if ss != 'o' and flg ==1:
            ans += 1
            flg = 0
    if flg ==1:ans += 1

print(ans)