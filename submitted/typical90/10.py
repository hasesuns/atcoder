import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
ichi_kumi = []
ni_kumi = []

for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        ichi_kumi.append(p)
        ni_kumi.append(0)
    else:
        ichi_kumi.append(0)
        ni_kumi.append(p)


acc_1 = [0] + ichi_kumi
acc_1 = list(accumulate(acc_1))
acc_2 = [0] + ni_kumi
acc_2 = list(accumulate(acc_2))

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    l, r = l-1, r-1
    ans_1 = acc_1[r + 1] - acc_1[l]
    ans_2 = acc_2[r + 1] - acc_2[l]
    print(ans_1, ans_2, sep=" ")