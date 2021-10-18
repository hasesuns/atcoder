N = int(input())
d = [int(_) for _ in input().split()]
ans = 0
d = sorted(d)

if d[N//2-1] != d[N//2]:
    ans = d[N//2] - d[N//2 - 1] 

print(ans)