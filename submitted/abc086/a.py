import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a,b = map(int, input().split())

if (a*b)%2==0:
    print('Even')
else:
    print('Odd')