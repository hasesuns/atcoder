import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

r, x, y = map(int, input().split())

dist = (x**2+y**2)**0.5

if dist < r:
    ans = 2
else:
    ans = int(- (-dist//r))

print(ans)