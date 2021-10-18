k = int(input())

s = input() #sys.stdin.readlineは最後が改行

if len(s)<=k:
    print(s)
else:
    ans = s[:k]+'...'
    print(ans)