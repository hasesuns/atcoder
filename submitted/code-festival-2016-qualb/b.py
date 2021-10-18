n, a,b = map(int, input().split())
s = input() #sys.stdin.readlineは最後が改行

tmpab=0
tmpb=0
for i in range(n):
    if s[i] == 'a':
        if tmpab < a+b:
            print('Yes')
            tmpab+=1
        else:
            print('No')
    elif s[i] == 'b':
        if tmpab < a+b and tmpb <b:
            print('Yes')
            tmpab+=1
            tmpb+=1
        else:
            print('No')
    else:
        print('No')
 