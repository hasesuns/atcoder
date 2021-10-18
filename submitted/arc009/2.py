num_dict = [0]*10

b = list( map(int, input().split()))
n = int(input())
a = list(list(input()) for i in range(n))

for i in range(10):
    num_dict[b[i]] = i

A = [(0,0) for i in range(n)]

for i in range(n):

    aa = ''
    for j in range(len(a[i])):
        aaj =  str(num_dict[int(a[i][j])])
        aa += aaj
    A[i] = (a[i], int(aa))

A.sort(key=lambda x:x[1])
for i in range(n):
    print(*A[i][0],sep='')