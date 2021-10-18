n = int(input())
s = input() #sys.stdin.readlineは最後が改行

rcount = 0
rmargin = 0
lcount = 0
lmargin = 0
for i in range(n):
    if s[i] == ')':
        if rmargin ==0: rcount +=1
        else: rmargin -= 1
    else: rmargin +=1

    if s[-1-i] == '(':
        if lmargin ==0: lcount +=1
        else: lmargin -= 1
    else: lmargin +=1

ans = '('*rcount + s + ')'*lcount
print(ans)