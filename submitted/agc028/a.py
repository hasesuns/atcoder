import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
s = input() #sys.stdin.readlineは最後が改行
t = input() #sys.stdin.readlineは最後が改行

from fractions import gcd

gcdnm = gcd(n, m)
L = (n * m) // gcdnm

gcdd = gcd(L//n, L//m)
l = (L//n *L//m) // gcdd


if s[0]!=t[0]:
    print(-1)
    exit()

i = 1


while l//(L//n)*i < n and l//(L//m)*i <m:
    if s[l//(L//n)*i] != t[l//(L//m)*i]:
        print(-1)
        exit()
    i+=1

print(L)


 