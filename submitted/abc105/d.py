from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

a = list( map(int, input().split()))

from itertools import accumulate
b = [0] + a
b = list(accumulate(b))

count_mod = defaultdict(int)

for i in range(n+1):
    bi_modm = b[i]%m
    if count_mod[bi_modm] is None: count_mod[bi_modm]=1
    else: count_mod[bi_modm] += 1

ans = 0
for count in count_mod.values():
    ans += count*(count-1)//2
print(ans)