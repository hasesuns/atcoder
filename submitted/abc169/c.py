import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
from decimal import *


a, b = input().split()

a = int(a)
b = Decimal(b)

print(int(a*b))
 