import itertools
import math


n =int(input())
xy= [tuple(map(int,input().split())) for i in range(n)]

nfact = math.factorial(n)

sum = 0

perm = list(itertools.permutations(xy))

for i in range(nfact):
    xy_ = perm[i]
    dist = 0
    for j in range(0,n-1):
        x1, y1 = xy_[j]
        x2, y2 = xy_[j+1]
        dist += ( (x1-x2)**2 + (y1-y2)**2 )**0.5
    sum += dist

ans = sum/nfact

print(ans)