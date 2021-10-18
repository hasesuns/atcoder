r = [i for i in range(1,101)]
r.reverse()

ans = []

y=39
x=0

while len(r):
    while x+2*r[-1]<=1500 and len(r):
        rr = r.pop()
        ans.append((x+rr,y))
        x= x+2*rr

        if len(r) == 0:
            break

    y = y+rr+rr+1

    if len(r)==0:
        break

    while x-2*r[-1]>=0 and len(r):
        rr = r.pop()
        ans.append((x-rr,y))
        x= x-2*rr

        if len(r) == 0:
            break

    y = y+rr+rr+1

    if len(r)==0:
        break

for i in range(100):
    print(*ans[i])