n = int(input())
s = input() #sys.stdin.readlineは最後が改行
k = int(input())

tt = s[k-1]

ans = []
for i in range(n):
    if s[i]!=tt:
        ans.append('*')
    else:
        ans.append(tt)

print(*ans,sep='')