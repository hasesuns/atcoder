import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

xorall = 0

for aa in a:
    xorall ^= aa

ans = []

for aa in a:
    ans.append(xorall^aa)

print(*ans,sep=' ')