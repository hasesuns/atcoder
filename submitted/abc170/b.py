import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x, y = map(int, input().split())


for turu in range(x+1):
    if turu*2 + (x-turu)*4 == y:
        print('Yes')
        exit()


print('No')