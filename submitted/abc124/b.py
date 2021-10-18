n = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(n):
    if max(h[:(i+1)]) <= h[i]:
        ans = ans +1
print(ans)