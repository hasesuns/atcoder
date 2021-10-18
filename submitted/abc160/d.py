import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, x, y = map(int, input().split())
ans = [0]*(n)

for i in range(1,n+1):
    for j in range(i+1,n+1):
        num = j-i
        num = min(num, abs(x-i)+abs(y-j)+1 )
        ans[num] += 1


print(*ans[1:], sep='\n')
 