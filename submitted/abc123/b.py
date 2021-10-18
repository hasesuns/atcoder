lst = [int(input()) for i in range(5)]

lst = sorted(lst, key =lambda x: 10 if x%10==0 else x%10, reverse = 1)
ans = 0
for l in lst[:4]:
    if l%10 == 0:
        ans += l
    else:
        ans += l//10*10 + 10
ans += lst[4]
print(ans)