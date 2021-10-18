n  = int(input())
a = list( map(int, input().split())) # a1 a2 ... aN

ans=0
right=0
count = 0
left = 0
while left < n:
    while right < n-1 and a[right] >= a[right+1]:
        right+=1

    count = right - left
    ans = max(ans, count)
    count = 0
    right += 1
    left = right

print(ans)