a, b = map(int, input().split())

pa = int(a * 100/8)
pb = int(b * 100/10)

ans1 = None
ans2 = None

for price in range(pb-1, pa+2):
    if int(price * 0.08) == a and int(price * 0.1) == b:
        ans1 = price
        break

for price in range(pa-1, pb+2):
    if int(price * 0.08) == a and int(price * 0.1) == b:
        ans2 = price
        break

if ans1 is None and ans2 is None:
    print(-1)
elif ans2 is None:
    print(ans1)
elif ans1 is None:
    print(ans2)
else:
    print(min(ans1,ans2))