import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list( map(int, input().split()))
b = list( map(int, input().split()))

ab = set(a+b)

bunshi = len(a) + len(b) -len(ab)
bunbo = len(a) + len(b) - bunshi

print(bunshi/bunbo)
 