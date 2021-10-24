import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
a.append(l)

def isok(ans):
    prev_pos = 0
    cnt_cut = 0
    for i in range(n+1):
        if a[i] - prev_pos >= ans:
            prev_pos = a[i]
            cnt_cut += 1

    if cnt_cut >= k+1:
        return True
    else:
        return False

ok = -1
ng = l + 1

while ng - ok > 1:
    m = (ok+ng)//2
    if isok(m):
        ok = m
    else:
        ng = m
print(ok)