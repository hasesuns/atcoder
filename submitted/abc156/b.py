import math
n, k = map(int, input().split())

if n == 1:
    print(1)
    exit()

ans = - (-math.log(n)//math.log(k))

print(int(ans))