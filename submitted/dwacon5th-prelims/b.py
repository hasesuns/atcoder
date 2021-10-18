import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
import math

n, k = map(int, input().split())
a = list( map(int, input().split()))

from itertools import accumulate
acc = [0] + a
acc = list(accumulate(acc))

beauty = []
left = right = 0

for left in range(n+1):
    for right in range(left + 1, n + 1):
        beauty.append(acc[right] - acc[left])

beauty.sort(reverse=True)

bimax = int(math.log2(max(beauty)))

ans = 0
check_nums = beauty
for i in reversed(range(bimax + 1)):
    cnt = 0
    next_check_nums = []
    for j in range(len(check_nums)):
        if (check_nums[j] >> i) & 1 == 1:
            next_check_nums.append(check_nums[j])
            cnt += 1
            if cnt == k:
                ans += 2**i
    if cnt >= k:
        check_nums = next_check_nums

print(ans)