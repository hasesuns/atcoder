n = int(input())
p = 10**9+7
s1 = input() #sys.stdin.readlineは最後が改行
s2 = input() #sys.stdin.readlineは最後が改行

ans = 1
pat = 0
i=0
while i<n:
    if s1[i] == s2[i]:
        if pat==1:
            ans*=2
        elif pat==2:
            ans*=1
        else:
            ans *=3
        ans %=p
        pat=1
        i+=1
    elif s1[i] != s2[i]:
        if pat==1:
            ans*=2
        elif pat==2:
            ans*=3
        else:
            ans *=6
        ans %=p
        pat=2
        i+=2

print(ans%p)