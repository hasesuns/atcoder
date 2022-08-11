import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, q = map(int, input().split())
s = input()[:-1]
now = 0

for i in range(q):
    t, x = map(int, input().split())
    if t == 2:
        print(s[(now+x-1)%n])
    else:
        now -= t * x