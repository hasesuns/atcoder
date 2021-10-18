s = list(input()) #sys.stdin.readlineは最後が改行

def mergecount(A):
    cnt = 0
    n = len(A)
    if n>1:
        A1 = A[:n>>1]
        A2 = A[n>>1:]
        cnt += mergecount(A1)
        cnt += mergecount(A2)
        i1=0
        i2=0
        for i in range(n):
            if i2 == len(A2):
                A[i] = A1[i1]
                i1 += 1
            elif i1 == len(A1):
                A[i] = A2[i2]
                i2 += 1
            elif A1[i1] <= A2[i2]:
                A[i] = A1[i1]
                i1 += 1
            else:
                A[i] = A2[i2]
                i2 += 1
                cnt += n//2 - i1
    return cnt

ans=0
ss = []
i=0
finish_calc = 0
while i<len(s):
    if s[i]=='A':
        ss.append(1)
        i+=1
        finish_calc=0
    elif i+1<len(s):
        if s[i]=='B' and s[i+1]=='C':
            ss.append(0)
            finish_calc=0
            i+=2
            continue
        if finish_calc==0:
            ans += mergecount(ss)
            ss=[]
            i+=1
            finish_calc=1
        else:
            i+=1
    elif finish_calc==0:
        ans += mergecount(ss)
        ss=[]
        i+=1
        finish_calc=1
    else:
        i+=1

if finish_calc==0:
    ans += mergecount(ss)

print(ans)
 