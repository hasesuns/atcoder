import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
b = list(map(int, input().split()))

WMAX = 50
BMAX = (WMAX + 1) * WMAX // 2 + WMAX
grundy_nums = [[float("inf")] * (BMAX + 1) for _ in range(WMAX + 1)] 

for ww in range(WMAX + 1):
    for bb in range(BMAX+1):
        inclued = [False] * (BMAX + 1) 
        if ww == 0 and bb <= 1:
            grundy_nums[ww][bb] = 0
            continue
        if ww >= 1 and bb + ww <= BMAX:
            inclued[grundy_nums[ww - 1][bb + ww]] = True
        for k in range(1, bb // 2 + 1):
            inclued[grundy_nums[ww][bb - k]] = True
        mex = inclued.index(False)
        grundy_nums[ww][bb] = mex
    BMAX -= ww

grundy_num = 0
for ww, bb in zip(w,b):
    grundy_num ^= grundy_nums[ww][bb]

if grundy_num == 0:
    print("Second")
else:
    print("First")