import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = t

for i in range(n*2):
    ans[i%n] = min(ans[i%n], ans[(i-1)%n] + s[(i-1)%n])

print(*ans, sep='\n')