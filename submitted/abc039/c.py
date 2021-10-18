s = input() #sys.stdin.readlineは最後が改行
piano = 'WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW'

n = piano.find(s)

if n <=1:print('Do')
elif 2<=n<=3:print('Re')
elif n==4:print('Mi')
elif 5<=n<=6:print('Fa')
elif 7<=n<=8:print('So')
elif 9<=n<=10:print('La')
elif n==11:print('Si')