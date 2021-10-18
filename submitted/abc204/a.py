import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
x, y = map(int, input().split())

xyz = [0,1,2]

if x == y:
    print(x)
else:
    xyz.remove(x)
    xyz.remove(y)
    print(xyz[0])