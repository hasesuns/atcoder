import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

ans = 0
for i in range(n):
    ans += abs(b[i] - a[i])

print(ans)