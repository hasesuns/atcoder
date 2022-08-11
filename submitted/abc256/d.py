import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
lr = [tuple(map(int,input().split())) for _ in range(n)]
lr = sorted(lr, key=lambda x: (x[0], x[1]))

l_now, r_now = lr[0]
ans = []
for l, r in lr[1:]:
    if l <= r_now:
        r_now = max(r, r_now)
    else:
        ans.append(f"{l_now} {r_now}")
        l_now = l
        r_now = r
ans.append(f"{l_now} {r_now}")

print(*ans, sep="\n")