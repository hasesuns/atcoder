h, w, x, y = map(int, input().split())
x -= 1
y -= 1

vertical = []
horizon = []

for i in range(h):
    s = input()
    vertical.append(s[y])
    if i == x:
        horizon = list(s)

ans = -1
for i in range(y, w):
    if horizon[i] == ".":
        ans += 1
    else:
        break

for i in reversed(range(y)):
    if horizon[i] == ".":
        ans += 1
    else:
        break

for i in range(x, h):
    if vertical[i] == ".":
        ans += 1
    else:
        break

for i in reversed(range(x)):
    if vertical[i] == ".":
        ans += 1
    else:
        break

print(ans)
 