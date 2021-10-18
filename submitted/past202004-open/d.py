s = input() #sys.stdin.readlineは最後が改行
n=len(s)
one  =  set(list(s))

two01 = []
twoX1 = []
two0X = []
for i in range(n-1):
    two01.append(s[i]+s[i+1])
    twoX1.append(s[i+1])
    two0X.append(s[i])
two01 = set(two01)
twoX1 = set(twoX1)
two0X = set(two0X)

thr012 = []
thrX12 = []
thr0X2 = []
thr01X = []
thr0XX = []
thrX1X = []
thrXX2 = []

for i in range(n-2):
    thr012.append(s[i]+s[i+1]+s[i+2])
    thrX12.append(s[i+1]+s[i+2])
    thr0X2.append(s[i]+s[i+2])
    thr01X.append(s[i]+s[i+1])
    thr0XX.append(s[i])
    thrX1X.append(s[i+1])
    thrXX2.append(s[i+2])

thr012 = set(thr012)
thrX12 = set(thrX12)
thr0X2 = set(thr0X2)
thr01X = set(thr01X)
thr0XX = set(thr0XX)
thrX1X = set(thrX1X)
thrXX2 = set(thrXX2)

ans = len(one)+1+len(two01)+len(twoX1)+len(two0X)\
    + len(thr012)+len(thrX12)+len(thr0X2)+len(thr01X)+len(thr0XX)+len(thrX1X)+len(thrXX2)

if n>1: ans+=1
if n>2: ans+=1

print(ans)