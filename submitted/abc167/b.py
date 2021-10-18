import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a,b,c,k = map(int, input().split())

if k <= a:
    print(k)
elif k <= a+b:
    print(a)
else:
    cc = k - (a+b)
    print(a-cc)