h,w= map(int, input().split())
a = input()

ans = 0
for i in range(h-1):
    a = a+ input()

from collections import Counter

c = Counter(a)

cm = c.most_common()


if h*w%2==1:
    cnt_odd = 0
    cnt_2 =0
    limit_2 = h//2 + w//2

    for k,v in cm:
        if v%2==1:
            cnt_odd+=1
            if cnt_odd >1:
                print('No')
                exit()
        elif v%4!=0:
            cnt_2+=1
            if cnt_2 >limit_2:
                print('No')
                exit()
    if cnt_odd == 0:
        print('No')
    else:
        print('Yes')

else:
    cnt_odd = 0
    cnt_2 =0
    if h%2!=0:
        limit_2 = w//2
    elif w%2!=0:
        limit_2 = h//2
    else:
        limit_2 = 0

    for k,v in cm:
        if v%2==1:
            cnt_odd+=1
            if cnt_odd >0:
                print('No')
                exit()
        elif v%4!=0:
            cnt_2+=1
            if cnt_2 >limit_2:
                print('No')
                exit()
    print('Yes')