n = int(input())
a = list( map(int, input().split()))

p =10**9+7

cnt= [0]*n
cnt[0]=1
ans = 3

if a[0]!=0:
    print(0)
    exit()

for i in range(1,n):
    if a[i]==0:
        ans *= (3-cnt[a[i]])
    else:
        ans *= (cnt[a[i]-1] - cnt[a[i]])
        if cnt[a[i]-1]==0:
            print(0)
            exit()

    ans%=p
    cnt[a[i]] += 1
    if cnt[a[i]]>3:
        print(0)
        exit()

print(ans%p)