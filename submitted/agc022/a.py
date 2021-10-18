s = input() #sys.stdin.readlineは最後が改行
if s=='zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()

s=list(s)
oa = ord('a')
alp = [True]*26
for i in range(len(s)):
    alp[ord(s[i])-oa]=False

if len(s)<26:
    nokori_min =alp.index(True)
    add = chr(nokori_min + ord('a'))
    s+=add

    print(*s,sep='')
    exit()

nokori = []


from bisect import bisect_right

for i in reversed(range(len(s))):
    if ord(s[i-1]) > ord(s[i]):
        nokori.append(s.pop())
    else:
        if nokori == []:
            tmp = s.pop()
            s[-1] = tmp
            break
        else:

            nokori.append(s.pop())
            nokori.sort()
            index = bisect_right(nokori, s[-1])
            s[-1] = nokori[index]
            break

print(*s,sep='')