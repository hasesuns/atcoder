import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(int(input()) for i in range(n))

cnt = 0
for i in range(n):
    if a[i]%2==1:cnt+=1

if cnt>0:
    print('first')
else:
    print('second')