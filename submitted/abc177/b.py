s = input() #sys.stdin.readlineは最後が改行
t = input() #sys.stdin.readlineは最後が改行

ans= 1000

for i in range(len(s)-len(t)+1):
    tmp = 0
    for j in range(len(t)):
        if s[i+j]!=t[j]: tmp+=1

    ans = min(ans,tmp)

print(ans)