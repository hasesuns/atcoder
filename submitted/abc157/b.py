a11, a12, a13 = map(int, input().split())
a21, a22, a23 = map(int, input().split())
a31, a32, a33 = map(int, input().split())
n = int(input())
b = list(int(input()) for i in range(n))

if a11 in b and a12 in b and a13 in b:
    print('Yes')
    exit()

if a21 in b and a22 in b and a23 in b:
    print('Yes')
    exit()

if a31 in b and a32 in b and a33 in b:
    print('Yes')
    exit()

if a11 in b and a21 in b and a31 in b:
    print('Yes')
    exit()

if a12 in b and a22 in b and a32 in b:
    print('Yes')
    exit()

if a13 in b and a23 in b and a33 in b:
    print('Yes')
    exit()

if a11 in b and a22 in b and a33 in b:
    print('Yes')
    exit()

if a31 in b and a22 in b and a13 in b:
    print('Yes')
    exit()

print('No')
exit()