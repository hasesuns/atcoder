s = input()
isOdd = True
for i in range(len(s)):
    if isOdd == False and s[i] == 'R':
        print('No')
        exit()
    if isOdd == True and s[i] == 'L':
        print('No')
        exit()
    isOdd = not isOdd

print('Yes')