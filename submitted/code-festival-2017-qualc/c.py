s = input() #sys.stdin.readlineは最後が改行
n=len(s)
ch = 0
ans = 0
left=0
right=n-1
while left<right:
    if s[left] == s[right]:
        left+=1
        right-=1
    else:
        if s[left] == 'x':
            ans+=1
            left+=1
        elif s[right] =='x':
            ans+=1
            right-=1
        else:
            print(-1)
            exit()
print(ans)