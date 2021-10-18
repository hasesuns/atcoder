import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

print(b - c)