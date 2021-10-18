s = input() #sys.stdin.readlineは最後が改行
n = int(s[-1])

if n in [2,4,5,7,9]:
    print('hon')
elif n in [0,1,6,8]:
    print('pon')
else:
    print('bon')
 