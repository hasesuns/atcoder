lst = [0]*5
for i in range(5):
    lst[i] = int(input())

k = int(input())

if max(lst) - min(lst) > k:
    print(':(')
else:
    print('Yay!')