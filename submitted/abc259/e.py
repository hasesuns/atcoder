import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
pe_list = []

from collections import defaultdict

pnmax = defaultdict(lambda: (0, 0)) #e, cnt
for i in range(n):
    m = int(input())
    pe_list.append([])
    for j in range(m):
        p, e = map(int, input().split())
        pe_list[i].append((p, e))
        e_old, cnt_old = pnmax[p]
        if e_old == e:
            pnmax[p] = (e, cnt_old+1)
        elif e_old < e:
            pnmax[p] = (e, 1)

ans = 0
used_patterns = set()

for i in range(n):
    pattern = []
    for p, e in pe_list[i]:
        e_old, cnt_old = pnmax[p]
        if e == e_old and cnt_old == 1:
            pattern.append((p, e))

    pattern = str(sorted(pattern, key=lambda x: x[0]))
    if pattern not in used_patterns:
        ans += 1
        used_patterns.add(pattern)

print(ans)