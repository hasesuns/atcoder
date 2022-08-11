import math
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b, d = map(int, input().split())

rad = d / 180 * math.pi
cos = math.cos(rad)
sin = math.sin(rad)

new_x = (a * cos) - (b * sin)
new_y = (a * sin) + (b * cos)


print(new_x, new_y)