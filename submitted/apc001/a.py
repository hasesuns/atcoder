import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
x, y = map(int, input().split())

if x%y==0:
    print(-1)
    exit()

ans = x
while ans<=10**18:
    if x%y!=0:
        print(x)
        exit()
    else:
        ans+=x