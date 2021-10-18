import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x,k,d = map(int, input().split())

x = abs(x)

if x == 0:
    if k % 2 == 0:
        print(0)
        exit()
    else:
        print(abs(d))
        exit()

bai = x//d

if bai >= k:
    print(x-k*d)
    exit()
else:
    x -= bai*d
    if (k-bai)%2==0:
        print(x)
        exit()
    else:
        print(abs(x-d))

 