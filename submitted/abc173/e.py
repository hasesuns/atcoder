import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list( map(int, input().split()))
p = 10**9+7

a.sort()

from bisect import bisect_left, bisect_right
zerostart = bisect_left(a, 0)
posstart = bisect_right(a, 0)

aneg = a[:zerostart]
cntzero = posstart - zerostart
apos = a[posstart:]

cntneg = len(aneg)
cntpos = len(apos)

# 答えが0になる時
if k > n-cntzero:
    print(0)
    exit()

# 答えが正になる時
if k <= cntpos or (k%2==0 and  k <= (cntneg//2)*2 + cntpos) or (k%2==1 and cntpos%2==1 and k <= (cntneg//2)*2 + cntpos-1):
    pos_pair_mix=[]

    apos.sort(reverse=True)
    for i in range(cntpos//2):
        pos_pair_mix.append((apos[2*i]*apos[2*i+1],+1,2*i))

    for i in range(cntneg//2):
        pos_pair_mix.append((aneg[2*i]*aneg[2*i+1],-1,2*i))

    pos_pair_mix.sort(key=lambda x:x[0],reverse=True)

    ans = 1
    i_last_apos=0

    for i in range(k//2):
        ans*=pos_pair_mix[i][0]%p
        ans%=p
        if pos_pair_mix[i][1]==1:
            i_last_apos = pos_pair_mix[i][2]+2

    if k%2==0:
        print(ans%p)
        exit()
    else:
        print((ans*apos[i_last_apos])%p)
        exit()

# 答えが負になる時
a.sort(key=lambda x:abs(x) )

ans = 1
for i in range(k):
    ans*=a[i]
    ans%=p

print(ans%p)