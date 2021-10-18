s = input() #sys.stdin.readlineは最後が改行

tmp =0
ans=0
for i in range(len(s)):
    if s[i]=='B':
        tmp+=1
    else:
        ans+=tmp

print(ans)