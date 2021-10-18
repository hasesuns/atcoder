import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b,c = map(int, input().split())

print(min(b+a+1,c)+b)