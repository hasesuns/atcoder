import itertools

n = int(input())
ans = 0
for i in range(3,len(str(n))+1):
    for tuple357 in itertools.product([3,5,7], repeat=i):
        if len(set(tuple357)) < 3:
            continue
        number = int(''.join(map(str,tuple357)))
        if number <= n:
            ans += 1

print(ans)