s = input() #sys.stdin.readlineは最後が改行

if 'RRR' in s:
    print(3)
elif 'RR' in s:
    print(2)
elif 'R' in s:
    print(1)
else:
    print(0)