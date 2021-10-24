import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
abc = list(map(int, input().split()))
abc.sort()

len = gcd(gcd(abc[0], abc[1]), abc[2])
ans = abc[0] // len - 1 + abc[1] // len - 1 + abc[2] // len - 1
print(ans)