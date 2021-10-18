n = int(input())
s = input() #sys.stdin.readlineは最後が改行


lan0 = []
lan1 = []

if s[0]=='#':
    lan0.append(0)

cnt0=0
cnt1=0

for i in range(n):
    if s[i] == '.':
        if cnt1 > 0:
            lan1.append(cnt1)
            cnt1=0
            cnt0=1
        else:
            cnt0+=1
    if s[i] == '#':
        if cnt0 > 0:
            lan0.append(cnt0)
            cnt0=0
            cnt1=1
        else:
            cnt1+=1

if cnt0>0:lan0.append(cnt0)
if cnt1>0:lan1.append(cnt1)



from itertools import accumulate
acc0 = list(reversed(lan0))
acc0 = list(accumulate(acc0))
acc0.reverse()
acc0 = acc0+[0] +[0]


acc1 = [0] + lan1
acc1 = list(accumulate(acc1))
acc1 = [0]+acc1

ans = n
for i in range(len(acc1)):
    ans = min(ans,acc0[i]+acc1[i])

print(ans)