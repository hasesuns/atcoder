import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b,x = map(int, input().split())

def isok(ans):
    if ans > 10**9:
        return False

    tmp = a * ans
    tmp += b*len(str(ans))

    if tmp <= x:
        return True
    else:
        return False

ok = 0
ng = 10**9+1

while ng - ok > 1:
    m = (ok+ng)//2
    if isok(m):
        ok = m
    else:
        ng = m
print(ok)