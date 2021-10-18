import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
b = []

if n%2 ==0:
    mae = []
    ushiro = []
    for i in range(0,n,2):
        ushiro.append(a[i])
    for i in reversed(range(1,n,2)):
        mae.append(a[i])
    ans = mae + ushiro
    print(*ans, sep=' ')
else:
    mae = []
    ushiro = []
    for i in range(1,n,2):
        ushiro.append(a[i])
    for i in reversed(range(0,n,2)):
        mae.append(a[i])
    ans = mae + ushiro
    print(*ans, sep=' ')