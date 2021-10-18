import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

s, w = map(int, input().split())

if w>=s:
    print('unsafe')
else:
    print('safe')