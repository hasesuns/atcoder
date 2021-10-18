import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

abcdef = [a,b,c,d,e,f]

from collections import Counter

cc = Counter(abcdef)

ccm = cc.most_common()

if ccm[0][1]==2 and ccm[1][1]==2 and ccm[2][1]==1 and ccm[3][1]==1:
    print('YES')
else:
    print('NO')