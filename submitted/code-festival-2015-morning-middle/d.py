import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
s = input() #sys.stdin.readlineは最後が改行


def chmax(a, b):
    if a >= b:
        return a
    else:
        return b
def lcs(S, T):
    dp = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] == T[j]:
                dp[i+1][j+1] = chmax(dp[i+1][j+1], dp[i][j] + 1)
            dp[i+1][j+1] = chmax(dp[i+1][j+1], dp[i+1][j])
            dp[i+1][j+1] = chmax(dp[i+1][j+1], dp[i][j+1])
    ans = ''
    i = len(S)
    j = len(T)
    while (i>0  and j>0):
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            ans += s[i-1]
            i -= 1
            j -= 1

    return ans[::-1]

maxheholen = 0
for i in range(1,n):
    heho = lcs(s[:i],s[i:])
    if len(heho) > maxheholen:
        maxheholen = len(heho)

print(n-maxheholen*2)