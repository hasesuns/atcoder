n = int(input())
s = input() #sys.stdin.readlineは最後が改行
s=s+s[0]

ans = ['X']*(n+2)

ans[0] = 'S'
ans[1] = 'S'

for zero, one in ['SS','SW','WS','WW']:
    ans[0] = zero
    ans[1] = one
    for i in range(1,n+1):
        if (s[i] == 'o' and ans[i]=='S') or (s[i] == 'x' and ans[i]=='W'):
            ans[i+1] = ans[i-1]
        else:
            ans[i+1] = 'S' if ans[i-1]=='W' else 'W'

    if ans[0:2] == ans[n:]:
        print(*ans[:n],sep='')
        exit()

print(-1)