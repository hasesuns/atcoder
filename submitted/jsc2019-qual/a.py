m, d = list(map(int, input().split()))

ans = 0
for i in range(1,m+1):
    for j in range(22, d+1):
        d1 = int(str(j)[1])            
        d10 = int(str(j)[0])
        if d1*d10==i and d1 >=2:
            ans += 1


print(ans)