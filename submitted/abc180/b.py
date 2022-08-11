import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

ma = 0
for xx in x:
    ma += abs(xx)

eu = 0
for xx in x:
    eu += xx**2
eu = eu ** 0.5

ch = max([abs(xx) for xx in x])

print(ma)
print(eu)
print(ch)