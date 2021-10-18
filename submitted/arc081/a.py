import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

from collections import Counter

c = Counter(a)

ma1 = 0
ma2 = 0

for k,v in c.items():
    if v < 2:
        continue

    if k > ma1:
        if v >= 4:
            ma2 = k
            ma1 = k
            continue
        else:
            ma2 = ma1
            ma1 = k
    elif k > ma2:
        ma2 = k

print(ma1*ma2)