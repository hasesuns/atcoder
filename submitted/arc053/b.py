from collections import Counter

s = input() #sys.stdin.readlineは最後が改行
n = len(s)
c=Counter(s)

odd_cnt = 0

for k,v in c.items():
    if v%2!=0:
        odd_cnt +=1

if odd_cnt<=1:
    print(n)
    exit()

pairs = (n-odd_cnt)//2

print(pairs//odd_cnt*2+1)