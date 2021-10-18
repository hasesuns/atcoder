s = input() #sys.stdin.readlineは最後が改行

n = len(s)
hn = (n-1)//2
hs = s[:hn]

for i in range(hn):
    if s[i] != s[-1-i]:
        print('No')
        exit()
    if hs[i] != hs[-1-i]:
        print('No')
        exit()

print('Yes')

 