n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

ans = 0

r_ = p
s_ = r
p_ = s

for i in range(k):
    if t[i] == 'r':
        ans += r_
    if t[i] == 's':
        ans += s_
    if t[i] == 'p':
        ans += p_

for i in range(k,n):
    if t[i] == t[i-k]:
        t[i] = 'z'
    else:
        if t[i] == 'r':
            ans += r_
        if t[i] == 's':
            ans += s_
        if t[i] == 'p':
            ans += p_

print(ans)