n, k, q = map(int, input().split())
a = list(int(input()) for i in range(q)) 
points = [k for _ in range(n)]


for i in range(q):
    points[a[i]-1] += 1

for j in range(n):
    points[j] -= q

    if points[j] > 0:
        print('Yes')
    else:
        print('No')