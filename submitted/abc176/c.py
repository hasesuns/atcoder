import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

ma = a[0]
ans = 0
for i in range(1,n):
    if ma > a[i]:
        ans+= ma-a[i]
    else:
        ma = a[i]

print(ans)