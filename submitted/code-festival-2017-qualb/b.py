import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
d = list( map(int, input().split()))
m = int(input())
t = list( map(int, input().split()))

from collections import Counter

cd = Counter(d)
ct = Counter(t)

for k,v in ct.items():
    if v > cd[k]:
        print('NO')
        exit()
print('YES')