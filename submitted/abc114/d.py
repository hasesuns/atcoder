import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from collections import defaultdict

N = int(input())

if N < 10:
    print(0)
    exit()


d = defaultdict(list)
d[2]=7
d[3]=4
d[5]=1
d[7]=1

#nの素因数分解(O(n**0.5)
def prime_factor(n):
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            if d[i] == []: d[i]=1
            else: d[i] += 1
            n = n//i
    if n != 1:
        if d[n] == []: d[n]=1
        else: d[n] += 1

for i in range(10,N+1):
    prime_factor(i)

cand2 = 0
cand4 = 0
cand14 = 0
cand24 = 0
cand74 = 0

for key,val in d.items():
    if val >= 2:
        cand2 += 1
        if val >=4:
            cand4 += 1
            if val >=14:
                cand14 += 1
                if val >=24:
                    cand24 += 1
                    if val >=74:
                        cand74 += 1


ans = 0
ans += cand4  * (cand4-1)//2 * (cand2-2)
ans += cand24 * (cand2-1)
ans += cand14 * (cand4-1)
ans += cand74

print(ans)
 