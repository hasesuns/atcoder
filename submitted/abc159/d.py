import collections
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
c = collections.Counter(a)

total = 0
for count in c.values():
    total +=  count*(count-1)//2

d = defaultdict(list)

for number in c.keys():
    count = c[number]
    d[number] = total - (count-1)

for i in a:
    print(d[i])
 