import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

from math import factorial
if n >1:
    a = factorial(n) / factorial(2) / factorial(n - 2)
else: a= 0

if m > 1:
    b = factorial(m) / factorial(2) / factorial(m - 2)
else: b= 0

print(int(a+b))