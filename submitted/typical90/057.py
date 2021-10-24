import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
MOD = 998244353

n, m = map(int, input().split())
A = [[0]*m for _ in range(n)]
for i in range(n):    
    t = int(input())
    a_list = list(map(int, input().split()))
    for a in a_list:
        A[i][a-1] = 1
s = list(map(int, input().split()))

def gauss_jordan_bit(bimat, is_extended: bool = False):
    rank: int = 0
    pivot_row2col_list = []
    h = len(bimat)
    w = len(bimat[0])
    for ww in range(w):
        if is_extended and ww == w - 1:
            break
        pivot = -1
        for hh in range(rank, h):
            if bimat[hh][ww]:
                pivot = hh
                break
        if pivot == -1: continue
        pivot_row2col_list.append(ww)
        bimat[pivot], bimat[rank] = bimat[rank], bimat[pivot]
        for hh in range(h):
            if hh != rank and bimat[hh][ww]:
                for j in range(w):
                    bimat[hh][j] ^= bimat[rank][j]
        rank += 1
    return (pivot_row2col_list, bimat, rank)

pivot_row2col_list, bimat, rank = gauss_jordan_bit(A)
pivot_col2row_list = [-1] * m
for row, col in enumerate(pivot_row2col_list):
    pivot_col2row_list[col] = row

goal = s[:]
for col_idx in range(m):
    if goal[col_idx] == 0:
        continue
    bimat_row_idx = pivot_col2row_list[col_idx]
    if bimat_row_idx == -1:  # Sに含まれているのに行列に存在していないパネルがあった時
        print(0)
        exit()
    for i in range(col_idx, m):
        goal[i] ^= bimat[bimat_row_idx][i]

print(pow(2, n-rank, mod=MOD))