import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, s = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

# dp[i][j]:i番目以前の商品を見たときの価値総和jが可能かどうか
dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True
select_item = [[None]*(s+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(s):
        if j+a[i-1] <= s and dp[i-1][j]:
            dp[i][j+a[i-1]] = True
            select_item[i][j+a[i-1]] = "A"
        if j+b[i-1] <= s and dp[i-1][j]:
            dp[i][j+b[i-1]] = True          
            select_item[i][j+b[i-1]] = "B"

if dp[n][s] == False:
    print("Impossible")
    exit()
    
ans = []
tmp = s
for i in range(n, 0, -1):
    if select_item[i][tmp] == "A":
        ans.append("A")
        tmp -= a[i-1]
    elif select_item[i][tmp] == "B":
        ans.append("B")
        tmp -= b[i-1]

ans.reverse()
print(*ans, sep="")