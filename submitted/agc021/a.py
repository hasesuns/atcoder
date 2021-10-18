n = int(input())
s= str(n)

if n<10:
    print(n)
    exit()

ans = 0

for i in range(1,len(s)):
    if int(s[i])!=9:
        for j in range(i):
            ans += int(s[j])
        ans-=1
        ans += 9*(len(s)-i)
        print(ans)
        exit()

ans=0
for i in range(len(s)):
    ans += int(s[i])
print(ans)