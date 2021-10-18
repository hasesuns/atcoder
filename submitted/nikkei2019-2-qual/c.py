import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))

a_sort = np.sort(a)
b_sort = np.sort(b)

# 1. 回数関係なくそもそも不可能なやつ → no
# 2-a. サイクルは1つだとしても，完璧じゃない組み合わせが1つ以上許容されるやつ → yes
# 2-b. サイクルが2以上にわけられるやつ → yes

# 1
if (a_sort > b_sort).any():
    print('No')
    exit()

# 2-a
if (a_sort[1:] <= b_sort[:-1]).any():
    print('Yes')
    exit()

# 2-b
index = b.argsort()
a = a[index]
sort_dict = a.argsort().tolist()
start = 0
from_ = start
count = 0
while True:
    count += 1
    from_ = sort_dict[from_]
    if from_ == start:
        break

if count != n:
    print('Yes')
else:
    print('No')

 