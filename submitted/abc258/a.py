import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

k = int(input())

hh = k // 60 + 21
mm = k % 60

sh = str(hh)
sm = str(mm)

if len(sh) == 1:
    sh = "0" + sh
if len(sm) == 1:
    sm = "0" + sm

ans = sh + ":" + sm
print(ans)