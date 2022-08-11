import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, x, y, z = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

values = []
for i in range(n):
    values.append((i+1, a[i], b[i]))
values = sorted(values, key=lambda x: (-x[1], x[0]))

ans = values[:x]
values2 = values[x:]
values2 = sorted(values2, key=lambda x: (-x[2], x[0]))

ans.extend(values2[:y])
values3 = values2[y:]
values3 = sorted(values3, key=lambda x: (-x[1]-x[2], x[0]))

ans.extend(values3[:z])
ans = sorted(ans, key=lambda x: x[0])

ans = [x[0] for x in ans]
print(*ans, sep="\n")
 