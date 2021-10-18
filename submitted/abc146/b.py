n = int(input())
s = input()
s_ = ['a']*len(s)

Zorder = ord('Z')
for i in range(len(s)):
    order = ord(s[i]) + n
    if order > Zorder:
        order -= 26
    s_[i] = chr(order)


print(*s_, sep='')