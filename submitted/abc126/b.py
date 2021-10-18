S = input()
YY = int(S[:2])
MM = int(S[2:])

if 0 < MM and MM < 13:
    if 0 < YY and YY < 13:
        print('AMBIGUOUS') 
    else:
        print('YYMM')
elif 0 < YY and YY < 13:
    print('MMYY')
else:
    print('NA')