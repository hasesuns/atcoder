n = int(input())
c = list(int(input()) for i in range(n))

ans = 0

for i in range(n):
    n_divisor = len([j for j in c if c[i] % j == 0]) - 1
    for n_right_divisor in range(n_divisor+1):
        if n_right_divisor % 2 ==1:
            continue

        prob = 1 / (n_divisor + 1)
        ans += prob

print(ans)