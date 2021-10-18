from collections import Counter

n = int(input())
d = list( map(int, input().split()))
c=Counter(d)
dmax = max(d)
MOD = 998244353

if d[0] != 0:
    print(0)
    exit()

if len(c)-1 != dmax:
    print(0)
    exit()

if c[0] != 1:
    print(0)
    exit()

ans = 1

for i in range(1,dmax):
    ans *= c[i]**c[i+1]
    ans %= MOD

print(ans)