import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, a,b = map(int, input().split())
s = list(int(input()) for i in range(n))

mi = min(s)
ma = max(s)
diff = ma - mi

if diff == 0 and b!=0:
    print(-1)
    exit()

p = b/diff
q = a - sum(s)*p/n

print(p,q)