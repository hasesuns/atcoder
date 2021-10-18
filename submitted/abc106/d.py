import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m, q_ = map(int, input().split())
acc = [[0]*(n+1) for _ in range(n+1)] # 最初に[0]を足しとく

for i in range(m):
    l, r = map(int, input().split())
    acc[l][r]+=1

#ヨコに累積和
for i in range(1,n+1):
    for j in range(1,n+1):
        acc[i][j] += acc[i-1][j]
#タテに累積和
for i in range(1,n+1):
    for j in range(1,n+1):
        acc[i][j] += acc[i][j-1]

ans = [0]*q_

for i in range(q_):
    p, q = map(int, input().split())
    ans[i] = acc[q][q]+acc[p-1][p-1]-acc[p-1][q]-acc[q][p-1]

print(*ans,sep='\n')