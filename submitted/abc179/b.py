import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

cnt = 0
flg = False

for i in range(n):
    a, b = map(int, input().split())
    if a==b:
        cnt += 1
    else:
        cnt =0

    if cnt>=3:
        flg = True

if flg:
    print('Yes')
else:
    print('No')