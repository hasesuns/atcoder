n, m = map(int, input().split())

c = [0]* m
s = [0]* m
for i in range(m):
    s[i], c[i] = map(int, input().split())

flg = True

if n == 1:
    i = 0
    i_str = str(i)
    for j in range(m):
        if i_str[s[j]-1] != str(c[j]):
            flg = False
            continue
    if flg==True:
        print(i)
        exit()
    flg = True

for i in range(10**(n-1),10**n):
    i_str = str(i)
    for j in range(m):
        if i_str[s[j]-1] != str(c[j]):
            flg = False
            continue
    if flg==True:
        print(i)
        exit()
    flg = True

print(-1)