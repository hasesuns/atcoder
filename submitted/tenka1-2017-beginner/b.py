import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

mib = float('inf')

for i in range(n):
    a, b = map(int, input().split())
    if mib > b:
        mib = b
        ans = a

ans += mib

print(ans)