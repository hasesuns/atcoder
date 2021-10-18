import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x, y = map(int, input().split())

if x<y:
    diff = abs(abs(x)-abs(y))
    if x*y>=0:
        print(diff)
        exit()
    else:
        print(diff+1)
        exit()


if y<x:
    diff = abs(abs(x)-abs(y))
    if x*y>0:
        print(diff+2)
    else:
        print(diff+1)