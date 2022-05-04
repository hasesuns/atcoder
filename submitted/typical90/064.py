import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))

diff_list = [0] * (n+1)
ans = [0] * (q+1)
for i in range(n+1):
    diff_list[i] = a[i%n] - a[i-1]
    if (i > 0 and i < n):
        ans[0] += abs(diff_list[i])

for i in range(q):
    l, r, v = map(int, input().split())
    l, r = l-1, r-1
    ans[i+1] = ans[i]
    if l > 0:
        ans[i+1] += - abs(diff_list[l]) + abs(diff_list[l] + v)
    if r < n-1:
        ans[i+1] += - abs(diff_list[r+1]) + abs(diff_list[r+1] - v)
    diff_list[l] += v
    diff_list[r+1] -= v
        
print(*ans[1:], sep='\n')