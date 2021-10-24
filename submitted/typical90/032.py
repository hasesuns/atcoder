import itertools
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = [[0]*n for _ in range(n)]    
for i in range(n):
    a[i] = list(map(int, input().split()))

m = int(input())
xy = [tuple(map(int,input().split())) for _ in range(m)]
dislike_list = [[] for _ in range(n)]
for i, (x,y) in enumerate(xy):
    x, y = x - 1, y - 1
    dislike_list[x].append(y)
    dislike_list[y].append(x)

ans = float("inf")
for order in itertools.permutations(list(range(n))):
    tmp = 0
    pre_runner = order[0]
    for leg, runner in enumerate(order):
        tmp += a[runner][leg]
        if runner in dislike_list[pre_runner]:
            break
        pre_runner = runner
    else:
        ans = min(ans, tmp)

if ans == float("inf"):
    ans = -1

print(ans)