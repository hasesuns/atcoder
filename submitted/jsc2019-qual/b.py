n, k = list(map(int, input().split()))
a = list( map(int, input().split())) 

MOD = 10**9 + 7

ansR = 0
ansL = 0

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            if i > j:
                ansL += 1
            if i < j:
                ansR += 1

ans = ansR*(k+1)*k//2%MOD + ansL*(k-1)*k//2%MOD

print(int(ans%MOD))