n = int(input())
p = list( map(int, input().split()))

ans = 0
i = 0
while i < n:
    i_num = p[i] - 1
    if i == i_num:
        ans+=1
        i += 1
    i+=1
print(ans)