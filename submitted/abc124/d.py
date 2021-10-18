import sys
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
s = input()

scomp = []

cnt = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        cnt += 1
    else:
        scomp.append(cnt)
        cnt = 1
scomp.append(cnt)


lens = len(scomp)
ans = 0

start = 0
if s[0] == '0':
    start = 1
    end = min(k*2,lens)
    tmp = sum(scomp[:end])
    ans = max(ans,tmp)

end = min(start + k*2+1,lens)
tmp = sum(scomp[start:end])
ans = max(ans,tmp)
for i in range(start,lens-k*2-2,2):
    tmp -= scomp[i]
    tmp -= scomp[i+1]
    tmp += scomp[i+k*2+1]
    tmp += scomp[i+k*2+2]
    ans = max(ans,tmp)

if s[-1] == '0':
    start = max(lens-k*2,0)
    tmp = sum(scomp[start:])
    ans = max(ans,tmp)

print(ans)
 