n = int(input())

ans = 0

table = [[0]*10 for _ in range(10)]

for number in range(1, n+1):
    i = int(str(number)[0])
    j = int(str(number)[-1])
    table[i][j] += 1

for i in range(1,10):
    for j in range(1, 10):
        ans += table[j][i] * table[i][j]
print(ans)
 