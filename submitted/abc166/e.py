import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

from collections import defaultdict
ar = defaultdict(list)
al = defaultdict(list)

for i in range(n):
    al[i+a[i]].append(i)
    ar[i-a[i]].append(i)

x = al.keys()

ans = 0
for i in x:
    ans += len(ar[i]) * len(al[i])

print(ans)