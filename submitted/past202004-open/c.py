import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
w = 2*n-1
h = n

S = [[-1 for i in range(w)] for j in range(h)]

for i in range(h):
    S[i] = list(input())

for i in reversed(range(h-1)):
    for j in range(w):
        if S[i][j]!='.' and (S[i+1][j-1] == 'X' or S[i+1][j] == 'X' or S[i+1][j+1] == 'X'):
            S[i][j] = 'X'

for i in range(h):
    print(*S[i],sep='')
 