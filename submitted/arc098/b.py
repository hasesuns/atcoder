import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list( map(int, input().split()))
ans=0
right=0
sum_pls = 0
sum_xor = 0

for left in range(n):

    while right<n and (sum_pls+a[right])==(sum_xor^a[right]):
        sum_pls += a[right]
        sum_xor ^= a[right]
        right+=1

    ans += right - left
    sum_pls -= a[left]
    sum_xor ^= a[left]

print(ans)