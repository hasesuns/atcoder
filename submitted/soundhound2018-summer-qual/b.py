s = input() #sys.stdin.readlineは最後が改行
w = int(input())

ans = []
for i in range(len(s)):
    if i%w==0:
        ans.append(s[i])

print(*ans,sep='')