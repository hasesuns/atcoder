x = input() #sys.stdin.readlineは最後が改行
n = len(x)

tama = 0
cnt = 0
for i in range(n):
    if x[i] =='S':
        tama+=1
    elif x[i] =='T' and tama>0:
        cnt += 2
        tama-=1
print(n-cnt)