import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
x = list( map(int, input().split()))

ans = float('inf')
for i in range(n-k+1):
    left = x[i]
    right = x[i+k-1]
    if left <= 0 <= right:
        tmp = -(left) + right
        tmp += min(-left,right)
        ans = min(ans,tmp)
    elif 0 < left:
        ans = min(ans,right)
    elif right < 0:
        ans = min(ans,abs(left))

print(ans)