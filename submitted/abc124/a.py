a, b = list(map(int, input().split()))
aa = a-1
bb = b-1
lst = sorted([a, b, aa, bb])

print(lst[2]+lst[3])