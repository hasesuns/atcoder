import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

a = [0]* n
b = [0]* n
for i in range(n):
    a[i], b[i] = map(int, input().split())

ans= 0
for i in reversed(range(n)):
    a[i]+=ans
    tmp = -(-a[i] // b[i])
    ans += tmp*b[i]-a[i]

print(ans)