a, b, k = map(int, input().split())

eatenA = min(a , k)
ans1 = a - eatenA
eatenB = max(k - a, 0)
ans2 = b -  eatenB

if ans2 < 0:
    ans2 = 0

print(ans1, ans2 )