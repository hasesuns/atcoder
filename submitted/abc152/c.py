n = int(input())
p = list(map(int, input().split()))

ans = 0
mini = p[0]
for i in range(n):
    if mini >= p[i]:
        ans += 1
    mini = min(mini, p[i])

print(ans)