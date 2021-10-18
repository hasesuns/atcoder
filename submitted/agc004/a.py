a,b,c = map(int, input().split())

abc = sorted([a,b,c])

ma = abc[2]

if ma%2==0:
    print(0)
else:
    print(abc[0]*abc[1])
 