import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

sa = set(a)
sa = list(sa)

if len(sa)>3:
    print('No')
    exit()

if len(sa)==3:
    aa = sa[0]
    bb = sa[1]
    cc = sa[2]
    if a.count(aa) != n/3 or a.count(bb) != n/3 or a.count(cc) != n/3:
        print('No')
        exit()
    if aa^bb^cc!=0:
        print('No')
        exit()

if len(sa)==2:
    aa = sa[0]
    bb = sa[1]
    if bb != 0 and aa != 0:
        print('No')
        exit()
    else:
        if aa==0:
            aa = bb
    if a.count(0) != n/3 or a.count(aa)!=n/3*2:
        print('No')
        exit()

if len(sa)==1:
    aa = sa[0]
    if aa != 0:
        print('No')
        exit()

print('Yes')
 