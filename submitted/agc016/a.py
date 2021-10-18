s = input() #sys.stdin.readlineは最後が改行

count = 0
ans=len(s)
tmp=0
for cc in list(set(s)):

    for i in range(len(s)):
        if s[i]==cc:
            tmp = max(tmp,count)
            count = 0
        else:
            count+=1

    tmp = max(tmp,count)

    ans = min(ans,tmp)
    tmp=0
    count=0

print(ans)