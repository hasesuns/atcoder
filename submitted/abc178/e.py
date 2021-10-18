import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

INF = float('inf')

plusmax = minusmax =-INF
plusmin = minusmin = INF

for i in range(n):
    x, y = map(int, input().split())

    x_minus_y = x-y
    x_plus_y = x+y

    plusmax = max(plusmax, x_plus_y)
    plusmin = min(plusmin, x_plus_y)
    minusmax = max(minusmax, x_minus_y)
    minusmin = min(minusmin, x_minus_y)

ans0 = plusmax - plusmin
ans1 = minusmax - minusmin
print( max(ans0, ans1))