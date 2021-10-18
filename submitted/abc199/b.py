import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
b = list( map(int, input().split()))

maxa = max(a)
minb = min(b)

ans = max(minb - maxa + 1, 0)
print(ans)