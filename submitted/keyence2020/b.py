n = int(input())
from collections import defaultdict
d = defaultdict(list)
X = []
xl = [tuple(map(int,input().split())) for i in range(n)]
for x,l in xl:
    d[x].append(x-l)
    d[x].append(x+l)
    X.append(x)

X.sort()


n_remove = 0


for i in range(1,n):
    x_1 = X[i-1]
    x_2 = X[i]
    min_1 , max_1 = d[x_1]
    min_2 , max_2 = d[x_2]

    if max_1 > min_2:
        n_remove += 1
        if max_2 >= max_1:
            d[x_2] = d[x_1]
            X[i] = X[i-1]


ans = n - n_remove
print(ans)