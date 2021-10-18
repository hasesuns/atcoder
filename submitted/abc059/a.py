import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

from itertools import accumulate
acc = a
acc = list(accumulate(acc))

def dfs(ind,prev,tmp,ans):
    if ind == n:
        return ans
    now = acc[ind]

    if prev > 0:
        if now + tmp >= 0:
            ans +=abs(now + tmp +1)
            tmp += -(now + tmp +1)
    elif prev < 0:
        if now + tmp <= 0:
            ans +=abs(now + tmp -1)
            tmp += -(now + tmp -1)

    return dfs(ind+1, now+tmp,tmp,ans)

ansM = dfs(0,-1,0,0)
ansP = dfs(0,+1,0,0)

print(min(ansM,ansP))