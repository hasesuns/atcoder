s = input() #sys.stdin.readlineは最後が改行

if s[-1]!='s':
    ans = s+'s'
else:
    ans = s+'es'

print(ans)