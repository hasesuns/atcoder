import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, X = map(int, input().split())

numP_N = [0]*N
numPB_N = [0]*N
numP_N[0] = 3
numPB_N[0] = 5
for i in range(1,N):
    numP_N[i] = numP_N[i-1] * 2 + 1
    numPB_N[i] = numPB_N[i-1] * 2 + 3

def rec(n, x):
    if n == 1:
        ans_1 = [0,0,1,2,3,3]
        return ans_1[x]

    if x == numPB_N[n-1]:
        return numP_N[n-1]

    elif x > numPB_N[n-2] + 2:
        return numP_N[n-2] + 1 + rec(n-1, x-numPB_N[n-2] - 2)

    elif x == numPB_N[n-2] + 2:
        return numP_N[n-2] + 1

    elif x == numPB_N[n-2] + 1:
        return numP_N[n-2]

    elif x < numPB_N[n-2] + 1:
        return rec(n-1, x-1)

print(rec(N,X))