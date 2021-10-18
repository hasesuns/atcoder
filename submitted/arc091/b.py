import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, K = map(int, input().split())
ans = 0

if K == 0:
    ans = N*N
    print(ans)
    exit()

for b in range(K+1, N+1):
    ans += N // b * (b - K)
    ans += max(N % b - K + 1, 0)
    
print(ans)