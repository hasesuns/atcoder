import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(int(input()) for i in range(n))

sa = list(set(a))
sa.sort()

from collections import defaultdict

d = defaultdict(list)

for i,ssa in enumerate(sa):
    d[ssa] = i

for i in range(n):
    print(d[a[i]])
    