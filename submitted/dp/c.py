import sys
input = sys.stdin.readline
n = int(input())
abc = [tuple(map(int,input().split())) for i in range(n)]

dp_a = [0]*n
dp_b = [0]*n
dp_c = [0]*n

a,b,c = abc[0]
dp_a[0] = a
dp_b[0] = b
dp_c[0] = c

for i in range(1,n):
    a, b, c = abc[i]
    dp_a[i] = max(dp_b[i-1]+a, dp_c[i-1]+a)
    dp_b[i] = max(dp_c[i-1]+b, dp_a[i-1]+b)
    dp_c[i] = max(dp_a[i-1]+c, dp_b[i-1]+c)

print(max(dp_a[-1], dp_b[-1], dp_c[-1]))