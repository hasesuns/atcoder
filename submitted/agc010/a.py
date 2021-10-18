import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

cnt = 0
for i in range(n):
    if a[i] %2 == 1: cnt+=1

if cnt%2==1:
    print('NO')
else:
    print('YES')

 