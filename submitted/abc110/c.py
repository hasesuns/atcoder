s = input() #sys.stdin.readlineは最後が改行
t = input() #sys.stdin.readlineは最後が改行

n = len(s)

from collections import defaultdict
ds = defaultdict(list)
dt = defaultdict(list)

for i in range(n):
    if s[i] in ds.keys():
        if ds[s[i]] != t[i]:
            print('No')
            exit()
    else:
        ds[s[i]] = t[i]

for i in range(n):
    if t[i] in dt.keys():
        if dt[t[i]] != s[i]:
            print('No')
            exit()
    else:
        dt[t[i]] = s[i]

print('Yes')