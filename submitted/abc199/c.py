import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
s = input()
s = list(s[:-1])
q = int(input())

is_flip = False

for i in range(q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if is_flip:
            s[(a+n)%(2*n)], s[(b+n)%(2*n)] = s[(b+n)%(2*n)], s[(a+n)%(2*n)]
        else:
            s[a], s[b] = s[b], s[a]
    else:
        is_flip = not is_flip

if is_flip:
    ans = s[n:] + s[:n]
else:
    ans = s
print(*ans, sep="")