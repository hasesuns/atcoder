import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
q = int(input())

from collections import Counter
cnt = Counter(a)

ans = [sum(a)]

for i in range(q):
    b, c = map(int, input().split())
    cb = cnt[b]
    if cb:
        cnt[b]=0
        cnt[c]+=cb
        ans.append(ans[-1]-cb*b+cb*c)
    else:
        ans.append(ans[-1])

for i in range(1,q+1):
    print(ans[i])