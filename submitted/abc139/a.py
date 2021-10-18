s = input()
t = input()
ans = 0
for _ in range(3):
    if s[_] == t[_]:
        ans += 1

print(ans)