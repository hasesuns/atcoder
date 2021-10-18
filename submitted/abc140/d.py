n, k = map(int, input().split())
s = input()
ans = 0
isOdd = False
for i in range(0, n-1):
    if s[i] == s[i+1]:
        ans += 1
    else:
        isOdd = not isOdd
        if isOdd and k > 0:
            ans += 2
            k -= 1

print(min(ans, n-1))