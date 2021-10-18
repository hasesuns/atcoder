import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n,a,b = map(int, input().split())

if a>b:
    print(0)
    exit()

if a==b:
    print(1)
    exit()

if n==1 and a!=b:
    print(0)
    exit()

mi = a*(n-1)+b
ma = a+b*(n-1)

print(ma-mi+1)