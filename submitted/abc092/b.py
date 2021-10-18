import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
d, x = map(int, input().split())

a = list(int(input()) for i in range(n))

ans = x
for i in range(n):
    ans += 1
    ans += (d-1)//a[i]
print(ans)