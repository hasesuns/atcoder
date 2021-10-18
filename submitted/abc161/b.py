import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

a = list( map(int, input().split()))

count = 0

suma = sum(a)

for i in range(n):
    if a[i] >= suma/4/m:
        count+=1

if count >=m:
    print('Yes')
else:
    print('No')