n, k, s = map(int, input().split())

if s < 10**9:
    ans = [s]*k + [s+1]*(n-k)
    print(*ans)
    exit()
if s == 10**9:
    if k != 0:
        ans = [s]*k + [1]*(n-k)
        print(*ans)
        exit()
    else:
        ans = [s-1]*n
        print(*ans)
        exit()