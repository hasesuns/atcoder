s = list(input()) #sys.stdin.readlineは最後が改行
k = int(input())

now = 0

while k>0 and now<len(s):
    if s[now]=='a':
        now+=1
        continue
    tmp = ord('z')-ord(s[now])+1
    if tmp<=k:
        s[now] = 'a'
        k -= tmp
        now+=1
    else:
        now+=1

if k>0:
    s[-1] = chr(ord(s[-1])+k%26 )

print(*s,sep='')