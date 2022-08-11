import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

offset = 0
ans = 0
for i in reversed(range(n)):
    if a[i] + offset >= 4:
        ans += 1
    offset += a[i]

print(ans)