n, k = map(int, input().split())
A = list( map(int, input().split()))
F = list( map(int, input().split())) 
A = sorted(A)
F = sorted(F, reverse = True)

def isok(ans):
    k_ = 0
    for a,f in zip(A,F):
        if a > ans//f:
            k_ += a - ans//f
            if k_ > k:
                return False
    return True

ok = max(A)*max(F)
ng = -1 # -1にしとけば答えが0の時も普通に扱えるな

while ok - ng > 1:
    m = (ok+ng)//2
    if isok(m):
        ok = m
    else:
        ng = m
print(ok)