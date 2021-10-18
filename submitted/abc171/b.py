import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
p = list( map(int, input().split()))

p.sort()

ans = sum(p[:k])
print(ans)