h, w = map(int, input().split())

if h == 1:
    print(w)
    exit()
if w == 1:
    print(h)
    exit()

ans = (h // 2 + h % 2) * (w // 2 + w % 2)
print(ans)