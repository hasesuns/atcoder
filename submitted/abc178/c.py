import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

p = 10**9+7


if n==1:
    print(0)
    exit()

_09 = pow(10,n,p)
_19 = _08 = pow(9,n,p)
_18 =  pow(8,n,p)

print((_09-_19*2+_18)%p)