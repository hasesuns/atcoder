n = int(input())
a = list( map(int, input().split()))

ans = 0
index = 1

for i in range(n):
    if index != a[i]:
        ans+=1
    else:
        index += 1

if ans == n:
    print(-1)
else:
    print(ans)