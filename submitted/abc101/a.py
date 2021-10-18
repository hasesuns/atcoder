s = input() #sys.stdin.readlineは最後が改行
p = s.count('+')
m = s.count('-')

print(p-m)