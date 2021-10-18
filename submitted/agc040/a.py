s = input() #sys.stdin.readlineは最後が改行
n = len(s)

INF = float('inf')

a = [-INF]*(n+1)

for i in range(n):
    if i==0 and s[i] =='<':
        a[i]=0
        continue
    if i==n-1:
        if s[i] =='>':
            a[i+1]=0
        continue

    if s[i] =='>' and s[i+1]=='<':
        a[i+1]=0


def left(i):
    while True:
        if i ==0:
            break
        if s[i-1] == '>' and a[i-1] <=a[i]:
            a[i-1]=a[i]+1
        else:
            break
        i-=1

def right(i):
    while True:
        if i==n:
            break
        if s[i] == '<' and a[i]>=a[i+1]:
            a[i+1]=a[i]+1
        else:
            break
        i+=1

for i in range(n+1):
    if a[i] == 0:
        left(i)
        right(i)

print(sum(a))