n = int(input())
h = list( map(int, input().split())) 

invh = h[::-1]
diff = 0

for i in range(n-1):
    if invh[i+1] - invh[i] >= 2:
        print('No')
        exit()
    elif invh[i+1] - invh[i] == 1:
        diff += 1
        if diff > 1:
            print('No')
            exit()
    elif invh[i+1] - invh[i] < 0:
        diff = 0
print('Yes')