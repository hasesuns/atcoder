import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

h, w, n = map(int, input().split())
ab = [tuple(map(int,input().split())) for _ in range(n)]
used_h = []
used_w = []

for a, b in ab:
    used_h.append(a)
    used_w.append(b)

sorted_used_h = sorted(list(set(used_h)))
sorted_used_w = sorted(list(set(used_w)))

h_to_new_h = {hh: i+1  for i, hh, in enumerate(sorted_used_h)}
w_to_new_w = {ww: i+1  for i, ww, in enumerate(sorted_used_w)}


ans = []
for a, b in ab:
    ans.append(f"{h_to_new_h[a]} {w_to_new_w[b]}")

print(*ans, sep='\n')