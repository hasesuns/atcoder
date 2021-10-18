n = int(input())


for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        a = i

b = n//a
ans = a + b -2
print(ans)