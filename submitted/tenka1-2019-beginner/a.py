import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b,c = map(int, input().split())

if a<=c<=b:
    print('Yes')
elif a>=c>=b:
    print('Yes')
else:
    print('No')