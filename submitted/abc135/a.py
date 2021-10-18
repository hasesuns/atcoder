a, b = list(map(int, input().split()))

if a < b:
    a1 = a
    a2 = b
else:
    a1 = b
    a2 = a

K = (a1 + a2)/2.
if K.is_integer():
    print(int(K))
else:
    print('IMPOSSIBLE')