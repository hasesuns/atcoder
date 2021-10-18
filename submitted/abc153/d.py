import math
h = int(input())

sou = int(math.log2(h))


ans = 1 + (2**(sou)-2)/(2-1) + 2**(sou)

print(int(ans))