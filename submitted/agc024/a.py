import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a,b,c,k = map(int, input().split())

if k%2==0:
    ans = a-b
else:
    ans = b-a

if abs(ans)>10**18:
    print('Unfair')
else:
    print(ans)