import sys
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

doubled_list = []
cnt_list = []
cnt = 0

for i in range(1,10**6):
    doubled = int(str(i) + str(i))
    doubled_list.append(doubled)
    cnt +=1
    cnt_list.append(cnt)

ans_idx = bisect_right(doubled_list, n) - 1
if ans_idx == -1:
    ans = 0
else:
    ans = cnt_list[ans_idx]

print(ans)