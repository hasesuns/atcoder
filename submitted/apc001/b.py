import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
b = list( map(int, input().split()))

sa = sum(a)
sb = sum(b)

al = sb-sa

if al<0:
    print('No')
    exit()

doub = 0
sing = 0

for i in range(n):
    diff = b[i]-a[i]
    if diff > 0:
        doub += -(-diff//2)
        sing += diff%2
    if diff < 0:
        sing += -diff

dnokori = al - doub
snokori = al - sing

if dnokori < 0 or snokori<0:
    print('No')
    exit()

if dnokori==0 and snokori==0:
    print('Yes')
    exit()

if dnokori==0:
    print('No')
    exit()

if snokori/dnokori == 2:
    print('Yes')
else:
    print('No')
 