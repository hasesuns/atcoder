s = input() #sys.stdin.readlineは最後が改行
n = len(s)
ans = 0
for i in range(n):
    if i%2==0:
        ans += int(s[i])
    else:
        ans -= int(s[i])

print(ans)