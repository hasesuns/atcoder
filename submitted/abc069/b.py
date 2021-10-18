h, w = map(int, input().split())
n = int(input())
a = list( map(int, input().split()))

ans = [[-1 for i in range(w)] for j in range(h)]

num_list = []
for i in range(len(a)):
    num_list.extend([i+1]*a[i])

k = 0
for i in range(h):
    if i %2 == 0:
        for j in range(w):
            ans[i][j] = num_list[k]
            k+=1
    else:
        for j in reversed(range(w)):
            ans[i][j] = num_list[k]
            k+=1


for i in range(h):
    print(*ans[i], sep = ' ')