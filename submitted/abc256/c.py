import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

(
    h1,
    h2,
    h3,
    w1,
    w2,
    w3,
) = map(int, input().split())

h = [h1, h2, h3]
table = [[0 for _ in range(3)] for _ in range(3)]


ans = 0

w = [0, 0, 0]
for left1 in range(1, h1-1):
    w[0] += left1
    for mid1 in range(1, h1 - left1):
        right1 = h1 - left1 - mid1
        w[1] += mid1
        w[2] += right1
        for left2 in range(1, h2-1):
            w[0] += left2
            for mid2 in range(1, h2 - left2):
                right2 = h2 - left2 - mid2
                w[1] += mid2
                w[2] += right2
                for left3 in range(1, h3-1):
                    w[0] += left3
                    for mid3 in range(1, h3 - left3):
                        right3 = h3 - left3 - mid3
                        w[1] += mid3
                        w[2] += right3
                        if w[0] == w1 and w[1] == w2 and w[2] == w3:
                            ans += 1
                        w[1] -= mid3
                        w[2] -= right3
                    w[0] -= left3
                w[1] -= mid2
                w[2] -= right2
            w[0] -= left2
        w[1] -= mid1
        w[2] -= right1
    w[0] -= left1

print(ans)