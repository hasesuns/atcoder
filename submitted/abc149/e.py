from bisect import bisect_left
from itertools import accumulate


n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

b = [0] + a
b.sort(reverse=True)
b = [0] +b
b = list(accumulate(b))

def isok(sum_):
    n_pattern = 0
    for i in range(n):
        n_pattern += n - bisect_left(a, sum_ - a[i])
        if n_pattern >= m:
            return True

    return False

ok = min(a)*2
ng = max(a)*2 +1

while ng - ok > 1:
    mid = (ok+ng)//2
    if isok(mid):
        ok = mid
    else:
        ng = mid

sum_ng = ng
sum_ok = ok

m_counter_ng = 0

ans = 0
for i in range(n):
    id_ng = bisect_left(a, sum_ng - a[i])
    ans += b[n-id_ng]
    ans += a[i]*(n - id_ng)
    m_counter_ng += n - id_ng

ans += sum_ok * (m - m_counter_ng)

print(ans)