s = list(input()) #sys.stdin.readlineは最後が改行
t = list(input()) #sys.stdin.readlineは最後が改行
ls=len(s)

from collections import defaultdict
d = defaultdict(list)

from bisect import bisect_right

for i in range(ls):
    d[s[i]].append(i+1)

ans = 0
prev =0
for i in range(len(t)):
    index = d[t[i]]
    if len(index)==0:
        print(-1)
        exit()
    elif len(index)==1:

        if index[0] <= prev:
            ans+=(ls-prev)+index[0]
        else:
            ans+=index[0]-prev
        prev = index[0]
    else:
        nex = bisect_right(index, prev)
        if nex == len(index):
            ans += (ls-prev)+index[0]
            prev = index[0]
        else:
            ans+= index[nex]-prev
            prev = index[nex]

print(ans)