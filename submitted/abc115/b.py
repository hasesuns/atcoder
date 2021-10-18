import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(int(input()) for i in range(n))

ma = max(a)

ans = sum(a)-ma//2

print(ans)