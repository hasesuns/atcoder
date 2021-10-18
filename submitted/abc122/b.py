s = input() #sys.stdin.readlineは最後が改行

ans = 0
cnt = 0
atgc = ['A','T','G','C']
for i in range(len(s)):
    if s[i] in atgc:
        cnt+=1
    else:
        ans = max(ans,cnt)
        cnt = 0
ans = max(ans,cnt)
print(ans)