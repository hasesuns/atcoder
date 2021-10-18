n, a, b = map(int, input().split())

ab = a + b
ans = n // ab * a
ans += min(n%ab,a)
print(ans)