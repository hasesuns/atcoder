import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

h, w = map(int, input().split())

hh, ww = map(int, input().split())

if h == hh or h ==ww:
    print('YES')
    exit()
if w == hh or w ==ww:
    print('YES')
    exit()
print('NO')