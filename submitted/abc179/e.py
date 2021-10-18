import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, x, m = map(int, input().split())

ans = 0

aa = x
ans += aa
aset = set([aa])
alist = [aa]

for i in range(1,n):
    aa = pow(aa,2,m)
    if aa in aset:
        offset = alist.index(aa)
        loop = alist[offset:i]
        nloop, tail = divmod(n-offset, len(loop))
        ans += sum(loop)*(nloop-1)
        ans += sum(loop[0:tail])
        break
    else:
        ans += aa
        aset.add(aa)
        alist.append(aa)

print(ans)
 