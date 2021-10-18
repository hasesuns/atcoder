s = input() #sys.stdin.readlineは最後が改行

l = len(s)
cc = s.count('o')
cc += 15-l
if cc >=8:
    print('YES')
else:
    print('NO')