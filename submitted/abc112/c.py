n = int(input())
xyh = [tuple(map(int,input().split())) for i in range(n)]

candidates =[]

for cx in range(101):
    for cy in range(101):
        ch = None
        for x,y,h in xyh:
            if h == 0:

                continue
            if ch == None:
                ch = h + abs(x-cx) + abs(y-cy)
                continue

            if ch != h + abs(x-cx) + abs(y-cy):
                break

        else:
            xyh_c = (cx, cy, ch)
            candidates.append(xyh_c)

for xyh_c in candidates:
    cx, cy, ch = xyh_c
    for x,y,h in xyh:
        if h != max(ch - abs(x-cx) - abs(y-cy) ,0):
            break
    else:
        print(cx, cy, ch)
        exit()
 