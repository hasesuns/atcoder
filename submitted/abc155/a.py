a, b, c = map(int, input().split())

abc = [a,b,c]
abc.sort()

if abc[0] == abc[1] and abc[1] != abc[2]:
    print('Yes')
    exit()

if abc[1] == abc[2] and abc[0] != abc[1]:
    print('Yes')
    exit()


print('No')