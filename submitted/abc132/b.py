n = int(input())
p = [int(_) for _ in input().split()]
ans = 0

for i in range(1,n-1):
    if p[i-1] < p[i] and p[i] <= p[i+1]:
        ans = ans + 1
    elif p[i+1] < p[i] and p[i] <= p[i-1]:
        ans = ans + 1
        # print(p[i-1], p[i],p[i+1])

print(ans)
    