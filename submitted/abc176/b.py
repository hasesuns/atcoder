s = list(input()) #sys.stdin.readlineは最後が改行

cnt=0

for ss in s:
    ss = int(ss)
    cnt+=ss
    cnt%=9

if cnt%9==0:
    print('Yes')
else:
    print('No')