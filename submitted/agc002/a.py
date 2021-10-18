import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b = map(int, input().split())

if a<=0 and b>=0:
    print('Zero')
    exit()

if a>0 and b>0:
    print('Positive')
    exit()


if (b-a)%2 == 0:
    print('Negative')
else:
    print('Positive')