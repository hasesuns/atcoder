n = int(input())
s = input()
passwords = []

firsts = []
firsts_seconds = [[]*10 for _ in range(10)]
firsts_seconds_thirds = [[]*10 for _ in range(100)]

for i in range(n-2):
    if len(firsts) == 10:
        break
    first =  s[i]
    if first in firsts:
        continue
    firsts.append(first)
    for j in range(i+1,n-1):
        if len(firsts_seconds[int(first)]) == 10:
            break
        second = s[j]
        first_second = first + second
        if first_second in firsts_seconds[int(first)]:
            continue
        firsts_seconds[int(first)].append(first_second)
        for k in range(j+1, n):
            password = first_second + s[k]
            if password not in firsts_seconds_thirds[int(first_second)]:
                firsts_seconds_thirds[int(first_second)].append(password)
                passwords.append(password)

print(len(passwords))
 