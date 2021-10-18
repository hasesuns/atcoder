n, a, b = map(int, input().split())

if (b-a)%2 == 0:
    print((b-a)//2)
else:
    if (a-1) <= (n-b):
        print(a-1 + 1 +(b-a-1)//2)
    else:
        print(n-b + 1 +(b-a-1)//2)