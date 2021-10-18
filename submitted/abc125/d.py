import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
A = list( map(int, input().split()))

apos = []
aneg = []

for a in A:
    if a >=0: apos.append(a)
    else: aneg.append(a)

apos.sort()
aneg.sort()

if len(aneg) % 2 == 0:
    ans = sum(apos) - sum(aneg)
else:
    if len(apos) == 0:
        ans = - sum(aneg) + 2*aneg[-1]
    else:
        if abs(apos[0]) > abs(aneg[-1]):
            ans = sum(apos) - sum(aneg) -  2*abs(aneg[-1])
        else:
            ans = sum(apos) - sum(aneg) - 2*abs(apos[0])


print(ans)