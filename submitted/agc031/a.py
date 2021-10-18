n = int(input())
s = list(input())
p=10**9+7

from collections import Counter

c = Counter(s)

ans = 1
for k,v in c.items():
    ans *=(v+1)%p

ans -=1
print(ans%p)