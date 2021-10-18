import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b,k = map(int, input().split())
taka=1
for i in range(k):
    if taka==1:
        if a%2==1:
            a-=1
        b = b+a//2
        a = a//2
        taka = 0
    else:
        if b%2==1:
            b-=1
        a = a+b//2
        b = b//2
        taka = 1

print(a,b)