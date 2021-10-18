import math
import sys
from bisect import bisect_right
from typing import List, Tuple

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
xy = [tuple(map(int, input().split())) for i in range(n)]


def calc_polar_angle_list(x0: int, y0: int, point_list: List[Tuple[int, int]]):
    angle_list = []
    for x, y in point_list:
        angle_list.append(math.atan2(y - y0, x - x0) % (2 * math.pi))

    return angle_list


ans = -1.0
for i, (x_mid, y_mid) in enumerate(xy):
    polar_angle_list = calc_polar_angle_list(x_mid, y_mid, xy[:i] + xy[i + 1 :])
    polar_angle_list.sort()

    for angle in polar_angle_list:

        target1_idx = bisect_right(polar_angle_list, angle + math.pi) % (n - 1)
        target0_idx = (target1_idx - 1) % (n - 1)

        candi0_angle = min(
            (polar_angle_list[target0_idx] - angle) % (2 * math.pi), (angle - polar_angle_list[target0_idx]) % (2 * math.pi)
        )
        candi1_angle = min(
            (polar_angle_list[target1_idx] - angle) % (2 * math.pi), (angle - polar_angle_list[target1_idx]) % (2 * math.pi)
        )

        ans = max(ans, candi0_angle, candi1_angle)

print(math.degrees(ans))