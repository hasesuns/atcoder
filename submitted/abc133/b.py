import math

n, d = list(map(int, input().split()))

x = [[0]*d for _ in range(n)]
ans = 0
for i in range(n):
    x[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        r2 = 0
        for k in range(d):
            r2 =  r2 + (x[i][k] - x[j][k])**2

        r = math.sqrt(r2)
        ans += r.is_integer()

print(ans)  