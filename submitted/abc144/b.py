n = int(input())

s = [0]*100
s[0] = 1
for i in range(1,10):
    for j in range(1, 10):
        s[i*10+j] = i*j

if n in s:
    print('Yes')
else:
    print('No')