n, k = map(int, input().split())
p = list( map(int, input().split()))
ans = 0
for i in range(k):
    ans += (1+p[i])*p[i]/2/p[i]

ans_ = ans

for left in range(1,n-k+1):
    ans_ -= (1+p[left-1])*p[left-1]/2/p[left-1]
    ans_ += (1+p[left+k-1])*p[left+k-1]/2/p[left+k-1]
    ans = max(ans, ans_)


print(ans)