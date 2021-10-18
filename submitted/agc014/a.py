import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a,b,c = map(int, input().split())

if a%2==1 or b%2==1 or c%2==1:
    print(0)
    exit()

if a==b==c and a%2==0:
    print(-1)
    exit()

sabc = a+b+c

cnt = 0
while True:
    a = (sabc-a)/2
    b = (sabc-b)/2
    c = (sabc-c)/2
    cnt+=1
    if a%2==1 or b%2==1 or c%2==1: break

print(cnt)