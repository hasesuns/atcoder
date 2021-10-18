N, L = list(map(int, input().split()))
S = [0]*N
for i in range(N):
    S[i] = input()

S.sort()
ans = ''.join(S)
print(ans)