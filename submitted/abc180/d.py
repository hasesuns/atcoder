import sys
from math import log

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x, y, a, b = map(int, input().split())

exp = 0
strength = x
if b / (a - 1) < strength:
    can_b_to_y = max((y - 1 - strength), 0) // b
    ans = int(can_b_to_y)
    print(ans)
    exit()
else:
    can_a_to_bound = int(log(max((b / (a - 1)) / strength, 1), a))
    can_a_to_y = int(log(max((y - 1) / strength, 1), a))
    if can_a_to_y < can_a_to_bound:
        ans = int(can_a_to_y)
        print(ans)
        exit()
    else:
        exp = can_a_to_bound
        strength = strength * (a ** can_a_to_bound)
        can_b_to_y = max((y - 1 - strength), 0) // b
        ans = int(exp + can_b_to_y)
        print(ans)
        exit()