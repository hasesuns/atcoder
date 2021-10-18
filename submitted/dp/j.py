import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))

num3 = a.count(3)
num2 = a.count(2)
num1 = a.count(1)

dp = [[[0]*(num1+num2+num3+1) for _ in range(num2+num3+1)] for _ in range(num3+1)]

for n3 in range(num3+1):
    for n2 in range(num2+num3+1):
        for n1 in range(num1+num2+num3+1):
            if n1 + n2 + n3 == 0: continue
            total = n1 + n2 + n3
            dp[n3][n2][n1] += n / total
            if n1 > 0:
                dp[n3][n2][n1] += n1/total * dp[n3][n2][n1-1]
            if n2 > 0 and n1+1<=num1+num2+num3:
                dp[n3][n2][n1] += n2/total * dp[n3][n2-1][n1+1]
            if n3 > 0 and n2+1<=num2+num3:
                dp[n3][n2][n1] += n3/total * dp[n3-1][n2+1][n1]

print(dp[num3][num2][num1])