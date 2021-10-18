n = int(input())
a = list( map(int, input().split()))

a_ = list(set(a))

if len(a) == len(a_):
    print('YES')
else:
    print('NO')