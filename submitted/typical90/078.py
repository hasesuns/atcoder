import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

ab = [tuple(map(int,input().split())) for _ in range(m)]
cnt_smaller_list = [0] * n
for i, (a,b) in enumerate(ab):
    a, b = a - 1, b - 1
    if a < b:
        cnt_smaller_list[b] += 1
    else:
        cnt_smaller_list[a] += 1

from collections import Counter
c = Counter(cnt_smaller_list)
ans = c[1]
print(ans)