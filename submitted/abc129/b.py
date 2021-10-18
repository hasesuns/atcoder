from itertools import accumulate

N = int(input())
W = [int(_) for _ in input().split()]

W_ = [0] + W
sumW = list(accumulate(W_))

ans = float('inf')

for T in range(N):
    S1 = sumW[T]
    S2 = sumW[N] - sumW[T]
    ans = min(ans, abs(S1 - S2))

print(ans)