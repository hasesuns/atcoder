import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
ans = 0 
for i in range(n):
    if a[i] >= 10:
        ans += a[i]-10

print(ans)