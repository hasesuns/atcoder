N = int(input())
S = [0]*N
P = [0]*N
A = [0]*N
for i in range(N):
    s, p =input().split()
    A[i] = [i, s, int(p)]

A = sorted(A,key=lambda x: (x[1],-x[2]))

for i in range(N):
    print( A[i][0]+1)