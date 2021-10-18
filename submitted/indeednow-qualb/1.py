import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x,y = map(int, input().split())
x2,y2 = map(int, input().split())

print(abs(x-x2)+abs(y-y2)+1)