import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

d = [[float('inf')]*n for i in range(n)]

for i in range(n):
    d[i] = list( map(int, input().split()))

for i in range(n):
    if d[i][i] != 0:
        print(-1)
        exit()

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                print(-1)
                exit()

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i==k or k==j :continue
            if d[i][j] == d[i][k] + d[k][j]:
                break
        else:
            ans += d[i][j]

print(ans//2)