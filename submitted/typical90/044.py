import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
txy = [tuple(map(int,input().split())) for _ in range(q)]

idx_list = list(range(n))
offset = 0

for i in range(q):
    t, x, y = txy[i]
    if t == 1:
        a[(x-1+offset)%n], a[(y-1+offset)%n] = a[(y-1+offset)%n], a[(x-1+offset)%n]
    elif t == 2:
        offset += n-1
    else:
        idx = idx_list[(i+offset)%n]
        print(a[(x-1+offset)%n])