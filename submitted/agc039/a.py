s = input()
k = int(input())
cnt = 0
cntw = 0
cntwflg = False
i = 0

if len(s) == 1:
    print(k//2)
    exit()

if len(list(set(s))) == 1:
    print((k*len(s))//2)
    exit()
while True:
    # print('i, s[i] ', i, s[i])
    if len(s)-1 < i:
        break
    if len(s)-1 == i:
        if s[i] == s[0]:
            cntw = 1
            if s[i-1]==s[i-2]:
                j = 0
                while s[j] == s[j+1]:
                    if j%2 == 0:
                        cntw = 0
                    else:
                        cntw = 1
                    j += 1
    elif s[i] == s[i+1]:
        cnt+= 1
        i += 1
    i += 1


ans = cnt*k+cntw*(k-1)
print(ans)