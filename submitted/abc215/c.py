from itertools import permutations

s, k = input().split()

ss = set()
for st in permutations(s):
    ss.add("".join(st))
slist = sorted(list(ss))

ans = slist[int(k)-1]

print(ans)