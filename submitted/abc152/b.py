a ,b = map(int, input().split())

small = min(a,b)
big = max(a,b)

ans = [str(small)]*big

print(*ans, sep='')