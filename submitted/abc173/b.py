n = int(input())

count = {'AC':0, 'WA':0,'TLE':0, 'RE':0}

for i in range(n):
    s = input() #sys.stdin.readlineは最後が改行
    count[s]+=1


print('AC x',count['AC'])
print('WA x',count['WA'])
print('TLE x',count['TLE'])
print('RE x',count['RE'])