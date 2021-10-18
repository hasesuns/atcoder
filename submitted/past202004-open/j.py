s = input() #sys.stdin.readlineは最後が改行
n= len(s)

ans = []
rev = []
rflg=0
tmp = []


for i in range(n):
    if s[i] == '(':
        if rflg > 0:
            rev.append(tmp)
            tmp = []
            rflg+=1
        else: rflg = 1
    elif s[i] == ')':
        if rflg > 1:
            tmp = rev.pop() + tmp+ tmp[::-1]
            rflg-=1
        elif rflg == 1:
            ans += tmp + tmp[::-1]
            tmp = []
            rflg-=1
    elif rflg >0:
        tmp += s[i]
    else:
        ans+=s[i]
print(*ans,sep='')
 