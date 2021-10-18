import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

h, w, a, b = map(int, input().split())
ans = 0

def dfs(cnt_a, h_j, w_i, floor):
    global ans

    if cnt_a == a:
        ans += 1

        return


    if w_i + 1 == w:  # 右端
        if h_j + 1 == h:  # 下端
            return
        else:  # 右端だが下端ではない
            # 置かない
            dfs(cnt_a, h_j+1, 0, floor)

            if floor[h_j][w_i] == 0:
                # 縦におく
                floor[h_j][w_i] = 1
                floor[h_j+1][w_i] = 1
                dfs(cnt_a+1, h_j+1, 0, floor)
                floor[h_j][w_i] = 0
                floor[h_j+1][w_i] = 0

    else:  # 右端ではない
        # 置かない
        dfs(cnt_a, h_j, w_i+1, floor)

        if floor[h_j][w_i] == 0 and floor[h_j][w_i+1] == 0:
            # 横に置く
            floor[h_j][w_i] = 1
            floor[h_j][w_i+1] = 1
            dfs(cnt_a+1, h_j, w_i+1, floor)
            floor[h_j][w_i] = 0
            floor[h_j][w_i+1] = 0

        if floor[h_j][w_i] == 0 and h_j + 1 < h:  # 下端でも右端でもなく下に置ける
            # 縦に置く
            floor[h_j][w_i] = 1
            floor[h_j+1][w_i] = 1
            dfs(cnt_a+1, h_j, w_i+1, floor)
            floor[h_j][w_i] = 0
            floor[h_j+1][w_i] = 0

floor = [[0 for i in range(w)] for j in range(h)]
dfs(cnt_a=0, h_j=0, w_i=0, floor=floor)

print(ans)