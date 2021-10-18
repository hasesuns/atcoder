n = int(input())

ans = -( -n // 1.08)

if int(ans * 1.08) == n:
    print(int(ans))
else:
    print(':(')