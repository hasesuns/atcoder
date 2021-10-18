import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
color2poslist_dict = defaultdict(list)

for i in range(n):
    x, c = map(int, input().split())
    color2poslist_dict[c].append(x)

# 順番に並び替える
for color, pos_list in color2poslist_dict.items():
    pos_list.sort()
    color2poslist_dict[color] = pos_list

color2poslist_dict[0] = [0]  # 0色目は座標0にあるとする

# dp[i][0 or 1]:i番目のL or Rに来るまでにかかった時間の最小値
dp = [[0]*2 for _ in range(n+1)]
dp[0][0] = dp[0][1] = 0

l_now_pos = r_now_pos = 0
for color in range(1, n+1):
    if color2poslist_dict[color] == []:
        dp[color] = dp[color-1]
        continue
    l_next_pos = color2poslist_dict[color][0]
    r_next_pos = color2poslist_dict[color][-1]

    l2l = abs(r_next_pos - l_now_pos) + abs(l_next_pos - r_next_pos)
    l2r = abs(l_next_pos - l_now_pos) + abs(r_next_pos - l_next_pos)
    r2l = abs(r_next_pos - r_now_pos) + abs(l_next_pos - r_next_pos)
    r2r = abs(l_next_pos - r_now_pos) + abs(r_next_pos - l_next_pos)

    dp[color][0] = min(dp[color-1][0] + l2l, dp[color-1][1] + r2l)
    dp[color][1] = min(dp[color-1][0] + l2r, dp[color-1][1] + r2r)

    l_now_pos = l_next_pos
    r_now_pos = r_next_pos

ans = min(dp[n][0] + abs(0 - l_now_pos), dp[n][1] + abs(0 - r_now_pos) )
print(ans)
 