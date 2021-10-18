import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

a.sort(reverse=True)

ans = 0
for i in range(n*2):
    if i%2==1: ans += a[i]
print(ans)
 