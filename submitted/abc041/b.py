import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a,b,c = map(int, input().split())
p = 10**9+7

a%=p
b%=p
c%=p

print((a*b*c)%p)
 