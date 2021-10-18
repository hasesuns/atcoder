s = input()

ans = 1
temp0 = s[0]
i = 1
while i < len(s):
    temp1 = s[i]
    while temp0 == temp1:
        i += 1
        if i >= len(s):
            ans -= 1
            break
        temp1 = temp1 + s[i]
    ans += 1 
    i += 1  
    temp0 = temp1 

print(ans)