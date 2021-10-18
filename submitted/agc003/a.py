s = input() #sys.stdin.readlineは最後が改行

from collections import Counter

c = Counter(s)

if c['N'] >0 and c['S']==0:
    print('No')
    exit()
if c['S'] >0 and c['N']==0:
    print('No')
    exit()
if c['W'] >0 and c['E']==0:
    print('No')
    exit()
if c['E'] >0 and c['W']==0:
    print('No')
    exit()

print('Yes')