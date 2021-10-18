import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
if n%2==1:
    if (n-1)//2 >= k-1: print('YES')
    else: print('NO')
else:
    if n//2 >= k: print('YES')
    else: print('NO')
      