n =int(input())
s = input()

m = n//2
s1 = s[0:m]
s2 = s[m:]

if n == 1:
    print('No')
    exit()

if s1 == s2:
    print('Yes')
else:
    print('No')