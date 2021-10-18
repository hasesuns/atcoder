import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
n-=1

ans = []

def Base_10_to_n(X, n, ans):
    if (int(X/n)):
        ans.append(chr(ord('a')+(X%n)))
        return Base_10_to_n(int(X/n)-1, n, ans)+str(X%n)
    ans.append(chr(ord('a')+(X%n)))
    return str(X%n)

num  = Base_10_to_n(n,26, ans)

ans.reverse()

print(*ans,sep='')