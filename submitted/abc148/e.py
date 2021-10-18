n = int(input())
ans = 0
if n % 2 != 0:
    print(0)
    exit()
denominator = 10
while n >= denominator:
    ans += n//denominator
    denominator *= 5

print(ans)