s = input() #sys.stdin.readlineは最後が改行

ans = 0

block = int(s[0])
if block==0: not0 = 0
else: not0 = 1

ans = 0

for i in range(1,len(s)-1,2):

    enzanshi = s[i]
    number = int(s[i+1])
    if enzanshi == "+":
        ans += not0
        if number==0: not0 = 0
        else: not0 = 1
    else:
        not0 = not0*(number!=0)

    # print(not0)

ans += not0

print(ans)