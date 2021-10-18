s = input() #sys.stdin.readlineは最後が改行
n=len(s)

from collections import Counter
c = Counter(s)
cnt = 0

for k,v in c.items():
    if v>1:
        cnt+=v*(v-1)//2

ans = n*(n-1)//2 -cnt + 1

print(ans)