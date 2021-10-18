import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, a,b = map(int, input().split())

print(min(a,b), max(a+b-n, 0) )