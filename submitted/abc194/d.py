import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

ans = 0

for i in range(n-1):
    ans += n / (n-i-1)

print(ans)