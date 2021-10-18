s = input() #sys.stdin.readlineは最後が改行

if len(s)==2:
    print(s)
else:
    print(s[::-1])