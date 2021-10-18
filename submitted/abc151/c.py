n, m = map(int, input().split())

from collections import defaultdict
d = defaultdict(list)
ab = [tuple(input().split()) for i in range(m)]

nAC = 0
nWA = 0


for a,b in ab:
    a = int(a)


    if len(d[a]) == 0:
        flag = 0
        num = 0
        d[a].append((flag, num))
    else:
        flag, num = d[a]


    if flag == 1:
        continue

    if flag == 0 and b == 'AC':
        flag = 1

    if flag == 0 and b == 'WA':
        num += 1

    d[a] = (flag, num)


for flag, num in d.values():
    if flag == 1:
        nAC += 1
        nWA += num

print(nAC, nWA)