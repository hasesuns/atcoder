s = input()
t = input()

from itertools import groupby

def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

srle = runLengthEncode(s)
trle = runLengthEncode(t)

if len(srle) != len(trle):
    print('No')
    exit()

for i, (ss, snum) in enumerate(srle):
    tt, tnum = trle[i]
    if ss != tt:
        print('No')
        exit()
    if snum == tnum:
        continue
    elif snum >= 2 and snum <= tnum:
        continue
    else:
        print('No')
        exit()

print('Yes')