import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

now = 0
angle_list = []

for i in range(n):
    now = (now + a[i]) % 360
    angle_list.append(now)

angle_list.append(0)
angle_list.append(360)
angle_list.sort()

diff_list = []
for i in range(n+1):
    diff_list.append(angle_list[i+1]- angle_list[i])

ans = max(diff_list)
print(ans)