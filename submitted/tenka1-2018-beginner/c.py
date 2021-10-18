import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(int(input()) for i in range(n))

a.sort()
if n%2==0:
    start = n//2-1
    left = 0
    right = n-1
    ans0 = abs(a[right]- a[start])
    while start != left:
        ans0+=abs(a[left]-a[right])
        right -= 1
        ans0+=abs(a[right]-a[left])
        left += 1

    start = n//2
    left = 0
    right = n-1
    ans1 = abs(a[left]- a[start])
    while start != right:
        ans1+=abs(a[right]-a[left])
        left += 1
        ans1+=abs(a[left]-a[right])
        right -= 1

    ans = max(ans0,ans1)
    print(ans)

if n%2==1:
    start = n//2
    left = 0
    right = n-1
    ans0 = abs(a[right]- a[start])
    while True:
        ans0+=abs(a[left]-a[right])
        right -= 1
        if start == right: break
        ans0+=abs(a[right]-a[left])
        left += 1


    left = 0
    right = n-1
    ans1 = abs(a[left]- a[start])
    while True:
        ans1+=abs(a[right]-a[left])
        left += 1
        if start == left: break
        ans1+=abs(a[left]-a[right])
        right -= 1

    ans = max(ans0,ans1)
    print(ans)
 