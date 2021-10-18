import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a,b, n = map(int, input().split())

if n >= b-1:
    x= b-1
    ans = int(a*x/b) - a*int(x/b)
    print(ans)
else:
    x = n
    ans = int(a*x/b) - a*int(x/b)
    print(ans)