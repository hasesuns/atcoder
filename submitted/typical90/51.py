import sys
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

n, k, p = map(int, input().split())
a = list(map(int, input().split()))

n_1st = n // 2
n_2nd = n - n_1st
k_1st = k // 2
k_2nd = k - k_1st

# data_1st[i][j]: 1stのデータからi個選んだ時の価格のパターン
data_1st = [[] for _ in range(n_1st + 1)]
for i in range(2 ** n_1st):
    val_tmp = 0
    cnt_num_tmp = 0
    for j in range(n_1st):
        if (i >> j) & 1 == 1:  # j桁目 is 1?
            val_tmp += a[j]
            cnt_num_tmp += 1
    data_1st[cnt_num_tmp].append(val_tmp)
for i in range(n_1st):
    data_1st[i].sort()

data_2nd = [[] for _ in range(n_2nd + 1)]
for i in range(2 ** n_2nd):
    val_tmp = 0
    cnt_num_tmp = 0
    for j in range(n_2nd):
        if (i >> j) & 1 == 1:  # j桁目 is 1?
            val_tmp += a[j + n_1st]
            cnt_num_tmp += 1
    data_2nd[cnt_num_tmp].append(val_tmp)
for i in range(n_2nd):
    data_2nd[i].sort()

ans = 0
for kosu_1st in range(n_1st+1):
    for val_1st in data_1st[kosu_1st]:
        if 0 <= k - kosu_1st <= n_2nd:
            pattern_2nd = bisect_right(data_2nd[k - kosu_1st], p - val_1st)
            ans += pattern_2nd

print(ans)