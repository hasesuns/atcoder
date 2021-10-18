s = list(input()) #sys.stdin.readlineは最後が改行

def my_index(l, x, default=-1):
    if x in l:
        return l.index(x)
    else:
        return default

while True:
    cc = my_index(s,'C')
    ff = my_index(s,'F')
    if cc == -1 or ff ==-1:
        print('No')
        exit()
    if cc < ff:
        print('Yes')
        exit()
    else:
        s.pop(ff)