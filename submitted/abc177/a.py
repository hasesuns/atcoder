import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

d,t,s = map(int, input().split())

if s*t >= d:
    print('Yes')
else:
    print('No')