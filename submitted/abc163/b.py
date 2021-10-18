import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list( map(int, input().split()))

suma = sum(a)
if suma > n:
    print(-1)
else:
    print(n-suma)