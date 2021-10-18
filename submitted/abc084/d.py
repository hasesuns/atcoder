import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

q = int(input())

def eratosthenes2(limit):
    is_prime = [1] * (limit + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]==0:
            continue
        for j in range(i * 2, limit + 1, i):
            is_prime[j] = 0
    return is_prime

limit = 10**5

is_prime = eratosthenes2(limit)
prime_list = [i for i in range(limit + 1) if is_prime[i]]

like_2017=[0]*limit

for p in prime_list:
    if is_prime[(p+1)//2]==1:
        like_2017[p] = 1

from itertools import accumulate
B = [0] + like_2017
B = list(accumulate(B))

ans=[0]*q
for i in range(q):
    l, r = map(int, input().split())
    ans[i]=B[r+1]-B[l]

print(*ans,sep='\n')