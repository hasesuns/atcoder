import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

me = sum(a)/n

for i in range(n):
    a[i]= abs(a[i]-me)

mia = min(a)
ans = a.index(mia)

print(ans)