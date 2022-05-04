import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 5000
acc = [[0]*(MAX+1) for _ in range(MAX+1)] # 最初に[0]を足しとく

for i in range(n):
    a, b = map(int, input().split())
    acc[a][b] += 1

#ヨコに累積和
for i in range(1,MAX+1):
    for j in range(1,MAX+1):
        acc[i][j] += acc[i-1][j]
#タテに累積和
for i in range(1,MAX+1):
    for j in range(1,MAX+1):
        acc[i][j] += acc[i][j-1]

ans = 0
for row in range(MAX - k):
    for col in range(MAX - k):
        ans = max(ans, acc[row+k+1][col+k+1]+acc[row][col]-acc[row+k+1][col]-acc[row][col+k+1])

print(ans)