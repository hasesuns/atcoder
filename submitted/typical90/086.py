import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, q = map(int, input().split())
xyzw = [tuple(map(int,input().split())) for _ in range(q)]

ans = 1
p = 10 ** 9 + 7

for i_th in range(60):
    cnt = 0
    for bin_num in range(1<<n):
        for x, y, z, w in xyzw:
            x -= 1
            y -= 1
            z -= 1
            x_th_is_1 = (bin_num >> x) & 1
            y_th_is_1 = (bin_num >> y) & 1
            z_th_is_1 = (bin_num >> z) & 1
            i_th_is_1 = (w >> i_th) & 1
            if x_th_is_1 | y_th_is_1 | z_th_is_1 != i_th_is_1:
                break
        else:
            cnt += 1
    ans *= cnt
    ans %= p

print(ans)