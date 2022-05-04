import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
target = sum(a) / 10
aa = a + a

right=0
array_sum = 0
for left in range(2*n):
    while right<2*n and array_sum + aa[right] <= target :
        array_sum += aa[right]
        right+=1
        if array_sum == target:
            print('Yes')
            exit()
    array_sum -= aa[left]

print("No")