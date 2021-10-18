h,w,a,b = map(int, input().split())


for i in range(h):
    if i<b:
        ansi = [0]*a+[1]*(w-a)
    else:
        ansi = [1]*a+[0]*(w-a)
    print(*ansi,sep='')