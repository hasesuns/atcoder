m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())

if m1 == 12:
    if m2 == 1:
        print(1)
        exit()

if m1 + 1 == m2:
    print(1)
    exit()
else:
    print(0)