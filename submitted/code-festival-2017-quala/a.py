s = input() #sys.stdin.readlineは最後が改行

ind = s.find('YAKI')
if ind ==0:
    print('Yes')
else:
    print('No')