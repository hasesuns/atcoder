n = int(input())
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

ans = 0
for i in range(n):
    a = list( map(int, input().split()))
    if 0<=sum(a)<20:
        ans+=1

print(ans)