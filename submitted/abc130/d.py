n, k = map(int, input().split())
a = list( map(int, input().split())) # a1 a2 ... aN

count=0
right=0
array_sum = 0
for left in range(n):
    # sum = a[left] #毎回初期化してたらしゃくとりの良さ行かせないよな
    while right<n and array_sum + a[right] < k :
        array_sum += a[right]
        # print(left, right, array_sum)
        right+=1

    count += n - right
    array_sum -= a[left]
print(count)