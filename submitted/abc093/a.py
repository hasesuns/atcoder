import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a,b,c = map(int, input().split())

abc = [a,b,c]
abc.sort()

aa = abc[0]
bb = abc[1]
cc = abc[2]

diff = bb-aa
ans = 0
if diff %2==0:
    ans += diff//2
    aa = bb
else:
    ans += diff//2 + 1
    aa = bb
    cc += 1

ans += (cc-bb)*2//2

print(ans)