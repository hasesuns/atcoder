n = int(input())
a = list( map(int, input().split()))
p = 10**9+7

len_max = len(list(format(max(a), 'b')))

bin_list = [0]*len_max

for a_ in a:
    for i in range(1,len_max+1):
        if a_ & (1<<(i-1)):
            bin_list[-i] += 1

ans = 0
for i in range(1,len_max+1):
    num_1 = bin_list[-i]%p
    ans += 2**(i-1)%p * num_1 * (n-num_1)%p

print(ans%p)