s = input() #sys.stdin.readlineは最後が改行
t = input() #sys.stdin.readlineは最後が改行
n = len(s)
ans = 0
for i in range(n):
    if s[i]!=t[i]:
        ans+=1

print(ans)