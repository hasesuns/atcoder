s = input()

i = 0
while i < len(s):
    if s[i:i+11] == 'dreameraser':
        i += 11
    elif s[i:i+10] == 'dreamerase':
        i += 10        
    elif s[i:i+7] == 'dreamer':
        i += 7
    elif s[i:i+6] == 'eraser':
        i += 6
    elif s[i:i+5] == 'dream' or s[i:i+5] == 'erase':
        i += 5
    else:
        print('NO')
        exit()

print('YES')