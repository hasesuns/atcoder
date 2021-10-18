import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b,c,d = map(int, input().split())

taka = -(-a//d)
ao = -(-c//b)


if taka < ao:
    print('No')
else:
    print('Yes')

 