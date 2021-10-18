import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
x = 1

isT = True

is_even = (len(bin(n))-2) %2 == 0

while x <= n:
    if isT^is_even:
        x = 2*x+1
    else:
        x = 2*x
    isT = not isT

if isT:
    print('Takahashi')
else:
    print('Aoki')
 