from math import log2

n = int(input())

target = int(log2(n))
ans = target -1
for tmp in [target-1, target, target+1]:
    if 2**tmp <= n:
        ans = tmp

print(ans)