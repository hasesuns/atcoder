from collections import Counter
n = int(input())
S = list(input() for i in range(n)) 

ctr = Counter()
ans = 0
for s in S:
    s =  ''.join(sorted(list(s)))
    if s in ctr:
        ans += ctr[s]
    ctr[s] += 1 

print(ans)