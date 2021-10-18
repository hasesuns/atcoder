import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

a.sort()

from bisect import bisect_left
from bisect import bisect_right

pos = n - bisect_left(a, 1)
neg = bisect_right(a, -1)


ans_exec = []

if pos>=neg:
    aa = a[max(0,neg-1):n-neg+1]
    for i in range(neg-1):
        ans_exec.append((a[-1-i], a[i]))
        aa.append(a[-1-i] - a[i])
    aa.sort()
    tmp = aa[0]
    for i in range(1,len(aa)-1):
        ans_exec.append((tmp, aa[i]))
        tmp = tmp-aa[i]
    ans_exec.append((aa[-1], tmp))
    ans = aa[-1] - tmp

elif pos<=neg:
    aa = a[max(0,pos-1):n-pos+1]
    for i in range(pos-1):
        ans_exec.append((a[i], a[-1-i]))
        aa.append(a[i] - a[-1-i])
    aa.sort()
    tmp = aa[-1]
    ans_exec.append((aa[-1], aa[0]))
    tmp = aa[-1]-aa[0]
    for i in range(1,len(aa)-1):
        ans_exec.append((tmp, aa[i]))
        tmp = tmp-aa[i]
    ans = tmp


print(ans)
for a,b in ans_exec:
    print(a,b)