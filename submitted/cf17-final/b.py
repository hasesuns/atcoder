s = input() #sys.stdin.readlineは最後が改行

from collections import Counter

c = Counter(s)
cm = c.most_common()

if len(c)==1:
    if len(s)==1:
        print('YES')
    else:
        print('NO')
    exit()

if len(c)==2:
    if len(s)==2:
        print('YES')
    else:
        print('NO')
    exit()

if len(c)==3:
    aa = cm[0][1]
    bb = cm[1][1]
    cc = cm[2][1]
    if aa-cc<2:
        print('YES')
    else:
        print('NO')