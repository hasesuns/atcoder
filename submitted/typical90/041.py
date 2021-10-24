from typing import List, Tuple


def convex_hull(points: List[Tuple[int, int]])->List[Tuple[int, int]]:
    """Monotone Chaineアルゴリズムで凸包を求める
    pointsで与えられる二次元平面上の点を全て包含する最小の凸多角形を形成する頂点のリストを計算して返す。

    Args:
        points (List[Tuple[int, int]]): [description]

    Returns:
        List[Tuple[int, int]]: [description]
    """

    def is_cw_turn(a: Tuple[int, int], b: Tuple[int, int], c: Tuple[int, int]) -> bool:
        """abcが時計回りか否かを判定して返す

        Args:
            a (Tuple[int, int]): [description]
            b (Tuple[int, int]): [description]
            c (Tuple[int, int]): [description]

        Returns:
            bool: [description]
        """
        return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]) > 0

    points.sort()
    lower = []
    for p in points:
        while len(lower) >= 2 and is_cw_turn(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and is_cw_turn(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def calc_polygon_double_area(sorted_points: List[Tuple[int, int]]) -> float:
    """多角形の面積の2倍の値を求める

    Args:
        sorted_points (List[Tuple[int, int]]): [description]

    Returns:
        float: [description]
    """
    double_area = 0
    for (x0, y0), (x1, y1) in zip(sorted_points, sorted_points[1:] + sorted_points[:1]):
        double_area += (x0 - x1) * (y0 + y1)
    double_area = abs(double_area)
    return double_area

def calc_num_boundary_lattice_points(sorted_points: List[Tuple[int, int]]) -> float:
    """多角形の境界上に存在する格子点の個数を求める

    Args:
        sorted_points (List[Tuple[int, int]]): [description]

    Returns:
        float: [description]
    """
    from math import gcd
    num_blp = 0
    for (x0, y0), (x1, y1) in zip(sorted_points, sorted_points[1:] + sorted_points[:1]):
        num_blp += gcd(abs(x1 - x0), abs(y1 - y0)) + 1
    num_blp -= len(sorted_points)
    return num_blp

import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
xy = [tuple(map(int,input().split())) for _ in range(n)]

verex = convex_hull(xy)

#　ピックの定理 S = i + b/2 - 1 を利用する
s_double = calc_polygon_double_area(verex)  # 内部でSを求めると誤差でバグが生まれてしまった。
b = calc_num_boundary_lattice_points(verex)
i = (s_double - b) // 2 + 1  # num_inner_lattice_point

ans = i + b - n
print(ans)