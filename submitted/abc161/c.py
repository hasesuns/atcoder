n, k = map(int, input().split())

ans1 = n%k
ans2 = k - n%k
print(min(ans1,ans2))