n,a,b = map(int, input().split())

if b-a==0:
    print('Borys')
    exit()

if (b-a)%2==1:print('Borys')
else:print('Alice')
 