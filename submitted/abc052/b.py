n, a, b = map(int, input().split())
x = list( map(int, input().split()))

ans = 0

for i in range(len(x)-1):
    toho = (x[i+1] - x[i])*a
    if toho <= b:
        ans += toho
    else:
        ans += b

print(ans)