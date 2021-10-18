s = input() #sys.stdin.readlineは最後が改行
n =len(s)

from collections import defaultdict
amari = defaultdict(lambda:0)
amari[0]=1
num=0
tmp=0

for i in range(n):
    num = tmp + int(s[-1-i])*pow(10,i,2019)
    tmp = num%2019
    amari[tmp]+=1

from math import factorial

ans = 0
for key,val in amari.items():
    if val>1:
        ans +=val*(val-1)//2

print(ans)