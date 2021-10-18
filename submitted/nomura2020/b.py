t = list(input()) #sys.stdin.readlineは最後が改行
n=len(t)
for i in range(n):
    if t[i] == '?':
        t[i]='D'
print(*t,sep='')