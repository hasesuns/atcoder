import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

A = [(aa,i) for i,aa in enumerate(a)]

ans = [1]*(2**n)

i = 0
while i<n:
    next_A = []
    for j in range(2**(n-i-1)):

        if A[2*j][0] > A[2*j+1][0]:
            ans[A[2*j+1][1]] = i+1
            next_A.append(A[2*j])
        else:
            ans[A[2*j][1]] = i+1
            next_A.append(A[2*j+1])

    A = next_A[:]
    i+=1

ans[A[0][1]]=n

print(*ans,sep='\n')
 