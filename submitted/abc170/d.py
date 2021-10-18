import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
a.sort()

from collections import Counter
cnt = Counter(a)

if a[0]==1:
    if cnt[1]==1:
        print(1)
    else:
        print(0)
    exit()

limit = a[-1]
is_prime = [0] * (limit + 1)

for aa in a:
    is_prime[aa]=1

for i in range(2, limit + 1):

    if is_prime[i]==0:
        continue
    for j in range(i * 2, limit + 1, i):
        is_prime[j] = 0

ans=0

for i in range(1,limit+1):
    if is_prime[i] and cnt[i] < 2:
        ans+=1

print(ans)

 