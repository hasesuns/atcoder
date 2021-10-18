n = int(input())
d = list( map(int, input().split())) 

ans = 0
sumd = sum(d)

for i in range(n):
    ans += d[i]*sum(d[i+1:])

print(ans)