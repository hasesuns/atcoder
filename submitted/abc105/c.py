n = int(input())

if n == 0:
    print(0)
    exit()


reverse_ans = []
i = 0
base = -2

while n != 0:
    if n % (base**(i+1)) == 0:
        reverse_ans.append(0)
    else:
        reverse_ans.append(1)
        n -= base**i

    i += 1

ans = reverse_ans[::-1]
print(*ans, sep ='')