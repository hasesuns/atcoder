h, n = [int(i) for i in input().split()]
a, b = [0]*n, [0]*n

eff = 0
eff_index = 0
for i in range(n):
    a[i], b[i] = [int(_) for _ in input().split()]

max_a = max(a)

ans = float('inf')
H = h + max_a
dp = [float('inf')] * (H+1)
# dp[i] iのダメージを与える最小消費魔力
dp[0] = 0
for i in range(H+1):
    for j in range(n):
        if i >= a[j]:
            dp[i] = min(dp[i], dp[i-a[j]]+b[j])

    if i >= h:
        ans = min(ans, dp[i])
print(ans)