import sys

sys.setrecursionlimit(10 ** 9)
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

diff = [[b[j][i]-a[j][i] for i in range(w)] for j in range(h)]

ans = 0

for i in range(h-1):
    for j in range(w-1):
        tmp_val = diff[i][j]
        ans += abs(tmp_val)
        diff[i+1][j] -= tmp_val
        diff[i][j+1] -= tmp_val
        diff[i+1][j+1] -= tmp_val
    if diff[i][w-1] != 0:
        print('No')
        exit()


for j in range(w):
    if diff[h-1][j] != 0:
        print('No')
        exit()

print('Yes')
print(ans)