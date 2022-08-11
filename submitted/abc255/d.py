import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from bisect import bisect_left
from itertools import accumulate

n, q = map(int, input().split())
a = list(map(int, input().split()))
x = list(int(input()) for _ in range(q))

a.sort()

neg_acc = [0] + [-aa for aa in a]
neg_acc = list(accumulate(neg_acc))

pos_acc = list(reversed(a))
pos_acc = list(accumulate(pos_acc))
pos_acc.reverse()
pos_acc = pos_acc + [0]

ans_list = []
for xx in x:
    index = bisect_left(a, xx)
    ans = (2*index - n)*xx + neg_acc[index]+pos_acc[index]
    ans_list.append(ans)

print(*ans_list, sep="\n")