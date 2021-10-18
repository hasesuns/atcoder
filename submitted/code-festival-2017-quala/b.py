import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

h, w, k= map(int, input().split())

if k%h==0 or k%w==0:
    print('Yes')
    exit()

for i in range(1,w):
    if w-i*2 != 0:
        if (k-i*h) % (w-i*2) == 0 and 0<(k-i*h) // (w-i*2)<=h:
            print('Yes')
            exit()

for i in range(1,h):
    if h-i*2 != 0:
        if (k-i*w) % (h-i*2) == 0 and 0<(k-i*w) // (h-i*2)<=w:
            print('Yes')
            exit()

print('No')