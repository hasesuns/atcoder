l, r = list(map(int, input().split()))
MOD = 2019
diff = r - l
ans = 0
if diff < 2019:
    l = l%MOD
    r = l + diff
    ans = 2018
    for i in range(l,r):
        for j in range(i+1, r+1):
            ans = min(ans, (i%MOD*j%MOD)%MOD )
      
print(ans)