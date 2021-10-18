import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

ans = 10**3
for a in range(1,n):
    b = n-a
    tmp = 0
    for j in reversed(range(len(str(a)))):
        tmpa = (a//(10**j))
        a -= tmpa*(10**j)
        tmp += tmpa
    for j in reversed(range(len(str(b)))):
        tmpb = (b//(10**j))
        b -= tmpb*(10**j)
        tmp += tmpb

    ans = min(ans,tmp)

print(ans)