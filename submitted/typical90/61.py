from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

q = int(input())
yamafuda = deque()
ans = []

for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        yamafuda.appendleft(x)
    elif t == 2:
        yamafuda.append(x)
    else:
        ans.append(yamafuda[x-1])

print(*ans, sep="\n")